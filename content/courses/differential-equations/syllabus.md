# Differential Equations for Living & Engineered Systems

**Maturity: partial. Version: 0.5.0.**

Build, solve, and interpret first- and second-order differential equations, coupled systems, stability, and numerical integration for biological and robotic dynamics.

## Prerequisites

Calculus I; linear algebra recommended. Structured required, recommended, and concurrent relationships appear in the manifest and remain subject to author review. This package establishes no university prerequisite equivalency.

## Authored outcomes

- Classify ODEs and choose solution methods.
- Interpret equilibria, time constants, and stability.
- Model coupled state variables as a vector system.
- Check numerical solutions against physical constraints.

## Proposed 14-week schedule

This is a proposed sequence, not a measured or reviewed semester. Week 3 now extends the existing forced-response reading with Fourier harmonics for one synthetic periodic input. Week 6 adds Laplace-transform initial-value problems after the constant-coefficient response material, together with a companion reading on impulse response, convolution and transfer functions. Week 9 groups the two related logistic readings—equilibria/harvesting and exact solution/fitting—in one block while keeping their distinct practice. The schedule does not establish weekly workload or semester equivalence.

| Week | Theme | Readings |
|---|---|---|
| 1 | First-order models and time constants | First-order models and time constants |
| 2 | A well-mixed perfused chamber: steady state, time constants and Euler stability | A well-mixed perfused chamber: first-order linear ODEs, steady state, time constants and a numerical check |
| 3 | Forced first-order systems: steps, ramps, periodic inputs and decaying inputs | Forced first-order systems: steps, ramps, periodic inputs and decaying inputs in a perfused chamber |
| 4 | Second-order systems and mechanical response | Second-order systems and mechanical response |
| 5 | Resonance and damping: free decay and forced oscillation | Resonance and damping: free decay and forced oscillation of a spring–mass–damper |
| 6 | Laplace transforms: initial-value problems, impulses, convolution and transfer functions | Laplace transforms for initial-value problems: initial data and delayed steps; Impulse response, convolution and transfer functions |
| 7 | Coupled systems, equilibria and stability | Coupled systems, equilibria, and stability |
| 8 | Phase portraits of linear systems: eigenvalues, eigenvectors and the flow | Phase portraits of linear systems: eigenvalues, eigenvectors and the shape of the flow |
| 9 | Logistic growth: equilibria, harvesting, exact solution and extrapolation | Equilibria and stability: harvesting a logistic population and two coupled compartments; logistic growth: the exact solution, fitting from data and the risk of extrapolating |
| 10 | Nonlinear systems and linearization: a toggle switch and bistability | Nonlinear systems and linearization: a two-gene toggle switch and bistability |
| 11 | Numerical ODEs and error control | Numerical ODEs and error control |
| 12 | Stiff equations and implicit methods | Stiff equations and implicit methods: stability limits of explicit Euler and the Michaelis–Menten depletion time; Stiff project guide (optional, ungraded) |
| 13 | Virtual lab: fitting decay models and testing them beyond the window | Virtual lab 1: fitting decay models to a time course and testing them beyond the window |
| 14 | When a fitted population model predicts negative counts: structure, step size and validation | When a fitted population model predicts negative counts: model structure, extrapolation, step size and validation |

## Assessment and study policy

Every lesson has public formative items (numeric, single-choice, multiple-select, data-interpretation, structured-response and CSV-upload) mapped to its objectives, plus retrieval cards for the review queue; each practice assessment also lists the course outcomes its items assess. Week 13 is a synthetic-data virtual lab and week 14 pairs a lesson on negative predicted counts with the course case and its self-assessment checklist. These are practice activities with unlimited retries and no institutional grade, university credit or transferable credit. Workload has not been measured.

## Optional stiff two-compartment project (ungraded)

The [stiff project guide](assignments/stiff-two-compartment-project-guide.md) makes the project below usable as open practice. It restates the project's system and tasks, works a separate system, and pairs a rehearsal system with open practice items in week 12. Five milestones, suggested for weeks 12–13, are Case studio self-checks whose responses are saved privately and never submitted, collected or scored.

## Inactive integrative project draft

The [stiff two-compartment project](assessment-specs/stiff-two-compartment-project-draft.md) combines an exact coupled-system solution with eigenvalue stability, positivity constraints and explicit-versus-implicit Euler comparisons. It is a mathematical paper draft using normalized synthetic parameters, not an experiment or real-system model. The draft itself is not scheduled, assigned, submitted or graded, and the open project guide above does not submit work to it; mathematical, workload and accessibility review remain necessary.

## Current limitations

The schedule above is proposed, not measured, and has not been reviewed by a qualified instructor. There are no graded homework sets, midterm or final; the optional project guide and its rehearsal are ungraded practice, and the project draft remains inactive. The four former compact readings now have expanded instruction, but workload, assessment, laboratory, and review gaps remain. The package cites no new papers: the lessons teach standard methods with synthetic data, and the typical values they quote (rate constants, damping ratios, step-size rules of thumb) are textbook-level and vary between sources. All populations, chambers, systems and numbers are synthetic; no lesson gives an experimental protocol or parameter values for any real organism, and nothing here says anything about any real culture or device. Qualified human review is required before this course could meet the complete-course standard.

## Sources and licensing

MIT OCW 18.03SC Fall 2011 Unit III is a link-only comparator for Fourier series and Laplace transforms; this addition selects only harmonic response for one periodic forcing example. Read source-map.json for module provenance and content/SOURCES_AND_LICENSES.md for the software/content license boundary. Listed source courses are public curriculum comparators; no affiliation or equivalency is implied.
