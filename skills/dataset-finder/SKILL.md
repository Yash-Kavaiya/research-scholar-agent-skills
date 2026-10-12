---
name: dataset-finder
description: Finds datasets and benchmarks for a research task across Hugging Face, OpenML, Kaggle, the UCI repository, Papers with Code, and domain archives, and compares them by size, licence, labels, and how widely they are used. Use when the user asks "find a dataset for X", "is there a benchmark for X", "where can I get data on X", "which dataset do papers use for X", or needs to choose and justify a dataset for experiments.
---

# Dataset Finder

Locate candidate datasets, check that each one can actually be used for the purpose (licence, access, labels, size), and recommend with reasons.

## When to use

- Choosing data for an experiment, thesis, or course project.
- Identifying the standard benchmark for a task so results are comparable.

Hand off instead when the user must collect new data (`survey-questionnaire-designer`, `methodology-designer`).

## Inputs

- Task and modality (text classification, medical image segmentation, tabular regression, time series).
- Requirements: minimum size, label type, language, domain, date range.
- Use: academic or commercial, which decides acceptable licences.
- Whether comparability with prior papers matters.

## Workflow

1. **Search the hubs with an API:**

   ```bash
   python scripts/find_datasets.py "sentiment analysis" --limit 10
   python scripts/find_datasets.py "chest x-ray" --sources huggingface --format json
   python scripts/find_datasets.py "credit" --sources openml
   ```

   Hugging Face results are sorted by downloads and include licence, task, size category, and gated status. OpenML matches on dataset name only, so give it a single keyword.
2. **Search the sources without an open API** using web search or the site itself:
   - Papers with Code: datasets by task, and which papers report results on them.
   - Kaggle: `kaggle datasets list -s "<query>"` if the Kaggle CLI is configured, otherwise the website.
   - UCI Machine Learning Repository: classic tabular datasets.
   - Zenodo, Figshare, Dataverse, OSF: datasets attached to papers.
   - Google Dataset Search for everything else.
   - Domain archives: PhysioNet (clinical signals), TCIA (cancer imaging), GEO and SRA (genomics), UK Data Service and ICPSR (social science), data.gov.in and data.gov (government), LDC and ELRA (language), OpenNeuro (neuroimaging).
3. **Find what the literature uses.** Search recent papers on the task with `paper-search` and note the datasets in their experiment sections. The benchmark most papers report on is usually the one to include.
4. **Check each candidate:**
   - *Licence*: what it permits (research only, commercial, redistribution). "Not stated" means unknown, not free.
   - *Access*: open, gated, application required, or a data use agreement. Estimate how long access takes.
   - *Content*: size, classes, label source and quality, class balance, splits provided.
   - *Provenance and ethics*: how it was collected, consent, personal data, known biases, any retraction or deprecation.
   - *Documentation*: a datasheet, data card, or paper to cite.
5. **Open the dataset card or paper** for the top candidates and confirm the details. Do not rely on the search listing.
6. **Recommend** a primary dataset and one or two secondary ones, with the reason and what each lets the user claim.

## Output format

```markdown
## Candidates for <task>
| Dataset | Source | Size | Labels | Licence | Access | Used by | Fit |
|---|---|---|---|---|---|---|---|

## Recommendation
- Primary: <dataset>, because ...
- Secondary: <dataset>, for generalisation or comparison
- Avoid: <dataset>, because <licence, deprecation, leakage, quality>

## How to obtain
Commands or steps, including any application.

## Cite as
<the dataset paper, verified>

## Not verified
- <details taken from listings that still need checking on the dataset page>
```

## Quality bar and pitfalls

- Only list datasets you found. Do not describe a dataset from memory without opening its page; names, sizes, and licences are easy to get wrong.
- Popularity is not quality. Check label noise reports and known issues for widely used benchmarks.
- A missing licence does not grant permission. Flag it.
- Some well-known datasets have been withdrawn for ethical or legal reasons. Check current status before recommending.
- Medical, biometric, and personal data usually need ethics approval and a data use agreement even when "public" (`ethics-irb-drafter`).
- Watch for overlap between a candidate's test set and pretraining corpora or other training sets.
- Do not help obtain gated or restricted data by going around the access process.

## Related skills

- `paper-search` to see which datasets recent papers use.
- `experiment-planner` to fit the datasets into the evaluation plan.
- `ethics-irb-drafter` when the data involves people.
- `paper-to-code-reproducer` when reproducing a paper needs its data.
- `reproducibility-checklist` for the dataset documentation the venue asks for.
