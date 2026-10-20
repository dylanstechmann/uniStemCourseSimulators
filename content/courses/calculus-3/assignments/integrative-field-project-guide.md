# Field project guide: amount and outward transfer in a bounded concentration field (optional, ungraded)

**Status:** open, optional and ungraded. Five milestone self-checks in the Case studio save responses privately; nothing is submitted, collected or scored. The separate inactive project draft and its proposed review rubric remain unreviewed and are not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 3–5 hours across weeks 13 and 14.
**Prerequisite lessons:** [Gradients in a concentration field](../modules/05-gradients-in-a-concentration-field.md), [Optimizing with and without constraints, and integrating in polar coordinates](../modules/06-constrained-optimization-and-polar-integrals.md), [Hessians, constraints and boundary optima](../modules/09-hessians-constraints-and-boundary-optima.md), [Multiple integrals and Jacobian measures](../modules/10-multiple-integrals-and-jacobian-measures.md) and [Surface flux and the divergence theorem](../modules/12-surface-flux-and-divergence.md).

## Purpose

One smooth field can be asked several questions: where it is largest, how much it holds in total, and how much leaves through the boundary. This project answers each with a different tool, gradients and boundary comparison, a polar integral with its Jacobian, an oriented line integral and the divergence theorem, and requires the answers to agree. It ends by separating a consequence of the chosen field from any claim about a real system.

## The project

Use coordinates x, y in metres. The synthetic surface concentration is

\[
c(x,y)=12-(x^2+y^2)\quad\text{amount/m}^2
\]

on the disk x² + y² ≤ 4 m², with the coefficients carrying the units needed for consistency. Take a constant diffusivity D = 0.5 m²/s and the flux J = −D∇c.

1. **Model and frame.** State the coordinate frame, units, region and assumptions. Compute ∇c, identify the constrained maximum and the boundary minimum, and explain why a zero gradient alone does not establish an extremum.
2. **Total amount.** Transform the disk integral to polar coordinates, state the Jacobian and bounds, integrate c over the region, and report the units of the result.
3. **Boundary transfer.** Parameterize the positively oriented circle, identify its outward unit normal, and integrate J·n around the boundary, keeping the orientation and sign explicit.
4. **Theorem check.** Compute ∇·J and its area integral over the disk. Compare it with the boundary integral, state which smoothness and domain conditions are satisfied, and describe how changing D to 0.75 m²/s changes the predicted transfer.
5. **Figure and interpretation.** Provide a labelled contour, gradient and flux figure with a text alternative or data table. Distinguish a mathematical consequence of the chosen field from a measurement, mechanism or claim about real tissue.

## Milestones

| Milestone | Suggested week | Task | Where to check yourself |
| --- | --- | --- | --- |
| Rehearsal | 13 | Work the rehearsal field, then use the open rehearsal practice set | **Practice gradebook**: Field project rehearsal |
| M1 | 13 | Frame, gradient and extrema (task 1) | Case studio: project milestone 1 |
| M2 | 13 | The polar total (task 2) | Case studio: project milestone 2 |
| M3 | 13 | The oriented boundary integral (task 3) | Case studio: project milestone 3 |
| M4 | 14 | The divergence check and the change in D (task 4) | Case studio: project milestone 4 |
| M5 | 14 | Figure, text alternative and interpretation (task 5) | Case studio: project milestone 5 |

Each Case studio milestone lists self-review statements. Responses are saved privately in this application and are never scored.

## Rehearsal field

Before the project, work the same steps on c(x, y) = 9 − 2(x² + y²) amount/m² on the disk of radius 1.5 m, with D = 0.4 m²/s, and on a change of D to 0.6 m²/s. Then check yourself with the open rehearsal practice set, which gives feedback on each value. Its field, radius and diffusivities differ from the project's, so its answers are not the project's answers.

## Worked example: a third field

Take c(x, y) = 5 − (x² + y²) on the unit disk, with D = 1 m²/s.

1. **Extrema.** ∇c = (−2x, −2y) vanishes only at the origin, where c = 5. On the boundary c = 4. The Hessian is negative definite, and the interior value exceeds every boundary value, so the global maximum on the disk is 5 at the center and the minimum is 4 on the circle.
2. **Total.** In polar coordinates c = 5 − r² and dA = r dr dθ, so \(\int_0^{2\pi}\int_0^1 (5-r^2)\,r\,dr\,d\theta = 2\pi(5/2-1/4)\) = 4.5π ≈ 14.14 amount.
3. **Boundary transfer.** J = −D∇c = (2x, 2y). With the counterclockwise circle and outward normal n = (x, y), J·n = 2(x² + y²) = 2 on the boundary, so ∮ J·n ds = 2 × 2π = 4π ≈ 12.57 amount/s.
4. **Theorem check.** ∇·J = 2 + 2 = 4, and its integral over the disk is 4 × π = 4π, the same transfer. Both routes are valid because J is smooth on the closed disk and the boundary is a smooth closed curve oriented with its outward normal.

Doubling D would double J and the transfer, but it would not change c or its total; the diffusivity enters only through the flux.

## Construction checks for the project

The inactive draft publishes its own values as visible self-checks for an ungraded exercise. After working the project, compare: the disk has radius 2 m and area 4π m²; the maximum is 12 amount/m² at the center and the boundary value 8 amount/m²; the polar total is 40π amount; J = (x, y) amount/(m·s) with divergence 2 amount/(m²·s); both the outward boundary integral and the divergence integral equal 8π amount/s; and at D = 0.75 m²/s the transfer is 12π amount/s. Matching these shows that the calculations are consistent, not that the figure, reasoning or interpretation are complete.

## Reporting conventions

- State every coefficient's units, and report totals in amount and transfers in amount/s.
- Keep π exact until the final step, then give a decimal.
- Write the orientation and the normal explicitly in every flux calculation.
- Disclose any software, spreadsheets or AI assistance you used.

## Self-review rubric

The inactive project draft proposes seven criteria for a future human reviewer and assigns them no points. For self-review, mark each criterion 0 (little or no evidence), 1 (developing evidence) or 2 (strong evidence).

| Criterion | Evidence of a strong response |
| --- | --- |
| Model and units | Field, domain, coordinate frame, coefficients and dimensions are explicit and consistent |
| Gradient and constrained extrema | Gradient and boundary behavior are correct; the global claim is justified over the stated disk |
| Coordinate measure | Polar bounds and Jacobian are correct, and the total amount has appropriate units |
| Flux and theorem check | Direct oriented flux matches the divergence integral, with signs and theorem conditions stated |
| Sensitivity and interpretation | The diffusivity change is recomputed and conclusions stay within the synthetic model |
| Figure and communication | Axes, units, arrows and a text alternative make the geometry interpretable |
| Reproducibility | Steps, formulas and numerical checks are clear enough for another learner to reproduce |

These marks are a self-check. They are not calibrated, carry no grade and do not stand in for an instructor's judgment.

## Limitations and provenance

The fields, regions and diffusivities are synthetic mathematical constructions. Agreement between the boundary and divergence integrals shows internal consistency for the chosen field; it is not a measurement, mechanism or claim about any tissue, device or transport process. Original guide and rehearsal field: CC BY 4.0, developed with substantial AI assistance.
