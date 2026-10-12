---
name: supervisor-finder
description: Finds potential PhD supervisors, postdoctoral mentors, and collaborators whose current research matches the user's interests, by searching recent publications and verifying each person's position on official pages, then drafts a short personalised first-contact email. Use when the user asks to "find professors working on X", "find a PhD supervisor", "who should I contact for a PhD in X", "find labs in Germany or the US for my topic", "write a cold email to a professor", or "check whether this professor is a good fit".
---

# Supervisor Finder

Identify researchers who are active in the user's area right now, confirm the facts about each, and help the user write to them in a way that gets read.

## When to use

- Looking for a PhD supervisor, postdoctoral host, or research collaborator.
- Assessing fit with a specific professor.
- Writing a first-contact email.

Hand off instead for the statement of purpose (`sop-and-research-statement-writer`) or the research proposal (`phd-research-proposal-writer`).

## Inputs

- Research interests, specific enough to search (a problem and a method, not a field).
- Constraints: countries, institutions, language, start date, funding needs, degree level.
- The user's background: degree, relevant projects, publications, skills.
- Any names already under consideration.

## Workflow

1. **Turn the interest into search queries**: 3 to 5 phrasings of the topic, as in `paper-search`.
2. **Find who is publishing on it now.** Use `paper-search` restricted to the last 3 to 4 years (its `--year-from` option, with JSON output), and tally the authors across the results. The senior or corresponding author (often last in CS, sciences, and engineering) is usually the group leader; first authors are usually students. Also check: programme committees and recent papers of the top venues in the area, authors of key papers found with `citation-graph-explorer`, and faculty lists of target departments.
3. **Build a longlist** of 10 to 20 names with their institution as shown on recent papers.
4. **Verify each person on official sources** (their institutional page, lab page, and Google Scholar or ORCID profile):
   - Current institution and position. People move; recent papers show old affiliations.
   - Whether they can supervise at the level sought, and are not retired, on long leave, or moved to industry.
   - Research themes in the last 2 to 3 years, which may differ from their most-cited work.
   - Stated instructions for prospective students. Many pages say how to apply, whether to email first, or that emails are not answered. Follow them.
   - Openings and funding: advertised positions, funded projects, programme deadlines.
5. **Assess fit** for each: topical overlap with recent work, methods match, group size and recent student output, where graduates went, and practical fit with the user's constraints. Read two or three recent papers of the top candidates (`paper-summarizer`).
6. **Shortlist 5 to 8** in tiers, with one specific reason for each.
7. **Draft the first email**, one per person, following these rules:
   - *Subject*: specific and plain: "Prospective PhD student (Fall 2027): robust speech recognition for low-resource languages".
   - *Length*: 120 to 180 words. Readable on a phone in under a minute.
   - *Paragraph 1*: who the sender is and the purpose, in two sentences.
   - *Paragraph 2*: one specific, accurate connection to a recent paper of theirs, with a thought or question that shows it was read, linked to the sender's own experience.
   - *Paragraph 3*: the ask: whether they are taking students for a given intake, or whether they would be open to a short conversation. Mention attached CV and transcript. Mention funding status if relevant.
   - Plain text, correct title and name, no attachments beyond a CV (and transcript if customary), no praise.
8. **Advise on sending**: use an institutional or professional address; send individually; follow up once after 10 to 14 days; then move on. Apply through the official process regardless of replies.
9. **Keep a tracking table** of who was contacted, when, and the response (`research-progress-tracker`).

## Output format

```markdown
## Shortlist for: <interest>, <constraints>
Verified on <date> from official pages.

| # | Name, position | Institution | Recent focus | Why a fit | Recent paper to cite | Application notes | Source |
|---|---|---|---|---|---|---|---|

## Not included, and why
- <Name>: moved to industry / not taking students / focus has shifted

## Draft emails
### To Prof. <Name>
Subject: ...
<body, 120 to 180 words>

## Before sending
- Confirm: <facts to recheck>; attach: CV, transcript
```

## Quality bar and pitfalls

- Every person, position, and paper must be verified from a retrieved source. Never produce a professor, email address, or paper from memory; a wrong affiliation or an invented paper in a first email ends the contact.
- Use only contact details published on official pages for professional contact. Do not guess or construct email addresses, and do not collect personal contact information.
- The email is the user's. Draft it from their real background, and have them read the cited paper themselves so they can discuss it.
- No mass mailing. Identical emails to many professors are recognised and ignored; a few well-prepared contacts work better.
- Do not overstate the user's experience or claim familiarity with work they have not read.
- Citation counts and rankings do not measure supervision quality. Where the user can, they should talk to current and former students.
- Respect stated preferences: if the page says "do not email, apply through the portal", the advice is to apply through the portal.
- Check eligibility and deadlines of the programme itself; a willing supervisor does not replace admission.

## Related skills

- `paper-search` and `citation-graph-explorer` to find active researchers and key papers.
- `topic-trend-analyzer` to see which groups lead a rising topic.
- `paper-summarizer` to read a candidate supervisor's recent work.
- `sop-and-research-statement-writer` and `phd-research-proposal-writer` for the application documents.
- `research-question-formulator` to state the research interest sharply.
- `research-progress-tracker` to track contacts and deadlines.
