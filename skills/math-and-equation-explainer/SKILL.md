---
name: math-and-equation-explainer
description: Explains equations, derivations, proofs, and notation from research papers step by step, defining every symbol, justifying each step, and checking dimensions and special cases. Use when the user pastes an equation or screenshot and asks "explain this equation", "how did they get from equation 3 to 4", "what does this notation mean", "derive this loss function", "walk me through this proof", or is stuck on the maths in a paper.
---

# Math and Equation Explainer

Make a piece of mathematics understandable to this reader: what each symbol is, what the expression says, and why each step follows.

## When to use

- A paper's equation, derivation, or proof is blocking the user.
- Notation is unfamiliar or inconsistent between papers.
- The user needs to re-derive a result to trust or extend it.

Hand off instead for understanding the paper as a whole (`paper-summarizer`) or for implementing the maths (`paper-to-code-reproducer`).

## Inputs

- The equation or derivation, with surrounding text. Context decides what symbols mean; ask for the paragraph before and after if it is missing.
- The paper or source, to check its notation section and conventions.
- The reader's level: what they already know (calculus, linear algebra, probability, measure theory). Ask if unclear.

## Workflow

1. **Transcribe the equation** in LaTeX and confirm it matches the source, especially for screenshots. Subscripts, superscripts, and bold or calligraphic letters change meaning.
2. **Build the symbol table.** For each symbol: name, type (scalar, vector, matrix, set, function, random variable, operator), shape or domain, and meaning here. Mark any symbol whose meaning you inferred from context.
3. **Say what the equation states in one plain sentence** before any algebra.
4. **Explain the structure**: which term does what, and what happens when each grows or vanishes.
5. **For a derivation, show every step.** One operation per line, each with its justification: the rule, identity, or assumption used (chain rule, Jensen's inequality, independence, a Taylor expansion to first order). Fill in the steps the paper skipped, and flag each one you supplied.
6. **Name the assumptions** each step needs (differentiability, interchange of limit and integral, i.i.d. samples, positive definiteness). Note any the paper does not state.
7. **Sanity-check:**
   - Dimensions or shapes agree on both sides.
   - A special or limiting case gives a known result.
   - A small numeric example works; compute it with code when the arithmetic is non-trivial.
8. **Give the intuition** last: a geometric picture, an analogy, or the reason the form is natural. Label analogies as such.
9. **If a step does not follow**, say so. State what you tried, where it breaks, and whether it looks like a typo, a missing assumption, or a gap in your reading.

## Output format

```markdown
## The equation
$$ ... $$   (source: <paper>, Eq. <n>)

## In one sentence
...

## Symbols
| Symbol | Type and shape | Meaning | Source |
|---|---|---|---|
| $\theta$ | vector in $\mathbb{R}^d$ | model parameters | §2 |
| $\lambda$ | scalar > 0 | regularisation weight | inferred from context |

## Term by term
- $...$: ...

## Derivation
1. Start from ... $$ ... $$
2. Apply <rule> because <reason>: $$ ... $$
3. *(step not shown in the paper)* ...

## Assumptions used
- ...

## Checks
- Shapes: ...
- Limiting case: as $\lambda \to 0$, ...
- Numeric example: ...

## Intuition
...
```

Use `$...$` and `$$...$$` so the maths renders. Match the paper's notation; if you must change it, say so once and keep a mapping.

## Quality bar and pitfalls

- Do not skip steps the reader cannot do in their head. "It can be shown that" is what they came to get past.
- Do not guess a symbol's meaning silently. Mark inferences, and check the paper's notation section first.
- Verify algebra you produce. Recompute a derivation numerically or symbolically (for example with SymPy) when it is long or error-prone.
- Papers contain typos and sign errors. If the derived result differs from the printed one, show both and say which you believe and why.
- Conventions differ across fields: row versus column vectors, numerator versus denominator layout for derivatives, log base, expectation subscripts. State the convention in use.
- Intuition is not proof. Keep the two separate.

## Related skills

- `paper-summarizer` for the context the equation sits in.
- `paper-critic` when a derivation's assumptions look unrealistic.
- `paper-to-code-reproducer` to turn the explained maths into an implementation.
- `latex-paper-formatter` to typeset derivations the user writes.
- `viva-defense-prep` when the user must explain the derivation aloud.
