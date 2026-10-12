---
name: citation-graph-explorer
description: Chases citations backward (what a paper cites) and forward (who cites it) from one or more seed papers, and detects seminal papers by finding references shared across the seeds. Use when the user asks "what are the foundational papers for X", "who cited this paper", "snowball from these papers", "find follow-up work to this paper", "trace the lineage of this method", or wants to expand a reading list from a few known papers.
---

# Citation Graph Explorer

Start from papers the user trusts and walk the citation graph in both directions. This finds work that keyword search misses because it uses different vocabulary.

## When to use

- The user has one to five good papers and wants the rest of the conversation around them.
- Finding the foundations of an area, or the latest work building on a result.
- The snowballing step of a systematic review.

Hand off instead when there are no seed papers yet (`paper-search`).

## Inputs

- Seed papers as DOIs or OpenAlex work ids. If the user gives titles, resolve them to DOIs with `paper-search` first and confirm each match.
- Direction of interest: foundations (backward), follow-ups (forward), or both.
- How many papers to list per direction (default 10).

## Workflow

1. **Resolve seeds** to DOIs. For arXiv-only papers use the arXiv DOI form `10.48550/arXiv.<id>`.
2. **Run the explorer:**

   ```bash
   python scripts/citation_graph.py 10.18653/v1/N19-1423 --top 10
   python scripts/citation_graph.py 10.18653/v1/N19-1423 10.48550/arXiv.1706.03762 --top 15 --format json
   ```

   For each seed it lists the most-cited references and the most-cited citing papers. Across seeds it ranks references by how many seeds cite them, then by citation count: the seminal-paper candidates. `--max-refs` caps references fetched per seed (default 200).
3. **Use two or more seeds** when the goal is seminal papers. With one seed the "seminal" list is only that paper's most-cited references, which is dominated by general classics (datasets, optimizers).
4. **Filter by role.** Mark each listed paper as foundation of the topic, general tool (dataset, metric, library), or tangential. Drop general tools unless the user wants them.
5. **Look for recent follow-ups separately.** The forward list is sorted by citations, so it favours older papers. For the newest follow-ups, search with `paper-search` using the seed's method name and a recent `--year-from`.
6. **Go one more hop** only on the two or three most relevant new papers. Unbounded snowballing grows quickly and drifts off topic.
7. **Report** the lineage: what the seeds build on, what builds on them, and which papers the user should read first.

## Output format

```markdown
## Seeds
1. Title (year), DOI, N citations, R references

## Foundations (backward)
| Paper (year) | Cited by seeds | Citations | Role |
|---|---|---|---|

## Follow-up work (forward)
| Paper (year) | Citations | What it adds to the seed |
|---|---|---|

## Suggested reading order
1. ... because ...

## Coverage notes
- Seeds whose reference lists were missing or incomplete in OpenAlex
- Hops performed
```

## Quality bar and pitfalls

- Confirm each seed resolved to the intended paper. The script prints the seed's title; a wrong DOI silently explores the wrong graph.
- OpenAlex reference lists are incomplete for some papers, especially preprints and older scans. A seed showing 0 references is a data problem; try the published version's DOI.
- Records for famous preprints are sometimes duplicated with odd years or DOIs. Cross-check a surprising year against the publisher page before quoting it.
- Citation counts measure attention, not correctness. A highly cited paper may be the one everyone criticises.
- Forward citations lag. Papers from the last few months have few or none; use a dated keyword search for those.
- Describe what a citing paper adds only after reading its abstract.

## Related skills

- `paper-search` to resolve seeds and to find very recent follow-ups.
- `paper-summarizer` for the papers selected for reading.
- `systematic-review-prisma` uses this for backward and forward snowballing.
- `literature-review-writer` and `related-work-writer` to write up the lineage.
- `novelty-checker` uses this to check follow-ups of the closest prior work.
