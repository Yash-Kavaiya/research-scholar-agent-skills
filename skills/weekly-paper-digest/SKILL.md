---
name: weekly-paper-digest
description: Produces a recurring digest of new papers in the user's research area from arXiv and OpenAlex for saved queries, skipping papers already reported, ranking by relevance, and adding a short note on why each top paper matters, with instructions for running it on a schedule. Use when the user asks to "send me new papers every week", "set up a paper digest", "what is new in my field this week", "track new arXiv papers on X", "keep me updated on my topic", or wants a literature alert.
---

# Weekly Paper Digest

Keep the user current with a short, filtered list of new papers, generated the same way each time so nothing is repeated and little is missed.

## When to use

- The user wants regular updates on one or more topics.
- A one-off "what appeared recently on X".
- Watching for competing or concurrent work during a project.

Hand off instead for a full literature search (`paper-search`) or long-term trend analysis (`topic-trend-analyzer`).

## Inputs

- Topics, as 2 to 6 search queries. Ask for the terms the user's community uses, and for arXiv categories if relevant (`cs.CL`, `stat.ML`, `q-bio.GN`).
- Period (default 7 days) and how many papers they want to see (default: top 10 to 15).
- Terms that raise priority: methods, datasets, or author groups the user follows.
- Where the digest should go: a file in the project, or a message.
- Whether it should run on a schedule.

## Workflow

1. **Write the queries.** Keep each to a phrase of 2 to 4 words. For arXiv, field syntax narrows results: `cat:cs.CL AND all:hallucination`, `ti:"graph neural"`, `au:lastname`. Plain phrases are searched as all words required on arXiv and as an exact phrase in title or abstract on OpenAlex.
2. **Save a config file** so every run uses the same settings:

   ```json
   {
     "queries": ["retrieval augmented generation", "cat:cs.CL AND all:hallucination"],
     "days": 7,
     "sources": ["arxiv", "openalex"],
     "max_per_query": 15,
     "boost": ["benchmark", "survey", "low-resource"],
     "state": "digest-seen.json"
   }
   ```

3. **Run the digest:**

   ```bash
   python scripts/digest.py --config digest.json --out digests/2026-03-09.md
   python scripts/digest.py --query "diffusion models" --query "cat:cs.CV AND all:video generation" --days 7
   ```

   The script fetches the newest arXiv submissions and recent OpenAlex articles and preprints per query, keeps those dated within the period (future-dated records are discarded), merges duplicates across queries and sources, drops anything recorded in the state file from earlier runs, and ranks by number of matching queries, then boost terms, then date. The state file is updated after each run; `--no-state` leaves it untouched for a trial run.
4. **Check the output.** If a source failed, the digest says so at the top; that source is not covered for this period, so rerun or note it. If results are off-topic, tighten the query; if empty, loosen it or lengthen the period.
5. **Curate.** Read the titles and abstracts returned. Select the papers that matter for this user and write one or two lines for each: what it does and why it is relevant to their work. Base this on the abstract, and say so; open the paper for anything that looks important or competing.
6. **Flag what needs action**: a paper that overlaps the user's current project (suggest `novelty-checker`), a new dataset or baseline, a survey worth reading in full.
7. **Deliver** the digest in the format below and save it next to earlier digests.
8. **Schedule it** if asked:
   - In Claude Code, use the `/schedule` command (or `/loop` within a session) with a prompt such as "Run the weekly-paper-digest skill with digest.json and save to digests/".
   - With cron: `0 8 * * 1 cd /path/to/project && python /path/to/scripts/digest.py --config digest.json --out digests/$(date +\%F).md`
   - On Windows, a Task Scheduler job running the same command weekly.

   A scheduled script run produces the raw list; the curation in step 5 needs an agent run.
9. **Review the queries every month or two**: add terms from papers the user found useful, and drop queries that only return noise.

## Output format

```markdown
# Paper digest: 2026-03-02 to 2026-03-09
Queries: `...`; `...`. Sources: arXiv, OpenAlex. <N> new papers; <k> selected.

## Read first
1. **Title** (authors, date, venue or arXiv id) <link>
   What: ...  Why it matters to you: ...
   Based on: abstract | full text

## Also relevant
- **Title** <link>: one line

## Needs action
- <paper> overlaps with your current project on X: run a novelty check.

## Not covered this period
- <source that failed, or none>
```

## Quality bar and pitfalls

- List only papers the script returned. Do not add papers from memory, and do not describe a paper beyond what its abstract or text says.
- A digest is not a complete search. arXiv and OpenAlex miss work in other venues and index with a delay; recent journal articles may appear weeks late.
- Preprints are not peer reviewed. Mark them, and be careful with strong claims in abstracts.
- Keep the state file with the project. Deleting it repeats old papers; sharing one state file across unrelated topics hides papers.
- arXiv asks clients to pause between requests; the script waits three seconds per call. Do not remove the delay or run it in tight loops.
- Fewer, better-chosen papers are more useful than a long list the user will not read. Ten is plenty.
- Say when a period returned nothing; silence can also mean the query is broken.

## Related skills

- `paper-search` for a deeper search when a digest item opens a new thread.
- `paper-summarizer` for papers selected to read in full.
- `novelty-checker` when a new paper overlaps the user's idea.
- `topic-trend-analyzer` for the longer view of the same topics.
- `research-progress-tracker` to log papers to read and follow-ups.
- `bibtex-manager` to add selected papers to the project's bibliography.
