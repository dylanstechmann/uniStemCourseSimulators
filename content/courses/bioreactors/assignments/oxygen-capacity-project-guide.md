# Oxygen project guide: transfer capacity against a growing demand (optional, ungraded)

**Status:** open, optional and ungraded. Five milestone self-checks in the Case studio save responses privately; nothing is submitted, collected or scored. The separate inactive project draft and its proposed review rubric remain unreviewed and are not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 3–5 hours across weeks 8 and 9.
**Prerequisite lessons:** [Oxygen transfer and consumption](../modules/02-oxygen-transfer-and-consumption.md), [Writing a cell-culture mass balance](../modules/06-cell-culture-mass-balance.md), [Controlling dissolved oxygen](../modules/11-dissolved-oxygen-control-and-the-capacity-limit.md) and [Virtual lab 1: measuring kLa by dynamic gassing-out](../labs/01-measuring-kla-by-dynamic-gassing-out.md).

## Purpose

The dissolved-oxygen lesson compares a vessel's transfer capacity with a culture's demand at one moment. This project follows the comparison through time. Demand grows exponentially, transfer depends on how far the dissolved oxygen sits below saturation, and the oxygen already in the liquid takes time to run down. The project separates two questions that are easy to confuse: when demand first equals what transfer could supply at the threshold, and when the dissolved oxygen actually reaches that threshold.

## The project

All quantities are normalized and synthetic; this is a mathematical exercise, not a vessel design, operating procedure or control specification. Let C(t) be a dissolved-oxygen index with saturation C* = 1 and initial value C(0) = 1. The transfer coefficient is k = 0.8 per time unit, and the demand starts at OUR₀ = 0.1 and grows as OUR(t) = OUR₀ e^(μt) with μ = 0.2 per time unit:

\[
\frac{dC}{dt}=k\,(C^*-C)-OUR_0\,e^{\mu t}.
\]

The threshold for the exercise is Ccrit = 0.4.

1. Define the oxygen deficit D = C* − C and derive its differential equation and initial condition.
2. Solve the linear equation for D(t) with an integrating factor. Verify the result at t = 0 and by substitution.
3. Compute the initial transfer-minus-demand margin at Ccrit, then find when an instantaneous quasi-steady capacity check would first predict demand equal to transfer at that threshold.
4. Find the time at which the transient state first reaches Ccrit. Show that D(t) is strictly increasing, bracket the crossing, and calculate it numerically to three decimals.
5. Compare the quasi-steady time with the transient crossing time. Evaluate C at the quasi-steady time and explain why stored dissolved oxygen delays the crossing in this model.
6. State where the model should stop being interpreted, and list the evidence that would be required before applying a balance like this to a real process. Do not invent operating conditions or safety advice.

## Milestones

| Milestone | Suggested week | Task | Where to check yourself |
| --- | --- | --- | --- |
| Rehearsal | 8 | Work the rehearsal model, then use the open rehearsal practice set | **Practice gradebook**: Oxygen project rehearsal |
| M1 | 8 | Deficit equation and its solution (tasks 1–2) | Case studio: project milestone 1 |
| M2 | 8 | Threshold capacity and the quasi-steady time (task 3) | Case studio: project milestone 2 |
| M3 | 8 | Monotonicity and the transient crossing (task 4) | Case studio: project milestone 3 |
| M4 | 9 | Comparing the two times (task 5) | Case studio: project milestone 4 |
| M5 | 9 | Where the model stops and what evidence is missing (task 6) | Case studio: project milestone 5 |

Each Case studio milestone lists self-review statements. Responses are saved privately in this application and are never scored.

## Rehearsal model

Before the project, work the same steps on a second normalized model, then check yourself with the open rehearsal practice set, which gives feedback on each value. The rehearsal uses k = 0.5, OUR₀ = 0.08, μ = 0.25 and Ccrit = 0.5, again with C* = 1 and C(0) = 1. Its parameters differ from the project's, so its answers are not the project's answers.

## Worked example: a third model

Take k = 1.0, OUR₀ = 0.2, μ = 0.5 and Ccrit = 0.5, with C* = 1 and C(0) = 1.

1. **Deficit.** With D = 1 − C, the balance becomes D′ + kD = OUR₀ e^(μt), and D(0) = 0 because the liquid starts saturated.
2. **Solution.** Multiplying by the integrating factor e^(kt) and integrating from 0 gives

   \[
   D(t)=\frac{OUR_0}{k+\mu}\left(e^{\mu t}-e^{-kt}\right)=\frac{0.2}{1.5}\left(e^{0.5t}-e^{-t}\right).
   \]

   At t = 0 the bracket is 1 − 1 = 0, as required.
3. **Capacity check.** At the threshold, transfer can supply k(C* − Ccrit) = 1.0 × 0.5 = 0.5, against an initial demand of 0.2, a margin of 0.3. Demand reaches 0.5 when 0.2 e^(0.5t) = 0.5, at t = ln(2.5)/0.5 ≈ 1.833.
4. **Transient crossing.** D′ = (0.2/1.5)(0.5 e^(0.5t) + e^(−t)) is always positive, so D rises and crosses 0.5 once. D(2) ≈ 0.344 and D(3) ≈ 0.591 bracket the crossing, and bisection gives t ≈ 2.680.
5. **Comparison.** At t ≈ 1.833, C ≈ 0.688, well above the threshold. Demand has already caught up with threshold capacity, but the oxygen stored in the liquid takes time to be drawn down, so the state crosses about 0.85 time units later.

After the first crossing the model keeps falling, and C would eventually become negative, which has no physical meaning. Interpretation stops at the first crossing.

## Reporting conventions

- Keep the deficit's sign convention fixed and state it once.
- Keep at least four significant figures in intermediate values; report crossing times to three decimals, as the project asks.
- Report the bracket you used and how you narrowed it, not only the final time.
- Disclose any software, spreadsheets or AI assistance you used.

## Self-review rubric

The inactive project draft proposes five criteria for a future human reviewer and assigns them no points. For self-review, mark each criterion 0 (absent), 1 (partly correct) or 2 (complete and consistent with the stated model).

| Criterion | Evidence of a complete response |
| --- | --- |
| Balance | Defines the deficit with a consistent sign and obtains the correct linear equation |
| Solution | Applies the integrating factor and verifies the initial condition |
| Capacity | Distinguishes threshold transfer capacity from instantaneous demand |
| Transient crossing | Shows monotonicity, brackets the root and reports a checked approximation |
| Limits | Separates the normalized model from real process or safety claims |

These marks are a self-check. They are not calibrated, carry no grade and do not stand in for an instructor's judgment.

## Limitations and provenance

All parameters are normalized teaching values. The model has one well-mixed liquid, a constant transfer coefficient, no probe dynamics, no control action and demand that grows without limit, and it says nothing about any real vessel, culture or control system. Original guide and rehearsal values: CC BY 4.0, developed with substantial AI assistance.
