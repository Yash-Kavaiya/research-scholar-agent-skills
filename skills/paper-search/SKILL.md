---
name: paper-search
description: Searches arXiv, Semantic Scholar, OpenAlex, PubMed, and Crossref in one call, merges duplicate records, and returns papers with authors, year, venue, DOI, link, abstract, and citation count. Use when the user asks to "find papers on X", "search the literature", "get me recent work about X", "find the paper titled ...", "look up this DOI", or when another skill needs real paper records instead of recalled ones.
---

# Paper Search

Retrieve real paper records from free scholarly APIs. No API key is needed. This is the base skill other research skills call whenever they need papers.

## When to use

- Any request for papers, references, or reading lists.
- Finding a specific paper from a partial title, author, or DOI.
- Whenever a claim about the literature needs a retrieved record behind it.

Hand off instead for citation chasing from known papers (`citation-graph-explorer`) or a protocol-driven search for a systematic review (`systematic-review-prisma`).

## Inputs

- Topic or question. Convert questions into keyword queries.
- Field, which decides the sources.
- Year range, and whether the user wants seminal work, recent work, or both.
- How many papers they want back.

## Workflow

1. **Pick sources by field.**

   | Field | Sources |
   |---|---|
   | CS, ML, physics, maths, statistics | `arxiv,semantic_scholar,openalex` |
   | Biomedicine, health, life sciences | `pubmed,openalex,crossref` |
   | Social sciences, humanities, engineering, other | `openalex,crossref,semantic_scholar` |
   | Unknown or interdisciplinary | all five (the default) |

2. **Write 2 to 4 queries**, not one: the user's terms, the field's standard terms, and a synonym or acronym variant. Short keyword queries work better than sentences.
3. **Run the search:**

   ```bash
   python scripts/search_papers.py "retrieval augmented generation" --limit 10 --format md --abstracts 300
   python scripts/search_papers.py "CRISPR off-target effects" --sources pubmed,openalex --year-from 2021 --sort citations
   python scripts/search_papers.py "graph neural networks survey" --format json --out results.json
   ```

   Options: `--sources`, `--limit` (per source), `--year-from`, `--year-to`, `--sort relevance|citations|year`, `--format json|md`, `--abstracts N`, `--out FILE`.
4. **Check the warnings.** A source that fails (Semantic Scholar often rate-limits without a key) is reported on stderr and in the `errors` field. Retry it once after a pause, or state that it was not searched.
5. **Screen the results.** Read titles and abstracts and drop off-topic hits. Lexical search returns papers that share words, not meaning.
6. **Fill gaps.** If a paper you expected is missing, search its exact title. For key papers, follow up with `citation-graph-explorer`.
7. **Present** the kept papers grouped by sub-theme or by role (survey, seminal, recent), with one line each on why it is relevant.

Optional environment variables for higher rate limits: `OPENALEX_MAILTO` (contact email), `S2_API_KEY`, `NCBI_API_KEY`. Never print their values.

## Output format

```markdown
## Papers on <topic>
Searched: <sources> on <date>. Queries: "...", "...". Not searched: <failed sources>.

### <Group, e.g. Surveys>
1. **Title** (year). First Author et al. *Venue*. <link> (N citations)
   Why relevant: <one line>

### <Group, e.g. Recent methods>
...

## Notes
- <gaps, missing full text, suggested follow-up searches>
```

When another skill is the consumer, pass the JSON file path instead.

## Quality bar and pitfalls

- Only report papers the script returned. Never add a paper from memory without retrieving its record; if you believe one exists, search for it by title.
- Report every field as retrieved. If the venue or DOI is empty, leave it empty.
- Citation counts differ between sources and favour older papers. Use them to find landmarks, not to rank recent work.
- arXiv requires every query word to appear, so long queries return little. Use 2 to 4 words there.
- PubMed accepts its own syntax (`"term"[tiab]`, MeSH, AND/OR). Use it for biomedical precision.
- Crossref covers the most publishers and has the weakest relevance ranking. It is best for exact titles and pasted reference strings.
- Preprints and their published versions may appear as two records when their DOIs and titles differ. Merge them by hand and cite the published version.
- Do not help bypass paywalls. Point to open-access versions (arXiv, PubMed Central, the OpenAlex landing page) when they exist.

## Related skills

- `citation-graph-explorer` to expand from the best hits.
- `paper-summarizer` and `paper-comparison-matrix` to digest what was found.
- `annotated-bibliography-builder` and `literature-review-writer` to write from the results.
- `bibtex-manager` to turn chosen papers into clean BibTeX.
- `citation-verifier` to check references that came from elsewhere.
