---
name: topic-trend-analyzer
description: Measures how a research topic is trending by counting publications per year, comparing the topic's share of all indexed papers, and finding the subtopics and keywords that are rising fastest. Use when the user asks "is X a hot topic", "is this field growing or saturated", "show publication trends for X", "which subfields are emerging", or needs trend evidence for a proposal's motivation section.
---

# Topic Trend Analyzer

Answer "how is this topic moving?" with counts from OpenAlex, and separate real growth from the growth of the literature as a whole.

## When to use

- Choosing between topics, or deciding whether an area is rising, mature, or fading.
- Supporting a motivation paragraph with numbers.

Hand off instead when the user wants specific open problems (`research-gap-finder`) or the key papers (`citation-graph-explorer`).

## Inputs

- The topic as a phrase that would appear in a title or abstract. Ask for alternative names (for example "LLM" and "large language model").
- Year range. Default: the last 10 complete years.
- Optional comparison topics.

## Workflow

1. **Run the trend script** for the topic and for each synonym or comparison topic:

   ```bash
   python scripts/trend_counts.py "diffusion models" --from 2016
   python scripts/trend_counts.py "federated learning" --from 2018 --window 2 --format json
   ```

   - The query is matched as an exact phrase in titles and abstracts. Add `--fulltext` to match the words anywhere, which is wider and noisier.
   - The current year is excluded by default because it is incomplete.
   - `--window N` sets the length of the two periods compared for rising subtopics and keywords.
2. **Check the query is measuring the topic.** Look at the rising subtopics. If unrelated fields appear (a search for "transformer" returning electrical engineering), tighten the phrase and rerun.
3. **Read the three signals together:**
   - *Count per year*: raw volume.
   - *Share per 10,000 indexed papers*: volume relative to everything published. A rising count with a flat share means the topic is only keeping pace.
   - *Compound annual growth*: one number for the whole range. It hides shape, so look at the series too.
4. **Classify the stage**: emerging (small counts, fast growth), rapid growth, plateau (share flat for 2 or more years), or decline.
5. **Interpret the rising lists.** "under N" in the Earlier column means the group was outside the 200 largest in the earlier window, so its true count is unknown and below N. Treat such rows as "new or emerging", not as growth from zero.
6. **Add context** the counts cannot give: a landmark paper, dataset, or tool release that explains an inflection. Verify it with `paper-search` before stating it.
7. **Report** with the table, a plot if the user wants one (`publication-figure-maker`), and the caveats.

## Output format

```markdown
## Trend: <topic>, <from> to <to>
Query: "<phrase>" in title and abstract (OpenAlex, retrieved <date>).

| Year | Papers | Share per 10,000 |
|---|---|---|

- Stage: <emerging | rapid growth | plateau | decline>
- Compound annual growth: <x>%
- Inflection: <year>, plausibly due to <verified event>, or "no clear cause identified"

## Rising subtopics
| Subtopic | Earlier window | Recent window | Change |

## Rising keywords
| Keyword | Earlier window | Recent window | Change |

## What this means for you
<two to four sentences tied to the user's decision>

## Caveats
```

## Quality bar and pitfalls

- Report the exact query. Trend numbers are meaningless without it, and synonyms change counts by large factors.
- Always give the share alongside the count. Global publication volume grows every year.
- Recent years are undercounted because indexing lags. Flag the last complete year as provisional.
- Publication volume is not quality or opportunity. A crowded topic can still have gaps, and a quiet one can be quiet for good reason.
- OpenAlex topic and keyword labels are assigned automatically and can be wrong. Treat them as hints.
- Do not attribute an inflection to an event you have not verified.

## Related skills

- `paper-search` to find the papers behind an inflection.
- `research-gap-finder` to look for open problems inside a rising subtopic.
- `publication-figure-maker` to plot the series.
- `venue-recommender` to see where the topic is being published.
- `weekly-paper-digest` to keep following the topic.
