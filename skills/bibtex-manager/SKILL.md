---
name: bibtex-manager
description: Cleans a BibTeX file by normalising fields, DOIs, and page ranges, protecting capitalisation in titles, merging duplicate entries, reporting missing required fields and preprints with published versions, and optionally filling DOIs from Crossref and regenerating citation keys. Use when the user asks to "clean my bib file", "fix my BibTeX", "remove duplicate references", "my references have wrong capitalization", "generate BibTeX for these papers", "fix bibliography warnings", or has a messy .bib exported from Zotero, Mendeley, or Google Scholar.
---

# BibTeX Manager

Turn a messy `.bib` file into a consistent one, with every change reported and the original left untouched.

## When to use

- A `.bib` file has duplicates, inconsistent formatting, missing fields, or capitalisation problems.
- BibTeX or biber prints warnings.
- Entries need creating from DOIs, titles, or a pasted reference list.

Hand off instead to confirm references are real (`citation-verifier`) or to output a formatted reference list in a named style (`citation-style-converter`).

## Inputs

- The `.bib` file.
- The `.tex` files that cite it, when keys may change.
- The venue's bibliography style, which decides how much detail is needed.
- Preferences: keep or regenerate keys, keep or drop abstracts and notes.

## Workflow

1. **Clean the file into a new file:**

   ```bash
   python scripts/clean_bibtex.py refs.bib --out refs.clean.bib --report bib-report.json
   python scripts/clean_bibtex.py refs.bib --out refs.clean.bib --fill-doi --sort
   python scripts/clean_bibtex.py refs.bib --out refs.clean.bib --rekey
   ```

   The script:
   - lowercases entry types and field names, collapses whitespace, and expands `@string` macros;
   - normalises DOIs to the bare form and drops a `url` that only repeats the DOI;
   - converts page ranges to `123--130`;
   - protects words with inner capitals in titles (`{BERT}`, `{ImageNet}`, `{mRNA}`) so bibliography styles do not lowercase them;
   - drops empty fields and, by default, `abstract`, `file`, and `keywords` (change with `--strip`; `--strip ""` keeps everything);
   - merges duplicates (same DOI, or same title and year), keeping the fuller entry and reporting `removed key → kept key`;
   - reports missing required fields per entry type, preprints that may have a published version, `et al` in author lists, and odd years.

   Options: `--fill-doi` looks up missing DOIs in Crossref and accepts only a near-exact title match with a matching year. `--rekey` regenerates keys as `authorYEARfirstword` (for example `vaswani2017attention`). `--sort` orders entries by key.
2. **Read the report** and act on each part:
   - *duplicates_merged*: replace the removed keys in the `.tex` files with the kept keys.
   - *keys_changed* (with `--rekey`): update every `\cite` accordingly. Only rekey when the user wants it; it touches the whole manuscript.
   - *problems*: fill missing fields from the publisher page or Crossref; replace preprints with the published version where one exists.
3. **Fix what the script cannot judge:**
   - Proper nouns with only an initial capital in titles (`{Bayesian}`, `{Markov}`, `{Europe}`): brace them by hand.
   - Venue names: use one form for each venue throughout (full name or the standard abbreviation, as the style requires).
   - Author names: `Last, First` form; `and` between authors; corporate authors in double braces `{{World Health Organization}}`; accents as Unicode with biber or as LaTeX commands with classic BibTeX.
   - Entry types: `@inproceedings` for conference papers, `@article` for journals, `@misc` with `eprint` and `archivePrefix` for arXiv preprints.
4. **Create entries for new references** from authoritative metadata:
   - By DOI: `curl -LH "Accept: application/x-bibtex" https://doi.org/<DOI>`.
   - By title: find the record with `paper-search`, then fetch by its DOI.
   - Publisher and DBLP exports are good; Google Scholar's BibTeX is often incomplete (missing pages, abbreviated venues) and needs checking.
5. **Compile** the document and clear the remaining BibTeX or biber warnings and any `[?]` citations.
6. **Replace the original only after the user agrees**, keeping a backup.

## Output format

- `refs.clean.bib`, formatted one field per line with a consistent field order.
- A report:

```markdown
## BibTeX cleanup
Entries: 142 in, 135 out.

### Duplicates merged (update these \cite keys)
| Removed key | Kept key |

### DOIs added
### Problems to resolve
| Key | Problem | Suggested fix |

### Manual changes made
```

## Quality bar and pitfalls

- Never invent a missing field. Volume, pages, year, and DOI come from the publisher, Crossref, or DBLP, or stay empty and reported.
- The script writes to a new file and refuses to overwrite its input. Keep the original until the document compiles with the new file.
- Changing keys breaks citations. Report every changed key and update the `.tex` files in the same step.
- Duplicate detection by title and year can merge two distinct works with the same title (an arXiv version and a journal version are the same work; a paper and its erratum are not). Review the merge list.
- An entry being well formed does not make it real. Run `citation-verifier` on references of uncertain origin.
- Do not brace an entire title (`{{Whole Title}}`) to preserve case. It defeats the bibliography style; brace only the words that need it.
- A DOI filled by title search should be opened once to confirm it is the right paper.

## Related skills

- `citation-verifier` to confirm entries exist and match their sources.
- `citation-style-converter` to render the list in APA, IEEE, Vancouver, or Harvard.
- `paper-search` to find records for new entries.
- `latex-paper-formatter` for the venue's bibliography setup.
- `annotated-bibliography-builder` uses the cleaned file.
- `camera-ready-checker` checks the final reference list.
