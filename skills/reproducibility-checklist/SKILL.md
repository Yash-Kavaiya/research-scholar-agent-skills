---
name: reproducibility-checklist
description: Completes reproducibility and reporting checklists for a paper, such as the NeurIPS paper checklist, the ML Reproducibility Checklist, ML Code Completeness, datasheets and model cards, and guidelines like CONSORT, STROBE, and ARRIVE, answering each item from evidence in the manuscript and listing what must be added. Use when the user asks to "fill the NeurIPS checklist", "complete the reproducibility checklist", "is my paper reproducible", "what do I need to report for reproducibility", "write a reproducibility statement", or prepares code and data for release.
---

# Reproducibility Checklist

Answer each checklist item from what the paper and its artifacts actually contain, cite where, and turn every gap into a concrete fix.

## When to use

- A venue requires a reproducibility or paper checklist with the submission.
- Preparing code, data, and models for release.
- Auditing a draft for missing experimental details before reviewers do.

Hand off instead for reimplementing someone else's paper (`paper-to-code-reproducer`).

## Inputs

- The manuscript with appendix, and the venue and year.
- The venue's current checklist text. Obtain it from the call for papers or the template; items and answer formats change between years.
- The code repository, configs, experiment log, and dataset documentation.

## Workflow

1. **Get the right checklist** for the venue and year:

   | Context | Checklist or guideline |
   |---|---|
   | NeurIPS | Paper checklist in the LaTeX template (claims, limitations, theory, experimental reproducibility, open access to data and code, experimental details, statistical significance, compute resources, ethics, broader impacts, safeguards, licences, assets, human subjects, LLM usage) |
   | ICML, ICLR, AAAI, ACL venues | Venue-specific reproducibility or responsible-research checklist |
   | General ML | ML Reproducibility Checklist (Pineau et al.); ML Code Completeness Checklist |
   | Datasets | Datasheets for Datasets; Data Statements |
   | Models | Model Cards |
   | Clinical trials | CONSORT; SPIRIT for protocols |
   | Observational studies | STROBE |
   | Systematic reviews | PRISMA 2020 |
   | Diagnostic accuracy | STARD |
   | Prediction models, clinical AI | TRIPOD+AI, CONSORT-AI |
   | Animal research | ARRIVE |
   | Qualitative research | COREQ, SRQR |

   The EQUATOR Network lists reporting guidelines for health research.
2. **Answer each item from evidence.** Search the manuscript, appendix, and repository for the information. Record the answer in the venue's format (Yes, No, N/A, or as specified), a one- or two-sentence justification, and the location (section, table, appendix, file).
3. **Apply the evidence rule**: "Yes" requires a location. If the information exists only in the author's head or the code, the answer is "No, to be added", and it becomes an action.
4. **Audit the experimental details** that reviewers most often find missing:
   - *Data*: sources, versions, licences, splits and how they were made, preprocessing, exclusions, statistics.
   - *Model and training*: architecture details, parameter counts, every hyperparameter with its final value, the search space and method and budget, selection criterion.
   - *Evaluation*: metric definitions, number of runs or seeds, what error bars represent, statistical tests.
   - *Compute*: hardware type, memory, runtime per run, total compute including failed and preliminary runs.
   - *Code*: dependencies with versions, training and evaluation commands, pretrained weights, random seeds, expected results.
   - *Theory*: full assumptions and complete proofs.
5. **Check the artifacts.** For a code release, against the ML Code Completeness items: dependency specification, training code, evaluation code, pretrained models, and a README with results and the commands that produce them. Verify the README commands run from a clean environment if possible.
6. **Handle anonymity.** For double-blind review, release code through an anonymised repository or supplementary zip, with no names, usernames, paths, or institution identifiers in code, commit history, or notebooks.
7. **Do not treat "No" as failure.** Venues state that an honest "No" with a justification is acceptable (for example proprietary data that cannot be released). A false "Yes" is a problem.
8. **Produce the action list**, ordered by reviewer impact, and draft the text to add for each gap.
9. **Write the reproducibility statement** where the venue asks for one: a short paragraph pointing to where data, code, hyperparameters, and proofs are found.

## Output format

```markdown
## <Checklist name>, <venue and year>

| # | Item | Answer | Justification | Where |
|---|---|---|---|---|
| 3 | Statistical significance: error bars reported and defined? | Yes | Mean ± s.d. over 5 seeds; defined in captions | Tables 2–3, §5.1 |
| 5 | Compute resources reported? | No (to add) | GPU type given; runtime and total compute missing | n/a |

## Actions before submission
| Priority | Gap | Text or artifact to add | Where |

## Reproducibility statement (draft)
> ...

## Items answered N/A, with the reason
```

For NeurIPS, also deliver the answers in the template's `\answerYes{}`, `\answerNo{}`, `\answerNA{}` form with justifications.

## Quality bar and pitfalls

- Answer truthfully. Never mark "Yes" for something not in the submission; reviewers check, and some venues desk-reject for inaccurate checklists.
- Do not invent details to close a gap (seeds, runtimes, hardware, hyperparameters). Ask the author or leave it as an action.
- Use the checklist wording for the current year. Do not reproduce an older version from memory as if it were current.
- "Code will be released upon acceptance" is a "No" for the submission as reviewed. Say so in the justification.
- Report total compute, including runs that did not make it into the paper, where the checklist asks.
- Releasing data has conditions: licences, consent, and personal information. Check before promising release.
- Reproducibility information in the appendix must be referenced from the main text, or readers will not find it.

## Related skills

- `experiment-logger` holds the configs, seeds, commits, and run times the checklist asks for.
- `experiment-planner` plans for these items before experiments start.
- `limitations-and-future-work-writer` for the limitations item.
- `ethics-irb-drafter` for human-subjects and data-consent items.
- `dataset-finder` for dataset licences and documentation.
- `self-peer-reviewer` uses the completed checklist as part of the pre-submission review.
- `camera-ready-checker` confirms the checklist is included in the final PDF.
