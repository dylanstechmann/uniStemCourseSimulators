# Numerical eigenproblems: direction convergence and residual evidence

**Status:** original instruction and public practice developed with substantial AI assistance. This week-11 reading uses exact small matrices and local calculations. It builds on Linear Algebra's eigenvector definitions and the numerical conditioning/solver readings. No learner implementation is executed or automatically certified.

## State the mathematical target

An eigenpair satisfies Av=λv with v nonzero. Multiplying v by any nonzero scalar describes the same eigenvector direction, so comparing raw vector components without a normalization convention can be misleading. Numerical routines typically return normalized vectors, and even then an overall sign or complex phase can differ.

For the symmetric matrix A=[[3,1],[1,3]], the vectors [1,1] and [1,−1] have eigenvalues 4 and 2. The first gives the same-sign mode and the second the opposing-sign mode. These facts can be verified by multiplication without using a characteristic polynomial. In a model x′=−Ax, they correspond to exponential decay rates 4 and 2; a dominant eigenvalue of A is not necessarily the slowest decay rate of −A.

## Derive power iteration from the mode decomposition

Write the initial vector as a combination of eigenvectors. For this A and x^0=[1,0], x^0=0.5[1,1]+0.5[1,−1]. After k unnormalized products, A^k x^0=0.5×4^k[1,1]+0.5×2^k[1,−1]. Relative to the first component's modal coefficient, the unwanted coefficient shrinks by (2/4)^k=2^−k.

Repeatedly multiplying without normalization can overflow. Normalize after each product, for example by its infinity norm or Euclidean norm, and retain the convention in the report. With infinity normalization, the first product gives [1,1/3] and the second [1,3/5]. The first component does not converge in magnitude because it is fixed to one; the direction converges toward [1,1].

Power iteration targets a uniquely dominant eigenvalue in magnitude when the initial vector has a nonzero component along its eigenvector and the relevant decomposition behaves appropriately. Starting exactly from [1,−1] in this example stays in the eigenvalue-2 direction. Roundoff might perturb that special start, but it is not a sound convergence guarantee. An algorithm's assumptions belong in the explanation.

## Estimate an eigenvalue with a Rayleigh quotient

For a real vector v, the Rayleigh quotient is ρ(v)=(vᵀAv)/(vᵀv). At v=[1,0], it is 3. At the first unnormalized product [3,1], it is 36/10=3.6. At the second product [10,6], it is 528/136=66/17≈3.88235294. Scaling v does not change the quotient.

For a symmetric matrix, a small angle to an eigenvector often yields a quotient with an error quadratic in that angle. This helps explain why eigenvalue estimates can appear converged while the direction still changes noticeably. Do not treat a stable quotient alone as proof that a mode shape is accurate.

## Check the defining equation

Given a normalized v and an estimate λ_hat, form r=Av−λ_hat v. A scale-aware relative residual is ||r||/(||A|| ||v||), assuming the denominator is nonzero. State the norm; changing norms changes the reported number.

For v=[1,0.5] and λ_hat=3.8, Av=[3.5,2.5], so r=[−0.3,0.6]. With infinity norms, ||A||∞=4, ||v||∞=1 and the relative residual is 0.15. The pair does not nearly satisfy the equation on this scale. Reporting only the approximate eigenvalue 3.8 conceals that evidence.

For real symmetric A, an orthonormal eigendecomposition implies that some eigenvalue lies within ||r||₂/||v||₂ of the Rayleigh quotient. This statement concerns eigenvalue proximity, not unique identification of a vector. If eigenvalues are clustered, an approximate invariant subspace can be meaningful even when an individual direction is sensitive. Nonsymmetric and defective matrices need a more careful conditioning analysis; this symmetric bound must not be applied indiscriminately.

## What happens without a unique dominant magnitude?

For diag(2,−2) and start [1,1], successive normalized products alternate between [1,−1] and [1,1]. Magnitudes do not separate, and ordinary power iteration does not converge to a single direction. A negative uniquely dominant eigenvalue also flips the vector sign each step, although its direction up to sign can converge. A convergence test should account for this sign ambiguity instead of interpreting a sign flip as a physical mode reversal.

Complex dominant pairs can produce rotating real iterates. Multiple or nearly equal dominant magnitudes slow or defeat the simplest iteration. A maximum iteration count and a residual-based status are therefore part of an implementation, not optional decoration.

## Inverse iteration is a solve at each step

To target a mode near a chosen shift σ, one may repeatedly solve (A−σI)w=v and normalize w. An eigenvector with eigenvalue λ is multiplied by 1/(λ−σ), so a nearby eigenvalue can dominate the inverse iteration. Do not form the inverse explicitly; use a factorization and triangular solves when the shifted matrix is fixed.

For A=diag(2,5), σ=1 and start [1,1], one solve gives w=[1,0.25]. Infinity normalization leaves those values unchanged, and the direction moves toward the eigenvalue-2 mode. Choosing σ exactly equal to an eigenvalue makes the shifted matrix singular, so the displayed solve is not defined. Choosing a very close shift can also make the solve ill-conditioned. A useful mathematical transformation can create a demanding numerical subproblem.

## A local verification workflow

Implement a matrix-vector product and normalization separately. Check dimensions, finite values, a nonzero initial vector and a nonzero product norm before division. Each iteration should retain enough information to report the quotient, residual and convergence status. Test on a diagonal matrix with known eigenpairs, the symmetric coupled example above, a deliberately unfavorable start and equal dominant magnitudes.

An invariant test is stronger than matching one library's sign convention. Verify Av≈λv and normalize consistently. Compare small problems with an independent direct calculation. A production library's output is useful evidence, but it is not a substitute for checking that the matrix represents the intended physical operator, boundary conditions and units.

## Practice and interpretation

Use A=[[4,1],[1,4]] and start [1,0] as a separate rehearsal. Identify both eigenpairs, carry out two products and compute the second Rayleigh quotient. Derive the modal convergence factor from the eigenvalues rather than guessing it from one rounded iterate. For a proposed pair v=[1,0], λ=4, compute the residual norm and its infinity-norm scale.

If this A enters x′=−Ax, state which mode decays more slowly and why power iteration on A emphasizes a different rate. Distinguish numerical mode evidence, time-scale interpretation and validation of the model that produced A. A correct eigenvalue computation cannot establish that the model includes all relevant mechanisms.

## Scope and attribution

The official [MIT OCW 2.086 Fall 2014 calendar](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-fall-2014/pages/calendar/) includes numerical eigenproblems with ODEs. The local reading covers power/inverse iteration and residual checks, not a full QR algorithm, large-scale Krylov methods or arbitrary nonsymmetric sensitivity. Its examples, explanations and practice are original CC BY 4.0 material authored with AI assistance. No comparator problems, code or instructional text were imported; qualified review and measured workload remain open.
