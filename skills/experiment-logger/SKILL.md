---
name: experiment-logger
description: Keeps a lab notebook for experiments by recording each run's name, configuration, metrics, git commit, and notes in an append-only log, recording decisions with their reasons, and rendering a Markdown notebook. Use when the user says "log this run", "keep track of my experiments", "which config gave the best result", "what changed between run 3 and run 7", "record why we dropped this idea", "set up a lab notebook", or has finished a run whose results should not be lost.
---

# Experiment Logger

Record what was run, with which settings, what came out, and why the next step was chosen. The log is the evidence behind every number in the paper.

## When to use

- At the start of experimental work, to set up the log.
- After every run, sweep, or analysis that produces a result.
- When a decision is made: an idea dropped, a setting fixed, a bug found.
- When writing up and looking for the run behind a number.

Hand off instead for planning what to run (`experiment-planner`) or reading what the results mean (`results-interpreter`).

## Inputs

- Run name and purpose.
- Configuration: hyperparameters, dataset, seed. A JSON config file is best.
- Metrics, with the split they were measured on.
- Paths to artifacts: checkpoints, plots, output files.
- For decisions: what was decided and the evidence.

## Workflow

1. **Set up once.** The log lives in the project at `experiments/log.jsonl`. Commit it to version control. If the team already uses a tracker (Weights & Biases, MLflow, TensorBoard), keep using it for curves and use this log for the run index and the decisions, with the tracker's run URL as an artifact.
2. **Record each run** as soon as it finishes, including failed ones:

   ```bash
   python scripts/log_run.py add --name baseline-resnet50 \
     --config lr=0.1 --config epochs=90 --config seed=0 \
     --metric val_top1=76.1 --metric test_top1=75.8 \
     --tags baseline --note "Reference run with the paper's schedule" \
     --artifact runs/baseline/ckpt.pt
   python scripts/log_run.py add --name sweep-03 --config-file configs/sweep03.json \
     --metric val_top1=77.4 --status completed
   python scripts/log_run.py add --name sweep-04 --config-file configs/sweep04.json \
     --status failed --note "NaN loss at step 1200 with lr=1.0"
   ```

   The script assigns an id, adds a timestamp, and records the git commit, branch, and whether the working tree had uncommitted changes. Use `--log PATH` before the subcommand for a different log file. Nested config files are flattened to dotted keys.
3. **Record decisions** when they are made:

   ```bash
   python scripts/log_run.py decision "Dropping label smoothing: no gain over 3 seeds (runs 4-6, mean diff 0.1, sd 0.3)"
   ```

   A good decision entry names the evidence (run ids) and the alternative that was rejected.
4. **Query the log:**

   ```bash
   python scripts/log_run.py best --metric val_top1 --mode max
   python scripts/log_run.py compare 3 7        # config and metric differences between two runs
   ```

5. **Render the notebook** for reading and for supervisor meetings:

   ```bash
   python scripts/log_run.py render             # writes experiments/NOTEBOOK.md
   ```

6. **Correct by appending.** Entries are never edited or deleted. If a run was logged with a wrong metric, add a decision entry saying so and log the corrected run again.
7. **Before writing the paper**, map every number in every table to a run id, and store that mapping with the paper.

## Output format

Each line of `experiments/log.jsonl` is one entry:

```json
{"id": 7, "time": "2026-03-04T15:12:09+05:30", "type": "run", "name": "sweep-03", "status": "completed",
 "config": {"lr": 0.01, "epochs": 90, "seed": 0}, "metrics": {"val_top1": 77.4},
 "tags": ["sweep"], "note": "", "artifacts": [], "git": {"commit": "a1b2c3d", "dirty": false, "branch": "main"}}
{"id": 8, "time": "...", "type": "decision", "text": "Fix lr=0.01 for all later runs (runs 5-7)"}
```

`NOTEBOOK.md` contains a runs table (id, date, name, status, one column per metric, commit, tags) followed by a chronological log of runs and decisions.

## Quality bar and pitfalls

- Log only what happened. Metrics are copied from the run's output, never typed from memory or rounded up.
- Log failed and negative runs. The record of what did not work prevents repeating it and belongs in the paper's honest account.
- A run logged with a dirty working tree (`*` after the commit) cannot be reproduced exactly from the commit. Commit before running anything that may be reported.
- Always record the seed and the dataset version or split.
- Name the split in the metric (`val_`, `test_`). Selecting on test metrics is a methodological error the log should make visible.
- Do not put secrets, API keys, or personal data in configs or notes; the log is committed.
- One entry per run. Averages over seeds are computed from the entries, not logged in place of them.

## Related skills

- `experiment-planner` defines the runs this log records.
- `ablation-study-designer` runs are logged with a shared tag.
- `paper-to-code-reproducer` logs reproduction runs and assumptions here.
- `results-interpreter` reads the log to produce findings.
- `reproducibility-checklist` draws on the recorded configs, seeds, and commits.
- `research-progress-tracker` summarises the log for supervisor meetings.
- `latex-table-generator` typesets results exported from the log.
