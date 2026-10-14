# Routing playbooks

## 1. Locating the stage

| The user has | Stage | Usual entry skill |
|---|---|---|
| An area, no topic | Topic selection | topic-trend-analyzer, research-gap-finder |
| A topic, no question | Framing | research-question-formulator |
| A question, no design | Design | methodology-designer or experiment-planner |
| A design, no data | Execution | experiment-logger; ethics-irb-drafter if people are involved |
| Data or results | Analysis | statistical-test-selector, qualitative-coding-assistant, results-interpreter |
| Findings, no draft | Writing | paper-outline-generator |
| A draft | Pre-submission | self-peer-reviewer |
| Reviews | Revision | rebuttal-writer |
| An accepted paper | Dissemination | camera-ready-checker, paper-to-slides, paper-to-poster, paper-to-blog |

Ask at most two questions to locate the stage, then state the assumption.

## 2. Playbooks for common goals

### "I am starting a PhD and need a topic"
1. topic-trend-analyzer on two or three candidate areas.
2. research-gap-finder on the most promising area.
3. novelty-checker on the user's preferred gap or idea.
4. research-question-formulator.
5. supervisor-finder if the supervisor is not yet chosen.
6. phd-research-proposal-writer.
Checkpoint after 2 and 3: the user chooses.

### "Write my literature review chapter"
1. paper-search and citation-graph-explorer to build the corpus (or use the user's sources).
2. paper-summarizer on key papers; paper-comparison-matrix for the synthesis matrix.
3. literature-review-writer.
4. citation-verifier; academic-tone-editor.

### "Get this paper ready to submit to <venue> in two weeks"
1. self-peer-reviewer, focused on fatal and major issues.
2. Fix plan: experiment-planner or ablation-study-designer for missing experiments that fit the time; limitations-and-future-work-writer for the rest.
3. citation-verifier and bibtex-manager.
4. reproducibility-checklist if required.
5. latex-paper-formatter to the venue template.
6. camera-ready-checker.
7. cover-letter-writer for journals.

### "Analyse my survey data and write the results"
1. statistical-test-selector for each research question.
2. results-interpreter.
3. publication-figure-maker and latex-table-generator.
4. Results text from results-interpreter; academic-tone-editor.

### "I got reviews back"
1. rebuttal-writer to build the response matrix.
2. experiment-planner for requested experiments.
3. rebuttal-writer to draft; academic-tone-editor to fit the limit.
4. After acceptance: camera-ready-checker.

### "Apply for funding"
1. research-gap-finder and novelty-checker to sharpen the idea, if needed.
2. grant-proposal-writer, using its scheme reference for Indian funders.
3. methodology-designer, sample-size-power-calculator for the methods section.
4. ethics-irb-drafter for ethics and data management.
5. citation-verifier.

### "Present my accepted paper"
paper-to-slides or paper-to-poster; paper-to-blog for announcement; paper-to-explainer-video if a video is required.

### "Prepare for my defence"
viva-defense-prep; paper-to-slides for the presentation; self-peer-reviewer on the thesis to find weak points.

## 3. Handoffs: what each step passes on

| From | To | Artifact |
|---|---|---|
| research-gap-finder | research-question-formulator | chosen gap with evidence |
| research-question-formulator | methodology-designer / experiment-planner | primary question, objectives, hypotheses |
| methodology-designer | sample-size-power-calculator | primary analysis and effect size source |
| experiment-planner | experiment-logger | run list and configs |
| statistical-test-selector | results-interpreter | test output JSON and descriptives |
| results-interpreter | paper-outline-generator | claims table with wording |
| paper-search | annotated-bibliography-builder, literature-review-writer | JSON or Markdown of retrieved papers |
| bibtex-manager | citation-verifier | cleaned .bib |
| self-peer-reviewer | rebuttal-writer (anticipation), experiment-planner | weakness list and fix plan |

Keep artifacts in one project folder so later steps can read them.

## 4. Stop conditions

| Condition | Action |
|---|---|
| No supportable gap found | Report; widen or shift the topic with the user |
| Idea already done | Report the closest work; return to gap finding or sharpen the idea |
| Design cannot answer the question | Revise the question or the design before proceeding |
| Required sample or compute out of reach | Rescope with the user |
| Results do not support the planned claim | Report; narrow claims or plan more work |
| References cannot be verified | Do not treat the document as finished |
| Ethics approval missing for human data | Stop data collection steps until approved |

## 5. Decisions that belong to the user

Topic and question choice; design choice; acceptance of risks; venue; any statement submitted under their name; disclosure of AI assistance; ethical judgements.

## 6. Status reporting

At the end of each session: what was produced (with file names), decisions made, decisions pending, next step, and anything that failed or could not be checked. For long projects, record this with research-progress-tracker.
