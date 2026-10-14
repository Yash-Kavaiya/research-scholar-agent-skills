# Ablation plan: <method name>

**Main metric:** <metric, direction>   **Datasets:** <...>   **Seeds:** <n>   **Scale:** <full / reduced: ...>

## Components and claims

| Component | Contribution of this paper? | Claim it supports | Ablation type | Variant definition |
|---|---|---|---|---|
| <A> | yes / inherited | <...> | remove / replace / vary / add | <exact change> |

## Structure

<leave-one-out | additive (order: ...) | factorial for A × B | sweeps for ...>

## Controls

| Factor | Held fixed or adjusted |
|---|---|
| Parameter count | <matched by ... / reported> |
| Training budget | <...> |
| Retuned hyperparameters | <which, budget> |
| Data and splits | identical |
| Seeds | identical set |

## Runs

| ID | Variant | Change from full | Seeds | Datasets | Cost per run | Total | Expected direction |
|---|---|---|---|---|---|---|---|
| F | Full | none | | | | | reference |
| A0 | w/o A | <...> | | | | | drop |

Total cost: <h>   Budget: <h>

## Results table (fill only from completed runs)

| Variant | A | B | C | <Metric> (mean ± sd) | Δ vs full | Params |
|---|---|---|---|---|---|---|
| Full | ✓ | ✓ | ✓ | | 0 | |
| w/o A | – | ✓ | ✓ | | | |
| w/o B | ✓ | – | ✓ | | | |
| w/o C | ✓ | ✓ | – | | | |
| Baseline | – | – | – | | | |

## Interpretation (after runs)

| Component | Finding | Supported claim |
|---|---|---|
