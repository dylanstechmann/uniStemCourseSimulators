# Linear Algebra for Modeling & Robotics

**Maturity: partial. Version: 0.4.0.** This is a personal learning project developed with substantial AI assistance, not an accredited university course.

Vectors, matrices, eigenstructure, least squares and linear transformations applied to state estimation, circuit networks and robot coordinates.

## Prerequisites

Calculus I; matrix arithmetic. Structured prerequisite relationships appear in the manifest and remain subject to author review. This package establishes no university prerequisite equivalency.

## Authored outcomes

- Solve linear systems and diagnose singularity.
- Interpret bases, rank, and null spaces.
- Use eigenvalues to describe linear dynamics.
- Fit an overdetermined model by least squares.

## Proposed 14-week schedule

This is proposed scope, not measured workload or a reviewed semester. Weeks 1, 2, 4 and 7 began as short prototype readings; those readings are now expanded, but each still has only two practice items. Week 7 now opens with a determinants reading before eigenvalues, following the 18.06SC Unit II order. Every reading has public formative items and retrieval cards. Week 13 is a synthetic-data lab; week 14 prepares the existing case checklist.

| Week | Reading | Items | Cards |
|---|---|---:|---:|
| 1 | Linear systems, elimination, and rank | 2 | 2 |
| 2 | Vector spaces, bases, and coordinate transforms | 2 | 2 |
| 3 | Rank, null space and all four fundamental subspaces: consistency and residual geometry | 15 | 8 |
| 4 | Least squares and data fitting | 2 | 2 |
| 5 | Least squares as linear algebra: fitting a calibration line, normal equations and reading residuals | 6 | 4 |
| 6 | Orthogonality, projections and QR: the geometry behind least squares | 9 | 4 |
| 7 | Determinants: volume scaling, row operations and invertibility; Eigenvalues and linear dynamical systems | 13 | 6 |
| 8 | Symmetric matrices, the spectral theorem and quadratic forms | 9 | 4 |
| 9 | Cell-state transitions as a Markov chain: transition matrices, the eigenvalue 1 and how fast a population settles | 6 | 4 |
| 10 | The singular value decomposition and low-rank approximation | 9 | 4 |
| 11 | Conditioning, error bounds and regularization | 9 | 4 |
| 12 | Centered PCA, scaling and interpretation; optional hidden-state project guide | 14 | 7 |
| 13 | Virtual lab 1: sensor geometry, noise and displacement estimates | 8 | 4 |
| 14 | Two displacement sensors: a small residual and an unreliable answer | 9 | 4 |

## Assessment and study policy

Practice includes numeric, single-choice, multiple-select, CSV upload and structured-choice checks. The lab asks for sensor estimates, errors and interpretation. Written discussion criteria are guidance, not automatically graded prose. Retries are unlimited and practice points do not establish an institutional grade, university credit or mastery. Assessments list the objectives and course outcomes their items assess; all four prototype lessons map to course outcomes; these authoring links remain provisional.

There are 16 readings, 113 public practice items and 59 retrieval cards, plus the existing self-assessment case checklist and five project-milestone self-checks. Week 3 now develops all four fundamental subspaces of a rectangular matrix and connects left-null orthogonality to consistency and least-squares residuals.

## Optional hidden-state reconstruction project (ungraded)

The [hidden-state project guide](assignments/hidden-state-reconstruction-project-guide.md) makes the project below usable as open practice. It restates the project's design, readouts and tasks, works a separate design and chain, and pairs synthetic rehearsal readouts with open practice items in week 12. Five milestones, suggested for weeks 12–13, are Case studio self-checks whose responses are saved privately and never submitted, collected or scored.

## Inactive integrative project draft

The [hidden-state reconstruction and transition-dynamics project](assessment-specs/hidden-state-reconstruction-project-draft.md) combines full-rank least squares, residual diagnostics, conditioning, orthonormal coordinates and a three-state transition model using a small synthetic dataset. The authoring draft itself is not scheduled, assigned, collected or graded, and the open project guide above does not submit work to it. Its values and unweighted rubric need independent mathematical, workload and accessibility review before any activation.

## Current limitations

All four compact legacy prototype readings now have expanded instructional content. There is no graded homework sequence, midterm, final or activated integrative project; the optional project guide and its rehearsal are ungraded practice, and the project draft remains inactive. One synthetic lab is not a laboratory sequence. Workload and accessibility have not been measured or reviewed. All uncertainty calculations depend on specified matrix scales and noise assumptions, and regularization supplies a convention rather than a new measurement. The package remains partial and unreviewed.

## Sources and licensing

The source map links the existing linear-algebra and engineering-mathematics scope references, the MIT 18.06SC Fall 2011 session on [the four fundamental subspaces](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/ax-b-and-the-four-subspaces/the-four-fundamental-subspaces/), and its [Unit II determinant sessions](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/least-squares-determinants-and-eigenvalues/). The MIT pages are curriculum comparators; no source text, problem or figure was copied. The new example and practice are original CC BY 4.0 content with substantial AI assistance. Source links do not establish review or endorsement.

See `source-map.json` for module provenance and `content/SOURCES_AND_LICENSES.md` for the software/content license boundary.
