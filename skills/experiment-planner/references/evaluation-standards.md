# Evaluation standards for computational experiments

## 1. Claim to experiment

| Claim type | Experiment that supports it | Result that would refute it |
|---|---|---|
| "Better than prior methods" | Main comparison on standard benchmarks under one protocol | No gain beyond seed variance, or gain only against weak baselines |
| "Component X is why" | Ablation removing or replacing X | Performance unchanged without X |
| "More efficient" | Accuracy against cost (time, memory, parameters, energy) at matched quality | Savings disappear at equal accuracy |
| "Robust" | Shifted, noisy, adversarial, or out-of-distribution test sets | Larger drop than baselines |
| "General" | Several datasets, domains, model sizes | Gain on one dataset only |
| "Scales" | Varying data or model size | Gain shrinks as scale grows |
| "Works with less supervision" | Varying label fraction | Gap closes or reverses at full data |

## 2. Baselines

Include one from each row.

| Baseline | Purpose |
|---|---|
| Strongest published method on the benchmark | Shows the result matters |
| Most widely used method | Familiar reference point |
| Simple baseline (linear model, nearest neighbour, heuristic, majority class) | Shows the task is not trivial and the complexity is needed |
| Your method minus the new idea | Isolates the contribution |
| Oracle or upper bound, if one exists | Shows the remaining headroom |

Fairness rules: the same data, preprocessing, and evaluation code; the same tuning budget (number of configurations tried) for every method; the same compute class. If published numbers are used, they must come from the identical protocol, and the table must say they were not rerun.

## 3. Data hygiene

| Rule | Check |
|---|---|
| Three-way split | Train to fit, validation to select, test to report once |
| No leakage | No duplicate or near-duplicate items across splits; no test information in preprocessing statistics; group-wise splits for grouped data (patients, users, documents) |
| Time order | For temporal data, test on later periods than training |
| Pretraining overlap | Check whether the test set appears in the pretraining corpus |
| Standard splits | Use the published split when one exists; publish yours otherwise |

## 4. Metrics

| Task | Common metrics | Notes |
|---|---|---|
| Classification | Accuracy, macro and micro F1, AUROC, AUPRC | Use macro F1 or AUPRC under class imbalance |
| Regression | MAE, RMSE, R² | Report in the target's units |
| Ranking and retrieval | MRR, nDCG@k, Recall@k, MAP | State k |
| Generation | BLEU, ROUGE, chrF, learned metrics, human evaluation | Automatic metrics correlate imperfectly with quality; state the implementation |
| Segmentation and detection | IoU, Dice, mAP | State thresholds |
| Calibration | ECE, Brier score | When probabilities are used downstream |
| Efficiency | Parameters, FLOPs, latency, throughput, peak memory, training hours | State hardware and batch size |
| Fairness | Performance gaps across groups | Define groups in advance |

Use the benchmark's official evaluation script where one exists.

## 5. Variance and significance

| Decision | Guidance |
|---|---|
| Number of seeds | Three at minimum, five or more when gaps are small or training is unstable |
| What to report | Mean and standard deviation, or a confidence interval; the number of runs |
| Comparing two methods on the same test items | Paired test: paired bootstrap, McNemar (classification), or paired t test over items or seeds |
| Many comparisons | Correct for multiplicity or state that results are exploratory |
| Checkpoint selection | Fixed rule decided in advance (last, or best on validation) |

A difference smaller than the seed-to-seed standard deviation is not evidence of improvement.

## 6. Hyperparameter search

State for every method: the parameters searched, the ranges, the method (grid, random, Bayesian), the number of trials, and the selection criterion. Report sensitivity to the one or two parameters that matter most.

## 7. Budget arithmetic

```
cost of one run          = wall-clock hours × number of GPUs      (from a timed pilot)
main experiments         = methods × datasets × seeds × cost
hyperparameter search    = trials × methods × datasets × cost at reduced scale
ablations and analyses   = variants × datasets × seeds × cost
total                    = (sum of the above) × 1.3                (failed and repeated runs)
```

Time the pilot on the real hardware with the real data loader. Estimates from other papers' hardware are unreliable.

## 8. Prioritisation

| Priority | Definition | Examples |
|---|---|---|
| P0 | The paper cannot be submitted without it | Main comparison; the ablation of the central idea |
| P1 | Reviewers will ask | Second dataset, sensitivity analysis, cost table |
| P2 | Strengthens the paper | Extra domains, qualitative examples, scaling curves |

Run P0 first at full rigour. Set a checkpoint after the first main result: continue, change direction, or stop.

## 9. Analyses reviewers expect

- Ablation of each claimed component.
- Sensitivity to key hyperparameters.
- Error analysis: where the method fails, with examples.
- Performance by subgroup, difficulty, or input length.
- Cost: training and inference.
- Qualitative examples chosen by a stated rule, not hand-picked successes.

## 10. Reporting checklist to plan for

Data sources and licences, splits, preprocessing, model details, all hyperparameters, search procedure, seeds, hardware, runtime, evaluation code, and the number of runs behind every number.
