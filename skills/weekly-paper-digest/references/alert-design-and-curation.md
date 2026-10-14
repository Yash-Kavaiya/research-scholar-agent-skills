# Alert design and curation

## 1. Query design

| Principle | Example |
|---|---|
| One concept per query | "retrieval augmented generation"; separately "hallucination detection" |
| Use the community's terms | Check titles of papers the user already reads |
| Two to four words | Long queries return nothing on arXiv |
| Add a category to cut noise | `cat:cs.CL AND all:hallucination` |
| Track a method by name | `all:"direct preference optimization"` |
| Track an author | `au:surname` (common surnames produce noise; combine with a category) |
| Track a dataset | the dataset's name as a phrase |

Start with three to six queries, then prune.

## 2. Common arXiv categories

| Category | Area |
|---|---|
| cs.AI | Artificial intelligence |
| cs.CL | Computation and language (NLP) |
| cs.CV | Computer vision |
| cs.LG | Machine learning |
| cs.IR | Information retrieval |
| cs.HC | Human-computer interaction |
| cs.CR | Cryptography and security |
| cs.RO | Robotics |
| cs.SE | Software engineering |
| stat.ML | Machine learning (statistics) |
| stat.ME | Statistical methodology |
| eess.AS, eess.IV, eess.SP | Audio and speech, image and video, signal processing |
| q-bio.* | Quantitative biology (for example q-bio.GN genomics, q-bio.NC neurons and cognition) |
| physics.* | Physics subfields |
| econ.EM | Econometrics |
| math.* | Mathematics subfields |

## 3. Ranking signals

| Signal | Use |
|---|---|
| Matched several queries | Likely central to the user's interests |
| Boost terms in title or abstract | User-chosen priorities (benchmark, survey, a method) |
| From groups the user follows | Add as boost terms or author queries |
| Code released | Often signalled in abstracts ("code is available") |
| Survey or benchmark | Higher value per paper for keeping up |

## 4. Curation

For each candidate in the top list, decide from the abstract:

| Decision | Criterion |
|---|---|
| Read first | Directly relevant to current work, or a major result |
| Also relevant | Related; worth a line |
| Needs action | Overlaps the user's project, new baseline or dataset, a survey to read fully |
| Skip | Off-topic despite matching words |

Write one or two lines per kept paper: what it does, why it matters to this user. Mark what was read: abstract or full text.

## 5. Signals of overlap with the user's project

- Same problem and similar method in the title or abstract.
- Uses the same dataset for a similar purpose.
- Cites the user's work or the same key papers.

Flag these for novelty-checker.

## 6. Tuning over time

| Observation | Adjustment |
|---|---|
| A query mostly returns noise | Add a category or a qualifying word; or drop it |
| Relevant papers missed | Add their key terms as a query |
| Too many papers per week | Raise ranking thresholds; fewer queries; shorter period |
| Too few | Lengthen the period; broaden a query |
| The user's focus changed | Replace queries |

Review the configuration every month or two.

## 7. Scheduling options

| Option | Notes |
|---|---|
| Claude Code `/schedule` or `/loop` | Runs the skill on a schedule with curation |
| cron (Linux, macOS) | Runs the script only; curation needs an agent run |
| Windows Task Scheduler | Same as cron |
| CI scheduled workflow | Script output as an artifact or an issue |

Keep the state file with the project so repeats are suppressed.
