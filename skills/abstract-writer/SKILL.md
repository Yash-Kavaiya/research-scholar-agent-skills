---
name: abstract-writer
description: Writes or revises a research abstract within a word limit, covering background, gap, method, results with numbers, and implication, in either structured or unstructured form, plus title and keyword options. Use when the user asks to "write an abstract", "shorten my abstract to 250 words", "make a structured abstract", "improve my abstract", "write a conference abstract", or needs a title and keywords for a paper.
---

# Abstract Writer

Write an abstract that lets a reader decide in one minute what was done, what was found, and whether to read on, using only what the paper contains.

## When to use

- A paper, thesis, or conference submission needs an abstract.
- An existing abstract is over the limit, vague, or missing results.

Hand off instead for the introduction (`introduction-writer`) or a plain-language summary for the public (`paper-to-blog`).

## Inputs

- The paper or its key content: problem, method, main results with numbers, conclusion. If the results are not final, say so and write placeholders the user must fill.
- Venue requirements: word limit (commonly 150 to 250), structured or unstructured, required headings, whether citations and abbreviations are allowed.
- Audience: specialist venue or broad journal.

## Workflow

1. **Check the requirements** in the venue's guidelines: limit, format, headings.
2. **Extract five things from the paper**, each as one sentence:
   - *Background*: the context the reader needs.
   - *Gap or problem*: what is unknown or unsolved.
   - *Method*: what was done, with the design, data, or approach named.
   - *Results*: the main findings with numbers and units.
   - *Conclusion*: what it means and for whom.
3. **Allocate the words.** For 250 words: background and gap 40 to 60, method 50 to 70, results 80 to 100, conclusion 30 to 40. Results get the most space.
4. **Draft** in the required form:
   - *Structured*: headings such as Background, Objective, Methods, Results, Conclusions (use the venue's exact headings).
   - *Unstructured*: one paragraph in the same order.
5. **Make the results specific.** Replace "significantly improved" with the value, the comparison, and the uncertainty: "reduced error from 12.4% to 9.1% (95% CI 8.3 to 9.9)". Include sample size or dataset.
6. **Tighten to the limit.** Cut background first, then method detail. Remove filler ("In this paper, we", "It is important to note"). Keep the numbers.
7. **Check against the paper**: every statement and number in the abstract appears in the body with the same value.
8. **Offer titles and keywords.** Three title options (descriptive, result-stating, and short), and 4 to 6 keywords that are not already in the title, using the field's indexing terms (MeSH for biomedical work).
9. **Report the word count.**

## Output format

```markdown
## Abstract (<N> words; limit <L>)
<text>

## Title options
1. ...
2. ...
3. ...

## Keywords
a; b; c; d; e

## Checks
- Numbers matched to: Table 2, §5.1
- Placeholders still to fill: [N], [effect size]
- Assumptions made: ...
```

When revising, also give a short list of what changed and why.

## Quality bar and pitfalls

- Never invent a result, number, or sample size to make the abstract read well. Use a bracketed placeholder and flag it.
- The abstract must stand alone: no undefined abbreviations, no references to figures or sections, and citations only if the venue allows them.
- Do not claim more than the results section supports. The abstract is the most-read part and overclaiming there does the most damage.
- State the main limitation in a clause when it changes how the result should be read (single site, small sample, simulation only).
- Past tense for what was done and found; present tense for conclusions and general statements.
- Avoid opening with a sentence so general it fits any paper in the field.
- Count words the way the venue does. Stay under the limit; submission systems reject overruns.

## Related skills

- `results-interpreter` provides the findings and the wording they support.
- `introduction-writer` expands the same arc into the introduction.
- `paper-outline-generator` fixes the message the abstract must carry.
- `academic-tone-editor` for a final clarity and concision pass.
- `venue-recommender` uses the abstract to match venues.
- `cover-letter-writer` reuses the abstract's main result.
