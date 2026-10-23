# Assignment 4: a solver verification portfolio

**Open, ungraded local implementation practice, authored with substantial AI assistance.** Proposed placement: week 13 after linear systems, nonlinear systems and eigenproblems. No learner code is executed or graded by the platform. The goal is evidence about algorithms on declared mathematical problems, not a speed contest or a claim about a real device.

## Three linked problems

First solve A_n u=b for the n-by-n tridiagonal matrix with diagonal 2 and immediate off-diagonals −1. Use homogeneous endpoint values and choose the reference interior vector u_i=sin(πi/(n+1)), i=1,…,n. Construct b by applying A_n to that vector rather than importing an external data file. This is a manufactured discrete solution for checking a linear solver.

Second find eigenpairs of the same matrix. The reference eigenvalues are λ_j=2−2cos(jπ/(n+1)), j=1,…,n; the sine vectors provide corresponding directions. Derive the identity by substituting the sine addition formulas into an interior matrix row, then verify the endpoint rows. Do not treat a formula printed here as sufficient proof that your indexing matches it.

Third solve the nonlinear system F=[x²+y²−5,x−y−1] from several declared initial guesses. The exact roots are (2,1) and (−1,−2). These three problems share residual and conditioning ideas but require different algorithms and interpretations.

## Part A: direct and iterative linear solves

Implement a small dense elimination method with a clearly documented pivot policy, or use a documented library factorization and independently implement the matrix-vector product and residual checks. Compare against a specialized tridiagonal solver or a stationary iteration whose convergence conditions you analyze. Keep matrix construction, solving and checking in separate functions.

Use n=3 as a hand-verifiable start, then n=10,100 and a larger size appropriate for your machine. Store the tridiagonal structure directly for the large case. Report the value count 3n−2 and distinguish it from actual memory including indexes, copies and factors. Do not allocate a giant dense matrix merely to prove it is larger.

Compute ||b−A u_hat||∞, a scaled backward-error measure and the actual error against the manufactured vector. Explain why the exact discrete solution lets you measure forward error here, whereas a production problem may not supply it. If you use an iteration, report its initial guess, termination rule, iteration count and failure status. A small iterate change alone is insufficient.

## Part B: eigenvalue and direction checks

For n=3, the eigenvalues are 2−sqrt(2),2 and 2+sqrt(2). Apply power iteration to a declared nonorthogonal start and compare its Rayleigh quotient with the largest reference value. Check Av−λv with a stated normalization and norm. Test a start that lacks the targeted mode to show why an initial projection matters.

For larger n, compare convergence as dominant eigenvalues become closer in magnitude. Count matrix-vector products and keep representation cost separate from mathematical iteration count. If using shifted inverse iteration, explain the selected shift and how factorization is reused; do not explicitly form a large inverse. A shift equal to an eigenvalue makes the shifted matrix singular.

## Part C: nonlinear convergence and failure evidence

Derive the Jacobian of F and verify at least one directional derivative with a finite-difference step sweep. Implement a full Newton step and one documented damping rule. Use initial points (2,0),(2,1.5),(−2,−1) and a point where x+y=0. Record the residual norm, scaled update and termination reason for every run.

A singular Jacobian should produce an explicit failure or a documented alternative step, not a silent success. If different starts find different roots, compare them with the exact geometric solution. Do not infer uniqueness from whichever run is easiest to plot. A residual merit function should use declared scales rather than units chosen after seeing convergence.

## Part D: cross-checks and cost claims

For n=3, choose reference u=[1,2,1]. Then b=A_3 u=[0,2,0]. This separate hand test checks the central and boundary rows, and a correct solve returns the original vector. It is not the same sine-vector experiment and should remain labeled as an additional test.

For the nonlinear system at (2,0), the full correction [0.25,1.25] increases the infinity residual norm to 1.625, while half the step reduces it to 0.5. Your trace should reproduce these values under the stated norm. This checks the sign of the correction, residual evaluation and acceptance decision simultaneously.

If reporting time, separate construction, factorization, repeated solves and validation. Perform warm-up and repeated timing carefully, describe the environment and avoid extrapolating one small case to all machines. Complexity describes scaling under a model; it does not supply measured seconds or a universal method ranking.

## Self-review and report

Submit nothing for a course grade. Keep a local portfolio containing equations, derivations, implementation/source versions, test cases, residual/error tables, convergence/failure traces and a limitations section. Explain which reference results came from analytical derivation, independent code, a library or AI assistance. Give text descriptions for plots.

The portfolio should show both success and a deliberately diagnosed failure. A collection of solver success flags is insufficient. Conversely, a failed test is useful when it identifies an assumption violation such as singularity, missing modal projection or inadequate iteration cap. Keep numerical verification distinct from validation of any physical interpretation.

All examples and tasks are original CC BY 4.0 material. [MIT OCW 2.086 Fall 2014 syllabus](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-fall-2014/pages/syllabus/) and [calendar](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-fall-2014/pages/calendar/) are link-only scope comparators. No external problem or implementation was imported; qualified review and measured workload remain open.
