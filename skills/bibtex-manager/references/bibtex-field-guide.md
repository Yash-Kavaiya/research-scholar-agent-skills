# BibTeX field guide

## 1. Entry types and required fields

| Type | Use for | Required | Common optional |
|---|---|---|---|
| @article | Journal article | author, title, journal, year | volume, number, pages, doi, month |
| @inproceedings | Conference paper | author, title, booktitle, year | pages, publisher, address, doi |
| @book | Whole book | author or editor, title, publisher, year | edition, address, isbn |
| @incollection | Chapter in an edited book | author, title, booktitle, publisher, year | editor, pages, chapter |
| @phdthesis | Doctoral thesis | author, title, school, year | address, url |
| @mastersthesis | Master's thesis | author, title, school, year | |
| @techreport | Report | author, title, institution, year | number, type |
| @misc | Preprints, software, datasets, web pages | title (plus author, year, howpublished or url) | eprint, archivePrefix, primaryClass, note |
| @online | Web resource (biblatex) | title, url, urldate | |

biblatex adds types such as @dataset and @software; check whether the venue uses BibTeX or biblatex.

## 2. arXiv preprints

```bibtex
@misc{key,
  author        = {Surname, Given and Surname, Given},
  title         = {Title},
  year          = {2024},
  eprint        = {2401.01234},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  doi           = {10.48550/arXiv.2401.01234}
}
```

Replace with the published version when one exists.

## 3. Author names

| Situation | Write |
|---|---|
| Standard | `Surname, Given` or `Given Surname`, joined with ` and ` |
| Particles | `van der Berg, Anna` (lowercase particle, sorts under v in some styles) |
| Suffix | `King, Jr., Martin` |
| Compound surname | `{García Márquez}, Gabriel` or `García Márquez, Gabriel` |
| Corporate author | `{World Health Organization}` (double braces stop it being parsed as a person) |
| Many authors | List all; styles truncate with "et al." themselves |
| Unicode names | Use UTF-8 with biber or a UTF-8-aware setup; otherwise LaTeX escapes (`M{\"u}ller`) |

## 4. Title capitalisation

Bibliography styles may convert titles to sentence case. Protect words that must keep capitals with braces around the word:

| Protect | Example |
|---|---|
| Acronyms | `{BERT}`, `{GPU}`, `{DNA}` |
| Proper nouns | `{Bayesian}`, `{Markov}`, `{Gaussian}`, `{Python}`, `{Europe}` |
| Mixed case | `{ImageNet}`, `{mRNA}`, `{iPhone}` |
| Chemical formulas and symbols | `{CO$_2$}` |

Do not wrap the entire title in double braces; that disables the style's case handling for every word.

## 5. Special characters

| Character | BibTeX |
|---|---|
| & | `\&` |
| % | `\%` |
| $ | `\$` (or math mode where intended) |
| _ | `\_` |
| # | `\#` |
| Accents | `{\'e}`, `{\"o}`, `{\c{c}}`, or UTF-8 with biber |
| En dash in pages | `--` |

## 6. Authoritative sources for entries

| Source | Quality | Notes |
|---|---|---|
| DOI content negotiation (`curl -LH "Accept: application/x-bibtex" https://doi.org/<DOI>`) | Good | Fields from the publisher's registration |
| Publisher's "export citation" | Good | Check capitalisation |
| DBLP | Very good for computing | Consistent venue names |
| Crossref search | Good | Same data as DOI lookups |
| Google Scholar export | Often incomplete | Missing pages, abbreviated venues; check every field |
| Reference managers (Zotero, Mendeley) | Depends on capture | Check entry types and capitalisation |

## 7. Keys

A readable scheme such as `surnameYEARfirstword` (`vaswani2017attention`) avoids collisions and makes citations recognisable. Changing keys requires updating every `\cite`; do it once, early.

## 8. Venue names

Use one form per venue throughout: either the full name ("Advances in Neural Information Processing Systems") or the standard abbreviation, as the style and venue require. Vancouver and AMA styles use NLM journal abbreviations.

## 9. Common BibTeX warnings

| Warning | Cause | Fix |
|---|---|---|
| `empty journal in ...` | Required field missing | Add the field |
| `can't use both author and editor fields` | Both present in a type that allows one | Keep the correct one |
| `I didn't find a database entry for ...` | Key cited but not in the `.bib` file | Add the entry or fix the key |
| `Repeated entry` | Duplicate key | Merge duplicates |
| `Too many commas in name` | Malformed author list | Use ` and ` between authors |
