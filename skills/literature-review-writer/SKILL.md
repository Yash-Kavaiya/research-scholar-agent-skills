---
name: literature-review-writer
description: Writes a literature review organised by themes, debates, and gaps instead of one paragraph per paper, with every claim tied to sources the user has supplied or that were retrieved. Use when the user asks to "write a literature review", "write chapter 2", "synthesize these papers", "turn my notes into a review", "my review reads like a list of summaries", or needs a survey-style background section.
---

# Literature Review Writer

Write a review that argues something about the state of knowledge. Each paragraph makes a point about the literature and uses several sources to support it.

## When to use

- A thesis literature-review chapter, a review article, or an extended background section.
- Restructuring a paper-by-paper draft into a synthesis.

Hand off instead for a short related-work section positioned against a specific contribution (`related-work-writer`), a protocol-driven review (`systematic-review-prisma`), or annotated entries (`annotated-bibliography-builder`).

## Inputs

- The sources: PDFs, notes, summaries, a `.bib` file, or a comparison matrix. If there are none, build the corpus first with `paper-search`.
- The review's purpose and the research question it leads to.
- Length, citation style, and audience (examiner, journal reader, general).
- The user's own position, if they have one. The review should build toward their study.

## Workflow

1. **Inventory the sources.** List each with a one-line note on what it contributes. Mark which were read in full, which only as abstracts, and which the user summarised.
2. **Build a synthesis matrix.** Rows are sources; columns are the themes, variables, or questions that recur. Fill cells with each source's finding or position. `paper-comparison-matrix` produces this.
3. **Find the structure in the matrix.** Choose one organising principle:
   - *Thematic*: by concept or sub-question (the default).
   - *Methodological*: by approach, when the methods are the debate.
   - *Chronological*: by period, only when the development of ideas is itself the point.
   - *Theoretical*: by framework or school.
4. **Outline with claims, not topics.** Each section heading gets a one-sentence claim about the literature ("Evidence for X is consistent in adults and absent in adolescents"). Show the outline to the user before drafting long reviews.
5. **Draft each paragraph** in this shape:
   - Topic sentence stating the point about the literature.
   - Evidence from two or more sources, compared: who agrees, who differs, and why (sample, method, measure, context).
   - Your evaluation: strength of evidence, limitations shared across the studies.
   - A link to the next point or to the gap.
6. **Write the transitions between sections** so the review moves from broad context to the specific gap.
7. **Close with the gap.** Summarise what is established, what is contested, and what is unknown, then state the gap the user's study addresses and how.
8. **Check every citation** against the source: does the cited paper say this? Then run `citation-verifier` on the finished text.

## Output format

```markdown
# Literature Review: <topic>

## 1. Introduction
Scope, how sources were found and selected, and how the review is organised.

## 2. <Theme stated as a claim>
Synthesised paragraphs with citations (Author, Year) or [n].

## 3. <Theme>
### 3.1 <Sub-theme>

## N. Summary and research gap
Established / contested / unknown, then the gap and the study that follows.

## References
```

Also deliver the synthesis matrix, and a list of claims you could not support from the supplied sources.

## Quality bar and pitfalls

- Cite only sources that were supplied or retrieved, and only for what they say. Never invent a reference or attach a real one to a claim it does not make. Mark unsupported statements `[citation needed]` for the user to resolve.
- Paragraphs that begin "Smith (2020) found ... Jones (2021) found ..." are summaries. Start with the idea and bring authors in as evidence.
- Compare and evaluate. A review that only reports is incomplete.
- Explain disagreements between studies by their differences in design or context where the sources allow it.
- Do not present a source you read only as an abstract as if you knew its methods.
- Keep direct quotation rare, and keep paraphrases far enough from the source wording (`plagiarism-and-paraphrase-checker`).
- Balance recency and foundations: include the seminal work and the last two years.
- Use one tense convention: past for specific findings, present for established knowledge.

## Related skills

- `paper-search` and `citation-graph-explorer` to build the corpus.
- `paper-summarizer` and `paper-comparison-matrix` to prepare the synthesis matrix.
- `research-gap-finder` to sharpen the closing gap statement.
- `related-work-writer` for the short, contribution-focused version.
- `citation-verifier` and `plagiarism-and-paraphrase-checker` before submission.
- `thesis-chapter-writer` when the review is a thesis chapter.
- `academic-tone-editor` for a final language pass.
