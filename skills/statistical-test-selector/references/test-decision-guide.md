# Test decision guide, assumptions, and APA reporting

## 1. Decision path

1. **What is the goal?** Compare groups, relate variables, predict an outcome, or test agreement or fit.
2. **What type is the outcome?** Continuous, ordinal, binary, count, categorical with more than two levels, time to event.
3. **How many groups or predictors?**
4. **Are observations independent?** Or paired, repeated, clustered.
5. **Are parametric assumptions reasonable?** Judged from design, sample size, and plots.

## 2. Full table

| Goal | Outcome | Groups or design | Parametric | Non-parametric or alternative |
|---|---|---|---|---|
| One sample against a value | Continuous | one | One-sample t test | Wilcoxon signed-rank |
| Two independent groups | Continuous | 2 | Welch's t test | Mann-Whitney U |
| Two related measures | Continuous | paired | Paired t test | Wilcoxon signed-rank |
| Three or more independent groups | Continuous | k | One-way ANOVA; Welch's ANOVA | Kruskal-Wallis |
| Three or more related measures | Continuous | repeated | Repeated-measures ANOVA; linear mixed model | Friedman |
| Two or more factors | Continuous | factorial | Factorial ANOVA | Aligned rank transform ANOVA |
| Group comparison adjusting for a covariate | Continuous | k | ANCOVA | Rank-based ANCOVA |
| Association | Two continuous | n/a | Pearson r | Spearman rho; Kendall tau |
| Association | Two categorical | independent | Chi-square test of independence | Fisher's exact test (small expected counts) |
| Change in a binary outcome | Binary | paired | McNemar test | n/a |
| Ordered categories | Ordinal | k | n/a | Mann-Whitney or Kruskal-Wallis; ordinal logistic regression |
| Predict continuous outcome | Continuous | predictors | Linear regression | Robust or quantile regression |
| Predict binary outcome | Binary | predictors | Logistic regression | n/a |
| Predict counts | Count | predictors | Poisson regression | Negative binomial (overdispersion) |
| Time to event | Survival | groups or predictors | Cox regression | Log-rank test; Kaplan-Meier |
| Clustered or longitudinal data | Any | nested | Mixed-effects models; GEE | n/a |
| Agreement between raters | Categorical | 2 raters | Cohen's kappa | Fleiss' kappa for more raters |
| Agreement between raters | Continuous | raters | ICC | Bland-Altman analysis |
| Fit to expected proportions | Categorical | one sample | Chi-square goodness of fit | Exact multinomial test |

## 3. Assumptions and what to do when they fail

| Assumption | Check | If violated |
|---|---|---|
| Independence | Design | Use paired, repeated, or mixed models. Not fixable by a different test of the same kind |
| Normality of residuals or differences | Q-Q plot; Shapiro-Wilk as a supplement | With n of about 30 or more per group, t tests and ANOVA are usually robust; otherwise transform or use rank-based tests |
| Equal variances | Levene's test; ratio of largest to smallest SD | Welch's t test and Welch's ANOVA; Games-Howell post hoc |
| Linearity | Residual plots | Transform, add terms, or use non-linear models |
| Expected counts of 5 or more | Expected table | Fisher's exact test (2×2); merge sparse categories |
| No influential outliers | Boxplots; Cook's distance | Check the data; robust methods; report with and without |
| Sphericity (repeated measures) | Mauchly's test | Greenhouse-Geisser correction, or a mixed model |

Formal normality tests reject trivial departures in large samples and miss real ones in small samples. Plots and design matter more.

## 4. Effect sizes to report

| Test | Effect size | Rough guide (small, medium, large) |
|---|---|---|
| t tests | Cohen's d or Hedges' g | 0.2, 0.5, 0.8 |
| Paired t | dz | 0.2, 0.5, 0.8 |
| ANOVA | Eta squared; partial eta squared; omega squared | 0.01, 0.06, 0.14 |
| Mann-Whitney, Wilcoxon | Rank-biserial r | 0.1, 0.3, 0.5 |
| Kruskal-Wallis | Epsilon squared | read like eta squared (0.01, 0.06, 0.14) as a rough guide |
| Correlation | r | 0.1, 0.3, 0.5 |
| Chi-square | Cramér's V (depends on df); phi for 2×2 | for df = 1: 0.1, 0.3, 0.5 |
| 2×2 tables | Odds ratio, risk ratio, risk difference | context-dependent |
| Regression | R², f², standardised coefficients | f²: 0.02, 0.15, 0.35 |

Interpret magnitude in the context of the field, not only by these guides.

## 5. Multiple comparisons

| Method | Controls | Use |
|---|---|---|
| Bonferroni | Family-wise error | Few planned comparisons; conservative |
| Holm | Family-wise error | Same situations; more powerful than Bonferroni |
| Tukey HSD | Family-wise error for all pairwise means | After a one-way ANOVA with equal variances |
| Games-Howell | Family-wise error, unequal variances | After Welch's ANOVA |
| Dunn's test with adjustment | Pairwise after Kruskal-Wallis | Rank-based post hoc |
| Benjamini-Hochberg | False discovery rate | Many tests, exploratory |

Define the family of tests before analysis.

## 6. APA style (7th edition) reporting

| Element | Format |
|---|---|
| Statistic symbols | Italic: *t*, *F*, *r*, *p*, *M*, *SD*, *N*, *n*, χ² |
| Degrees of freedom | In parentheses: *t*(58) = 2.71; *F*(2, 87) = 5.12; χ²(1, *N* = 80) = 4.21 |
| p-values | Exact to two or three decimals; *p* < .001 for smaller values; no leading zero |
| Leading zero | Omit for values that cannot exceed 1 (*p*, *r*, eta squared); keep for others (*d* = 0.45) |
| Decimals | Two for most statistics |
| Confidence intervals | 95% CI [lower, upper] |
| Means | *M* = 70.2, *SD* = 8.1 |

Examples:

- Independent groups: The treatment group scored higher (*M* = 75.8, *SD* = 7.9) than the control group (*M* = 70.2, *SD* = 8.1), *t*(57.9) = 2.71, *p* = .009, *g* = 0.69, 95% CI of the difference [1.46, 9.74].
- ANOVA: Accuracy differed across models, *F*(2, 87) = 5.12, *p* = .008, η² = .11. Tukey tests showed ...
- Correlation: Study hours were positively correlated with grades, *r*(48) = .43, *p* = .002, 95% CI [.17, .63].
- Chi-square: Outcome was associated with treatment, χ²(1, *N* = 80) = 8.12, *p* = .004, *V* = .32.
- Mann-Whitney: Scores were higher in group B, *U* = 210.5, *p* = .021, *r* = .34.

## 7. Interpretation rules

- A non-significant result means the data do not show an effect at this sample size; report the interval to show what effects remain plausible.
- Statistical significance is not practical importance; discuss the effect size in units that matter.
- "A is significant and B is not" does not show that A and B differ; test the difference.
- Pre-register or at least fix the analysis before seeing the outcome data where possible.
