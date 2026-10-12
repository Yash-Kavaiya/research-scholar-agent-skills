---
name: annotated-bibliography-builder
description: Builds an annotated bibliography in which each entry has a correctly formatted citation followed by a summary, an evaluation of the source, and a note on its relevance to the user's project. Use when the user asks for an "annotated bibliography", "annotate these sources", "write annotations for my references", "reading list with notes", or has a coursework or proposal requirement for annotated entries.
---

# Annotated Bibliography Builder

Produce entries that let a reader judge each source without opening it: what it says, how far to trust it, and what it is for in this project.

## When to use

- A coursework, proposal, or thesis-stage annotated bibliography.
- Organised reading notes before writing a review.

Hand off instead for synthesis across sources (`literature-review-writer`) or a single in-depth summary (`paper-summarizer`).

## Inputs

- The sources: PDFs, links, DOIs, or a `.bib` file. If the user has only a topic, find sources with `paper-search` and confirm the selection.
- The project's research question, so relevance notes are specific.
- Citation style (APA 7, MLA 9, Chicago, IEEE, Harvard) and any length rule per annotation (commonly 100 to 200 words).
- Annotation type required: descriptive (summary only), evaluative (summary and assessment), or reflective (adds use in the project). Default: all three parts.
- Ordering: alphabetical by author (default), chronological, or grouped by theme.

## Workflow

1. **Verify the metadata** of each source against Crossref or the publisher page (`citation-verifier`): authors, year, title, venue, volume, pages, DOI.
2. **Read each source** to the depth its role needs. Record whether it was read in full or as an abstract.
3. **Write the citation** in the required style.
4. **Write the annotation** in three parts:
   - *Summary* (2 to 4 sentences): the question, the method or approach, and the main finding or argument.
   - *Evaluation* (1 to 3 sentences): source type and authority, strength of evidence, limitations, and how it compares with other sources in the list.
   - *Relevance* (1 to 2 sentences): what this source does for the user's project: background, method to adopt, evidence for a claim, a counter-position, or a gap it exposes.
5. **Keep a consistent voice and length.** Third person, present tense for what the source argues, past tense for what a study did.
6. **Add a tag line** when the list is long: theme, method, and a relevance rating (core, supporting, peripheral).
7. **Order and format** the list. For APA, the annotation is a new paragraph indented under a hanging-indent citation.
8. **Summarise the set**: coverage by theme and year, and what is missing.

## Output format

```markdown
# Annotated Bibliography: <project title>
Research question: ...
Style: APA 7. <N> sources.

Author, A. A., & Author, B. B. (2023). Title of the article. *Journal Name, 12*(3), 45–67. https://doi.org/...

> **Summary.** ...
> **Evaluation.** ...
> **Relevance.** ...
> *Tags: theme; method; core. Read: full text.*

(next entry)

## Coverage notes
| Theme | Sources | Gap |
```

Offer a `.bib` export with the annotation in the `annote` field when the user works in LaTeX.

## Quality bar and pitfalls

- Every entry is a real, verified source. Never fabricate an entry to reach a required count; say how many could be found.
- Do not annotate from the abstract and present it as a reading. Mark abstract-only entries.
- An annotation is not the abstract reworded. Write it in your own words and add evaluation.
- Evaluation needs a basis: sample size, design, venue, recency, whether findings were replicated. "A useful source" says nothing.
- Relevance must name the project. "Relevant to my topic" says nothing.
- Follow the style manual for the citation exactly (capitalisation, italics, DOI format). Mixed styles are the most common fault.
- Keep within the length rule. Markers count words.

## Related skills

- `paper-search` to find sources, and `citation-verifier` to confirm their metadata.
- `paper-summarizer` and `paper-critic` for the summary and evaluation parts.
- `citation-style-converter` to switch the list between styles.
- `bibtex-manager` for the `.bib` export.
- `literature-review-writer` to turn the annotations into a synthesis.
