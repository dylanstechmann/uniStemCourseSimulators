# Hidden-state reconstruction and transition dynamics: inactive project draft

**Status:** authoring draft only. This project is not scheduled, assigned, submitted, collected or graded. It is not a protected assessment or evidence of real cell behavior. All channels, state labels, transitions, values and errors below are synthetic teaching constructs.

## Purpose and outcomes

Use a small overdetermined linear model to estimate a three-component state vector, then express and propagate it in coordinates adapted to a transition matrix. The draft targets the course outcomes to solve systems and diagnose singularity, interpret rank and bases, use eigenvalues for discrete dynamics, and fit an overdetermined model by least squares.

## Scenario and data

A fictional simulator reports five readout channels as linear mixtures of three abstract states A, B and C. Let `b = A x + e`, where `x` is the unknown state mixture and `e` is readout error. The values do not represent biomarkers, a real instrument or a biological experiment. The complete public dataset is [state-readouts.csv](state-readouts.csv):

\[
A=\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\\1&0&0\\0&1&0\end{bmatrix},\qquad
b=\begin{bmatrix}0.21\\0.49\\0.30\\0.19\\0.51\end{bmatrix}.
\]

The measurement relation is assumed linear and the rows are equally weighted. Fit by least squares; do not impose a nonnegativity or sum-to-one constraint silently. In this constructed example the unconstrained estimate happens to be a valid mixture.

## Work sequence

1. Inspect the columns of `A`. Find its rank and nullity, and explain whether the three components are identifiable from these channels.
2. Form `AᵀA` and `Aᵀb`, solve the least-squares normal equations, and verify the estimate by an orthogonal QR-based solve or by checking that the residual is orthogonal to every column of `A`.
3. Report `b − A x̂`, its squared Euclidean norm, the singular values of `A`, and its 2-norm condition number. Explain why a nonzero residual is compatible with a unique least-squares estimate.
4. For a separate synthetic time-evolution exercise, use column vectors and

   \[
   T=\begin{bmatrix}0.8&0.1&0.1\\0.1&0.8&0.1\\0.1&0.1&0.8\end{bmatrix},\qquad p_{k+1}=Tp_k,
   \]

   starting at your estimate `p₀ = x̂`. Verify nonnegativity and that each column of `T` sums to one. Compute `p₁` and identify the stationary composition.
5. Change to the orthonormal basis

   \[
   q_0=(1,1,1)/\sqrt3,\quad q_1=(1,-1,0)/\sqrt2,\quad q_2=(1,1,-2)/\sqrt6.
   \]

   Show that the mean coordinate is unchanged by `T` and both contrast coordinates are multiplied by 0.7. Use the eigenvalues to explain convergence, then state why this abstract transition model does not support a claim about any real population.

## Author calculation key

The columns of `A` are independent, so `rank(A)=3` and `nullity(A)=0`. The normal equations are

\[
A^TA=\operatorname{diag}(2,2,1),\qquad A^Tb=(0.40,1.00,0.30)^T,
\]

giving `x̂=(0.20,0.50,0.30)`. With the residual convention `r=b−Ax̂`, `r=(0.01,−0.01,0,−0.01,0.01)` and `Aᵀr=0`; the squared residual norm is `0.0004`. The singular values are `√2, √2, 1`, so `κ₂(A)=√2≈1.4142`.

The transition is `T=0.7I+0.1 11ᵀ`, so its eigenvalues are `1, 0.7, 0.7`. The normalized stationary vector is `π=(1/3,1/3,1/3)`. One step gives `p₁=(0.24,0.45,0.31)`. In the stated orthonormal basis the coordinates of `p₀` are `(1/√3, −0.3/√2, 0.1/√6)`; the last two coordinates shrink by 0.7 per step, while the first remains fixed. This establishes only the arithmetic of the synthetic model.

## Proposed unweighted review rubric

| Criterion | Evidence for future human review |
|---|---|
| Identifiability | Uses rank and nullity to justify whether all three weights can be recovered |
| Least squares | Computes the estimate and checks residual orthogonality |
| Numerical interpretation | Reports singular values and distinguishes fit residual from conditioning |
| Dynamics | Checks the transition convention, stationary vector and eigenmode behavior |
| Limits | Separates the constructed mathematics from claims about real biological states |

The criteria have no point weights or automatic prose grader. Human reasoning, workload, mathematical accuracy, accessibility, and delivery policy remain unreviewed. Do not activate this draft or describe it as a course assessment until those reviews and the course's missing homework, laboratory and exam components are addressed.

## Provenance

Original authoring and constructed values, CC BY 4.0, developed with substantial AI assistance. No external dataset or real experimental procedure is included.
