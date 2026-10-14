# Citation style differences and CSL usage

## 1. How the main styles differ

| Feature | APA 7 | IEEE | Vancouver (NLM) | Harvard (Cite Them Right) | Chicago author-date | MLA 9 |
|---|---|---|---|---|---|---|
| In-text | (Author, Year) | [1] | (1) or superscript | (Author Year) or (Author, Year) | (Author Year) | (Author page) |
| Order of list | Alphabetical | Order of first citation | Order of first citation | Alphabetical | Alphabetical | Alphabetical |
| Author names | Surname, I. I. | I. I. Surname | Surname II | Surname, I. | Surname, Given | Surname, Given |
| Authors listed | Up to 20 | Up to 6, then et al. (varies) | Up to 6, then et al. | All or per guide | Up to 10 | Two, then et al. for three or more |
| Title case | Sentence case (articles), italic book and journal | Sentence case in quotes | Sentence case, no quotes | Sentence case in quotes | Title case in quotes | Title case in quotes |
| Journal names | Full, italic | Abbreviated, italic | NLM abbreviation | Full, italic | Full, italic | Full, italic |
| DOI | As URL | doi: prefix | doi: prefix | As URL | As URL | As DOI |

Details vary by edition and institution; render with a processor and check against the official guide.

## 2. Choosing the CSL file

| Style | CSL file |
|---|---|
| APA 7th | apa.csl |
| IEEE | ieee.csl |
| Vancouver (NLM) | nlm-citation-sequence.csl |
| Vancouver, superscript variant | nlm-citation-sequence-superscript.csl |
| Harvard (Cite Them Right) | harvard-cite-them-right.csl |
| Elsevier Harvard | elsevier-harvard.csl |
| Elsevier numbered | elsevier-with-titles.csl |
| Chicago author-date | chicago-author-date.csl |
| Chicago notes and bibliography | chicago-notes-bibliography.csl (or chicago-shortened-notes-bibliography.csl) |
| MLA 9th | modern-language-association.csl |
| AMA | american-medical-association.csl |
| Springer basic author-date | springer-basic-author-date.csl |
| Nature | nature.csl |

For a specific journal, search the CSL styles repository or the Zotero Style Repository by journal name; many journals have their own file or an alias.

## 3. Pandoc commands

```bash
# reference list only, from a .bib file
pandoc -f bibtex refs.bib --citeproc --csl apa.csl -t plain --wrap=none -o references.txt
pandoc -f bibtex refs.bib --citeproc --csl ieee.csl -t docx -o references.docx

# a Markdown manuscript with [@key] citations
pandoc paper.md --citeproc --bibliography refs.bib --csl apa.csl -o paper.docx

# CSL JSON for other tools
pandoc -f bibtex refs.bib -t csljson -o refs.json
```

Pandoc 2.11 or later includes citeproc. Use `-f biblatex` for biblatex files.

## 4. LaTeX equivalents

| Target | BibTeX | biblatex |
|---|---|---|
| APA | `apacite` package or `apalike` (approximate) | `\usepackage[style=apa]{biblatex}` |
| IEEE | `\bibliographystyle{IEEEtran}` | `style=ieee` (biblatex-ieee) |
| Vancouver | `\bibliographystyle{vancouver}` | `style=vancouver` |
| Author-year generic | `plainnat` with natbib | `style=authoryear` |
| Numeric generic | `plain`, `unsrt` | `style=numeric` |
| Chicago | `chicago` | `style=chicago-authordate` (biblatex-chicago) |

## 5. Switching between numeric and author-year text

| From | To | Edits |
|---|---|---|
| Numeric ("as shown in [3]") | Author-year | Rephrase so the author can be named: "as Smith et al. (2020) showed"; use `\citet` and `\citep` |
| Author-year ("Smith (2020) found") | Numeric | Rephrase: "One study found [3]" or keep the name: "Smith et al. [3] found" |
| Footnotes (Chicago notes) | Author-date | Move citations into the text; remove note-only commentary or keep it as footnotes |

## 6. Data problems that show in output

| Symptom | Cause in the data | Fix in the data |
|---|---|---|
| Acronyms lowercased | Title not protected | Brace the acronym in the `.bib` |
| Organisation shown as "Organization, W. H." | Corporate author parsed as a person | Double braces around the name |
| Missing volume or pages | Fields absent | Add from the publisher |
| Wrong item type (book chapter shown as article) | Entry type wrong | Change the type |
| Journal not abbreviated for Vancouver | No abbreviation available to the style | Add `journalabbreviation` or the abbreviated journal name as the style expects |
| "n.d." for a dated work | Year missing | Add year |

Fix the data, then re-render; never patch the output by hand.

## 7. Check a sample by type

Compare one rendered example of each type (article, book, chapter, conference paper, thesis, web page, preprint, dataset) with the style manual's examples.
