---
name: latex-paper-formatter
description: Converts a draft in Word, Markdown, plain text, or another LaTeX class into a venue's official LaTeX template (IEEE, ACM, Springer LNCS, NeurIPS, ICML, ICLR, ACL, Elsevier) and fixes compile errors, overfull boxes, float placement, and bibliography setup. Use when the user asks to "format my paper for IEEE", "convert this to the NeurIPS template", "move my paper from ACM to Springer format", "put this Word draft into LaTeX", "fix my LaTeX errors", or "my paper is over the page limit after switching templates".
---

# LaTeX Paper Formatter

Move a draft into the venue's official template without altering its content, and deliver a project that compiles cleanly.

## When to use

- A draft must be put into a specific venue's LaTeX template.
- A paper is being resubmitted to a venue with a different template.
- A LaTeX project has compile errors or layout warnings.

Hand off instead for final pre-submission checks (`camera-ready-checker`), tables (`latex-table-generator`), or figures (`publication-figure-maker`).

## Inputs

- The draft and its assets: text, figures, tables, and the `.bib` file.
- Target venue, year, and submission type (review or camera-ready; anonymous or not).
- The official template, or permission to obtain it.

## Workflow

1. **Get the official template for the current year** from the venue or publisher. Never reconstruct a template from memory or modify its style file.

   | Venue family | Class or style | Source |
   |---|---|---|
   | IEEE conferences and journals | `IEEEtran` | CTAN, IEEE Template Selector |
   | ACM | `acmart` (options such as `sigconf`, `manuscript`, `review`, `anonymous`) | CTAN, ACM primary article template page |
   | Springer LNCS | `llncs` | Springer's LNCS author page |
   | Springer journals | `sn-jnl` | Springer Nature LaTeX template page |
   | NeurIPS, ICML, ICLR | venue style file for that year | the conference website |
   | ACL, EMNLP, NAACL | `acl` style | the `acl-org/acl-style-files` repository |
   | Elsevier | `elsarticle` | CTAN, Elsevier author pages |
   | CVPR, ICCV, ECCV | author kit for that year | the conference website |

2. **Start from the template's sample file.** Copy it, confirm it compiles unchanged, then move content in. This isolates template problems from content problems.
3. **Convert the content:**
   - From Word or Markdown: `pandoc draft.docx -o body.tex --wrap=none` (or `draft.md`), then clean the result: headings to `\section`, lists, citations to `\cite{}`, cross-references to `\label` and `\ref`. Pandoc's output for tables and equations usually needs rewriting.
   - From another LaTeX class: keep the body, replace the preamble with the new template's, and port only the packages the paper needs.
4. **Map the front matter** to the template's commands: title, authors, affiliations, emails, abstract, keywords, CCS concepts (ACM), and the anonymous option for review. These differ in every class; use the sample file's pattern.
5. **Fix package conflicts.** Templates load their own packages; remove duplicates (`geometry`, `times`, `caption`, `natbib`, `hyperref` are frequent offenders) and anything that changes margins, fonts, or spacing.
6. **Set up the bibliography** the way the template does: its `.bst` with BibTeX, or `biblatex` only if the venue allows. Use the citation commands the style expects (`\citep` and `\citet` for author-year, `\cite` for numeric).
7. **Fit figures and tables** to the new column width: `\includegraphics[width=\columnwidth]`, `figure*` and `table*` for full width in two-column layouts, and regenerate figures at the new size if text in them becomes unreadable.
8. **Compile** with `latexmk -pdf main.tex` and resolve, in order: errors, undefined references and citations, overfull hboxes above a few points, and float placement.
9. **Check the length** against the limit. If over, report by how much and suggest content cuts or moving material to the appendix.
10. **Deliver** the project, the compiled PDF, and a list of anything that needs the author's decision.

## Output format

```
paper/
  main.tex            # template preamble, \input of sections
  sections/*.tex
  figures/
  references.bib
  <template files, unmodified>
  main.pdf
```

Plus a report:

```markdown
- Template: <name, version or year, source URL>
- Compile: <N> errors, <M> warnings remaining (listed)
- Length: <pages> of <limit>
- Changes made to content: none | <list>
- Needs your decision: <items>
```

## Quality bar and pitfalls

- Do not change the template's margins, fonts, font sizes, or spacing to gain space (`\vspace` hacks, `\small` body text, altered `\baselinestretch`). Venues reject or desk-return papers for this.
- Do not alter the paper's content during formatting. Report any sentence, number, or reference that had to change.
- Use the template for the correct year and submission type; review and camera-ready versions differ.
- Do not claim the paper compiles unless it was compiled. If no TeX installation is available, say the output is untested.
- Keep anonymity for double-blind review: no author names, acknowledgements, or identifying metadata, and third-person self-citation.
- A missing or unresolved citation prints as `[?]`. Clear all of them before delivery.
- Type 3 fonts in figures cause rejections at IEEE and ACM venues; embed TrueType fonts (see `publication-figure-maker`).

## Related skills

- `paper-outline-generator` for structure and length budget.
- `latex-table-generator` and `publication-figure-maker` for items resized to the new template.
- `bibtex-manager` and `citation-style-converter` for the bibliography.
- `camera-ready-checker` for the final compliance check.
- `math-and-equation-explainer` when equations need retyping from a Word draft.
- `academic-tone-editor` if cuts are needed to meet the page limit.
