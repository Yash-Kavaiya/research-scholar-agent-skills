# Threats-to-validity catalogue and writing patterns

## 1. Catalogue by validity type

### Internal validity (is the causal or comparative claim sound?)

| Threat | Typical wording of the limitation |
|---|---|
| Confounding | "Groups differed in <X>, which may explain part of the difference." |
| Unequal tuning or effort | "Baselines used published hyperparameters while our method was tuned, which may favour our method." |
| Selection bias | "Participants self-selected, so they may be more motivated than the population." |
| Attrition | "Dropout was higher in <group>, which may bias the comparison." |
| Leakage | "We cannot rule out overlap between the test set and pretraining data." |
| Researcher degrees of freedom | "Analyses were not preregistered." |

### Construct validity (do the measures capture the concept?)

| Threat | Wording |
|---|---|
| Proxy metric | "<Metric> measures <X>, which is only a proxy for <concept>." |
| Self-report | "Outcomes were self-reported and may reflect social desirability." |
| Unvalidated instrument | "The adapted scale has not been validated in this population." |
| Annotator disagreement | "Inter-annotator agreement was moderate (kappa = 0.55), limiting label reliability." |

### External validity (does it generalise?)

| Threat | Wording |
|---|---|
| Narrow sample | "All participants were from one university." |
| Single dataset or domain | "We evaluate on English news text only." |
| Scale | "Experiments use models up to <size>; behaviour at larger scale is untested." |
| Time | "Data were collected in <period>; patterns may have changed." |
| Setting | "Laboratory conditions may not reflect use in the field." |

### Statistical conclusion validity

| Threat | Wording |
|---|---|
| Low power | "The sample can detect only effects of d = 0.6 or larger." |
| Few runs | "Results are averaged over three seeds; variance estimates are imprecise." |
| Multiple comparisons | "We tested <n> outcomes without correction; secondary results are exploratory." |

### Other

| Area | Examples |
|---|---|
| Method assumptions | Requires labelled data, stationarity, access to gradients |
| Resource requirements | Compute, memory, or data that limit who can use it |
| Ethics and societal impact | Bias across groups, privacy, misuse, environmental cost |
| Delimitations (chosen scope) | "We focus on <X> and do not address <Y>." |

## 2. Three-part limitation

> **What:** All participants were recruited from one hospital. **Consequence:** Practice patterns there may differ from smaller clinics, so the effect on referral times may not transfer. **Bound or mitigation:** The effect on documentation time, which depends on the software rather than local practice, is less likely to be affected.

Mitigation sentences must describe what was actually done or argued, not what could have been done.

## 3. Severity triage

| Severity | Consequence | Where it belongs |
|---|---|---|
| Changes a headline claim | The abstract or introduction overstates | Reword those claims; then state the limitation |
| Narrows a claim's scope | Holds only under conditions | Limitations section, with the scope |
| Minor | Completeness | Brief mention or omit |

## 4. Future work patterns

| Source | Pattern |
|---|---|
| From a limitation | "Because <limitation>, a next step is <study>, which would show <what>." |
| From an unexpected result | "The drop on <condition> suggests <hypothesis>; testing <design> would distinguish it from <alternative>." |
| From a new question the work opens | "If <finding> holds, <question> follows; <approach> could address it." |
| From an extension | "Extending <method> to <setting> requires <change>; we expect <outcome> because <reason>." |

Two to four concrete items are enough. Each names a question, an approach, and why it follows.

## 5. Tone

| Avoid | Prefer |
|---|---|
| Apology ("Unfortunately, due to time constraints") | Fact ("The study covers one semester.") |
| Defensiveness ("This does not affect our results.") | Reasoned bound ("This is unlikely to affect X because Y.") |
| Vague ("More research is needed.") | Specific question and design |
| Promises ("We will show") | Plans ("A next step is to test") |

## 6. Venue requirements

Some venues require a limitations section and treat its absence as a reason to reject; some ask for broader-impact or ethics statements; checklists ask whether limitations are discussed. Check the current call.
