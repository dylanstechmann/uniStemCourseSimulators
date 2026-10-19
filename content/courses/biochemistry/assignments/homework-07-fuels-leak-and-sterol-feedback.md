# Homework 7 practice: fat and ketone fuels, proton leak and sterol feedback

**Status:** open formative practice; this packet and its answer specifications are public and are not suitable for a protected or summative exam. It does not contribute to a course grade. The separate inactive Homework 7 review candidate is not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 2–3 hours
**Prerequisite lessons:** [Mitochondrial bioenergetics](../modules/11-mitochondrial-bioenergetics-and-atp-yield.md), [Fatty-acid beta-oxidation](../modules/19-fatty-acid-beta-oxidation.md), [Ketone-body synthesis and use](../modules/22-ketone-body-synthesis-and-use.md), [Glycogen storage and mobilization](../modules/17-glycogen-storage-and-mobilization.md) and [Cholesterol synthesis and lipoprotein transport](../modules/24-cholesterol-and-lipoproteins.md).
**Dataset:** [synthetic hepatocyte cholesterol ledger](homework-07-cholesterol-ledger.csv).

## Purpose

Weeks 11 and 12 follow fuel carbon into mitochondria and back out again as ketone bodies, and follow cholesterol through a feedback loop. The common skill is an explicit ledger with its convention stated: ATP equivalents only under named P/O values, a proton-motive force only with its electrical and pH parts, and a cholesterol pool only for a defined cell and interval. The dataset compares hepatocyte cultures with and without a fictional inhibitor of HMG-CoA reductase.

## Learning objectives

After working through the packet, learners should be able to:

1. Build a beta-oxidation and citric-acid-cycle ledger for an even-chain fatty acid and express it per mole and per O₂.
2. Apply the course's conditional ketone-body ATP-equivalent values and explain why liver exports ketones.
3. Calculate a proton-motive force, the free energy per mole of protons, and the cost of proton leak.
4. Compute cellular cholesterol-pool changes per culture and connect the pattern to sterol feedback.
5. Explain why muscle glycogen fuels muscle rather than blood glucose.

## Part A — stearate

Use the course convention: 2.5 ATP per mitochondrial NADH, 1.5 per FADH₂, 3 NADH, 1 FADH₂ and 1 GTP per acetyl-CoA in the citric acid cycle, 1 GTP = 1 ATP equivalent, and 2 ATP equivalents to activate a free fatty acid. For stearate (C18:0), find the acetyl-CoA produced, the ATP equivalents per mole and the ATP equivalents per O₂; complete oxidation uses 26 O₂ per stearate. Compare with glucose at about 5.33 ATP per O₂.

## Part B — ketone bodies

A synthetic extrahepatic mitochondrial model oxidizes 3.0 mmol acetoacetate and 2.4 mmol D-β-hydroxybutyrate. The lesson's convention assigns 19 and 21.5 ATP equivalents per mole, values that already include SCOT's bypass of one GTP-forming step. Find the total and explain why liver exports ketones instead of oxidizing them by this route.

## Part C — the proton gradient and leak

In a synthetic mitochondrial preparation at 37 °C, Δψ = 140 mV and the matrix is 0.80 pH unit more alkaline. Use Δp = Δψ + 61.5 mV × ΔpH, the free energy F × Δp per mole of protons, and 32 ATP per glucose (4 substrate-level, 28 oxidative). Find ATP per glucose when 20% of the proton flux leaks.

**In words:** both the voltage and the pH difference push protons back into the matrix, and leak removes part of the oxidative ATP while substrate-level ATP is unaffected.

## Part D — the cholesterol ledger

Three control cultures and three treated with a fictional HMG-CoA reductase inhibitor were measured over the same interval.

| Column | Meaning |
| --- | --- |
| `condition`, `culture` | `control` or `inhibitor`; each culture is one independent preparation |
| `synthesis_ug_per_h` | Cholesterol synthesis, μg/h |
| `ldlr_uptake_ug_per_h` | LDL-receptor-mediated uptake, μg/h |
| `bile_acid_conversion_ug_per_h` | Conversion to bile acids, μg/h |
| `vldl_export_ug_per_h` | Export in VLDL, μg/h |

To use the software checks, open **Practice gradebook** and select **Homework 7: fat and ketone fuels, proton leak and sterol feedback (open, ungraded practice)**. For each culture compute net change = synthesis + uptake − conversion − export, average within each condition, and upload one UTF-8 CSV with exactly this header and column order, with rows `control` and `inhibitor`:

```text
condition,culture_count,mean_net_change_ug_per_h,mean_ldlr_uptake_ug_per_h
```

Then use the structured check to explain the uptake change, the boundary of a cellular ledger, and why muscle glycogen does not directly raise blood glucose.

## Worked calculation

For lauroyl-CoA (C12:0) under the same convention: 12/2 − 1 = 5 turns and 6 acetyl-CoA, so NADH = 5 + 18 = 23, FADH₂ = 5 + 6 = 11 and GTP = 6. From free laurate, ATP equivalents = 23 × 2.5 + 11 × 1.5 + 6 − 2 = 78. For a hepatocyte with synthesis 20, uptake 15, conversion 12 and export 8 μg/h, the pool changes by +15 μg/h under those rates; that is a property of the modeled cell, not a plasma LDL change.

## Analytic instructor rubric

For instructor-led discussion, use 0–2 points for each criterion: 0 for absent or incompatible evidence, 1 for a partly correct response, 2 for the evidence described. This guide is not connected to the software gradebook.

| Criterion | Evidence for full credit |
| --- | --- |
| Fatty-acid ledger | Counts turns, acetyl-CoA and carriers, states the convention and explains the lower ATP per O₂. |
| Ketone ledger | Applies the stated per-mole values and the SCOT boundary, and explains hepatic export. |
| Gradient and leak | Combines Δψ and ΔpH correctly and applies leak only to oxidative ATP. |
| Cholesterol pool | Computes per-culture net change, averages cultures and links rising uptake to SREBP2 feedback. |
| Boundaries | Separates the cellular pool from plasma LDL and liver glucose export from muscle glycogen use. |

The autograded practice covers a subset of these criteria with deterministic numeric, CSV and structured-choice rules. Its keys are open in this repository. Written explanations are not scored automatically.

## Limitations and provenance

Original exercise with constructed values. ATP-equivalent totals depend on the stated P/O convention and ignore transport, leak and other costs unless stated. The cultures and inhibitor are fictional; nothing here is treatment, dosing or dietary advice, and no laboratory protocol is given. Original packet and synthetic dataset: CC BY 4.0.
