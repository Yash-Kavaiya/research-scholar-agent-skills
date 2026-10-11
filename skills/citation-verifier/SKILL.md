---
name: citation-verifier
description: Verifies that every reference in a bibliography or manuscript exists in Crossref, OpenAlex, or arXiv with matching title, authors, and year, and then checks that each cited source supports the sentence that cites it. Catches fabricated and hallucinated citations. Use when the user asks to "check my references", "verify these citations", "are these references real", "check for hallucinated citations", "does this paper actually say that", or before submitting any document whose references came from an AI tool or from memory.
---

# Citation Verifier

Two checks for every reference: does it exist as cited, and does it say what the text claims it says. The first is done by script; the second requires reading the source.

## When to use

- Before submitting any paper, thesis, proposal, or report.
- Whenever references were produced by an AI assistant, copied from another paper's reference list, or typed from memory.
- When a reviewer or supervisor questions a citation.

Hand off instead for formatting and de-duplicating a `.bib` file (`bibtex-manager`) or switching citation style (`citation-style-converter`).

## Inputs

- The references as a `.bib` file. If they are in a Word or plain-text list, convert them first (paste each into `paper-search`, or use the Crossref lookup in `bibtex-manager`).
- The manuscript (`.tex` or text), for the claim check.
- Access to the cited papers' full text where possible.

## Workflow

1. **Run the existence check:**

   ```bash
   python scripts/verify_citations.py references.bib
   python scripts/verify_citations.py references.bib --tex paper.tex --format json --out citation-report.json
   ```

   Each entry is looked up by DOI (Crossref, then OpenAlex), by arXiv id, and otherwise by title search, and receives a status:

   | Status | Meaning | Action |
   |---|---|---|
   | `verified` | A record was found; title, year, and first author agree | Proceed to the claim check |
   | `mismatch` | A record exists but fields differ (wrong year, wrong author, DOI points to another paper, DOI does not resolve) | Correct the entry from the database record |
   | `possible_match` | Only a loosely similar title was found | Open the candidate and confirm by hand |
   | `not_found` | No record in Crossref or OpenAlex | Treat as suspect; see step 2 |
   | `lookup_failed` | A database could not be reached | Rerun later; this says nothing about the reference |

   The exit code is non-zero unless every entry is verified.
2. **Investigate `not_found` entries.** Search the exact title in quotes on the web, on Google Scholar, and on the publisher's or journal's site; check the first author's publication list. Books, theses, technical reports, standards, and older or non-English work are often not indexed, and are real. If nothing turns up anywhere, the reference is very likely fabricated: remove it and find a real source for the claim with `paper-search`, or remove the claim.
3. **Fix `mismatch` entries** from the matched record. A common pattern in fabricated references is a real title with invented authors or venue, or a real DOI attached to a different paper. Do not "fix" by keeping the invented parts.
4. **Check claims against sources.** With `--tex`, the report lists the sentences that cite each key. For each one:
   - Open the source (abstract at minimum; the relevant section for specific claims, numbers, and quotations).
   - Judge: *supports* (the source states this), *partially supports* (weaker, narrower, or conditional), *does not support* (says something else, or the opposite), *cannot verify* (no access to full text).
   - Check quoted text word for word, and numbers digit for digit, with a page or section.
5. **Check the text and the list against each other.** The report lists keys cited but missing from the `.bib`, and entries never cited.
6. **Watch for citation problems beyond existence:** a retracted paper (check the publisher page or Retraction Watch); a preprint cited when a published version exists; a secondary source cited for a primary finding; a review cited for an original result.
7. **Report** every reference's status and every claim judgement, with the corrections made.

## Output format

```markdown
## Citation verification report
Checked <N> references on <date> against Crossref, OpenAlex, arXiv.
<a> verified, <b> mismatch, <c> possible match, <d> not found, <e> lookup failed.

### Existence
| Key | Status | Problem | Correction |
|---|---|---|---|

### Claim support
| Key | Sentence | Verdict | Evidence (source location) | Fix |
|---|---|---|---|---|
| smith2021 | "X improves Y by 30% \cite{smith2021}." | partially supports | reports 30% on one of three datasets (Table 2) | add the condition |

### Cited but not in the bibliography
### In the bibliography but never cited
### Could not verify (no full-text access)
```

## Quality bar and pitfalls

- Never mark a reference verified from memory. Verified means a database record was retrieved in this run.
- `not_found` is a warning, not a verdict. State what else was checked before calling a reference fabricated.
- Never repair a suspect reference by inventing plausible details. Replace it with a retrieved record or remove it.
- A real paper cited for something it does not say is still a citation error. The existence check alone is half the job.
- Say which claims were checked against full text and which only against an abstract. Abstract-level checks cannot confirm specific numbers.
- A title-search match can be a different paper with a similar title. Compare authors, year, and venue.
- Be honest about coverage: list everything that could not be verified so the author can check it.

## Related skills

- `bibtex-manager` to clean and complete entries after verification.
- `paper-search` to find a real source for a claim whose reference was removed.
- `citation-style-converter` once the list is correct.
- `paper-summarizer` to read a source closely for the claim check.
- `self-peer-reviewer` and `camera-ready-checker` run this before submission.
- `literature-review-writer`, `related-work-writer`, and `introduction-writer` should all end with this check.
