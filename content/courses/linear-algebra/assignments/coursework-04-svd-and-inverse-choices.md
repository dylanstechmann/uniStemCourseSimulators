# Assignment 4: SVD, minimum norm and inverse choices

Develop a cumulative report distinguishing exact identifiability, minimum-norm conventions, rank truncation and regularization. Use [SVD](../modules/10-singular-value-decomposition-and-low-rank-approximation.md), [conditioning/regularization](../modules/11-conditioning-and-regularization.md) and [the four subspaces](../modules/07-rank-null-space-and-identifiability.md). Retain matrices, checked decompositions, proofs and parameter comparisons locally. Browser practice assesses selected outputs and interpretations, not your complete report or code. All data are exact synthetic numbers, with no real sensor inference.

## An underdetermined measurement map

Let A have rows (1,1,0) and (0,0,2), with output b=(2,2). Find its rank, null space and every exact input solution. Identify which input contrast remains invisible. Derive the minimum-Euclidean-norm exact solution by both affine-family optimization and the row-space/null-space decomposition. Explain why selecting that solution does not measure the invisible contrast or establish its true value.

Compute a full or reduced SVD with singular values in descending order. State the dimensions of every factor and check orthonormality and reconstruction. Compare the nonzero eigenvalues of A transpose A and A A transpose, accounting for their different zero multiplicities. A rectangular matrix does not have ordinary eigenvalues in the same sense as a square linear map; use the correct object rather than calling its singular values eigenvalues of A.

Use the SVD to construct the pseudoinverse and recover the minimum-norm exact input. Derive why every added null vector leaves Ax unchanged and increases the squared norm from that minimum. Connect this to the proof in Assignment 1 rather than treating a pseudoinverse command as new information. State where the choice of input norm enters and how a different scaling could choose a different representative.

## Truncate a mode and name the tradeoff

Keep only the larger singular value, setting the other inverse singular response to zero. Calculate the truncated reconstruction, its output residual norm, input norm and fraction of squared matrix Frobenius norm retained. Distinguish matrix approximation error from inverse-solution output error. Explain why a large retained energy fraction does not automatically establish acceptable reconstruction for every b; a right-hand side aligned with a dropped mode can be affected strongly.

Construct such a contrasting right-hand side and compare exact and truncated responses. Then slightly perturb one singular value while keeping b fixed and explain how an inverse can amplify a small measurement-direction component. Keep exact zero singular values separate from small nonzero ones. A tolerance used by software is a declared numerical/model decision, not a proof that the exact matrix rank changed.

## Ridge uses a different objective

Define x_lambda to minimize ||Ax−b||²+lambda||x||² with lambda>0 and all variables dimensionless. Derive (A transpose A+lambda I)x_lambda=A transpose b and prove its uniqueness from positive definiteness. In singular coordinates, derive the filter sigma/(sigma²+lambda), showing how it differs from the exact inverse factor 1/sigma and the truncated zero response.

For lambda=2, solve the problem exactly. Compute both the output residual norm and input norm, then compare them with the exact minimum-norm and rank-one truncated choices. Do not call the regularized vector another exact solution if its output residual is nonzero. State how a chosen penalty parameter expresses a convention or modeling assumption; no noise distribution or optimal selection criterion is supplied by the dataset.

Investigate lambda tending to zero from above and tending to infinity. Explain which limiting vector is selected in the null space and why the full exact affine family is not recovered by a single regularized limit. Compare with imposing a hard constraint on input norm rather than a penalty. If you claim equivalence for a chosen parameter pair, verify the active constraint and hypotheses rather than assuming every constraint/penalty choice matches automatically.

## Self-review and completion standard

The exact family is x1+x2=2 and x3=1; the invisible direction is (1,−1,0). Minimum norm gives (1,1,1), with squared norm three. Singular values are two and sqrt(2). The rank-one inverse reconstruction is (0,0,1), with residual norm two, input norm one and retained matrix-energy fraction 4/6. Its loss of the first output is a deliberate truncation consequence.

At lambda=2 the ridge vector is (1/2,1/2,2/3). Its output is (1,4/3), leaving residual (1,2/3) and residual norm sqrt(13)/3. Compare the objective values directly to verify minimization under the stated penalty; do not compare only residuals across different objectives. The minimum-norm exact, truncated and ridge results each answer a different declared question.

A complete report includes checked SVD/pseudoinverse factors, an invisible-direction proof, all three solution/residual/norm ledgers, filter derivations, parameter limits and a right-hand-side sensitivity counterexample. This original AI-assisted assignment uses [MIT OCW 18.06 Spring 2010 syllabus](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/) as a link-only scope comparator; no source exercise, data or implementation was imported. The course remains partial and unreviewed; written proof quality, actual learner workload and qualified mathematical review remain open.
