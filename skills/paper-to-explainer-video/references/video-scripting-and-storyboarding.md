# Video scripting and storyboarding

## 1. Formats

| Format | Length | Aspect | Narration words | Notes |
|---|---|---|---|---|
| Short vertical clip | 30–90 s | 9:16 | 70–200 | Hook in the first 2–3 s; captions burned in; one idea |
| Video abstract | 2–5 min (venue rules) | 16:9 | 300–700 | Often required format and size limits |
| Explainer | 5–10 min | 16:9 | 700–1,400 | Room for method and one analysis |
| Recorded conference talk | slot length | 16:9 | as a talk | Slides with voice-over and an optional speaker inset |

## 2. Narration writing for the ear

| Rule | Reason |
|---|---|
| Short sentences, one idea each | Listeners cannot reread |
| Active voice | Clearer agent |
| Repeat key terms | Synonyms confuse listeners |
| Numbers rounded and few | Hard to retain by ear |
| Signpost transitions ("Here's the problem.") | Orientation |
| Read aloud and time it | Written scripts run long |

About 150 words per minute; leave pauses for animations to land.

## 3. Hooks

| Type | Example |
|---|---|
| Question | "What if a model could learn a new language from a hundred sentences?" |
| Surprising fact | "Half of the test questions in this benchmark appear online word for word." |
| Result first | "We cut labelling cost in half without losing accuracy. Here's how." |
| Concrete scenario | "A radiologist has 30 seconds per scan ..." |

## 4. Scene grammar

| Element | Guidance |
|---|---|
| Scene length | 5–20 s |
| Visual change | Something should change at least every few seconds |
| Build-up | Introduce elements as they are mentioned |
| Highlight | Colour or scale the element being discussed; dim the rest |
| Consistency | Same colour and shape for the same concept throughout |
| On-screen text | A few keywords; never the full narration |

## 5. Animation patterns for research content

| Content | Animation |
|---|---|
| Architecture | Blocks appear in order; data flows along arrows |
| Equation | Terms appear one at a time; transform to show derivation steps |
| Comparison chart | Axes draw, then bars or lines grow; the key difference highlighted |
| Algorithm | Step-by-step state changes on a small example |
| Dataset | Grid of examples zooming into one |
| Before and after | Split screen or wipe |

## 6. Manim notes (for mathematical and algorithmic content)

| Need | Manim objects and animations |
|---|---|
| Text and equations | `Text`, `MathTex`, `Write`, `TransformMatchingTex` |
| Diagrams | `Rectangle`, `RoundedRectangle`, `Circle`, `Arrow`, `VGroup`, `Create`, `GrowArrow` |
| Charts | `Axes`, `BarChart`, `plot`, `Create` |
| Emphasis | `Indicate`, `Circumscribe`, `FadeToColor` |
| Timing | `self.wait()`, `run_time=` matched to narration |

Render scenes separately and assemble with the narration track.

## 7. Captions and accessibility

- Captions from the final script (SRT or VTT), timed to the narration.
- Contrast for text and diagrams.
- No flashing more than three times per second.
- Do not rely on colour alone.

## 8. Audio

Record in a quiet room with a decent microphone; normalise levels; music, if any, low under narration and licensed. Synthetic voices should be disclosed where the venue or platform requires.

## 9. Asset list

Figures to remake at video resolution, diagrams to animate, screen recordings, B-roll, music and its licence, end card (title, authors, venue, link, funding).

## 10. Venue requirements

Check length, resolution, file size and format, caption requirements, and anonymity rules for review-stage videos.
