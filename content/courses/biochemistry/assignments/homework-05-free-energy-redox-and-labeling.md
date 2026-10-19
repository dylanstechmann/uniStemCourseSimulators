# Homework 5 practice: free energy, redox, labeling and nucleotide links

**Status:** open formative practice; this packet and its answer specifications are public and are not suitable for a protected or summative exam. It does not contribute to a course grade. The separate inactive Homework 5 review candidate is not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 2–3 hours
**Prerequisite lessons:** [Free energy in the cell](../modules/06-free-energy-coupling-and-redox.md), [Nucleotide biosynthesis and salvage](../modules/25-nucleotide-biosynthesis-and-salvage.md), [Bioenergetics and central carbon metabolism](../modules/03-bioenergetics-and-central-carbon-metabolism.md) and [The citric acid cycle](../modules/15-citric-acid-cycle-carbon-and-redox.md).
**Dataset:** [synthetic citrate labeling](homework-05-citrate-labeling.csv).

## Purpose

Weeks 8 and 9 move from enzymes to the energy and carbon accounts of metabolism. The questions here practise the distinction between a standard free-energy value and the actual ΔG in a cell, between a redox potential difference and the energy available at a particular step, and between a labeling fraction and a flux. A short folate scenario connects the nucleotide lesson to the same habit of following one cofactor through linked reactions.

## Learning objectives

After working through the packet, learners should be able to:

1. Calculate an actual ΔG and an equilibrium ratio and predict when a near-equilibrium step reverses.
2. Combine standard free energies for a coupled reaction and evaluate it under cellular ratios.
3. Convert reduction-potential differences into free energy and explain why electrons entering at ubiquinone support fewer pumped protons.
4. Summarize culture-level isotopologue data and keep labeling separate from flux.
5. Trace how folate regeneration links purine assembly and thymidylate formation.

## Part A — an actual ΔG

A fictional isomerization G ⇌ H has ΔG°′ = +7.5 kJ/mol. At 37 °C (RT = 2.577 kJ/mol) the next enzyme keeps [H]/[G] at 0.020. Use ΔG = ΔG°′ + RT ln([H]/[G]) and K′eq = exp(−ΔG°′/RT). Then predict what happens if [H]/[G] rises to 0.10.

## Part B — phosphocreatine as an ATP buffer

Phosphocreatine hydrolysis has ΔG°′ ≈ −43.0 kJ/mol and ATP hydrolysis ≈ −30.5 kJ/mol; textbook-level values vary between sources. For phosphocreatine + ADP → creatine + ATP, find ΔG°′ and K′eq, then the actual ΔG in a synthetic muscle cell with [phosphocreatine]/[creatine] = 2.0 and [ATP]/[ADP] = 10, where Q = ([creatine][ATP])/([phosphocreatine][ADP]).

## Part C — a redox ladder

Use textbook-level standard reduction potentials: NAD⁺/NADH −0.320 V, fumarate/succinate +0.031 V and ubiquinone/ubiquinol +0.045 V. With ΔG°′ = −nFΔE°′, n = 2 and F = 96.485 kJ/(V·mol), compare electrons passing from succinate to ubiquinone with electrons passing from NADH to ubiquinone.

**In words:** the free energy released is proportional to how much higher the acceptor's reduction potential is than the donor's.

## Part D — citrate labeling across cultures

Independently prepared cultures received a pulse of uniformly ¹³C-labeled glucose and were harvested once, at 5 or 20 minutes. Each row reports the citrate isotopologue percentages; other isotopologue classes are taken as zero in this simplified dataset.

| Column | Meaning |
| --- | --- |
| `culture` | Culture C1–C6; each is harvested once |
| `minutes_after_pulse` | 5 or 20 |
| `m0_pct`, `m2_pct`, `m3_pct` | Percentages of citrate with 0, 2 or 3 ¹³C atoms |

To use the software checks, open **Practice gradebook** and select **Homework 5: free energy, redox, labeling and nucleotide links (open, ungraded practice)**. For each culture calculate the labeled fraction (M+2 + M+3), average the cultures at each time, and upload one UTF-8 CSV with exactly this header and column order, with rows `minute_5` and `minute_20`:

```text
time_point,culture_count,mean_labeled_pct,mean_m3_pct
```

Then use the structured check to interpret the change, the M+3 signature and what a flux estimate would need.

## Part E — folate and nucleotides

A fictional compound inhibits dihydrofolate reductase in a cell model. Decide what the enzyme normally does, which nucleotide routes a sustained loss of tetrahydrofolate would limit, and how purine and pyrimidine assembly differ.

## Worked calculation

For a different fictional step with ΔG°′ = −4.0 kJ/mol and a cellular product/substrate ratio of 8.0 at 37 °C, ΔG = −4.0 + 2.577 × ln 8.0 = −4.0 + 5.36 = +1.36 kJ/mol: despite a favorable standard value, the step runs backward at that ratio, because K′eq = exp(4.0/2.577) = 4.72 is below 8.0. For the labeling data, a culture with 60% M+0, 30% M+2 and 10% M+3 has a labeled fraction of 40%; that is a property of the measured pool at harvest, not a rate.

## Analytic instructor rubric

For instructor-led discussion, use 0–2 points for each criterion: 0 for absent or incompatible evidence, 1 for a partly correct response, 2 for the evidence described. This guide is not connected to the software gradebook.

| Criterion | Evidence for full credit |
| --- | --- |
| Actual free energy | Uses ΔG°′ + RT ln Q with natural logarithms and compares Q with K′eq to predict direction. |
| Coupling | Combines standard values for the stated overall reaction and evaluates the actual ΔG under the given ratios. |
| Redox | Uses acceptor minus donor potentials and links the small succinate-to-ubiquinone step to fewer pumped protons. |
| Labeling | Summarizes cultures as units and separates label incorporation from flux. |
| Nucleotide links | Traces dihydrofolate regeneration to purine assembly and thymidylate formation and contrasts ring-construction order. |

The autograded practice covers a subset of these criteria with deterministic numeric, CSV and structured-choice rules. Its keys are open in this repository. Written explanations are not scored automatically.

## Limitations and provenance

Original exercise with constructed values; concentrations are treated as activities and the potentials are textbook-level values that differ among sources. The cells, compounds and labeling percentages are fictional, and the folate scenario is a mechanism exercise, not a statement about any drug or treatment. Original packet and synthetic dataset: CC BY 4.0.
