# Homework 4 practice: fitting replicate rates without a reciprocal plot

**Status:** open formative practice; this packet and its answer specifications are public and are not suitable for a protected or summative exam. It does not contribute to a course grade. The separate inactive Homework 4 review candidate is not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 2–3 hours
**Prerequisite lessons:** [Enzyme kinetics from data](../modules/05-enzyme-kinetics-from-data-and-inhibition-modes.md) and [Virtual lab 1: enzyme kinetics and inhibition](../labs/01-enzyme-kinetics-and-inhibition-from-data.md).
**Dataset:** [synthetic replicate rates](homework-04-replicate-rates.csv).

## Purpose

The week-7 virtual lab estimates kinetic parameters from a double-reciprocal line on tidy data. Real replicates scatter, and the reciprocal transformation gives the slowest, noisiest rates the most leverage. This set repeats the analysis on scattered synthetic data in two ways, by nonlinear least squares on the measured rates and by the reciprocal line, and asks what the difference does to the inhibition constant and to the apparent mode of inhibition.

## Learning objectives

After working through the packet, learners should be able to:

1. Summarize replicate rates by condition and substrate concentration with the assay day as the unit.
2. Fit the Michaelis–Menten hyperbola by nonlinear least squares and report Vmax and Km with units.
3. Compare those estimates with a double-reciprocal fit and explain the difference.
4. Estimate a competitive inhibition constant and recognize a spurious Vmax change.

## Scenario and data dictionary

A fictional purified enzyme was assayed at 1, 2, 4, 8, 16 and 32 μM substrate on three independent assay days, without inhibitor (`control`) and with 6.0 μM of a fictional inhibitor (`inhibitor`). Each rate is an initial rate from a validated early window.

| Column | Meaning |
| --- | --- |
| `condition` | `control` or `inhibitor` |
| `substrate_um` | Substrate concentration, μM |
| `assay_day` | D1, D2 or D3; each day has its own enzyme dilution and reactions |
| `rate_um_per_min` | Initial rate, μM product per minute |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Homework 4: fitting replicate rates without a reciprocal plot (open, ungraded practice)**.

### Part A — summarize

Average the three assay days at each concentration within each condition. Upload one UTF-8 CSV with exactly this header and column order, with rows `control` and `inhibitor`:

```text
condition,assay_days,mean_v_1um,mean_v_4um,mean_v_32um
```

### Part B — nonlinear fit

Fit v = Vmax[S]/(Km + [S]) to the six control means by minimizing the sum of squared rate residuals. A spreadsheet solver, Python's `scipy.optimize.curve_fit` or any curve-fitting tool works; the platform itself does not run code. Start near Vmax = 60 μM/min and Km = 5 μM. Fitting all eighteen replicate rates with equal weight reaches the same optimum, because every concentration has three replicates.

**In words:** choose the Vmax and Km that make the predicted hyperbola as close as possible to the measured mean rates, judged by squared differences on the rate scale.

### Part C — reciprocal fit

Fit a straight line to 1/v against 1/[S] for the same six control means by ordinary least squares. The intercept is 1/Vmax and the slope is Km/Vmax. Compare both parameters with Part B and explain the difference.

### Part D — inhibition constant

Fit the inhibitor means the nonlinear way. Under a simple competitive model, α = Km(apparent)/Km and K_I = [I]/(α − 1). Compare the result with what the reciprocal fits would give, and compare the two methods' Vmax values for the inhibitor series.

### Part E — boundaries

Use the structured check to name the replicate unit, the initial-rate condition and the claim a good competitive fit supports.

## Worked calculation

For a fixed trial Km, the best-fitting Vmax has a closed form: with x = [S]/(Km + [S]) for each point, Vmax = Σ(v·x)/Σ(x²). At Km = 4.0 μM the six control x values are 0.200, 0.333, 0.500, 0.667, 0.800 and 0.889, which give Vmax ≈ 60.1 μM/min. Repeating this for nearby Km values and keeping the smallest sum of squared residuals is a transparent way to check a solver. On the reciprocal scale, the 1 μM point sits at 1/[S] = 1.0, far from the others, so scatter in its rate moves the fitted line most.

## Analytic instructor rubric

For instructor-led discussion, use 0–2 points for each criterion: 0 for absent or incompatible evidence, 1 for a partly correct response, 2 for the evidence described. This guide is not connected to the software gradebook.

| Criterion | Evidence for full credit |
| --- | --- |
| Summary | Averages assay days per concentration and condition and keeps three days as the replicate count. |
| Nonlinear fit | Reports Vmax and Km with units from an untransformed least-squares fit and states the starting values or method. |
| Method comparison | Quantifies the reciprocal fit's differences and explains the leverage of low-rate points. |
| Inhibition | Computes α and K_I from the nonlinear fits and recognizes the reciprocal Vmax difference as an artifact. |
| Scope | Limits the conclusion to a model of purified-enzyme rates in this assay. |

The autograded practice covers a subset of these criteria with deterministic numeric, CSV and structured-choice rules; fitted values are accepted within a small tolerance. Its keys are open in this repository. Written explanations are not scored automatically.

## Limitations and provenance

Original exercise with constructed rates: the scatter was designed for teaching, not drawn from a measured error distribution, so no confidence intervals are implied. The enzyme and inhibitor are fictional, and no laboratory protocol is given. Weighted fits and parameter uncertainty would be needed for real data. Original packet and synthetic dataset: CC BY 4.0.
