---
name: research-gap-finder
description: Scans recent papers on a topic and lists open problems, contradictions between studies, and under-explored areas, each tied to the papers that reveal it. Use when the user asks "what are the research gaps in X", "what is still unsolved", "find me a thesis or paper topic in X", "where can I contribute", or wants open problems extracted from a set of papers they supply.
---

# Research Gap Finder

Produce a ranked list of research gaps, each backed by evidence from named papers. A gap is a specific question the literature has not answered, and the list must show why you believe that.

## When to use

- The user has a topic and wants to know what is still open.
- The user has a pile of papers and wants the gaps across them.

Hand off instead when:

- The user already has an idea and wants to know if it is new: use `novelty-checker`.
- The user wants publication counts and hot subfields: use `topic-trend-analyzer`.

## Inputs

- Topic, as narrow as the user can state it. If it is as broad as "machine learning in healthcare", ask for one narrowing choice (task, population, modality, or method family) before searching.
- Time window. Default: the last 3 years, plus the most recent survey of any age.
- Field and target output (thesis, conference paper, grant), because they change which gaps are feasible.
- Any papers the user already has.

## Workflow

1. **Collect a corpus.** Use `paper-search` to gather 25 to 40 papers: recent surveys first, then the most-cited recent work, then the newest preprints. Record the queries used.
2. **Read where gaps are stated.** For each paper read the abstract, the limitations and future-work sections, and the conclusion. For surveys read the "open challenges" section in full. Use full text when it is available; say so when only abstracts were read.
3. **Extract candidate gaps** into a working table: paper, claim or limitation, type. Use these types:
   - *Stated*: authors name it as future work or a limitation.
   - *Contradiction*: two papers report conflicting findings on the same question.
   - *Coverage*: a population, language, domain, scale, or setting no paper evaluates.
   - *Method*: a missing baseline, an assumption nobody tests, an evaluation everyone shares that has a known flaw.
   - *Transfer*: a technique established in a neighbouring area and not yet tried here.
4. **Cluster** candidates that describe the same gap, and keep every supporting paper.
5. **Check each cluster is still open.** Run one targeted search per gap for work from the last 18 months that closes it. Drop closed gaps or restate what remains.
6. **Rank** by evidence strength (how many independent papers point to it), importance (what changes if it is answered), and feasibility for this user.
7. **Report** using the format below, and offer `research-question-formulator` for the gap the user picks.

## Output format

```markdown
## Research gaps: <topic>
Corpus: <N> papers, <years>, sources searched, queries used. Full text read for <M>.

### 1. <Gap stated as an unanswered question>
- Type: stated | contradiction | coverage | method | transfer
- Evidence: <Paper A (year)> reports ...; <Paper B (year)> lists ... as future work.
- Why it matters: <one or two sentences>
- What a study would need: <data, method, resources>
- Confidence it is still open: high | medium | low, because <the check you ran>

### 2. ...

## Gaps considered and dropped
- <gap>: closed by <paper>.

## Coverage limits
- <what was not searched or not read in full>
```

Give 5 to 8 gaps. Fewer, well-supported gaps are better than a long list.

## Quality bar and pitfalls

- Every gap cites at least one real paper you retrieved, with title and year. Never cite from memory without retrieving the record.
- "Little research exists on X" needs a search that shows it. State the query and the count.
- Do not present the absence of a paper in your sample as proof nobody has done it. Report it as "not found in this search".
- A contradiction needs both sides named, with the conditions under which each result was obtained. Many apparent contradictions are differences in dataset or metric.
- Avoid gaps that are just "apply method M to dataset D" unless there is a reason the result would be informative.
- If only abstracts were read, say so in the corpus line. Limitations rarely appear in abstracts.

## Related skills

- `paper-search` and `citation-graph-explorer` to build the corpus.
- `topic-trend-analyzer` to see whether a gap sits in a growing or fading area.
- `novelty-checker` to test a specific idea that comes out of a gap.
- `research-question-formulator` to turn a chosen gap into questions and hypotheses.
