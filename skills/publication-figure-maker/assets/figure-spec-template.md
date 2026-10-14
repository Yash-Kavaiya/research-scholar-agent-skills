# Figure spec: <figure label>

**Message (one sentence):** <...>
**Venue and width:** <venue>, one column | full width   **Size:** <width × height in>
**Data:** <file, columns, runs per point>   **Script:** <path>

## Design

| Item | Choice |
|---|---|
| Chart type | <...> |
| x | <quantity (unit)>, linear / log |
| y | <quantity (unit)>, linear / log, starts at <...> |
| Series | <name: colour, marker, line style> |
| Uncertainty | <SD / SE / 95% CI over n runs>, as bars / bands |
| Panels | <single / small multiples: ...> |
| Highlight | <series or region> |
| Legend | <position / direct labels> |

## Caption

> <what is plotted; conditions; what uncertainty shows; takeaway>

## LaTeX

```latex
\begin{figure}[t]
  \centering
  \includegraphics{figures/<name>}
  \caption{<caption>}
  \label{fig:<label>}
\end{figure}
```

## Checks

- [ ] Rendered at final size and inspected at 100%
- [ ] Fonts embedded, no Type 3
- [ ] Readable in greyscale
- [ ] Same method colours as other figures
- [ ] Values match the data file
