---
name: introduction-writer
description: Writes the introduction of a research paper or thesis as a funnel from context to problem to gap to contribution to outline, with claims that match the paper's results and citations the user has supplied. Use when the user asks to "write my introduction", "improve the intro", "write the motivation", "how do I state my contributions", "my introduction is too long or unfocused", or needs the opening section of a paper.
---

# Introduction Writer

Write an introduction that answers four questions in order: what is the problem, why does it matter, what is missing, and what does this paper add.

## When to use

- A paper or thesis chapter needs its introduction drafted or restructured.
- Contributions need to be stated clearly.

Hand off instead for the abstract (`abstract-writer`) or the full review of prior work (`related-work-writer`, `literature-review-writer`).

## Inputs

- The paper's contribution and main results (from the outline or the results section). Write the introduction after the results are known.
- The gap in prior work and the key references that establish it.
- Venue, audience, and length budget (often 1 to 1.25 pages for conference papers; longer for journals and theses).
- The user's `.bib` file or reference list.

## Workflow

1. **Fix the message**: one sentence stating what the paper shows and why it matters. The introduction exists to set up and deliver this sentence.
2. **Plan the moves** (the CARS model: establish a territory, establish a niche, occupy the niche), one paragraph each:
   1. *Context*: the area and why it matters, specific to this problem. Start close to the topic; skip the history of the field.
   2. *Problem*: the specific problem and the current state of solving it, with the key citations.
   3. *Gap*: what existing work does not do, stated precisely, with evidence. "However, ..." is the hinge of the introduction.
   4. *This paper*: what you do about the gap, in one or two sentences on the approach and why it should work.
   5. *Results and contributions*: the headline results with numbers, then the contributions.
   6. *Outline* of the paper: one or two sentences, only where the venue expects it.
3. **Write the contributions** as 2 to 4 specific, checkable items. Each names what was done and where the evidence is:
   - Weak: "We propose a novel framework for X."
   - Strong: "We introduce M, a method that does X without requiring Y (Section 3)."
   - Strong: "On benchmarks A and B, M reduces error by 12% relative to the best prior method at one third of the compute (Section 5)."
4. **Draft the paragraphs**, each starting with a sentence that states its point. A reader who reads only first sentences should follow the argument.
5. **Calibrate the claims** to the evidence: "we show" for demonstrated results, "we provide evidence that" for partial support. Match the wording used in the results section exactly.
6. **Place the citations.** Every statement about the field or prior work needs one from the supplied references. Mark statements that need a citation the user has not provided as `[citation needed]`.
7. **Point to Figure 1** if the paper has an overview figure, by the second or third paragraph.
8. **Check consistency** with the abstract, the related work, and the conclusion: same gap, same contributions, same numbers.

## Output format

```markdown
## Introduction (<N> words)
<paragraphs, with \cite{key} or (Author, Year) from the supplied references>

Our contributions are:
- ...
- ...

## Notes
- Paragraph plan: context / problem / gap / approach / results / outline
- [citation needed]: <statements still lacking a supplied source>
- Claims to verify against results: <list with section pointers>
```

## Quality bar and pitfalls

- Cite only supplied or retrieved references. Never invent a citation to support a sentence; mark the need instead.
- Do not state results the paper does not contain, or round them favourably.
- The gap must be real and specific. "Little attention has been paid to X" needs to be true; check with `novelty-checker` if unsure.
- Avoid openers that could start any paper ("In recent years, deep learning has achieved great success").
- Do not criticise prior work beyond what is needed to motivate yours, and be accurate about what it does.
- Contributions are things the paper delivers, not activities ("we conduct extensive experiments" is not a contribution; what the experiments show is).
- "Novel" and "first" are claims a reviewer will test. Use "first" only with a qualifier you can defend ("to our knowledge", plus a search).
- Keep to the length budget. An introduction that fills two pages of an eight-page paper takes space from the evidence.

## Related skills

- `paper-outline-generator` supplies the message, claims, and budget.
- `results-interpreter` supplies the claim wording the results support.
- `novelty-checker` and `research-gap-finder` back the gap statement.
- `related-work-writer` covers prior work in depth so the introduction can stay brief.
- `abstract-writer` compresses the same arc.
- `citation-verifier` checks the cited claims.
- `academic-tone-editor` for the final language pass.
