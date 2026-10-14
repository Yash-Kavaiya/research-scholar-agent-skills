# Chart choice, styling, and pgfplots

## 1. Chart choice by message

| Message | Chart | Avoid |
|---|---|---|
| Change over an ordered variable | Line with markers | Bars for many points; unordered x |
| Compare a few categories | Bar or dot plot, sorted, starting at zero for bars | Pie, 3D, stacked bars for exact comparison |
| Compare many categories | Dot plot or horizontal bars, sorted | Vertical bars with rotated labels |
| Distribution | Histogram, density, box, violin; strip or beeswarm for small n | Mean bars without spread |
| Relationship | Scatter; add a fit only with a reason | Lines joining unordered points |
| Part of a whole | Stacked bar, with few parts | Pie with many slices |
| Matrix | Heatmap with a perceptually uniform colormap | Rainbow colormaps |
| Many small comparisons | Small multiples, shared axes | One crowded panel |
| Before and after per subject | Slope chart or paired dots | Two separate bars |
| Trade-off between two metrics | Scatter with methods labelled, the better corner marked | Two separate bar charts |

## 2. Encoding series

| Channel | Rule |
|---|---|
| Colour | Okabe-Ito or another colour-blind-safe palette; same colour for the same method across all figures |
| Marker | Different marker per series, so the figure works in greyscale |
| Line style | Solid for the proposed method, dashed or dotted for baselines, consistently |
| Direct labels | Prefer labels at line ends to a legend when there are few series |
| Emphasis | Highlight the series under discussion; mute the rest in grey |

## 3. Sizes at print scale

| Element | Size |
|---|---|
| Axis labels | Same size as the caption text (often 8–9 pt) |
| Tick labels | 1 pt smaller than axis labels, never below about 6–7 pt |
| Line width | 1–1.5 pt for data; 0.5–0.8 pt for axes |
| Markers | 3–5 pt |

Create the figure at its final physical width and include it without scaling.

## 4. Uncertainty

| Display | Use |
|---|---|
| Error bars | Discrete points; state SD, SE, or CI and n |
| Shaded band | Continuous curves |
| Box or violin | Distributions over many runs |
| Individual runs as thin lines | Few runs; shows variability honestly |

Say in the caption what the bars or bands are. SD shows spread; SE and CI show precision of the mean.

## 5. Axes

- Label every axis with the quantity and unit: "Latency (ms)".
- Bars start at zero; lines may not, but make truncation visible.
- Log scales for quantities spanning orders of magnitude; label them clearly.
- Same axis limits across panels meant to be compared.
- Avoid dual y-axes; use two panels.

## 6. Captions

Pattern: what is plotted; the conditions (data, runs); what error bars mean; the takeaway in one sentence.

> Validation accuracy during training on CIFAR-100 for three methods. Lines show the mean and shaded bands one standard deviation over five seeds. Our method reaches the baseline's final accuracy in 40% fewer epochs.

## 7. Output and fonts

- PDF (vector) for line plots and charts; PNG at 300 dpi only for raster content or slides.
- Embed TrueType fonts (`pdf.fonttype` 42); Type 3 fonts are rejected by some publishers.
- Rasterise only dense scatter layers (`rasterized=True` on that artist) to keep file size down.
- Check with `pdffonts figure.pdf`.

## 8. pgfplots equivalent

```latex
% \usepackage{pgfplots} \pgfplotsset{compat=1.18}
\begin{tikzpicture}
\begin{axis}[
  width=\columnwidth, height=0.68\columnwidth,
  xlabel={Training epochs}, ylabel={Accuracy (\%)},
  legend pos=south east, legend style={draw=none, font=\footnotesize},
  tick label style={font=\footnotesize}, label style={font=\small},
  grid=major, grid style={gray!20}]
\addplot+[mark=o, color={rgb,255:red,0;green,114;blue,178}] table[x=epoch, y=ours, col sep=comma] {data.csv};
\addplot+[mark=square, dashed, color={rgb,255:red,213;green,94;blue,0}] table[x=epoch, y=baseline, col sep=comma] {data.csv};
\legend{Ours, Baseline}
\end{axis}
\end{tikzpicture}
```

Error bands: `\addplot [name path=upper, draw=none] ...; \addplot [name path=lower, draw=none] ...; \addplot [fill=blue!15] fill between[of=upper and lower];` with `\usepgfplotslibrary{fillbetween}`.

## 9. Common problems

| Problem | Fix |
|---|---|
| Text too small after inclusion | Recreate at final width; do not scale with `width=` |
| Legend covers data | Move outside the axes or use direct labels |
| Colours indistinguishable in print | Add markers or line styles |
| Overlapping tick labels | Fewer ticks; rotate only as a last resort |
| Inconsistent styles across figures | One style module for all figures |
| Different method colours in different figures | Fix a colour map per method name |
