---
name: paper-comparison-matrix
description: Builds a table comparing several papers on method, dataset, metrics, results, and limitations, with each cell taken from the paper and unreported values marked. Use when the user asks to "compare these papers", "make a comparison table", "build a literature matrix", "create a synthesis matrix", "summarize these studies in a table", or needs a state-of-the-art table for a review or related-work section.
---

# Paper Comparison Matrix

Line up N papers on the same dimensions so differences and patterns are visible. The table is a reading aid first and a manuscript table second.

## When to use

- Three or more papers on the same problem need comparing.
- A literature review or related-work section needs a summary table.
- Choosing a baseline or method to build on.

Hand off instead for one paper (`paper-summarizer`) or for prose synthesis (`literature-review-writer`).

## Inputs

- The papers: PDFs, links, or a list from `paper-search`. Full text is needed for results and setup.
- The purpose of the comparison, which decides the columns.
- Output format: Markdown (default), CSV, or LaTeX.

## Workflow

1. **Choose columns from the purpose.** Start from the set for the study type and trim to what matters. Six to nine columns is readable.

   | Study type | Columns |
   |---|---|
   | ML or computational | Paper, Year, Task, Method (core idea), Dataset(s), Metric(s), Main result, Baselines compared, Code available, Limitation |
   | Clinical or experimental | Study, Year, Design, Population (N), Intervention, Comparator, Outcome, Effect (with CI), Follow-up, Risk of bias |
   | Qualitative or social science | Study, Year, Context, Sample, Design, Data collection, Analysis approach, Key themes, Limitation |
   | Systems or engineering | Paper, Year, Problem, Architecture, Workload, Metric, Result, Scale, Open source |

2. **Define each column** in one line before filling, so every row is filled the same way ("Main result = the headline number on the most common benchmark").
3. **Fill row by row from the paper**, noting the source location of each number. Use `NR` for "not reported" and `n/a` for "not applicable". Never leave a cell blank or guess.
4. **Make results comparable or say they are not.** Before putting numbers in one column, confirm the same dataset, split, metric definition, and evaluation protocol. Otherwise add a column for the difference or a footnote.
5. **Order the rows** meaningfully: chronologically, by method family, or by result. Add a group header row per family when there are more than 8 papers.
6. **Write the reading** under the table: 3 to 6 observations that the table makes visible, such as common datasets, a metric nobody reports, results that conflict, and conditions nobody tests.
7. **Export.** For LaTeX, save as CSV and pass to `latex-table-generator`.

## Output format

```markdown
## Comparison: <topic> (<N> papers)
Column definitions: Method = ...; Main result = ...; NR = not reported.

| Paper | Year | Method | Dataset | Metric | Main result | Code | Limitation |
|---|---|---|---|---|---|---|---|
| Author et al. [1] | 2023 | ... | ... | F1 | 87.2 (Tab. 3) | yes | ... |

Notes
- a: evaluated on a different split; not directly comparable.

## What the table shows
1. ...

## Gaps visible in the table
- ...
```

## Quality bar and pitfalls

- Every cell comes from the paper. `NR` is correct and useful; an invented value is a fabrication.
- Do not rank papers by numbers measured under different protocols. This is the most common error in such tables.
- Keep cells short (a phrase or a number). Long explanations go in notes under the table.
- Use the same unit, decimal places, and metric direction throughout a column.
- Report each paper's own numbers for its own method. Numbers a paper reports for its competitors are often lower than the competitors' own.
- State the selection: how these N papers were chosen and what was left out.
- If only abstracts were available for some rows, mark those rows.

## Related skills

- `paper-search` and `citation-graph-explorer` to choose the papers.
- `paper-summarizer` for per-paper notes that feed the rows.
- `latex-table-generator` to typeset the matrix.
- `literature-review-writer` and `related-work-writer` to write the synthesis around it.
- `research-gap-finder` uses the empty and `NR` cells as gap candidates.
- `systematic-review-prisma` uses the matrix as its data-extraction table.
