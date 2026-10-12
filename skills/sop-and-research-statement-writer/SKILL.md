---
name: sop-and-research-statement-writer
description: Helps write statements of purpose, personal statements, and research statements for graduate admission, fellowships, postdoctoral and faculty applications, built from the applicant's real experience and tailored to each programme's prompt and length limit. Use when the user asks to "write my SOP", "statement of purpose for MS or PhD", "improve my personal statement", "write a research statement for a faculty or postdoc application", "tailor my SOP to this university", or "cut my statement to 1000 words".
---

# SOP and Research Statement Writer

Help the applicant tell a true, specific account of what they have done, what they want to do, and why this programme or position is the place to do it.

## When to use

- Statement of purpose or personal statement for master's or PhD admission.
- Research statement for a fellowship, postdoctoral, or faculty application.
- Revising, tailoring, or shortening an existing statement.

Hand off instead for a full research proposal (`phd-research-proposal-writer`) or the email to a professor (`supervisor-finder`).

## Inputs

- The exact prompt and limits (words, characters, or pages) for each application. Prompts differ; some ask for separate research and personal statements.
- The applicant's CV and the stories behind it: for each project, what they did, what was hard, what they found, and what it changed in their thinking.
- Research interests, as specifically as they can state them.
- The target programme: faculty they want to work with and why, labs, courses, resources.
- Anything to address: a low grade, a gap, a change of field.

Interview the applicant before drafting. Without their specifics, a statement is generic, and generic statements are the ones that fail.

## Workflow

1. **Read the prompt** and list what it asks. Answer every part, in the order that serves the reader.
2. **Collect the raw material.** For each significant experience ask: What was the problem? What exactly did you do, as distinct from the team? What tools or methods? What was the result (numbers, a paper, a deployed system)? What did you learn that shapes what you want to do next?
3. **Find the thread**: the question or theme that connects the experiences to the proposed study. The statement argues that the applicant's past leads to this next step.
4. **Choose the structure:**

   *Statement of purpose (admission)*
   1. Opening: the research interest stated directly, with the experience or question that produced it. No childhood anecdotes or quotations.
   2. Preparation: two or three experiences in depth, with contribution and outcome, in preference to a list of everything.
   3. Research interests and goals: the problems the applicant wants to work on and why they matter, at a level that shows they have read the area.
   4. Fit: specific faculty (two or three), with what in their recent work connects to the applicant's interests; relevant resources.
   5. Career goals and close.

   *Research statement (postdoc or faculty)*
   1. Research vision in one paragraph.
   2. Past and current work: the problems, the applicant's contributions, the results and their impact, with citations to their papers.
   3. Future agenda: two or three directions for the next 3 to 5 years, with first projects, methods, likely funding sources, and how students would be involved.
   4. Fit with the department: collaborations and facilities.

5. **Draft in the applicant's voice**: first person, active verbs, concrete nouns. Show with detail and outcome; do not assert qualities ("I am passionate and hardworking").
6. **Address weaknesses briefly and factually**, where needed: what happened, and what has changed since, in two or three sentences without excuses.
7. **Tailor each version.** Only the fit section and some emphasis should change between programmes, but those must change for real. Verify every faculty name, lab, and paper mentioned against the department's site (`supervisor-finder`, `paper-search`).
8. **Cut to the limit** by removing generalities first. Keep the specifics.
9. **Final checks**: programme and university names correct in every version; prompt fully answered; limit met; no claim the applicant cannot support in an interview.

## Output format

```markdown
## Statement of Purpose: <Programme, University> (<n> words; limit <L>)
<the statement>

---
## Notes
- Thread: ...
- Tailored elements: faculty named and why; resources
- Facts verified: <faculty and papers checked on the department site, date>
- Placeholders for you to fill or confirm: [...]
- Suggestions for other versions: what to swap for <University B>
```

For revisions, give the revised text and a short list of what changed and why.

## Quality bar and pitfalls

- Every experience, result, role, grade, and award in the statement must be true and the applicant's own. Never invent or inflate achievements, publications, or the applicant's share of team work. Ask when a detail is missing; do not fill it in.
- The statement must remain the applicant's. Draft from their material and keep their voice, so they can stand behind every sentence. Tell them to check each programme's policy on AI assistance in application materials; some require disclosure or prohibit it.
- Never name a professor, lab, or paper without verifying it exists and that the professor is still at the institution and taking students where that can be determined.
- Avoid the standard failures: opening with a quotation or a childhood story; listing the CV in prose; praising the university's ranking; vague interests ("AI and machine learning"); the same statement sent everywhere.
- Research statements need a future agenda that is distinct from the applicant's advisor's programme.
- Do not disclose sensitive personal information the applicant has not chosen to share.
- Respect the limit. Admissions readers stop at it.

## Related skills

- `supervisor-finder` to identify faculty and verify their current work.
- `paper-search` to read a target professor's recent papers.
- `phd-research-proposal-writer` when a proposal accompanies the statement.
- `research-question-formulator` to sharpen the stated research interests.
- `academic-tone-editor` for a language pass that preserves the applicant's voice.
- `grant-proposal-writer` for fellowship applications that need a project plan.
