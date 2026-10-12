---
name: architecture-diagram-maker
description: Creates model architecture, pipeline, system, and workflow diagrams for papers as editable TikZ, Mermaid, Graphviz, or SVG source, with consistent shapes, labelled data flow, and sizing for the venue's column width. Use when the user asks to "draw my model architecture", "make a pipeline diagram", "create Figure 1 for my paper", "make a system overview figure", "draw a flowchart of my method", or "turn this description into a TikZ diagram".
---

# Architecture Diagram Maker

Draw a diagram that lets a reader understand the method's structure in under a minute, from source that can be edited and recompiled.

## When to use

- A paper needs an overview figure of a model, pipeline, system, or study procedure.
- An existing diagram is cluttered or does not match the method section.

Hand off instead for data plots (`publication-figure-maker`) or the PRISMA flow diagram (`systematic-review-prisma`).

## Inputs

- A description of the method: components, their order, what passes between them, and what is new. The method section or the code is the best source.
- What the diagram must convey: the one idea a reader should take away.
- Venue and width (one column or full width), and whether colour is available.
- Preferred format.

## Workflow

1. **List the elements** from the method description: inputs, processing blocks, outputs, losses or objectives, and the connections with what flows along them (tensor shapes, data types, signals). Confirm the list with the user before drawing; diagram errors usually start here.
2. **Decide the level of detail.** An overview figure shows 5 to 9 blocks. Internal detail of a block goes in a second, zoomed diagram. Highlight the novel component; draw standard components plainly.
3. **Choose the format:**

   | Format | Use when |
   |---|---|
   | TikZ | LaTeX papers; fonts match the document; precise control; the default for publication |
   | Mermaid | Drafts, READMEs, Markdown, quick iteration |
   | Graphviz (DOT) | Large graphs where automatic layout matters |
   | SVG | Slides, posters, web; later editing in Inkscape or Figma |

4. **Lay it out.** One main direction of flow (left to right, or top to bottom). Align blocks on a grid, keep spacing equal, and avoid crossing arrows. Group related blocks with a dashed or lightly shaded container.
5. **Apply a visual grammar and keep it throughout:**
   - Shape encodes type: rounded rectangle for operations or modules, plain rectangle or cylinder for data, circle for an operator (sum, concatenation), diamond for a decision.
   - Colour encodes role (for example trainable, frozen, input and output), with at most 3 or 4 colours from a colour-blind-safe set, and a second cue (border style, pattern) so it survives greyscale.
   - Solid arrows for data flow; dashed for gradients, optional paths, or training-only connections.
   - Every arrow that is not obvious gets a label.
6. **Write the source.** A TikZ starting point:

   ```latex
   % \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta,fit,backgrounds}
   \begin{tikzpicture}[node distance=6mm and 9mm, font=\footnotesize,
     block/.style={draw, rounded corners=2pt, minimum height=7mm, minimum width=16mm, align=center},
     data/.style={draw, minimum height=7mm, minimum width=12mm, align=center, fill=black!5},
     new/.style={block, fill=orange!25, thick},
     arr/.style={-{Latex[length=1.6mm]}}]
     \node[data] (x) {Input $x$};
     \node[block, right=of x] (enc) {Encoder};
     \node[new, right=of enc] (mod) {Our module};
     \node[block, right=of mod] (dec) {Decoder};
     \node[data, right=of dec] (y) {Output $\hat{y}$};
     \draw[arr] (x) -- (enc);
     \draw[arr] (enc) -- node[above] {$h$} (mod);
     \draw[arr] (mod) -- node[above] {$z$} (dec);
     \draw[arr] (dec) -- (y);
     \draw[arr, dashed] (enc.south) -- ++(0,-5mm) -| node[pos=0.25, below] {skip} (dec.south);
   \end{tikzpicture}
   ```

7. **Size it for the page.** Set font size in the diagram to match the caption size, and check the total width against the column (`\columnwidth` or `\textwidth`). Do not shrink with `\resizebox` until text is unreadable.
8. **Compile or render it** and look at the result. Fix overlaps, clipped labels, and uneven spacing.
9. **Check against the method section**: every block in the diagram is described in the text with the same name and symbol, and every component in the text that matters appears in the diagram.
10. **Write the caption**: what the diagram shows, how to read it (legend for colours and arrow styles), and what is new.

## Output format

- The diagram source (`.tex`, `.mmd`, `.dot`, or `.svg`) and the rendered PDF or PNG.
- The caption and LaTeX include snippet.
- A legend line for shapes, colours, and arrow styles.
- A short list of assumptions made about the architecture where the description was incomplete.

## Quality bar and pitfalls

- Draw what the method does. Do not add components, connections, or dimensions that were not described; ask, or list the assumption.
- Names and symbols must match the paper exactly.
- A diagram that needs a paragraph to decode has too much in it. Split it.
- Do not use colour as the only way to tell things apart.
- No decorative 3D, shadows, gradients, or icons that carry no information.
- Deliver source that compiles. If it could not be compiled in this environment, say so.
- Vector output only for line diagrams. Screenshots of drawing tools blur in print.
- Do not copy a figure from another paper. Redraw in your own layout, and cite the source if the structure is theirs.

## Related skills

- `paper-outline-generator` plans where the overview figure goes.
- `publication-figure-maker` for plots, with matching colours and font sizes.
- `math-and-equation-explainer` to confirm symbols and shapes used as labels.
- `latex-paper-formatter` to place the figure in the template.
- `paper-to-slides`, `paper-to-poster`, and `paper-to-explainer-video` reuse the diagram.
- `paper-to-code-reproducer` when the diagram is drawn from an implementation.
