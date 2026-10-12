## Run notes

- Evaluated on Windows 11 with SkillEvaluator 0.5.0, SkillSpector, Semgrep 1.180.0, and Gitleaks 8.30.1.
- LLM checks used the `nv_build` provider with judge model `nvidia/nemotron-3-ultra-550b-a55b`.
- The static results (quality score, Tier 1 without LLM, Tier 2 similarity) are deterministic and can be reproduced with the commands at the end.
- The LLM results are not deterministic. Scores for the same skill moved by a few points between runs, and the provider rate-limited the key (HTTP 429) after roughly an hour of continuous use, so the LLM numbers were collected over several runs.

## What changed in the skills because of the evaluation

1. **Frontmatter was invalid YAML in about half the skills.** Descriptions containing `: ` were unquoted. All string values are now quoted, and a test parses every file with a YAML parser.
2. **Descriptions** were rewritten in the third person, cut to 200 characters or fewer, and given a "Not for ..." boundary. Trigger phrases moved into the Examples section.
3. **New sections in every skill**: Purpose, Prerequisites, Examples (five trigger requests, three non-trigger requests with the skill to use instead, and a worked example), Limitations, and Troubleshooting. Workflow was renamed Instructions.
4. **Metadata**: `version`, `metadata.author`, `metadata.tags`; scripted skills also declare `compatibility`, `allowed-tools`, and `permissions`.
5. **Scripted skills** gained an Available Scripts table, shebang lines, an HTTPS-only check before any request, and a refusal to parse XML that declares a DTD or entities.
6. **Least privilege**: each skill's API client is now generated from `shared/scholarly_api.py` and trimmed to the functions that skill calls. `bibtex-manager` can reach only Crossref and `topic-trend-analyzer` only OpenAlex, where before every network skill carried the client for all five APIs. This removed the high-severity "excessive agency" findings and cut medium findings in the static gate from 58 to 21.
7. **Disclosure**: the eight network skills now tell the user what is sent to public APIs, and `novelty-checker` asks before searching for an unpublished idea.
8. **No bytecode in skill folders**: scripts set `sys.dont_write_bytecode`, so running them no longer leaves `__pycache__` inside a skill.

## Findings that remain, and why

- **External Transmission (medium, 7 skills).** These scripts query scholarly APIs; that is their function. Each endpoint is listed in the skill's `compatibility` field and Prerequisites.
- **subprocess call (medium, `experiment-logger`).** The script runs `git` with fixed arguments and no shell to record the commit of a run.
- **Tainted flow (medium, `weekly-paper-digest`).** The script reads its own state file of already-reported papers and writes it back.
- **Excessive Permissions (low, 4 skills).** A heuristic notice on skills that declare `network`, `env`, and `file_write`. Each permission corresponds to code in the skill.
- **Magic numbers (low, advisory lint).** Numeric constants such as HTTP status codes and default limits.
- **Description-behaviour mismatch (high, LLM pass only).** Raised on a few skills in some runs and not in others. The judge compared the skill description with one chunk of code or with an example snippet. `citation-style-converter` was flagged although it contains no code. Treat these as needing a human look, not as confirmed defects.
- **Stale LLM rows.** `topic-trend-analyzer`, `paper-search`, and `weekly-paper-digest` were last scanned by the LLM security pass before their API clients were trimmed. The "excessive agency" findings listed for `topic-trend-analyzer` describe the old five-API client, which that skill no longer carries. Their static results are current.
- **Incomplete LLM scans.** `skillspector-llm` means the LLM security pass timed out after 300 seconds; `llm-verification` means the verifier returned verdicts for only some findings. SkillEvaluator counts either as an incomplete gate even when no finding fails. None of these skills has a failing static check.

## Not done

- **Tier 3 live evaluation was not run.** It needs Docker and the Harbor CLI, and neither is installed on this machine. The eval datasets are in place (`skills/<name>/evals/evals.json`, three cases per skill) and pass `skillevaluator tier3 validate`. They are built from each skill's Examples section by `tools/build_eval_datasets.py`. SkillEvaluator's own dataset generator was tried first; it fell back to template prompts for many skills, so its output was not used.
- **Tier 2 intra-skill redundancy check** (`context-optimization-check`) was not run. The inter-skill similarity check was run: 59 skills indexed, no duplicates at the 0.75 threshold.
- **The skills have not been tested with a live agent.** The scores say the documentation is well formed and that an LLM judge finds it clear. They do not show that an agent using a skill does better than one without it. Tier 3 is the check for that.

## Decisions for the maintainer

- **Licence.** The repository has no LICENSE file and the skills declare no `license`. The licence check passed with nothing to evaluate. Choose one before publishing.
- **Author email.** `metadata.author` uses the `Name <email>` form SkillEvaluator asks for, with the address already public in the git history. Replace it with a no-reply address if preferred.
- **`permissions` field.** It satisfies SkillSpector's least-privilege check but is not part of the Agent Skills specification. Claude Code ignores unknown frontmatter fields.
- **Description length.** The 200-character cap is SkillEvaluator's scoring rule; the Agent Skills limit is 1024. Shorter descriptions carry fewer trigger phrases. If routing in Claude Code turns out to miss requests, lengthen the descriptions and accept a 1.25-point deduction per skill.

## Reproduce

```bash
uv tool install --python 3.13 "skillevaluator[all] @ git+https://github.com/NVIDIA/SkillEvaluator.git"
uv tool install "git+https://github.com/NVIDIA/SkillSpector.git"
uv tool install semgrep            # plus Gitleaks from your package manager

python tools/run_skillevaluator.py                                             # static quality score
python tools/run_skillevaluator.py --command tier1 --out evals/skillevaluator/static -- --no-llm
skillevaluator similarity-check skills -r json -o evals/skillevaluator/tier2/reports

export NVIDIA_API_KEY=...          # or OPENAI_API_KEY / ANTHROPIC_API_KEY; never commit it
python tools/run_skillevaluator.py --command tier1 --jobs 2                    # LLM security and rubric
python tools/run_skillevaluator.py --command tier1 --resume                    # rerun skills that did not pass
python tools/build_eval_report.py                                              # rebuild REPORT.md

skillevaluator tier3 evaluate skills/<name>                                    # needs Docker and Harbor
```
