# SkillEvaluator review

Evaluated with NVIDIA SkillEvaluator 0.5.0 (https://docs.nvidia.com/skills/skillevaluator) on 12 October 2026.
LLM-backed checks used `nvidia/nemotron-3-ultra-550b-a55b` through the `nv_build` provider.

## Results

| Check | Result |
|---|---|
| Tier 1 deterministic gate (`tier1 --no-llm`): schema, version, security, PII, licence, code risk, secrets, integrity, dependencies, unicode, quality, script lint | 59 of 59 skills pass; 0 critical, 0 high findings |
| Static quality score | 100.0 for every skill (baseline before the rewrite: mean 82.2, min 75) |
| Tier 1 LLM rubric judge | 35 of 59 skills judged, all pass; mean 94.2, min 86.4, max 99.5. The other 24 were not judged: the endpoint returned HTTP 429 (rate limit) |
| Tier 2 inter-skill similarity | Pass: 59 skills indexed, no duplicates at threshold 0.75 |
| Tier 3 live agent evaluation | Not run. Needs Docker or WSL2; native Windows local mode is unsupported by the tool |

## Not done

- Rubric scores for the 24 unjudged skills. Rerun when the rate limit clears: `python tools/run_skillevaluator.py --command rubric-eval --resume`.
- The combined `tier1` run with the LLM security pass. It reported most skills as incomplete because the LLM calls timed out or were rate-limited, and it produced LLM findings (description-behaviour mismatch on a few scripted skills) that looked at one code chunk at a time. `evals/skillevaluator/tier1/` holds that partial run and should not be read as a result.
- Tier 3 datasets: generated for `citation-verifier` only (`skills/citation-verifier/evals/evals.json`). Generate the rest with `skillevaluator create-eval-dataset skills/<name> --full`.

## Remaining findings in the deterministic gate (none blocking)

- Medium `External Transmission (E1)`: the scholarly API client calls Crossref, OpenAlex, Semantic Scholar, arXiv and PubMed. This is the purpose of those scripts.
- Medium `subprocess module call (AST4)`: `experiment-logger` runs `git` to record the commit.
- Low: magic numbers in scripts, and the declared `permissions` list.

## Per-skill scores

| Skill | Deterministic gate | Quality | Rubric (0-100) |
|---|---|---|---|
| ablation-study-designer | pass | 100.0 | 95.9 |
| abstract-writer | pass | 100.0 | 97.7 |
| academic-tone-editor | pass | 100.0 | 98.2 |
| annotated-bibliography-builder | pass | 100.0 | 98.6 |
| architecture-diagram-maker | pass | 100.0 | 95.0 |
| bibtex-manager | pass | 100.0 | 95.9 |
| camera-ready-checker | pass | 100.0 | 92.3 |
| citation-graph-explorer | pass | 100.0 | 92.3 |
| citation-style-converter | pass | 100.0 | 98.6 |
| citation-verifier | pass | 100.0 | 92.3 |
| cover-letter-writer | pass | 100.0 | 90.0 |
| dataset-finder | pass | 100.0 | 97.3 |
| ethics-irb-drafter | pass | 100.0 | 96.4 |
| experiment-logger | pass | 100.0 | 93.6 |
| experiment-planner | pass | 100.0 | 90.0 |
| grant-proposal-writer | pass | 100.0 | 89.1 |
| idea-to-paper-pipeline | pass | 100.0 | 92.3 |
| introduction-writer | pass | 100.0 | 92.3 |
| latex-paper-formatter | pass | 100.0 | 95.0 |
| latex-table-generator | pass | 100.0 | 99.5 |
| limitations-and-future-work-writer | pass | 100.0 | 93.6 |
| literature-review-writer | pass | 100.0 | 97.7 |
| math-and-equation-explainer | pass | 100.0 | 97.7 |
| methodology-designer | pass | 100.0 | 94.5 |
| novelty-checker | pass | 100.0 | 92.3 |
| paper-comparison-matrix | pass | 100.0 | not judged (429) |
| paper-critic | pass | 100.0 | 90.5 |
| paper-outline-generator | pass | 100.0 | 98.6 |
| paper-search | pass | 100.0 | 86.4 |
| paper-summarizer | pass | 100.0 | 92.7 |
| paper-to-blog | pass | 100.0 | 92.7 |
| paper-to-code-reproducer | pass | 100.0 | 99.1 |
| paper-to-explainer-video | pass | 100.0 | 92.7 |
| paper-to-poster | pass | 100.0 | 92.3 |
| paper-to-slides | pass | 100.0 | not judged (429) |
| phd-research-proposal-writer | pass | 100.0 | not judged (429) |
| plagiarism-and-paraphrase-checker | pass | 100.0 | 90.0 |
| publication-figure-maker | pass | 100.0 | 93.6 |
| qualitative-coding-assistant | pass | 100.0 | not judged (429) |
| rebuttal-writer | pass | 100.0 | not judged (429) |
| related-work-writer | pass | 100.0 | not judged (429) |
| reproducibility-checklist | pass | 100.0 | not judged (429) |
| research-gap-finder | pass | 100.0 | not judged (429) |
| research-progress-tracker | pass | 100.0 | not judged (429) |
| research-question-formulator | pass | 100.0 | not judged (429) |
| research-scholar-orchestrator | pass | 100.0 | not judged (429) |
| results-interpreter | pass | 100.0 | not judged (429) |
| sample-size-power-calculator | pass | 100.0 | not judged (429) |
| self-peer-reviewer | pass | 100.0 | not judged (429) |
| sop-and-research-statement-writer | pass | 100.0 | not judged (429) |
| statistical-test-selector | pass | 100.0 | not judged (429) |
| supervisor-finder | pass | 100.0 | not judged (429) |
| survey-questionnaire-designer | pass | 100.0 | not judged (429) |
| systematic-review-prisma | pass | 100.0 | not judged (429) |
| thesis-chapter-writer | pass | 100.0 | not judged (429) |
| topic-trend-analyzer | pass | 100.0 | not judged (429) |
| venue-recommender | pass | 100.0 | not judged (429) |
| viva-defense-prep | pass | 100.0 | not judged (429) |
| weekly-paper-digest | pass | 100.0 | not judged (429) |
