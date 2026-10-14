# Reproduction protocol

## 1. Specification checklist

Extract every item with its location in the paper. Mark missing items "unspecified".

| Area | Items |
|---|---|
| Data | Source and version; download date; filtering; train, validation, test split sizes and seeds; preprocessing and normalisation statistics; augmentation and its probabilities; tokeniser and vocabulary; maximum length; class mapping |
| Model | Architecture diagram and equations; layer sizes; activations; normalisation type and placement; dropout locations and rates; initialisation; positional encoding; parameter count |
| Objective | Each loss term; weights between terms; label smoothing; regularisation; temperature and margins |
| Optimisation | Optimiser and its betas or momentum; learning rate; schedule (warm-up, decay, restarts); batch size (per device and global); gradient accumulation; epochs or steps; weight decay and which parameters it excludes; gradient clipping; mixed precision; EMA |
| Evaluation | Metric and its implementation; checkpoint selection rule; test-time augmentation; decoding settings (beam size, temperature); number of runs reported; whether results are mean, median, or best |
| Compute | Hardware, number of devices, training time |
| Randomness | Seeds; nondeterministic operations |

## 2. Where hidden details usually are

| Detail | Look in |
|---|---|
| Hyperparameters | Appendix tables; supplementary material; config files in the repository |
| Preprocessing | The cited predecessor paper; the dataset's standard pipeline |
| Evaluation protocol | Footnotes of the results table; the benchmark's official script |
| Tricks that matter | Ablation tables; implementation-details paragraphs; code comments |
| Corrections | Later arXiv versions; errata; issues on the code repository |

## 3. Resolving unspecified details

Use the first source available, and log each decision.

1. The official code (read even if not reused; check its licence).
2. The authors' earlier paper or the method it extends.
3. The benchmark's standard practice in papers from the same period.
4. The framework's default.
5. A justified choice, tested both ways if cheap.

Assumptions log columns: item, choice, source of the choice, expected effect if wrong, tested.

## 4. Unit tests that catch common errors

| Test | Expected | Catches |
|---|---|---|
| Output shapes on a tiny batch | Match the specification | Wrong reshapes, broadcasting |
| Parameter count | Within about 1% of the paper | Wrong sizes, missing or extra layers |
| Initial loss on random data | About ln(C) for C-class cross-entropy; about the target variance for MSE | Bad initialisation, wrong loss scaling |
| Overfit one batch | Loss near zero within a few hundred steps | Broken gradients, frozen layers, wrong optimiser wiring |
| Gradient check on a custom operation | Matches finite differences | Wrong derivatives |
| Equation tests | Hand-computed values match | Misread formula |
| Metric check | Matches a reference implementation on known inputs | Metric bugs (averaging, thresholds) |
| Determinism | Same seed gives the same result twice | Uncontrolled randomness |
| Data pipeline | Visualise samples after augmentation; label counts per split | Label shifts, augmentation bugs, leakage |

## 5. Scaling up

1. Small model, small data subset, short schedule: confirm the loss falls and metrics move.
2. Full data, short schedule: compare the learning curve's early shape with any curve in the paper.
3. Full configuration, one seed.
4. Remaining seeds.

Log every run with config, seed, and commit.

## 6. Interpreting the comparison

| Outcome | Definition | Report as |
|---|---|---|
| Reproduced | Within the paper's reported variance, or within a small margin set before running | "Reproduced" with numbers |
| Close | Same ordering of methods and conclusions; small numeric gap outside variance | "Close; gap of x" with likely causes |
| Not reproduced | Conclusions change or the gap is large | "Not reproduced" with what was checked |
| Reduced scale | Could not run the paper's scale | "Partial reproduction at reduced scale"; state what can and cannot be concluded |

## 7. Diagnosing a gap

Work through in order and change one thing at a time.

| # | Suspect | Check |
|---|---|---|
| 1 | Evaluation | Same metric code, same split, same checkpoint rule, same decoding |
| 2 | Data preprocessing | Normalisation, tokenisation, filtering, resolution |
| 3 | Training length and schedule | Steps, warm-up, decay endpoint |
| 4 | Batch size and learning-rate scaling | Global batch; linear scaling rules |
| 5 | Regularisation | Weight decay exclusions, dropout placement, augmentation strength |
| 6 | Initialisation and normalisation details | Pre- or post-norm, epsilon values |
| 7 | Numerical precision | Mixed precision, loss scaling |
| 8 | Variance | More seeds; the paper may report a best run |
| 9 | Paper error | Equation versus text versus code disagreement |

## 8. Repository layout and README

```
README.md      how to install, train, evaluate; results table versus the paper; deviations
SPEC.md        the extracted specification with paper locations
ASSUMPTIONS.md every unspecified detail and the choice made
configs/       one file per experiment, every hyperparameter
src/           data, model, loss, train, evaluate
tests/         the unit tests above
requirements.txt with pinned versions
```

README results table columns: setting, paper value, reproduced mean ± sd over n seeds, difference, status.

## 9. Licences and credit

Reimplementing from a paper is normal practice. Copying code requires the original licence to permit it and attribution. Datasets keep their own licences. Cite the paper and, if used, the official code.

## 10. Contacting authors

Ask specific, answerable questions in one short email: the exact detail missing, what you tried, and the gap you observe. Thank them and offer to share the reproduction.
