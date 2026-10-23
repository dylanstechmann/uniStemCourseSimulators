# Defective matrices, transient growth and matrix exponentials

An eigenvalue describes evolution along an eigenvector. It does not automatically describe the norm of every state at every time. A matrix can lack a full eigenvector basis, and even a stable matrix can exhibit temporary amplification. This reading extends [linear dynamics](03-eigenvalues-and-linear-dynamical-systems.md), [the spectral theorem](09-symmetric-matrices-spectral-theorem-and-quadratic-forms.md) and the existing Markov example to show where diagonalization arguments need additional hypotheses. All states and matrices are exact constructed examples, not biological populations or control-system specifications.

## Repeated eigenvalues do not supply independent eigenvectors

Take J with rows (1/2,2) and (0,1/2). Its characteristic polynomial is (lambda−1/2) squared. To find the eigenvectors, solve (J−I/2)x=0, which requires the second component to vanish. The eigenspace therefore has dimension one although the eigenvalue has algebraic multiplicity two. There is no invertible matrix of two eigenvector columns, so the formula J=PDP inverse with a diagonal D is unavailable.

Call this matrix defective. It does not contradict the spectral theorem: J is not symmetric. A repeated eigenvalue in a symmetric real matrix has enough orthogonal eigenvectors within its eigenspace. Counting roots of the characteristic polynomial is different from counting independent eigenvectors. The distinction is structural, not a small floating-point tolerance decision.

## A nilpotent part gives exact powers

Write J=lambda I+N with lambda=1/2 and N having only upper-right entry two. Since N squared is zero, the binomial expansion terminates:

$$J^n=\lambda^n I+n\lambda^{n-1}N,\qquad n\ge1.$$

The identity term commutes with N, and all terms with N squared or higher vanish. For n=0 use the identity matrix directly. If lambda were zero, handle that nilpotent case separately instead of evaluating a negative power at n=0. This is a selected two-by-two derivation, not a full Jordan canonical-form algorithm.

Starting from x0=(0,1), the state after n steps is (2n(1/2)^(n−1),(1/2)^n). The first three states are (2,1/2), (2,1/4) and (3/2,1/8). The initial Euclidean norm is one; after the first step it is sqrt(17)/2, larger than two. Yet both components ultimately approach zero because geometric decay dominates the polynomial factor n. Thus eigenvalues inside the unit circle imply asymptotic stability in this finite-dimensional example without guaranteeing monotone decay in the chosen norm.

Do not replace J^n by lambda^n times the identity. That would erase the coupling responsible for the transient. Conversely, do not infer that one amplified step means the state must diverge forever. Distinguish one-step norm, maximum transient amplification and long-time behavior.

## Continuous time has a related polynomial factor

For A with rows (−1,4) and (0,−1), write A=−I+N, where N squared is zero. The matrix exponential series yields

$$e^{At}=e^{-t}(I+tN).$$

It equals the identity at t=0, and differentiating verifies d(exp(At))/dt=A exp(At). Starting from (0,1), the solution is (4t exp(−t),exp(−t)). At t=1 its norm is sqrt(17)/e, about 1.516, above the initial norm despite two eigenvalues −1. The first component reaches its maximum at t=1. That is not a claim that the entire vector norm peaks at the same time; different observables can have different maxima.

Eliminating the second variable provides another derivation: ydot=−y gives y=exp(−t), then xdot+x=4exp(−t) has solution x=4t exp(−t) with x(0)=0. This independent component calculation checks the matrix-exponential formula and its initial condition. A numerical trajectory should reproduce both the transient and eventual decay under refinement.

## Norm growth depends on the symmetric part

For a real solution xdot=Ax, differentiate the squared Euclidean norm: d(x transpose x)/dt=x transpose(A transpose+A)x. If the symmetric part (A+A transpose)/2 is negative definite, every nonzero state decreases in Euclidean norm instantaneously. This is a stronger statement than negative real parts of the eigenvalues of A. The symmetric part controls this particular instantaneous norm derivative; it does not replace the evolution equation.

A matrix need not be normal to have monotone norm decay. For a contrasting A with rows (−2,3) and (0,−2), the symmetric part has eigenvalues −2±1.5, both negative. Its solutions therefore decrease in Euclidean norm even though its repeated eigenvalue also has only one eigenvector. The [dynamics assignment](../assignments/coursework-03-dynamics-and-transients.md) asks you to prove that contrast rather than treating non-normality as a guarantee of transient growth.

## Coordinates and interpretation

An invertible change of basis can alter ordinary coordinate Euclidean norms. To compare the same physical norm, carry its metric along as in the [coordinate reading](factorizations-maps-and-coordinates.md). Eigenvalues are similarity invariants; arbitrary coordinate norm values are not. If state variables have different units or scales, a norm also requires a justified weighting before it can be interpreted physically.

Use exact powers or component solutions as references, identify the observable being compared and state the chosen norm and metric. Separate asymptotic stability from bounded-time amplification and from any real system's admissibility constraints. This original AI-assisted instruction uses [MIT OCW 18.06 Spring 2010 syllabus](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/) and [calendar](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/calendar/) as link-only scope comparators for diagonalization, linear differential equations and change of basis. No source proof, problem or code was imported. General Jordan theory, complex/Fourier methods, pseudospectra and real-model validation remain deferred. The package remains partial and unreviewed; workload and qualified proof review are open.
