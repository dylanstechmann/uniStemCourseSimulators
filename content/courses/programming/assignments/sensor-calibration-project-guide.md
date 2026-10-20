# Sensor-calibration project guide: a reproducible pipeline tested on held-out batches (optional, ungraded)

**Status:** open, optional and ungraded. Five milestone self-checks in the Case studio save responses privately; nothing is submitted, collected or scored, and no learner code runs in this application. The separate inactive project draft and its proposed review rubric remain unreviewed and are not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 6–10 hours across weeks 13 and 14.
**Prerequisite lessons:** [Data structures, units, and reproducible code](../modules/01-data-structures-units-and-reproducible-code.md), [Input contracts, parsing and pure scientific functions](../modules/08-contracts-parsing-and-pure-functions.md), [Testing a scientific function](../modules/05-testing-scientific-functions-and-provenance.md), [Regression, uncertainty, and validation](../modules/03-regression-uncertainty-and-validation.md), [Least squares, rank and scaled coordinates](../modules/12-least-squares-rank-and-scaled-coordinates.md), [Visualization and uncertainty communication](../modules/04-visualization-and-uncertainty-communication.md) and [Grouped validation, thresholds and reproducible reports](../modules/13-grouped-validation-thresholds-and-reproducibility.md).
**Data:** the [project records](../assessment-specs/sensor-calibration-records.csv) and the [rehearsal records](calibration-rehearsal-records.csv).

## Purpose

The project asks for a small analysis that someone else can rerun and check: read synthetic sensor records under a declared contract, fit a calibration line on training batches, and test how well it transfers to batches it has never seen. The numbers are simple on purpose. The point is the pipeline around them: a reader that rejects bad rows with reasons, a fitting function with guards and known-answer tests, a validation split that matches the prediction target, a readable figure, and a bundle that reproduces the report.

## The project

The records describe a synthetic sensor, not a real instrument, biological sample or clinical measurement. The file has 90 rows with the columns record_id, batch_id, split, standard_mM, signal_mV and replicate_id: five known standards (0, 0.5, 1, 2 and 4 mM), three replicate readings at each level, and six batches. Batches B01–B04 are marked train and B05–B06 held_out.

The values follow a published rule so that your code can be checked against known answers: signal_mV = 20 + 3 × standard_mM + batch offset + replicate offset, with batch offsets −1, 0, 0, 1, 4 and −3 mV for B01 to B06 and replicate offsets −0.2, 0 and +0.2 mV. Batch offsets make it possible for a calibration to fit its training data well and still transfer poorly to a new batch.

Rules for the analysis:

- Fit signal_mV = intercept + slope × standard_mM only on rows marked train.
- Keep each held-out batch whole when evaluating transfer. A random row split answers a different question, because it puts measurements from one batch on both sides.
- Define residuals as observed − predicted, state each metric's denominator and units, and report B05 and B06 separately.
- Do not use batch_id as a predictive input for unseen batches.

The five milestones are the draft's deliverables:

1. **Contract and provenance.** Write a pure reader that checks required columns, unique record IDs, finite numeric values, the declared units and the allowed split labels. Test malformed and non-finite rows with mutated copies of the file, and keep every rejected row with its reason.
2. **Calibration function.** Fit the intercept and slope from the training rows with a documented least-squares method. Guard against empty, constant-level or rank-deficient input, and keep conversion and fitting functions separately testable.
3. **Validation report.** Freeze the batch split before fitting. Report the training fit and the held-out signed bias and RMSE for each held-out batch. Explain why a random-row split can understate error for a new-batch target, and why this synthetic offset model does not establish real-device performance.
4. **Figure and interpretation.** Show the observations, the training calibration line and the held-out residuals with labelled units. Add a text description or a data table so that the interpretation does not depend on colour or image inspection.
5. **Reproducible bundle.** Provide source code, tests, run instructions, Python and library versions, the input file's SHA-256 and the generated outputs, so that another person can reproduce the report from a clean checkout.

## Milestones

| Milestone | Suggested week | Task | Where to check yourself |
| --- | --- | --- | --- |
| Rehearsal | 13 | Run your reader, fit and validation code on the rehearsal records, then use the open rehearsal practice set | **Practice gradebook**: Calibration project rehearsal |
| M1 | 13 | Reader, contract checks and mutated-fixture tests | Case studio: project milestone 1 |
| M2 | 13 | Calibration function, guards and known-answer tests | Case studio: project milestone 2 |
| M3 | 13 | Frozen batch split, per-batch bias and RMSE | Case studio: project milestone 3 |
| M4 | 14 | Figure with units and a text or table alternative | Case studio: project milestone 4 |
| M5 | 14 | Reproducible bundle from a clean checkout | Case studio: project milestone 5 |

Each Case studio milestone lists self-review statements. Responses are saved privately in this application and are never scored. Your code runs on your own computer; nothing here executes or inspects it.

## Rehearsal records

The [rehearsal file](calibration-rehearsal-records.csv) has the same columns as the project file and works as a known-answer test for your code before you run it on the project. Its valid rows follow signal_mV = 12 + 5 × standard_mM + batch offset + replicate offset, with standards 0, 1, 2 and 3 mM, two replicates per level (−0.3 and +0.3 mV), training batches T1–T3 (offsets −0.6, +0.3 and +0.9 mV) and held-out batches H1 and H2 (+2.5 and −1.5 mV). Some rows break the contract on purpose.

Use one contract for both files: reject every row whose record_id appears more than once, whose signal is not a finite number, or whose split is not train or held_out, and keep each rejected row with its reason. When an ID appears twice with different values, nothing in the file says which row is right, so neither is kept. Then fit the training rows, evaluate H1 and H2, and compare your counts, fit and per-batch errors with the open rehearsal practice set, which gives feedback on each value.

## Worked example: a three-point calibration

One synthetic training batch reads 10.0, 14.2 and 17.8 mV at 0, 2 and 4 mM.

1. **Center.** The mean standard is 2 mM and the mean signal 14.0 mV.
2. **Fit.** Σ(x − x̄)(y − ȳ) = (−2)(−4.0) + 0 × 0.2 + 2 × 3.8 = 15.6 and Σ(x − x̄)² = 8, so the slope is 15.6/8 = 1.95 mV/mM and the intercept 14.0 − 1.95 × 2 = 10.1 mV.
3. **Training error.** The predictions are 10.1, 14.0 and 17.9 mV, so the residuals are −0.1, +0.2 and −0.1 mV. They sum to zero, as least-squares residuals with an intercept must, and the training RMSE is √(0.06/3) ≈ 0.141 mV.
4. **A new batch.** A held-out batch reads 12.6 mV at 1 mM and 16.4 mV at 3 mM. The calibration predicts 12.05 and 15.95 mV, so the residuals are +0.55 and +0.45 mV: a mean residual of +0.50 mV and an RMSE of √(0.2525) ≈ 0.502 mV, more than three times the training RMSE.

The line describes its own batch well and still misses the new batch by a nearly constant offset. Only a held-out batch could show that. The same calculation as a small function, with the guards that milestone 2 asks for:

```python
import math


def fit_line(levels, signals):
    """Ordinary least squares for signal = intercept + slope * level; returns (intercept, slope)."""
    if len(levels) != len(signals) or len(levels) < 2:
        raise ValueError("need at least two paired observations")
    mean_x = math.fsum(levels) / len(levels)
    mean_y = math.fsum(signals) / len(signals)
    sxx = math.fsum((x - mean_x) ** 2 for x in levels)
    if sxx == 0:
        raise ValueError("all standards are equal, so the slope is not identifiable")
    sxy = math.fsum((x - mean_x) * (y - mean_y) for x, y in zip(levels, signals))
    slope = sxy / sxx
    return mean_y - slope * mean_x, slope
```

A known-answer test would call `fit_line([0, 2, 4], [10.0, 14.2, 17.8])` and compare the result with (10.1, 1.95) using a tolerance, not exact equality.

## Construction checks for the project

Because the project data follow the published rule above, the inactive draft lists the values that a correct pipeline reproduces: an intercept of 20 mV and a slope of 3 mV/mM from the training rows, held-out mean residuals of +4 mV for B05 and −3 mV for B06, and RMSE values of about 4.003 and 3.004 mV. Use them as a final known-answer check after your own code has produced its results. Matching them shows that the calculation does what it claims; it does not show that the reader, tests, figure, interpretation or bundle are complete.

## Reporting conventions

- Report the slope in mV/mM and the intercept, bias and RMSE in mV, with the number of rows behind each value.
- Keep full precision in calculations and round only reported values.
- Use residual = observed − predicted throughout, and say so in the report.
- Disclose any software, libraries or AI assistance you used.

## Self-review rubric

The inactive project draft proposes seven criteria for a future human reviewer and assigns them no points. For self-review, mark each criterion 0 (little or no evidence), 1 (developing evidence) or 2 (strong evidence).

| Criterion | Evidence of a strong response |
| --- | --- |
| Input contract | Validates schema, units, finite values and unique IDs; rejected records keep their reasons |
| Function and test design | Small, explicit functions have independent known-answer and failure tests |
| Numerical fit | Training-only least squares, rank checks, units and residual definitions are clear |
| Validation target | Whole held-out batches stay untouched until evaluation; per-batch denominators and errors are reported |
| Figure and access | The figure has units, readable labels, residual information and a text alternative or table |
| Bounded interpretation | Separates synthetic construction from real performance and identifies the batch-shift limitation |
| Reproducibility | Versioned instructions, an input digest, tests and outputs let another person rerun the analysis |

These marks are a self-check. They are not calibrated, carry no grade and do not stand in for an instructor's or code reviewer's judgment.

## Limitations and provenance

The records, offsets and rehearsal data are synthetic teaching values generated from stated rules. The calibration is a straight line with constant batch offsets; real sensors can drift, saturate, respond nonlinearly or change with temperature and age, and nothing here describes a real instrument, assay or clinical measurement. This application does not run, test or inspect learner code. Original guide and synthetic rehearsal data: CC BY 4.0, developed with substantial AI assistance.
