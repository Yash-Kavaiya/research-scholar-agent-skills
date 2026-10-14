# Review criteria, reviewer questions, and scoring

## 1. Axes and the questions reviewers ask

| Axis | Questions |
|---|---|
| Significance | Does the problem matter? Who will use the result? Would the field change its practice or belief? |
| Novelty | What is new compared with the closest work? Is that work cited and compared? Is the novelty in the idea, the evidence, or the setting? |
| Soundness | Is the method correct? Do the experiments or proofs support each claim? Are comparisons fair? Are statistics appropriate? |
| Evaluation | Strongest baselines? Multiple datasets? Ablations? Variance? Failure cases? Cost? |
| Clarity | Can a reader in the area follow it? Are terms defined? Do figures stand alone? Could the method be reimplemented? |
| Related work | Are key papers missing? Is prior work described fairly? |
| Reproducibility | Code, data, hyperparameters, seeds, compute? |
| Ethics and limitations | Are risks, limitations, and data issues addressed? |

## 2. Three reviewer stances

| Stance | Focus | Typical comment |
|---|---|---|
| Subfield expert | Closest work, standard evaluation, whether the gain is real | "The comparison omits X (2024), which addresses the same problem." |
| Methodologist | Design, statistics, confounds, leakage | "Results are single runs; the 0.6-point gain is within typical seed variance." |
| Generalist or area chair | Clarity, significance, scope of claims | "The introduction does not explain why this problem matters beyond the benchmark." |

## 3. Frequent reasons for rejection

| Reason | Check |
|---|---|
| Incremental contribution | Is the difference from the closest work stated and shown to matter? |
| Missing or weak baselines | Are the strongest, most recent baselines included and tuned? |
| Overclaiming | Does every claim in the abstract have matching evidence? |
| Limited evaluation | More than one dataset or setting? |
| Unclear writing | Can the method be summarised from the paper alone? |
| Missing related work | Recent venue papers on the topic cited? |
| Out of scope | Does the venue publish this kind of paper? |
| Reproducibility concerns | Details and code available? |
| Ethical concerns | Data provenance, consent, misuse addressed? |

## 4. Severity

| Level | Definition | Typical consequence |
|---|---|---|
| Fatal | A main claim is unsupported or the method is incorrect | Reject |
| Major | The contribution is weakened or the evidence incomplete | Reject or major revision |
| Minor | Clarity, presentation, small omissions | Revision requested |
| Nitpick | Typos, formatting | Noted |

## 5. Scoring scales (illustrative)

| Venue type | Typical form |
|---|---|
| ML conferences | Overall score (for example 1 to 10 or 1 to 6), confidence (1 to 5), sub-scores for soundness, presentation, contribution |
| ACL-style conferences | Soundness and excitement scores, overall assessment, confidence |
| Journals | Recommendation: accept, minor revision, major revision, reject; comments to the editor and to the authors |

Use the target venue's current reviewer form; scales change.

## 6. Writing the mock review

| Part | Content |
|---|---|
| Summary | The paper in the reviewer's words: problem, approach, claims, evidence |
| Strengths | Specific, with locations |
| Weaknesses | Ranked by severity, each with location, why it matters, and what would resolve it |
| Questions | Ones whose answers could change the assessment |
| Missing references | Retrieved, with why they matter |
| Scores and recommendation | On the venue's scale, with confidence and reasoning |

## 7. Turning the review into a fix plan

| Issue type | Fix |
|---|---|
| Missing experiment that is feasible | Run it |
| Missing experiment that is not feasible | Narrow the claim; state the limitation |
| Overclaim | Reword to match the evidence |
| Unclear passage | Rewrite; add a figure or example |
| Missing citation | Add and discuss |
| Structural problem | Reorganise sections |

Prioritise by severity and by time to deadline.
