# Tail project guide: certifying a finite approximation to an infinite total (optional, ungraded)

**Status:** open, optional and ungraded. Five milestone self-checks in the Case studio save responses privately; nothing is submitted, collected or scored. The separate inactive project draft and its proposed review rubric remain unreviewed and are not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 2–4 hours across weeks 13 and 14.
**Prerequisite lessons:** [Improper integrals, singularities and comparison](../modules/08-improper-integrals-and-comparison.md), [Taylor approximations with an error bound](../modules/06-taylor-approximations-and-error-bounds.md), [Alternating series and error certificates](../modules/10-alternating-series-and-error-certificates.md) and [Taylor polynomials and integrated error](../modules/12-taylor-polynomials-and-integrated-error.md).

## Purpose

An infinite accumulation can often be computed only approximately: cut it off at a finite point, approximate the remaining piece, and say how large the error can be. This project builds such a certificate for one exact function. It joins the limit definition of an improper integral, a tolerance on the omitted tail, a Taylor approximation, and an integrated Lagrange remainder bound, and it ends by separating approximation error from model error.

## The project

Let x ≥ 0 be a dimensionless coordinate and q(x) = e^(−x), an exact teaching model with no biological, mechanical or experimental interpretation. On [0, 1], use the degree-four Maclaurin polynomial

\[
P_4(x)=1-x+\frac{x^2}{2}-\frac{x^3}{6}+\frac{x^4}{24}.
\]

1. Evaluate Q = ∫₀^∞ q(x) dx from the limit definition of the improper integral, and explain why the limit is finite.
2. Find the omitted tail after a cutoff T. Calculate it at T = 3, then find the smallest cutoff for which the tail is at most 0.01.
3. Integrate P₄ exactly on [0, 1].
4. Use the Lagrange remainder for e^(−x) to bound the absolute error in ∫₀¹ P₄(x) dx. Compare the bound with the actual error obtained from the exact integral.
5. Combine the degree-four approximation over [0, 1] with the exact tail over [1, ∞). Report the resulting approximation to Q, its signed error and the separate sources of error.
6. Explain why a small Taylor remainder certifies approximation to the stipulated function but does not validate that function as a model for any external system.

## Milestones

| Milestone | Suggested week | Task | Where to check yourself |
| --- | --- | --- | --- |
| Rehearsal | 13 | Work the rehearsal function, then use the open rehearsal practice set | **Practice gradebook**: Tail project rehearsal |
| M1 | 13 | The improper integral and the tail tolerance (tasks 1–2) | Case studio: project milestone 1 |
| M2 | 13 | The integrated Taylor polynomial (task 3) | Case studio: project milestone 2 |
| M3 | 13 | The Lagrange certificate (task 4) | Case studio: project milestone 3 |
| M4 | 14 | The combined approximation and its error (task 5) | Case studio: project milestone 4 |
| M5 | 14 | Approximation error versus model error (task 6) | Case studio: project milestone 5 |

Each Case studio milestone lists self-review statements. Responses are saved privately in this application and are never scored.

## Rehearsal function

Before the project, work the same steps on q(x) = e^(−x/2) with the degree-three polynomial P₃(x) = 1 − x/2 + x²/8 − x³/48 on [0, 1], a tail evaluated at T = 4, and the same 0.01 tolerance. Then check yourself with the open rehearsal practice set, which gives feedback on each value. Its function, polynomial degree and cutoff differ from the project's, so its answers are not the project's answers.

## Worked example: a third function

Take q(x) = e^(−2x), the degree-two polynomial P₂(x) = 1 − 2x + 2x² on [0, 0.5], and a tail tolerance of 0.001.

1. **Improper integral.** ∫₀^b e^(−2x) dx = (1 − e^(−2b))/2, which tends to 1/2 as b → ∞ because e^(−2b) → 0.
2. **Tail.** The tail after T is e^(−2T)/2. It is at most 0.001 when e^(−2T) ≤ 0.002, that is T ≥ ln(500)/2 ≈ 3.107. The tail shrinks as T grows, so every larger cutoff works too.
3. **Taylor integral.** ∫₀^0.5 P₂ dx = 0.5 − 0.25 + (2/3)(0.125) ≈ 0.3333, against the exact (1 − e^(−1))/2 ≈ 0.3161: the polynomial is too large by about 0.0173.
4. **Certificate.** The third derivative is −8e^(−2ξ), so |q‴(ξ)| ≤ 8 on [0, 0.5] and |R₃(x)| ≤ 8x³/6. Integrating gives at most (4/3)(0.5⁴/4) ≈ 0.0208, and the actual error, about 0.0173, sits below it.
5. **Combination.** Adding the exact tail beyond 0.5, e^(−1)/2 ≈ 0.1839, gives ≈ 0.5173 for a total of 0.5. All of the error comes from the truncated piece on [0, 0.5], because the tail was computed exactly.

A tighter certificate needs a higher degree or a shorter interval. Neither one says anything about whether e^(−2x) describes a real process; the bound concerns only how closely the polynomial follows the function it was built from.

## Reporting conventions

- Write each improper integral as a limit of a finite integral before evaluating it.
- Keep exact fractions where the polynomial integral gives them, and report decimals to sensible precision.
- State the interval on which every derivative bound holds, and report signed errors with their sign.
- Disclose any software, spreadsheets or AI assistance you used.

## Self-review rubric

The inactive project draft proposes five criteria for a future human reviewer and assigns them no points. For self-review, mark each criterion 0 (absent), 1 (partly correct) or 2 (complete and consistent with the stated model).

| Criterion | Evidence of a complete response |
| --- | --- |
| Improper integral | Uses the limiting definition and states the convergence result |
| Tail requirement | Derives the tail and solves the tolerance inequality with the correct direction |
| Taylor approximation | Integrates all polynomial terms correctly |
| Error certificate | Uses an interval-valid derivative bound and integrates it |
| Interpretation | Separates approximation to the stipulated formula from validation of an external model |

These marks are a self-check. They are not calibrated, carry no grade and do not stand in for an instructor's judgment.

## Limitations and provenance

The functions are exact mathematical teaching models with no physical, biological or experimental meaning. Remainder bounds hold only on the intervals where their derivative bounds were derived, and they control approximation error, not measurement uncertainty or model discrepancy. Original guide and rehearsal function: CC BY 4.0, developed with substantial AI assistance.
