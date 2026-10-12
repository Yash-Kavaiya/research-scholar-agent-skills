---
name: self-peer-reviewer
description: Reviews the user's own manuscript the way a demanding reviewer would before submission, producing a full referee report with summary, strengths, weaknesses ranked by severity, questions, scores on the venue's criteria, a likely decision, and a prioritised fix list. Use when the user asks to "review my paper before I submit", "act as Reviewer 2", "what would reviewers say", "find the weaknesses in my draft", "will this get accepted", or wants a mock peer review.
---

# Self Peer Reviewer

Find the reasons a reviewer would reject the paper while there is still time to fix them. The review is strict, specific, and fair.

## When to use

- A draft is complete, or nearly, and submission is days or weeks away.
- After a rejection, to reassess before resubmitting.
- To decide whether a paper is ready for a particular venue.

Hand off instead for critiquing someone else's published paper (`paper-critic`) or for responding to real reviews (`rebuttal-writer`).

## Inputs

- The full manuscript with appendix. Reviewing an abstract or outline gives a different, weaker result; say so if that is all there is.
- Target venue and its review criteria and form, from the reviewer guidelines.
- Time until the deadline, which decides what fixes are feasible.
- Anything the authors already consider weak.

## Workflow

1. **Read as a reviewer would**: title and abstract, then figures and tables, then the introduction and conclusion, then the full paper. Note first impressions after the first pass; reviewers form their opinion early.
2. **Summarise the paper** in 3 to 5 sentences in your own words: problem, approach, main claims, evidence. If this is hard to write, the paper has a clarity problem, and that is a finding.
3. **Check claims against evidence.** List every claim in the abstract and introduction and find its support. Flag claims that are unsupported, supported only partly, or stated more strongly than the results allow.
4. **Review along the standard axes:**
   - *Novelty and significance*: what is new relative to the closest work, and whether that work is cited and compared. Run `novelty-checker` if the closest work is not discussed.
   - *Technical soundness*: correctness of the method, proofs, and analysis; validity of the design; fairness of comparisons; confounds; statistics (see the table in `paper-critic`).
   - *Experimental rigour*: baselines, datasets, ablations, variance, significance, missing experiments a reviewer would ask for.
   - *Clarity*: organisation, definitions, notation, figures readable on their own, reproducible description.
   - *Related work*: coverage, accuracy, positioning.
   - *Reproducibility and ethics*: details, code and data, limitations stated, human-subjects or data issues.
5. **Take three reviewer stances** and record what each would say:
   - The expert in the subfield, who knows the closest prior work and the standard evaluation.
   - The methodologist, who checks the statistics and experimental design.
   - The outsider, who reads quickly and judges clarity and significance.
6. **Rank the weaknesses**: *fatal* (likely rejection by itself), *major* (must be addressed), *minor* (should be fixed), *nitpicks*. For each: where it is, why it matters, and what would resolve it.
7. **Score** on the venue's own scale and criteria, with a confidence level, and state the likely outcome with the reasoning. Give a range, not a certainty.
8. **Build the fix plan** for the time available: what to fix now, what to reword or scope down, what to acknowledge as a limitation, and what cannot be fixed before the deadline.
9. **Check the desk-reject risks**: scope, length, formatting, anonymity, missing required sections (`camera-ready-checker`).

## Output format

```markdown
# Mock review: <title> for <venue>

## Summary of the paper
## Strengths
1. ... (where)

## Weaknesses
### Fatal
### Major
- **W1. <issue>** (§, Table, Fig.). Why it matters: ... To resolve: ...
### Minor
### Nitpicks

## Questions for the authors
## Missing references
## Scores (venue's scale)
| Criterion | Score | Reason |
Overall: <score>, confidence <level>. Likely outcome: <range>, because ...

## What the three reviewers would say
- Expert: ...  Methodologist: ...  Outsider: ...

## Fix plan (time available: <n> days)
| Priority | Fix | Effort | Addresses |
```

## Quality bar and pitfalls

- Be strict. A flattering review is useless here; the author asked in order to hear the problems. Do not soften a fatal flaw into a suggestion.
- Be specific and locatable. "Experiments are weak" helps nobody; "Table 2 compares against baselines from 2019 only; the 2023 method X is missing" does.
- Be fair. Do not invent flaws, demand experiments outside the paper's scope, or hold the paper to a different venue's standard.
- Verify before claiming something is missing: search the appendix. Name missing related work only after retrieving it.
- The predicted outcome is an estimate. Real reviewers vary; never promise acceptance or rejection.
- Distinguish what is wrong with the research from what is wrong with the presentation. The fixes differ.
- If the main result does not hold up, say so directly, with the evidence.
- Keep the manuscript confidential: it is unpublished work.

## Related skills

- `paper-critic` provides the validity checklist applied here.
- `novelty-checker` and `citation-verifier` for the novelty and reference checks.
- `results-interpreter` to recalibrate overclaimed results.
- `limitations-and-future-work-writer` for weaknesses best handled by stating them.
- `experiment-planner` and `ablation-study-designer` for experiments the review calls for.
- `reproducibility-checklist` and `camera-ready-checker` for compliance.
- `rebuttal-writer` uses this review to prepare for likely criticisms.
- `venue-recommender` if the review suggests a different venue.
