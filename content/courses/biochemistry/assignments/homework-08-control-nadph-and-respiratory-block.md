# Homework 8 practice: control, NADPH supply and a respiratory block

**Status:** open formative practice; this packet and its answer specifications are public and are not suitable for a protected or summative exam. It does not contribute to a course grade. The separate inactive Homework 8 review candidate is not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 2–3 hours
**Prerequisite lessons:** [Flux control and regulation](../modules/12-flux-control-and-layers-of-regulation.md), [The pentose phosphate pathway](../modules/18-pentose-phosphate-pathway.md), [Fatty-acid synthesis](../modules/23-fatty-acid-synthesis.md) and [Reading a metabolic perturbation](../modules/13-reading-a-metabolic-perturbation.md).
**Dataset:** [synthetic respiratory-block rates](homework-08-respiratory-block.csv).

## Purpose

The last two weeks ask how a pathway is controlled and how a whole cell responds when one part is blocked. The set uses flux control coefficients and an enzyme's turnover time to separate fast and slow control, links fatty-acid synthesis to the pentose phosphate pathway through NADPH, and ends with culture-level rates from a respiratory-chain block, where the measurement that discriminates between explanations matters more than the size of any one change.

## Learning objectives

After working through the packet, learners should be able to:

1. Use the summation theorem and control coefficients to predict small flux changes, and state the limit of linear estimates.
2. Calculate how long a change in enzyme amount takes under first-order turnover.
3. Connect the NADPH demand of palmitate synthesis to oxidative pentose-phosphate flux and other NADPH sources.
4. Summarize culture-level glucose, lactate and oxygen rates and choose the measurement that separates a respiratory block from a glycolytic defect.

## Part A — control

A synthetic four-enzyme pathway has C₁ = 0.40, C₂ = 0.35 and C₃ = 0.15 under one condition. Find C₄ from ΣC = 1 and the predicted flux change for a 30% increase in enzyme 2. Then explain why doubling enzyme 1 usually gives less than the linear estimate.

**In words:** a control coefficient is the fractional change in flux per fractional change in one enzyme, and the coefficients of a whole pathway add up to one.

## Part B — how fast enzyme amount changes

An enzyme with an 18-hour half-life is induced, so its synthesis rate jumps to a new constant value. Under first-order turnover, find the time to reach 75% of the way to the new level.

## Part C — NADPH for palmitate

A synthetic adipocyte preparation makes 1.5 mmol palmitate from cytosolic acetyl-CoA. Fatty-acid synthase uses 14 NADPH per palmitate; each glucose 6-phosphate through the oxidative pentose phosphate branch yields 2 NADPH. If that branch supplies 60% of the NADPH, find the NADPH required and the glucose 6-phosphate oxidized, and name another NADPH source from the course.

## Part D — a respiratory block

Three control cultures and three treated with a fictional respiratory-chain inhibitor were measured in the same medium.

| Column | Meaning |
| --- | --- |
| `condition`, `culture` | `control` or `inhibitor`; each culture is one independent preparation |
| `glucose_uptake_mmol_per_l_h` | Glucose uptake, mmol/(L·h) |
| `lactate_output_mmol_per_l_h` | Lactate output, mmol/(L·h) |
| `oxygen_use_mmol_per_l_h` | Oxygen consumption, mmol/(L·h) |

To use the software checks, open **Practice gradebook** and select **Homework 8: control, NADPH supply and a respiratory block (open, ungraded practice)**. Average each rate within each condition and upload one UTF-8 CSV with exactly this header and column order, with rows `control` and `inhibitor`:

```text
condition,culture_count,mean_glucose_uptake,mean_lactate_output,mean_oxygen_use
```

Then use the structured check to choose the discriminating measurement, interpret lactate per glucose and state what the rates do not establish.

## Worked calculation

The control cultures are close to the lesson's model with an ATP demand of 8.0 mmol/(L·h) and 85% oxidative supply: glucose uptake = 0.85 × 8.0/32 + 0.15 × 8.0/2 = 0.2125 + 0.600 = 0.8125 mmol/(L·h), lactate output = 2 × 0.600 = 1.20 and oxygen use = 6 × 0.2125 = 1.275. If glycolysis alone must supply 8.0 mmol/(L·h), uptake becomes 4.0 and lactate 8.0, a 4.9-fold rise in glucose uptake. Compare these model values with the measured culture means before interpreting them.

## Analytic instructor rubric

For instructor-led discussion, use 0–2 points for each criterion: 0 for absent or incompatible evidence, 1 for a partly correct response, 2 for the evidence described. This guide is not connected to the software gradebook.

| Criterion | Evidence for full credit |
| --- | --- |
| Control coefficients | Applies summation and the linear estimate and explains why large changes give smaller gains. |
| Turnover time | Uses first-order approach to a new steady state with the stated half-life. |
| NADPH ledger | Scales NADPH to palmitate, converts the pentose-phosphate share to glucose 6-phosphate and names malic enzyme. |
| Respiratory block | Summarizes cultures, uses oxygen use to discriminate explanations and interprets 2 lactate per glucose. |
| Scope | Does not identify a blocked complex or make a clinical claim from culture rates. |

The autograded practice covers a subset of these criteria with deterministic numeric, CSV and structured-choice rules. Its keys are open in this repository. Written explanations are not scored automatically.

## Limitations and provenance

Original exercise with constructed values. Control coefficients apply to one condition and to small changes; the cultures, inhibitor and rates are fictional, and the model ignores other fuels such as glutamine. No laboratory protocol or medical interpretation is given. Original packet and synthetic dataset: CC BY 4.0.
