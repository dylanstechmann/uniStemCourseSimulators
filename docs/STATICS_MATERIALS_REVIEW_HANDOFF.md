# Statics & Materials course review handoff

This handoff targets Statics & Mechanics of Materials, package version 0.6.0. The [review snapshot](STATICS_MATERIALS_REVIEW_SNAPSHOT.md) identifies the exact public files. The package remains partial, unreviewed and formative-only; no reviewer or approval is recorded.

## Review scope

- Review the proposed sequence, prerequisites, outcome/objective mappings and mathematical level.
- Independently recalculate representative equilibrium, distributed-load reactions, piecewise shear and moment, point-force jumps, axial compatibility/load sharing, torsion, bending, failure, fatigue, buckling, deflection, Weibull and fatigue-lab keys.
- Check the beam draft's simply supported reactions, center-load moment, rectangular section moment, bending-stress and Euler–Bernoulli deflection equations, SI conversions and load-limit formulas.
- Compare the week-7 multiaxial reading with MIT OCW 2.001 Lectures 12–15; recalculate the Poisson and generalized-Hooke strains, volumetric strain, lateral-constraint stress, fully and partly constrained thermal stresses, hoop, axial and spherical stresses and radius growth, and the worked tank thickness and volume change. Confirm that nothing is presented as a pressure rating or design basis.
- Check the week-8 project guide and its rehearsal: the restated beam and candidates against the draft and CSV, the worked example on a separate beam, the rehearsal's section, stress, deflection and limit-load keys, and the wording of the five milestone self-checks. Confirm that the guide and rehearsal do not reveal the project's own results.
- Check the fatigue lab's dataset link, which now resolves to the package-pinned CSV, and that the project's candidate table is served as a learner resource.
- Confirm the two teaching criteria remain separate and arbitrary, and that the comparison is not framed as real component design, structural safety evidence or an implant recommendation.
- Assess how the project fits with the fatigue lab and week-14 scaffold failure case; review accessible alternatives, manual accessibility and likely workload.

## Author-side evidence and its limits

For version 0.4.5, the focused Statics & Materials suite passed 10 tests, including recomputation from the candidate CSV and checks of the inactive project's pass/fail set. That earlier evidence does not cover the 0.4.6 beam-diagram lesson or 0.4.7 compatibility addition; no test suite was run for either increment. For 0.4.8 the shared recalculation registry recomputes every numeric key from closed forms, and a new file checks the eight new keys separately. That file solves the isotropic stiffness relation for strains by Gaussian elimination, finds thermal stresses by bisection on length compatibility, and integrates the pressure over a cut for vessel stresses. A further test checks the values stated in the reading. The release also corrects stale limitation counts. For 0.5.0, a dedicated test recomputes every rehearsal key with exact rational arithmetic in N, mm and MPa, recomputes the guide's worked example and confirms that neither the guide nor the rehearsal states the project's own results. Full-suite results are in the validation report. Author-side checks do not establish independent engineering review, structural safety, accessibility, learner outcomes, semester workload or university equivalency. The project draft is inactive and its optional learner guide is ungraded practice; graded homework, exams and a full laboratory sequence remain absent.

## Review record to complete only after review

After a review actually occurs, record reviewer name and qualifications, date, package version and archive digest, artifacts examined, concrete findings and disposition. Keep separate decisions for mathematical correctness, instructional design, assessment, accessibility, workload and release. Do not infer approval from the package hash or test results.

## Deeper compatibility/material-history target (2026-10-22)

Review target 0.6.0 adds selected indeterminate-beam/energy/settlement/contact and elastic–perfectly plastic unloading/redistribution readings, plus two paper assignments. Check signs, compatibility, unilateral support constraints, constitutive branches, residual equilibrium and work/energy distinctions. All loads/materials are synthetic; no real design or material validation is supplied. Written diagrams, derivations, workload and qualified review remain open. The current snapshot pins the package.
