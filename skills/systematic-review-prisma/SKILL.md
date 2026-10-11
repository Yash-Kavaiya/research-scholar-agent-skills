---
name: systematic-review-prisma
description: Runs a systematic literature review following PRISMA 2020, covering the protocol, database search strings, de-duplication, two-stage screening against inclusion criteria, data extraction, quality appraisal, and the flow diagram with checked counts. Use when the user says "systematic review", "systematic literature review", "SLR", "PRISMA", "scoping review", "write search strings for Scopus and PubMed", "screen these records", or "make a PRISMA flow diagram".
---

# Systematic Review (PRISMA 2020)

Carry out a review that someone else could repeat: a written protocol, documented searches, explicit criteria, recorded decisions, and a flow diagram whose numbers add up.

## When to use

- A systematic review, scoping review (PRISMA-ScR), or systematic mapping study.
- Any single stage of one: search strings, screening, extraction, or the flow diagram.

Hand off instead for a narrative or thematic review without a protocol (`literature-review-writer`).

## Inputs

- Review question, and the review type (systematic, scoping, mapping, rapid).
- Databases the user can access (Scopus, Web of Science, PubMed, IEEE Xplore, ACM DL, PsycINFO, ERIC). Access decides the search plan.
- Date range, languages, publication types.
- Number of reviewers. One-reviewer screening is a limitation that must be reported.

## Workflow

1. **Protocol.** Write it before searching: question in PICO, PECO, or SPIDER form (`research-question-formulator`), eligibility criteria, databases, search strategy, screening process, extraction fields, appraisal tool, synthesis method. Recommend registering it (PROSPERO for health, OSF otherwise).
2. **Eligibility criteria.** A table of inclusion and exclusion criteria, each testable from a title, abstract, or full text. Number them; exclusion reasons at full text cite these numbers.
3. **Search strings.** Build concept blocks: synonyms joined with OR inside a block, blocks joined with AND. Then write the string in each database's syntax:
   - Scopus: `TITLE-ABS-KEY(("machine learning" OR "deep learning") AND (diagnos* OR detect*))`
   - Web of Science: `TS=(("machine learning" OR "deep learning") AND (diagnos* OR detect*))`
   - PubMed: `("machine learning"[tiab] OR "Machine Learning"[Mesh]) AND (diagnos*[tiab] OR detect*[tiab])`
   - IEEE Xplore: `("All Metadata":"machine learning" OR "All Metadata":"deep learning") AND ...`

   Test each string against 3 to 5 known relevant papers; if any is missed, revise. Record the final string, database, date, and hit count.
4. **Export and de-duplicate.** The user exports results as CSV or RIS (the agent usually cannot query subscription databases). Then:

   ```bash
   python scripts/prisma_flow.py dedupe pubmed.ris scopus.csv wos.csv --out screening.csv --counts counts.json
   ```

   This merges the exports, removes duplicates by DOI and normalized title, writes `screening.csv` with empty decision columns, and records identification counts.
5. **Title and abstract screening.** Fill `title_abstract_decision` with `include` or `exclude` for every row, applying the criteria. When in doubt, include; doubt is resolved at full text. With two reviewers, screen independently and report agreement (Cohen's kappa).
6. **Full-text screening.** For each included row, fill `fulltext_decision` with `include`, `exclude`, or `not_retrieved`. Every exclusion needs an `exclusion_reason` using a fixed short list tied to the criteria ("Wrong population", "No empirical data").
7. **Snowball.** Run `citation-graph-explorer` on the included studies and screen the additions the same way. PRISMA 2020 reports these under "other methods"; report their counts separately in the text.
8. **Tally and draw the flow diagram.**

   ```bash
   python scripts/prisma_flow.py tally screening.csv --counts counts.json
   python scripts/prisma_flow.py diagram counts.json --format mermaid   # or --format tikz
   ```

   `tally` refuses incomplete sheets (missing decisions or reasons). `diagram` refuses counts that do not add up and names the inconsistent box.
9. **Extract data** from included studies into a table with predefined fields (`paper-comparison-matrix`).
10. **Appraise quality or risk of bias** with a tool suited to the designs: RoB 2 (randomised trials), ROBINS-I (non-randomised), CASP (qualitative), JBI checklists, QUADAS-2 (diagnostic), MMAT (mixed). Report per-study judgements.
11. **Synthesize.** Narrative or thematic synthesis by default; meta-analysis only when studies are similar enough in design, outcome, and measure. Report heterogeneity.
12. **Write up** against the PRISMA 2020 checklist (27 items) and state which items are not applicable.

## Output format

Deliver these files, plus the manuscript sections on request:

- `protocol.md`: question, criteria table, databases, search strings, process.
- `search-log.md`: table of database, date, exact string, hits.
- `screening.csv`: every record with decisions and reasons.
- `counts.json` and the flow diagram (Mermaid or TikZ).
- `extraction.csv` and the quality-appraisal table.
- A PRISMA checklist table: item, where reported.

## Quality bar and pitfalls

- Never invent hit counts, screening decisions, or flow-diagram numbers. Every number comes from the exported files and the screening sheet.
- The free APIs in `paper-search` do not replace Scopus or Web of Science. If the user has no database access, use them and state that the search covered OpenAlex, PubMed, and so on, by name.
- A string that was never tested against known relevant papers is a draft.
- Screening decisions made by an AI assistant must be reported as such in the methods, and a human should check a sample at least. Say this to the user.
- Excluding at full text without a recorded reason breaks the flow diagram and the review.
- Do not pool results from incompatible designs or outcomes to obtain a single number.
- Scoping reviews do not need quality appraisal; systematic reviews do. Do not mix the labels.

## Related skills

- `research-question-formulator` for the PICO or SPIDER question.
- `paper-search` for open-database searching and `citation-graph-explorer` for snowballing.
- `paper-comparison-matrix` for the extraction table.
- `paper-critic` for per-study appraisal reasoning.
- `literature-review-writer` to write the synthesis.
- `bibtex-manager` to clean the included-studies bibliography.
- `publication-figure-maker` for forest plots and summary charts.
