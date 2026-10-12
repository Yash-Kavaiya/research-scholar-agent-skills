---
name: research-scholar-orchestrator
description: Routes any research or academic request to the right research-scholar skill or sequence of skills, covering topic selection, literature search and review, study design, analysis, writing, figures, citations, submission, funding, and dissemination. Use when a research request spans several stages, when it is unclear which skill applies, or when the user says "help me with my research", "I am starting a PhD or thesis", "what should I do next on my paper", "take this project from A to B", or names a goal such as "get this paper ready to submit".
---

# Research Scholar Orchestrator

Work out where the user is in the research lifecycle, pick the smallest set of skills that gets them to their stated goal, and run them in an order where each one's output feeds the next.

## When to use

- The request needs more than one skill, or the right skill is not obvious.
- The user describes a goal, not a task.
- A long project needs a plan across stages.

Go straight to a single skill when the request names one task that one skill covers. Use `idea-to-paper-pipeline` when the user wants the whole path from topic to reviewed draft.

## Inputs

- The goal, in the user's words, and the deadline if there is one.
- The field and the type of output (paper, thesis, proposal, review, talk).
- What already exists: topic, papers collected, data, results, draft, reviews.
- Constraints: venue, word limits, institutional rules, tools available.

Ask at most two or three questions, only for what cannot be inferred. State the assumption and proceed for everything else.

## Workflow

1. **Locate the stage.** Identify the furthest point the user has reached: no topic; topic but no question; question but no design; data but no analysis; results but no draft; draft but not submission-ready; under review; accepted; or applying for a position or funding.
2. **Match the request to skills** with the routing table.

   | The user wants to | Skills, in order |
   |---|---|
   | Find a topic or problem | `topic-trend-analyzer` → `research-gap-finder` → `novelty-checker` → `research-question-formulator` |
   | Check an idea is new | `novelty-checker` (uses `paper-search`, `citation-graph-explorer`) |
   | Find and read papers | `paper-search` → `citation-graph-explorer` → `paper-summarizer` |
   | Understand or judge one paper | `paper-summarizer` → `math-and-equation-explainer` → `paper-critic` |
   | Compare several papers | `paper-comparison-matrix` |
   | Write a literature review | `paper-search` → `paper-comparison-matrix` → `literature-review-writer` → `citation-verifier` |
   | Do a systematic review | `research-question-formulator` → `systematic-review-prisma` → `literature-review-writer` |
   | Write related work | `novelty-checker` → `related-work-writer` |
   | Build a reading list with notes | `paper-search` → `annotated-bibliography-builder` |
   | Design a study | `research-question-formulator` → `methodology-designer` → `sample-size-power-calculator` → `survey-questionnaire-designer` → `ethics-irb-drafter` |
   | Plan computational experiments | `dataset-finder` → `experiment-planner` → `ablation-study-designer` → `experiment-logger` |
   | Reproduce a paper | `paper-summarizer` → `paper-to-code-reproducer` → `experiment-logger` |
   | Analyse quantitative data | `statistical-test-selector` → `results-interpreter` |
   | Analyse interviews or text | `qualitative-coding-assistant` → `results-interpreter` |
   | Write a paper from results | `results-interpreter` → `paper-outline-generator` → `publication-figure-maker` / `architecture-diagram-maker` / `latex-table-generator` → `introduction-writer` → `related-work-writer` → `limitations-and-future-work-writer` → `abstract-writer` → `academic-tone-editor` |
   | Write a thesis | `thesis-chapter-writer`, with `literature-review-writer` and `methodology-designer` for those chapters |
   | Fix references | `bibtex-manager` → `citation-verifier` → `citation-style-converter` |
   | Check originality of wording | `plagiarism-and-paraphrase-checker` |
   | Get a paper submission-ready | `self-peer-reviewer` → `citation-verifier` → `reproducibility-checklist` → `latex-paper-formatter` → `camera-ready-checker` |
   | Choose where to submit | `venue-recommender` → `cover-letter-writer` |
   | Respond to reviews | `rebuttal-writer`, then `camera-ready-checker` after acceptance |
   | Apply for funding | `grant-proposal-writer` |
   | Apply for a PhD or position | `supervisor-finder` → `phd-research-proposal-writer` → `sop-and-research-statement-writer` |
   | Present or publicise work | `paper-to-slides`, `paper-to-poster`, `paper-to-blog`, `paper-to-explainer-video` |
   | Prepare for a defence | `viva-defense-prep` |
   | Keep up with the field | `weekly-paper-digest` |
   | Track a long project | `research-progress-tracker` |
   | Go from idea to draft in one run | `idea-to-paper-pipeline` |

3. **Trim the sequence** to what the goal needs. Skip any step whose output the user already has, after checking that it is adequate.
4. **Present the plan** in a few lines: the steps, what each produces, and where the user's decision is needed. Then start; do not wait for approval of an obvious plan.
5. **Run each skill fully**, following its own instructions, and pass its output to the next. Keep working files in one project folder so later steps can read them.
6. **Stop at decision points** that belong to the user: choice of topic, research question, design, venue, and anything that would be submitted in their name.
7. **Apply the integrity rules at every step** (below), and run `citation-verifier` before any document with references is treated as finished.
8. **Close with status**: what was produced, what remains, and the next step, recorded with `research-progress-tracker` for multi-session projects.

## Output format

```markdown
## Plan for: <goal>
Stage: <where you are now>. Deadline: <date or none>.

| Step | Skill | Produces | Needs from you |
|---|---|---|---|
| 1 | paper-search | corpus of ~30 papers | topic confirmation |
| 2 | ... | ... | ... |

(work proceeds, one section per step)

## Status
- Done: ...
- Open decisions: ...
- Next: ...
```

## Quality bar and pitfalls

These rules hold across every skill in the collection:

- **No fabrication.** Never invent references, quotations, data, results, statistics, reviewer comments, approvals, or facts about venues, people, or funders. Retrieve them or mark them as unknown.
- **Verify citations.** Any reference that did not come from a retrieved record is unverified until `citation-verifier` has checked it.
- **The work is the researcher's.** The skills help plan, analyse, draft, and check. Research decisions, the data, and responsibility for what is submitted remain with the user, who should read and understand everything that goes out under their name.
- **Disclose AI assistance** as the venue, institution, or funder requires. When the user is unsure of the policy, tell them to check it.
- **Report honestly.** State limitations, negative results, failed checks, and anything that could not be verified.
- **Protect confidential material**: unpublished manuscripts, participant data, and papers under review.

Routing pitfalls:

- Do not run a long chain when one skill answers the question.
- Do not skip the design and analysis skills to reach the writing skills; a paper written on weak results needs the results fixed, not better prose.
- Do not continue past a failed step (no gap found, idea already published, underpowered design, unverifiable references). Report it and replan.
- Current facts (deadlines, page limits, scheme rules, templates) come from the source at the time of use.

## Related skills

- `idea-to-paper-pipeline` for the full sequence from topic to self-reviewed draft.
- `research-progress-tracker` to hold the plan, milestones, and next actions across sessions.
- `weekly-paper-digest` to keep the literature current while the project runs.
- `paper-search` and `citation-verifier`, which most routes depend on.
- `research-gap-finder`, `methodology-designer`, `results-interpreter`, `paper-outline-generator`, and `self-peer-reviewer` are the usual entry points for the five main stages.
