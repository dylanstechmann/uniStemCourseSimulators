# Original synthetic fabrication-evidence laboratory

**Status:** Original zero-point lab in partial Materials Engineering for Fabrication 0.1.0; unreviewed and formative-only. Every part, lot, gauge and measurement is fictional synthetic data. No physical fabrication, gauge setup, calibration procedure, production capability claim or release approval is included.

## Learning objectives

1. Recompute clearance, capability and yield for every relevant public CSV row.
2. Separate independent parts within lots from repeated gauge readings and prevent improper pooling.
3. Trace evidence fields to a bounded disposition with missing evidence on hold.

## Data dictionary and provenance

Download [fabrication-evidence.csv](fabrication-evidence.csv). Its 16 rows represent four fictional parts in each of four lots. Each row has a unique part ID, one actual dimension and one repeated reading of that same part. `record_relation` explicitly states that the repeated reading is not an independent part. The actual-dimension rows within a lot are the part-level records for this exercise; the repeated column is measurement-repeat evidence only.

Specification limits for the dimension are LSL = 9.90 mm and USL = 10.10 mm. The `summary_mean_mm` and `within_sigma_mm` fields are declared lot-summary inputs for capability arithmetic, not estimates to recompute from the four displayed dimensions. `process_state` declares whether the synthetic model is stable for the arithmetic exercise. L04 contains a special-cause shift, so capability is withheld even though numeric columns are blank rather than fabricated. This is a teaching convention, not evidence that real four-part samples establish stability.

Other fields preserve drawing/BOM revision, gauge and calibration identity, material/process evidence, first-article and nonconformance state. Hole and shaft actuals support direct clearance arithmetic. Limit columns support separate worst-case review. All `data_status` values must remain `synthetic-original`.

## Audit sequence

**1. Verify structure and independence.** Confirm 16 unique part IDs, four lots and four actual parts per lot. Check that each repeated reading belongs to the same part. Do not count 32 rows of evidence by splitting actual and repeated readings, and do not treat four lots as one homogeneous process.

**2. Recompute clearances.** For P03, hole actual = 10.06 mm and shaft actual = 9.98 mm, so actual clearance = 0.08 mm. For P07, 10.10−10.01 = 0.09 mm. Repeat for every row and check the sign. Actual clearance is not the worst-case limit: the latter uses the hole lower and shaft upper limit columns.

**3. Recompute capability only where allowed.** L02 declares mean 10.01 mm and within sigma 0.02 mm with a stable arithmetic model. Cp = (10.10−9.90)/(6×0.02) = 1.666666… and Cpk = min[(10.10−10.01)/(3×0.02), (10.01−9.90)/(3×0.02)] = 1.5. L03 has mean 10.04 and sigma 0.025, giving Cp = 1.333333… and Cpk = 0.8. L04 has a special-cause signal; do not compute or interpret Cp/Cpk for it and do not pool it with another lot.

**4. Recompute yield and lot structure.** L01 has four accepted actual dimensions out of four inspected, so observed yield = 100%. L04 has three accepted of four because P16 is 10.12 mm, giving 75%. Yield uses actual parts, not repeated readings. Verify L02 and L03 separately and preserve the fact that observed inspection yield is not a future probability or proof of true conformance.

**5. Audit the evidence chain.** Join each part to its lot, drawing/BOM revision, gauge/calibration, material and process evidence, first-article and nonconformance fields. An in-specification dimension cannot compensate for an open nonconformance or missing qualification. The lab’s own disposition remains `evidence_gaps_remain` for any scenario with unresolved fields. A scenario marked `synthetic_review_complete` elsewhere in the project still would not mean production approved.

## Expected self-check

A complete response includes all 16 clearances, all limit checks, per-lot accepted counts and yields, L01–L03 capability arithmetic where permitted, the L04 withheld interpretation, and a paragraph explaining why repeated readings and pooled lots cannot inflate independent evidence. Include traceability gaps and the exact responsible real-world evidence role needed to resolve them.

## Common mistakes

Do not use the repeated reading as a second part, calculate Cpk for L04, pool L02 and L03 to obtain a new sigma, use control limits as specifications, or accept P16. Do not convert four-part teaching samples into validated process capability. Do not supply feeds/speeds, gauge settings, calibration steps or a release signature.

The [MIT 2.830J Spring 2008 calendar](https://ocw.mit.edu/courses/2-830j-control-of-manufacturing-processes-sma-6303-spring-2008/pages/calendar/) and [NIST/SEMATECH monitoring chapter](https://www.itl.nist.gov/div898/handbook/pmc/pmc.htm) are link-only comparators for broader variation, SPC and capability methods. No source problem, data or prose is imported. This agent-authored synthetic lab is not qualified engineering, statistical or metrology review.
