# Homework 3 practice: initial rates, efficiency and inhibition modes

**Status:** open formative practice; this packet and its answer specifications are public and are not suitable for a protected or summative exam. It does not contribute to a course grade. The separate inactive Homework 3 review candidate is not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 2–3 hours
**Prerequisite lessons:** [Enzyme mechanisms and inhibition](../modules/02-enzyme-mechanisms-and-inhibition.md) and [Enzyme kinetics from data](../modules/05-enzyme-kinetics-from-data-and-inhibition-modes.md).
**Dataset:** [synthetic progress curves](homework-03-progress-curves.csv).

## Purpose

Every kinetic parameter rests on rates that are genuinely initial. This set starts there, with progress curves where an early window and a late window give different answers, and then uses the Michaelis–Menten model to compare two substrates and two inhibition modes. The aim is to know which quantity answers which question: kcat/Km at low substrate, kcat at saturation, and an inhibition pattern as a model fit rather than a structure.

## Learning objectives

After working through the packet, learners should be able to:

1. Calculate rates from defined time windows of a progress curve and judge which window is an initial rate.
2. Compare substrates by kcat/Km and by kcat, and say which comparison applies at low and at saturating substrate.
3. Predict rates under competitive and uncompetitive inhibition and say which mode substrate can overcome.
4. Explain why reciprocal plots distort estimates and why kcat needs the active-site concentration.

## Part A — progress curves

Four independent assays of a fictional enzyme started at 100 μM substrate. Product was measured at 0, 2, 4 and 20 minutes; one product forms per substrate consumed.

| Column | Meaning |
| --- | --- |
| `assay` | Assay A1–A4; each is an independent reaction |
| `substrate_initial_um` | Substrate at time zero, μM |
| `product_0min_um` … `product_20min_um` | Product at 0, 2, 4 and 20 minutes, μM |

For each assay calculate the rate over 0–4 minutes and over 0–20 minutes as (product at the end − product at the start) ÷ window length, then average the four assays for each window.

To use the software checks, open **Practice gradebook** and select **Homework 3: initial rates, efficiency and inhibition modes (open, ungraded practice)**. Upload one UTF-8 CSV with exactly this header and column order, with rows `window_0_4_min` and `window_0_20_min`:

```text
window,assay_count,mean_rate_um_per_min
```

Then report how much substrate was used by 4 minutes and how far the 0–20 minute rate falls below the 0–4 minute rate, and choose which window to report.

## Part B — two substrates

The same enzyme acts on S1 (kcat = 300 s⁻¹, Km = 150 μM) and S2 (kcat = 60 s⁻¹, Km = 6 μM). Compute each kcat/Km and their ratio. Decide which substrate is converted faster when both are present at 1 μM, and which gives the higher maximal rate when each is tested alone at saturation.

## Part C — two inhibition modes

With Vmax = 80 μM/min and Km = 8 μM, an inhibitor at 10 μM with K_I = 5 μM gives α = 1 + [I]/K_I = 3. Under competitive inhibition the apparent Km is αKm; under uncompetitive inhibition both Vmax and Km are divided by α. Predict the rate at 40 μM substrate for each model.

**In words:** a competitive inhibitor raises the substrate needed for half-maximal rate, while an uncompetitive inhibitor lowers the maximal rate and the half-saturating concentration together.

## Part D — what a fit can show

Use the structured check to interpret a rising apparent Km with constant Vmax, explain reciprocal-plot distortion and name the denominator for kcat.

## Worked calculation

Suppose an assay forms 3.0 μM product in the first 5 minutes from 120 μM substrate and 21.0 μM by 30 minutes. The 0–5 minute rate is 3.0/5 = 0.60 μM/min, with 2.5% of the substrate used; the 0–30 minute rate is 21.0/30 = 0.70 μM/min. A late window that gives a *higher* rate than the early one would itself be a warning: it suggests a lag, activation or an assay artifact rather than an initial rate, so inspect the whole curve before choosing a window. For S1 and S2 in Part B, kcat/Km is a second-order constant in μM⁻¹ s⁻¹; it is not a binding constant.

## Analytic instructor rubric

For instructor-led discussion, use 0–2 points for each criterion: 0 for absent or incompatible evidence, 1 for a partly correct response, 2 for the evidence described. This guide is not connected to the software gradebook.

| Criterion | Evidence for full credit |
| --- | --- |
| Rate windows | Computes per-assay rates, averages assays, and chooses the linear early window with under about 10% substrate used. |
| Efficiency | Uses kcat/Km for low, competing substrate and kcat at saturation, with units. |
| Inhibition modes | Predicts both rates from the stated α and explains which mode substrate overcomes. |
| Method limits | Explains reciprocal-plot distortion and the active-site denominator for kcat. |
| Claim boundary | Treats a kinetic pattern as model consistency, not a binding-site determination. |

The autograded practice covers a subset of these criteria with deterministic numeric, CSV and structured-choice rules. Its keys are open in this repository. Written explanations are not scored automatically.

## Limitations and provenance

Original exercise with constructed values. The enzyme, substrates, inhibitor and assays are fictional, and no laboratory protocol is given. Real enzymes can show multiple substrates, product inhibition, substrate inhibition or tight binding that these simple models omit. Original packet and synthetic dataset: CC BY 4.0.
