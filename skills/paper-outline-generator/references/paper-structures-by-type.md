# Paper structures, display items, and length budgets

## 1. Structures by paper type

### Empirical research (IMRaD)

| Section | Job | Typical share |
|---|---|---|
| Introduction | Context, gap, question, contribution | 10–15% |
| Methods | Enough detail to repeat the study | 20–25% |
| Results | Findings in the order of the questions, no interpretation | 25–30% |
| Discussion | Meaning, comparison with prior work, limitations, implications | 20–25% |
| Conclusion | The answer in a paragraph | 2–5% |

### Machine learning and other method papers (8 to 10 pages)

| Section | Typical pages | Contents |
|---|---|---|
| Introduction | 1–1.25 | Problem, gap, idea, results preview, contributions list, Figure 1 |
| Related work | 0.75–1 | Three to five lines of research, each with a contrast |
| Preliminaries or problem setup | 0.25–0.5 | Notation, task definition |
| Method | 2–2.5 | Overview, components, objective, algorithm box if useful |
| Experiments | 2.5–3 | Setup, main results table, ablations, analysis |
| Limitations | 0.25 | Often required by the venue |
| Conclusion | 0.25 | Summary and outlook |
| Appendix | unlimited or capped | Proofs, hyperparameters, extra results, checklist |

### Systems papers

Introduction; background and motivation (the bottleneck, with measurements); design (goals, architecture, key mechanisms); implementation; evaluation (end-to-end, micro-benchmarks, scalability, comparison); discussion; related work; conclusion.

### Theory papers

Introduction with an informal statement of the main result; related work; preliminaries and assumptions; main results with theorems; proof sketches; discussion of tightness and assumptions; full proofs in the appendix.

### Dataset and benchmark papers

Motivation and gap in existing data; collection; annotation (guidelines, workers, agreement, payment); quality control; statistics; baselines and analysis; intended uses and limits; ethics, licence, and maintenance; datasheet.

### Review articles

Introduction and scope; review method (search, selection); thematic or taxonomic sections; synthesis tables; open problems; conclusion.

### Short papers and letters

One contribution, one main result, compressed related work. Many venues allow 4 pages plus references.

## 2. Contribution statements

Each contribution states what was done and points to the evidence.

| Type | Pattern |
|---|---|
| Method | "We propose <name>, which <does X without Y> (Section 3)." |
| Finding | "We show that <finding> across <scope> (Section 5)." |
| Resource | "We release <dataset or tool> with <size and property> (Section 4)." |
| Analysis | "We identify <failure mode or phenomenon> and explain it by <cause> (Section 6)." |

## 3. Display items

| Item | Purpose | Placement |
|---|---|---|
| Figure 1 | The idea at a glance, or the headline result | Top of page 1 or 2 |
| Method diagram | Architecture or pipeline | Method section |
| Main results table | The central comparison | Start of experiments |
| Ablation table | Attribution of the gain | After the main table |
| Analysis figures | Trends, scaling, sensitivity | Analysis subsection |
| Qualitative examples | Concrete behaviour | End of experiments or appendix |

Plan display items before text. Readers often read the abstract, figures, and tables first.

## 4. What counts toward the limit

Check the call for papers: references, appendices, acknowledgements, ethics statements, and checklists are counted differently by different venues. Budget against the counted pages only.

## 5. Common structural problems

| Problem | Fix |
|---|---|
| Main result appears late | Preview it in the introduction and Figure 1 |
| Method explained only through equations | Add an overview paragraph and a diagram before details |
| Results section interprets and discusses | Move interpretation to the discussion |
| Several unrelated contributions | Cut to one message; move the rest to another paper |
| Experiments that support no claim | Remove or move to the appendix |
| Related work longer than the method | Cut to the closest work and groups |

## 6. Reverse outline check

After drafting, write one line per paragraph stating its point. Read the lines in order: they should form the argument. Paragraphs whose line repeats an earlier one, or does not support a claim, are candidates for cutting.

## 7. Venue facts to confirm

| Fact | Where |
|---|---|
| Page limit and what counts | Call for papers |
| Template and its year | Author kit |
| Required sections and statements | Call for papers, reviewer guidelines |
| Anonymity rules | Submission instructions |
| Supplementary material rules | Submission instructions |
| Checklist requirements | Template or call |
