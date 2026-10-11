---
name: plagiarism-and-paraphrase-checker
description: Compares a draft with the sources it drew on, flags sentences that are copied verbatim or paraphrased too closely, checks quotations and citations are in place, and helps the author fix each passage by quoting, citing, or rewriting from understanding. Use when the user asks to "check my draft for plagiarism", "is this paraphrase too close to the original", "did I paraphrase this properly", "check my literature review against these papers", "check for self-plagiarism", or wants to make sure their writing is properly attributed before submission.
---

# Plagiarism and Paraphrase Checker

Find the places where a draft is too close to its sources, and fix them properly: quote and cite, cite, or rewrite from the idea. The goal is correct attribution.

## When to use

- Before submitting a paper, thesis chapter, or assignment that draws on sources.
- When the author is unsure whether a paraphrase is far enough from the original.
- When reusing the author's own earlier text (self-plagiarism or text recycling).

Hand off instead to verify references exist (`citation-verifier`) or for a general language edit (`academic-tone-editor`).

**Scope.** This skill helps authors attribute their own work correctly. Do not use it to disguise copied text so that similarity software misses it, or to reword someone else's work for submission as the user's own. If that is the request, decline that part and offer the proper fix: quote, cite, or write from understanding.

## Inputs

- The draft, as plain text or Markdown (convert PDF or Word to text first).
- The source texts the draft drew on, as text files. The check is only as complete as this set.
- The citation style, and the institution's or venue's rules on similarity and on reuse of the author's earlier work.

## Workflow

1. **Collect the sources.** Ask which papers each section was written from. For a literature review, that means the papers discussed in it. Convert each to text (`pdftotext paper.pdf paper.txt`, or pandoc for Word).
2. **Run the comparison:**

   ```bash
   python scripts/similarity.py draft.txt source1.txt source2.txt source3.txt
   python scripts/similarity.py draft.md paper.txt --min-run 6 --threshold 0.4 --format json
   ```

   For every draft sentence, the script finds the longest run of consecutive words shared with a source and the share of the sentence's word trigrams found in a source, then flags:

   | Flag | Criterion (defaults) | Meaning |
   |---|---|---|
   | `verbatim` | 8 or more consecutive shared words, not in quotation marks | Copied text presented as the author's own |
   | `close_paraphrase` | 50% or more of the sentence's trigrams shared | Source's sentence with words swapped |
   | `quoted` | A copied run inside quotation marks | Fine if cited with a page number; check it |

   `--min-run` and `--threshold` tighten or loosen the criteria. The exit code is non-zero when anything other than quotes is flagged.
3. **Review each flag in context.** Some matches are legitimate: technical terms, method and dataset names, standard phrases of the field ("the results are shown in Table"), and properly quoted material. Dismiss these with a note.
4. **Look beyond the script.** Lexical overlap misses:
   - *Structural paraphrase*: the same sequence of ideas and sentence structure as the source, with all words changed. Compare paragraphs with their source paragraphs.
   - *Idea plagiarism*: an idea, argument, or finding from a source stated without citation, in entirely new words.
   - *Translated text*: copied from a source in another language.
   - *Figures, tables, and data* reused without permission or credit.
5. **Check every borrowed idea has a citation** next to it, and every direct quotation has quotation marks, a citation, and a page number.
6. **Fix each flagged passage** with the author, choosing one:
   - *Quote it*: when the exact words matter. Add quotation marks, citation, and page.
   - *Cite and rewrite from understanding*: close the source, state the point in the context of the author's own argument (why it matters here, how it relates to other sources), then check against the source for accuracy. Changing words within the source's sentence is not a rewrite.
   - *Synthesize*: combine the point with what other sources say, so the sentence is the author's analysis.
   - *Remove it* if it is not needed.
7. **For the author's own earlier work**: reuse of published text needs a citation to the original and, often, the publisher's permission; methods sections have more latitude in many fields, but the venue's policy governs. Thesis reuse of the author's papers follows the university's rules.
8. **Rerun** the comparison after the fixes and report what remains.

## Output format

```markdown
## Similarity check
Draft: <file>, <N> sentences. Compared with: <list of source files>.
Flagged: <a> verbatim, <b> close paraphrase, <c> quoted. Overall trigram overlap: <x>%.

### Passages to fix
| # | Draft sentence | Source | Issue | Recommended fix |
|---|---|---|---|---|

### Dismissed matches
- Sentence 14: standard method description and dataset name.

### Attribution gaps (found by reading)
- Paragraph 3 presents <idea> from <source> without a citation.

### Not covered
- Sources not supplied: ...; no web or database comparison was run.
```

## Quality bar and pitfalls

- State the coverage. This compares the draft with the supplied files only. It is not a web-wide or publisher-database check, and a clean result here does not predict a similarity score from institutional software.
- Never report a percentage as "the plagiarism score". Similarity is evidence to review, and plagiarism is a judgement about attribution.
- A citation does not make copied wording acceptable. Verbatim text needs quotation marks as well.
- Do not fix a close paraphrase by substituting synonyms. That leaves the source's structure and remains too close, and it defeats the purpose of the check.
- Do not rewrite quotations, and do not change the meaning of the source when rewriting.
- Keep legitimately shared technical wording. Forcing odd synonyms for standard terms damages the text.
- Be straightforward with the author about serious cases: long unattributed passages need substantial rewriting or quotation, not polishing.

## Related skills

- `citation-verifier` to confirm that cited sources say what is attributed to them.
- `literature-review-writer` and `related-work-writer`, whose synthesis approach avoids close paraphrase in the first place.
- `paper-summarizer` to understand a source well enough to write about it independently.
- `academic-tone-editor` for the language pass after attribution is fixed.
- `thesis-chapter-writer` for reuse of the author's published papers in a thesis.
- `camera-ready-checker` as part of the pre-submission checks.
