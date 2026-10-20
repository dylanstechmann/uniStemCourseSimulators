# Scaffold project guide: comparing synthetic candidates against explicit constraints (optional, ungraded)

**Status:** open, optional and ungraded. Five milestone self-checks in the Case studio save responses privately; nothing is submitted, collected or scored. The separate inactive project draft and its proposed review rubric remain unreviewed and are not served to learners.
**Introduced in:** course package version 0.4.0.
**Suggested time (unvalidated author estimate):** 2–4 hours across weeks 12 and 13.
**Prerequisite lessons:** [Scaffold architecture, degradation, and mechanics](../modules/02-scaffold-architecture-degradation-and-mechanics.md), [Porous scaffolds: porosity, stiffness and permeability](../modules/06-porosity-stiffness-and-permeability.md), [Degradation and release from hydrogels](../modules/05-degradation-and-release-time-scales.md) and [Virtual lab 1: degradation time course of a synthetic scaffold](../labs/01-degradation-time-course-of-a-synthetic-scaffold.md).
**Data:** the [project candidate table](../assessment-specs/scaffold-property-comparison.csv) and the [rehearsal candidate table](scaffold-rehearsal-candidates.csv).

## Purpose

The degradation lab follows one constructed scaffold over time. This project compares several hypothetical scaffold profiles at once, across architecture, transport and time-dependent mechanical support. It uses explicit constraints instead of a weighted score, so a strong result on one property cannot hide a failure on another. The last step names the evidence that a table like this cannot supply.

## The project

The candidate table gives, for candidates A, B and C, the initial porosity φ (`porosity_fraction`), the initial modulus E₀ in MPa, a permeability index (`permeability_scale_1e-12_m2`, in units of 10⁻¹² m²) and the modulus half-time t½ in days. For this exercise alone, assume

E(t) = E₀ × 2^(−t/t½).

A hypothetical candidate passes at a stated horizon only if it meets all four teaching criteria: φ ≥ 0.65, permeability index ≥ 4, E₀ ≥ 1.5 MPa and E(t) ≥ 0.8 MPa at the horizon. These numbers exist only for transparent arithmetic; they are not acceptance criteria for any real application, and nothing here predicts biocompatibility, cell response, structural safety or in-vivo behavior.

1. Recalculate E(42) and E(56) for A, B and C. Keep at least four significant digits during calculations and report MPa to three decimals.
2. Build a pass/fail matrix for the four criteria at day 42. Identify which candidates fail architecture, transport, initial mechanics or the time-dependent modulus requirement; do not average criteria into a single score.
3. Derive the time at which each modeled modulus reaches 0.8 MPa. Compare the resulting support horizons, then identify the maximum horizon that meets every criterion.
4. Repeat the feasibility decision at day 56 and explain why a candidate that passes at day 42 can fail under the longer horizon.
5. List the important missing evidence that prevents the table from supporting a real material decision, including uncertainty, degradation modes, geometry, loading, cell response, biological evidence and application-specific acceptance criteria.

## Milestones

| Milestone | Suggested week | Task | Where to check yourself |
| --- | --- | --- | --- |
| Rehearsal | 12 | Work the rehearsal candidates, then use the open rehearsal practice set | **Practice gradebook**: Scaffold project rehearsal |
| M1 | 12 | E(42) and E(56) for each candidate (task 1) | Case studio: project milestone 1 |
| M2 | 12 | Pass/fail matrix at day 42 (task 2) | Case studio: project milestone 2 |
| M3 | 12 | Support times and the maximum horizon (task 3) | Case studio: project milestone 3 |
| M4 | 13 | The decision at day 56 (task 4) | Case studio: project milestone 4 |
| M5 | 13 | Missing evidence (task 5) | Case studio: project milestone 5 |

Each Case studio milestone lists self-review statements. Responses are saved privately in this application and are never scored.

## Rehearsal candidates

The [rehearsal table](scaffold-rehearsal-candidates.csv) has the same columns and two candidates, P and Q, judged against different teaching criteria at different horizons: porosity ≥ 0.70, permeability index ≥ 5, E₀ ≥ 2.0 MPa and E(t) ≥ 1.0 MPa, at day 30 and day 45. Work the same steps on it, then check yourself with the open rehearsal practice set, which gives feedback on each value. Its candidates, criteria and horizons differ from the project's, so its answers are not the project's answers.

## Worked example: one more candidate

Take a separate synthetic candidate X with φ = 0.80, permeability index 9, E₀ = 3.0 MPa and t½ = 20 days, judged against a modulus criterion of 1.2 MPa.

1. **Modulus.** At day 10, E(10) = 3.0 × 2^(−10/20) = 3.0 × 0.7071 ≈ 2.121 MPa.
2. **Support time.** Setting 3.0 × 2^(−t/20) = 1.2 gives t = 20 × log₂(3.0/1.2) = 20 × log₂(2.5) ≈ 26.44 days.
3. **Horizon.** X meets the modulus criterion at any horizon up to about 26.4 days and fails it after that, whatever its porosity and permeability.

Each half-time halves whatever modulus remains, so the modulus never reaches zero in this model, but it does cross any fixed threshold at a definite time. A natural logarithm needs the conversion log₂(x) = ln(x)/ln(2); using ln(x) alone shortens the support time by a factor of about 0.69.

## Reporting conventions

- Report moduli in MPa to three decimals and times in days with sensible precision.
- Keep at least four significant digits in intermediate values and round only reported results.
- Mark each criterion separately in the matrix, and say which criterion each failing candidate misses.
- Disclose any software, spreadsheets or AI assistance you used.

## Self-review rubric

The inactive project draft proposes five criteria for a future human reviewer and assigns them no points. For self-review, mark each criterion 0 (absent), 1 (partly correct) or 2 (complete and consistent with the stated model).

| Criterion | Evidence of a complete response |
| --- | --- |
| Degradation calculation | Applies the exponential half-time relation with correct values and units |
| Constraint logic | Evaluates every criterion separately and does not average away a failure |
| Time horizon | Solves the threshold time and repeats the decision at the longer horizon |
| Evidence limits | Identifies missing material, biological and uncertainty evidence |
| Scope | Avoids presenting the synthetic comparison as a real selection or safety recommendation |

These marks are a self-check. They are not calibrated, carry no grade and do not stand in for an instructor's judgment.

## Limitations and provenance

The candidates, criteria and horizons are synthetic teaching values. The single-exponential modulus model ignores uncertainty, degradation mode, geometry, loading and any biological response, and nothing here is a material specification, scaffold design, implant recommendation or claim about a real material. Original guide and synthetic rehearsal data: CC BY 4.0, developed with substantial AI assistance.
