# Assignment 4: feedback dynamics, bounds and reserve

Develop an analytic and computational report using [two-state water feedback](../modules/delayed-feedback-and-water-balance.md), [homeostasis/gain](../modules/08-homeostasis-balance-and-feedback-gain.md) and [compensation/reserve](../modules/14-compensation-and-reserve.md). Keep equations, source or calculation tables, checks and interpretation locally. Browser checkpoints assess selected values and choices, not your simulation or report. All variables are normalized deviations and all coefficients invented; no result is a hormone level, fluid recommendation or health assessment.

## Define the unbounded model

Use tauW wdot=u−w+g h and tauH hdot=−h−k w. Set tauW=2, tauH=1 in arbitrary time units, g=1, k=2, and switch u from zero to 0.3 at time zero with w(0)=h(0)=0. Define the positive signs and distinguish the water-pool deviation w, control-signal deviation h, input disturbance u and their absolute reference quantities. Negative h is allowed as a below-reference signal; it does not mean negative absolute hormone concentration.

Derive steady state, initial derivatives and the homogeneous characteristic equation after subtracting equilibrium. Compute the modal roots and state why their real parts determine asymptotic stability in this finite linear model. Distinguish oscillatory modes from the actual peak of one state or output. Derive an exact solution, use a matrix exponential, or construct an independently verified reference by another appropriate method; do not treat a smooth numerical graph as the reference itself.

Integrate the response at several step sizes and compare w, h and state-equation residuals at matching times. State the time interval and error measure. Check a zero-disturbance case, a no-feedback case and scaling of the linear response with disturbance amplitude. Determine whether either signal overshoots its final value and distinguish a finite transient from an unstable long-time trajectory. General solver design is taught in Programming; here the declared balance and modal solution supply checks.

## Add a bounded controller target

Replace the target −kw by clip(−kw,−0.1,+0.4) before applying the first-order controller relaxation: tauH hdot=clip(−kw,−0.1,+0.4)−h. The water equation remains unchanged. Explain why this is a different model from merely clipping h after a numerical step. If h starts inside the interval, examine the derivative at each boundary to check that the continuous target law keeps it inside.

First test whether the unbounded equilibrium lies within the allowed target range. If it does not, solve the appropriate saturated branch and verify its clipping inequality. Compare the new final water deviation and control effort with the unbounded result. State how exhausted control range can enlarge an offset while nominal small-signal gains remain the same. This is a reserve concept within a normalized model, not an inferred failure of any person's endocrine system.

Simulate the bounded response with event or branch handling appropriate to the continuous piecewise law. Track the requested target, clipped target and actual h separately. Compare a step-size refinement study and verify the state remains admissible. A post-step correction can hide an inconsistent trajectory, so retain the original differential equations and branch conditions as verification evidence.

## Sensor bias and inference

For a separate unbounded comparison, let the sensor read w+b with b=0.05, so the target is −k(w+b). Derive the new equilibrium and compare the sensed value, actual water deviation and control effort. Explain why a single observed output does not uniquely identify sensor bias, gain, disturbance and effector limit. Propose a controlled comparison with at least two endpoints that would separate two candidate explanations, stating contrasting predicted outcomes.

Discuss which conclusions would change with an explicit time delay, nonlinear transport, variable solute amount or another interacting organ loop. The positive-parameter stability proof for these two states is not a guarantee about every real negative-feedback system. Identify evidence needed to calibrate a physiological interpretation, including baseline/scales, time courses, manipulated inputs and independent observations of effector action.

## Self-review after independent work

The unbounded equilibrium is w=0.1 and h=−0.2. Initial wdot is 0.15 per time unit and initial hdot zero. Modal roots are −0.75 plus or minus i sqrt(15)/4. Those values allow a stable oscillatory approach; the actual transient must satisfy the initial state and input equation.

The minimum target −0.1 excludes the unbounded equilibrium. The lower-saturated branch has h=−0.1 and w=0.2, requesting −kw=−0.4, so its clipping condition holds. With the separate sensor bias and no clipping, w=(0.3−2×0.05)/3=1/15 and h=−7/30. Keep the bounded and biased comparisons separate rather than mixing their assumptions.

A complete report retains balance/normalization, analytic or independently checked reference, initial/final/modal evidence, numerical refinement, clipping invariance/branch checks and an identifiable comparison plan. This original AI-assisted coursework uses [MIT OCW HST.542J Organ Transport Systems Spring 2004](https://ocw.mit.edu/courses/hst-542j-quantitative-physiology-organ-transport-systems-spring-2004/pages/calendar/) as a link-only scope comparator and imports no source problem, code or physiological response data. Actual learner workload and qualified physiological review remain open; the package remains partial and unreviewed.
