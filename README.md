# Research Scholar Agent Skills

59 agent skills that cover the research lifecycle, from choosing a problem to defending the thesis. Each skill is a folder with a `SKILL.md` that tells an AI agent when to use it, what to ask for, how to do the work, what to deliver, and what to avoid. Sixteen skills also ship a Python script for the parts that should be computed, not written from memory: literature search, citation checks, statistics, power analysis, tables, figures, and PDF checks.

The skills work in Claude Code as a plugin, and in any agent that reads the `SKILL.md` format.

## Install

**Claude Code plugin**

```
/plugin marketplace add Yash-Kavaiya/research-scholar-agent-skills
/plugin install research-scholar@research-scholar-agent-skills
```

On Claude Code 2.1.275 or later this also works in one step:

```
/plugin install research-scholar --marketplace Yash-Kavaiya/research-scholar-agent-skills
```

**Copy the skills you want**

```bash
git clone https://github.com/Yash-Kavaiya/research-scholar-agent-skills
cp -r research-scholar-agent-skills/skills/paper-search ~/.claude/skills/
```

Every skill folder is self-contained, so single skills can be copied on their own.

**Script requirements**

Python 3.10 or later. The literature and citation scripts use only the standard library. The statistics, figure, and PDF scripts need the packages in `requirements.txt`:

```bash
pip install -r requirements.txt
```

No API key is needed. These optional environment variables raise rate limits: `OPENALEX_MAILTO` (your contact email), `S2_API_KEY` (Semantic Scholar), `NCBI_API_KEY` (PubMed).

## Use

Ask for what you need in plain language; each skill's description lists the phrases that trigger it.

- "Find research gaps in federated learning for medical imaging" → `research-gap-finder`
- "Check whether these references are real" → `citation-verifier`
- "How many participants do I need for a two-group comparison with d = 0.5?" → `sample-size-power-calculator`
- "Turn results.csv into a LaTeX table with the best results in bold" → `latex-table-generator`
- "Review my paper like Reviewer 2 before I submit to ACL" → `self-peer-reviewer`
- "Help me with my research" or a goal that spans stages → `research-scholar-orchestrator`

The scripts can also be run directly:

```bash
python skills/paper-search/scripts/search_papers.py "retrieval augmented generation" --limit 5 --format md
python skills/citation-verifier/scripts/verify_citations.py references.bib --tex paper.tex
python skills/sample-size-power-calculator/scripts/power_calc.py ttest-ind --effect 0.5 --power 0.8
python skills/statistical-test-selector/scripts/run_test.py two-groups data.csv --value score --group condition
python skills/latex-table-generator/scripts/csv_to_booktabs.py results.csv --second --arrows
python skills/camera-ready-checker/scripts/check_pdf.py paper.pdf --max-pages 9 --anonymous
```

## Skills

### 1. Finding a problem

| Skill | What it does | Script |
|---|---|---|
| `research-gap-finder` | Scans recent papers on a topic and lists open problems, contradictions, and under-explored areas |  |
| `research-question-formulator` | Turns a vague interest into testable questions and hypotheses (PICO, FINER) |  |
| `novelty-checker` | Checks whether an idea has already been done and finds the closest prior work | yes |
| `topic-trend-analyzer` | Tracks publication volume, rising keywords, and hot subfields over time | yes |

### 2. Literature discovery and reading

| Skill | What it does | Script |
|---|---|---|
| `paper-search` | Unified search across arXiv, Semantic Scholar, OpenAlex, PubMed, and Crossref | yes |
| `citation-graph-explorer` | Forward and backward citation chasing and seminal-paper detection | yes |
| `paper-summarizer` | Structured summary covering problem, method, data, results, limitations |  |
| `paper-critic` | Critical reading for weak assumptions, missing baselines, and threats to validity |  |
| `paper-comparison-matrix` | A table comparing N papers on method, dataset, metrics, and results |  |
| `math-and-equation-explainer` | Step-by-step explanation of derivations and notation |  |

### 3. Literature review

| Skill | What it does | Script |
|---|---|---|
| `systematic-review-prisma` | Full PRISMA workflow with search strings, screening, inclusion criteria, and flow diagram | yes |
| `literature-review-writer` | Thematic synthesis rather than paper-by-paper summaries |  |
| `related-work-writer` | A related-work section positioned against your contribution |  |
| `annotated-bibliography-builder` | Annotated entries with relevance notes |  |

### 4. Research design and methodology

| Skill | What it does | Script |
|---|---|---|
| `methodology-designer` | Picks qualitative, quantitative, or mixed design with justification |  |
| `experiment-planner` | Variables, controls, baselines, ablations, and compute budget |  |
| `sample-size-power-calculator` | Power analysis and sample size justification | yes |
| `survey-questionnaire-designer` | Likert scales, validity checks, and pilot plan |  |
| `dataset-finder` | Locates datasets on Hugging Face, Kaggle, UCI, and Papers with Code | yes |
| `ethics-irb-drafter` | Ethics application, consent forms, and data management plan |  |

### 5. Experiments and analysis

| Skill | What it does | Script |
|---|---|---|
| `paper-to-code-reproducer` | Implements a paper's method from the PDF |  |
| `statistical-test-selector` | Picks the right test, runs it, and reports in APA style | yes |
| `results-interpreter` | Turns raw numbers into findings, with honest caveats |  |
| `ablation-study-designer` | Decides which components to remove and how to report it |  |
| `qualitative-coding-assistant` | Thematic coding of interviews and transcripts |  |
| `experiment-logger` | Lab notebook that tracks runs, configs, and decisions | yes |

### 6. Writing

| Skill | What it does | Script |
|---|---|---|
| `paper-outline-generator` | IMRaD outline adapted to the target venue |  |
| `abstract-writer` | Structured abstract within word limits |  |
| `introduction-writer` | Context, gap, contribution, and outline flow |  |
| `academic-tone-editor` | Fixes clarity, hedging, and concision, and removes AI-sounding prose |  |
| `latex-paper-formatter` | Converts drafts to IEEE, ACM, Springer, NeurIPS, or ACL templates |  |
| `thesis-chapter-writer` | Long-form chapters with consistent cross-chapter terminology |  |
| `limitations-and-future-work-writer` | The section people usually write poorly |  |

### 7. Figures and tables

| Skill | What it does | Script |
|---|---|---|
| `publication-figure-maker` | matplotlib and TikZ plots at journal quality | yes |
| `architecture-diagram-maker` | Model and pipeline diagrams |  |
| `latex-table-generator` | Converts CSV to booktabs tables with best results bolded | yes |

### 8. Citations and integrity

| Skill | What it does | Script |
|---|---|---|
| `citation-verifier` | Confirms every reference exists and supports the claim (catches hallucinated citations) | yes |
| `bibtex-manager` | Cleans, deduplicates, and fixes BibTeX entries | yes |
| `citation-style-converter` | Converts between APA, IEEE, Vancouver, and Harvard |  |
| `plagiarism-and-paraphrase-checker` | Flags text that is too close to its source | yes |
| `reproducibility-checklist` | Fills in NeurIPS or ML reproducibility checklists |  |

### 9. Submission and peer review

| Skill | What it does | Script |
|---|---|---|
| `venue-recommender` | Matches a paper to journals and conferences by scope, impact, and deadline |  |
| `self-peer-reviewer` | Simulates Reviewer 2 before you submit |  |
| `rebuttal-writer` | Point-by-point response to reviewers |  |
| `cover-letter-writer` | Editor cover letter with highlights |  |
| `camera-ready-checker` | Page limits, anonymization, formatting, and metadata | yes |

### 10. Funding and career

| Skill | What it does | Script |
|---|---|---|
| `grant-proposal-writer` | Aims, significance, budget, and timeline (including Indian schemes such as DST, SERB, and UGC) |  |
| `phd-research-proposal-writer` | Admission or synopsis proposal |  |
| `sop-and-research-statement-writer` | Statement of purpose and research statement |  |
| `supervisor-finder` | Finds professors by research fit and drafts a cold email |  |

### 11. Dissemination

| Skill | What it does | Script |
|---|---|---|
| `paper-to-slides` | Conference talk deck |  |
| `paper-to-poster` | Academic poster layout |  |
| `paper-to-blog` | Plain-language blog post or thread |  |
| `paper-to-explainer-video` | Script and animation storyboard |  |
| `viva-defense-prep` | Likely examiner questions and model answers |  |

### 12. Orchestrators

| Skill | What it does | Script |
|---|---|---|
| `research-scholar-orchestrator` | Master skill that routes a request to the right skills in sequence |  |
| `idea-to-paper-pipeline` | Chains topic, gap, review, method, draft, and self-review |  |
| `weekly-paper-digest` | Scheduled digest of new papers in your area | yes |
| `research-progress-tracker` | Milestones, supervisor meeting notes, and next actions |  |

## Principles the skills share

- **No fabrication.** References, quotations, data, results, and facts about venues, funders, and people are retrieved or marked as unknown. They are never invented.
- **Verify citations.** A reference is unverified until it has been checked against a database record, and a real paper cited for something it does not say is still an error.
- **The work is the researcher's.** The skills help plan, analyse, draft, and check. Decisions, data, and responsibility for what is submitted stay with the person whose name is on it.
- **Disclose AI assistance** as your venue, institution, or funder requires.
- **Report honestly.** Limitations, negative results, and anything that could not be checked are stated.
- **Check current facts at the source.** Page limits, deadlines, templates, and funding rules change every year; the skills tell the agent to read the current call instead of relying on memory.

Two skills have limits worth knowing before you rely on them. `plagiarism-and-paraphrase-checker` compares a draft only with the source files you give it; it is not a web or publisher-database check. `citation-verifier` reports a reference as `not_found` when Crossref and OpenAlex have no record, which is a strong warning but not proof, since books, theses, and older work are often not indexed.

## Repository layout

```
.claude-plugin/        plugin and marketplace manifests
skills/<name>/         SKILL.md, plus scripts/ and references/ where needed
shared/scholarly_api.py   canonical API client and BibTeX parser
tools/                 catalog.json, validate_skills.py, sync_shared.py
tests/                 offline tests for every script
```

Skills that call scholarly APIs carry their own copy of the client as `scripts/_scholarly_api.py`. Edit `shared/scholarly_api.py`, then run `python tools/sync_shared.py`.

## Develop

```bash
python tools/validate_skills.py   # structure, frontmatter, cross-references, script references
python -m pytest                  # offline tests; no network needed
```

A skill's `SKILL.md` has frontmatter (`name`, a `description` of at most 200 characters, `version`, and `metadata` with `author` and `tags`; scripted skills also declare `compatibility`, `allowed-tools`, and `permissions`), then these sections in order: Purpose, When to use, Prerequisites, Inputs, Instructions, Available Scripts (scripted skills only), Output format, Examples, Quality bar and pitfalls, Limitations, Troubleshooting, Related skills. The validator enforces this.

## Evaluation

The skills are evaluated with [NVIDIA SkillEvaluator](https://docs.nvidia.com/skills/skillevaluator). Results and the method are in [`evals/skillevaluator/REPORT.md`](evals/skillevaluator/REPORT.md).

```bash
uv tool install --python 3.13 "skillevaluator[all] @ git+https://github.com/NVIDIA/SkillEvaluator.git"
python tools/run_skillevaluator.py                    # static quality score for every skill
python tools/run_skillevaluator.py --command tier1    # full Tier 1 gate (needs a provider key for the LLM rubric)
```

The LLM-backed checks read the provider key from the environment (`NVIDIA_API_KEY`, `OPENAI_API_KEY`, or `ANTHROPIC_API_KEY`). Never commit a key.
