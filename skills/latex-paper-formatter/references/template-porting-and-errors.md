# Template porting and LaTeX error guide

## 1. Front matter by class

| Class | Title and authors | Abstract and keywords | Anonymous option |
|---|---|---|---|
| IEEEtran | `\title{}`, `\author{\IEEEauthorblockN{...}\IEEEauthorblockA{...}}`, `\maketitle` | `\begin{abstract}`, `\begin{IEEEkeywords}` | Remove author block for double-blind; check the conference instructions |
| acmart | `\title{}`, one `\author{}` per author with `\affiliation{}` and `\email{}`; abstract before `\maketitle` | `\begin{abstract}`, `\keywords{}`, CCS concepts with `\ccsdesc` | Class option `anonymous`; also `review` for line numbers |
| llncs (Springer LNCS) | `\title{}`, `\author{}` with `\inst{}`, `\institute{}` | `\begin{abstract}`, `\keywords{}` inside it | Replace authors and institutes with "Anonymous" |
| sn-jnl (Springer Nature) | `\author*[1]{...}`, `\affil[1]{...}` | `\abstract{}`, `\keywords{}` | Per journal |
| elsarticle | `\begin{frontmatter}`, `\title`, `\author`, `\affiliation` | `\begin{abstract}`, `\begin{keyword}` | Per journal |
| NeurIPS, ICML, ICLR style files | `\title`, `\author` | `\begin{abstract}` | Default is anonymous; a `final` or `preprint` option shows authors |
| ACL style | `\title`, `\author` | `\begin{abstract}` | Option for review mode adds line numbers and anonymity |

Copy the pattern from the template's sample file; details change between versions.

## 2. Packages that conflict with templates

| Package or command | Problem | Action |
|---|---|---|
| `geometry`, `fullpage`, margin changes | Alters the page layout | Remove |
| `times`, `mathptmx`, font packages | Template sets fonts | Remove unless the template asks for them |
| `\usepackage{caption}` with options | Changes caption style | Remove, or keep without options if the template allows |
| `natbib` loaded twice | Option clash | Keep the template's loading |
| `hyperref` loaded early | Must usually load near the end | Move after other packages, or rely on the template |
| `cite` with `natbib` | Incompatible | Keep one, as the template expects |
| `subfigure` | Obsolete, conflicts with `subcaption` | Use `subcaption` |
| `\baselinestretch`, `\linespread`, `setspace` | Alters spacing | Remove |
| `titlesec` | Changes headings | Remove |

## 3. Bibliography setup

| Template | Style | Commands |
|---|---|---|
| IEEEtran | `\bibliographystyle{IEEEtran}` with BibTeX | `\cite{}` |
| acmart | `\bibliographystyle{ACM-Reference-Format}` | `\cite{}`, `\citet{}`, `\citep{}` (natbib) |
| llncs | `\bibliographystyle{splncs04}` | `\cite{}` |
| NeurIPS and ICLR | natbib author-year or numeric per instructions | `\citet{}`, `\citep{}` |
| ACL | `\bibliographystyle{acl_natbib}` | `\citet{}`, `\citep{}` |
| elsarticle | `elsarticle-num` or `elsarticle-harv` | per style |

Use biblatex only if the venue accepts it. Production systems often need the `.bbl` file uploaded with the source.

## 4. Converting from Word or Markdown

1. `pandoc draft.docx -o body.tex --wrap=none` (or from Markdown).
2. Replace pandoc's section macros and remove `\tightlist` and similar helpers.
3. Rewrite tables as booktabs tables.
4. Retype equations that came through as images or Unicode.
5. Replace manual references ("Figure 3") with `\label` and `\ref`.
6. Replace typed citations with `\cite` keys from the `.bib` file.
7. Escape special characters: `% & _ # $ { }`.

## 5. Figures and tables in the new layout

| Situation | Approach |
|---|---|
| Two-column template, wide figure | `figure*` and `\textwidth` |
| Single column | `\includegraphics[width=\columnwidth]{...}` |
| Text in the figure becomes tiny | Regenerate the figure at the new width rather than scaling |
| Wide table | Reduce columns or decimals, `table*`, then `\resizebox` as a last resort |
| Float placement | `[t]` or `[tb]`; avoid `[h!]` everywhere; place the float near its first reference |

## 6. Common errors

| Message | Cause | Fix |
|---|---|---|
| `Undefined control sequence` | Misspelt command, or package not loaded | Check spelling; add the package if allowed |
| `Missing $ inserted` | Math symbol or underscore in text | Wrap in `$...$` or escape `\_` |
| `File ... not found` for a `.sty` file | Package not installed | Install via the distribution's package manager |
| `Option clash for package` | Loaded twice with different options | Load once; pass options with `\PassOptionsToPackage` before the class |
| `Too many unprocessed floats` | Many floats queued | Add `\clearpage` at a sensible point; reduce float count |
| `Citation ... undefined` | Key missing from `.bib` or BibTeX not run | Fix the key; run latexmk |
| `Reference ... undefined` | Label missing or one compile pass | Fix the label; compile again |
| `Overfull \hbox` | Line too long | Rephrase, allow hyphenation, break URLs with `\url`, resize tables |
| `Underfull \hbox` | Loose line | Usually harmless; rephrase if visible |
| `Font shape ... undefined` | Missing font variant | Use the template's fonts |
| `Dimension too large` | Plot coordinates out of range | Rescale data or the axis |

Compile with `latexmk -pdf main.tex`. Read the log from the first error; later errors often follow from it.

## 7. Getting within the page limit legitimately

1. Cut redundant text and tighten sentences.
2. Shorten related work to the closest groups.
3. Move proofs, details, and secondary results to the appendix.
4. Merge or reduce figures; regenerate figures at a compact aspect ratio.
5. Shorten long tables.

Never alter margins, font size, line spacing, or float spacing in ways the template does not provide. Venues check and reject.

## 8. Camera-ready differences

Authors and affiliations restored; acknowledgements and funding added; copyright block or licence text per the publisher; final option of the style file; PDF metadata (title, authors) set; PDF validator passed where required.
