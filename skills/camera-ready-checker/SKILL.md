---
name: camera-ready-checker
description: Runs final checks on a paper PDF and its sources before submission or camera-ready upload, covering page limit, page size, font embedding, PDF metadata, anonymisation for double-blind review, template compliance, references, figures, and required statements. Use when the user asks to "check my paper before submission", "camera-ready check", "is my paper anonymized", "check formatting and page limits", "PDF eXpress says my fonts are not embedded", "final submission checklist", or is about to upload to a conference or journal system.
---

# Camera-Ready Checker

Catch the mechanical problems that cause desk rejection or production delays: length, fonts, identity leaks, and missing required parts.

## When to use

- Before an initial submission, especially to a double-blind venue.
- Before uploading the camera-ready version after acceptance.
- When a publisher's checker (IEEE PDF eXpress, ACM TAPS, OpenReview validation) rejects the file.

Hand off instead for content review (`self-peer-reviewer`) or converting to the template (`latex-paper-formatter`).

## Inputs

- The PDF, and the LaTeX or Word sources.
- The venue's current formatting instructions and call for papers: page limit and what it excludes, paper size, template and version, anonymity policy, required sections and checklists, supplementary rules, file size limit.
- Stage: review submission or camera-ready.
- For anonymity checks: author names, institutions, usernames, project and grant names.

## Workflow

1. **Record the venue's rules** from its current instructions. Do not assume last year's limits.
2. **Run the PDF check:**

   ```bash
   python scripts/check_pdf.py paper.pdf --max-pages 9 --paper letter
   python scripts/check_pdf.py paper.pdf --max-pages 8 --paper a4 --anonymous \
     --names "Jane Doe,Example University,janedoe,ProjectName"
   ```

   It reports: page count and the page where the References heading starts; page size; every font with subtype and embedding status (Type 3 and non-embedded fonts are problems); PDF metadata; and, with `--anonymous`, possible identity leaks (author in metadata, listed names in text or metadata, an acknowledgements section, email addresses, non-anonymous repository links, and first-person references to prior work). `--format json` gives machine-readable output. The exit code is non-zero when a problem is found.
3. **Interpret the page count.** The script treats the page where References starts as the end of content. Confirm what the venue counts: some include references, acknowledgements, or appendices in the limit; some require appendices in a separate file.
4. **Check template compliance by eye**, comparing with the template's sample PDF: margins, column width, font and size, line spacing, title block, heading styles, caption style, page numbers and headers (present for review, often absent for camera-ready), and line numbers where required. Search the sources for space-saving hacks: `\vspace{-`, `\baselinestretch`, `\small` or `\footnotesize` around body text, altered `\textheight` or margins, `\looseness`, modified style files.
5. **Anonymity (review stage).** Beyond the script:
   - Self-citations in the third person ("Smith et al. [3] showed", not "we showed [3]").
   - No identifying acknowledgements, grant numbers, or institution names in text, figures, or screenshots.
   - Code and data links through an anonymising service; supplementary files and their metadata also anonymous.
   - File names and embedded figure metadata without author names.
   - Clear the PDF metadata (`\hypersetup{pdfauthor={}}` or the template's anonymous option).
6. **Fonts and figures.** For Type 3 fonts, regenerate matplotlib figures with `pdf.fonttype` set to 42 (`publication-figure-maker`). Check figure resolution (300 dpi or more for raster images), legibility at printed size, and readability in greyscale.
7. **References and cross-references.** No `[?]` or `??` in the PDF; no "Error! Reference source not found"; all figures and tables referenced in the text; reference list complete and in the venue's style; DOIs where required. Run `citation-verifier` if not already done.
8. **Required content.** Abstract within the limit; keywords; required sections and statements (limitations, ethics, broader impact, data availability, funding, conflicts, author contributions); the venue's checklist included (`reproducibility-checklist`).
9. **Camera-ready extras.** Author names, affiliations, and emails exactly as registered; acknowledgements and funding restored; copyright or licence block and the correct conference or DOI information in the template; PDF title and author metadata set; accessibility requirements (alt text, tagged PDF) where the publisher asks; the publisher's validator passed; copyright form submitted; reviewers' required changes made.
10. **Final proofread of the first page and all captions**, then report.

## Output format

```markdown
## Pre-submission check: <paper>, <venue> (<stage>)
Rules taken from: <URL, date>

| Check | Result | Detail |
|---|---|---|
| Page limit (9 + refs) | PASS | content ends p. 9; refs start p. 9 |
| Page size | PASS | letter |
| Fonts embedded, no Type 3 | FAIL | Type 3: DejaVuSans (Fig. 4) |
| Anonymity | FAIL | acknowledgements section p. 9; github.com/... p. 6 |
| Template unmodified | PASS | no spacing overrides found |
| References resolve | PASS | |
| Required sections | FAIL | limitations section missing |

## Must fix before upload
1. ...
## Should fix
## Could not check (needs your confirmation)
```

## Quality bar and pitfalls

- Run the script on the final PDF, the exact file to be uploaded, after the last compile.
- The script checks mechanics only. It cannot measure margins or judge template fidelity, and it cannot see names inside images. Say what was and was not checked.
- Report a failed check as failed. Do not suggest hiding a length overrun with spacing tricks; venues detect and reject these. Cut content instead.
- An empty anonymity report does not prove anonymity: the name list must be complete, and writing style, dataset names, and URLs can still identify authors.
- Do not edit content at this stage without telling the authors. For camera-ready, changes beyond what reviewers requested may need the chairs' approval.
- Take limits from the current call, and quote the source in the report.
- Keep a copy of exactly what was submitted.

## Related skills

- `latex-paper-formatter` to fix template and compile problems.
- `publication-figure-maker` to regenerate figures with embedded fonts.
- `citation-verifier` and `bibtex-manager` for the reference list.
- `reproducibility-checklist` for the venue checklist.
- `self-peer-reviewer` for content issues found late.
- `cover-letter-writer` for the rest of a journal submission package.
- `academic-tone-editor` when cuts are needed to meet the limit.
