---
name: results-interpreter
description: Turns raw results such as tables of numbers, statistical output, logs, or model metrics into clearly stated findings, each with its evidence, effect size, uncertainty, and caveats, and drafts the results and discussion text. Use when the user asks "what do these results mean", "interpret this output", "help me write the results section", "is this improvement meaningful", "explain this regression table", or pastes numbers and wants to know what they can claim.
---

# Results Interpreter

Say what the numbers support, how strongly, and where they stop. A finding is a claim plus its evidence plus its limits.

## When to use

- Experiments or analyses are done and need to become findings.
- Writing the results and discussion sections.
- Deciding whether an improvement is real and whether it matters.

Hand off instead to run the statistics (`statistical-test-selector`) or to plan further experiments (`experiment-planner`, `ablation-study-designer`).

## Inputs

- The results: tables, CSV files, statistical output, training logs, confusion matrices, plots.
- What was being tested: the research questions, hypotheses, or claims.
- The setup: datasets, baselines, metrics, sample sizes, number of runs or seeds, how the baselines were obtained.
- The analysis plan, if one was fixed in advance.

Ask for the setup when it is missing. Numbers cannot be interpreted without knowing how they were produced.

## Workflow

1. **Check the numbers before reading them.** Do totals and percentages add up? Are any values impossible (accuracy above 100, negative variance, identical results across seeds)? Are the best results suspiciously good (possible leakage)? Raise problems first.
2. **Restate each question or hypothesis** and locate the numbers that bear on it.
3. **Describe before inferring.** State the direction and size of each difference in plain terms and in the metric's units: absolute difference, relative change, and effect size.
4. **Quantify uncertainty.** Use the variance across seeds or participants, confidence intervals, and tests. If there is one run and no variance, say the result is a single observation and cannot be separated from noise. Compute what can be computed from the supplied data with code, not by eye.
5. **Judge practical significance.** Compare the difference with: run-to-run noise; the gap between existing methods on this benchmark; the minimal difference that matters in use; and the extra cost of getting it.
6. **Look for the pattern across conditions.** Where does the effect hold, shrink, or reverse (datasets, subgroups, sizes, difficulty levels)? An average can hide opposite effects.
7. **Consider alternative explanations** for each finding: confounds (more parameters, more data, more tuning), selection of the best checkpoint or seed, measurement artefacts, multiple comparisons, regression to the mean.
8. **Grade each finding**: *well supported* (consistent, replicated across datasets or seeds, clear of noise), *suggestive* (right direction, limited evidence), or *inconclusive*.
9. **Report negative and null results** with the same care. State what was tried and what the data rule out.
10. **Draft the text.** Results: what was found, with numbers, in the order of the research questions, no interpretation beyond what the numbers show. Discussion: what it means, how it relates to prior work, alternative explanations, limitations.

## Output format

```markdown
## Data checks
- <anything inconsistent or suspicious, or "no issues found">

## Findings
### F1. <Claim in one sentence>
- Evidence: <numbers, table or figure reference>
- Size: <absolute, relative, effect size>; uncertainty: <CI, SD over n seeds, test>
- Holds for: ... Does not hold for: ...
- Alternative explanations: ...
- Support: well supported | suggestive | inconclusive

### F2. ...

## What you can and cannot claim
| Claim | Verdict | Wording to use |

## Suggested additional analyses
## Draft text
### Results
### Discussion
```

## Quality bar and pitfalls

- Use only the numbers provided or computed from them. Never fill in a missing value, standard deviation, or p-value.
- Do not turn "not significant" into "no effect", or "significant" into "important".
- Correlational results get correlational verbs: "is associated with", not "leads to" or "improves".
- "Outperforms" needs a fair comparison: same data, same tuning effort, variance reported. Otherwise write "obtains a higher score under these conditions".
- A gain smaller than the seed-to-seed standard deviation is not a finding.
- Do not explain a result with a mechanism that was not tested. Offer it as a hypothesis and say what would test it.
- Report all conditions that were run, including the ones that did not work.
- Match the strength of the wording to the grade: "shows" for well supported, "suggests" for suggestive.
- If the results contradict the user's hypothesis, say so plainly. Do not look for a framing that hides it.

## Related skills

- `statistical-test-selector` to compute tests, effect sizes, and intervals.
- `experiment-logger` as the source of run records.
- `ablation-study-designer` and `experiment-planner` for the follow-up analyses.
- `publication-figure-maker` and `latex-table-generator` to present the findings.
- `limitations-and-future-work-writer` uses the caveats recorded here.
- `abstract-writer` and `introduction-writer` take the "wording to use" column.
- `self-peer-reviewer` checks the claims against the evidence again before submission.
