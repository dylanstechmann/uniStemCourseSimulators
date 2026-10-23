# Assignment 1: methods, domains and initial-value evidence

This is an open, ungraded mathematical report connecting the first-order, numerical and new variable-coefficient readings. Its purpose is to make a solution claim reviewable: an expression, a graph and a solver-success message are different forms of evidence. All equations and parameters are synthetic and normalized. Retain your derivations, code and report locally. The browser checks selected numbers and interpretations; it cannot evaluate the completeness of your argument.

## Deliverable and notation

Prepare a report with an equation/initial-value/domain table, analytic calculations, a numerical comparison and a counterexample analysis. State the interval of every claim. Use a different symbol for a time step and for the dependent state. If your software estimates derivatives or residuals on a grid, identify the grid and distinguish that sampled test from an identity derived analytically. No fixed study-hour estimate or completion grade is assigned.

## Part A: a distinct variable-coefficient IVP

Solve

$$y'+2t y=2t,\qquad y(0)=3.$$

Derive an integrating factor from its defining differential equation and normalize it at zero. Integrate the resulting product derivative, impose the initial value and simplify. Then differentiate your expression and reconstruct the original equation. Identify whether the coefficients impose a finite singular boundary. Explain why a single constant time constant does not describe this relaxation over the entire real line.

The analytic comparison gives $y=1+2e^{-t^2}$ and $y'=-4t e^{-t^2}$. At $t=1$, $y=1+2/e\approx1.73576$. The factor at that time is $e$, while the constant equilibrium particular solution is one. The initial derivative is zero even though the state differs from the particular solution: the coefficient $2t$ itself vanishes at the initial time. A constant-rate decay formula would miss that behavior.

Implement an explicit integrator and compare at $t=1$ with decreasing steps that land exactly at the target time. Report signed and absolute errors. Estimate an observed order only where errors are not dominated by roundoff, and retain the method definition with your results. Reverse-time integration is a separate stability question; a formula existing for negative time does not make every forward or backward numerical method well conditioned.

## Part B: local uniqueness does not promise global boundedness

Consider the separate IVP

$$z'=z^2,\qquad z(0)=2.$$

Derive $z=2/(1-2t)$ and find the maximal connected interval containing zero. It ends at $t=1/2$; $z(1/4)=4$. The vector field is smooth everywhere in finite $(t,z)$, yet the solution escapes to infinity in finite forward time. Explain which theorem statement is local and why smoothness alone does not supply an infinite-time bounded trajectory.

A formula evaluated for $t>1/2$ gives negative values but does not continue this initial-value solution through its singularity. Demonstrate the distinction between an algebraic expression's disconnected domain and an IVP trajectory's connected interval. If an adaptive solver stops before the singularity, record its termination condition and compare increasing values with the analytic solution. Do not treat a tiny accepted step as evidence that the solution crosses the escape time.

## Part C: prove nonuniqueness with actual solutions

For a third problem use

$$v'=3\sqrt{|v|},\qquad v(0)=0.$$

Construct a forward family that remains zero until any chosen $a\geq0$ and then equals $\tfrac94(t-a)^2$. Verify the equation on each open piece, continuity at the join, and equality of the one-sided first derivatives there. The zero solution is another member of the solution set. State precisely how this differs from merely failing a sufficient local-Lipschitz hypothesis.

Use $a=1$ as a check: at $t=2$, $v=9/4$ and $v'=9/2$. Compare this branch with the identically zero branch at the same time. A solver initialized exactly at zero may stay there; that output is valid and does not rule out the delayed branches. Perturbing the initial value changes the IVP and should be labeled as a different problem.

## Part D: method selection and lost equilibria

For each of the three equations, identify whether separation, a linear integrating factor or both are applicable. List any states lost by dividing by the dependent variable or a function of it. Substitute those states into the original equation. Explain why superposition applies to differences of solutions of the linear equation but not arbitrary sums of solutions of the nonlinear examples.

Include one intentionally wrong candidate and reject it through the original residual or initial condition. A wrong candidate that happens to match one sampled value is a useful demonstration of why one checkpoint cannot replace a derivation. Separate mathematical existence, numerical approximation, and suitability as a model of a real system; this assignment establishes only the first two within its stated examples.

## Self-review and scope

Your retained report should contain the integrating-factor derivation, the exact residual identity, numerical refinement evidence, the finite escape/domain argument and the explicit nonunique family. The relevant [18.03SC Fall 2011 syllabus](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/syllabus/syllabus/) and [Unit I](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-i-first-order-differential-equations/) are link-only comparators for method choice and plausibility checks. Problems and solutions here are original with substantial AI assistance. General existence proofs, singular boundary-value theory and qualified mathematical review remain open. This report does not establish university credit, measured workload or a complete course.
