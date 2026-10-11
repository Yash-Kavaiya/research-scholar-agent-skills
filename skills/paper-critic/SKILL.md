---
name: paper-critic
description: Reads a research paper critically and reports weak assumptions, missing baselines, statistical problems, and threats to validity, each tied to a specific place in the paper and rated by severity. Use when the user asks to "critique this paper", "what are the weaknesses of this paper", "can I trust these results", "is this methodology sound", "prepare me for journal club", or needs a critical appraisal of someone else's work.
---

# Paper Critic

Assess whether a paper's evidence supports its claims. Every criticism must point at something specific in the paper and explain what it changes about the conclusions.

## When to use

- Deciding how much to rely on a paper.
- Journal club, reading group, or a critical appraisal assignment.
- Writing a formal review of someone else's submission.

Hand off instead for a neutral summary (`paper-summarizer`) or for stress-testing the user's own draft before submission (`self-peer-reviewer`).

## Inputs

- Full text of the paper, including appendix and supplementary material when available.
- The user's purpose: build on it, cite it, review it, or teach it.
- Field, which decides the checklist in step 3.

## Workflow

1. **List the claims.** Write down each claim made in the abstract, introduction, and conclusion. Number them. The critique is organised around these.
2. **Map evidence to claims.** For each claim, find the experiment, analysis, proof, or citation offered for it. A claim with no evidence, or evidence weaker than the claim's wording, is your first finding.
3. **Run the validity checks** for the paper type:

   | Area | Questions |
   |---|---|
   | Internal validity | Confounds? Was the comparison fair (same data, tuning budget, compute)? Randomisation and blinding? Leakage between train and test? |
   | Baselines | Are the strongest current baselines included? Were they tuned or copied from old papers? Is there a simple baseline? |
   | Statistics | Sample size, number of seeds or runs, variance reported, tests appropriate, multiple comparisons corrected, effect sizes given? |
   | Measurement | Do the metrics capture the claimed property? Any validated instrument? Ceiling effects? |
   | External validity | How many datasets, populations, or settings? Are they representative of the claimed scope? |
   | Ablations | Is the gain attributed to the right component? Is anything bundled together? |
   | Assumptions (theory) | Which are needed, are they realistic, and where do the proofs use them? |
   | Reproducibility | Code, data, hyperparameters, preregistration? |
   | Reporting | Selective reporting, cherry-picked examples, claims in the abstract absent from the results? |

4. **Rate each issue**: *critical* (a main claim does not follow), *major* (a claim is weakened or its scope narrows), *minor* (clarity or completeness).
5. **Say what would fix it**: the experiment, analysis, or rewording that would resolve the issue.
6. **Record strengths** with the same specificity. A critique that lists only faults misjudges the paper.
7. **Give the bottom line**: which claims stand, which stand with a narrower scope, and which are unsupported.

## Output format

```markdown
# Critical reading: <Title> (<authors>, <year>)

## Claims and support
| # | Claim | Evidence offered | Supported? |
|---|---|---|---|
| 1 | ... | Table 2, §5.1 | yes / partly / no |

## Strengths
- ... (where in the paper)

## Issues
### Critical
- **<issue>** (§/Table/Fig). Why it matters: ... What would resolve it: ...
### Major
### Minor

## Bottom line
What can be relied on, and under which conditions.

## Questions for the authors
1. ...
```

## Quality bar and pitfalls

- Locate every criticism: section, table, figure, or equation. Unlocated criticism cannot be checked.
- Verify before asserting absence. "No variance reported" requires having looked in the appendix.
- Criticise what the paper claims, not what you wish it had studied. Missing scope is a limitation only if the paper claims that scope.
- Distinguish "not shown" from "false". Most weaknesses are insufficient evidence.
- Do not demand experiments that are impossible for the setting (a new clinical trial, industrial-scale compute) without saying so.
- Name the baseline you think is missing, and check it existed before the paper's submission date.
- Keep tone professional. The target is the work.

## Related skills

- `paper-summarizer` to establish what the paper says before judging it.
- `math-and-equation-explainer` to check a derivation step by step.
- `statistical-test-selector` to confirm whether the paper's test was appropriate.
- `self-peer-reviewer` applies the same scrutiny to the user's own draft.
- `paper-comparison-matrix` to see how the paper's setup compares with its neighbours.
