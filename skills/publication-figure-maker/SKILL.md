---
name: publication-figure-maker
description: Creates publication-quality plots with matplotlib or TikZ/pgfplots at the venue's exact column width, with readable fonts, embedded fonts, colour-blind-safe colours, error bars, and vector output. Use when the user asks to "make a figure for my paper", "plot these results", "make this plot publication ready", "fix my matplotlib figure for IEEE", "my figure text is too small", "convert this plot to TikZ", or needs a line, bar, box, scatter, or heatmap figure from data.
---

# Publication Figure Maker

Produce figures that are legible at printed size, honest about the data, and accepted by the publisher's production checks.

## When to use

- Results need plotting for a paper, thesis, poster, or slides.
- An existing figure has small text, wrong size, poor colours, or font-embedding problems.

Hand off instead for model and pipeline schematics (`architecture-diagram-maker`) or tables (`latex-table-generator`).

## Inputs

- The data (CSV, JSON, arrays, or the experiment log), with variance across runs if it exists.
- The message of the figure: the one comparison or trend the reader should see.
- Venue and whether the figure spans one column or the full width.
- Output needs: PDF for LaTeX, PNG for slides, greyscale-safe if the venue prints in black and white.

## Workflow

1. **State the figure's point in one sentence.** It decides the chart type and what is emphasised.
2. **Choose the chart type:**

   | To show | Use | Avoid |
   |---|---|---|
   | Trend over an ordered variable | Line plot with markers | Bars for many x values |
   | Comparison across categories | Bar chart or dot plot, sorted | Pie charts, 3D bars |
   | Distribution | Box, violin, or histogram; strip plot for small n | Bar of means alone |
   | Relationship between two variables | Scatter, with fit only if justified | Connecting unordered points |
   | Matrix (confusion, correlation, attention) | Heatmap with a perceptually uniform colormap (`viridis`, `cividis`) | `jet` and rainbow maps |
   | Many conditions | Small multiples with shared axes | One crowded panel |

3. **Set the style and size with the script:**

   ```python
   import matplotlib.pyplot as plt
   import pubstyle                      # copy scripts/pubstyle.py next to the plotting script

   pubstyle.apply("ieee")               # 8 pt fonts, thin axes, embedded TrueType fonts
   fig, ax = plt.subplots(figsize=pubstyle.figsize("ieee", columns=1))
   for i, (name, y, sd) in enumerate(series):
       ax.plot(x, y, color=pubstyle.PALETTE[i], marker=pubstyle.MARKERS[i],
               linestyle=pubstyle.LINESTYLES[i], label=name)
       ax.fill_between(x, y - sd, y + sd, color=pubstyle.PALETTE[i], alpha=0.15, linewidth=0)
   ax.set_xlabel("Training epochs"); ax.set_ylabel("Accuracy (%)"); ax.legend()
   pubstyle.save(fig, "figures/accuracy")   # accuracy.pdf (vector) and accuracy.png (300 dpi)
   ```

   ```bash
   python scripts/pubstyle.py widths                      # column and text widths per venue
   python scripts/pubstyle.py demo --venue neurips --out demo
   ```

   Venues: `ieee`, `acm`, `neurips`, `icml`, `iclr`, `acl`, `cvpr`, `springer-lncs`, `nature`, `elsevier`, `thesis-a4`. `figsize(venue, columns=2)` gives the full text width; `aspect` or `height` sets the height. Confirm the width against the current template.
4. **Create the figure at final size** and include it in LaTeX without scaling (`\includegraphics{figures/accuracy}`), so 8 pt text in the figure is 8 pt on the page.
5. **Encode redundantly.** Distinguish series by colour and by marker or line style, so the figure works in greyscale and for colour-blind readers. `PALETTE` is the Okabe-Ito set.
6. **Show uncertainty**: error bars or bands, with the caption saying what they are (standard deviation, standard error, or 95% CI) and over how many runs.
7. **Label everything**: axis labels with units, a legend or direct labels, and tick labels that are readable. No title inside the figure; the caption carries it.
8. **Write the caption**: what is plotted, the conditions, what the error bars are, and the takeaway in one sentence.
9. **Check the output.** Open the PDF at 100% zoom. Verify fonts are embedded (`pdffonts figure.pdf`: no Type 3) and the size matches the column.
10. **For TikZ/pgfplots** (when the venue or user wants native LaTeX figures), export the data to CSV and write a `pgfplots` axis with the same width, `\pgfplotsset{compat=1.18}`, and the same colours. Compile it before delivering.

## Output format

- `figures/<name>.pdf` and `figures/<name>.png`
- The plotting script, reading the data file, so the figure can be regenerated
- The caption text and the LaTeX include snippet:

```latex
\begin{figure}[t]
  \centering
  \includegraphics{figures/accuracy}
  \caption{Validation accuracy over training. Shaded bands show $\pm 1$ standard deviation over 5 seeds.}
  \label{fig:accuracy}
\end{figure}
```

## Quality bar and pitfalls

- Plot only the data provided. Never fabricate, smooth away, or omit points to improve the picture, and say so if outliers were removed.
- Bar charts start at zero. If the axis is truncated on a line plot, make it obvious.
- Do not use two y-axes to imply a relationship, or different axis ranges across panels meant for comparison.
- A mean without spread hides the result. If there is one run, say so in the caption.
- Text in the figure should be no smaller than about 6 to 7 pt at printed size.
- Rasterised plots (PNG, JPG) of line art blur in print. Use PDF or EPS; rasterise only dense scatter layers or images.
- Remove chart junk: gridlines darker than the data, boxes, shadows, redundant legends.
- Keep colours and names consistent for the same method across all figures in the paper.
- Run the script and look at the result before delivering it.

## Related skills

- `results-interpreter` decides what the figure should show.
- `statistical-test-selector` supplies intervals and significance marks.
- `experiment-logger` is the source of run data.
- `architecture-diagram-maker` for schematic figures.
- `latex-table-generator` when exact values matter more than the trend.
- `latex-paper-formatter` to place figures in the template.
- `paper-to-slides` and `paper-to-poster` reuse the figures at larger font sizes.
