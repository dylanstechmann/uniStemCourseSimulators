# Assignment 2: projections, orthogonality and quadratic minima

Develop a report linking least-squares geometry, orthogonal factorizations and positive-definite quadratic forms. Use [projections and QR](../modules/08-orthogonality-projections-and-qr.md), [symmetric forms](../modules/09-symmetric-matrices-spectral-theorem-and-quadratic-forms.md) and [coordinate metrics](../modules/factorizations-maps-and-coordinates.md). Keep exact calculations and proofs locally. Browser checkpoints assess selected responses, not a proof, numerical implementation or the validity of any real data model.

## An overdetermined fit with a geometric residual

Let B have rows (1,0), (1,1), (1,2) and y=(1,2,2). Derive the normal equations for minimizing the squared Euclidean residual. Solve them in exact arithmetic, then independently obtain the same fitted coefficients by constructing a reduced QR factorization. State the sign convention used for the orthonormal columns; changing a column sign requires the matching row of R to change, leaving the product unchanged.

Calculate fitted outputs, the residual r=y−B beta and its norm. Verify B transpose r=0 directly. Show that the fitted output is the orthogonal projection of y onto the column space by proving the Pythagorean residual identity for an arbitrary coefficient perturbation. Explain why uniqueness of the coefficients requires independent columns, whereas the projected output can be unique even with redundant coefficient columns.

Construct the projection matrix P=B(B transpose B) inverse B transpose. Check P transpose=P and P squared=P by exact multiplication. Find its rank and eigenvalue possibilities from the projector identity. Explain the distinction between a three-by-three map on observation space and the two fitted coefficients. An output-space projection matrix is not an inverse of the rectangular B.

## Change the geometry deliberately

Repeat the conceptual derivation when the first observation receives weight two and the other two weight one. State the positive diagonal weight matrix W and the objective r transpose Wr. Derive B transpose Wr=0 and explain why an ordinary unweighted residual dot product can now be nonzero at the weighted optimum. The changed fit is a changed objective, not evidence that either data source became more accurate merely because a weight was assigned.

Compare the weighted fit with rescaling the observation coordinates by square roots of the weights. Identify which inner product then becomes Euclidean and carry the transformations through both design and response. Discuss why variable units and scaling affect a chosen norm. Report the assumptions under which weights could be interpreted statistically; none are supplied by this exact teaching table.

## A positive-definite quadratic problem

Let C have rows (3,1) and (1,3), and let d=(2,4). Define f(z)=one half z transpose Cz−d transpose z. Derive the stationary equation, solve it and calculate the minimum value. Compute the eigenvalues of C and prove strict positivity of its quadratic form. Complete the square to show f(z)−f(zstar)=one half (z−zstar) transpose C(z−zstar), giving a global uniqueness argument rather than only a stationary-point calculation.

Find a Cholesky factor of C and use it to rewrite the quadratic as a squared norm plus a constant after a suitable shift. Check the factorization by multiplication. Explain why positive diagonal entries alone would not have proved positive definiteness for an arbitrary symmetric matrix. Supply a two-by-two counterexample with positive diagonal entries but a negative quadratic value in some direction.

## Similarity and congruence are different claims

For S with columns (1,0) and (1,1), compare S inverse A S and S transpose A S when A=diag(2,3). Derive which transformation describes a linear map and which describes its scalar quadratic form. Verify that the former preserves eigenvalues while the latter preserves positive definiteness in this example but has different ordinary-coordinate eigenvalues. Explain the role of G=S transpose S if comparing physical lengths in the nonorthogonal basis.

## Self-review and retained evidence

The unweighted coefficients are (7/6,1/2), fitted outputs (7/6,5/3,13/6), and residual (−1/6,1/3,−1/6). Residual norm squared is 1/6. Recompute these from both normal equations and QR, then verify the exact residual orthogonality before using browser feedback.

The quadratic matrix C has eigenvalues four and two. Its unique minimizer is (1/4,5/4) with value −11/4. The completed-square identity proves every distinct point has a larger value. For the separate coordinate example, the map matrix has rows (2,−1),(0,3), while the form matrix has rows (2,2),(2,5). Their different transformation rules are the point of the comparison, not a contradiction.

A complete report retains QR/normal-equation agreement, projection identities, a weighted-objective derivation, a strict quadratic-minimum proof, checked Cholesky factors and a coordinate/metric comparison. This original assignment was developed with substantial AI assistance. [MIT OCW 18.06 Spring 2010 syllabus](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/) is a link-only scope comparator; no source problem, proof or figure was imported. Written proofs, workload and qualified review remain open; the package is partial and unreviewed.
