"""Validate the structure of every skill in skills/.

Usage:
    python tools/validate_skills.py            # full check against tools/catalog.json
    python tools/validate_skills.py --partial  # skip the "all catalog skills present" check while building
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
SHARED = ROOT / "shared" / "scholarly_api.py"
SHARED_COPY_NAME = "_scholarly_api.py"

REQUIRED_HEADINGS = [
    "## Purpose",
    "## When to use",
    "## Prerequisites",
    "## Inputs",
    "## Instructions",
    "## Output format",
    "## Examples",
    "## Quality bar and pitfalls",
    "## Limitations",
    "## Troubleshooting",
    "## Related skills",
]
# NVIDIA SkillEvaluator deducts for descriptions over 200 characters; the Agent Skills limit is 1024.
MAX_DESCRIPTION = 200
MAX_LINES = 500
REQUIRED_METADATA = ("author", "tags")
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SCRIPT_REF_RE = re.compile(r"scripts/([A-Za-z0-9_]+\.py)")
BACKTICK_RE = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`")


def load_catalog() -> dict[str, str]:
    data = json.loads((ROOT / "tools" / "catalog.json").read_text(encoding="utf-8"))
    return {name: blurb for skills in data.values() for name, blurb in skills.items()}


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Return (frontmatter, body).

    Top-level `key: value` lines become entries; indented lines under a key with
    no value (such as `metadata:`) are stored as `parent.child`.
    """
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter opening '---'")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("missing frontmatter closing '---'")
    meta: dict[str, str] = {}
    parent = ""
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise ValueError(f"bad frontmatter line: {line!r}")
        if line[0].isspace():
            meta[f"{parent}.{key.strip()}"] = value.strip()
        else:
            parent = key.strip()
            meta[parent] = value.strip().strip('"')
    return meta, text[end + 5 :]


def section(body: str, heading: str) -> str:
    start = body.find(heading)
    if start == -1:
        return ""
    nxt = body.find("\n## ", start + len(heading))
    return body[start : nxt if nxt != -1 else len(body)]


def validate_skill(skill_dir: Path, known: set[str]) -> list[str]:
    errors: list[str] = []
    name = skill_dir.name
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return [f"{name}: SKILL.md missing"]
    text = skill_md.read_text(encoding="utf-8").replace("\r\n", "\n")
    try:
        meta, body = parse_frontmatter(text)
    except ValueError as exc:
        return [f"{name}: {exc}"]

    if meta.get("name") != name:
        errors.append(f"{name}: frontmatter name {meta.get('name')!r} != directory name")
    if not NAME_RE.match(name):
        errors.append(f"{name}: name is not lowercase kebab-case")
    desc = meta.get("description", "")
    if not desc:
        errors.append(f"{name}: description missing")
    if len(desc) > MAX_DESCRIPTION:
        errors.append(f"{name}: description is {len(desc)} chars (max {MAX_DESCRIPTION})")
    if "<" in desc or ">" in desc:
        errors.append(f"{name}: description contains angle brackets")
    if not re.fullmatch(r"\d+\.\d+\.\d+", meta.get("version", "")):
        errors.append(f"{name}: version missing or not major.minor.patch")
    for field in REQUIRED_METADATA:
        if not meta.get(f"metadata.{field}"):
            errors.append(f"{name}: metadata.{field} missing")
    if len(text.splitlines()) > MAX_LINES:
        errors.append(f"{name}: SKILL.md has {len(text.splitlines())} lines (max {MAX_LINES})")
    scripted = (skill_dir / "scripts").is_dir()
    if scripted and "## Available Scripts" not in body:
        errors.append(f"{name}: has scripts but no '## Available Scripts' section")

    # Headings inside fenced code blocks are template text, not sections of the skill.
    outline = re.sub(r"```.*?```", "", body, flags=re.S)
    last = -1
    for heading in REQUIRED_HEADINGS:
        pos = outline.find("\n" + heading + "\n")
        if pos == -1:
            errors.append(f"{name}: missing section {heading!r}")
        elif pos < last:
            errors.append(f"{name}: section {heading!r} is out of order")
        last = max(last, pos)

    related = set(BACKTICK_RE.findall(section(body, "## Related skills")))
    if not related:
        errors.append(f"{name}: Related skills section names no skills")
    for other in sorted(related - known):
        errors.append(f"{name}: related skill `{other}` does not exist")
    if name in related:
        errors.append(f"{name}: lists itself as a related skill")

    referenced = set(SCRIPT_REF_RE.findall(body))
    scripts_dir = skill_dir / "scripts"
    present = {p.name for p in scripts_dir.glob("*.py")} if scripts_dir.is_dir() else set()
    for script in sorted(referenced - present):
        errors.append(f"{name}: SKILL.md references scripts/{script}, which does not exist")
    for script in sorted(present - referenced):
        if not script.startswith("_"):
            errors.append(f"{name}: scripts/{script} is never mentioned in SKILL.md")

    copy = scripts_dir / SHARED_COPY_NAME
    if copy.is_file():
        import sync_shared  # the per-skill client is the shared one trimmed to what the skill's scripts call

        roots = sync_shared.consumers().get(scripts_dir, set())
        expected = sync_shared.trim(SHARED.read_text(encoding="utf-8"), roots) if roots else None
        if expected is None:
            errors.append(f"{name}: carries {SHARED_COPY_NAME} but no script imports it")
        elif copy.read_text(encoding="utf-8") != expected:
            errors.append(f"{name}: {SHARED_COPY_NAME} is out of date (run python tools/sync_shared.py)")
    return errors


def validate(partial: bool = False) -> list[str]:
    catalog = load_catalog()
    expected = set(catalog)
    actual = {p.name for p in SKILLS.iterdir() if p.is_dir()} if SKILLS.is_dir() else set()
    errors: list[str] = []
    for extra in sorted(actual - expected):
        errors.append(f"{extra}: not in tools/catalog.json")
    if not partial:
        for missing in sorted(expected - actual):
            errors.append(f"{missing}: skill directory missing")
    # Related skills are checked against the catalog, so they may name skills not built yet.
    for name in sorted(actual):
        errors.extend(validate_skill(SKILLS / name, expected))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--partial", action="store_true", help="do not require all catalog skills to exist yet")
    args = parser.parse_args()
    errors = validate(partial=args.partial)
    count = len([p for p in SKILLS.iterdir() if p.is_dir()]) if SKILLS.is_dir() else 0
    for err in errors:
        print("ERROR", err)
    print(f"{count} skills checked, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
