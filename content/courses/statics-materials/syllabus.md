# Statics & Mechanics of Materials

**Maturity: partial. Version: 0.6.0.**

Equilibrium, internal loads, deformation and selected material/failure models with explicit boundary conditions and synthetic structures.

## Prerequisites

Physics: Mechanics; Calculus I. Structured required, recommended, and concurrent relationships appear in the manifest and remain subject to author review. This package establishes no university prerequisite equivalency.

## Authored outcomes

- Solve force and moment equilibrium.
- Compute axial, torsional, and bending stress.
- Relate material response to boundary conditions.
- Use safety factors with an explicit failure criterion.

## Proposed 14-week schedule

This is a proposed scope, not a measured or reviewed semester. Each week lists its readings. The opening week groups free-body diagrams with a short body-equilibrium application; week 2 develops beam loading, shear and bending moment before stress; week 3 now pairs axial stress and extension with an introductory redundant-member compatibility example; week 7 pairs stress transformation with multiaxial Hooke's law, thermal strain and thin-walled pressure vessels. All four compact prototype readings in weeks 1, 3, 4 and 8 now have expanded instruction, and every lesson has public formative items and retrieval cards.

| Week | Readings and activities |
| --- | --- |
| 1 | [Free-body diagrams and equilibrium](modules/01-free-body-diagrams-and-equilibrium.md); [Force and moment equilibrium in the body: free-body diagrams of a forearm holding a load](modules/06-forearm-free-body-equilibrium.md) |
| 2 | [Distributed loads, shear force, and bending moment](modules/14-distributed-loads-shear-and-moment.md) |
| 3 | [Axial load, stress, strain, and compatibility](modules/02-axial-load-stress-and-strain.md) |
| 4 | [Torsion and bending](modules/03-torsion-and-bending.md) |
| 5 | [Bending of a long bone: second moment of area, combined stresses and why bones are hollow](modules/05-bending-of-a-long-bone.md) |
| 6 | [Beam deflection and stiffness: three-point bending, superposition and what the span and thickness control](modules/11-beam-deflection-and-flexural-modulus.md); [Indeterminate beams, energy compatibility and support contact](modules/indeterminate-beams-and-contact.md) |
| 7 | [Combined stress: principal stresses, Mohr's circle and yield criteria](modules/10-principal-stresses-mohrs-circle-and-yield.md); [Multiaxial Hooke's law, thermal strain and thin-walled pressure vessels](modules/15-multiaxial-hookes-law-thermal-strain-and-pressure-vessels.md) |
| 8 | [Failure criteria, fatigue, and design margins](modules/04-failure-criteria-fatigue-and-design-margins.md); [Beam project guide: strength and stiffness of three synthetic sections (optional, ungraded)](assignments/beam-strength-and-stiffness-project-guide.md); [Constitutive history, plastic set and load redistribution](modules/plasticity-unloading-and-redistribution.md) |
| 9 | [Stress concentrations: holes, notches and why the nominal stress is not the stress that fails a part](modules/07-stress-concentrations-holes-and-notches.md); [Assignment 1: redundant-support compatibility and contact](assignments/coursework-01-support-compatibility.md) |
| 10 | [Buckling of slender struts: Euler's critical load, effective length and slenderness](modules/09-buckling-of-slender-struts.md) |
| 11 | [Fatigue under cyclic loading: S–N curves, Basquin's law, mean stress and cumulative damage](modules/08-fatigue-sn-curves-and-cumulative-damage.md) |
| 12 | [Virtual lab 1: fatigue lives, scatter and run-outs](labs/01-fatigue-lives-scatter-and-run-outs.md) |
| 13 | [Strength of brittle materials: flaws, scatter and the Weibull distribution](modules/12-weibull-strength-and-the-size-effect.md) |
| 14 | [Why a scaffold that meets its strength target can still collapse: a failure analysis and an accelerated test plan](modules/13-cyclic-perfusion-failure-analysis-and-test-plan.md); [Assignment 2: material history and residual-load report](assignments/coursework-02-material-history.md) |

## Assessment and study policy

Every topic lesson has public formative items (numeric, single-choice, multiple-select, data-interpretation, structured-response and CSV-upload) mapped to its objectives, plus retrieval cards for the review queue; each practice assessment also lists the course outcomes its items assess. Week 12 is a synthetic-data virtual lab and week 14 pairs a failure-analysis lesson with the course case and its self-assessment checklist. These are practice activities with unlimited retries and no institutional grade, university credit or transferable credit. Workload has not been measured.

## Connected paper coursework (open, ungraded)

Week 9 adds a redundant-support compatibility/contact report; week 14 adds a material-history and residual-load report. Each supplies distinct synthetic inputs, derivation tasks, independent checks and self-review values. Browser checkpoints do not evaluate written derivations, free-body diagrams, code or a real structural/material assessment. The 14-block proposal and workload remain unmeasured and unreviewed.

## Optional beam strength-and-stiffness project (ungraded)

The [beam project guide](assignments/beam-strength-and-stiffness-project-guide.md) makes the project below usable as open practice. It restates the project's beam, candidates and tasks, works a separate synthetic beam, and pairs two rehearsal candidates with open practice items in week 8. Five milestones, suggested for weeks 8–9, are Case studio self-checks whose responses can be saved privately and are not submitted for grading.

## Inactive integrative project draft

The [simply supported beam portfolio](assessment-specs/beam-strength-and-stiffness-project-draft.md) combines equilibrium, bending stress, elastic deflection and separate strength/stiffness limits across three synthetic candidates. It is a paper exercise, not a component design or safety basis; the draft itself is not scheduled, assigned, submitted or graded, and the open project guide above does not submit work to it.

## Current limitations

The schedule above is proposed, not measured, and has not been reviewed by a qualified instructor. There are no graded homework sets, midterm or final; the optional project guide and its rehearsal are ungraded practice, and the project draft remains inactive. The beam sequence now develops distributed loads, cut-section equilibrium, shear and moment diagrams before stress; week 3 introduces compatibility with one parallel-bar example, and the new beam reading develops a propped cantilever through compatibility, energy, settlement and contact. The new material-history reading develops selected unloading, plastic set and parallel-member redistribution; broader truss/frame and nonlinear beam analysis remain thin. Two new paper assignments require independent support/contact and constitutive-history reports. A broader coursework and laboratory sequence remains unfinished. The lessons teach standard models with synthetic data, and the typical values they quote (moduli, strengths, fatigue and fracture constants, heat capacities) are textbook-level and vary between sources. All loads, materials, specimens and numbers are synthetic; no lesson gives a design basis, test protocol or safety advice, and nothing here says anything about any real device, implant or person. Qualified human review is required before this course could meet the complete-course standard.

## Sources and licensing

MIT OpenCourseWare, **2.001 Mechanics & Materials I**, Fall 2006, is a link-only curriculum comparator. Its course description frames mechanics through geometry/compatibility, forces and material response; the syllabus and readings include force-deformation, static indeterminacy, truss deformation and indeterminate beams. The local sequence now extends the earlier parallel-elastic-bar example with selected indeterminate-beam/energy/contact and elastic–perfectly plastic history models. The reading does not copy or adapt MIT notes, figures, problems or other assets. See source-map.json for exact links and provenance; no affiliation or equivalency is implied.

Current inventory: 21 reading/activity routes, 128 public practice items and 75 retrieval cards. Counts do not establish semester depth. This personal hobby and learning project uses substantial AI assistance; no qualified approval or owner walkthrough is inferred.
