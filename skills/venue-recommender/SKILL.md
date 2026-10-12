---
name: venue-recommender
description: Recommends journals and conferences for a paper by matching its topic and contribution to venue scope, checking where similar papers were published, and comparing indexing, review time, acceptance rate, cost, and deadlines, with a predatory-venue check. Use when the user asks "where should I submit this paper", "which journal fits my paper", "find conferences for my work", "is this journal predatory", "suggest Scopus or SCI indexed journals", or needs a ranked submission plan with backups.
---

# Venue Recommender

Produce a shortlist of venues where the paper fits and has a realistic chance, with every fact about each venue taken from a current source.

## When to use

- A paper is nearly ready and the venue is undecided.
- A paper was rejected and needs the next venue.
- The user wants to check a journal's legitimacy.

Hand off instead for formatting to the chosen venue (`latex-paper-formatter`) or the cover letter (`cover-letter-writer`).

## Inputs

- Title, abstract, and keywords, or the draft.
- Paper type and maturity: full study, short paper, work in progress, review, dataset.
- The user's constraints: indexing required by their institution (Scopus, Web of Science SCIE/SSCI/ESCI, UGC-CARE, ABDC, CORE rank), deadline (for example a thesis submission requirement), budget for article processing charges, open-access requirement, journal or conference preference.
- Venues already tried or ruled out.

## Workflow

1. **Characterise the paper**: field, subfield, method type, contribution type (new method, empirical study, application, theory, review), and honest strength (incremental, solid, strong).
2. **Find where similar work is published.** This is the strongest signal of fit.
   - Search with `paper-search` for the closest 15 to 20 papers from the last three years and tally their venues.
   - Check the venues of the paper's own most-cited references.
   - Use publisher matchers as a secondary input: Elsevier Journal Finder, Springer Journal Suggester, Wiley Journal Finder, IEEE Publication Recommender, JANE (biomedical).
3. **Build a longlist** of 8 to 12 venues from the tally.
4. **Collect current facts for each venue from its own website and the indexing databases**, with the date checked:
   - Aims and scope, and recent articles similar to this paper.
   - Indexing, verified at the source: the Scopus source list, the Web of Science Master Journal List, DOAJ for open-access journals, the UGC-CARE list where required.
   - Metrics, from the venue or the index: impact factor (Journal Citation Reports), CiteScore, SJR quartile, CORE rank for CS conferences. Give the year of each metric.
   - Time to first decision and to publication, acceptance rate, where the venue reports them.
   - Cost: article processing charge, page charges, waivers.
   - Conferences: submission deadline, notification date, location and dates, proceedings publisher and indexing, page limit.
   - Format rules that affect effort: length, template, double-blind.
5. **Check legitimacy.** Warning signs of a predatory or low-quality venue: unsolicited email invitations; promised acceptance or review in days; fees not stated up front; a scope covering unrelated fields; editorial board members who cannot be verified; false indexing or impact-factor claims; a name imitating a known journal (check for hijacked or cloned journal sites by confirming the URL from the index's own record). Use the Think. Check. Submit. checklist.
6. **Score fit and tier.** For each venue: scope fit (high, medium, low), a realistic assessment of chances given the paper's strength, and whether it meets the user's constraints.
7. **Recommend a ladder**: one ambitious venue, two or three realistic ones, and one safe option, in submission order, with the reformatting effort between steps. One venue at a time: simultaneous submission of the same paper is misconduct.
8. **State what to confirm** before submitting: deadline, limits, fees.

## Output format

```markdown
## Paper profile
Field / contribution type / strength: ...
Constraints: ...

## Where similar papers appear
| Venue | Similar recent papers (n) | Examples |

## Shortlist (facts checked on <date>)
| Venue | Type | Scope fit | Indexing | Metric (year) | Decision time | Cost | Deadline | Source |
|---|---|---|---|---|---|---|---|---|

## Recommended order
1. <Venue>: why first; what would need changing
2. ...
Fallback: ...

## Legitimacy notes
## Confirm before submitting
```

## Quality bar and pitfalls

- Never state an impact factor, quartile, acceptance rate, deadline, fee, or indexing status from memory. Retrieve it and cite the source and date, or write "not verified".
- Indexing changes. Journals are added to and dropped from Scopus and Web of Science; verify on the index itself, not on the journal's own claims.
- A high metric does not mean a good fit. Scope fit and audience come first; out-of-scope submissions are desk-rejected.
- Be honest about the tier. Recommending only top venues for an incremental paper costs the author months.
- Do not recommend a venue with warning signs to meet a deadline or indexing requirement. Say plainly that fast, guaranteed publication is the mark of a predatory outlet.
- Conference deadlines repeat yearly but shift; give the current cycle's date from the call for papers.
- Check the venue's policy on preprints and on prior conference versions before recommending a journal extension.

## Related skills

- `paper-search` and `citation-graph-explorer` to find where similar work appears.
- `topic-trend-analyzer` to see which venues publish the topic.
- `abstract-writer` supplies the abstract used for matching.
- `self-peer-reviewer` for an honest read of the paper's strength.
- `latex-paper-formatter` and `camera-ready-checker` for the chosen venue's format.
- `cover-letter-writer` for the submission letter.
- `rebuttal-writer` when the venue has an author-response stage.
