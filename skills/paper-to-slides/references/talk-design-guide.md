# Talk design guide

## 1. Time budgets by format

| Format | Speaking time | Content slides | Results shown | Notes |
|---|---|---|---|---|
| Lightning or spotlight | 3–5 min | 3–5 | 1 | Problem, idea, one result, pointer to the poster or paper |
| Conference talk | 10–15 min | 10–14 | 2–3 | Most common |
| Long conference or seminar | 20–30 min | 15–25 | 3–5 | Room for method detail and one analysis |
| Invited talk or job talk | 45–60 min | 30–45 | Several studies | A research programme, not one paper |
| Thesis defence presentation | 20–45 min (per regulations) | 20–35 | All contributions | Contributions first, then each study |
| Journal club | 15–30 min | 10–20 | The paper's main evidence | Authors' claims and the presenter's critique, separated |

## 2. Assertion titles

The title states the slide's point as a sentence.

| Topic title | Assertion title |
|---|---|
| Results | Our method halves labelling cost at equal accuracy |
| Related work | Existing methods need paired data that clinics rarely have |
| Method overview | A frozen encoder plus a small adapter learns from 100 examples |
| Ablation | The adapter, not the encoder, drives the gain |

Audiences remember assertion titles. Keep them to two lines.

## 3. Slide composition

| Rule | Detail |
|---|---|
| One message per slide | If two, split |
| Visual first | A figure, diagram, or example supports the title |
| Text limit | About 30 words; no paragraphs |
| Font sizes | Titles 28–40 pt; body at least 18–20 pt; figure text at least 16 pt |
| Contrast | Dark text on light background or the reverse; avoid low-contrast colour pairs |
| Colour-blind safe | Same palette as the paper's figures |
| Reveal | Build complex figures step by step |
| Equations | Only when the equation is the point; explain each symbol aloud |
| Numbers | Few, large, with units and the comparison |

## 4. Rebuilding paper figures for slides

| Paper figure | Slide version |
|---|---|
| Multi-panel figure | One panel per slide |
| Table with many rows | A bar chart of three rows, or the table with the key row highlighted |
| Small fonts | Regenerate at slide size |
| Many series | The proposed method and the best baseline; others in grey |
| Dense architecture diagram | Simplified version with only the parts discussed |

## 5. Speaker notes

- Write as spoken sentences, about 130 words per minute.
- First sentence of each slide's notes says the assertion.
- End each slide's notes with the transition to the next.
- Mark where to pause after a key result.

## 6. Opening and closing

| Part | Pattern |
|---|---|
| Opening (first 30 seconds) | A concrete example of the problem, or the result stated plainly; then why it matters |
| Closing | The takeaway sentence, the one result to remember, links (paper, code), contact; leave this slide up during questions |

Do not end on a "Thank you" or "Questions?" slide alone; the summary slide is more useful during questions.

## 7. Backup slides

Prepare for the questions you are likely to get: missing baselines, ablations, dataset details, failure cases, cost, limitations, the closest related work, and anything reviewers raised. Number backup slides (B1, B2) for quick navigation.

## 8. Rehearsal

| Step | Check |
|---|---|
| First full run | Total time; slides that run long |
| Cut | Remove a slide rather than speed up |
| Second run | Mark the slide that should be reached at the halfway time |
| Q&A practice | Answer the likely questions in under a minute each |
| Equipment | Aspect ratio (16:9 usually), fonts embedded or PDF, videos playing, adapter, clicker |

## 9. Journal club structure

Context and question; the paper's method; the main results as the authors present them; the presenter's critique (validity, missing comparisons); discussion questions for the group.
