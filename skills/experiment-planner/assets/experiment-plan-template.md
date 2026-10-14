# Experiment plan: <paper or project>

**Deadline:** <date>   **Compute available:** <GPU hours, hardware>   **People:** <...>

## Claims and experiments

| # | Claim | Experiment | Supports if | Refutes if | Priority |
|---|---|---|---|---|---|
| C1 | <...> | E1 | <...> | <...> | P0 |

## Setup

| Item | Choice | Note |
|---|---|---|
| Datasets and splits | <...> | standard split: yes / no |
| Baselines | <...> | rerun / published under same protocol |
| Metrics | <...> | official script: yes / no |
| Held constant | <data, preprocessing, tuning budget, hardware> | |
| Seeds | <n> | |
| Statistical comparison | <mean ± sd; paired test> | |
| Checkpoint selection | <rule> | |
| Hyperparameter search | <parameters, ranges, trials, criterion> | same budget for all methods |

## Experiment list

| ID | Purpose | Methods × datasets × seeds | Cost per run | Total | Priority | Status |
|---|---|---|---|---|---|---|
| E1 | Main comparison | <a × b × c> | <h> | <h> | P0 | planned |
| E2 | Ablation | | | | P0 | |
| E3 | Sensitivity | | | | P1 | |

## Budget

| Item | GPU hours |
|---|---|
| Pilot timing (measured) | <h per run> |
| Main experiments | <h> |
| Hyperparameter search | <h> |
| Ablations and analyses | <h> |
| Margin (30%) | <h> |
| **Total** | <h> of <h> available |

**Cut order if over budget:** <E5, then E4, ...>

## Timeline

| Week | Work | Checkpoint |
|---|---|---|
| 1 | <...> | First main result: go / change / stop |

## Risks and fallbacks

| Risk | Sign | Fallback |
|---|---|---|
| Main result is negative | <...> | <what is still publishable> |
| Baseline cannot be reproduced | | |

## Logging

Runs recorded with: config, seed, commit, dataset version, metrics by split. Tool: <...>
