# Experiment logging practices

## 1. What every run entry should hold

| Field | Why |
|---|---|
| Name and purpose | Which question the run answers |
| Full configuration | Reproducing the run |
| Seed | Separating variance from effects |
| Dataset and version or hash | Results depend on data |
| Code commit and dirty flag | Reproducing the exact code |
| Environment (key library versions, hardware) | Numerical differences between setups |
| Metrics by split (val_, test_) | Avoiding selection on test |
| Status (completed, failed, aborted) | Failed runs are information |
| Artifacts (checkpoints, plots, tracker URL) | Finding outputs later |
| Note | What was expected and what happened |

## 2. Decision entries

A good decision entry has: what was decided, the evidence (run ids and numbers), the alternative rejected, and the consequence for later runs.

| Weak | Strong |
|---|---|
| "Dropped label smoothing." | "Dropping label smoothing: runs 4–6 (with) vs 7–9 (without) differ by 0.1 ± 0.3 top-1; keeping the simpler setup for all later runs." |
| "Fixed a bug." | "Bug in the validation loader shuffled labels (found by checking class counts). Runs 1–12 have invalid val metrics; test metrics unaffected. Rerun 3 and 8 for the table." |

## 3. Naming

Use names that sort and read well: `<experiment>-<variant>-<seed>`, for example `abl-no-aug-s2`. Tags group runs: `baseline`, `ablation`, `sweep`, `paper-table-2`.

## 4. Append-only discipline

- Never edit or delete entries. Corrections are new entries that reference the old id.
- Log failures and aborted runs with the reason.
- Commit the log with the code so history is kept.

## 5. Reproducibility hygiene

| Practice | Reason |
|---|---|
| Commit before any run that may be reported | The commit hash then identifies the code |
| Configs in files, not only command-line flags | Full record of settings |
| Fixed seeds and deterministic flags where feasible | Repeatable results |
| Record library versions (`pip freeze` into an artifact) | Version drift changes results |
| Save evaluation outputs (predictions), not only scores | Recompute metrics or analyse errors later |

## 6. Working with other trackers

| Tool | Keep there | Keep in this log |
|---|---|---|
| Weights & Biases, MLflow, TensorBoard, Aim | Curves, system metrics, media | Run index, final metrics, decisions, tracker run URL as an artifact |
| Notebook files | Exploration | Conclusions as decision entries |
| Spreadsheet | Summary tables for meetings | Generate it from the log, not by hand |

## 7. From log to paper

Before writing, build a mapping from every number in every table and figure to run ids:

| Table | Cell | Value | Runs | Aggregation |
|---|---|---|---|---|
| Table 2 | Ours, CIFAR-10 | 95.1 ± 0.2 | 31, 32, 33 | mean ± sd |

Keep the mapping in the repository. It answers reviewer questions and protects against copying a wrong number.

## 8. Sensitive content

Do not write API keys, passwords, tokens, or personal data into configs or notes; the log is committed. Use environment variables for secrets.

## 9. Lab notebook for non-computational work

The same structure works for wet-lab or field work: date, aim, protocol version, materials and lot numbers, observations, deviations, results, decisions. Entries are dated and never altered; corrections are new entries.
