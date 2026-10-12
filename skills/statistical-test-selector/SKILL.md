---
name: statistical-test-selector
description: Chooses the appropriate statistical test for a research question and data, checks its assumptions, runs it on a CSV, and reports the result in APA style with an effect size and confidence interval. Use when the user asks "which statistical test should I use", "t test or ANOVA", "is this difference significant", "run a Mann-Whitney", "my data is not normal, what now", "report this in APA format", or shares data and wants it analysed.
---

# Statistical Test Selector

Match the test to the design and the data, verify the assumptions, compute with a script, and report what the result does and does not show.

## When to use

- Planning the analysis for a study.
- Analysing collected data to compare groups or test an association.
- Checking whether a reported test was appropriate.

Hand off instead for sample-size planning (`sample-size-power-calculator`) and for turning results into findings (`results-interpreter`).

## Inputs

- The research question or hypothesis.
- The outcome variable and its type (continuous, ordinal, binary, count, categorical).
- The predictor or grouping: number of groups, independent or paired/repeated.
- Sample size per group, and the data file when it exists (CSV, long format: one row per observation).
- Anything that breaks independence: repeated measures, clusters, matched samples.

## Workflow

1. **Classify the question** and pick the candidate test:

   | Goal | Outcome | Design | Parametric | Non-parametric |
   |---|---|---|---|---|
   | Compare 2 groups | Continuous | Independent | Welch's t test | Mann-Whitney U |
   | Compare 2 conditions | Continuous | Paired | Paired t test | Wilcoxon signed-rank |
   | Compare 3+ groups | Continuous | Independent | One-way ANOVA or Welch's ANOVA | Kruskal-Wallis |
   | Compare 3+ conditions | Continuous | Repeated | Repeated-measures ANOVA or mixed model | Friedman |
   | Association | Two continuous | n/a | Pearson r | Spearman rho |
   | Association | Two categorical | Independent | Chi-square | Fisher's exact (2×2, small counts) |
   | Paired proportions | Binary | Paired | McNemar | n/a |
   | Predict an outcome | Continuous / binary / count | Several predictors | Linear / logistic / Poisson regression | n/a |
   | Clustered or longitudinal | Any | Nested | Mixed-effects model, GEE | n/a |

2. **Run the script** for the designs it covers. It checks assumptions, picks the test, and reports:

   ```bash
   python scripts/run_test.py two-groups data.csv --value score --group condition
   python scripts/run_test.py two-groups data.csv --value score --group time --paired --subject id
   python scripts/run_test.py multi-groups data.csv --value accuracy --group model
   python scripts/run_test.py correlation data.csv --x hours --y grade
   python scripts/run_test.py categorical data.csv --row treatment --col outcome
   ```

   The JSON output contains descriptives, assumption checks (Shapiro-Wilk, Levene, expected counts), the chosen test with the `reason`, the statistic, p-value, effect size, post hoc comparisons for 3+ groups, and an `apa` string. `--test` overrides the choice; use it when the analysis plan fixed the test in advance.
3. **How the script decides.** Independent two-group comparisons default to Welch's t test, which does not assume equal variances. Non-parametric tests are chosen when normality is rejected and a group has fewer than 30 observations. For 3+ groups, Levene's test decides between classic and Welch's ANOVA. Post hoc: Tukey HSD after ANOVA; Holm-adjusted pairwise tests otherwise.
4. **For designs the script does not cover** (repeated measures with 3+ levels, factorial ANOVA, regression, mixed models, McNemar, Friedman), write the analysis in Python (`scipy`, `statsmodels`, `pingouin`) or R, run it, and report the same elements.
5. **Inspect the data yourself.** Look at group sizes, outliers, and a plot. Assumption tests are underpowered in small samples and oversensitive in large ones; the plot and the design matter more than the Shapiro-Wilk p-value.
6. **Correct for multiple comparisons** when several tests address one question (Holm or Benjamini-Hochberg), and say which family of tests was corrected.
7. **Report** with descriptives, the test, the statistic with degrees of freedom, the exact p-value, the effect size, and a confidence interval. Start from the `apa` string and write `chi-square`, `eta squared`, and similar names as symbols (χ², η²) in the manuscript.

## Output format

```markdown
## Analysis
- Question: ...
- Variables: outcome <type>, grouping <levels, independent | paired>
- Test: <name>. Why: <reason from assumption checks and design>

## Assumption checks
| Check | Result | Verdict |

## Result
Descriptives: control M = 70.2, SD = 8.1, n = 30; treatment M = 75.8, SD = 7.9, n = 30.
> Scores were higher in the treatment group than in the control group, t(57.9) = −2.71, p = .009, g = −0.69, 95% CI of the difference [−9.74, −1.46].

## Post hoc comparisons (if any)
## Interpretation and caveats
```

## Quality bar and pitfalls

- Run the test; never estimate a statistic or p-value. Every reported number comes from executed code.
- The design decides the test before the data does. Paired data analysed as independent, or repeated measures treated as separate observations, is the most damaging error.
- Report the effect size and interval with every test. A p-value alone says nothing about magnitude.
- p > .05 means the data are inconclusive at this sample size. It does not show there is no effect.
- Do not test several outcomes or subgroups and report only the significant ones.
- Choosing the test after seeing which one gives p < .05 is p-hacking. Record the choice and its reason first.
- Report exact p-values (p = .032), and p < .001 for very small ones. Never write p = .000.
- Likert single items are ordinal: use rank-based tests or ordinal models.

## Related skills

- `sample-size-power-calculator` to plan the sample for the chosen test.
- `methodology-designer` and `experiment-planner` for the analysis plan.
- `results-interpreter` to turn the output into findings.
- `publication-figure-maker` to plot the comparison.
- `latex-table-generator` for the results table.
- `paper-critic` uses the same table to check tests in published papers.
