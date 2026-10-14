# PRISMA 2020 items, search building, and appraisal tools

## 1. Protocol contents

Write these before searching, and record any later change with its date and reason.

| Section | Contents |
|---|---|
| Rationale and question | Why the review is needed; the question in PICO, PECO, SPIDER, or PCC form |
| Eligibility criteria | Population, intervention or exposure or phenomenon, comparator, outcomes, study designs, years, languages, publication types |
| Information sources | Each database and platform, grey literature, registers, citation chasing, contact with authors |
| Search strategy | Full string for at least one database; date to be run |
| Selection process | Number of reviewers per stage, how disagreements are resolved, software |
| Data items and extraction | Fields, form, pilot extraction, number of extractors |
| Risk of bias or quality appraisal | Tool, level (study or outcome), number of assessors |
| Synthesis | Narrative, thematic, or meta-analysis; effect measures; heterogeneity; subgroup and sensitivity analyses |
| Registration | PROSPERO (health), OSF, or other |

## 2. Building a search string

1. List the concepts from the question (usually two to four). Do not include outcomes as a concept unless the yield is unmanageable; outcomes are often missing from abstracts.
2. For each concept list free-text synonyms, spelling variants, acronyms, and the controlled vocabulary term.
3. Join synonyms with OR inside parentheses; join concepts with AND.
4. Add truncation and phrase marks.
5. Translate to each database.
6. Validate: the string must retrieve every paper in a set of three to five known relevant papers. If one is missed, find the missing term and add it.

### Syntax by database

| Feature | Scopus | Web of Science | PubMed | IEEE Xplore | ACM DL |
|---|---|---|---|---|---|
| Title, abstract, keywords | `TITLE-ABS-KEY(...)` | `TS=(...)` | `[tiab]` plus `[Mesh]` | `"All Metadata":` | `Abstract:(...)` and `Title:(...)` |
| Phrase | `"deep learning"` | `"deep learning"` | `"deep learning"[tiab]` | `"deep learning"` | `"deep learning"` |
| Truncation | `diagnos*` | `diagnos*` | `diagnos*[tiab]` | `diagnos*` | `diagnos*` |
| Proximity | `W/3`, `PRE/3` | `NEAR/3` | not supported | `NEAR/3` | not supported |
| Year limit | `PUBYEAR > 2014` | `PY=(2015-2025)` | `2015:2025[dp]` | filter | filter |

Check each platform's current help page; syntax differs between vendors' interfaces to the same database.

### Worked example

Question: does gamification improve engagement in higher education?

- Concept A: gamif* OR "game-based learning" OR "game elements" OR badges OR leaderboard*
- Concept B: "higher education" OR universit* OR undergraduate* OR "college students"
- Concept C: engagement OR motivation OR participation

Scopus: `TITLE-ABS-KEY((gamif* OR "game-based learning" OR "game elements" OR badges OR leaderboard*) AND ("higher education" OR universit* OR undergraduate* OR "college students") AND (engagement OR motivation OR participation)) AND PUBYEAR > 2014`

## 3. Search log

Record for every database: platform, date run, the exact string, limits applied, and the number of records. Rerun and update the log if the search is more than about a year old at submission.

## 4. Screening rules

- Pilot the criteria on 50 to 100 records with all reviewers, then refine wording.
- Title and abstract stage: exclude only when clearly ineligible. Unclear goes forward.
- Full-text stage: one primary reason per excluded report, from a fixed ordered list (apply the first reason that fits).
- Two reviewers independently where possible. Report agreement (Cohen's kappa) and how conflicts were settled.
- A study reported in several papers counts once; link the reports.

## 5. PRISMA 2020 flow numbers

| Box | Count |
|---|---|
| Identification | Records from each database and register; records from other methods (websites, citation searching) reported separately |
| Removed before screening | Duplicates; records marked ineligible by automation tools; other reasons |
| Screened | Records screened; records excluded |
| Retrieval | Reports sought; reports not retrieved |
| Eligibility | Reports assessed; reports excluded, with each reason and its count |
| Included | Studies included; reports of included studies |

Each box must follow arithmetically from the one above.

## 6. Appraisal tools by study design

| Design | Tool |
|---|---|
| Randomised trials | RoB 2 |
| Non-randomised intervention studies | ROBINS-I |
| Cohort and case-control | Newcastle-Ottawa Scale; JBI checklists |
| Cross-sectional | JBI checklist; AXIS |
| Diagnostic accuracy | QUADAS-2 |
| Qualitative | CASP qualitative checklist; JBI |
| Mixed designs in one review | MMAT |
| Prediction models | PROBAST |
| Systematic reviews (in an umbrella review) | AMSTAR 2 |
| Certainty of the body of evidence | GRADE |

Scoping reviews map evidence and normally do not appraise quality. Use PRISMA-ScR for reporting them.

## 7. Synthesis choice

| Situation | Approach |
|---|---|
| Similar designs, populations, outcomes, and measures | Meta-analysis with a random-effects model; report heterogeneity (I², tau²) and prediction interval |
| Comparable outcomes, different measures | Standardised effect sizes, or synthesis without meta-analysis (SWiM) |
| Diverse designs or outcomes | Narrative synthesis with tables grouped by a stated logic |
| Qualitative evidence | Thematic synthesis or meta-ethnography |

## 8. PRISMA 2020 checklist, by section

| Section | Items to report |
|---|---|
| Title | Identify the report as a systematic review |
| Abstract | Structured summary (PRISMA for Abstracts) |
| Introduction | Rationale; objectives |
| Methods | Eligibility criteria; information sources; search strategy; selection process; data collection process; data items; risk of bias assessment; effect measures; synthesis methods; reporting bias assessment; certainty assessment |
| Results | Study selection with flow diagram; study characteristics; risk of bias in studies; results of individual studies; results of syntheses; reporting biases; certainty of evidence |
| Discussion | Interpretation; limitations of the evidence and of the review; implications |
| Other | Registration and protocol; support; competing interests; availability of data, code, and materials |

Take the exact item wording from the current PRISMA statement when completing the checklist for submission.
