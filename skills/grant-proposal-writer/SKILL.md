---
name: grant-proposal-writer
description: Drafts research grant proposals against a funder's call, including specific aims, significance, preliminary work, methodology, work plan and timeline, budget with justification, and expected outcomes, for international funders and for Indian schemes from ANRF (formerly SERB), DST, UGC, DBT, CSIR, and ICSSR. Use when the user asks to "write a grant proposal", "draft my ANRF or SERB proposal", "apply for a DST project", "UGC research grant", "write specific aims", "prepare a project budget and justification", or "find funding schemes I am eligible for".
---

# Grant Proposal Writer

Write a proposal that answers the funder's questions in the funder's format: what will be done, why it matters, why this team can do it, and what it costs.

## When to use

- A funding call is open and a proposal must be drafted or improved.
- The user wants to know which schemes suit their career stage and idea.
- A section is needed: aims, budget justification, timeline, impact.

Hand off instead for a PhD admission proposal (`phd-research-proposal-writer`) or a personal statement (`sop-and-research-statement-writer`).

## Inputs

- The call for proposals and the funder's format or template. This is the governing document; obtain the current version.
- The research idea, aims, and preliminary results.
- The applicant: position, institution, career stage, publications, prior grants, collaborators.
- Budget ceiling, duration, and the institution's overhead and cost norms.
- Deadline and submission portal.

## Workflow

1. **Match the scheme to the applicant.** Check eligibility before writing: career stage, age limits, employment status, institution type, nationality, and restrictions on holding other grants. For Indian schemes see `references/indian-schemes.md`, then confirm every condition on the funder's current call page. For other countries, find the equivalent early-career and standard grants (for example NSF CAREER and standard grants, NIH R01/R21/K awards, ERC Starting/Consolidator/Advanced, UKRI, DFG, ARC, JSPS).
2. **Extract the requirements** from the call into a checklist: sections, page or word limits, font and margins, budget heads and ceilings, required attachments (endorsement letter, certificates, biodata, quotations), and the review criteria with their weights.
3. **Write the one-paragraph pitch first**: the problem, the gap, the central hypothesis or goal, the approach, and the payoff. Everything else expands this.
4. **Draft the aims or objectives.** Two to four aims, each specific and assessable, related but not dependent on each other's success (if Aim 1 fails, Aim 2 must still be doable). For each: the question, the approach in a line, and the expected outcome.
5. **Write the core sections**, mapped to the review criteria:
   - *Background and significance*: what is known, the gap, why now, and who benefits. For national funders, tie it to stated priorities only where the link is real.
   - *Preliminary work*: the applicant's results that show feasibility.
   - *Methodology*: per aim, the design, methods, data, analysis, and success criteria (`methodology-designer`, `experiment-planner`).
   - *Risks and alternatives*: what could fail and the fallback for each.
   - *Work plan*: tasks, milestones, and deliverables per quarter or half-year, as a Gantt-style table.
   - *Team, facilities, and collaboration*: who does what, and what the host institution provides.
   - *Outcomes and impact*: publications, datasets, software, patents, trained personnel, societal or industrial use, with realistic numbers.
6. **Build the budget** under the funder's heads, typically: manpower (fellows and staff at the funder's current emolument rates), equipment (with quotations), consumables, travel, contingency, other costs, and institutional overheads at the permitted rate. Year-wise table, then a justification line for every item tying it to a task.
7. **Check compliance**: eligibility, limits, formatting, attachments, ethics and biosafety clearances, and declarations.
8. **Review as a panel would**: score the draft against the criteria and fix the weakest criterion first.
9. **List what the applicant must supply**: institutional endorsement, quotations, CV details, certificates.

## Output format

```markdown
# <Project title>
Scheme: <funder, scheme, call year>. Duration: <months>. Budget: <total>.

## Summary / Abstract (within limit)
## Objectives
## Background, gap, and significance
## Preliminary work
## Methodology (by objective)
## Risks and mitigation
| Risk | Likelihood | Mitigation or alternative |
## Work plan
| Task | Y1 H1 | Y1 H2 | Y2 H1 | ... | Deliverable |
## Budget
| Head | Year 1 | Year 2 | Year 3 | Total | Justification |
## Expected outcomes and impact
## References

---
## Compliance checklist (from the call)
## To be supplied by the applicant
## Facts to confirm on the funder's site
```

## Quality bar and pitfalls

- The call document governs. Never state eligibility, ceilings, fellowship rates, overhead percentages, or deadlines from memory; quote the current call, or mark the item "confirm on the funder's site". Scheme names and rules in India changed with the move from SERB to ANRF and continue to change.
- Write from the applicant's real record. Do not invent preliminary results, publications, collaborations, letters of support, or facilities.
- The budget must be real: rates from the funder's norms, equipment from quotations. Unjustified or padded items are cut and cost credibility.
- Aims that are too many or too ambitious for the duration are the most common reason for rejection.
- Follow the format exactly. Proposals are returned unread for exceeding limits or missing attachments.
- Submitting the same proposal to two funders usually must be declared, and double funding is not permitted.
- Plagiarism checks are applied to proposals; text reused from the applicant's papers should be rewritten for this purpose and cited.
- Human, animal, biosafety, and data-protection approvals are the applicant's responsibility and often must be in place or applied for.

## Related skills

- `research-gap-finder`, `novelty-checker`, and `research-question-formulator` for the idea and aims.
- `literature-review-writer` for the background section.
- `methodology-designer`, `experiment-planner`, and `sample-size-power-calculator` for the methodology.
- `ethics-irb-drafter` for ethics and data management sections.
- `citation-verifier` for the reference list.
- `academic-tone-editor` to fit word limits.
- `research-progress-tracker` to run the funded project against its milestones.
