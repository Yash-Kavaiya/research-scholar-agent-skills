---
name: paper-to-code-reproducer
description: Implements a research paper's method from the PDF, extracting the algorithm, architecture, hyperparameters, and evaluation protocol, recording every detail the paper leaves out, and comparing the reproduced numbers with the reported ones. Use when the user asks to "implement this paper", "reproduce these results", "turn this paper into code", "write PyTorch code for this method", "there is no official code for this paper", or needs a baseline reimplemented.
---

# Paper to Code Reproducer

Turn a paper into working code and an honest account of how close the reproduction is. Papers omit details; the work is in finding those gaps and recording how each was filled.

## When to use

- A paper has no released code, or its code is unusable.
- A baseline must be reimplemented for a fair comparison.
- The user wants to understand a method by building it.

Hand off instead for understanding only (`paper-summarizer`, `math-and-equation-explainer`).

## Inputs

- The paper's full text with appendix and supplementary material.
- Which result to reproduce (a specific table or figure). Reproducing "the paper" is too broad.
- Framework, hardware, and time available.
- The dataset, or access to it.

## Workflow

1. **Look for existing code first.** Check the paper and its arXiv page for a repository link, search Papers with Code and GitHub, and check the authors' pages. If official code exists, read it; it resolves ambiguities even when you reimplement. Check its licence before reusing any of it.
2. **Fix the target**: one table or figure, the exact metric, dataset, and split.
3. **Extract the specification** into a document:
   - Data: source, preprocessing, augmentation, splits, tokenisation or normalisation.
   - Model: every layer or step with dimensions, activations, normalisation, initialisation.
   - Objective: loss terms with weights, regularisation.
   - Optimisation: optimiser, learning rate and schedule, warm-up, batch size, epochs or steps, gradient clipping, precision, weight decay, EMA.
   - Evaluation: metric definition, checkpoint selection, test-time settings, number of seeds.
   - Compute: hardware and training time reported.

   Give each item a source (section, equation, table, appendix) or mark it **unspecified**.
4. **Resolve the unspecified items** in this order: official code; the paper's cited predecessor or the standard for that benchmark; the framework default; your judgement. Record each choice and its basis in an assumptions log. Offer to draft an email to the authors for details that matter and cannot be inferred.
5. **Plan the build** in testable units: data pipeline, model, loss, training loop, evaluation. Use a config file for every hyperparameter and fix seeds.
6. **Implement with checks at each unit:**
   - Shape assertions and a forward pass on a tiny batch.
   - Parameter count against the paper's reported count.
   - Loss on random input against the expected value (for example ln(C) for C-way cross-entropy at initialisation).
   - Overfit a single small batch to near-zero loss before any full run.
   - Unit tests for equations implemented from the paper, on hand-computed cases.
   - The evaluation metric checked against a reference implementation.
7. **Run small, then scale.** A short run on a data subset first, then the full configuration. Log every run (`experiment-logger`).
8. **Compare with the paper** in a table: reported, reproduced (mean and standard deviation over seeds), and the difference. State whether the reproduction is within the paper's own variance, close, or not reproduced.
9. **Diagnose gaps** systematically: data preprocessing, evaluation protocol, schedule length, an assumption from step 4. Change one thing at a time.
10. **Write the README**: how to run, results table, assumptions log, known deviations.

## Output format

```
repo/
  README.md            # commands, results vs paper, deviations
  SPEC.md              # extracted specification with sources
  ASSUMPTIONS.md       # every unspecified detail and the choice made
  configs/<exp>.yaml
  src/{data,model,loss,train,evaluate}.py
  tests/
  requirements.txt
```

Results table in the README:

```markdown
| Setting | Paper | Ours (mean ± sd, n seeds) | Difference |
|---|---|---|---|
```

## Quality bar and pitfalls

- Report the numbers you obtained. Never copy the paper's numbers into the "ours" column, and never claim a reproduction that was not run to completion. If only a reduced run was possible, label it as such.
- Do not hide deviations. A reproduction with documented differences is useful; one with silent differences misleads.
- Most failed reproductions come from data preprocessing and evaluation protocol, not the model. Check those first.
- Papers contain errors and omissions. When an equation and the text disagree, note it, pick one with a reason, and test both if cheap.
- Do not tune on the test set to match the reported number.
- Respect licences for code and data. Reimplementing from a paper is fine; copying code from a repository needs its licence to allow it and attribution.
- If compute is far below what the paper used, say what can and cannot be verified at the smaller scale.

## Related skills

- `paper-summarizer` and `math-and-equation-explainer` to understand the method first.
- `dataset-finder` to obtain the data.
- `experiment-logger` to record runs and decisions.
- `experiment-planner` when the reproduction is a baseline in a larger study.
- `results-interpreter` to interpret differences from the reported numbers.
- `reproducibility-checklist` to document the reproduction.
