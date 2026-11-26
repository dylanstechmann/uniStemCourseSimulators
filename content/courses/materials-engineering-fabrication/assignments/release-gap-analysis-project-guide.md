# Fabrication release-evidence gap-analysis project guide

**Status:** Original optional project in partial Materials Engineering for Fabrication 0.1.0; unreviewed, zero-point and formative-only. It produces a fictional review handoff, not a supplier approval or production release. Fabrication readiness is the review objective, never an achieved claim.

## Learning objectives

1. Build a five-milestone evidence gap analysis for a fictional component.
2. Recompute stack, RSS and lot-yield values and test every evidence gate.
3. Finish only with synthetic_review_complete or evidence_gaps_remain.

## Brief and rehearsal data

Use [release-gap-rehearsal.csv](release-gap-rehearsal.csv) with the six readings and [fabrication-evidence.csv](../labs/fabrication-evidence.csv). Every scenario is `synthetic-original`; names and evidence flags are invented. No physical experiment, supplier contact, software execution, machine setup or standards certification is required.

The CSV includes worst-case clearance inputs, three explicitly independent RSS terms, inspected/accepted lot counts and evidence fields for drawing/BOM alignment, engineering/safety review, material/process qualification, calibrated inspection/MSA, lot traceability, first-article coverage, nonconformance closure and change control. The authorized-release-role field describes a real-world requirement. It is not a signature and never authorizes this project.

For each scenario, calculate worst-case minimum clearance = hole lower limit − shaft upper limit. R02 gives 10.04−10.00 = 0.04 mm. Calculate RSS only because `independence_declared` is `yes`: R04 gives √(0.01²+0.02²+0.02²) = 0.03 mm. Accepted-lot yield = accepted/inspected×100; R05 gives 18/20×100 = 90%. Do not replace RSS with the sum of its terms and do not treat either result as inspection approval.

## Milestone 1: requirements and definition audit

Write the fictional function, loads/temperature/media/wear context, datum and assembly requirements. Check drawing and BOM revisions for alignment and identify affected risk, process and inspection records. Missing approved definitions or unresolved engineering/safety review produce `evidence_gaps_remain`. Record every assumption rather than filling gaps with plausible values.

## Milestone 2: process and geometric evidence

Summarize the selected fictional process route by mechanisms and evidence needs, without parameters. Audit process–structure–property and defect risks. Recompute every worst-case and RSS row, keeping methods separate and checking the declared independence field. Connect datums, fits and inspection consequences. R02’s 0.04 mm clearance and R04’s 0.03 mm RSS are arithmetic results only.

## Milestone 3: metrology, capability and lot evidence

Recompute accepted yield for all five rows and audit lot structure. Use the lab CSV to rehearse stable-only capability and repeated-reading boundaries. Check calibrated inspection/MSA, material/process qualification, supplier-lot linkage and first-article evidence. A 90% accepted-lot yield for R05 does not close its missing process-qualification gate. No Cp/Cpk may be interpreted for unstable or improperly pooled data.

## Milestone 4: risk, nonconformance and change-control audit

Trace each risk to a control-plan record and each nonconformance to containment, evaluation and verified closure. Verify that drawing/BOM, supplier, process or inspection changes have authorized change review. R03’s open nonconformance and R05’s missing qualification remain gaps even if their arithmetic is correct. Do not treat ordinal risk products as probabilities or high first-article coverage as complete coverage.

## Evidence matrix and reproducibility check

Before the final handoff, make one row per scenario and one column per gate. Enter the exact CSV value beside each gate, then cite the calculation or reading that explains its consequence. “Complete-synthetic” is a fictional field value rather than an externally verified fact. A second reader should be able to reproduce R02 clearance, R04 RSS and every yield without hidden notes. The matrix should also explain why a failed evidence gate cannot be averaged against a favorable numeric result. Preserve blank or missing observations as unknown; never infer zero defects or automatic closure from an empty field.

## Milestone 5: bounded review handoff

Assemble common scenario IDs, all calculations, source/evidence links, unresolved items and required real-world roles. Evaluate the teaching gates in a fixed order: controlled definition; engineering/safety review; material/process qualification; calibrated inspection/MSA; lot traceability; first-article evidence; nonconformance closure; change control; named authorized human release requirement. Any `missing`, `open`, `unstable`, `unauthorized` or `not-covered` state means `evidence_gaps_remain`.

Only R04 has every fictional teaching flag satisfied and therefore receives `synthetic_review_complete`. This means only that its synthetic review checklist is complete. R01, R02, R03 and R05 remain `evidence_gaps_remain`. No row may receive production_approved. Real readiness would still require approved drawings/BOM, qualified engineering and safety review, material/process qualification, calibrated inspection/MSA, lot traceability, nonconformance closure and named authorized human release outside this course.

Use the six Case studio entries: one integrative case and five zero-point milestones. Every criterion is self-assessed and zero-point. The checklists do not grade prose, certify competence, satisfy a standard or release hardware. A strong handoff is reproducible and makes remaining evidence gaps impossible to miss.
