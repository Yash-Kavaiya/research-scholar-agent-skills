# Effect sizes, conversions, and sample-size adjustments

## 1. Effect-size measures and conventional benchmarks

Benchmarks are Cohen's conventions. Use them only when no better basis exists, and say so.

| Measure | Used for | Small | Medium | Large |
|---|---|---|---|---|
| d | Difference between two means | 0.2 | 0.5 | 0.8 |
| f | One-way ANOVA | 0.10 | 0.25 | 0.40 |
| r | Correlation | 0.1 | 0.3 | 0.5 |
| w | Chi-square | 0.1 | 0.3 | 0.5 |
| h | Difference between two proportions | 0.2 | 0.5 | 0.8 |
| f² | Multiple regression | 0.02 | 0.15 | 0.35 |
| Eta squared | Proportion of variance | 0.01 | 0.06 | 0.14 |

## 2. Computing an effect size from what you have

| You have | Formula |
|---|---|
| Two means and SDs | d = (M1 − M2) / SD_pooled, with SD_pooled = sqrt(((n1 − 1)SD1² + (n2 − 1)SD2²) / (n1 + n2 − 2)) |
| A raw difference that matters and the SD | d = minimal important difference / SD |
| A t statistic, independent groups | d = t × sqrt(1/n1 + 1/n2) |
| Two proportions | h = 2·asin(sqrt(p1)) − 2·asin(sqrt(p2)) |
| Group means for ANOVA | f = SD of the group means / within-group SD |
| Eta squared | f = sqrt(eta² / (1 − eta²)) |
| d for two groups | f = d / 2 |
| R² | f² = R² / (1 − R²) |
| d, equal groups | r = d / sqrt(d² + 4) |
| r | d = 2r / sqrt(1 − r²) |
| Odds ratio | d ≈ ln(OR) × sqrt(3) / π |
| Paired design from a between-subjects d | dz = d / sqrt(2(1 − ρ)), where ρ is the correlation between the paired measures |

When ρ is unknown, 0.5 is a common planning value; report it as an assumption and show the result for 0.3 and 0.7.

## 3. Where the effect size should come from

| Source | Strength | Caution |
|---|---|---|
| Smallest effect of practical importance | Best: ties the study to a decision | Requires a judgement that must be argued |
| Meta-analysis | Pooled over studies | Publication bias inflates it; consider the lower confidence bound |
| Several prior studies | Reasonable | Small early studies overestimate |
| One prior study | Weak | Use a deliberately smaller value |
| Pilot study | Good for feasibility and variance | Too imprecise for the effect itself |
| Convention | Last resort | Reviewers and committees see it as unjustified |

## 4. Reference sample sizes

Two-sided alpha = 0.05. Computed with the bundled script's method; rerun the script for the exact case.

| Design | Effect | Power 0.80 | Power 0.90 |
|---|---|---|---|
| Independent t test (per group) | d = 0.2 | 394 | 527 |
| | d = 0.5 | 64 | 86 |
| | d = 0.8 | 26 | 34 |
| Paired t test (pairs) | dz = 0.5 | 34 | 44 |
| One-way ANOVA, 3 groups (total) | f = 0.25 | 159 | 207 |
| Correlation | r = 0.3 | 85 | 113 |
| Chi-square, df = 1 | w = 0.3 | 88 | 117 |

Halving the effect size roughly quadruples the sample.

## 5. Adjustments

| Situation | Adjustment |
|---|---|
| Attrition | Recruit n / (1 − dropout rate) |
| Unequal groups, ratio k = n2/n1 | Total rises by (1 + k)² / (4k) relative to equal groups |
| Several primary outcomes or comparisons (m) | Bonferroni: alpha / m; rerun the calculation with the new alpha |
| Cluster sampling or cluster randomisation | Multiply by the design effect 1 + (m − 1) × ICC, where m is the average cluster size |
| Covariate adjustment (ANCOVA) | Multiply by (1 − ρ²), where ρ is the covariate-outcome correlation |
| One-sided test | Fewer needed; use only with a prespecified direction and where the opposite result would be treated as null |
| Non-parametric analysis planned | Add about 15% to the parametric n (asymptotic relative efficiency of rank tests) |
| Finite population of size N | n_adjusted = n / (1 + (n − 1)/N) for surveys estimating a proportion |

## 6. Surveys estimating a proportion

n = z² × p(1 − p) / e², with z = 1.96 for 95% confidence, p the expected proportion (0.5 if unknown), and e the margin of error.

| Margin of error | n (p = 0.5, 95%) |
|---|---|
| ±10% | 97 |
| ±5% | 385 |
| ±3% | 1068 |

Apply the finite population correction for small populations, and divide by the expected response rate to get the number to invite.

## 7. Designs the script does not cover

| Design | Use |
|---|---|
| Repeated-measures and mixed ANOVA | G*Power; simulation |
| Multiple regression | G*Power (f²); rule-of-thumb minimums are weak substitutes |
| Logistic regression | Events-per-variable guidance plus dedicated formulas or simulation |
| Mixed and multilevel models | Simulation (for example `simr` in R) |
| Survival analysis | Number of events drives power; dedicated formulas |
| Structural equation models | Simulation or RMSEA-based methods |
| Equivalence and non-inferiority | Dedicated formulas with the margin stated |

## 8. Writing the justification

Include: the primary outcome and test, the effect size with its source, alpha, power, sidedness, the resulting n, the adjustments made, and the software. Add one sentence on what effect the study cannot detect.

## 9. What not to do

- Choose the effect size that yields the sample you already have.
- Report "post hoc power" from the observed effect.
- Power only the primary outcome and then interpret subgroup tests as if they were powered.
- Treat a non-significant result from a small study as evidence of no effect.
