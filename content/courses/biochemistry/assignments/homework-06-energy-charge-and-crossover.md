# Homework 6 practice: energy charge, crossover and reciprocal control

**Status:** open formative practice; this packet and its answer specifications are public and are not suitable for a protected or summative exam. It does not contribute to a course grade. The separate inactive Homework 6 review candidate is not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 2–3 hours
**Prerequisite lessons:** [Glycolysis and its control](../modules/10-glycolysis-energy-charge-and-amp-signal.md) and [Gluconeogenesis](../modules/16-gluconeogenesis-bypass-and-reciprocal-control.md).
**Dataset:** [synthetic crossover measurements](homework-06-crossover.csv).

## Purpose

Week 10 pairs a pathway's arithmetic with its control. Energy charge and AMP show how a modest fall in ATP becomes a strong signal; a crossover pattern shows where a pathway has been slowed; and the reciprocal control of glycolysis and gluconeogenesis shows why cells avoid running opposing steps at full speed together. The dataset is a crossover experiment: glycolytic intermediates measured in control and compound-treated cultures.

## Learning objectives

After working through the packet, learners should be able to:

1. Calculate AMP from the adenylate kinase equilibrium and the adenylate energy charge, and explain AMP amplification.
2. Count the ATP, GTP and NADH ledgers for gluconeogenesis from lactate.
3. Summarize intermediates by condition and locate a slowed step from a crossover.
4. Explain reciprocal control through fructose 2,6-bisphosphate and the purpose of avoiding futile cycles.

## Part A — energy charge

A stressed synthetic cell has ATP 2.5 mM and ADP 0.75 mM, with adenylate kinase at equilibrium (K = 1), so [AMP] = [ADP]²/[ATP]. The resting cell in the glycolysis lesson had ATP 3.0, ADP 0.3 and AMP 0.03 mM. Calculate AMP and the energy charge EC = ([ATP] + ½[ADP])/([ATP] + [ADP] + [AMP]), and compare AMP with the resting value.

**In words:** energy charge weights ADP as half an ATP, and AMP grows with the square of ADP, so it changes far more in relative terms than ATP does.

## Part B — glucose from lactate

A synthetic hepatic preparation makes 3.0 mmol glucose from lactate. From two pyruvate, one glucose costs 4 ATP, 2 GTP and 2 NADH, and lactate dehydrogenase makes one NADH for each lactate oxidized to pyruvate. Count ATP and GTP, and decide the net NADH balance.

## Part C — a crossover experiment

Three control cultures and three cultures treated with a fictional compound were extracted at the same time.

| Column | Meaning |
| --- | --- |
| `condition`, `culture` | `control` or `treated`; each culture is one independent preparation |
| `g6p_umol_per_g` … `pyruvate_umol_per_g` | Glucose 6-phosphate, fructose 6-phosphate (F6P), fructose 1,6-bisphosphate (FBP), phosphoenolpyruvate (PEP) and pyruvate, μmol per g protein |

To use the software checks, open **Practice gradebook** and select **Homework 6: energy charge, crossover and reciprocal control (open, ungraded practice)**. Average each intermediate within each condition and upload one UTF-8 CSV with exactly this header and column order, with rows `control` and `treated`:

```text
condition,culture_count,mean_f6p,mean_fbp,mean_pep
```

Then calculate treated/control ratios for F6P and FBP and decide where the crossover places the slowed step.

## Part D — reciprocal control

Use the structured check to state what fructose 2,6-bisphosphate does in liver, how glucagon shifts the balance in the lesson's model, and why opposing enzymes are coordinated.

## Worked calculation

For a different cell with ATP 2.0 mM and ADP 0.40 mM (K = 1), AMP = 0.16/2.0 = 0.080 mM and EC = (2.0 + 0.20)/(2.0 + 0.40 + 0.080) = 0.887. Because AMP = ADP²/ATP, the energy charge depends only on the ATP/ADP ratio here; two cells with the same ratio have the same charge even with different totals. In a crossover, write each treated/control ratio in pathway order; the step whose substrate ratio is above 1 and whose product ratio is below 1 is the candidate site.

## Analytic instructor rubric

For instructor-led discussion, use 0–2 points for each criterion: 0 for absent or incompatible evidence, 1 for a partly correct response, 2 for the evidence described. This guide is not connected to the software gradebook.

| Criterion | Evidence for full credit |
| --- | --- |
| Adenylates | Calculates AMP and energy charge and explains the squared dependence that amplifies AMP. |
| Gluconeogenesis ledger | Keeps ATP, GTP and NADH separate and accounts for NADH made from lactate. |
| Crossover | Summarizes cultures, orders ratios along the pathway and names PFK-1 without claiming a flux value. |
| Reciprocal control | Assigns opposite F2,6BP effects, links glucagon to lower F2,6BP and explains the cost of a futile cycle. |
| Scope | Treats liver regulation as a tissue-specific model rather than a universal rule. |

The autograded practice covers a subset of these criteria with deterministic numeric, CSV and structured-choice rules. Its keys are open in this repository. Written explanations are not scored automatically.

## Limitations and provenance

Original exercise with constructed values. The cells, compound and metabolite levels are fictional, adenylate kinase is treated as exactly at equilibrium with K = 1, and free and bound nucleotide pools are not distinguished. No laboratory protocol or medical interpretation is given. Original packet and synthetic dataset: CC BY 4.0.
