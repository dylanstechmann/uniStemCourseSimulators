# Assignment 5: a reproducible dynamical-model study

**Open, ungraded implementation and reporting practice with substantial AI-assisted authoring.** Proposed placement: week 14. This packet synthesizes contracts, ODE integration, linear algebra, Monte Carlo and reporting. All states and parameters are invented. Work locally and save code, tests and a report; the browser checks selected numerical fields rather than running or evaluating your implementation.

## Define the model before choosing a solver

Consider two dimensionless compartments:

a′=−k a, b′=k a−ℓ b, a(0)=1 and b(0)=0.

Time is measured in a declared synthetic unit. Both k and ℓ have inverse-time units. Introduce a cumulative loss c′=ℓ b with c(0)=0. Then a+b+c=1 should remain constant. The state b is a downstream compartment, not an independent replicate. The model is a mathematical transfer ledger and makes no claim about biological compartments, treatments or devices.

For k≠ℓ, the exact solution is a(t)=exp(−kt), b(t)=k[exp(−kt)−exp(−ℓt)]/(ℓ−k), and c=1−a−b. Derive b using an integrating factor. For k=ℓ, derive the limit b(t)=kt exp(−kt) instead of dividing by zero. This repeated-rate limit is a mathematical test of both derivation and numerical evaluation.

## Part A: verify fixed-step methods

Implement explicit Euler and Heun for the three-state system. Use k=1, ℓ=2 and final time t=1, comparing grids h=0.1,0.05 and 0.025. Ensure the final time is represented consistently and preserve all three states in the same update. Updating b using a newly updated a while other terms use the old state implements a different method.

Compare every state with the analytical solution and report endpoint/max-grid errors. Also report minimum state values and the maximum error in a+b+c. A method can preserve the linear total and still give an inaccurate time trajectory. Explain this distinction using your tables rather than declaring a conservation check a complete validation.

Check the scalar amplification limits that constrain explicit Euler for the negative eigenvalues −k and −ℓ. At these parameter values a large stable step can still violate positivity or accuracy. Derive the relevant conditions before interpreting the plot. A visually smooth line drawn through sparse output does not establish integration accuracy.

## Part B: compare an adaptive or implicit solver

Use a documented local library solver, or implement an explicitly described adaptive pair, for the same initial-value problem. Record software version, tolerances, event settings, termination status and evaluation counts. Compare accepted solution values on a common output grid without assuming the solver's internal steps equal that grid.

Then set k=1 and ℓ=1000. Identify the fast and slow time scales and explain why explicit Euler requires a step below 0.002 for strict fast-mode absolute stability. Compare an appropriate stiff method with a nonstiff method under declared accuracy tolerances. Do not call an implicit result accurate merely because it remains finite; compare it with the known solution and refine tolerances.

The exact expression for b can suffer cancellation when k≈ℓ. Implement a stable evaluation using the analytical limit or an exponential-difference formulation such as expm1, and test continuity near equality. State the threshold or formula choice explicitly. A reference function that itself loses precision cannot reliably certify another solver.

## Part C: add parameter variation without hiding numerical bias

Let k be uniform on [0.8,1.2] and keep ℓ=2. The target is the model expectation of a(1), not the mean of a real population. Its exact value is [exp(−0.8)−exp(−1.2)]/0.4. Estimate it by Monte Carlo with documented private generator streams and report sampling standard error.

Repeat using a coarser and finer ODE evaluation inside each draw. Match the k draws intentionally across the two numerical methods so their paired difference isolates numerical effects more clearly. Report that dependence rather than treating the paired outputs as independent samples. Increasing the number of draws reduces sampling scatter but does not remove a biased integration method.

Keep uncertainty in k separate from uncertainty in whether the model structure is appropriate. A narrow Monte Carlo interval conditional on a uniform distribution does not validate that distribution or establish mechanism. If you explore a different parameter distribution, label it as a sensitivity scenario and state how the estimand changes.

## Part D: a complete evidence report

Include equations, units, parameter definitions, analytical derivation, repeated-rate limit, fixed-step refinement, solver settings, invariant/positivity checks, uncertainty design and a reproducibility manifest. Present plots with labeled axes and text alternatives. Disclose external libraries, source versions and AI assistance, distinguishing your own reasoning from tool-generated calculations.

Provide at least one intentionally failing configuration and diagnose it. Examples include an explicit step outside the fast stability interval, an in-place mixed-time update, a nonfinite rate, or a reference formula evaluated at k=ℓ without a limit. Do not conceal failed runs from the final evidence table.

## Self-review after attempting the model

At k=1, ℓ=2 and t=1, a=exp(−1)≈0.36787944 and b=exp(−1)−exp(−2)≈0.23254416, leaving c≈0.39957640. The total is one up to rounding. At k=ℓ=1, b(1)=exp(−1). These are analytical checks, not measured observations.

The stated uniform-k expectation is approximately 0.37033688. Independently evaluate the integral before using that number as a test. Your implementation should reproduce the exact values within its declared numerical tolerance and explain why the empirical Monte Carlo mean need not equal the exact expectation in a single finite run.

This original assignment is CC BY 4.0 and uses [MIT OCW 2.086 Fall 2014 syllabus](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-fall-2014/pages/syllabus/) as a link-only computational-coursework comparator. No external assignment, code or dataset was imported. Qualified scientific/code/accessibility review and measured workload remain open.
