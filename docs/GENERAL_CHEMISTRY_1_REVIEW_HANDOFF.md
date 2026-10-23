# General Chemistry I course review handoff

This handoff targets General Chemistry I, package version 0.5.0. The [review snapshot](GENERAL_CHEMISTRY_1_REVIEW_SNAPSHOT.md) identifies the exact public files. The package remains partial, unreviewed and formative-only; no reviewer or approval is recorded. The local General Chemistry I/II boundary divides a single 5.111SC comparator and does not claim two independent course equivalents.

## Review scope

- Review the proposed sequence, prerequisites, outcome/objective associations and mathematical level.
- Independently recalculate representative electron-configuration, periodic-trend, stoichiometry, solution, thermochemistry, Lewis/VSEPR, N2/O2 bond-order and magnetic-occupancy, and equilibrium answers. Check that the ten-week calendar preserves stable lesson, question and card IDs and does not imply semester equivalence.
- Compare the week-2 valence-bond reading with MIT OCW 5.111SC Unit II Lecture 14; check the hybrid angles and s-character, the bent-molecule estimates from cos θ = −1/λ², the σ/π counts and the illustrative π-bond enthalpy, and confirm that the stated model limits (O₂ paramagnetism, delocalization, no d-orbital hybrids for main-group atoms) are adequate.
- Check the inactive abstract equilibrium draft's feasible extent interval, conserved-unit bookkeeping, activity convention, `Q/K` direction, quadratic roots, equilibrium amounts and enthalpy sign.
- Confirm that the abstract tokens are clearly distinguished from chemical species and that no handling procedure or biological recommendation is implied.
- Review how the draft complements the existing buffer-calibration lab; assess accessibility, likely workload and chemical accuracy.

## Author-side evidence and its limits

Historical version 0.4.6 records an 87-test focused run for equilibrium and energy calculations. No tests were run for versions 0.4.7 or 0.4.8. Version 0.4.9 restored a VSEPR case without changing any item. For 0.4.10 the General Chemistry I recalculation file recomputes all 72 numeric keys. The eight new keys are checked by building explicit hybrid coefficient vectors and verifying their orthonormality. The bent-molecule s-character comes from bisection on orthogonality, with lone-pair hybrids completed by Gram–Schmidt. σ/π counts are taken from explicit bond lists. A further test checks the values stated in the reading. The full-suite result is in the validation report. Version 0.4.8 passed content validation (25 packages, 417 lessons, 2,575 questions, 1,429 cards and 25 cases; zero errors and explicit depth warnings), and direct MO occupancy arithmetic agrees for N2, O2 and O2+. Objective/assessment report checks and package snapshot verification remain author-side evidence. None establishes independent chemical review, accessibility, learner outcomes, measured workload or course equivalency. The project remains inactive and ungraded; graded homework, exams and a laboratory sequence remain absent.

## Review record to complete only after review

After a review actually occurs, record reviewer name and qualifications, date, package version and archive digest, artifacts examined, concrete findings and disposition. Keep separate decisions for chemical accuracy, instructional design, assessment, accessibility, workload and release. Do not infer approval from the package hash or test results.

## Open project route (2026-10-22)

The current guide, separate worked example, rehearsal and five private milestone self-checks make the existing project usable as ungraded practice. [The route regression tests](../tests/content/test_remaining_course_project_routes.py) independently recalculate every new numeric field and exercise the backend grader, including exact counts and continuous-quantity precision. Review the written explanation, evidence limits and proposed workload independently; automated arithmetic is not subject review. Historical snapshot evidence remains preserved.

## Electronic and coupled-ledger target (2026-10-22)

Target 0.6.0 adds two foundations and four reports. Check one-electron energies, radial normalization/mode/mean/cumulative measure and node/state counts; nonorthogonal amplitude normalization, projected energies, phase conventions and particle-matched occupancy references; physical reaction-extent roots, dimensionless pressure quotient and rigid-vessel internal-energy versus enthalpy boundaries; reference-calibrated two-component spectral reconstruction and a distinct cumulative gas ledger. These are synthetic models, not measured spectra, dissociation energies or laboratory validation. Fourteen scheduled blocks and selected checkpoints establish neither full-report quality nor measured workload. Qualified review remains open.
