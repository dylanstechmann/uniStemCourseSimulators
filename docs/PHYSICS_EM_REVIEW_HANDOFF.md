# Physics: Electricity & Magnetism course review handoff

This handoff targets Physics: Electricity & Magnetism, package version 0.6.0. The [review snapshot](PHYSICS_EM_REVIEW_SNAPSHOT.md) identifies the exact public files. The package remains partial, unreviewed and formative-only; no reviewer or approval is recorded.

## Review scope

- Review the proposed schedule, prerequisites, objective/outcome associations and mathematical level.
- Independently recalculate representative field/potential, capacitance, dielectric energy, Kirchhoff/Thevenin, RC/RL, magnetic induction, electrode-loading, phasor and virtual-lab work.
- Independently recalculate displacement current and inside/outside capacitor magnetic fields, and check peak-versus-average Poynting flux and plane-wave energy density assumptions.
- Independently recalculate path/phase conditions, equal-source interference intensity and far-field fringe spacing/positions, including the stated coherence and small-angle assumptions.
- Compare the week-8 field-sources reading with MIT OCW 8.02 sessions 14–19; independently recalculate the loop and segment fields, Ampère's-law results inside a thick wire, in a toroid and between parallel wires, and the dipole moment, torque, turning work and far-field comparison.
- Check the new portfolio's resonant frequency, quality factor, bandwidth, half-power roots, lead/lag sign, peak/RMS distinction, average resistor power and electric/magnetic energy comparison.
- Examine whether the ideal series-RLC assumptions and fictional selection limits are clear and appropriately scoped.
- Confirm that the draft complements the calibration/loading lab and recording case without implying a real instrument design, biological measurement or device-safety claim.
- Review notation, accessible alternatives, manual accessibility and likely weekly workload.

## Author-side evidence and its limits

For version 0.4.5, the focused Physics E&M suite passed 114 tests, including independent recomputation of the RLC portfolio and package snapshot identity. That historical suite does not cover the 0.4.6 Maxwell or 0.4.7 interference lessons; no test suite was run for either increment. For 0.4.8 the Physics E&M recalculation file recomputes all 82 numeric keys. The eight new keys use numerical Biot–Savart summation over discretized paths, Ampère's law with the enclosed current integrated over the cross-section, and torque summed as r × (I dl × B) around a tilted loop; turning work integrates that torque over angle. A further test checks the values stated in the reading. The full-suite result is in the validation report. These are author-side checks and do not establish independent physics review, accessible learner usability, semester workload, student learning or university equivalency. Graded homework, exams and a complete laboratory sequence remain absent; the project is inactive and ungraded.

For 0.5.0, [the project-route tests](../tests/content/test_physics_em_project_route.py) recompute all 13 numeric rehearsal answers, solve the half-power reactance conditions by bisection instead of the guide's quadratic formula, check selection and phase reasoning, and recompute the worked example. The calculated responses must earn credit at the three significant figures requested in the prompts; both tie-breaking conventions are accepted for the exact halfway reactance. Route checks cover the guide, rehearsal, ungraded milestones and package-pinned lab resource. The full-suite result is in the validation report. These checks were written and run by an AI coding agent; they do not establish independent subject review or an owner walkthrough.

## Review record to complete only after review

After a review actually occurs, record reviewer name and qualifications, date, package version and archive digest, artifacts examined, concrete findings and disposition. Keep separate decisions for mathematical and physical correctness, instructional design, assessment, accessibility, workload and release. Do not infer approval from the package hash or test results.

## Field/induction/wave-boundary target (2026-10-22)

Current target 0.6.0 adds three foundations, four reports and twenty checkpoints/cards. Check continuous cylindrical charge integration, finite potential references, induced conductor signs and field-versus-charge energy integrals; mutual-inductance passivity, complete reference reversals and signed source/storage/loss; mechanical induction power; current-sheet jump/outgoing signs, retarded time and two outward normals; perfect-reflection standing energy, flux and momentum; and isolated capacitor charge/dissipation. The wave packet states consistent rounded constants. Code/diagrams/reports, broader theory/coursework, experimental competence, equipment validity, workload and qualified review remain open. Earlier evidence above is historical; the current snapshot pins the new target.
