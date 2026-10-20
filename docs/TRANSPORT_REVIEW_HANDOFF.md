# Thermodynamics & Transport review handoff

This handoff targets Thermodynamics & Transport package version 0.5.0. The [review snapshot](TRANSPORT_REVIEW_SNAPSHOT.md) identifies the exact public files. The course remains partial, unreviewed and formative-only; no reviewer or approval is recorded.

## Review scope

- Review the proposed 14-week undergraduate scope, its prerequisite expectations and placement of the new reading after the control-volume and entropy treatments.
- Recalculate ΔrG°=−RT ln K, ΔrG=RT ln(Q/K), and the A⇌B equilibrium composition using the stated dimensionless activities and concentration standard.
- Check that the sign of ΔrG is interpreted as a thermodynamic direction and that K is kept distinct from a rate constant.
- Assess whether the ideal-dilute, closed-batch, fixed-temperature and no-side-reaction assumptions are visible enough for engineering students.
- Compare the bounded local treatment with MIT OCW 20.110J Fall 2005 sessions 8–12; phase equilibrium, nonideal solutions and broader biomolecular thermodynamics remain outside the lesson.
- Check the week-10 energy-balance reading against MIT OCW 20.330J sessions L7–L8: recalculate stream heating, hydrostatic feed pressure, efflux speed, constriction pressure drop, Poiseuille losses, Reynolds numbers, pump power and viscous heating, and confirm that Bernoulli's validity limits and the first-law sign convention are clear.
- Check the week-13 slab project guide and its rehearsal: the restated slab and conditions against the draft, the worked example on a separate slab with Bi = 1.0, the rehearsal's profile, temperature, average and Biot keys, and the wording of the five milestone self-checks. Confirm that the guide and rehearsal do not reveal the project's own results, and that the oxygen-profile lab's dataset link now resolves to the package-pinned CSV.
- Recalculate representative diffusion/reaction, pressure-drop, oxygen-limit, heat-transfer and entropy-balance work elsewhere in the course.

## Author-side evidence and its limits

Repository content validation passed for 25 packages, 422 lessons, 2,627 questions, 1,453 cards and 25 cases with zero errors or explicit depth warnings. The example was independently recalculated: at 298 K, K=4 gives ΔrG°≈−3.43 kJ/mol; Q=0.20 gives ΔrG≈−7.43 kJ/mol; a closed 1.20 mM A+B batch has equilibrium concentrations 0.24 mM A and 0.96 mM B. The package digest matches the snapshot. No test suite was run for 0.4.7. These checks are not independent thermodynamic review, measured workload, accessible usability or course-equivalence evidence. For 0.5.0 a dedicated test recomputes every rehearsal key from an exact rational finite-difference solution of the slab equation, with an Euler–Maclaurin-corrected average, rather than from the closed form used to author them; it also recomputes the guide's worked example and checks that the guide and rehearsal do not state the project's results.

For 0.4.9 the shared registry checks every numeric key from closed forms, and a new file checks the eight new energy-balance keys separately. It uses a free-fall simulation for efflux speed and integrates dP = −ρv dv across a constriction. Laminar losses come from integrating the parabolic profile and bisecting for the pressure drop. A further test checks the values stated in the reading. The full-suite result is in the validation report.

## Review record to complete only after review

After an actual review, record reviewer qualifications, date, exact package version and archive digest, artifacts examined, specific findings and disposition. Keep separate decisions for scientific correctness, instructional design, assessment, accessibility, workload and release. A matching hash is an identity check, not approval.
