# Original synthetic process-reconciliation lab

This is a paper-and-data lab using only [process-reconciliation.csv](process-reconciliation.csv). No physical experiment is required or supplied. The dataset describes three fictional steady nonreactive mixing scenarios, LAB-01, LAB-02 and LAB-03, each with two feeds and one product. Generic species A, B and S are used throughout. The exercise develops conservation, evidence-role and residual reasoning; it does not validate a sensor, uncertainty model or physical process.

## Dataset structure and evidence roles

Each row has a scenario ID, stream ID and stream role. Columns prefixed `measured_` contain invented measurement records. Columns prefixed `reconciled_` contain values assigned by the declared steady total/component-balance model. These roles must not be merged. A measured value can disagree with a reconciled value, and a blank measured value can coexist with a balance-derived reconciled value. `data_status = synthetic-original` applies to every row.

The `record_relation` field states that rows within a scenario are correlated and are not independent replicates. Rows reused within a scenario are correlated records, not independent replicates. Feed and product rows share the same constructed closure conditions, so nine rows do not establish nine independent physical observations. Reusing a scenario in several questions also does not increase sample size. Report descriptive per-scenario closure and residuals only; do not calculate pooled independent-replicate intervals or statistical significance from this CSV.

The `evidence_status` field highlights unknown measurements. In LAB-03, feed-2 measured total is blank and product measured B is blank. Blank means unknown, never zero. The reconciled total and component fields remain present because the exercise declares that all three scenarios satisfy steady closure. Those derived values are not replacement measurements and should not be copied into measured columns.

## Recompute conservation for every row

For each scenario, verify total closure:

reconciled total(feed 1) + reconciled total(feed 2) = reconciled total(product).

Then repeat the check independently for A, B and S. For LAB-01, totals are 40 + 60 = 100 kg/h, A flows are 20 + 18 = 38 kg/h, B flows are 12 + 30 = 42 kg/h and S flows are 8 + 12 = 20 kg/h. The synthetic measured product A is 41 kg/h, so it differs from the reconciled A value. Do not change feed values simply to make that measured product value appear correct.

For LAB-02, reconciled totals are 25 + 75 = 100 kg/h. The measured product total is 102 kg/h. Using the declared convention residual = measured − reconciled, the product-total residual is +2 kg/h. The residual is a comparison statistic, not a new stream flow and not proof that a particular measurement is faulty. Check A, B and S closure independently even though this question highlights the total residual.

For LAB-03, feed B flows are 12 and 35 kg/h, so reconciled product B is 47 kg/h. The blank measured product-B field remains unknown. All other reconciled component and total balances must also close. Across the three scenarios, component flows should sum to their corresponding totals within each row, and all values should be nonnegative. Record any violation rather than silently repairing the source CSV.

## Reconciliation and its limits

A deterministic reconciliation imposes declared equations. It does not automatically minimize a statistically justified objective, allocate error to the correct instrument or prove uniqueness. Alternative sets of adjustments may satisfy the same balances. A defensible weighted reconciliation would need uncertainty, covariance, bias and independence evidence not provided here. The measured discrepancies in this dataset are deliberately simple teaching signals, not a sensor-diagnosis exercise.

Prepare a table with one summary per scenario: total feed sum, reconciled product total, each component feed sum, each reconciled product component, measured-minus-reconciled residual where available, and unknown measured fields. Then write a short interpretation distinguishing what is measured, what is derived and what remains unresolved. Include the record-relation disclosure verbatim or in equivalent clear language.

## Extension questions without invented data

Ask which additional independent measurement could test a chosen reconciled value, but do not fabricate its result. Consider how a negative flow or a component sum exceeding its row total would challenge the model. Explain why total closure cannot compensate for a component imbalance and why a blank cannot be interpreted as zero. If you propose an alternative adjustment, show that it also satisfies every balance and acknowledge that the data do not uniquely select it.

The final lab handoff is a zero-point formative artifact: a completed scenario summary, residual calculations, unknown-value register and model-boundary paragraph. It contains no instrument instructions, process settings, equipment ratings or operating recommendations. Successful arithmetic demonstrates only that the learner can reproduce the declared conservation relationships and evidence distinctions.


## Evidence and use boundary

This original reading is part of an explicitly partial university-level survey. It is unreviewed and formative-only. Every process, stream, property and observation is synthetic and fictional; generic labels A, B and S do not identify real chemicals. Worked precision supports reproducible arithmetic, not measurement accuracy. Arithmetic closure is not proof of safe or feasible operation. No real production recipe, hazardous condition, plant operating target, controller setting, line or pump sizing, equipment rating, relief sizing, or safety/release approval is supplied. Qualified scientific, engineering, safety and instructional review remains unresolved.
