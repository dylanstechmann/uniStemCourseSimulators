# Solving linear systems: factor once, check the residual, preserve sparsity

**Status:** original ungraded instruction with substantial AI assistance. The matrices are synthetic. This week-11 reading extends the conditioning lesson from interpreting a computed answer to choosing and checking an algorithm. Linear Algebra provides the underlying vector-space definitions; numerical computing adds finite-precision behavior, storage and stopping rules.

## An inverse is an explanation, not the usual algorithm

For Ax=b with a nonsingular square matrix, x=A^−1 b is a mathematical identity. A numerical solver usually factors A and solves triangular systems instead of constructing every entry of its inverse. This avoids unnecessary work and gives a clear path for reusing a factorization with many right-hand sides. It does not make an ill-conditioned problem well-conditioned.

Take A=[[4,1],[2,3]] and b=[6,8]. Eliminate the lower-left entry by subtracting half the first row from the second. The result has U=[[4,1],[0,2.5]] and transformed right-hand side [6,5]. Back substitution gives x_2=2 and x_1=1. The factors are L=[[1,0],[0.5,1]] and U as above, with A=LU. Forward substitution Ly=b produces y=[6,5]; back substitution Ux=y produces the solution.

The multiplication LU recovers A, which checks the factorization independently of b. Substituting x into the original system gives [6,8], checking the solve. These checks catch different defects. A factorization could be correct while a right-hand-side permutation or substitution index is wrong.

## Pivoting changes the factorization contract

The nonsingular matrix [[0,1],[2,3]] has a zero first pivot. Division by that pivot fails even though the system has a unique solution. Swapping rows makes elimination possible. With row permutation P, the conventional relation is PA=LU, so the right-hand side must also become Pb. Applying P to A alone solves a different system.

Partial pivoting chooses a large-magnitude available pivot in the current column. It usually limits dangerous multipliers, but it is not a universal guarantee against all growth or all input conditioning. For physical quantities with disparate units, sensible scaling also matters. A tiny pivot in one unit system does not by itself give a scale-independent singularity diagnosis.

A library solver should report singularity or failure explicitly. Replacing a failed solve with zeros, silently deleting equations or accepting a nonfinite vector hides the defect. When rank deficiency is meaningful, formulate a least-squares or constrained problem and state what identifies its solution. That is a model decision, not an exception handler.

## Cost depends on what is reused

A dense factorization takes work proportional to n³ in the usual elimination model, while solving another right-hand side using the factors takes work proportional to n². Solving ten right-hand sides need not perform ten factorizations when A is unchanged. If A changes between runs, reusing old factors without justification solves the wrong problem.

For n=1000, dense double-precision storage for A alone is 1000²×8=8,000,000 bytes. Actual solver memory can be larger because factors, copies and workspace also occupy space. This estimate is not a benchmark or a promise about elapsed time. Cache layout, hardware, implementation and matrix structure affect performance.

## Iteration is a recurrence with a convergence condition

Split A=D+R, where D contains the diagonal. Jacobi iteration uses x^(k+1)=D^−1(b−Rx^k). All components on the right come from the old vector. Updating components immediately in place gives a different method, Gauss–Seidel. Either can be appropriate, but a test and convergence analysis must match the implemented recurrence.

For A=[[4,−1],[−1,4]], b=[1,2] and x^0=[0,0], Jacobi gives x^1=[0.25,0.5] and x^2=[0.375,0.5625]. The exact solution is [0.4,0.6]. The iteration matrix B=−D^−1 R has off-diagonal entries 0.25, so its infinity norm is q=0.25. Errors satisfy e^(k+1)=B e^k and therefore contract by at most q in this norm.

A computable a posteriori bound under q<1 is ||x*−x^k||∞ ≤ q/(1−q) ||x^k−x^(k−1)||∞. At k=2, the iterate change is 0.125, giving bound 1/24≈0.0416667. Actual error is 0.0375. The bound follows from summing a geometric tail; it is not valid merely because a routine is called “iterative.” A sufficient norm test can fail even when a more detailed spectral analysis shows convergence.

## Stopping should describe the original equation

A small change between iterates can indicate convergence, stagnation or an inappropriately scaled update. Also evaluate r=b−Ax. A normwise backward-error measure is ||r||/(||A|| ||x||+||b||), with a declared norm and treatment of a zero denominator. Relate the residual to conditioning before claiming a small forward error. The earlier conditioning lesson provides a nearly dependent example where these differ substantially.

Use an iteration cap and explicit failure status. Record method, initial guess, tolerances, iteration count and final residual. A routine that returns its last vector after reaching the cap without a warning makes nonconvergence look like success.

## Preserve the structure of a discretized balance

A one-dimensional steady diffusion problem, −u″=f on an interval with fixed endpoint values, can yield a tridiagonal system after centered finite differences. Interior rows contain a central 2 and neighboring −1 coefficients, with the grid-spacing factor handled consistently in the right-hand side. Nonzero endpoint values contribute to the right-hand side; discarding them changes the boundary-value problem.

An n-by-n tridiagonal matrix has at most 3n−2 potentially nonzero entries, compared with n² dense entries. At n=1000 this is 2998 values. Three-diagonal storage uses roughly 8×2998=23,984 bytes for values alone; sparse index and metadata overhead depend on the representation. Do not describe this value-only count as the entire memory footprint.

A specialized tridiagonal elimination can take linear work and storage under suitable pivot conditions. A general sparse factorization can introduce fill-in, so “sparse input” does not guarantee equally sparse factors. Constructing a dense matrix and then converting it to sparse already paid the dense memory cost. Assemble the intended structure directly when large n makes that cost important.

## Worked verification task

For the LU example, reuse L and U with a second right-hand side [1,0]. Forward substitution gives [1,−0.5], and back substitution gives x=[0.3,−0.2]. Multiplication by the original A recovers [1,0]. A separate Jacobi rehearsal uses the same diagonally dominant A but b=[2,1], so the first two iterates from zero are [0.5,0.25] and [0.5625,0.375]. Compute its exact solution and the contraction bound yourself.

For a discretized diffusion test, choose a polynomial with a known second derivative and fixed endpoints, build the interior right-hand side, and check the recovered grid values. Then refine the grid for a non-polynomial reference and separate discretization error from linear-solver error. A tiny linear residual only verifies the discrete equations; it does not prove a fine enough physical grid.

## Scope and sources

[MIT OCW 2.086 Fall 2014 syllabus](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-fall-2014/pages/syllabus/) and [calendar](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-fall-2014/pages/calendar/) frame the linear-system and sparse-computation strand. This original reading develops small factorizations, one convergent iteration and structured discretization. General preconditioning, production sparse solvers and full roundoff analysis require further study. No external asset or code is copied. Original material is CC BY 4.0; review and workload measurement remain open.
