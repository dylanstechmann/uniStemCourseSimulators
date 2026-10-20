# Washout model project guide: rates, roots, accumulation and quadrature error (optional, ungraded)

**Status:** open, optional and ungraded. Five milestone self-checks in the Case studio save responses privately; nothing is submitted, collected or scored. The separate inactive project draft and its proposed review rubric remain unreviewed and are not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 4–6 hours across weeks 12–14.
**Prerequisite lessons:** [Derivative rules and chain rule](../modules/02-derivative-rules-and-chain-rule.md), [Curve shape, critical points and constrained optimization](../modules/09-shape-analysis-and-constrained-optimization.md), [Rolle's Theorem, the Mean Value Theorem and consequences](../modules/14-rolle-mean-value-theorem-and-consequences.md), [Local approximations, Newton steps and sensitivity](../modules/12-local-approximations-newton-and-sensitivity.md), [Definite integrals and the fundamental theorem](../modules/04-definite-integrals-and-the-fundamental-theorem.md), [Accumulation, the fundamental theorem and substitution](../modules/10-accumulation-ftc-and-substitution.md) and [Numerical derivatives, quadrature and error budgets](../modules/11-numerical-derivatives-integrals-and-error.md).
**Data:** the [project signal table](../assessment-specs/washout-capstone-signals.csv) and the [rehearsal signal table](washout-rehearsal-signals.csv).

## Purpose

The project follows one constructed washout signal through the main tools of the course: derivatives and their signs, a root found by Newton's method and justified by monotonicity, an exact integral and its average, a numerical integral from sampled values, and the effect of a wrong background. Each step answers a different question about the same function, and the last step separates what exact arithmetic can show from what it cannot say about real measurements.

## The project

For 0 ≤ t ≤ 24 hours, the constructed corrected signal is

S(t) = 18e^(−0.08t) + 6e^(−0.015t), and the observed signal is Y(t) = S(t) + 3,

where the blank of 3 signal units is known exactly. The project table lists Y at t = 0, 4, 8, …, 24 hours, rounded to six decimals; the formula, not the table, defines the continuous model. The two exponential terms are mathematical components of a synthetic example, not evidence for two real compartments.

1. Derive S′(t) and S″(t). Find the initial rate of change, show that S decreases on the interval, and use the sign of S″ to identify where the decline is steepest.
2. Find when the corrected signal first reaches 8 units. Establish that there is a unique root on [20, 24], then apply Newton's method to f(t) = S(t) − 8 starting at t₀ = 20 h. Report at least two iterations and substitute the final estimate back into f.
3. Evaluate the exact cumulative corrected signal, the integral of S from 0 to 24 h, and its average over the interval, with units. State how integrating Y instead changes the result.
4. Using only the seven equally spaced table values, compute composite Simpson's rule with h = 4 h. Compare it with the exact integral by absolute and relative error, and explain why the approximation does not establish the accuracy of the model itself.
5. If an analyst subtracts a blank of 3.05 instead of 3.00, calculate the change in the 24-hour corrected integral and explain which assumption created the difference.
6. Write a short limitations note distinguishing the exact arithmetic in this constructed example from model selection or interpretation for a real dataset.

## Milestones

| Milestone | Suggested week | Task | Where to check yourself |
| --- | --- | --- | --- |
| Rehearsal | 12 | Work the rehearsal signal, then use the open rehearsal practice set | **Practice gradebook**: Washout project rehearsal |
| M1 | 12 | Derivatives, monotonicity and curvature (task 1) | Case studio: project milestone 1 |
| M2 | 12 | The root on [20, 24] and Newton's method (task 2) | Case studio: project milestone 2 |
| M3 | 13 | Exact integral, average and the blank's contribution (task 3) | Case studio: project milestone 3 |
| M4 | 13 | Simpson's rule and its error (task 4) | Case studio: project milestone 4 |
| M5 | 14 | Blank sensitivity and the limitations note (tasks 5–6) | Case studio: project milestone 5 |

Each Case studio milestone lists self-review statements. Responses are saved privately in this application and are never scored. The rehearsal uses a different two-term signal, blank, target and step size, so its answers are not the project's answers.

## Worked example: a one-term washout

The virtual lab's teaching signal, C(t) = 20e^(−0.1t) with a blank of 2, shows each step with numbers that can be checked in closed form.

1. **Derivatives.** C′(t) = −2e^(−0.1t) < 0 and C″(t) = 0.2e^(−0.1t) > 0, so C decreases throughout and falls fastest at the start. At 10 hours it falls at C′(10) = −2e^(−1) ≈ −0.736 units per hour.
2. **A root and Newton's method.** C reaches 4 exactly at t = 10 ln 5 ≈ 16.0944 h. Newton's method on f(t) = C(t) − 4 from t₀ = 15 h gives t₁ = 15 − 0.462603/(−0.446260) ≈ 16.0366 and t₂ ≈ 16.0942, with residual f(t₂) ≈ 0.00007. The sign change on [15, 20] gives a root, and C′ < 0 makes it unique; for the two-term project signal no closed form exists, so that argument is what justifies trusting the iteration.
3. **Accumulation.** The integral of C from 0 to 20 h is 200(1 − e^(−2)) ≈ 172.933 signal·hours, an average of 8.647 signal units. Integrating the uncorrected signal adds 2 × 20 = 40.
4. **Quadrature.** Simpson's rule with h = 5 h on the values at 0, 5, 10, 15 and 20 h gives (5/3)[20 + 4(12.1306) + 2(7.3576) + 4(4.4626) + 2.7067] ≈ 172.991, about 0.058 above the exact value, as in the numerical-calculus lesson.
5. **Background.** Subtracting 2.05 instead of 2 lowers every corrected value by 0.05, so the 20-hour integral falls by 0.05 × 20 = 1.0 signal·hours. The calculus is exact; the change comes entirely from the blank assumption.

## Reporting conventions

- Keep units on every quantity: signal units, hours, signal units per hour and signal·hours.
- Keep at least six significant figures in intermediate values and round only the reported result.
- Separate exact model values, numerical approximations and interpretations.
- Disclose any software, spreadsheets or AI assistance you used.

## Self-review rubric

The inactive project draft proposes five criteria for a future human reviewer and assigns them no points. For self-review, mark each criterion 0 (absent), 1 (partly correct) or 2 (complete and consistent with the stated model).

| Criterion | Evidence of a complete response |
| --- | --- |
| Derivatives | Correct rates, signs, units and monotonicity and curvature reasoning |
| Root finding | Justified interval, Newton updates and a residual check |
| Accumulation | Exact antiderivative, average value and blank contribution |
| Numerical error | Correct six-panel Simpson calculation and comparison with the exact integral |
| Assumptions | Separates quadrature error from model error and limits interpretation to constructed data |

These marks are a self-check. They are not calibrated, carry no grade and do not stand in for an instructor's judgment.

## Limitations and provenance

All signals, blanks and parameters are constructed. Exact arithmetic on a known model is not model selection: real washout data would need a choice among models, uncertainty in the blank and in each observation, and independent validation. Nothing here establishes a real clearance estimate, a biological mechanism, dosing guidance, a device specification or an experimental protocol. Original guide and synthetic rehearsal data: CC BY 4.0.
