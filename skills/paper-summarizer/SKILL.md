---
name: paper-summarizer
description: Produces a structured summary of a research paper covering the problem, method, data, results, limitations, and what to take from it, with every number traced to a page, table, or figure. Use when the user shares a PDF, arXiv link, or pasted paper and asks to "summarize this paper", "explain what this paper does", "give me the key findings", "TL;DR this", or wants reading notes for many papers in a consistent format.
---

# Paper Summarizer

Summarize what the paper actually says, in a fixed structure that makes papers comparable and makes each claim checkable against the source.

## When to use

- One paper needs to be understood quickly.
- Several papers need notes in the same format for a review.

Hand off instead for evaluation of the paper's soundness (`paper-critic`), side-by-side comparison (`paper-comparison-matrix`), or a derivation walk-through (`math-and-equation-explainer`).

## Inputs

- The paper: PDF, link, or pasted text. Get the full text. If only the abstract is available, say so and produce an abstract-level summary labelled as such.
- Reader's background and purpose (deciding whether to read it, citing it, reproducing it, reviewing it). This sets the depth.
- Length wanted: one paragraph, one page (default), or detailed notes.

## Workflow

1. **Read in passes.** Title, abstract, introduction's contribution list, and conclusion first. Then figures and tables with captions. Then method and experiments. Then limitations, appendix, and footnotes where caveats live.
2. **Identify the paper type** (empirical, method, theory, survey, position, dataset, systems) and adapt the sections: a survey has a taxonomy instead of a method; a theory paper has assumptions and theorems instead of data.
3. **Extract, do not infer.** For each section below, pull the paper's own statements and note where they appear (section, table, figure, or page).
4. **Record results with their conditions**: metric, dataset, baseline, and the size of the difference. "Improves accuracy" is not a result; "84.1% vs 81.3% top-1 on ImageNet-1k against ResNet-50 (Table 2)" is.
5. **Separate the authors' claims from your reading.** Limitations the authors state go under Limitations. Anything you noticed that they did not say goes under Reader notes and is marked as yours.
6. **Write the one-sentence takeaway last**, after the details are fixed.
7. **Check every number** in the summary against the paper once more before sending.

## Output format

```markdown
# <Title> (<First author> et al., <year>, <venue>)
Link/DOI: ...   Type: <empirical | method | theory | survey | dataset | position>
Read: <full text | abstract only | sections X to Y>

**One-sentence takeaway:** ...

## Problem
What is being solved, and why existing approaches fall short (as the authors frame it).

## Approach
The core idea in plain language, then the key technical steps. Name the components.

## Data and setup
Datasets, sample sizes, participants, baselines, metrics, compute.

## Results
- <Result with numbers, metric, dataset, baseline> (Table/Fig/§)
- ...

## Limitations stated by the authors
- ...

## Reader notes (mine, not the authors')
- Unstated assumptions, missing comparisons, questions to check.

## Useful for
How this paper could be used or cited in the reader's work.

## Terms
| Term | Meaning in this paper |
```

For a one-paragraph summary keep the order: problem, approach, main result with numbers, main limitation.

## Quality bar and pitfalls

- Never state a number, dataset, or claim that is not in the paper. If the paper is unclear, write "not reported".
- Do not summarize from the abstract and present it as a full reading. Abstracts overstate.
- Keep the authors' hedges. "Suggests" must not become "shows".
- Report the comparison, not just the headline number. Gains over weak or untuned baselines read very differently.
- Use the paper's own terminology first, then explain it. Renaming things makes the summary hard to match to the source.
- For long papers, say which appendices were not read.

## Related skills

- `paper-search` to obtain the paper and its metadata.
- `paper-critic` for a critical assessment after the summary.
- `paper-comparison-matrix` to line up several summaries.
- `math-and-equation-explainer` when the method section needs unpacking.
- `annotated-bibliography-builder` and `literature-review-writer` consume these summaries.
- `paper-to-code-reproducer` when the next step is implementing the method.
