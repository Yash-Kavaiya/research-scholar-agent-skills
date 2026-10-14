# Ablation design patterns

## 1. Ablation types

| Type | What changes | Use when | Pitfall |
|---|---|---|---|
| Remove | Component deleted | It is optional to the pipeline | Removal may change capacity or break training |
| Replace with standard | Swapped for the common alternative | Removal is impossible or unfair | Choice of replacement drives the result; justify it |
| Replace with random or constant | Learned part replaced by random or fixed values | Testing whether learning in that part matters | Can be unrealistically weak |
| Vary | A continuous setting swept | Loss weights, sizes, temperatures, data amounts | Too few points to see the shape |
| Add incrementally | Components added one at a time to a baseline | Showing how gains accumulate | Results depend on the order |
| Oracle | A component replaced by ground truth | Showing the ceiling for improving that component | Only diagnostic |
| Shuffle | Inputs or features permuted | Testing reliance on structure or order | Interpretation needs care |

## 2. Structures and run counts

| Structure | Runs (n components) | Shows | Use |
|---|---|---|---|
| Leave-one-out | n + 1 | Each part is needed alongside the others | Default |
| Additive | n + 1 | Cumulative contribution | When the build-up story matters; justify the order |
| Full factorial | 2ⁿ | All interactions | Two or three key components |
| One-factor sweep | points × settings | Sensitivity | Key hyperparameters |

Multiply by the number of seeds and datasets.

## 3. Controls

| Confound | Control |
|---|---|
| Capacity changes | Match parameter count by widening another part, or report parameters per variant and discuss |
| Training budget | Same steps or epochs, same early-stopping rule |
| Hyperparameters tuned for the full model | Retune key ones (learning rate) per variant within the same budget, or state they were not retuned |
| Data | Identical splits, preprocessing, and augmentation |
| Randomness | Same seeds across variants |
| Compute or inference cost | Report alongside quality |

## 4. Interactions

Two components interact when the effect of removing both differs from the sum of removing each.

| Variant | Score |
|---|---|
| Full | 80 |
| without A | 76 |
| without B | 77 |
| without A and B | 70 |

Individual drops: 4 and 3, sum 7. Joint drop: 10. The extra 3 points are an interaction: A and B help each other. Leave-one-out alone would understate their joint value.

## 5. Seeds and significance

- Use the same number of seeds as the main table.
- Report mean ± SD and the difference from the full model.
- For small differences, use a paired comparison across seeds or test items.
- A difference inside the seed spread means no measurable contribution under these conditions.

## 6. Analyses that usually accompany ablations

| Analysis | Shows |
|---|---|
| Hyperparameter sensitivity | Whether the gain depends on a narrow setting |
| Data scaling | Whether the component matters more with little or much data |
| Model scaling | Whether the component's value shrinks at larger sizes |
| Cost per component | Accuracy gained per unit of compute, memory, or latency |
| Per-subset breakdown | Which inputs the component helps |
| Qualitative cases | Concrete examples of what changes, chosen by a stated rule |

## 7. Reading the finished table

| Pattern | Interpretation |
|---|---|
| Large drop when removed | Component contributes in this setting |
| No drop | Not needed here; reconsider the claim |
| Removal improves results | The component hurts; investigate before publishing |
| Drop only on some datasets | The contribution is conditional; say where |
| Big drop for a small component | Check whether removal also broke something else |

## 8. Writing it up

For each component: what was changed, the difference with its variability, and what the result shows. Keep claims within the conditions tested ("on dataset A, at this scale").

## 9. Budget-saving options

| Option | Trade-off |
|---|---|
| Ablate on one representative dataset | Generality not shown; say so |
| Ablate at a smaller scale | Effects may differ at full scale; state the scale |
| Fewer seeds for clearly large effects | Keep full seeds for close calls |
| Factorial only for the two central components | Interactions among others untested |
