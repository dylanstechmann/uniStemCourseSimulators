# Assignment 3: powers, exponentials and transient behavior

Build a proof-and-simulation study using [defective matrices and transients](../modules/defective-matrices-and-transient-dynamics.md), [linear dynamics](../modules/03-eigenvalues-and-linear-dynamical-systems.md) and [coordinate metrics](../modules/factorizations-maps-and-coordinates.md). Save exact derivations, any implementation, refinement evidence and interpretation locally. Browser checkpoints assess selected numbers and choices; they do not evaluate proofs, code, graphs or a real dynamical model. All states and coefficients are dimensionless teaching values unless a time scale is explicitly chosen.

## Discrete dynamics without a full eigenvector basis

Let J have rows (0.6,1.5) and (0,0.6), with x0=(0,1). Compute the characteristic polynomial and a basis for each eigenspace. Explain why a repeated eigenvalue does not supply the two independent columns needed for diagonalization. Write J as lambda I+N and verify N squared is zero. Derive an exact expression for J to the nth power for positive integers n, keeping the n=0 initial state separate.

Calculate states at n=1,2,5 and 20 using both the formula and repeated matrix multiplication. Compare each Euclidean norm with the initial norm and with lambda to the nth power. Explain why the scalar eigenvalue factor alone misses the coupling. Prove both components tend to zero despite any initial amplification. A finite plot cannot by itself establish an infinite-time limit; use a geometric-versus-polynomial argument with its assumptions stated.

Find the step giving the largest first component by comparing successive positive terms, not by treating the integer step as a continuous variable without checking neighboring integers. Then find or bound the largest vector norm separately. Explain why the maximizing step for one coordinate need not maximize the chosen norm or every linear observable. State exactly what quantity each reported maximum concerns.

## A continuous contrast

Let A have rows (−2,3) and (0,−2), again starting from x0=(0,1). Derive exp(At) by the nilpotent series and independently solve the two scalar differential equations in sequence. Verify the initial state and derivative equation. Evaluate the state at t=0.5 and find the first coordinate's peak time and amplitude. Keep the full vector norm distinct from that coordinate.

Compute the symmetric part H=(A+A transpose)/2 and its eigenvalues. Derive d||x||²/dt=2x transpose Hx. Use the largest eigenvalue of H to prove the Euclidean norm strictly decreases for every nonzero state in this example. Contrast this with the reading's A having rows (−1,4),(0,−1), whose state from the same initial vector has norm above one at t=1. Both matrices are defective; defectiveness or non-normality alone is not a guarantee of norm growth.

Derive an exponential norm bound for the monotone example from the quadratic inequality. Explain how that bound differs from the exact first-coordinate maximum. A conservative envelope need not be attained. If you use a numerical ODE solver, compare at least three step sizes with the exact component solution and retain both state and norm-law errors. General numerical-solver implementation belongs to Programming; here the analytic matrix structure supplies the reference.

## Coordinate changes and model meaning

Choose an invertible nonorthogonal S and transform one of the systems to new coordinates. Verify similarity preserves its eigenvalues. Compare ordinary coordinate Euclidean norms before and after transformation, then carry G=S transpose S so both descriptions evaluate the same physical norm. Explain why an apparent change in amplification can be caused by changing the norm rather than changing the underlying evolution.

Give an example of a linear observable c transpose x whose transient differs from the full norm. Discuss the extra constraints needed if state entries were interpreted as nonnegative populations or physical quantities with different units. Eigenvalue stability alone does not establish those constraints or justify a physical interpretation. No biological population, controller or device is modeled by the supplied matrices.

## Self-review after independent work

The discrete state is [1.5n(0.6)^(n−1),(0.6)^n] for n≥1. At n=2 it is (1.8,0.36); at n=5 it is (0.972,0.07776). The only eigenvalue is 0.6, with a one-dimensional eigenspace. The first step already increases the norm above one, yet the long-time state is zero. Verify both claims with the exact expression.

For the continuous contrast, the state is exp(−2t)(3t,1). At t=0.5 it is (1.5/e,1/e), and the first coordinate peaks there. H has eigenvalues −0.5 and −3.5, so d||x||²/dt≤−||x||². The norm therefore decreases even though one component starts at zero and initially increases. Components and total norms answer different questions.

A complete study contains eigenspace dimension, exact powers/exponentials, independent recurrence/component checks, asymptotic and transient arguments, a symmetric-part proof and a coordinate/observable audit. This original AI-assisted assignment uses [MIT OCW 18.06 Spring 2010 calendar](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/calendar/) as a link-only scope comparator; no source problem, proof or code was imported. Qualified review and actual learner workload remain open. The package stays partial and unreviewed.
