# Physics: Mechanics for Biomedical Engineers review handoff

This handoff targets Physics: Mechanics for Biomedical Engineers, package version 0.5.0. The [review snapshot](PHYSICS_MECHANICS_REVIEW_SNAPSHOT.md) identifies the exact public files. The package remains partial, unreviewed and formative-only; no reviewer or approval is recorded.

## Review scope

- Review the proposed schedule, prerequisites, objective/outcome associations and mathematical level.
- Independently recalculate representative kinematics, force balance, energy, fixed- and variable-mass momentum, impulse, rolling, damping, material response and machine-compliance examples. For the new lesson, check inertial-frame momentum flux, the sign of relative exhaust velocity, the ideal rocket equation and the retained-mass capture contrast.
- Compare the week-10 gravitation reading with the MIT OCW 8.01SC Week 2 gravitation lesson and Week 3 orbital worked example; recalculate the field strengths, orbital speeds and periods, the Kepler radius, potential and orbital energies, the energy to reach orbit and the escape speeds, and confirm that nothing is presented as mission design.
- Check that the centrifuge lesson treats RCF as an acceleration ratio and makes no sedimentation-time, temperature or equipment-operation inference.
- Check the week-11 project guide and its rehearsal: the restated candidates against the CSV (the draft's table now lists candidate C's 0.6 kg disk mass, matching its CSV and reference calculations), the worked single-rotor example, the rehearsal keys and the wording of the five milestone self-checks. Confirm that the guide and rehearsal do not reveal the project's own results.
- Check the compliance lab's dataset link, which now resolves to the package-pinned CSV, and that the project's candidate table is served as a learner resource.
- Check the portfolio's equal-RCF angular-speed calculation, rpm conversion, uniform-disk inertia, rotational energy and point-imbalance force.
- Confirm that all rotor candidates and parameters are explicitly fictional, the model omissions are visible, and no number is presented as a speed setting or equipment safety claim.
- Assess whether the paper-only portfolio complements rather than duplicates the compliance/orientation lab and tendon self-assessment case; check accessibility and likely workload.

## Author-side evidence and its limits

Historical version 0.4.5 records a focused 106-test Mechanics run, including independent rotor recalculation and package snapshot identity. No tests were run for versions 0.4.6 or 0.4.7. Version 0.4.8 added a rotating-frame section without changing any item. For 0.4.9 the Mechanics recalculation file recomputes all 74 numeric keys. The eight new keys are checked against RK4-simulated orbits, with the circular speed found by bisection so that a simulated quarter turn keeps its radius. Potential energy comes from integrating the force to infinity, and the field from differentiating that potential numerically. A further test checks the values stated in the reading. For 0.5.0, a dedicated test recomputes every rehearsal key from its CSV, finding each speed by bisection on ω²r, checks the draft and guide tables against the project CSV, recomputes the guide's worked example and confirms that neither the guide nor the rehearsal states the project's own results. Full-suite results are in the validation report. Version 0.4.7 passed repository content validation (25 packages, 417 lessons, 2,559 questions, 1,420 cards and 25 cases; zero errors and explicit depth warnings), and its new rocket and capture examples were recalculated directly. These author-side checks do not establish independent mechanical review, equipment safety, accessible learner usability, semester workload, student learning or university equivalency. The rotor portfolio draft remains inactive, its optional learner guide is ungraded practice, and no graded course assessments are present.

## Review record to complete only after review

After a review actually occurs, record reviewer name and qualifications, date, package version and archive digest, artifacts examined, concrete findings and disposition. Keep separate decisions for mechanical and mathematical accuracy, instructional design, assessment, accessibility, workload and release. Do not infer approval from the package hash or test results.
