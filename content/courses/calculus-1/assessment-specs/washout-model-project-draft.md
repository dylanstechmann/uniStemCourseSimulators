# Washout model portfolio: inactive project draft

**Status:** authoring draft only. It is not scheduled, assigned, submitted, collected or graded, and it is not a protected assessment. All signals and model parameters are constructed. They establish no real clearance estimate, biological mechanism, dosing guidance, device specification or experimental protocol.

## Purpose and outcomes

This paper-only portfolio connects derivatives, monotonicity, Newton's method, the Fundamental Theorem of Calculus, numerical quadrature and sensitivity to an assumed background. The synthetic model deliberately differs from the single-rate signal in the existing virtual lab so learners can examine a known changing slope without claiming that a multi-exponential model is identifiable from real observations.

## Model and observations

For `0 ≤ t ≤ 24` hours, let the constructed corrected signal be

\[
S(t)=18e^{-0.08t}+6e^{-0.015t},\qquad Y(t)=S(t)+3,
\]

where the exact known blank is 3 signal units. The seven values in [washout-capstone-signals.csv](washout-capstone-signals.csv) are `Y(t)` rounded to six decimals; the CSV is a plotting/checking dataset, while the formula defines the continuous model. The two exponentials are mathematical components of a synthetic example, not evidence for two real compartments.

## Work sequence

1. Derive `S′(t)` and `S″(t)`. Find the initial rate of change, show that `S` decreases on the interval, and use the sign of `S″` to identify where the magnitude of the decline is largest.
2. Find when the corrected signal first reaches 8 units. Establish that there is a unique root on `[20,24]`, then apply Newton's method to `f(t)=S(t)−8` starting at `t₀=20 h`. Report at least two iterations and substitute the final estimate back into `f`.
3. Evaluate the exact cumulative corrected signal `∫₀²⁴ S(t) dt` and its average over the interval, with units. State how integrating `Y` instead changes the result.
4. Using only the seven equally spaced CSV values, compute composite Simpson's rule with `h=4 h`. Compare it with the exact integral by absolute and relative error. Explain why the approximation does not establish the accuracy of the model itself.
5. If an analyst subtracts a blank of 3.05 instead of the stipulated 3.00, calculate the change in the 24-hour corrected integral and explain which assumption created the difference.
6. Write a short limitations note distinguishing the exact arithmetic in this constructed example from model selection or interpretation for a real dataset.

## Author calculation key

\[
S′(t)=-1.44e^{-0.08t}-0.09e^{-0.015t},\qquad
S″(t)=0.1152e^{-0.08t}+0.00135e^{-0.015t}>0.
\]

Thus `S′<0` and increases toward zero: the signal decreases throughout, and its steepest decline on `[0,24]` occurs at `t=0`, where `S′(0)=−1.53` signal units/hour. At the target, `f(20)=0.079046648` and `f′(20)=−0.357404626`; the first Newton estimate is `t₁=20.221169 h`, and the second is `t₂=20.222844 h`, where `|f(t₂)|<4×10⁻⁸`. Since `S′<0`, the crossing on `[20,24]` is unique.

The exact integral is

\[
\int_0^{24}S(t)\,dt=\frac{18}{0.08}(1-e^{-1.92})+\frac{6}{0.015}(1-e^{-0.36})=312.942903\text{ signal·hours},
\]

and its average is `13.039288` signal units. Integrating the uncorrected `Y` adds `3×24=72` signal·hours, giving `384.942903`. Composite Simpson's rule on the rounded CSV values gives `312.953964` signal·hours; absolute error is `0.011061` and relative error is approximately `0.00353%`. Subtracting 3.05 instead of 3.00 reduces the 24-hour corrected integral by `0.05×24=1.2` signal·hours.

## Proposed unweighted review rubric

| Criterion | Evidence for future human review |
|---|---|
| Derivatives | Correct rates, signs, units and monotonicity/curvature reasoning |
| Root finding | Justified interval, Newton updates and a residual check |
| Accumulation | Exact antiderivative, average value and blank contribution |
| Numerical error | Correct six-panel Simpson calculation and comparison with the exact integral |
| Assumptions | Separates quadrature error from model error and limits interpretation to constructed data |

The rubric is unweighted and has no automatic prose grader. Workload, accessibility, mathematical accuracy and instructional design require qualified review. Do not activate this draft or describe it as a course assessment until those reviews and the course's missing homework, laboratory and exam components are addressed.

## Provenance

Original authoring and synthetic values, CC BY 4.0, developed with substantial AI assistance. No third-party dataset or real-world procedure is included.
