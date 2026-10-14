# Digest configuration

```json
{
  "queries": ["<query 1>", "cat:<category> AND all:<term>"],
  "days": 7,
  "sources": ["arxiv", "openalex"],
  "max_per_query": 15,
  "boost": ["<term>", "<term>"]
}
```

Schedule: <day and time>, via <scheduler>   State file: kept in <folder>
Reviewed on: <date>   Changes: <...>

---

# Paper digest: <start date> to <end date>

**Queries:** <...>   **Sources:** <...>   **New papers:** <n>; selected: <n>
**Not covered this period:** <failed sources or none>

## Read first

1. **<Title>** (<authors>, <date>, <venue or arXiv id>) <link>
   What: <...>   Why it matters to you: <...>   Based on: abstract | full text

## Also relevant

- **<Title>** <link>: <one line>

## Needs action

- <paper>: overlaps with <project>; run a novelty check.
- <paper>: new dataset or baseline <name>.

## Query notes

- <queries returning noise or missing papers; proposed changes>
