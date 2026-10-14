# Cellular Biomechanics course review handoff

This handoff targets Cellular Biomechanics & Mechanobiology, package version 0.3.9. The [review snapshot](CELLULAR_BIOMECHANICS_REVIEW_SNAPSHOT.md) identifies the exact public files. The package remains partial, unreviewed and formative-only; no reviewer or approval is recorded.

## Review scope

- Review the proposed schedule, prerequisites, objective/outcome associations and quantitative level.
- Independently recalculate representative stress/strain, indentation, relaxation, rheology, traction, force-clutch, dose-response and factorial-design work.
- Compare the week-5 filament-mechanics reading with MIT OCW 20.310J sessions 2 and 19; recalculate persistence lengths, tangent correlations, worm-like-chain sizes, entropic spring constants, Marko–Siggia forces, Euler buckling loads and lengths, and bundle factors, and confirm that actin-like and microtubule-like values are labelled synthetic.
- Recalculate the size-scaling example, diffusivity conversion and 1.5 mm prediction; assess whether the fixed-shape/boundary-condition assumptions, independent-unit treatment and model-identifiability limits are clear.
- Check the new portfolio's instantaneous and equilibrium moduli, step-relaxation stress, frequency-dependent storage/loss moduli, loss tangent, threshold selection and dissipated energy density, including unit conversions.
- Examine the single-relaxation-time, linear-response assumptions and whether the stated model checks are appropriately scoped.
- Confirm that the project complements rather than duplicates the stiffness/ligand-density virtual lab and case, and that none of its synthetic model candidates are presented as measured materials or predictors of cell behavior.
- Review notation, accessible alternatives, manual accessibility and likely weekly workload.

## Author-side evidence and its limits

The focused Cellular Biomechanics suite passed 8 tests for version 0.3.6, including independent recomputation of the viscoelastic portfolio and package snapshot identity. No tests were run for 0.3.7. Version 0.3.8 changed only number formatting. For 0.3.9 the shared registry checks every numeric key from closed forms. A new file checks the eight new keys separately. ⟨R²⟩ comes from integrating the tangent correlation along the contour, and buckling loads and lengths from a shooting method on κy″ + Fy = 0. The worm-like-chain force comes from inverting the extension. A further test checks the values stated in the reading. The full-suite result is in the validation report. Current author-side checks for 0.3.7 include repository content validation (25 courses, 418 lessons, 2,583 questions, 1,433 cards and 25 cases; zero errors or explicit depth warnings), direct recalculation of the new L-squared scaling and unit conversion, refreshed objective/candidate reports, and the current package digest. These are author-side checks; they do not establish independent mechanical review, accessible learner usability, semester workload, student learning or university equivalency. Graded homework, exams and a full laboratory sequence remain absent; the project is inactive and ungraded.

## Review record to complete only after review

After a review actually occurs, record reviewer name and qualifications, date, package version and archive digest, artifacts examined, concrete findings and disposition. Keep separate decisions for mathematical and mechanical correctness, instructional design, assessment, accessibility, workload and release. Do not infer approval from the package hash or test results.
