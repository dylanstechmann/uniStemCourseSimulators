# Differential Equations for Living & Engineered Systems

**Maturity: partial. Version: 0.7.0.**

Build, solve, and interpret first- and second-order differential equations, coupled systems, stability, and numerical integration for biological and robotic dynamics. See the [scope crosswalk](scope-crosswalk.md) for the comparison with MIT OCW 18.03SC and Harvard Math 21b.

## Prerequisites

Calculus I; linear algebra recommended. Structured required, recommended, and concurrent relationships appear in the manifest and remain subject to author review. This package establishes no university prerequisite equivalency.

## Authored outcomes

- Classify ODEs and choose solution methods.
- Interpret equilibria, time constants, and stability.
- Model coupled state variables as a vector system.
- Check numerical solutions against physical constraints.

## Proposed 14-week schedule

This is a proposed sequence, not a measured or reviewed semester. Week 4 adds forced linear equations (exponential response, complex replacement and undetermined coefficients) between the characteristic equation and the resonance lesson. Week 3 now extends the existing forced-response reading with Fourier harmonics for one synthetic periodic input. Week 6 adds Laplace-transform initial-value problems after the constant-coefficient response material, together with a companion reading on impulse response, convolution and transfer functions. Week 9 groups the two related logistic readings—equilibria/harvesting and exact solution/fitting—in one block while keeping their distinct practice. The schedule does not establish weekly workload or semester equivalence.

| Week | Readings and activities |
| --- | --- |
| 1 | [First-order models and time constants](modules/01-first-order-models-and-time-constants.md) |
| 2 | [A well-mixed perfused chamber: first-order linear ODEs, steady state, time constants and a numerical check](modules/05-well-mixed-chamber-and-euler-stability.md); [Initial-value problems, variable coefficients and intervals](modules/initial-value-problems-and-variable-coefficients.md) |
| 3 | [Forced first-order systems: steps, ramps, periodic inputs and decaying inputs in a perfused chamber](modules/07-forced-first-order-systems-in-a-perfused-chamber.md); [Assignment 1: methods, domains and IVP evidence](assignments/coursework-01-initial-value-domains.md) |
| 4 | [Second-order systems and mechanical response](modules/02-second-order-systems-and-mechanical-response.md); [Forced linear equations: exponential response, complex replacement and undetermined coefficients](modules/23-forced-linear-equations-exponential-response-and-undetermined-coefficients.md) |
| 5 | [Resonance and damping: free decay and forced oscillation of a spring–mass–damper](modules/08-resonance-and-damping-of-a-spring-mass-damper.md) |
| 6 | [Laplace transforms for initial-value problems: initial data and delayed steps](modules/14-laplace-transform-initial-value-problems.md); [Impulse response, convolution and transfer functions](modules/15-impulse-response-convolution-and-transfer-functions.md); [Fourier filtering and truncation evidence](modules/fourier-filtering-and-error-bounds.md) |
| 7 | [Coupled systems, equilibria, and stability](modules/03-coupled-systems-equilibria-and-stability.md); [Assignment 2: forcing, resonance and error budgets](assignments/coursework-02-forcing-and-response.md) |
| 8 | [Phase portraits of linear systems: eigenvalues, eigenvectors and the shape of the flow](modules/09-phase-portraits-of-linear-systems.md); [Assignment 3: coupled forcing and conservation](assignments/coursework-03-coupled-system-evidence.md) |
| 9 | [Equilibria and stability: harvesting a logistic population and two coupled compartments](modules/06-equilibria-stability-and-coupled-compartments.md); [Logistic growth: the exact solution, fitting from data and the risk of extrapolating](modules/10-logistic-growth-solution-fitting-and-extrapolation.md) |
| 10 | [Nonlinear systems and linearization: a two-gene toggle switch and bistability](modules/11-linearization-and-bistability-in-a-toggle-switch.md); [Nonlinear radius and invariant cycles](modules/nonlinear-radius-and-limit-cycles.md) |
| 11 | [Numerical ODEs and error control](modules/04-numerical-odes-and-error-control.md) |
| 12 | [Stiff equations and implicit methods: stability limits of explicit Euler and the Michaelis–Menten depletion time](modules/12-stiff-equations-and-implicit-methods.md); [Stiff project guide: one coupled system from its exact solution to its numerical behavior (optional, ungraded)](assignments/stiff-two-compartment-project-guide.md) |
| 13 | [Virtual lab 1: fitting decay models to a time course and testing them beyond the window](labs/01-fitting-decay-models-and-testing-them-beyond-the-window.md) |
| 14 | [When a fitted population model predicts negative counts: model structure, extrapolation, step size and validation](modules/13-negative-counts-model-structure-step-size-and-validation.md); [Assignment 4: nonlinear and numerical claims](assignments/coursework-04-nonlinear-and-numerical-claims.md) |

## Assessment and study policy

Current inventory: 25 reading/activity routes, 152 public practice items, 86 retrieval cards and six Case studio prompts. These counts do not establish semester depth.

Every lesson has public formative items (numeric, single-choice, multiple-select, data-interpretation, structured-response and CSV-upload) mapped to its objectives, plus retrieval cards for the review queue; each practice assessment also lists the course outcomes its items assess. Week 13 is a synthetic-data virtual lab and week 14 pairs a lesson on negative predicted counts with the course case and its self-assessment checklist. These are practice activities with unlimited retries and no institutional grade, university credit or transferable credit. Workload has not been measured.

## Connected coursework (open, ungraded)

Four original reports require method/domain/nonuniqueness evidence (week 3), resonant/impulse responses and harmonic/transient error budgets (week 7), repeated-mode forced and conserved transfer systems (week 8), and nonlinear cycle/zero-parameter/numerical claims (week 14). Foundations in weeks 2, 6 and 10 supply the additional derivations. Retain code, proofs, plots and reports locally; browser checkpoints evaluate selected outputs and interpretations. The existing fitting lab and stiff project remain available. Workload and qualified review are open.

## Optional stiff two-compartment project (ungraded)

The [stiff project guide](assignments/stiff-two-compartment-project-guide.md) makes the project below usable as open practice. It restates the project's system and tasks, works a separate system, and pairs a rehearsal system with open practice items in week 12. Five milestones, suggested for weeks 12–13, are Case studio self-checks whose responses can be saved privately and are not submitted for grading.

## Inactive integrative project draft

The [stiff two-compartment project](assessment-specs/stiff-two-compartment-project-draft.md) combines an exact coupled-system solution with eigenvalue stability, positivity constraints and explicit-versus-implicit Euler comparisons. It is a mathematical paper draft using normalized synthetic parameters, not an experiment or real-system model. The draft itself is not scheduled, assigned, submitted or graded, and the open project guide above does not submit work to it; mathematical, workload and accessibility review remain necessary.

## Current limitations

The schedule above is proposed, not measured, and has not been reviewed by a qualified instructor. There are no graded homework sets, midterm or final; the optional project guide and its rehearsal are ungraded practice, and the project draft remains inactive. The four former compact readings now have expanded instruction, but workload, assessment, laboratory, and review gaps remain. The package cites no new papers: the lessons teach standard methods with synthetic data, and the typical values they quote (rate constants, damping ratios, step-size rules of thumb) are textbook-level and vary between sources. All populations, chambers, systems and numbers are synthetic; no lesson gives an experimental protocol or parameter values for any real organism, and nothing here says anything about any real culture or device. Qualified human review is required before this course could meet the complete-course standard.

## Sources and licensing

MIT OCW 18.03SC Fall 2011 Unit III is a link-only comparator for Fourier series and Laplace transforms; this addition selects only harmonic response for one periodic forcing example. Read source-map.json for module provenance and content/SOURCES_AND_LICENSES.md for the software/content license boundary. Listed source courses are public curriculum comparators; no affiliation or equivalency is implied.

The 0.6.0 expansion compares actual first-order, forced-response, transform and nonlinear readings with [MIT OCW 18.03SC Fall 2011 syllabus](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/syllabus/syllabus/) and its four units. It develops variable-coefficient integrating factors and local/global IVP distinctions; square-input filtering, phase and uniform output-tail certificates; and an exactly reducible nonlinear cycle with a nonhyperbolic boundary. Four reports integrate those with existing methods. The comparator has a broader problem-set/exam sequence; its workload expectation is not assigned to this local package. Local Calculus I/linear-algebra preparation differs from the source course’s multivariable corequisite. General existence proofs, broad Fourier/bifurcation/chaos theory, PDEs and boundary-value theory remain outside this selected scope. All new text/problems are original and AI-assisted; no source assets were imported.

The 0.7.0 second-comparator pass adds the [Harvard Math 21b Spring 2015 syllabus](https://people.math.harvard.edu/archive/21b_spring_15/syllabus.html) (link-only) beside 18.03SC. Its lecture on inhomogeneous differential equations and 18.03SC Unit II's exponential-response, undetermined-coefficients, linear-operator and pure-resonance sessions identified a general method for forced linear equations as a topic both courses teach and this package lacked; the new week-4 reading closes that gap and also introduces Euler's formula, which Unit I's complex-arithmetic sessions teach. Partial differential equations, named only by Harvard 21b, remain a recorded gap. The [scope crosswalk](scope-crosswalk.md) records the comparison as an AI-assisted, unreviewed analysis of titles, not of lecture content or assessment. No source prose, handout, figure or problem is imported.
