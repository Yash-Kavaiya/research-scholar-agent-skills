# Table spec: <table label>

**Purpose:** main results | ablation | statistics | hyperparameters | cost | comparison
**Placement:** one column (`table`) | full width (`table*`)
**Source CSV:** <path>   **Generated from runs:** <provenance file or run ids>

## Columns

| Column | Content | Direction | Decimals | Mark best? |
|---|---|---|---|---|
| Method | row label | n/a | n/a | n/a |
| <Metric 1> | <...> | higher / lower is better | <n> | yes |
| <Params (M)> | <...> | n/a | <n> | no |

## Rows

- Order: <baselines by year, then ours>
- Rule before: <row label>
- Groups: <...>

## Command

```bash
python scripts/csv_to_booktabs.py <csv> --caption "<...>" --label tab:<label> \
  --lower-is-better "<cols>" --no-bold "<cols>" --decimals <n> --second --arrows \
  --midrule-before "<label>" --out <file.tex>
```

## Caption

> <what; metric and direction; bold and underline meaning; ± meaning and n; sources of non-comparable numbers>

## Manual edits after generation

- <column groups, notes, siunitx alignment>

## Checks

- [ ] Every value matches the CSV
- [ ] Best values correct for each direction
- [ ] Compiles; fits the width
- [ ] Non-comparable numbers marked
