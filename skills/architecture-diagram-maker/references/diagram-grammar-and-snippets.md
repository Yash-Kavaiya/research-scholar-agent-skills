# Diagram grammar and source snippets

## 1. Visual grammar

| Element | Encoding |
|---|---|
| Operation or module | Rounded rectangle |
| Data, tensor, or dataset | Plain rectangle, or parallelogram for inputs and outputs |
| Storage or database | Cylinder |
| Operator (sum, concatenation, product) | Small circle with the symbol |
| Decision | Diamond |
| Group or stage | Dashed or lightly shaded container with a label |
| Data flow | Solid arrow |
| Gradient, feedback, training-only path | Dashed arrow |
| Optional path | Dotted arrow |
| Novel component | Accent fill and thicker border |
| Frozen or pretrained component | Grey fill or a lock icon note in the legend |

Define the grammar once in a legend if it is not obvious, and keep it the same across all figures in the paper.

## 2. Layout rules

- One main direction of flow.
- Align blocks to a grid; equal spacing.
- No crossing arrows where a reordering removes them.
- Labels on arrows only where the content is not obvious (tensor names, shapes).
- Five to nine blocks per diagram; split detail into a second figure.
- Text size equal to caption text at print scale.

## 3. TikZ building blocks

```latex
% \usepackage{tikz,amssymb}   (amssymb provides \mathbb used in arrow labels)
% \usetikzlibrary{positioning,arrows.meta,fit,backgrounds,shapes.geometric,calc}
\tikzset{
  block/.style={draw, rounded corners=2pt, minimum height=7mm, minimum width=16mm, align=center, font=\footnotesize},
  data/.style={draw, minimum height=7mm, minimum width=12mm, align=center, fill=black!5, font=\footnotesize},
  op/.style={draw, circle, inner sep=1pt, font=\footnotesize},
  new/.style={block, fill=orange!25, thick},
  frozen/.style={block, fill=black!10},
  group/.style={draw, dashed, rounded corners=3pt, inner sep=4mm},
  arr/.style={-{Latex[length=1.6mm]}},
  grad/.style={arr, dashed}
}
```

Patterns:

```latex
% horizontal chain
\node[data] (x) {$x$};
\node[block, right=of x] (enc) {Encoder};
\draw[arr] (x) -- (enc);

% branch and merge with an operator
\node[op, right=of enc] (sum) {$+$};
\draw[arr] (enc) -- (sum);
\draw[arr] (x.north) |- ++(0,6mm) -| (sum.north);   % skip connection over the top

% container around a stage
\begin{scope}[on background layer]
  \node[group, fit=(enc)(sum), label={[font=\footnotesize]above:Stage 1}] {};
\end{scope}

% label on an arrow
\draw[arr] (enc) -- node[above, font=\scriptsize] {$h \in \mathbb{R}^{d}$} (sum);

% stacked layers (repeated block)
\node[block] (l1) {Layer};
\node[block, above=1mm of l1, xshift=1mm, yshift=-0.5mm] {} ;  % offset copies suggest depth
```

Compile standalone diagrams with `\documentclass[tikz,border=2pt]{standalone}` to get a tightly cropped PDF.

## 4. Mermaid

```
flowchart LR
  x[/Input x/] --> enc(Encoder)
  enc --> mod(Our module):::new
  mod --> dec(Decoder) --> y[/Output/]
  enc -. skip .-> dec
  classDef new fill:#ffd9b3,stroke:#333,stroke-width:2px
```

`LR` or `TB` sets direction; `(...)` rounded, `[...]` rectangle, `[/.../]` parallelogram, `{...}` decision, `[(...)]` cylinder; `-.->` dotted.

## 5. Graphviz (DOT)

```
digraph G {
  rankdir=LR; node [shape=box, style=rounded, fontname="Helvetica", fontsize=10];
  x [shape=parallelogram, label="Input x"];
  mod [label="Our module", style="rounded,filled", fillcolor="#ffd9b3"];
  x -> enc -> mod -> dec -> y;
  enc -> dec [style=dashed, label="skip"];
}
```

Render with `dot -Tpdf diagram.dot -o diagram.pdf`.

## 6. Common diagram types

| Type | Layout tips |
|---|---|
| Model architecture | Input left, output right; repeated blocks as a stack with "×N" |
| Training pipeline | Data, model, loss, optimiser in a loop; gradients dashed |
| Inference pipeline | Linear chain with optional branches |
| System architecture | Clients, services, storage; group by tier |
| Study procedure | Participants flow top to bottom with numbers at each step |
| Taxonomy | Tree, left to right or top to bottom |

## 7. Checks

- Every block named as in the text.
- Shapes and colours used consistently with the legend.
- Readable in greyscale.
- Compiles from source; rendered output inspected.
- No component drawn that the method does not have.
