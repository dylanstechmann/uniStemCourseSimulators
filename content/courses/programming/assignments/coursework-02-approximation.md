# Assignment 2: a numerical-calculus verification notebook

**Open, ungraded implementation practice, with substantial AI-assisted authoring.** Proposed placement: week 7 after finite differences and quadrature. Work locally in your own environment. The browser checks selected response fields; it does not inspect source code, plots or written derivations. Save a reproducible notebook or script and a report locally.

## The constructed problem

Use f(x)=exp(x) on [0,1]. Its derivative equals f and its integral is exp(1)−1. These identities supply independent analytical reference values. The function is dimensionless; if interpreting x as a normalized time, state the reference time scale before assigning physical derivative units. Do not describe the mathematical samples as experimental observations.

Implement composite trapezoids on uniform grids and central differences at x=0.5. Use step sizes h=1/4,1/8,1/16,1/32 for an initial comparison. Ensure each integration grid reaches exactly the same endpoints. The derivative stencil must use the actual declared step rather than the integration array index by accident. Keep quadrature and derivative contracts separate even if they share the same function.

## Part A: derive and implement

Derive the weighted trapezoid sum, including interval widths and half weights at the endpoints. Show why a constant function integrates to its value times the interval length. Derive the central derivative from symmetric Taylor expansions and state its smoothness assumptions. Implement each operation with explicit validation of the grid/step and finite outputs.

Use at least one additional known-answer test for each method. Trapezoids integrate a linear function exactly on any ordered grid; central differences differentiate a quadratic exactly in real arithmetic. Those tests expose weighting and denominator defects, but neither is sufficient to verify the formal order on arbitrary smooth functions. Use exp(x) for the refinement study rather than relying exclusively on exactness cases.

## Part B: measure numerical convergence

For every integration grid report the approximation, signed error, absolute error and number of function evaluations. For the derivative do the same at the fixed point x=0.5. Compute successive error ratios and an observed order log2(error_coarse/error_fine) when both errors are nonzero. Explain why second-order behavior is expected in the asymptotic regime.

Use the difference between two resolutions to form a Richardson estimate with divisor three. Compare that estimate with the known actual fine-grid error. State the sign convention before extrapolating. A match is conditional on smoothness and the leading error model; a visually flat table at machine precision does not demonstrate infinitely high order.

## Part C: introduce a controlled disturbance

Replace a function evaluation by f_tilde(x)=exp(x)+δ(x), where you choose a deterministic bounded disturbance and declare it before comparing results. For example use δ(x)=10^−5 sin(700x). Keep the reference target clear: are you differentiating f_tilde itself, or using perturbed evaluations to estimate f′? These are different tasks.

Sweep derivative steps down toward floating-point resolution and display where further refinement stops helping the chosen target. Compare the observed behavior with an Ah²+B/h envelope, but do not fit a convenient envelope and call it a proven bound. Explain which constants or disturbance properties would be needed for a justified bound. Repeat with an input scaling x=s z to show that a literal step value has no universal meaning independent of units.

## Part D: interpolation and evaluation evidence

Fit a quadratic interpolant to the separate table (0,1),(0.5,1.75),(1,3). Compute its value at x=0.25 and verify all three nodes. The interpolant is p(x)=x²+x+1, so p(0.25)=1.3125. Its integral over [0,1] is 11/6. This table is a separate constructed problem; it is not a coarse table of exp(x).

Explain why exact node agreement does not establish accuracy between nodes when the true generating function is unknown. Give one alternative function that agrees at all three nodes but differs elsewhere, for example p(x)+c x(x−0.5)(x−1). Show the product vanishes at the nodes. Extrapolation beyond [0,1] adds another domain assumption. Do not substitute regression terminology for a method that exactly interpolates the stated nodes.

## A worked separate comparison

For f(x)=x² on [0,1], two trapezoid intervals give 0.375 and four give 0.34375. The exact integral is 1/3, so the fine error is 1/96. Richardson's difference estimate gives (0.375−0.34375)/3=1/96. This identity follows from the quadratic's exact error form. Use it as an implementation test before interpreting the exponential experiment.

## Self-review and report

Your report should include formulas, input scales, unit conventions, grid definitions, known-answer tests, convergence tables and a text explanation of every plot. For exp(x), an implementation that omits endpoint half weights or uses N points as N intervals will fail the analytic comparison. A derivative that improves at moderate h can worsen at tiny h because cancellation amplifies evaluation error.

The interpolation reference above is p(0.25)=1.3125 and integral 11/6≈1.8333333; it does not supply the exponential integration results. Compute those yourself and preserve enough intermediate precision to assess convergence. State the distinction between numerical error for a chosen function and evidence that a function represents real data.

Original functions, tasks and explanation are CC BY 4.0 with disclosed AI assistance. [MIT OCW 2.086 Fall 2014 calendar](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-fall-2014/pages/calendar/) is a link-only numerical-calculus comparator; no external exercise or code was reproduced. Workload and qualified review remain unmeasured/open.
