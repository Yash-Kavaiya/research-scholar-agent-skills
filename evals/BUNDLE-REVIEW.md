# Bundle review: SkillEvaluator results after adding reference guides and templates

Date: 14 October 2026. Tool: NVIDIA SkillEvaluator 0.5.0. LLM judge: `nvidia/nemotron-3-ultra-550b-a55b` (nv_build).

## What changed

Every skill is now a bundle: `SKILL.md`, a reference guide in `references/`, a fill-in template in `assets/`, and `evals/evals.json`. 119 new guide and template files, about 61,426 words. Each is listed in a Reference files section of its `SKILL.md`, and `tools/validate_skills.py` now fails a skill that lacks either kind or leaves one unlisted.

## Results

| Check | Result |
|---|---|
| Tier 1 deterministic gate (schema, security, PII, licence, code risk, secrets, integrity, dependencies, unicode, quality, lint), no LLM | 59 of 59 pass; 0 critical, 0 high |
| Static quality score | 100 for every skill |
| LLM rubric judge | 59 of 59 pass; mean 93.9, min 87.7, max 100.0 |
| LaTeX snippets in the guides (pgfplots, booktabs, siunitx, threeparttable, TikZ) | Compiled with pdflatex and rendered; one missing package note (amssymb) fixed |
| Tier 3 live agent runs | Not run: needs Docker or WSL2 on this machine |

## Rubric criteria (mean, min, out of 10)

| Criterion | Mean | Min |
|---|---|---|
| description_clarity | 9.3 | 9 |
| instruction_clarity | 9.4 | 9 |
| example_quality | 9.2 | 8 |
| documentation_completeness | 9.8 | 9 |
| scope_definition | 9.3 | 9 |
| professional_tone | 9.1 | 9 |
| trigger_simulation | 9.6 | 9 |
| workflow_completeness | 9.6 | 9 |
| error_handling_quality | 8.8 | 8 |

## Lowest-scoring skills

| Skill | Rubric | Criteria below 9 |
|---|---|---|
| cover-letter-writer | 87.7 | example_quality 8, error_handling_quality 8 |
| ethics-irb-drafter | 87.7 | example_quality 8, error_handling_quality 8 |
| results-interpreter | 87.7 | example_quality 8, error_handling_quality 8 |
| grant-proposal-writer | 90.0 | none |
| idea-to-paper-pipeline | 90.0 | none |
| literature-review-writer | 90.0 | error_handling_quality 8 |

## Fixes made during review

- CONSORT and SPIRIT references updated to the 2025 versions.
- Unsourced effect-size thresholds for epsilon squared replaced with a stated rough guide.
- A CSL file name corrected (chicago-notes-bibliography.csl); all CSL names in the guides were checked against the CSL repository.
- Sample sizes quoted in the power-analysis guide checked against the bundled script.
- Two phrases that the security scanner read as anti-refusal instructions reworded without changing meaning.

## Per-skill results

| Skill | Gate | Quality | Rubric |
|---|---|---|---|
| ablation-study-designer | pass | 100.0 | 96.4 |
| abstract-writer | pass | 100.0 | 93.6 |
| academic-tone-editor | pass | 100.0 | 92.7 |
| annotated-bibliography-builder | pass | 100.0 | 91.4 |
| architecture-diagram-maker | pass | 100.0 | 92.3 |
| bibtex-manager | pass | 100.0 | 95.0 |
| camera-ready-checker | pass | 100.0 | 90.9 |
| citation-graph-explorer | pass | 100.0 | 93.6 |
| citation-style-converter | pass | 100.0 | 93.6 |
| citation-verifier | pass | 100.0 | 97.7 |
| cover-letter-writer | pass | 100.0 | 87.7 |
| dataset-finder | pass | 100.0 | 93.6 |
| ethics-irb-drafter | pass | 100.0 | 87.7 |
| experiment-logger | pass | 100.0 | 93.6 |
| experiment-planner | pass | 100.0 | 98.6 |
| grant-proposal-writer | pass | 100.0 | 90.0 |
| idea-to-paper-pipeline | pass | 100.0 | 90.0 |
| introduction-writer | pass | 100.0 | 95.0 |
| latex-paper-formatter | pass | 100.0 | 92.3 |
| latex-table-generator | pass | 100.0 | 93.6 |
| limitations-and-future-work-writer | pass | 100.0 | 93.6 |
| literature-review-writer | pass | 100.0 | 90.0 |
| math-and-equation-explainer | pass | 100.0 | 98.6 |
| methodology-designer | pass | 100.0 | 90.0 |
| novelty-checker | pass | 100.0 | 91.4 |
| paper-comparison-matrix | pass | 100.0 | 99.1 |
| paper-critic | pass | 100.0 | 98.6 |
| paper-outline-generator | pass | 100.0 | 92.3 |
| paper-search | pass | 100.0 | 98.6 |
| paper-summarizer | pass | 100.0 | 95.0 |
| paper-to-blog | pass | 100.0 | 99.1 |
| paper-to-code-reproducer | pass | 100.0 | 93.6 |
| paper-to-explainer-video | pass | 100.0 | 96.4 |
| paper-to-poster | pass | 100.0 | 90.0 |
| paper-to-slides | pass | 100.0 | 95.0 |
| phd-research-proposal-writer | pass | 100.0 | 95.9 |
| plagiarism-and-paraphrase-checker | pass | 100.0 | 92.3 |
| publication-figure-maker | pass | 100.0 | 92.7 |
| qualitative-coding-assistant | pass | 100.0 | 98.6 |
| rebuttal-writer | pass | 100.0 | 91.4 |
| related-work-writer | pass | 100.0 | 90.0 |
| reproducibility-checklist | pass | 100.0 | 93.6 |
| research-gap-finder | pass | 100.0 | 93.6 |
| research-progress-tracker | pass | 100.0 | 91.4 |
| research-question-formulator | pass | 100.0 | 90.5 |
| research-scholar-orchestrator | pass | 100.0 | 93.6 |
| results-interpreter | pass | 100.0 | 87.7 |
| sample-size-power-calculator | pass | 100.0 | 94.5 |
| self-peer-reviewer | pass | 100.0 | 99.1 |
| sop-and-research-statement-writer | pass | 100.0 | 90.0 |
| statistical-test-selector | pass | 100.0 | 100.0 |
| supervisor-finder | pass | 100.0 | 100.0 |
| survey-questionnaire-designer | pass | 100.0 | 93.6 |
| systematic-review-prisma | pass | 100.0 | 93.6 |
| thesis-chapter-writer | pass | 100.0 | 98.6 |
| topic-trend-analyzer | pass | 100.0 | 91.4 |
| venue-recommender | pass | 100.0 | 98.6 |
| viva-defense-prep | pass | 100.0 | 93.6 |
| weekly-paper-digest | pass | 100.0 | 92.3 |
