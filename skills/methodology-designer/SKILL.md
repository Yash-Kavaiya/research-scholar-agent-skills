---
name: methodology-designer
description: Selects and justifies a research design (quantitative, qualitative, or mixed methods) for a research question, specifying sampling, data collection, analysis, validity, and limitations, and writes the methodology section. Use when the user asks "which methodology should I use", "qualitative or quantitative", "design my study", "write my methodology chapter", "justify my research design", or needs chapter 3 of a thesis or the methods part of a proposal.
---

# Methodology Designer

Choose a design that can answer the research question within the user's constraints, and justify each choice against the alternatives.

## When to use

- A study is being planned and the design is open.
- A methodology chapter or section must be written or defended.

Hand off instead for computational experiment details (`experiment-planner`), sample-size numbers (`sample-size-power-calculator`), or the instrument itself (`survey-questionnaire-designer`).

## Inputs

- Research question(s) and hypotheses. If they are vague, run `research-question-formulator` first.
- Field and its norms.
- Constraints: time, budget, access to participants or data, equipment, skills, ethics limits.
- What already exists: datasets, instruments, pilot results.

## Workflow

1. **Classify the question.** The type of question drives the design:

   | Question asks | Family | Typical designs |
   |---|---|---|
   | Does X cause Y? | Quantitative, experimental | RCT, quasi-experiment, A/B test, controlled lab or computational experiment |
   | How much, how often, how related? | Quantitative, descriptive or correlational | Cross-sectional survey, cohort, case-control, secondary data analysis |
   | How or why do people experience X? | Qualitative | Phenomenology, grounded theory, case study, ethnography, narrative |
   | Both the pattern and the explanation | Mixed methods | Convergent, explanatory sequential (quant then qual), exploratory sequential (qual then quant) |
   | Does this artefact work? | Design science, engineering | Build and evaluate, benchmark study, simulation |

2. **State the stance briefly** when the field expects it: positivist or post-positivist, interpretivist, pragmatist. One paragraph, tied to the question.
3. **Compare two or three candidate designs** in a table: what each could answer, what it costs, its main threat to validity, and feasibility for this user. Recommend one.
4. **Specify the chosen design:**
   - *Population and sampling*: target population, sampling frame, method (random, stratified, purposive, snowball), and sample size with its basis (power analysis, or saturation for qualitative work).
   - *Variables or phenomena*: independent, dependent, control, and confounding variables with operational definitions; or the phenomenon and sensitising concepts.
   - *Data collection*: instruments, procedures, setting, timeline, pilot.
   - *Analysis*: the method for each research question, with software.
   - *Quality*: for quantitative work, internal, external, construct, and statistical-conclusion validity, and reliability. For qualitative work, credibility, transferability, dependability, and confirmability, with the technique used for each (triangulation, member checking, audit trail).
   - *Ethics*: consent, confidentiality, risk, data handling.
   - *Limitations and delimitations.*
5. **Build the alignment matrix**: each research question mapped to data source, instrument, and analysis. A row with a missing cell means the design cannot answer that question.
6. **Draft the methodology section** in the venue's structure, in future tense for proposals and past tense for completed studies.

## Output format

```markdown
## Recommended design: <name>
Why this design: ...

## Alternatives considered
| Design | Answers the RQ? | Cost and time | Main validity threat | Verdict |

## Alignment matrix
| Research question | Data source | Instrument | Analysis |

## Design specification
### Population and sampling
### Variables and operational definitions
### Data collection procedure
### Analysis plan
### Validity and reliability (or trustworthiness)
### Ethical considerations
### Limitations and delimitations

## Open decisions and risks
```

Follow with the prose methodology section when asked.

## Quality bar and pitfalls

- Justify by fit to the question, not by preference or familiarity. Say why the rejected designs were rejected.
- Do not claim causation from a design that cannot support it. Correlational designs get correlational wording throughout.
- Mixed methods needs a reason and an integration point (where and how the strands are combined). Two unconnected studies are not mixed methods.
- Qualitative sample sizes are justified by saturation and depth, not power analysis.
- Convenience sampling is acceptable when stated as such with its consequence for generalisation.
- Cite methodological sources for the design (for example Creswell, Yin, Braun and Clarke) only after confirming the reference details.
- A design the user cannot execute in their time and access is the wrong design. Say so and scale it.

## Related skills

- `research-question-formulator` supplies the questions and hypotheses.
- `sample-size-power-calculator` for the quantitative sample size.
- `survey-questionnaire-designer` for instruments.
- `experiment-planner` for computational and lab experiments.
- `statistical-test-selector` and `qualitative-coding-assistant` for the analysis plan.
- `ethics-irb-drafter` for the ethics application.
- `thesis-chapter-writer` and `phd-research-proposal-writer` use the methodology section.
