---
name: phd-research-proposal-writer
description: Writes a PhD research proposal or synopsis for admission, registration, or doctoral committee approval, covering title, background, literature gap, research questions and objectives, proposed methodology, timeline, expected contributions, and references, in the university's required format. Use when the user asks to "write a PhD research proposal", "draft my PhD synopsis", "research proposal for PhD admission", "proposal for my RDC or DRC meeting", "pre-registration proposal", or needs a research plan for a doctoral application.
---

# PhD Research Proposal Writer

Write a proposal that shows a committee three things: there is a real gap, the candidate has a workable plan to address it, and the project fits a doctoral timeline.

## When to use

- Applying for PhD admission where a research proposal is required.
- Preparing the synopsis for registration or a research committee (RDC, DRC, RAC).
- A confirmation or upgrade report early in the PhD.

Hand off instead for a funding application (`grant-proposal-writer`) or a personal statement (`sop-and-research-statement-writer`).

## Inputs

- The university's and department's format and limits: sections, word or page count (admission proposals are often 1,500 to 3,000 words; registration synopses run longer), citation style.
- The candidate's research interest, background, and any prior work (master's thesis, publications, projects).
- The prospective supervisor's research area, if known.
- Stage: admission, registration, or confirmation. The expected depth differs.
- Resources and constraints: duration, funding, access to data, labs, or field sites.

## Workflow

1. **Get the required format** from the university. Follow its headings and limits exactly; where none is given, use the structure in the output format below.
2. **Narrow the topic** to something one person can complete in three to five years. Move from area to topic to a specific problem (`research-gap-finder`, `research-question-formulator`).
3. **Ground it in the literature.** Search and read enough to establish what is known and what is missing (`paper-search`). At admission stage 15 to 25 well-chosen sources suffice; a registration synopsis needs a fuller review. Cite only what was retrieved.
4. **State the gap and the research problem** in a short paragraph that follows from the literature.
5. **Write the research questions and objectives**: one overarching aim, and 3 to 4 objectives with measurable verbs, each of which could become a thesis chapter or paper. Add hypotheses where the design is confirmatory.
6. **Propose the methodology** per objective: design, data or materials and how they will be obtained, methods and tools, analysis, and validation. Show feasibility: name the dataset, instrument, or lab. Admission proposals may leave options open, but must show the candidate understands the choices (`methodology-designer`).
7. **Scope and limits**: what is included and excluded, and the main risk with a fallback.
8. **Plan the timeline** by semester or quarter: coursework and literature review, each objective, publications, thesis writing, submission. Be realistic about ethics approval, data collection, and writing time.
9. **State the expected contributions**: to knowledge, method, and practice. Specific and modest beats grand.
10. **Fit to the department** (admission): one or two sentences on how the project relates to the supervisor's or group's work, based on their actual publications.
11. **Write the title last**: specific, under about 15 words, naming the problem and approach.
12. **Compile the references** and verify them (`citation-verifier`).

## Output format

```markdown
# <Title>
Candidate: ...  Proposed supervisor: ...  Department: ...

## 1. Introduction and background
## 2. Review of literature and research gap
## 3. Problem statement
## 4. Research questions, aim, and objectives
## 5. Proposed methodology
| Objective | Data / materials | Method | Analysis | Outcome |
## 6. Scope and limitations
## 7. Work plan
| Activity | S1 | S2 | S3 | S4 | S5 | S6 |
## 8. Expected contributions
## 9. Ethical considerations (if applicable)
## 10. References

---
Word count: <n> of <limit>
To confirm or supply: ...
```

## Quality bar and pitfalls

- The proposal must be the candidate's own plan, built from their interests and reading. Write it with them: ask for their ideas and background, and do not produce a generic proposal for them to submit unread. They will have to defend it in an interview.
- Tell the candidate to check the university's policy on AI assistance in application documents.
- Every reference must be real and retrieved. Committees check, and a fabricated citation ends an application.
- A proposal is a plan, not a result. Do not predict findings as facts.
- Too broad is the usual fault. "AI in healthcare" is an area; a proposal needs a problem.
- The methodology must be doable with the access the candidate actually has. Name the data source and confirm it exists.
- Do not claim "no work has been done" without a search that shows it.
- Tailoring to a supervisor means engaging with their research, not flattering them.
- Proposals are run through similarity checks. Text copied from sources, including the candidate's own master's thesis without citation, will be flagged.

## Related skills

- `research-gap-finder`, `topic-trend-analyzer`, and `novelty-checker` to settle the topic and gap.
- `research-question-formulator` for questions and objectives.
- `paper-search` and `literature-review-writer` for the review section.
- `methodology-designer` and `sample-size-power-calculator` for the methodology.
- `ethics-irb-drafter` where human participants are involved.
- `supervisor-finder` to identify and approach potential supervisors.
- `sop-and-research-statement-writer` for the accompanying statement.
- `citation-verifier` and `plagiarism-and-paraphrase-checker` before submission.
- `viva-defense-prep` for the proposal interview or committee presentation.
