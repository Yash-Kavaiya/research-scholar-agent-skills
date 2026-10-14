# Sample size justification: <study title>

## Inputs

| Item | Value | Source or reason |
|---|---|---|
| Primary outcome | <...> | |
| Primary analysis | <test> | |
| Design | <two independent groups / paired / k groups / correlation / proportions / chi-square> | |
| Effect size | <d / dz / f / r / h / w = value> | <meta-analysis, prior study, minimal important difference, convention> |
| Alpha | <0.05>, <two-sided / one-sided> | |
| Target power | <0.80 / 0.90> | |
| Allocation ratio | <1:1> | |
| Expected attrition | <%> | |
| Other adjustments | <clustering ICC and cluster size; multiple outcomes; covariates> | |

## Result

| Quantity | Value |
|---|---|
| Required per group / pairs / total | <n> |
| Achieved power at that n | <x> |
| After attrition adjustment | <n to recruit> |
| After other adjustments | <n> |

Command used: `<script command>`

## Sensitivity

| Effect size | n per group | Total N | To recruit |
|---|---|---|---|
| <smaller plausible> | | | |
| <planned> | | | |
| <larger plausible> | | | |

## Justification paragraph

> An a priori power analysis for <test> indicated that <n> participants per group (N = <total>) are needed to detect an effect of <measure> = <value> with <power>% power at a <two-sided> alpha of <alpha>. The effect size was based on <source>. Allowing for <%> attrition, <n> participants will be recruited. Calculations used noncentral distributions in SciPy.

## What this sample cannot detect

<Effects smaller than <value> will not be reliably detected; secondary and subgroup analyses are exploratory.>

## Assumptions

- <correlation between paired measures, ICC, response rate, and where each came from>
