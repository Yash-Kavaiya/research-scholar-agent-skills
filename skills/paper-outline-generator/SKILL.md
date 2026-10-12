---
name: paper-outline-generator
description: Produces a section-by-section outline for a research paper adapted to the target venue and paper type, with the claim each section must make, the figures and tables it needs, a page or word budget, and the missing material. Use when the user asks to "outline my paper", "structure this paper", "what sections should my paper have", "plan the paper before writing", "turn these results into a paper outline", or is starting a draft for a journal or conference.
---

# Paper Outline Generator

Plan the paper as an argument before any prose is written: what it claims, what evidence supports each claim, and where each piece goes within the venue's limits.

## When to use

- Results exist (or are planned) and a draft is about to start.
- A draft has structural problems and needs re-planning.
- Converting a thesis chapter or report into a paper.

Hand off instead for a thesis chapter (`thesis-chapter-writer`) or for writing individual sections (`abstract-writer`, `introduction-writer`).

## Inputs

- The contribution in one or two sentences, and the main results.
- Target venue and paper type (full research paper, short paper, journal article, review, systems or dataset paper).
- The venue's current call for papers or author guidelines: page or word limit, required sections, template.
- Available figures, tables, and experiments, and what is still missing.

## Workflow

1. **Get the venue's rules** from its current author guidelines. Limits and required sections change yearly; do not rely on memory. Record: length limit and what counts toward it (references and appendices often do not), required statements (ethics, limitations, data availability, reproducibility checklist), anonymisation, template.
2. **Write the one-sentence message** of the paper: "We show that X, which matters because Y." If this cannot be written, the paper is not ready to outline; say so.
3. **List the claims** (usually 2 to 4) and attach the evidence for each: an experiment, a table, a proof, a study. A claim with no evidence is either cut or becomes a to-do item.
4. **Choose the structure** for the paper type and field:

   | Type | Typical structure |
   |---|---|
   | Empirical (sciences, medicine, social science) | IMRaD: Introduction, Methods, Results, Discussion; structured abstract |
   | ML or CS conference | Introduction, Related Work, Method, Experiments, (Analysis), Limitations, Conclusion |
   | Systems | Introduction, Background and Motivation, Design, Implementation, Evaluation, Related Work, Conclusion |
   | Theory | Introduction, Preliminaries, Main Results, Proof Sketches, Discussion; full proofs in appendix |
   | Dataset or benchmark | Introduction, Related Datasets, Construction, Statistics and Analysis, Baselines, Limitations and Ethics |
   | Review | Introduction, Method of the review, Thematic sections, Open Problems, Conclusion |

5. **Outline each section** with: its purpose in one sentence, the points in order (one line per paragraph), the figures and tables it contains, and its length budget.
6. **Plan the display items first.** Most readers look at figures and tables before the text. Decide Figure 1 (the overview or key result), the main results table, and which results go to the appendix.
7. **Budget the length.** Allocate pages or words per section so the total fits. For an 8 to 9 page conference paper a common split is: introduction 1 to 1.25, related work 0.75 to 1, method 2 to 2.5, experiments 2.5 to 3, discussion and conclusion 0.5. Adjust to the paper.
8. **Check the flow**: reading only the section headings and the first sentence of each paragraph should convey the whole argument.
9. **List the gaps**: missing experiments, figures, citations, or decisions, each with an owner and priority.

## Output format

```markdown
# Outline: <working title>
Venue: <name, year>. Limit: <pages/words, what counts>. Template: <name>. Required: <statements>.
Message: <one sentence>

## Claims and evidence
| # | Claim | Evidence | Where |

## Sections
### 1. Introduction (≈1 page)
Purpose: ...
- P1: context ...
- P2: problem and gap ...
- P3: approach ...
- P4: contributions (bulleted)
Display: Fig. 1 (overview)

### 2. ...

## Display items
| Item | Shows | Supports claim | Status |

## Appendix plan
## Missing before drafting
| Item | Needed for | Priority |
```

## Quality bar and pitfalls

- Do not state a venue's page limit or required sections from memory as fact. Take them from the current guidelines, or mark them "typical, confirm".
- The outline must not include results that do not exist. Mark planned experiments as planned.
- Every section earns its place by supporting a claim. Cut sections that only record effort.
- One main message. Papers that try to carry three unrelated contributions get rejected for lack of focus.
- Put the main result early. Do not make the reader wait for it until page 7.
- Keep the outline at the level of paragraphs. Section headings alone are not an outline.

## Related skills

- `results-interpreter` supplies the claims the outline is built on.
- `venue-recommender` if the venue is not yet chosen.
- `introduction-writer`, `abstract-writer`, `related-work-writer`, and `limitations-and-future-work-writer` draft the sections.
- `publication-figure-maker`, `architecture-diagram-maker`, and `latex-table-generator` produce the display items.
- `latex-paper-formatter` sets up the venue template.
- `idea-to-paper-pipeline` runs this as one stage of the full sequence.
