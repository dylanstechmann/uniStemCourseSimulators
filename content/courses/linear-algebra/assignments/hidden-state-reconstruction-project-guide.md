# Hidden-state project guide: least-squares reconstruction and transition dynamics (optional, ungraded)

**Status:** open, optional and ungraded. Five milestone self-checks in the Case studio save responses privately; nothing is submitted, collected or scored. The separate inactive project draft and its proposed review rubric remain unreviewed and are not served to learners.
**Introduced in:** course package version 0.4.0.
**Suggested time (unvalidated author estimate):** 3–5 hours across weeks 12 and 13.
**Prerequisite lessons:** [Least squares and data fitting](../modules/04-least-squares-and-data-fitting.md), [Markov chains for cell-state transitions](../modules/06-markov-chains-for-cell-state-transitions.md), [Rank, null space and identifiability](../modules/07-rank-null-space-and-identifiability.md), [Singular value decomposition and low-rank approximation](../modules/10-singular-value-decomposition-and-low-rank-approximation.md) and [Conditioning and regularization](../modules/11-conditioning-and-regularization.md).
**Data:** the [project readouts](../assessment-specs/state-readouts.csv) and the [rehearsal readouts](rehearsal-readouts.csv).

## Purpose

The project uses one small overdetermined model twice. First it estimates a three-component state vector from five noisy readouts by least squares, asking whether the components are identifiable and how sensitive the estimate is. Then it propagates that vector with a transition matrix and expresses the motion in coordinates adapted to the matrix, where the convergence becomes obvious. It ends by separating the arithmetic from any claim about real states.

## The project

A fictional simulator reports five readout channels as linear mixtures of three abstract states A, B and C, with b = Ax + e. The values do not represent biomarkers, an instrument or an experiment. The project readouts file gives

\[
A=\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\\1&0&0\\0&1&0\end{bmatrix},\qquad
b=\begin{bmatrix}0.21\\0.49\\0.30\\0.19\\0.51\end{bmatrix}.
\]

The rows are equally weighted. Fit by least squares, and do not impose a nonnegativity or sum-to-one constraint silently.

1. Inspect the columns of A. Find its rank and nullity, and explain whether the three components are identifiable from these channels.
2. Form AᵀA and Aᵀb, solve the normal equations, and verify the estimate by a QR-based solve or by checking that the residual is orthogonal to every column of A.
3. Report b − A x̂, its squared Euclidean norm, the singular values of A and its 2-norm condition number. Explain why a nonzero residual is compatible with a unique estimate.
4. For a separate time-evolution exercise with column vectors, use

   \[
   T=\begin{bmatrix}0.8&0.1&0.1\\0.1&0.8&0.1\\0.1&0.1&0.8\end{bmatrix},\qquad p_{k+1}=Tp_k,
   \]

   starting at p₀ = x̂. Verify nonnegativity and that each column of T sums to one, compute p₁, and identify the stationary composition.
5. Change to the orthonormal basis q₀ = (1, 1, 1)/√3, q₁ = (1, −1, 0)/√2 and q₂ = (1, 1, −2)/√6. Show how T acts on each coordinate, use the eigenvalues to explain convergence, and state why this abstract transition model does not support a claim about any real population.

## Milestones

| Milestone | Suggested week | Task | Where to check yourself |
| --- | --- | --- | --- |
| Rehearsal | 12 | Work the rehearsal readouts and chain, then use the open rehearsal practice set | **Practice gradebook**: Hidden-state project rehearsal |
| M1 | 12 | Rank, nullity and identifiability (task 1) | Case studio: project milestone 1 |
| M2 | 12 | The least-squares estimate and its check (task 2) | Case studio: project milestone 2 |
| M3 | 12 | Residual, singular values and conditioning (task 3) | Case studio: project milestone 3 |
| M4 | 13 | The transition, its stationary vector and the new basis (tasks 4–5) | Case studio: project milestone 4 |
| M5 | 13 | Convergence and the limits of the model (task 5) | Case studio: project milestone 5 |

Each Case studio milestone lists self-review statements. Responses are saved privately in this application and are never scored.

## Rehearsal readouts and chain

The [rehearsal readouts](rehearsal-readouts.csv) mix two abstract states P and Q in four channels with weight rows (1, 0), (0, 1), (1, 1) and (1, 0). A separate two-state chain uses T = [[0.85, 0.30], [0.15, 0.70]] from p₀ = (0.40, 0.60). Work the same steps on them, then check yourself with the open rehearsal practice set, which gives feedback on each value. The design, readouts and chain differ from the project's, so their answers are not the project's answers.

## Worked example: a third design and chain

Take two states, three channels with weight rows (1, 0), (0, 1) and (1, −1), and readouts b = (0.5, 0.3, 0.25).

1. **Identifiability.** The columns (1, 0, 1) and (0, 1, −1) are independent, so the rank is 2, the nullity 0, and the least-squares estimate is unique.
2. **Normal equations.** AᵀA = [[2, −1], [−1, 2]] and Aᵀb = (0.75, 0.05). The determinant is 3, so x̂ = ((2 × 0.75 + 0.05)/3, (0.75 + 2 × 0.05)/3) ≈ (0.5167, 0.2833).
3. **Residual and conditioning.** r = b − A x̂ ≈ (−0.0167, 0.0167, 0.0167), and Aᵀr = (0, 0) confirms the solution. ‖r‖² ≈ 0.000833. The eigenvalues of AᵀA are 3 and 1, so the singular values are √3 and 1 and κ₂(A) = √3 ≈ 1.732.
4. **A two-state chain.** For T = [[0.9, 0.4], [0.1, 0.6]], each column sums to one and the eigenvalues are 1 and 0.9 + 0.6 − 1 = 0.5. Starting from p₀ = (1, 0), p₁ = (0.9, 0.1). The stationary vector solves 0.1π₁ = 0.4π₂, giving π = (0.8, 0.2), and the other mode halves at every step.

In a basis of eigenvectors, the stationary coordinate stays fixed and the other coordinate is multiplied by 0.5 each step; that is the whole of the convergence argument. None of it says anything about real cells.

## Reporting conventions

- Use column vectors throughout, and state the residual convention r = b − A x̂.
- Keep at least four significant figures in intermediate values and round only reported results.
- Check column sums and nonnegativity before iterating a transition matrix.
- Disclose any software, spreadsheets or AI assistance you used.

## Self-review rubric

The inactive project draft proposes five criteria for a future human reviewer and assigns them no points. For self-review, mark each criterion 0 (absent), 1 (partly correct) or 2 (complete and consistent with the stated model).

| Criterion | Evidence of a complete response |
| --- | --- |
| Identifiability | Uses rank and nullity to justify whether all three weights can be recovered |
| Least squares | Computes the estimate and checks residual orthogonality |
| Numerical interpretation | Reports singular values and distinguishes fit residual from conditioning |
| Dynamics | Checks the transition convention, stationary vector and eigenmode behavior |
| Limits | Separates the constructed mathematics from claims about real biological states |

These marks are a self-check. They are not calibrated, carry no grade and do not stand in for an instructor's judgment.

## Limitations and provenance

The readouts, weights and transition matrices are synthetic teaching constructs. Unweighted least squares assumes equal error variance across channels, and an unconstrained fit need not return a valid mixture. Nothing here describes any real instrument, biomarker, cell type or population. Original guide and synthetic rehearsal data: CC BY 4.0, developed with substantial AI assistance.
