# Reproduction: <paper title> (<authors>, <year>)

**Target:** <Table or Figure n>, <metric> on <dataset, split>
**Official code:** <link and licence | none found>
**Framework and versions:** <...>   **Hardware:** <...>

## How to run

```bash
pip install -r requirements.txt
python -m src.train --config configs/<name>.yaml --seed 0
python -m src.evaluate --checkpoint <path> --split test
```

## Results

| Setting | Paper | Reproduced (mean ± sd, n seeds) | Difference | Status |
|---|---|---|---|---|
| <...> | <value> | <value ± sd, n> | <...> | reproduced / close / not reproduced / reduced scale |

## Specification summary

| Item | Value | Source |
|---|---|---|
| <learning rate> | <...> | <paper Table n / code / assumption A3> |

## Assumptions log

| ID | Unspecified item | Choice | Source of choice | Expected effect if wrong | Tested |
|---|---|---|---|---|---|
| A1 | <...> | <...> | <official code / predecessor / convention / judgement> | <...> | yes / no |

## Deviations from the paper

- <scale, data version, hardware, anything changed and why>

## Gap diagnosis

| Suspect | What was checked | Finding |
|---|---|---|

## Tests

- <list of unit tests and their status>

## Credits

- Paper: <citation>
- Code reused: <none / repository, licence>
- Data: <dataset, licence>
