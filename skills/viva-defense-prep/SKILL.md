---
name: viva-defense-prep
description: Prepares a candidate for a thesis viva, dissertation defence, proposal defence, or qualifying exam by generating the questions examiners are likely to ask from the candidate's own thesis, outlining answers built from its content, running mock question sessions with feedback, and planning the opening presentation. Use when the user asks to "prepare me for my viva", "what will examiners ask about my thesis", "mock defence", "practice defence questions", "prepare for my PhD defence or pre-submission seminar", or "how do I answer questions about my limitations".
---

# Viva and Defence Prep

Get the candidate ready to explain, justify, and defend their own work aloud. The preparation is built from their thesis, and the answers must be ones they understand and can give themselves.

## When to use

- A thesis viva or defence, at master's or doctoral level.
- A proposal defence, confirmation or upgrade review, qualifying exam, or pre-submission seminar.
- A job talk or conference question session about the candidate's research.

Hand off instead for the defence slides (`paper-to-slides`) or for a critique of the thesis as a document (`self-peer-reviewer`).

## Inputs

- The thesis or proposal, in full if possible; at least the abstract, contributions, methodology, and conclusions.
- The exam format: country and institution conventions (closed viva with two examiners, public defence with a committee, presentation length), duration, and possible outcomes.
- The examiners' names and fields, if known.
- The candidate's own list of what worries them.
- Time until the exam.

## Workflow

1. **Establish the format** from the university's regulations and the supervisor: who examines, how long, whether there is a presentation, and what outcomes are possible.
2. **Read the thesis as an examiner would.** Note the claimed contributions, every methodological choice, the weakest evidence, anything unusual, and any inconsistency between chapters.
3. **Generate questions in the standard categories**, specific to this thesis and referring to its chapters and figures:

   | Category | Examples |
   |---|---|
   | Opening | Summarise your thesis in three minutes. What is your main contribution? Why this topic? |
   | Contribution and originality | What do we know now that we did not before? How does it differ from <closest work>? |
   | Literature | Which works most influenced you? What has appeared since you submitted? Why did you not engage with <school or author>? |
   | Methodology | Why this design and not <alternative>? How did you choose the sample, dataset, or parameters? What threatens validity? |
   | Results | Walk me through Figure X. Is this difference meaningful? What surprised you? How do you explain <anomalous result>? |
   | Limitations | What is the weakest part? What would you do differently? How far do the findings generalise? |
   | Implications | Who should care? What follows for practice or theory? |
   | Future work | What is the next study? What would you do with three more years? |
   | Ownership | Which parts were your own work in the co-authored chapters? Explain how you implemented <component>. |
   | Fundamentals | Define <core concept>. Derive or explain <basic result your method relies on>. |

4. **Predict examiner-specific questions.** Look up each examiner's recent work (`paper-search`) and note where their methods, theories, or findings touch the thesis. Examiners ask from their own expertise, and it is reasonable to expect their relevant papers to be cited.
5. **Mark the hard questions**: the ones aimed at real weaknesses. Prepare these most.
6. **Outline answers with the candidate.** For each question give bullet points drawn from the thesis with chapter and page pointers, and have the candidate say the answer in their own words. A useful structure: answer directly in one sentence, give the reasoning or evidence, acknowledge the limit, and stop.
7. **Teach the handling techniques:**
   - Pause before answering; ask for clarification of an unclear question.
   - For a real weakness: agree it is a limitation, explain the reason for the choice, say what effect it has on the conclusions, and what would address it. Defend the reasoning; do not deny the weakness.
   - When you do not know: say so, then reason aloud about how you would find out.
   - When the examiner is right: concede and note it as a correction.
   - Keep answers to one or two minutes unless asked to expand.
8. **Run mock sessions.** Ask one question at a time, wait for the candidate's answer, then give feedback on content, structure, and length, with follow-up questions as an examiner would press. Increase difficulty across rounds. Record recurring problems.
9. **Prepare the opening presentation** if required: contributions-first, timed to the slot (`paper-to-slides`), and the three-minute spoken summary regardless.
10. **Plan the final week**: reread the thesis and mark it with tabs; list typos and errors found, to bring as a corrections sheet; reread key references and check for new publications in the area; rehearse the summary aloud; settle logistics.

## Output format

```markdown
# Defence preparation: <thesis title>
Format: <examiners, duration, presentation>. Date: ...

## Three-minute summary (outline for you to say in your own words)
## Question bank
### Likely (prepare all)
| # | Question | Category | Answer points (thesis location) |
### Hard (prepare most carefully)
### Examiner-specific
| Examiner | Their relevant work | Likely questions |

## Weak points and how to discuss them
| Weakness | Why the choice was made | Effect on conclusions | What would fix it |

## Mock session log
| Round | Question | Feedback | To improve |

## Final-week checklist
```

## Quality bar and pitfalls

- Answers come from the candidate's thesis and understanding. Do not write polished answers to memorise; examiners detect recitation and follow-up questions break it. Give points and have the candidate phrase them.
- Do not invent content the thesis does not contain, or supply justifications for choices the candidate did not make. Ask them why they made each choice.
- Predicted questions are probabilities. Tell the candidate that unexpected questions will come and that the skill being practised is reasoning aloud about their own work.
- Do not advise evasion or bluffing. Admitting a limit and reasoning about it is the answer examiners respect.
- Check examiner facts from retrieved sources; do not attribute papers or views to an examiner from memory.
- Be honest in feedback. If an answer is weak or the candidate cannot explain a part of their thesis, say so now, while there is time to fix it.
- Formats and outcomes differ by country and institution. Take them from the regulations, not from general knowledge.
- Preparation covers the whole thesis, including the early chapters written years ago.

## Related skills

- `self-peer-reviewer` and `paper-critic` to find the weaknesses examiners will find.
- `limitations-and-future-work-writer` for articulating limitations clearly.
- `paper-to-slides` for the opening presentation.
- `paper-search` and `citation-graph-explorer` to check examiners' work and recent publications.
- `math-and-equation-explainer` to rehearse explaining derivations aloud.
- `thesis-chapter-writer` for corrections after the defence.
- `research-progress-tracker` to schedule the preparation.
