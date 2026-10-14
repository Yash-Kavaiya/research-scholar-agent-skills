# Checklist items explained, with evidence to look for

## 1. ML paper checklists (NeurIPS-style), by topic

Wording and numbering change by year; map these topics onto the current form.

| Topic | What it asks | Evidence that supports "Yes" | Common reason for an honest "No" |
|---|---|---|---|
| Claims | Do the abstract and introduction reflect the contributions and scope? | Claims match results sections; scope stated | n/a; fix the claims instead |
| Limitations | Are limitations discussed? | A limitations section or paragraph | Rarely acceptable to answer No |
| Theory | Are assumptions stated and proofs complete? | Assumptions listed; full proofs in appendix | Proof sketches only |
| Experimental reproducibility | Is enough disclosed to reproduce the main results? | Data, model, training, evaluation details | Proprietary model or data |
| Open access to data and code | Are code and data released or will they be? | Repository link, anonymised for review; instructions | Licence or privacy restrictions |
| Experimental settings | Are splits, hyperparameters, and their selection described? | Appendix table; selection method | |
| Statistical significance | Are error bars or tests reported and defined? | Mean ± SD with n; CI; test names | Single-run large-scale training (justify) |
| Compute resources | Are hardware, time, and total compute reported? | Hardware type, hours per run, total including failed runs | |
| Code of ethics | Does the work conform to the venue's ethics code? | Statement | |
| Broader impacts | Are positive and negative societal impacts discussed? | Section or paragraph | Foundational work with no direct path (justify) |
| Safeguards | Are safeguards for high-risk releases described? | Access controls, usage policies | N/A when nothing risky is released |
| Licences for existing assets | Are creators credited and licences respected? | Citations and licence names for datasets, code, models | |
| New assets | Are released assets documented? | Datasheet, model card, README, licence | |
| Human subjects and crowdsourcing | Instructions, payment, and approvals? | Instructions in appendix, pay rate, IRB statement | N/A when no human participants |
| IRB approval | Was ethics approval obtained where required? | Approval statement | N/A when not applicable |
| Use of LLMs | Is LLM use in the method or writing declared as required? | Statement per the venue's policy | |

## 2. ML Reproducibility Checklist (general)

| Area | Items |
|---|---|
| Models and algorithms | Clear description; complexity analysis; link to code |
| Theory | Assumptions; complete proofs |
| Datasets | Statistics; splits; preprocessing; download link or simulation code; licence |
| Code | Dependencies; training code; evaluation code; pretrained models; README with commands and results |
| Results | Hyperparameter ranges and selection; number of runs; definition of statistics; variance; average runtime; computing infrastructure |

## 3. ML Code Completeness Checklist

| Item | Evidence |
|---|---|
| Specification of dependencies | requirements.txt or environment.yml with versions |
| Training code | Script that reproduces training |
| Evaluation code | Script that reproduces the reported metrics |
| Pre-trained models | Download link |
| README with results and commands | Table of results and the exact commands |

## 4. Reporting guidelines outside ML

| Guideline | Study type | Key items |
|---|---|---|
| CONSORT 2025 (replaces CONSORT 2010; CONSORT-AI extension for AI interventions) | Randomised trials | Flow diagram, randomisation, allocation concealment, blinding, prespecified outcomes, registration, harms |
| SPIRIT 2025 (replaces SPIRIT 2013) | Trial protocols | Schedule of enrolment and assessments; outcomes; sample size; data management |
| STROBE | Observational studies | Setting, participants, variables, bias, study size, statistical methods, missing data |
| PRISMA 2020 | Systematic reviews | Search, selection, flow diagram, risk of bias, synthesis |
| STARD | Diagnostic accuracy | Reference standard, cross-tabulation, flow |
| TRIPOD+AI | Prediction models | Data sources, predictors, model development, validation, performance measures |
| ARRIVE 2.0 | Animal research | Study design, sample size, randomisation, blinding, outcome measures |
| COREQ, SRQR | Qualitative research | Research team, reflexivity, sampling, data collection, analysis |
| CHEERS | Health economic evaluations | Perspective, costs, outcomes, uncertainty |

The EQUATOR Network maintains the current versions and extensions.

## 5. Datasheets, data statements, and model cards

| Document | Sections |
|---|---|
| Datasheet for datasets | Motivation; composition; collection process; preprocessing and labelling; uses; distribution; maintenance |
| Data statement (NLP) | Curation rationale; language variety; speaker and annotator demographics; speech situation; text characteristics |
| Model card | Model details; intended use; factors; metrics; evaluation data; training data; quantitative analyses; ethical considerations; caveats |

## 6. Answering rules

| Answer | When | Justification needed |
|---|---|---|
| Yes | The information is in the submission | Location (section, appendix, file) |
| No | It is not, for a reason | The reason (proprietary, privacy, cost, scope) |
| N/A | The item does not apply | Why it does not apply |

Some venues treat inaccurate answers as grounds for rejection. Fix the paper rather than the answer where possible.

## 7. Total compute

Report: hardware type and count, hours per run, number of runs (including hyperparameter search, failed and preliminary runs where the venue asks), and the total in GPU-hours or equivalent.

## 8. Anonymised artifacts for review

Anonymise code repositories (author names, usernames, paths, commit history, notebook metadata, licence headers) or provide a supplementary archive. State in the paper how code will be released after review.
