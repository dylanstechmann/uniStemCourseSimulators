# Linear Algebra for Modeling & Robotics

**Maturity: partial. Version: 0.5.0.** This is a personal learning project developed with substantial AI assistance, not an accredited university course.

Vectors, matrices, eigenstructure, least squares and linear transformations applied to state estimation, circuit networks and robot coordinates.

## Prerequisites

Calculus I; matrix arithmetic. Structured prerequisite relationships appear in the manifest and remain subject to author review. This package establishes no university prerequisite equivalency.

## Authored outcomes

- Solve linear systems and diagnose singularity.
- Interpret bases, rank, and null spaces.
- Use eigenvalues to describe linear dynamics.
- Fit an overdetermined model by least squares.
- Analyze coordinate metrics, positive-definite forms and generalized inverse conventions using explicit invariants.

## Proposed 14-week schedule

This is proposed scope, not measured workload or a reviewed semester. Weeks 1, 2, 4 and 7 began as short prototype readings; those readings are now expanded, but each still has only two practice items. Week 7 now opens with a determinants reading before eigenvalues, following the 18.06SC Unit II order. Every reading has public formative items and retrieval cards. Week 13 is a synthetic-data lab; week 14 prepares the existing case checklist.

| Week | Readings and activities |
| --- | --- |
| 1 | [Linear systems, elimination, and rank](modules/01-linear-systems-elimination-and-rank.md) |
| 2 | [Vector spaces, bases, and coordinate transforms](modules/02-vector-spaces-bases-and-coordinate-transforms.md) |
| 3 | [Rank, null space and all four fundamental subspaces: counting independent information](modules/07-rank-null-space-and-identifiability.md); [Factorizations, linear maps and coordinate geometry](modules/factorizations-maps-and-coordinates.md) |
| 4 | [Least squares and data fitting](modules/04-least-squares-and-data-fitting.md); [Assignment 1: subspaces, consistency and coordinate maps](assignments/coursework-01-subspaces-and-maps.md) |
| 5 | [Least squares as linear algebra: fitting a calibration line, normal equations and reading residuals](modules/05-least-squares-calibration-and-residuals.md) |
| 6 | [Orthogonality, projections and QR: the geometry behind least squares](modules/08-orthogonality-projections-and-qr.md) |
| 7 | [Determinants: volume scaling, row operations and invertibility](modules/14-determinants-volume-row-operations-and-invertibility.md); [Eigenvalues and linear dynamical systems](modules/03-eigenvalues-and-linear-dynamical-systems.md) |
| 8 | [Symmetric matrices, the spectral theorem and quadratic forms](modules/09-symmetric-matrices-spectral-theorem-and-quadratic-forms.md); [Assignment 2: projections, orthogonality and quadratic minima](assignments/coursework-02-projections-and-quadratic-forms.md) |
| 9 | [Cell-state transitions as a Markov chain: transition matrices, the eigenvalue 1 and how fast a population settles](modules/06-markov-chains-for-cell-state-transitions.md); [Defective matrices, transient growth and matrix exponentials](modules/defective-matrices-and-transient-dynamics.md) |
| 10 | [The singular value decomposition and low-rank approximation](modules/10-singular-value-decomposition-and-low-rank-approximation.md); [Assignment 3: powers, exponentials and transient behavior](assignments/coursework-03-dynamics-and-transients.md) |
| 11 | [Conditioning, error bounds and regularization](modules/11-conditioning-and-regularization.md) |
| 12 | [Centered PCA, scaling and interpretation](modules/12-centered-pca-and-scaling.md); [Hidden-state project guide: least-squares reconstruction and transition dynamics (optional, ungraded)](assignments/hidden-state-reconstruction-project-guide.md) |
| 13 | [Virtual lab 1: sensor geometry, noise and displacement estimates](labs/01-sensor-geometry.md) |
| 14 | [Two displacement sensors: a small residual and an unreliable answer](modules/13-displacement-sensor-case.md); [Assignment 4: SVD, minimum norm and inverse choices](assignments/coursework-04-svd-and-inverse-choices.md) |

## Assessment and study policy

Practice includes numeric, single-choice, multiple-select, CSV upload and structured-choice checks. The lab asks for sensor estimates, errors and interpretation. Written discussion criteria are guidance, not automatically graded prose. Retries are unlimited and practice points do not establish an institutional grade, university credit or mastery. Assessments list the objectives and course outcomes their items assess; all four prototype lessons map to course outcomes; these authoring links remain provisional.

There are 22 reading/activity routes, 133 public practice items and 79 retrieval cards, plus the existing self-assessment case checklist and five project-milestone self-checks. Week 3 now develops all four fundamental subspaces of a rectangular matrix and connects left-null orthogonality to consistency and least-squares residuals.

## Connected mixed proof/application coursework (open, ungraded)

Four assignments in weeks 4, 8, 10 and 14 require locally retained subspace/consistency/coordinate proofs, projection/weighted-objective/quadratic-minimum arguments, exact powers/exponentials/transient comparisons, and SVD/pseudoinverse/truncation/ridge ledgers. New week-3 and week-9 foundations develop factorization/map/metric/functional transformations and selected defective/transient dynamics. Browser checkpoints evaluate selected outputs, not proofs, reports or code. The existing lab and hidden-state project remain available; workload and qualified review remain open.

## Optional hidden-state reconstruction project (ungraded)

The [hidden-state project guide](assignments/hidden-state-reconstruction-project-guide.md) makes the project below usable as open practice. It restates the project's design, readouts and tasks, works a separate design and chain, and pairs synthetic rehearsal readouts with open practice items in week 12. Five milestones, suggested for weeks 12–13, are Case studio self-checks whose responses can be saved privately and are not submitted for grading.

## Inactive integrative project draft

The [hidden-state reconstruction and transition-dynamics project](assessment-specs/hidden-state-reconstruction-project-draft.md) combines full-rank least squares, residual diagnostics, conditioning, orthonormal coordinates and a three-state transition model using a small synthetic dataset. The authoring draft itself is not scheduled, assigned, collected or graded, and the open project guide above does not submit work to it. Its values and unweighted rubric need independent mathematical, workload and accessibility review before any activation.

## Current limitations

All four compact legacy prototype readings now have expanded instructional content. There is no graded homework sequence, midterm, final or activated integrative project; the optional project guide and its rehearsal are ungraded practice, and the project draft remains inactive. One synthetic lab is not a laboratory sequence. Workload and accessibility have not been measured or reviewed. All uncertainty calculations depend on specified matrix scales and noise assumptions, and regularization supplies a convention rather than a new measurement. The package remains partial and unreviewed.

## Sources and licensing

The source map links the existing linear-algebra and engineering-mathematics scope references, the MIT 18.06SC Fall 2011 session on [the four fundamental subspaces](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/ax-b-and-the-four-subspaces/the-four-fundamental-subspaces/), and its [Unit II determinant sessions](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/least-squares-determinants-and-eigenvalues/). The MIT pages are curriculum comparators; no source text, problem or figure was copied. The new example and practice are original CC BY 4.0 content with substantial AI assistance. Source links do not establish review or endorsement.

See `source-map.json` for module provenance and `content/SOURCES_AND_LICENSES.md` for the software/content license boundary.

The 0.5.0 expansion compares actual elimination, basis, symmetric/SVD and dynamics instruction with [MIT OCW 18.06 Spring 2010 syllabus](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/) and [calendar](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/calendar/). The local prerequisite remains Calculus I; MIT lists 18.02, and this comparison establishes no prerequisite or course equivalence. General Jordan/canonical-form theory, complex/Fourier work, linear programming and broad numerical factorization remain deferred or selective. All new proofs, matrices and coursework are original; no source asset was imported.
