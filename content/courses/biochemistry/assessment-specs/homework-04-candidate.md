# Homework 4 review candidate: enzyme-kinetics data analysis

**State: inactive answer-free review candidate.** This 5-case, 50-point draft covers proposed week(s) 7. It is not scheduled, assigned, submitted, graded or included in the course assessment policy. An unreviewed private key/grader draft is stored outside this public package; it is not approved or active. This public candidate does not define a due date, attempt rule or time estimate. Draft points are for blueprint discussion only.

## Preparation and purpose

This set practices the full data path from replicate summaries to fitted parameters and an evidence-bounded inhibition interpretation. Each row in the accompanying dataset is a synthetic initial-rate observation. It is not a wet-lab protocol and does not identify a real enzyme or inhibitor. Read the corresponding course lessons before attempting the cases. Every row and entity is fictional. Use only the values and assumptions stated in this brief, the attached data file and the relevant lesson. Keep units and denominators explicit. A result supports only the quantity or model requested; it does not establish a real enzyme mechanism, patient state, treatment choice or laboratory outcome. Structured response fields do not score free-text reasoning unless a later reviewed rubric explicitly says otherwise.

## Dataset and response boundaries

The accompanying UTF-8 CSV is the sole source of candidate-specific numeric observations. It uses case identifiers to associate rows with prompts and records the stipulated context. For case 3, the `inhibitor_concentration_uM` column gives the stipulated inhibitor concentration on inhibitor-condition rows. Units are part of the data, not decorative labels. The values are synthetic; repeated observations must not be described as independent biological replicates beyond their stated identifiers. Do not extrapolate beyond the model range or treat a teaching parameter as a measured biological constant. Unless a prompt says otherwise, report numeric answers to three significant figures and use the units requested in the structured response fields. These cases do not define deadlines, required course workload, grade weights, partial-credit rules or an approved assessment schedule.

## Candidate cases

1. Use the paired replicate initial-rate observations in the dataset and keep substrate concentrations grouped by condition. Calculate the mean control initial rate at 40 µM substrate. Calculate the mean inhibitor-condition initial rate at 40 µM substrate.
2. Fit the untransformed control replicate means to v = Vmax[S]/(Km + [S]) by minimizing squared rate residuals; do not use a reciprocal plot. Estimate Vmax for the control series. Estimate Km for the control series.
3. Compare the inhibitor series with control at matched substrate concentrations. Estimate apparent Km under the inhibitor condition. Estimate the inhibition constant using the simple competitive model and supplied inhibitor concentration.
4. Interpret the fitted parameter pattern without treating a model fit as a molecular structure determination. Which simple inhibition mode is consistent with an increased apparent Km and approximately unchanged Vmax? Which limitation should be reported for a double-reciprocal estimate?
5. Use the assay context stated in the candidate instructions. Which condition best supports an initial-rate interpretation? What is the replicate unit in this dataset?

## Limits and review needed

This draft is a prospective assessment blueprint, not a validated graded assignment. Before activation, the data and every numerical result need independent recalculation; the private key and grader need candidate-specific hash checks and mutation testing; a qualified biochemical reviewer and assessment-blueprint reviewer must examine the exact version; accessibility and fairness need review; workload must be measured after the required schedule is frozen; protected delivery must be verified for this candidate; and an operator must approve release and retake policy. The candidate remains outside the live manifest until all gates are resolved. No reviewer is identified or implied by this authoring.

## Provenance

Original answer-free authoring with synthetic teaching data, CC BY 4.0. No external assessment, real assay or third-party dataset was copied.
