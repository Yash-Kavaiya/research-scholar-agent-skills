---
name: experiment-planner
description: Plans experiments before they are run, defining hypotheses, variables, controls, baselines, datasets and splits, metrics, seeds and statistical comparison, ablations, and a compute and time budget in priority order. Use when the user asks to "plan my experiments", "design the evaluation", "what baselines should I compare against", "what experiments do reviewers expect", "estimate the compute I need", or is about to start running experiments for a paper.
---

# Experiment Planner

Decide what will be run, why, and at what cost before any compute or lab time is spent. Each experiment exists to support or refute a specific claim.

## When to use

- Before starting the experimental work for a paper or thesis chapter.
- When a deadline or budget forces choosing which experiments to run.
- When reviewers asked for more experiments and the response needs a plan.

Hand off instead for overall study design with human participants (`methodology-designer`) or the detailed ablation table (`ablation-study-designer`).

## Inputs

- The claims the paper intends to make, in order of importance.
- The method and what is new in it.
- Resources: hardware, GPU hours or lab time, people, deadline.
- Target venue, which sets the expected evaluation standard.
- Existing results, code, and datasets.

## Workflow

1. **Map claims to experiments.** Write each claim as a testable statement and list the experiment that would support it and the result that would refute it. Drop experiments that support no claim.
2. **Define variables.**
   - Independent: what you vary (method, component, hyperparameter, data size).
   - Dependent: metrics, with direction and unit.
   - Controlled: everything held equal across compared conditions (data, preprocessing, tuning budget, compute, seeds).
   - Confounds: differences that could explain the result other than your method (parameter count, pretraining data, training time).
3. **Choose baselines.** Include: the strongest published method on this benchmark; the most widely used method; a simple baseline (linear model, heuristic, previous version); and your method without its new part. Plan to tune baselines with the same budget as your method, or cite their published numbers under the same protocol.
4. **Choose datasets and splits.** At least two datasets when claiming generality. Fix train, validation, and test splits; use standard splits where they exist. Model selection uses validation only. Check for leakage (`dataset-finder` helps locate candidates).
5. **Choose metrics.** The field's standard metric first, then metrics for the property you claim (robustness, efficiency, calibration, fairness). Report cost metrics (parameters, FLOPs, latency, training time) when claiming efficiency.
6. **Plan for variance.** Fix the number of seeds (3 to 5 minimum for stochastic training) and the statistical comparison: mean with standard deviation or confidence interval, and a test when differences are small (`statistical-test-selector`).
7. **Plan ablations and analyses** (`ablation-study-designer`): component removal, sensitivity to key hyperparameters, scaling behaviour, failure cases, qualitative examples.
8. **Budget.** Estimate cost per run from a timed pilot, then multiply: configurations × datasets × seeds. Add the hyperparameter search and a 30% margin for failed and repeated runs.
9. **Prioritise.** Label each experiment P0 (the paper cannot be submitted without it), P1 (reviewers will ask), or P2 (nice to have). Schedule P0 first and set a go/no-go checkpoint after the first main result.
10. **Set up logging** before the first run (`experiment-logger`): config, seed, commit, metrics.

## Output format

```markdown
## Claims and experiments
| # | Claim | Experiment | Supports if | Refutes if | Priority |

## Setup
- Datasets and splits: ...
- Baselines: ... (source of numbers: rerun | published under same protocol)
- Metrics: ...
- Controlled factors: ...
- Seeds and statistical comparison: ...

## Experiment list
| ID | Purpose | Configs × datasets × seeds | Cost per run | Total | Priority |

## Budget
Total: <GPU hours / lab days>. Available: <...>. Margin: 30%. Cut order if over budget: ...

## Timeline and checkpoints
## Risks and fallbacks
```

## Quality bar and pitfalls

- Do not invent cost estimates. Time a pilot run, or state the estimate as a guess with its basis.
- The test set is used once per reported configuration. Tuning on test data invalidates the results.
- A baseline that is not tuned, or run on a different protocol, does not support a comparison claim.
- One dataset and one seed do not support a general claim.
- Decide the analysis before seeing the results. Choosing metrics and subsets afterwards is selective reporting.
- Plan what happens if the main result is negative: which finding would still be publishable.
- If the budget does not cover P0, say so now and reduce scope (fewer datasets, smaller models) openly.

## Related skills

- `research-question-formulator` for the claims and hypotheses.
- `dataset-finder` for datasets and benchmarks.
- `ablation-study-designer` for the component analysis.
- `experiment-logger` to record runs as they happen.
- `statistical-test-selector` for comparing results across seeds.
- `results-interpreter` once the numbers are in.
- `reproducibility-checklist` to plan for what the venue will ask.
