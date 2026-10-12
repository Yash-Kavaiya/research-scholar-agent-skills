"""Run NVIDIA SkillEvaluator checks on every skill and summarise the results.

Needs the `skillevaluator` CLI (https://docs.nvidia.com/skills/skillevaluator):
    uv tool install --python 3.13 "skillevaluator[all] @ git+https://github.com/NVIDIA/SkillEvaluator.git"

Usage:
    python tools/run_skillevaluator.py                       # quality-check on all skills (no key needed)
    python tools/run_skillevaluator.py --command tier1 --jobs 3   # full Tier 1 gate, LLM rubric included
    python tools/run_skillevaluator.py --skills paper-search bibtex-manager
    python tools/run_skillevaluator.py --command tier1 -- --no-llm
    python tools/run_skillevaluator.py --command tier1 --resume   # rerun only skills that did not pass

The LLM-backed checks read the provider key from the environment (for example NVIDIA_API_KEY).
Writes summary.json and summary.md under evals/skillevaluator/<command>/; raw per-skill reports
go to a reports/ folder there, which is not committed because it contains local paths.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run_one(command: str, skill_dir: Path, out_dir: Path, extra: list[str]) -> dict:
    report_dir = out_dir / "reports" / skill_dir.name
    report_dir.mkdir(parents=True, exist_ok=True)
    for old in report_dir.glob("*.json"):
        old.unlink()
    base = {k: v for k, v in os.environ.items() if k not in ("PYTHONUTF8", "PYTHONIOENCODING")}
    # On Windows, SkillEvaluator 0.5.0 can crash decoding SkillSpector's output in one console
    # encoding mode and not the other, so a run that leaves no report is retried in UTF-8 mode.
    for mode in ({}, {"PYTHONUTF8": "1", "PYTHONIOENCODING": "utf-8"}):
        proc = subprocess.run(
            ["skillevaluator", *command.split(), str(skill_dir), "-r", "json", "-o", str(report_dir), *extra],
            capture_output=True, text=True, encoding="utf-8", errors="replace", env={**base, "NO_COLOR": "1", **mode})
        if any(report_dir.glob("*.json")):
            break
    return row_from_report(skill_dir.name, report_dir, proc.returncode)


def row_from_report(skill: str, report_dir: Path, exit_code: int | None = None) -> dict:
    """Build a summary row from the newest JSON report in a skill's report folder."""
    reports = sorted(report_dir.glob("*.json"), key=lambda p: p.stat().st_mtime)
    data = json.loads(reports[-1].read_text(encoding="utf-8")) if reports else {}
    row = {"skill": skill, "exit_code": exit_code, "passed": data.get("overall_passed"),
           "status": data.get("overall_status") or "no report", "incomplete_scans": data.get("incomplete_scans", []),
           "severity": data.get("severity_counts", {}), "quality_score": None, "quality_grade": None,
           "rubric_score": None, "rubric_criteria": {}, "validators": {}, "findings": []}
    for result in data.get("results", []):
        name = result.get("validator", "")
        row["validators"][name] = result.get("status")
        quality = result.get("quality") or {}
        if name == "QUALITY" and quality:
            row["quality_score"], row["quality_grade"] = quality.get("overall_score"), quality.get("grade")
        rubric = result.get("rubric_eval") or {}
        if name == "RUBRIC_EVAL" and rubric.get("execution_status") == "succeeded":
            row["rubric_score"] = rubric.get("overall_score")
            row["rubric_criteria"] = {c["id"]: c["score"] for c in rubric.get("checks", [])}
            row["rubric_summary"] = rubric.get("summary", "")
        for finding in result.get("findings", []):
            if name == "RUBRIC_EVAL" and finding.get("check_name", "").startswith("rubric_") \
                    and finding.get("check_name") != "rubric_overall":
                continue  # per-criterion scores are kept in rubric_criteria
            path = (finding.get("file_path") or "").replace("\\", "/")
            row["findings"].append({"validator": name, "severity": finding.get("severity"),
                                    "check": finding.get("check_name"), "message": finding.get("message"),
                                    "file": path.split("/skills/")[-1] if "/skills/" in path else path.split("/")[-1],
                                    "line": finding.get("line_number")})
    return row


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def summarise(rows: list[dict], command: str) -> str:
    lines = [f"# SkillEvaluator `{command}` summary", "",
             f"Skills: {len(rows)}. Status: " + ", ".join(f"{n} {s}" for s, n in Counter(r["status"] for r in rows).most_common()) + "."]
    quality = [r["quality_score"] for r in rows if r["quality_score"] is not None]
    rubric = [r["rubric_score"] for r in rows if r["rubric_score"] is not None]
    if quality:
        lines.append(f"Static quality score: mean {mean(quality):.1f}, min {min(quality):.1f}, max {max(quality):.1f}.")
    if rubric:
        lines.append(f"LLM rubric score ({len(rubric)} skills judged): mean {mean(rubric):.1f}, "
                     f"min {min(rubric):.1f}, max {max(rubric):.1f}.")
    totals = Counter()
    for r in rows:
        totals.update({k: v for k, v in r["severity"].items() if v})
    lines.append("Findings by severity: " + (", ".join(f"{totals[s]} {s}" for s in ("critical", "high", "medium", "low")
                                                         if totals[s]) or "none") + ".")
    lines += ["", "| Skill | Status | Quality | Rubric | Critical | High | Medium | Low | Incomplete scans |",
              "|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: r["skill"]):
        sev = r["severity"]
        lines.append(f"| {r['skill']} | {r['status']} | {r['quality_score'] if r['quality_score'] is not None else 'n/a'} | "
                     f"{r['rubric_score'] if r['rubric_score'] is not None else 'n/a'} | {sev.get('critical', 0)} | "
                     f"{sev.get('high', 0)} | {sev.get('medium', 0)} | {sev.get('low', 0)} | "
                     f"{', '.join(map(str, r['incomplete_scans']))} |")
    validators = Counter()
    for r in rows:
        validators.update(f"{name}: {status}" for name, status in r["validators"].items())
    if validators:
        lines += ["", "## Validator outcomes", "", "| Skills | Validator: status |", "|---|---|"]
        lines += [f"| {count} | {key} |" for key, count in sorted(validators.items())]
    criteria: dict[str, list[float]] = {}
    for r in rows:
        for cid, score in r["rubric_criteria"].items():
            criteria.setdefault(cid, []).append(score)
    if criteria:
        lines += ["", "## LLM rubric criteria (0 to 10; 7 is the pass mark)", "", "| Criterion | Mean | Min | Skills below 7 |", "|---|---|---|---|"]
        lines += [f"| {cid} | {mean(v):.1f} | {min(v)} | {sum(1 for s in v if s < 7)} |" for cid, v in criteria.items()]
    messages = Counter()
    for r in rows:
        for key in {f"[{f['severity']}] {f['validator']} / {f['check']}: {re.sub(r'\\d+', 'N', str(f['message']))[:150]}"
                    for f in r["findings"]}:
            messages[key] += 1
    lines += ["", "## Findings by frequency", "", "| Skills affected | Finding |", "|---|---|"]
    lines += [f"| {count} | {message} |" for message, count in messages.most_common()] or ["| 0 | none |"]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--command", default="quality-check", help="skillevaluator subcommand, e.g. quality-check, tier1")
    parser.add_argument("--skills", nargs="*", help="skill names (default: all)")
    parser.add_argument("--out", default="evals/skillevaluator", help="output directory")
    parser.add_argument("--jobs", type=int, default=1, help="skills evaluated in parallel")
    parser.add_argument("--resume", action="store_true",
                        help="keep skills that passed in the existing summary and rerun the rest (LLM checks can time out)")
    parser.add_argument("--from-reports", action="store_true",
                        help="rebuild the summary from existing report files without running the evaluator")
    parser.add_argument("extra", nargs="*", help="extra arguments passed to skillevaluator after --")
    args = parser.parse_args()

    out_dir = ROOT / args.out / args.command.replace(" ", "-")
    names = args.skills or sorted(p.name for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").is_file())
    kept: list[dict] = []
    previous_rows: list[dict] = []
    if args.resume and (out_dir / "summary.json").exists():
        # Keep earlier passes; rerun everything else, plus any skills named with --skills.
        previous = json.loads((out_dir / "summary.json").read_text(encoding="utf-8"))
        previous_rows = previous
        forced = set(args.skills or [])
        kept = [row for row in previous if row.get("passed") and row["skill"] not in forced]
        done = {row["skill"] for row in kept}
        names = sorted(p.name for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").is_file() and p.name not in done)

    def work(name: str) -> dict:
        row = run_one(args.command, ROOT / "skills" / name, out_dir, args.extra)
        print(f"{name:42} {row['status']:10} quality={row['quality_score']} rubric={row['rubric_score']} "
              f"findings={len(row['findings'])}", flush=True)
        return row

    def write(rows: list[dict]) -> None:
        rows = sorted(rows, key=lambda row: row["skill"])
        (out_dir / "summary.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
        (out_dir / "summary.md").write_text(summarise(rows, args.command), encoding="utf-8")

    if args.from_reports:
        # Rebuild the summary from report files already on disk, without running anything.
        rows = [row_from_report(p.name, out_dir / "reports" / p.name)
                for p in sorted((ROOT / "skills").iterdir()) if (out_dir / "reports" / p.name).is_dir()]
        write(rows)
        print(f"rebuilt {out_dir / 'summary.md'} from {len(rows)} report folders")
        return 0 if all(r["passed"] for r in rows) else 1

    rows = list(kept)
    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        for row in pool.map(work, names):
            rows.append(row)
            if args.resume:
                # Save after every skill so an interrupted run can be resumed. Without --resume the
                # previous summary is left in place until the run completes.
                by_name = {r["skill"]: r for r in previous_rows}
                by_name.update({r["skill"]: r for r in rows})
                write(list(by_name.values()))
    write(rows)
    print(f"\nwrote {out_dir / 'summary.md'}")
    return 0 if all(r["passed"] for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
