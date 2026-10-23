# Programming & Numerical Methods for Bioengineering

**Maturity: partial. Version: 0.6.0.**

Reproducible scientific computing, data structures, visualization, numerical integration, model fitting, and error analysis for experimental and engineered systems.

This is a personal hobby and learning project developed with substantial AI assistance. The expanded authored sequence supports local implementation and model/error reasoning; it has no independent approval or measured semester workload.

## Prerequisites

Algebra, introductory calculus and basic probability. Linear Algebra and Differential Equations provide useful shared foundations; numerical-method readings restate only the pieces needed for their algorithms. No university prerequisite equivalency is established.

## Authored outcomes

- Write modular code with explicit inputs and outputs.
- Select numerical methods and diagnose error.
- Fit models without confusing interpolation and validation.
- Make reproducible plots and document data provenance.
- Interpolate a value from tabulated data and assess the error and domain limits.

## Proposed 14-block sequence

The calendar preserves stable lesson IDs and groups new foundations with the relevant existing units. Five local implementation assignments complement selected browser checks; the app does not run learner code. A study budget of roughly 6–9 hours per block, including implementation, is an unvalidated author planning estimate, not measured workload or credit. Use the assignment scope and your own work log to test it.

| Week | Readings and activities |
| --- | --- |
| 1 | [Data structures, units, and reproducible code](modules/01-data-structures-units-and-reproducible-code.md) |
| 2 | [Input contracts, parsing and pure scientific functions](modules/08-contracts-parsing-and-pure-functions.md) |
| 3 | [Testing a scientific function: known answers, tolerances, seeds and provenance](modules/05-testing-scientific-functions-and-provenance.md) |
| 4 | [How long will it take? Algorithmic cost, scaling and choosing data structures for research code](modules/06-algorithmic-cost-and-scaling.md); [Assignment 1: validated observation tables](assignments/coursework-01-contracts.md) |
| 5 | [Array shapes, broadcasting and memory-aware reductions](modules/09-array-shapes-broadcasting-and-memory.md) |
| 6 | [Floating-point arithmetic in scientific code: rounding, cancellation and comparing numbers safely](modules/07-floating-point-rounding-and-cancellation.md) |
| 7 | [Numerical integration and differential models](modules/02-numerical-integration-and-differential-models.md); [Numerical differentiation, noise and step selection](modules/differentiation.md); [Assignment 2: numerical-calculus verification](assignments/coursework-02-approximation.md) |
| 8 | [Root brackets, residuals and conditioning](modules/10-root-brackets-residuals-and-conditioning.md); [Factorization, iteration and sparse linear systems](modules/linear-solvers.md); [Nonlinear systems, Jacobians and damped Newton steps](modules/nonlinear-systems.md) |
| 9 | [Quadrature, step error and stability checks](modules/11-quadrature-step-error-and-stability.md); [Adaptive ODE error control, stiffness and verification](modules/adaptive-odes.md) |
| 10 | [Regression, uncertainty, and validation](modules/03-regression-uncertainty-and-validation.md); [Interpolation: exact fit at nodes, error between them](modules/15-interpolation-error-and-extrapolation.md) |
| 11 | [Linear-system conditioning, residuals and solution error](modules/14-linear-system-conditioning-residuals-and-solution-error.md); [Least squares, rank and scaled coordinates](modules/12-least-squares-rank-and-scaled-coordinates.md); [Numerical eigenpairs, iteration and residuals](modules/eigenproblems.md) |
| 12 | [Visualization and uncertainty communication](modules/04-visualization-and-uncertainty-communication.md); [Monte Carlo estimation, uncertainty and reproducibility](modules/monte-carlo.md); [Assignment 3: reproducible estimator study](assignments/coursework-03-simulation.md) |
| 13 | [Grouped validation, thresholds and reproducible reports](modules/13-grouped-validation-thresholds-and-reproducibility.md); [Sensor-calibration project guide: a reproducible pipeline tested on held-out batches (optional, ungraded)](assignments/sensor-calibration-project-guide.md); [Assignment 4: solver verification portfolio](assignments/coursework-04-solvers.md) |
| 14 | [Virtual lab 1: contract checks and held-out donor reports](labs/01-contracts-and-held-out-donor-reports.md); [Assignment 5: reproducible dynamical-model study](assignments/coursework-05-dynamics.md) |

## Coursework and practice

The current package contains 28 lessons/activity guides, 145 public practice items and 93 retrieval cards. Counts measure inventory, not instructional depth. Six new readings develop finite differences, Monte Carlo, linear/sparse solvers, eigenproblems, coupled nonlinear solves and adaptive/stiff ODEs with separate worked/rehearsal cases.

Five original assignments require local parsing/tests, numerical-calculus convergence, estimator/coverage experiments, solver verification and a dynamical-model report. Each packet supplies mathematical inputs, verification targets, implementation/failure tasks and a self-review discussion. Selected arithmetic/interpretation checkpoints receive open practice feedback. Code, derivations, plots and written evidence are not automatically evaluated or given a course grade.

## Existing project and lab

The [sensor-calibration project guide](assignments/sensor-calibration-project-guide.md) and the synthetic contract/held-out-donor lab remain available. Project milestone responses may be saved privately in Case studio and do not generate grades. The [sensor-calibration authoring proposal](assessment-specs/integrative-sensor-calibration-project.md) remains an inactive, ungraded draft and is not part of the assessment schedule. Open rehearsal is not a secure examination.

## Scope and remaining depth

The link-only comparators are [MIT OCW 2.086 Fall 2014 syllabus](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-fall-2014/pages/syllabus/) and [calendar](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-fall-2014/pages/calendar/). The local sequence now develops selected numerical-calculus, probability/simulation, matrix/eigenvalue, ODE and nonlinear-system strands through original instruction and implementation tasks. It uses Python-oriented examples rather than reproducing MIT software or assignments.

Production sparse/preconditioned/Krylov methods, a complete adaptive-library implementation, arbitrary nonsymmetric eigenvalue conditioning, MCMC and general nonlinear convergence theory remain beyond this introductory boundary. Barycentric/piecewise interpolation and broader regressions remain selective. Graded release, independent scientific/code/accessibility review and measured workload remain open. No endorsement, credit or university equivalence is implied. Original new instruction is CC BY 4.0; source handling is recorded in the source map and repository source/license policy.
