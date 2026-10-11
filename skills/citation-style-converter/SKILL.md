---
name: citation-style-converter
description: Converts reference lists and in-text citations between citation styles such as APA 7, IEEE, Vancouver, Harvard, Chicago, MLA, and AMA using pandoc with CSL style files, so the formatting comes from a citation processor instead of being typed by hand. Use when the user asks to "convert my references to APA", "change citation style from IEEE to Harvard", "format this reference in Vancouver", "the journal wants a different reference style", or "switch from numeric to author-year citations".
---

# Citation Style Converter

Change citation style by re-rendering structured reference data with a citation processor. Hand-reformatting hundreds of references produces errors; a CSL processor does not.

## When to use

- A journal, university, or resubmission requires a different citation style.
- A reference list needs formatting in a named style.
- In-text citations must switch between numeric and author-year.

Hand off instead to fix the underlying reference data (`bibtex-manager`) or to check references are real (`citation-verifier`).

## Inputs

- The references as structured data: `.bib`, RIS, EndNote XML, or CSL JSON. If the user has only a formatted list, see step 2.
- The target style and edition (APA 7, IEEE, Vancouver, Harvard variant, Chicago author-date or notes, MLA 9), or the journal's name.
- The manuscript format (LaTeX, Markdown, Word) when in-text citations must change too.

## Workflow

1. **Identify the exact target style.** "Harvard" has no single definition; ask which institution's or journal's version. Many journals have their own CSL style; search the CSL repository by journal name.
2. **Get structured data.** If the references exist only as formatted text:
   - Look each one up in Crossref by pasting the reference string into `paper-search` (`--sources crossref`), confirm the match, and fetch BibTeX by DOI.
   - References with no DOI (books, reports) are entered by hand into the `.bib` file.
   - Do not parse formatted strings by guesswork into fields; mis-split author names and titles then propagate into every style.
3. **Get the CSL style file** from the official repository:

   | Style | File name |
   |---|---|
   | APA 7th | `apa.csl` |
   | IEEE | `ieee.csl` |
   | Vancouver (NLM) | `nlm-citation-sequence.csl` |
   | Harvard (Cite Them Right) | `harvard-cite-them-right.csl` |
   | Chicago author-date | `chicago-author-date.csl` |
   | MLA 9 | `modern-language-association.csl` |
   | AMA | `american-medical-association.csl` |

   ```bash
   curl -fLO https://raw.githubusercontent.com/citation-style-language/styles/master/apa.csl
   ```

   Other styles and journal-specific files are in the same repository and searchable at the Zotero Style Repository.
4. **Render the reference list** with pandoc (version 2.11 or later):

   ```bash
   pandoc -f bibtex refs.bib --citeproc --csl apa.csl -t plain --wrap=none -o references.txt
   pandoc -f bibtex refs.bib --citeproc --csl ieee.csl -t docx -o references.docx   # keeps italics
   ```

   Use `-f biblatex` for biblatex-flavoured files. Use `-t html` or `-t docx` when italics matter; plain text drops them.
5. **Convert in-text citations** according to the manuscript format:
   - *Markdown*: citations written as `[@key]` re-render with the new style:
     `pandoc paper.md --citeproc --bibliography refs.bib --csl apa.csl -o paper.docx`
   - *LaTeX*: change the bibliography style, not the text. With BibTeX: `\bibliographystyle{IEEEtran}`, `apalike`, `plainnat`, `vancouver`. With biblatex: `\usepackage[style=apa]{biblatex}` (or `ieee`, `vancouver`, `authoryear`). When moving between numeric and author-year, also revise sentences that depend on the form ("as shown in [3]" versus "as shown by Smith (2020)"), using `\citet` and `\citep`.
   - *Word*: change the style in the reference manager (Zotero, Mendeley, EndNote) so fields update. If citations are plain text, they must be re-linked or edited by hand; say so.
6. **Review the output** against the style guide for the things processors cannot fix because the data is wrong: title capitalisation stored in the wrong case, missing fields, corporate authors split as people, journal abbreviations (Vancouver and AMA use NLM abbreviations).
7. **Fix the data, not the output.** Correct the `.bib` entry and re-render, so the fix survives the next style change.

## Output format

- The reference list in the target style (`.txt`, `.docx`, or `.html`).
- The converted manuscript or the changed preamble lines, when in-text citations were converted.
- A report:

```markdown
- Target style: APA 7 (apa.csl from the CSL repository, retrieved <date>)
- References rendered: <N>
- Entries with data problems (fixed in the .bib): ...
- Entries needing your check: ...
- Sentences reworded for the citation form: ...
```

## Quality bar and pitfalls

- Do not hand-format or retype references. Formatting comes from the processor; typing introduces errors in punctuation, italics, and order.
- Never fill a field the style requires with a guess (issue number, publisher city, access date). Report it as missing.
- Sentence-case styles (APA, Vancouver) lowercase titles. Words that must keep capitals need protecting in the data (`{BERT}` in BibTeX), or they will be lowercased.
- Numeric styles number by first appearance (IEEE, Vancouver) or alphabetically depending on the style; never renumber by hand.
- The style edition matters (APA 6 and 7 differ on DOIs, publisher locations, and author counts).
- Check a sample of each reference type (article, book, chapter, conference paper, web page, thesis) against the official guide; rare types are where styles and data most often disagree.
- If pandoc is not installed, say so and give the commands for the user to run; do not fall back to manual formatting presented as processed output.

## Related skills

- `bibtex-manager` to clean the source data first.
- `citation-verifier` to confirm the references before formatting them.
- `paper-search` to recover structured records for references that exist only as text.
- `latex-paper-formatter` for the venue's bibliography setup in LaTeX.
- `annotated-bibliography-builder` when entries also need annotations.
- `camera-ready-checker` for the final reference-format check.
