# Claim strength, alternative explanations, and wording

## 1. Size in context

Express each difference three ways:

| Form | Example |
|---|---|
| Absolute | Error fell from 12.4% to 9.1% (3.3 percentage points) |
| Relative | A 27% relative reduction in error |
| Standardised | d = 0.45; or the gap expressed in seed standard deviations |

Then compare it with:

| Benchmark | Question |
|---|---|
| Noise | Is the gap larger than run-to-run or sampling variability? |
| Prior progress | How large were typical improvements between earlier methods on this benchmark? |
| Practical threshold | Is it above the smallest difference that matters to users, patients, or decisions? |
| Cost | What extra compute, data, time, or complexity does it require? |

## 2. Grading the evidence

| Grade | Criteria | Wording |
|---|---|---|
| Well supported | Consistent across datasets, seeds, or samples; outside noise; fair comparison; design supports the claim type | "shows", "demonstrates", "X outperforms Y on ..." |
| Suggestive | Right direction; limited replication, small sample, or borderline intervals | "suggests", "indicates", "is consistent with" |
| Inconclusive | Within noise, conflicting, or underpowered | "we found no clear difference", "the data do not distinguish" |
| Contradicted | Evidence against the hypothesis | "did not improve", "contrary to our hypothesis" |

## 3. Wording by design

| Design | Allowed verbs | Avoid |
|---|---|---|
| Randomised experiment | causes, increases, reduces, improves | |
| Observational, cross-sectional | is associated with, predicts, co-occurs with | leads to, drives, impacts, results in |
| Computational comparison, fair protocol | outperforms on <benchmark>, achieves higher <metric> | is better (general), solves |
| Single dataset | on <dataset> | in general, robust |
| Qualitative | participants described, a theme was, suggests | proves, most people (without counts) |

## 4. Alternative explanations to rule out or name

| Alternative | Question |
|---|---|
| Unequal effort | Did the new method get more tuning, data, compute, or parameters? |
| Selection of results | Were seeds, checkpoints, datasets, or subgroups chosen after seeing results? |
| Leakage | Could test information have reached training? |
| Confounding | Is a third variable driving both? |
| Regression to the mean | Were groups selected on extreme scores? |
| Measurement artefact | Does the metric reward something other than the claimed property? |
| Multiple comparisons | How many tests were run to find this one? |
| Novelty or demand effects | Would participants behave differently simply because something changed? |
| Ceiling or floor | Is there room to improve on the measure? |
| Chance | What do the interval and the number of runs allow? |

## 5. Patterns across conditions

Look for:

- Where the effect is largest and smallest (dataset, subgroup, difficulty, length, size).
- Reversals: conditions where the method is worse. Report them.
- Dose-response: whether the effect grows with the amount of the intervention.
- Interaction: whether one factor's effect depends on another.
- Averages hiding opposite subgroup effects (Simpson's paradox).

## 6. Data checks before interpretation

| Check | Red flag |
|---|---|
| Totals and percentages | Do not add up |
| Impossible values | Accuracy above 100, negative counts or variances |
| Identical numbers across seeds | Seeds not applied |
| Suspiciously good results | Possible leakage |
| Missing conditions | Runs omitted from the table |
| Inconsistent n | Sample size differs between tables without explanation |

## 7. Results versus discussion

| Results section | Discussion section |
|---|---|
| What was found, in the order of the research questions | What it means |
| Numbers, intervals, tests | Comparison with prior work |
| Neutral verbs (was, showed, differed) | Mechanisms, offered as explanations to be tested |
| No speculation | Alternative explanations and limitations |
| Figures and tables referenced | Implications for practice and future research |

## 8. Sentence patterns

- Main finding: "<Method> reduced <metric> from <a> to <b> (<interval or SD>, <n> runs), a <relative> reduction."
- Comparison: "Compared with <baseline>, <method> achieved <metric> of <x> versus <y> (<test>, <p>, <effect size>)."
- Null result: "We found no clear difference in <metric> between <A> and <B> (<estimate>, 95% CI [<l>, <u>]); effects larger than <u> can be ruled out."
- Heterogeneity: "The gain was largest on <condition> (<x>) and absent on <condition> (<y>)."
- Limitation: "Because <design limit>, these results show <what>, not <what>."

## 9. Negative and null results

Report them with the same structure: what was tested, how, the estimate with its interval, and what the data rule out. A clear null result with adequate power is a finding.
