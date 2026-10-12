---
name: related-work-writer
description: Writes the related-work section of a research paper, grouping prior work into a few lines of research and stating for each how the user's contribution differs. Use when the user asks to "write the related work section", "position my paper against prior work", "how do I differentiate from paper X", "my related work is just a list", or needs a background and related-work section for a conference or journal submission.
---

# Related Work Writer

Write a related-work section that does two jobs: shows the reader you know the area, and makes clear what your paper does that the others do not.

## When to use

- A conference or journal paper needs a related-work or background section.
- An existing section lists papers without positioning the contribution.

Hand off instead for a long standalone review (`literature-review-writer`) or to find out whether the idea is new at all (`novelty-checker`).

## Inputs

- The paper's contribution: the claims from the introduction, or the abstract.
- The prior work to cover: a `.bib` file, PDFs, or the output of `novelty-checker`. If the list is thin, search first with `paper-search`.
- Venue and its conventions: placement (after the introduction or before the conclusion), length (often 0.5 to 1 page in conferences), citation style.
- Whether the submission is double-blind.

## Workflow

1. **State the contribution in one sentence.** Everything in the section is selected relative to it.
2. **Group the prior work into 3 to 5 lines of research.** Typical groups: the same problem with other methods; the same method on other problems; the components you build on; alternative formulations; benchmarks and evaluations.
3. **For each group, record** the representative papers, what they have in common, the best current result or understanding, and their limitation relevant to your work.
4. **Write one paragraph per group:**
   - A bolded run-in heading or a topic sentence naming the line of work.
   - What the line does, citing several papers together where they share an idea.
   - One or two papers discussed individually: the closest and the strongest.
   - The contrast sentence: how your work differs and why that difference matters.
5. **Treat the closest paper carefully.** Describe it accurately and fairly, then state the precise difference (assumption, setting, guarantee, scale, supervision). Reviewers often include its authors.
6. **Include concurrent work.** Mention recent preprints that overlap, labelled as concurrent, with the difference stated.
7. **Check coverage** against the venue's last two years: search the venue name with the topic so the obvious papers are not missing.
8. **Verify every citation** says what you attribute to it, then run `citation-verifier`.

## Output format

```latex
\section{Related Work}

\paragraph{<Line of research 1>.}
<What this line does> \cite{a,b,c}. <Closest work> \cite{d} ... In contrast, our approach ...

\paragraph{<Line of research 2>.}
...
```

Or the same in Markdown. Alongside the section deliver:

- A positioning table: paper, what it does, how ours differs.
- A list of cited keys that are missing from the `.bib` file.
- Any claims about prior work you could not verify from the sources.

## Quality bar and pitfalls

- Never cite a paper you have not retrieved, and never describe one beyond what you have read. A wrong description of a reviewer's paper is costly.
- Every paragraph ends by relating the group to your work. A paragraph with no contrast is a list.
- State differences as facts ("requires paired data; ours does not"), not judgements ("suffers from", "fails to").
- Do not claim prior work "cannot" do something unless its authors say so or you tested it.
- Do not inflate novelty by omitting the closest paper. Reviewers will find it.
- For double-blind venues, cite your own prior work in the third person.
- Keep it proportionate. Depth belongs on the closest two or three works.
- Do not pad the reference list with papers you do not discuss.

## Related skills

- `novelty-checker` supplies the closest prior work and the differences.
- `paper-search` and `citation-graph-explorer` to check coverage.
- `paper-comparison-matrix` for the positioning table.
- `literature-review-writer` for the long-form version.
- `introduction-writer` so the gap stated in the introduction matches this section.
- `citation-verifier` and `bibtex-manager` for the references.
