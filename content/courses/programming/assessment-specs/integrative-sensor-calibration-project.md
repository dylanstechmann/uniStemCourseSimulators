# Integrative project draft: reproducible sensor-calibration pipeline

**Inactive authoring draft for Programming & Numerical Methods for Bioengineering 0.4.6.** This proposal is not a scheduled assignment, does not collect submissions, and carries no points or course grade. The course does not execute learner code. Human review, workload measurement, accessibility review, delivery policy and activation decisions are all outstanding.

## Project brief

Build a small, reproducible analysis repository that calibrates a synthetic sensor on four training batches and tests transfer to two held-out batches. Use the public [synthetic records](sensor-calibration-records.csv) and their [deterministic generator](generate_sensor_calibration_records.py). The values exercise code and statistical reasoning; they describe no real instrument, biological sample or clinical measurement.

The exercise integrates the course outcomes: modular functions with explicit contracts; numerical fitting and error checks; a validation split aligned with the new-batch prediction target; and a labelled, reproducible report. The model is deliberately simple: `signal_mV = intercept_mV + slope_mV_per_mM * standard_mM`. Batch offsets make it possible for a calibration to fit training data and still transfer poorly to a new batch.

## Data and split rules

The file has five known standards (0, 0.5, 1, 2 and 4 mM), three replicate readings at each level, and six batches, for 90 rows. Batches B01–B04 are training data; B05–B06 are held out by batch. `signal_mV` is generated as `20 + 3 * standard_mM + batch_offset_mV + replicate_offset_mV`, with batch offsets −1, 0, 0, 1, 4 and −3 mV respectively and replicate offsets −0.2, 0 and +0.2 mV. The deterministic rule keeps the synthetic model and data independently inspectable.

Fit the calibration only on rows marked `train`. Keep the whole batch together when evaluating transfer; a random row split answers a different question because it places measurements from a known batch on both sides. Report residual sign as `observed − predicted`, state each metric's denominator and units, and show results for B05 and B06 separately. Do not add batch identifiers as predictive inputs for unseen batches.

## Milestones and deliverables

1. **Contract and provenance:** implement a pure reader that checks required columns, unique record IDs, finite numeric values, the declared units and allowed split labels. Test malformed and non-finite rows through mutated fixtures; preserve each rejected row and its reason.
2. **Calibration function:** fit intercept and slope from the training rows using a documented least-squares method. Guard against empty, constant-level or rank-deficient inputs. Keep conversion and fitting functions separately testable.
3. **Validation report:** freeze the training/held-out batch split before fitting. Report training fit and held-out signed bias and RMSE by batch. Explain why a random-row split can understate error for a new-batch target and why this synthetic offset model does not establish real-device performance.
4. **Figure and interpretation:** show observations, the training calibration line and held-out residuals with labelled units. Include a text description or data table so interpretation does not depend on colour or image inspection.
5. **Reproducible bundle:** provide source code, tests, run instructions, Python/library versions, input-file SHA-256, and generated outputs. A reviewer should be able to reproduce the report from a clean checkout.

## Author-side construction checks

Because the records are public and the project is inactive, these values are visible self-checks rather than protected answer keys. Ordinary least squares on the balanced training split recovers an intercept of 20 mV and a slope of 3 mV/mM. With residuals defined as observed minus predicted, held-out mean errors are +4 mV for B05 and −3 mV for B06; their RMSE values are about 4.003 mV and 3.004 mV. A correct report should show that the shared calibration does not transfer equally to both held-out batches.

## Draft human rubric

No point weights or performance threshold are set. The reviewer should judge evidence in each category rather than infer quality from whether a program runs.

| Criterion | Strong evidence | Developing evidence | Little or no evidence |
| --- | --- | --- | --- |
| Input contract | Validates schema, units, finite values and unique IDs; rejected records retain reasons. | Most checks are present, with one ambiguity in validation or reporting. | Invalid rows are silently changed, dropped or accepted. |
| Function and test design | Small, explicit functions have independent known-answer and failure tests. | Core calculation runs, but edge cases or separation of responsibilities are weak. | Results cannot be reproduced or checked. |
| Numerical fit | Training-only least squares, rank checks, units and residual definitions are clear. | Fit is usable but has a unit, conditioning or explanation gap. | Held-out data enter the fit, or the calculation is materially incorrect. |
| Validation target | Whole held-out batches remain untouched until evaluation; per-batch denominators and errors are reported. | Group split is used but reporting or target explanation is incomplete. | Random-row split is treated as new-batch evidence. |
| Figure and access | Figure has units, readable labels, residual information and a text alternative or table. | Most information is present but one key label or alternative is missing. | Plot is uninterpretable or communicates no held-out result. |
| Bounded interpretation | Separates synthetic construction from real performance and identifies the batch-shift limitation. | Conclusions are mostly bounded with one unsupported inference. | Claims general device or biological validity from the toy data. |
| Reproducibility | Versioned instructions, input digest, tests and outputs let another person rerun the analysis. | A minor environment or provenance detail is missing. | Another person cannot recreate the reported result. |

The draft deliberately has no automatic score. Before any activation, course owners must decide submission and collaboration rules, measure student workload, review accommodations and accessible alternatives, arrange qualified programming/statistics review, and confirm a safe human-feedback workflow. This draft does not establish completion of those gates.
