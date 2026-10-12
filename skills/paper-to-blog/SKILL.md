---
name: paper-to-blog
description: Rewrites a research paper as a plain-language blog post, press-style summary, or social media thread for a chosen audience, leading with the finding, explaining the method by analogy, and keeping the caveats and numbers accurate. Use when the user asks to "write a blog post about my paper", "explain my paper for a general audience", "make a Twitter/X or LinkedIn thread about this paper", "write a lay summary", "plain-language summary", or wants to publicise a publication.
---

# Paper to Blog

Explain the research to people outside the subfield without saying anything the paper does not support. Accuracy is kept; jargon and detail are what go.

## When to use

- Announcing or explaining a new paper on a blog, lab website, newsletter, or social platform.
- A journal or funder requires a lay or plain-language summary.
- Explaining someone else's paper to a wider audience.

Hand off instead for a talk (`paper-to-slides`) or a video (`paper-to-explainer-video`).

## Inputs

- The paper, including its limitations section.
- The audience: general public, practitioners in the field's industry, researchers in neighbouring fields, students, or policymakers.
- The format and platform: blog post (600 to 1,200 words), lay summary (150 to 300 words, per the journal's rules), thread (6 to 12 posts within the platform's character limit), LinkedIn post, newsletter item.
- Voice: the author's own first person, a lab's voice, or third-person reporting.
- Links to include: paper, preprint, code, data, demo.

## Workflow

1. **Find the story.** Answer in one sentence each: What did you find? Why should this reader care? What can someone do with it? What is still unknown? The first answer is the opening.
2. **Pick the audience's level** and decide which terms must be explained and which can be dropped. Explain a term the first time or replace it with a description.
3. **Structure for the format.**

   *Blog post*
   1. Title that states the finding or asks the question it answers.
   2. Opening paragraph: the finding and why it matters, in plain words.
   3. The problem: what was unknown or hard, with a concrete example.
   4. What was done: the approach by analogy or example, no more method than the reader needs.
   5. What was found: the two or three main results, with the key numbers in context.
   6. What it means and what it does not: implications and limits.
   7. What comes next, and links.

   *Thread*
   1. Post 1: the finding and why it matters, standing alone, with the key figure.
   2. Posts 2 to 3: the problem.
   3. Posts 4 to 6: the approach and results, one idea and ideally one image each.
   4. One post on limitations.
   5. Final post: link to the paper and code, credit to co-authors and funders.

   *Lay summary*: follow the journal's headings and word limit; aim for a reading age of about 12 to 14.
4. **Translate the numbers.** Put them in context ("from 12 errors in 100 to 9") and prefer absolute figures to relative ones for risks and effects. State what was measured, on what or whom.
5. **Use analogies carefully.** An analogy should make the mechanism clearer; say where it stops being accurate if a reader might over-extend it.
6. **Keep the caveats.** State the study type and its limits in plain language: sample, setting, whether it is a preprint not yet peer reviewed, and correlation versus causation. Match the paper's verbs: if the paper says "is associated with", the post does too.
7. **Choose visuals**: one clear figure from the paper, simplified and re-captioned, or a diagram (`publication-figure-maker`, `architecture-diagram-maker`). Add alt text.
8. **Write a headline that is true.** No "breakthrough", "cure", "solves", or "proves". Check that the headline alone would not mislead.
9. **Check against the paper**, sentence by sentence, for anything stronger than the source. For a post about someone else's paper, make clear whose work it is and link to it.
10. **Give variants**: alternative titles and, for threads, a shorter version.

## Output format

```markdown
## <Title>
<post body, with subheadings for a blog post>

*Paper: <citation and link>. Code: <link>. Authors: ...*

---
## Notes
- Audience and reading level: ...
- Claims checked against: §, Table, Fig.
- Caveats included: ...
- Alternative titles: ...
- Suggested image and alt text: ...
```

For a thread: numbered posts, each within the platform's limit, with the character count.

## Quality bar and pitfalls

- Never state a result, number, or implication that is not in the paper. Simplifying is allowed; changing the claim is not.
- Do not turn a study in mice, in simulation, or on one dataset into a claim about people or the real world. Say what was studied.
- Health, safety, and financial topics need extra care: no advice to readers, and the limits stated near the top.
- Keep relative and absolute effects straight; "doubles the risk" from 1 in 10,000 to 2 in 10,000 must say so.
- Label a preprint as not yet peer reviewed.
- Avoid hype words and manufactured suspense. Readers and journalists discount them, and they damage the author's credibility.
- Credit co-authors, collaborators, and funders, and check the journal's embargo and press policy before publishing.
- Do not use copyrighted figures from the published version without checking the licence; use the author's own originals or an open-access version.
- Write in the author's voice from their material. If the user will post it under their name, they should read and own every sentence.

## Related skills

- `paper-summarizer` to extract the findings and limitations accurately.
- `results-interpreter` for wording that matches the strength of the evidence.
- `abstract-writer` for the formal counterpart.
- `publication-figure-maker` and `architecture-diagram-maker` for a simplified visual.
- `paper-to-explainer-video`, `paper-to-slides`, and `paper-to-poster` for other formats.
- `academic-tone-editor` is the opposite direction (formal register); do not apply it to the post.
