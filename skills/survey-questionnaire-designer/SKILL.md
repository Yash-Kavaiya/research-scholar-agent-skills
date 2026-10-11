---
name: survey-questionnaire-designer
description: Designs survey questionnaires and interview guides, mapping constructs to items, choosing response scales such as Likert, removing leading and double-barrelled wording, and planning validity checks, reliability analysis, and a pilot. Use when the user asks to "design a questionnaire", "write survey questions", "create a Likert scale", "review my survey", "make an interview guide", "how do I validate my questionnaire", or needs an instrument for a thesis or study.
---

# Survey and Questionnaire Designer

Build an instrument in which every item measures something the research question needs, and plan how its validity and reliability will be shown.

## When to use

- A new questionnaire, an adaptation of an existing scale, or a semi-structured interview guide.
- Reviewing a draft survey for wording and structure problems.

Hand off instead for the choice of design (`methodology-designer`), the sample size (`sample-size-power-calculator`), or analysing responses (`statistical-test-selector`, `qualitative-coding-assistant`).

## Inputs

- Research questions and the constructs to measure.
- Respondents: who they are, language, literacy, how they will be reached.
- Mode: online, paper, phone, face to face.
- Length limit (aim for under 10 to 12 minutes online) and any existing instruments the user knows of.

## Workflow

1. **List the constructs** from the research questions and define each one. For every construct record its dimensions and the source of the definition.
2. **Search for validated scales first.** Check with `paper-search` whether an established instrument exists (for example SUS for usability, TAM items for technology acceptance, PHQ-9 for depression, NASA-TLX for workload). Using or adapting a validated scale is stronger than writing a new one. Record the scale's source, its reported reliability, and its licence or permission terms; some scales require permission or a fee.
3. **Build the blueprint**: a table of construct, dimension, item, source (adopted, adapted, new), and scale. Aim for 3 to 5 items per dimension for multi-item scales. Any item that maps to no construct is cut.
4. **Write or adapt the items.** Rules:
   - One idea per item. Split "The system is fast and easy to use".
   - Plain words, no jargon, under about 20 words.
   - No leading wording ("How helpful was our excellent support?"), no loaded terms.
   - No double negatives. Use reverse-worded items sparingly and mark them for reverse scoring.
   - A specific time frame where behaviour is asked about ("in the past 7 days").
   - Response options that are exhaustive and mutually exclusive, with "Not applicable" or "Prefer not to say" where needed.
5. **Choose response scales.** Likert agreement with 5 or 7 points, all points labelled, same direction throughout. Use frequency or quality anchors when the item is not an agreement statement. Keep one scale format per block.
6. **Order the questionnaire**: information and consent, screening questions, easy and engaging items first, grouped by topic, sensitive items late, demographics last. Add an attention check for long online surveys and disclose it in the methods.
7. **Plan validity and reliability:**
   - Content validity: review by 3 to 5 experts; compute a content validity index if the field expects it.
   - Face validity and comprehension: cognitive interviews with 5 to 8 people from the target group.
   - Pilot: 20 to 30 respondents or more; check completion time, missing data, floor and ceiling effects, item variance.
   - Reliability: Cronbach's alpha or McDonald's omega per scale (0.70 or above is the usual threshold), item-total correlations.
   - Construct validity: exploratory factor analysis for new scales (plan about 5 to 10 respondents per item), confirmatory analysis in a second sample when possible.
8. **For translated instruments**, plan forward and back translation and a comprehension check.
9. **For interview guides**: 6 to 10 open main questions, each with probes; no yes/no or leading questions; an opening warm-up and a closing "anything else".
10. **Deliver** the instrument, the blueprint, the scoring key, and the validation plan.

## Output format

```markdown
## Blueprint
| Construct | Dimension | Item ID | Item | Source | Scale | Reverse |

## Questionnaire
### Information and consent
### Section A: <topic>
A1. <item>   ( ) Strongly disagree ( ) Disagree ( ) Neutral ( ) Agree ( ) Strongly agree

### Demographics

## Scoring key
- <Scale>: mean of A1 to A5; A3 reverse-scored.

## Validation and pilot plan
| Step | Who | n | Criterion |

## Notes for the methods section
```

## Quality bar and pitfalls

- Do not present a newly written scale as validated. It is validated only after the evidence is collected.
- Do not reproduce a copyrighted scale's items without confirming the terms. Give the citation and tell the user to obtain permission where required.
- Never invent reliability figures for an existing scale. Quote them from the retrieved source or say they need to be looked up.
- Changing item wording or the number of scale points alters a validated scale; report it as adapted and re-check reliability.
- Likert items are ordinal. Summed multi-item scales are commonly treated as interval; single items should not be.
- Collect only the demographics the analysis needs. Each extra personal item raises ethics and privacy cost.
- Every survey with human respondents needs ethics review and informed consent (`ethics-irb-drafter`).

## Related skills

- `research-question-formulator` and `methodology-designer` for the constructs and design.
- `paper-search` to find validated scales.
- `sample-size-power-calculator` for the number of respondents.
- `ethics-irb-drafter` for consent and the ethics application.
- `statistical-test-selector` and `qualitative-coding-assistant` to analyse the responses.
