---
name: academic-tone-editor
description: Edits academic prose for clarity, concision, precise hedging, and formal register, removing filler, inflated vocabulary, stacked hedges, and formulaic phrasing while preserving meaning, technical terms, numbers, and citations. Use when the user asks to "improve the academic tone", "edit my paragraph", "make this more formal", "make this concise", "proofread my paper", "this sounds like AI wrote it, make it read naturally", or wants a language edit of a draft.
---

# Academic Tone Editor

Make the writing clearer and tighter without changing what it says. The author's claims, numbers, terms, and citations stay exactly as they are.

## When to use

- A draft section needs a language edit before submission or supervisor review.
- Prose is wordy, vague, informal, over-hedged, or formulaic.
- A non-native English writer wants idiom and grammar corrected.

Hand off instead when the problem is structure or argument (`paper-outline-generator`, `self-peer-reviewer`), or when text is too close to a source (`plagiarism-and-paraphrase-checker`).

## Inputs

- The text.
- Field and venue, and British or American spelling.
- Edit depth: *proofread* (grammar, spelling, punctuation only), *copyedit* (also wording and sentence structure; default), or *substantive* (also paragraph order and flow, with suggestions flagged).
- Anything that must not change: defined terms, quoted material, a required phrase.
- The venue's or institution's policy on AI-assisted editing, if the user knows it.

## Workflow

1. **Read the whole passage** before changing anything. Note the argument, the defined terms, and the author's voice.
2. **Protect the content.** Mark what will not be altered: technical terms, numbers and units, citations, equations, quotations, and the strength of each claim.
3. **Edit in passes:**
   1. *Clarity*: one idea per sentence; subject and verb close together; the actor named where it matters ("we measured", not "measurements were performed" when who did it matters); pronouns with a clear referent; terms used consistently (do not alternate "method", "approach", "technique" for the same thing).
   2. *Concision*: cut openers that carry nothing ("It is worth noting that", "In order to", "It can be seen that"); replace nominalisations with verbs ("perform an analysis of" becomes "analyse"); remove repeated statements and summaries of what was just said.
   3. *Hedging*: one hedge per claim, matched to the evidence. "May possibly suggest" becomes "suggests". Remove hedges from things that are simply true; keep them where the evidence is partial. Never strengthen a claim beyond what the author wrote.
   4. *Register*: no contractions or colloquialisms; no intensifiers ("very", "extremely", "clearly", "obviously"); no promotional words ("groundbreaking", "remarkable", "cutting-edge"); plain words over ornate ones ("use" over "utilise", "show" over "showcase").
   5. *Formulaic patterns*: vary sentence openings and length; remove signposting that announces instead of saying ("This section will discuss"); break up automatic triplets and paired contrasts used for rhythm; cut closing sentences that only restate the paragraph; remove stock transitions ("Moreover", "Furthermore", "Additionally") where the logic is already clear.
   6. *Mechanics*: grammar, articles, agreement, tense (past for what was done, present for general truths and what the paper shows), punctuation, spelling variant, number and unit style.
4. **Check meaning.** Compare each edited sentence with the original. If an edit changed the claim, its strength, or its scope, revert it or flag it as a question.
5. **Query, do not guess.** Where a sentence is ambiguous, give both readings and ask. Do not pick one and rewrite.
6. **Return** the edited text, a short change summary, and the queries.

## Output format

```markdown
## Edited text
<the full passage, ready to paste>

## What changed
- Concision: <N> words to <M> words
- Main edits: <three to six bullets with a before/after example each>

## Queries for the author
1. "<original sentence>": did you mean A or B?

## Left unchanged on purpose
- <terms, quotes, or sentences kept as written, and why>
```

For LaTeX input, return valid LaTeX and leave commands, labels, citations, and maths untouched. Offer a tracked-changes view (`latexdiff`, or bold and strikethrough) when asked.

## Quality bar and pitfalls

- Do not change the meaning, add content, or introduce a claim, number, example, or citation that was not in the original.
- Do not weaken or strengthen claims. Hedging edits adjust wording to evidence the author already described.
- Keep technical terms and defined notation even when a synonym would read better.
- Preserve the author's voice. An edit that makes every paragraph sound the same has gone too far.
- The purpose of removing formulaic phrasing is readability. This skill is for improving the author's own writing; it is not a tool for disguising the origin of text or evading detection software. If the user asks about AI-use rules, tell them to follow their venue's or institution's disclosure policy.
- Do not rewrite quotations or reference-list entries.
- When the passage has a problem that editing cannot fix (a missing step in the argument, an unsupported claim), say so instead of smoothing over it.

## Related skills

- `self-peer-reviewer` for problems of argument and evidence.
- `plagiarism-and-paraphrase-checker` when wording is too close to a source.
- `abstract-writer` and `introduction-writer` when a section needs rewriting, not editing.
- `thesis-chapter-writer` for terminology consistency across chapters.
- `latex-paper-formatter` for formatting after the language is settled.
- `citation-style-converter` for reference formatting.
