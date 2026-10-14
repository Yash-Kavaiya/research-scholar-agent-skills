# Positioning patterns for related-work sections

## 1. Ways to group prior work

Choose three to five groups. Each group should relate differently to your contribution.

| Grouping | Groups look like | Good for |
|---|---|---|
| By problem | Same problem, other methods; neighbouring problems | Method papers |
| By method family | Supervised approaches; self-supervised; rule-based | Papers proposing a new approach in a crowded area |
| By component | Work on each part your system combines | Systems and pipeline papers |
| By assumption | Methods requiring X; methods requiring Y; methods requiring neither | Papers that relax an assumption |
| By evaluation | Benchmarks and metrics; analyses and critiques | Benchmark, dataset, and analysis papers |
| By application | Uses of the technique in each domain | Application papers |

A common, reliable layout: (1) the problem and its main approaches, (2) the technique you build on, (3) the closest work, (4) evaluation or data.

## 2. Paragraph template

1. **Run-in heading or topic sentence** naming the line of work.
2. **What the line does**, citing several papers together for the shared idea.
3. **One or two papers singled out**: the strongest and the closest, described accurately.
4. **Contrast sentence**: how your work differs, and why that matters.

## 3. Contrast sentences

| Relation | Pattern |
|---|---|
| Removes a requirement | "These methods require <X>. Ours needs only <Y>." |
| Different setting | "Prior work studies <setting A>; we address <setting B>, where <what changes>." |
| Builds on | "We build on <method> and extend it to <...> by <...>." |
| Complementary | "This line is orthogonal to ours and could be combined with it." |
| Different goal | "Whereas <A> optimises <X>, our aim is <Y>." |
| Different evidence | "<A> report <finding> on <data>; we test whether it holds for <...>." |
| Generalises | "<A> is the special case of our formulation where <...>." |

State differences as facts about the two approaches. Avoid evaluative verbs ("suffers from", "fails to", "ignores") unless you demonstrate the failure.

## 4. The closest paper

- Describe it in a way its authors would accept.
- State the precise difference: assumption, supervision, architecture, objective, data, scale, guarantee, or evaluation.
- Say what the difference buys, and point to the experiment that shows it.
- If the difference is small, say what it enables. Reviewers judge small differences by their consequences.

## 5. Concurrent work

| Case | How to write it |
|---|---|
| Appeared within a few months of your submission | "Concurrent with our work, <A> propose <...>. Unlike them, we <...>." |
| Appeared after submission | Add at revision or camera-ready, labelled as concurrent or subsequent |
| Very similar | Cite it, state the differences factually, and compare empirically if feasible |

## 6. Placement and length

| Placement | When |
|---|---|
| After the introduction | The reader needs the context to follow the method; common in ML, NLP, and vision venues |
| Before the conclusion | The method is easier to position once explained; common in systems and theory |
| Merged into background | Short papers; journals with a combined section |

Typical length is half a page to one page in an eight to ten page conference paper. Journals allow more.

## 7. Coverage check

- The most-cited papers on the problem.
- The last two years of the target venue on this topic.
- The papers your method's components come from.
- The strongest baselines in your experiments (each should be cited here).
- Any survey, cited once for readers who want more.

Every cited paper should earn its place. Padding with undiscussed citations is noticed.

## 8. Double-blind writing

- Refer to your own earlier work in the third person: "Lee et al. (2023) showed", not "we showed in [3]".
- Do not cite unpublished work of your own in a way that identifies you.
- Do not omit your own closely related work; that also draws attention.

## 9. Faults reviewers flag

| Fault | Fix |
|---|---|
| A list of papers with one sentence each | Group them and add the contrast |
| The closest work missing | Add it and state the difference |
| Mischaracterising a paper | Reread its method section; quote its own claim |
| Claiming prior methods "cannot" do something | Show it or soften to what was demonstrated |
| Only old citations | Add the recent venue papers |
| Related work that reads as an attack | Rephrase as factual differences |
