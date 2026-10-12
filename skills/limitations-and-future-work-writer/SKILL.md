---
name: limitations-and-future-work-writer
description: Writes the limitations and future-work sections of a paper or thesis, identifying real threats to validity, stating how each affects the conclusions, and proposing specific follow-up studies that address them. Use when the user asks to "write the limitations section", "what are the limitations of my study", "write future work", "write threats to validity", "reviewers say my limitations are superficial", or a venue requires a limitations statement.
---

# Limitations and Future Work Writer

State plainly where the study's conclusions stop, and what would extend them. A good limitations section raises a reader's trust; a vague one lowers it.

## When to use

- A paper, thesis, or report needs a limitations, threats-to-validity, or future-work section.
- A venue requires a limitations statement (several ML and NLP venues do).
- Reviewers criticised the limitations as generic.

Hand off instead for a full critique of the draft (`self-peer-reviewer`).

## Inputs

- The paper's claims and the methods and results behind them. Read the methods and results sections, not just the abstract.
- The caveats already noted during analysis (`results-interpreter` output, lab notebook).
- Venue requirements: separate section or part of the discussion, any length rule, any required broader-impact content.
- What the user already knows is weak. They usually know; ask.

## Workflow

1. **List the claims** the paper makes. Limitations are limits on these claims.
2. **Audit the study** against each category and write down what applies:

   | Category | Questions |
   |---|---|
   | Sample and data | Size, how selected, single site or source, time period, missing data, label quality |
   | Internal validity | Confounds, no control or randomisation, baseline tuning, leakage, researcher degrees of freedom |
   | Measurement | Proxy metrics, self-report, instrument validity, annotator agreement, ceiling effects |
   | External validity | Other populations, languages, domains, scales, settings, time |
   | Statistical | Power, number of seeds or runs, multiple comparisons, assumptions |
   | Scope | What was deliberately not studied (delimitations) |
   | Method assumptions | Conditions under which the method works; known failure cases |
   | Resources | Compute, cost, or data requirements that restrict who can use or reproduce it |
   | Ethics and impact | Bias, privacy, misuse potential, environmental cost |

3. **Select the limitations that matter**: those that could change a conclusion or its scope. Usually 3 to 6. Drop ones that apply to all research ("more data would help").
4. **Write each limitation in three parts:**
   - *What*: the specific limitation.
   - *Consequence*: which claim it affects and in which direction (might overstate the effect, may not hold for X).
   - *Mitigation or bound*: what was done to reduce it, or why the main conclusion still stands, or an honest statement that it is unresolved.

   Example: "All participants were undergraduate students at one university, so the usability results may not transfer to older or less technically experienced users; the error-rate findings, which depend on the interface and not on prior experience, are less likely to be affected."
5. **Order** by importance to the conclusions, most serious first.
6. **Derive future work from the limitations and findings.** Each item names the question, the approach, and why it follows:
   - Weak: "Future work could explore other datasets."
   - Strong: "Because all three evaluation corpora are English news text, the next step is to test whether the gain holds on low-resource languages, starting with the X benchmark, where tokenisation differences may reduce it."
7. **Separate near and far.** Two or three concrete next studies, then at most one or two longer-term directions.
8. **Check the tone**: factual, without apology and without defensiveness.

## Output format

```markdown
## Limitations
<3 to 6 paragraphs or a compact list, each: limitation, consequence, mitigation or bound>

## Future Work
<2 to 4 specific directions, each tied to a finding or limitation>

---
## Notes for the author
| Limitation | Affects claim | Severity | Addressed in text? |
- Limitations considered and left out, with the reason
- Any limitation serious enough that a claim in the abstract or introduction should be reworded
```

## Quality bar and pitfalls

- Limitations must be true of this study. Do not invent weaknesses to fill the section, and do not omit a real one because it is uncomfortable.
- Do not describe mitigations that were not carried out.
- A limitation with no stated consequence is filler. Say what it does to the conclusions.
- Do not follow every limitation with "however, this does not affect our results". Say so only when you can explain why.
- If a limitation undermines a headline claim, the claim needs rewording in the abstract and introduction. Tell the user; do not bury it here.
- Future work is not a list of everything left undone, and not a reservation of territory. Reviewers discount vague lists.
- Do not promise future work as if it were a result ("we will show").
- Distinguish limitations (weaknesses) from delimitations (chosen scope).

## Related skills

- `results-interpreter` records the caveats this section draws on.
- `paper-critic` and `self-peer-reviewer` find the weaknesses a reviewer would raise.
- `research-gap-finder` reads other papers' versions of this section to find gaps.
- `abstract-writer` and `introduction-writer` when claims must be reworded to match.
- `reproducibility-checklist` covers resource and reporting limits in checklist form.
- `thesis-chapter-writer` for the thesis conclusion chapter.
