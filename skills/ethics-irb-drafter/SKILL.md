---
name: ethics-irb-drafter
description: Drafts research ethics application material for human-participant and personal-data studies, including the protocol summary, risk assessment, participant information sheet, informed consent form, and data management plan, for review by the user's ethics committee. Use when the user asks to "write my IRB application", "ethics committee form", "IEC or REB submission", "draft a consent form", "participant information sheet", "data management plan", or "do I need ethics approval for this study".
---

# Ethics and IRB Drafter

Prepare complete first drafts of ethics documents from the user's actual study plan. The institution's committee decides; these drafts make its job, and the user's, easier.

## When to use

- A study involves human participants, their data, or human biological material.
- A funder or journal requires a data management plan or ethics statement.
- The user is unsure whether review is needed.

Hand off instead for the study design itself (`methodology-designer`) or the questionnaire (`survey-questionnaire-designer`).

## Inputs

- The study protocol: aims, design, participants, procedures, duration.
- Institution and country, and the committee's own form or template if it has one. Always use the institution's template when it exists.
- Participants: who, how many, how recruited, any vulnerable groups (children, patients, prisoners, students of the researcher, people with impaired capacity).
- Data: what is collected, identifiability, where stored, who has access, sharing plans.
- Funding and conflicts of interest.

Collect the facts first. Do not fill gaps with plausible-sounding details; list them as questions.

## Workflow

1. **Decide the review route** with the user: full review, expedited review, or exemption, according to the institution's rules. Explain the usual criteria, and state that only the committee can confirm the category. Research on public, non-identifiable data often qualifies for exemption but still commonly needs a formal determination.
2. **Identify the applicable frameworks**: the Declaration of Helsinki and the Belmont principles (respect for persons, beneficence, justice); national rules such as the Common Rule (US), ICMR National Ethical Guidelines (India), TCPS 2 (Canada); data law such as GDPR (EU/UK) or the DPDP Act (India). Name the ones that apply and tell the user to confirm with their research office.
3. **Draft the protocol summary**: background and justification, aims, design, participants with inclusion and exclusion criteria, sample size and its basis, recruitment, procedures step by step, time burden per participant.
4. **Write the risk assessment** as a table: risk (physical, psychological, social, legal, economic, privacy), likelihood, severity, mitigation. Include what happens on incidental findings or participant distress, with a referral route.
5. **Draft the participant information sheet** in plain language (aim for a reading age of about 12 to 14): purpose, why they were invited, what participation involves and how long, risks and benefits, voluntariness and the right to withdraw without penalty (and until when data can be withdrawn), confidentiality and its limits, data storage and retention, payment or compensation, who to contact with questions or complaints, and the approval reference.
6. **Draft the consent form**: short first-person statements with initial boxes, covering each element of the information sheet, separate optional consents (audio recording, data sharing, future contact), and signature lines. Add an assent form and parental consent for minors, and a verbal or online consent script where written consent is not practical.
7. **Draft the data management plan**: data types and volume; identifiers and how data is pseudonymised or anonymised; storage location and security; access control; retention period and deletion; sharing and repository; legal basis for processing; international transfer.
8. **Assemble supporting items**: recruitment text, instruments, debrief sheet, researcher safety plan, and the checklist of attachments the committee asks for.
9. **List what the user must supply or confirm**, and the points most likely to draw committee questions.

## Output format

Separate documents, each headed **DRAFT for review by <committee name>**:

- `protocol-summary.md`
- `risk-assessment.md` (table)
- `participant-information-sheet.md`
- `consent-form.md` (and assent or verbal script if needed)
- `data-management-plan.md`
- `open-questions.md`: facts still needed, and decisions that belong to the user, supervisor, or committee.

## Quality bar and pitfalls

- These are drafts. Say clearly that the institution's ethics committee must review and approve before any recruitment or data collection, and that this is not legal advice.
- Never state that a study "is exempt" or "does not need approval". Say what the rules usually provide and who decides.
- Never invent approval numbers, committee names, contact details, insurance arrangements, or storage systems. Use bracketed placeholders such as `[committee contact]` and list them.
- Consent language must be accurate about risks and about the limits of confidentiality (for example mandatory reporting, or small samples where people may be identifiable).
- Anonymous means no one, including the researcher, can identify a participant. Coded data with a key is pseudonymous. Do not mix the terms.
- Deception, covert observation, and research with vulnerable groups need specific justification and safeguards; flag them for the supervisor.
- Collecting data before approval cannot be fixed afterwards. Warn the user if their timeline implies it.
- Scraped or secondary data can still involve personal data and platform terms. Raise it.

## Related skills

- `methodology-designer` supplies the protocol details.
- `survey-questionnaire-designer` supplies the instruments to attach.
- `sample-size-power-calculator` for the sample-size justification.
- `dataset-finder` when secondary data and its licence are involved.
- `grant-proposal-writer` and `phd-research-proposal-writer` reuse the ethics and data management sections.
- `qualitative-coding-assistant` follows the confidentiality terms set here.
