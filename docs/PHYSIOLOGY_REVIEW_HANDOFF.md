# Human Physiology for Engineers review handoff

This handoff targets Human Physiology for Engineers, package version 0.6.0. The [review snapshot](PHYSIOLOGY_REVIEW_SNAPSHOT.md) identifies the exact public files. The package remains partial, unreviewed and formative-only; no reviewer or approval is recorded.

## Review scope

- Review the proposed schedule, prerequisites, objective/outcome associations and mathematical level.
- Compare the new cardiac pressure-volume treatment with MIT OCW HST.542J Spring 2004 undergraduate calendar topics on cardiovascular models and the heart as a pump.
- Independently recalculate the synthetic loop values: EDV 120 mL, ESV 50 mL gives SV 70 mL and 0.933 J/beat at 100 mmHg mean ejection pressure; the stipulated 120 mmHg, ESV 70 mL perturbation gives SV 50 mL and 0.800 J/beat. Verify the 1.33322×10⁻⁴ J per mmHg·mL conversion and the fixed-rate cardiac-output changes.
- Confirm that the rectangular estimate is clearly separated from a measured PV-loop integral and is not presented as a clinical estimate, universal afterload response or patient-specific prediction.
- Independently recalculate representative membrane, transport, pressure-flow, Fick-principle, renal-clearance, wound-closure lab and compensation/reserve examples.
- Check the week-4 passive membrane and cable reading: membrane time constant, input resistance, length constant and conduction-velocity scaling.
- Check the week-3 Hodgkin–Huxley reading: the membrane equation, the voltage-clamp argument, gating steady states and time constants, conductances from n⁴ and m³h, and whether the simulated threshold, spike-shape and refractory numbers are presented as model outputs rather than measurements. The classic parameter values were not checked against the scanned 1952 paper.
- Check the new ledger's units, reference-marker clearance, filtered-load and excretion arithmetic, net transport classifications, fractional excretion, and idealized glucose transport maximum.
- Confirm that all measurements are explicitly synthetic, assumptions are stated, and no clinical interpretation, test protocol or treatment advice is implied.
- Assess whether the paper-only ledger complements rather than duplicates the scratch-assay virtual lab and compensation/reserve case; check accessibility and likely workload.

## Author-side evidence and its limits

For package version 0.4.6, the focused Physiology suite passed 8 tests, including independent recomputation of the renal-clearance ledger and package snapshot identity. No test suite was run for 0.4.7 at the user's direction. For version 0.4.9, a dedicated test recomputes every new Hodgkin–Huxley key by integrating the gating equations and re-runs the full model to check each stated spike, threshold and refractory number; run results are recorded in [VALIDATION_REPORT.md](VALIDATION_REPORT.md). The prior results do not apply to the new pressure-volume material and do not establish independent scientific review, clinical suitability, accessible learner usability, semester workload, student learning or university equivalency. The renal-clearance project remains an inactive draft, and no graded course assessments are present.

## Review record to complete only after review

After a review actually occurs, record reviewer name and qualifications, date, package version and archive digest, artifacts examined, concrete findings and disposition. Keep separate decisions for scientific and mathematical accuracy, instructional design, assessment, accessibility, workload and release. Do not infer approval from the package hash or test results.

## Open project route (2026-10-22)

The current guide, separate worked example, rehearsal and five private milestone self-checks make the existing project usable as ungraded practice. [The route regression tests](../tests/content/test_remaining_course_project_routes.py) independently recalculate every new numeric field and exercise the backend grader, including exact counts and continuous-quantity precision. Review the written explanation, evidence limits and proposed workload independently; automated arithmetic is not subject review. Historical snapshot evidence remains preserved.

## Organ-system and feedback target (2026-10-22)

Current target 0.6.0 adds three foundations, four connected reports and twenty checkpoints/cards. Check delivered-fraction serial amount/water ledgers and unit conversions; qualitative segment transport and medullary-gradient/permeability distinction; scaled two-state feedback signs, initial derivatives, eigenmodes, target clipping and separate bias; nonlinear oxygen-content mixing, resistance boundary conditions, delivery versus uptake and equivalent-fraction nonidentifiability. Check the corrected right-hand n^4 slope at nonzero n0. New parameters are invented, not calibrated physiological estimates. Solver/report evaluation, broader organ depth, experimental competence, workload and qualified review remain open. Existing evidence above is historical; the current snapshot pins the new target.
