---
name: novelty-checker
description: Checks whether a research idea has already been done by searching scholarly databases with several phrasings, ranking the closest prior work, and stating exactly how the idea differs from each. Use when the user asks "has this been done before", "is my idea novel", "find the closest prior work", "check novelty before I start", or needs a novelty statement for a proposal or paper.
---

# Novelty Checker

Find the papers closest to an idea and report, for each, what overlaps and what does not. The output is an evidence-based judgement with stated limits, never a guarantee.

## When to use

- Before the user commits time to an idea.
- When a proposal, introduction, or rebuttal needs a defensible novelty claim.

Hand off instead when the user has no specific idea yet (`research-gap-finder`) or wants a broad reading list (`paper-search`).

## Inputs

- The idea in one or two sentences. If it is vague, restate it as: *task or problem* + *method or intervention* + *setting or data* + *claimed benefit*, and confirm.
- Field, and any papers the user already knows are close.

## Workflow

1. **Decompose the idea** into its components (problem, method, setting, benefit). Novelty usually lives in one component or in their combination, so name which.
2. **Write 4 to 6 query phrasings**: the user's own terms, standard field terms, synonyms and older names for the method, the problem alone, the method alone, and the method applied in a neighbouring setting.
3. **Run the search:**

   ```bash
   python scripts/closest_work.py --idea "<idea>" \
     --query "<phrasing 1>" --query "<phrasing 2>" --query "<phrasing 3>" --top 15
   ```

   The script searches arXiv, OpenAlex, Semantic Scholar, and Crossref, merges duplicates, and ranks by term overlap and by how many phrasings found each paper. Add `--sources pubmed,openalex` for biomedical ideas. A warning about a failed source means that source was not searched; say so in the report.
4. **Read the top candidates.** Open the abstract of the top 10, and the method section of the top 3 to 5. The ranking is lexical, so a low-ranked paper with different vocabulary can still be the closest. Scan all returned titles.
5. **Chase one hop.** For the 2 closest papers, check their recent citing papers with `citation-graph-explorer`. Follow-up work is where an idea is most often already done.
6. **Compare component by component** in a table, one row per close paper.
7. **Give a verdict** from this scale, with the reason:
   - *Already done*: a paper does the same thing in the same setting.
   - *Incremental*: same approach with a minor change in data or setting.
   - *Differentiated*: a clear difference in at least one component that would change the result or its use.
   - *No close work found*: nothing within the searched sources. State this as a search result, not a fact about the world.
8. **Suggest how to sharpen** the idea so the difference is larger or easier to defend.

## Output format

```markdown
## Idea
<restated: problem + method + setting + benefit>

## Search performed
Sources: ... (failed: ...). Queries: ... Date: <today>.

## Closest prior work
| # | Paper (year) | Same problem | Same method | Same setting | What differs |
|---|---|---|---|---|---|

## Verdict: <already done | incremental | differentiated | no close work found>
<two to four sentences of reasoning naming the papers>

## Novelty statement you can defend
> Unlike <A> and <B>, which ..., this work ...

## What this check did not cover
- <unsearched venues, non-English work, patents, papers under review, very recent preprints>

## Ways to sharpen the idea
```

## Quality bar and pitfalls

- Never say "this is novel" without qualification. Say what was searched, when, and what was found.
- Every paper in the table must be a retrieved record with a working link. Do not fill the table from memory.
- Different terminology hides prior work. If all queries share the same key term, the search is too narrow.
- Check dates. A preprint from last month can overturn the verdict; sort one search by date.
- Same method on a new dataset is usually incremental. Say so, and say what would make it more than that.
- Patents, theses, and industry reports are not covered by these sources. List that under limits when it matters.

## Related skills

- `paper-search` for broader or source-specific searching.
- `citation-graph-explorer` to check follow-up work on the closest papers.
- `research-gap-finder` when the idea turns out to be done and the user needs a new direction.
- `related-work-writer` to turn the comparison table into a related-work section.
- `research-question-formulator` to rewrite the question after sharpening the idea.
