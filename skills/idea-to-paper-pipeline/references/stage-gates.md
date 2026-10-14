# Stage gates

Each stage has entry criteria (what must exist to start), exit criteria (what must be true to move on), and stop conditions (when to go back).

## Stage 1. Topic and gap

| | |
|---|---|
| Entry | A topic or idea; field; output type |
| Work | topic-trend-analyzer; research-gap-finder; research-question-formulator |
| Exit | One gap chosen by the user with at least two pieces of evidence; one primary question with objectives; FINER assessment with Feasible and Ethical judged acceptable |
| Stop | No gap survives the still-open check; question cannot be answered with accessible data |
| Artifacts | 01-gap.md |

## Stage 2. Novelty

| | |
|---|---|
| Entry | The primary question and the idea addressing it |
| Work | novelty-checker; citation-graph-explorer on the closest papers |
| Exit | Verdict of differentiated (or incremental with a stated, defensible difference); novelty statement drafted |
| Stop | Already done; return to Stage 1 with the next gap or sharpen the idea |
| Artifacts | 02-novelty.md |

## Stage 3. Literature

| | |
|---|---|
| Entry | Novelty verdict accepted |
| Work | paper-search; citation-graph-explorer; paper-summarizer; paper-comparison-matrix; related-work-writer or literature-review-writer; bibtex-manager |
| Exit | Corpus with search log; matrix; positioning text; clean .bib; the user confirms coverage |
| Stop | A newly found paper does the same thing; return to Stage 2 |
| Artifacts | 03-literature/ |

## Stage 4. Design

| | |
|---|---|
| Entry | Question, positioning |
| Work | methodology-designer or experiment-planner; sample-size-power-calculator; survey-questionnaire-designer; ablation-study-designer; ethics-irb-drafter; experiment-logger setup |
| Exit | Design approved by the user (and supervisor); ethics approval applied for where needed; budget fits resources |
| Stop | Design infeasible within resources; rescope |
| Artifacts | 04-design.md; ethics drafts |
| Pause | The user collects data or runs experiments. No later stage starts without real results. |

## Stage 5. Results

| | |
|---|---|
| Entry | Real data or experiment outputs, logged |
| Work | statistical-test-selector or qualitative-coding-assistant; results-interpreter |
| Exit | Findings graded; claims table with agreed wording |
| Stop | Results do not support a paper as planned; options: more data, narrower claim, negative-result paper |
| Artifacts | 05-results.md |

## Stage 6. Outline and draft

| | |
|---|---|
| Entry | Agreed claims |
| Work | paper-outline-generator; publication-figure-maker; architecture-diagram-maker; latex-table-generator; introduction-writer; limitations-and-future-work-writer; abstract-writer; academic-tone-editor; latex-paper-formatter |
| Exit | Complete draft in the venue template; the user has read it in full |
| Stop | Structural problems found; return to the outline |
| Artifacts | 06-draft/ |

## Stage 7. Citation and integrity check

| | |
|---|---|
| Entry | Complete draft |
| Work | citation-verifier; plagiarism-and-paraphrase-checker; reproducibility-checklist |
| Exit | All references verified or knowingly resolved; similarity issues fixed; checklist answered |
| Stop | Unverifiable references remain unaddressed |
| Artifacts | 07-citations.md |

## Stage 8. Mock review and submission prep

| | |
|---|---|
| Entry | Verified draft |
| Work | self-peer-reviewer; fixes; venue-recommender if open; camera-ready-checker; cover-letter-writer |
| Exit | The user decides to submit, revise, or change venue |
| Stop | A fatal weakness; return to Stage 5 or 6 |
| Artifacts | 08-review.md |

## Re-entry

When the user arrives with existing work, check the exit criteria of earlier stages against what exists, then start at the first stage whose exit criteria are not met.
