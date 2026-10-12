---
name: research-question-formulator
description: Turns a vague research interest or a chosen gap into precise, testable research questions and hypotheses using PICO, SPIDER, and FINER. Use when the user says "help me frame my research question", "I am interested in X but do not know what to ask", "write hypotheses for my study", "is this a good research question", or needs objectives and hypotheses for a proposal or synopsis.
---

# Research Question Formulator

Move from "I am interested in X" to one primary question, a few secondary questions, and hypotheses that a study could actually test.

## When to use

- The user has an interest, a gap, or a draft question and needs it sharpened.
- A proposal needs an aims, objectives, or hypotheses section.

Hand off instead when the user has no gap yet (`research-gap-finder`) or wants the study design itself (`methodology-designer`).

## Inputs

- The interest or gap in the user's own words.
- Field and study type they expect (experiment, observational, qualitative, computational, review).
- Constraints: time, data they can access, equipment or compute, ethics limits.
- Purpose: thesis, paper, grant, coursework.

Ask only for what is missing. Two or three questions are usually enough.

## Workflow

1. **Restate the interest** in one sentence and confirm it.
2. **Pick the framing tool** by study type:

   | Study type | Framework | Elements |
   |---|---|---|
   | Intervention or comparison (clinical, education, HCI, A/B) | PICO(T) | Population, Intervention, Comparison, Outcome, (Time) |
   | Exposure or observational | PECO | Population, Exposure, Comparison, Outcome |
   | Qualitative or mixed | SPIDER | Sample, Phenomenon of Interest, Design, Evaluation, Research type |
   | Computational or engineering | Task, Method, Baseline, Metric, Setting | what is being done, how, against what, measured how, under which conditions |

3. **Fill the framework** as a table. Mark any element the user has not decided, and propose a default.
4. **Draft 3 candidate primary questions** at different scopes (narrow, medium, ambitious). Each must name its variables or phenomenon and its population or setting.
5. **Score each with FINER** in a table: Feasible, Interesting, Novel, Ethical, Relevant. Give a one-line reason per cell. Do not assert novelty without a check; say "unverified, run `novelty-checker`".
6. **Recommend one** and say why.
7. **Derive from it:**
   - 2 to 4 secondary questions.
   - Objectives written with measurable verbs (estimate, compare, identify, evaluate).
   - For quantitative questions: a null and an alternative hypothesis per primary outcome, with the direction of the expected effect and the variable types.
   - For qualitative questions: no hypotheses. Give the central question and sub-questions instead.
8. **Define the terms** the question relies on, with how each would be measured.

## Output format

```markdown
## Framing (<framework>)
| Element | Value | Status |
|---|---|---|

## Candidate questions
1. Narrow: ...
2. Medium: ...
3. Ambitious: ...

## FINER assessment
| Question | Feasible | Interesting | Novel | Ethical | Relevant |
|---|---|---|---|---|---|

## Recommended primary question
> ...

## Secondary questions
## Objectives
## Hypotheses
- H0: ...
- H1: ... (direction, variables, how measured)

## Operational definitions
| Term | Definition | Measure |
|---|---|---|

## Open decisions for you
```

## Quality bar and pitfalls

- A good question can be answered by data. Reject "How can we improve X?" in favour of "Does A improve X compared with B in population P, measured by M?".
- One question, one main outcome. Split double-barrelled questions.
- Hypotheses must be falsifiable and state direction when theory supports one.
- Do not write hypotheses for exploratory or qualitative work to make it look rigorous.
- Keep the scope within the stated constraints. Say plainly when the ambitious version does not fit a master's timeline.
- Yes/no questions are fine for confirmatory studies. For exploratory work prefer "to what extent" or "how".

## Related skills

- `research-gap-finder` supplies the gap this question addresses.
- `novelty-checker` verifies the Novel column.
- `methodology-designer` and `experiment-planner` design the study that answers the question.
- `sample-size-power-calculator` uses the hypotheses and expected effect size.
- `phd-research-proposal-writer` and `grant-proposal-writer` take the questions and objectives as input.
