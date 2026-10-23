# Assignment 1: subspaces, consistency and coordinate maps

Write a proof-and-calculation packet using the [four-subspace reading](../modules/07-rank-null-space-and-identifiability.md) and [factorization/coordinate reading](../modules/factorizations-maps-and-coordinates.md). Retain row reductions, bases, proofs and residual checks locally. Browser practice evaluates selected values and choices, not the written proof, code or diagrams. Every matrix and vector is constructed; a consistent algebraic model is not automatically a valid measurement model.

## A rectangular map with redundant equations

Let A have four rows (1,0,1), (0,1,1), (1,1,2) and (2,−1,1). Its input space is three dimensional and its output space four dimensional. Find its row-reduced form, pivot columns and rank. Give bases for the column space, row space, null space and left-null space. State the ambient space and dimension for each. Select original columns of A for a column-space basis; row reduction preserves row space but generally changes the actual column-space vectors.

Verify the bases directly. Multiply A by each proposed null vector and A transpose by each proposed left-null vector. Check independence rather than relying only on the right number of vectors. Explain how rank-nullity accounts for both the three-dimensional input and four-dimensional output spaces. Prove the orthogonality relations between row space and null space, and between column space and left-null space, using the relevant dot products.

## Consistency depends on the right-hand side

Use b=(1,2,3,0). Find one solution xp and describe every solution as xp plus the null space. Verify the complete family by substitution into all four original equations. Identify which linear combinations of the input coordinates are fixed by b even though the individual coordinates need not be fixed. Distinguish a free coordinate from an unconstrained physical quantity; a change of input basis can relocate which coordinate is called free.

Find the minimum-Euclidean-norm solution in that affine family. Derive it by minimizing its squared norm as a function of the free parameter. Then prove the same result geometrically: the minimum-norm solution is perpendicular to the null space, so any added null vector increases the squared norm by its own squared norm. This is an algebraic convention selecting among identical outputs, not a new observation of an unmeasured component.

Change only the fourth component of b to 0.3. Test consistency using both the augmented rank and left-null dot products. Identify a linear relation among the output coordinates that the changed b violates. Explain why adding an arbitrary null vector to an old input cannot correct an output component outside the column space. A least-squares fit may be possible, but it solves a different optimization problem from exact consistency.

## Reuse a factorization and track coordinates

For a separate square matrix C with rows (0,1,2), (1,1,0), (2,3,1), verify the reading's pivoted factorization PC=LU by multiplication. Use it to solve for two different right-hand sides that you choose by first selecting distinct known input vectors and forming b=Cx. Keep P applied to both right-hand sides. Report residuals in the original unpermuted equations and explain why checking only LUx=b would miss a permutation mistake.

For a separate basis S with columns (1,0) and (1,1), take z=(1,2) and x=Sz. Compute the physical vector and its Euclidean norm squared. Compute the Gram matrix G and verify that z transpose Gz gives the same norm. Transform the standard-coordinate functional d=(1,2) into its z-coordinate coefficients, then verify the scalar pairing in both coordinate systems. Explain why the functional coefficients and vector coordinates use different transformation rules.

## Claim audit and self-review

For each claim, prove it with hypotheses or supply a counterexample: more equations than unknowns guarantees a unique solution; a zero determinant proves every right-hand side is inconsistent; row operations preserve column-space vectors; and minimum norm recovers the true value of an unobserved coordinate. State whether your counterexample addresses exact arithmetic or sensitivity to noisy data. Do not substitute a numerical tolerance for an exact rank proof.

For the rectangular A, rank is two, nullity one and left-nullity two. One null vector is (−1,−1,1); left-null vectors include (−1,−1,1,0) and (−2,1,0,1). For the original b, xp=(1,2,0) works and the full family is xp+t(−1,−1,1). Minimum norm occurs at t=1, giving (0,1,1) with squared norm two. The observable sums x1+x3 and x2+x3 stay one and two. After the fourth output changes, the second listed left-null pairing is 0.3, demonstrating inconsistency.

Your packet should include all four checked bases, the full solution family, two minimum-norm arguments, consistency tests, factorization reuse and a metric/functional ledger. This original AI-assisted assignment uses [MIT OCW 18.06 Spring 2010](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/calendar/) as a link-only scope comparator; no source problem or proof was imported. Qualified review and measured workload remain open, and the course remains partial and unreviewed.
