# Thermodynamics & Transport review handoff

This handoff targets Thermodynamics & Transport package version 0.7.0. The [review snapshot](TRANSPORT_REVIEW_SNAPSHOT.md) identifies the exact public files. The course remains partial, unreviewed and formative-only; no reviewer or approval is recorded.

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

## Deeper thermodynamics/transport target (2026-10-22)

Version 0.6.0 added phase/activity and local-stability derivations, ion/coupled/osmotic ledgers and conservative finite-volume geometry, with three connected assignments. Check transfer signs, standard states, concentration bases, equilibrium-versus-rate claims, boundary distances, positivity conditions and conservation/refinement evidence. Automated checkpoints do not evaluate learner code or written reasoning; workload and qualified review remain open. The current snapshot pins the exact package.

## Second-comparator target (2026-10-28)

Current target 0.7.0 adds the [scope crosswalk](../content/courses/transport/scope-crosswalk.md) against MIT OCW 20.110J Fall 2005 and Open Yale Courses PHYS 200, and a week-1 reading on the closed-system first law, ideal-gas processes and reversible versus irreversible expansion (three objectives, 13 items, four cards). Check whether the crosswalk's labels are fair, given that it compares lecture titles, with Yale overviews and chapter titles read for Lectures 20–24, that 20.110J is a physical-chemistry style course on biomolecular systems, and that PHYS 200 is an introductory physics course. In the reading, check the state-function and path-function distinction, the sign convention ΔU = Q − W against the control-volume lesson, the ideal-gas heat capacities and γ, the isothermal and reversible adiabatic results (137.0 J, 144.2 K, 97.1 J, 19.98 kPa), the constant-pressure and constant-volume heats, the irreversible-expansion work and entropy-generation numbers (83.1 J, 0.2771 J/K, 0.1796 J/K, 53.9 J), and the syringe worked example. [The recalculation registry](../tests/content/test_ai_assisted_checks.py) recomputes the ten new numeric keys from closed forms, and [the lesson test](../tests/content/test_transport_closed_system_first_law_lesson.py) recomputes every number the reading states by quadrature of P dV, an RK4 integration of the adiabat, an entropy integral and a staged expansion that approaches the reversible work. Heat engines and the Carnot cycle, thermochemistry, the Joule–Thomson experiment, statistical thermodynamics, single-component phase equilibria, solvation and the Debye length remain recorded gaps. Workload and qualified review remain open.
