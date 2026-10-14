# Table design rules and advanced LaTeX patterns

## 1. Principles

- Booktabs rules only: `\toprule`, `\midrule`, `\bottomrule`, `\cmidrule`.
- No vertical lines; use whitespace and column groups.
- Caption above the table.
- Numbers right-aligned or decimal-aligned; text left-aligned.
- Units in the header, not repeated in cells.
- Same decimals within a column; no more precision than the measurement supports.
- Mark the best value per column, including when it is a baseline.
- State metric direction (↑ or ↓) in the header or caption.

## 2. Column groups

```latex
\begin{tabular}{lcccc}
  \toprule
  & \multicolumn{2}{c}{Dataset A} & \multicolumn{2}{c}{Dataset B} \\
  \cmidrule(lr){2-3} \cmidrule(lr){4-5}
  Method & Acc. $\uparrow$ & F1 $\uparrow$ & Acc. $\uparrow$ & F1 $\uparrow$ \\
  \midrule
  ...
  \bottomrule
\end{tabular}
```

## 3. Row groups

```latex
\midrule
\multicolumn{5}{l}{\textit{Supervised}} \\
Method 1 & ... \\
Method 2 & ... \\
\midrule
\multicolumn{5}{l}{\textit{Self-supervised}} \\
...
```

Or `\multirow{2}{*}{Group}` from the `multirow` package for a label spanning rows.

## 4. Decimal alignment with siunitx

```latex
% \usepackage{siunitx}
\begin{tabular}{l S[table-format=2.1] S[table-format=2.2(2)]}
  \toprule
  Method & {Acc.} & {Error} \\
  \midrule
  A & 81.3 & 12.40(15) \\
  B & 84.1 & 9.80(20) \\
  \bottomrule
\end{tabular}
```

Wrap non-numeric header cells in braces. For bold inside `S` columns, use `\bfseries` with the `detect-weight` option (siunitx v3: `\sisetup{detect-weight, mode=text}`), or switch that cell to text.

## 5. Notes below the table

```latex
% \usepackage{threeparttable}
\begin{table}[t]
\centering
\begin{threeparttable}
\caption{...}
\begin{tabular}{lcc}
  ...
  Method X\tnote{a} & ... \\
  ...
\end{tabular}
\begin{tablenotes}\footnotesize
  \item[a] Reported by the original authors under a different split.
\end{tablenotes}
\end{threeparttable}
\end{table}
```

## 6. Fitting width

| Step | Action |
|---|---|
| 1 | Shorten headers; define abbreviations in the caption |
| 2 | Reduce decimals |
| 3 | Move secondary columns to an appendix table |
| 4 | `\setlength{\tabcolsep}{4pt}` locally |
| 5 | `table*` for full width in two-column layouts |
| 6 | Rotate with `sidewaystable` (rotating package) for very wide tables in journals |
| 7 | `\resizebox{\columnwidth}{!}{...}` only as a last resort; it shrinks the font |

## 7. Captions

Pattern: what the table reports; the metric and direction; what bold and underline mean; what ± means and over how many runs; where non-comparable numbers come from.

> Test accuracy (%) on three benchmarks. Higher is better. Best results in bold, second best underlined. Mean ± standard deviation over five seeds. † Reported by the original authors.

## 8. Typical table types

| Table | Rows | Columns |
|---|---|---|
| Main results | Methods, baselines first, ours last | Benchmarks and metrics |
| Ablation | Full model, then variants | Components (✓ / –), metric, delta |
| Dataset statistics | Datasets | Size, classes, splits, domain |
| Hyperparameters | Parameters | Values per dataset |
| Cost | Methods | Parameters, FLOPs, latency, memory |
| Literature comparison | Papers | Properties (✓ / ✗) |

## 9. Common mistakes

| Mistake | Fix |
|---|---|
| Bolding by hand and missing a lower-is-better column | Let the script mark best values |
| Mixing numbers from different protocols in one column | Footnote or separate |
| Inconsistent decimals | Use `--decimals` |
| Table too wide | Steps in section 6 |
| Caption below the table | Move above |
| Missing values left blank | Use "--" with a note |
