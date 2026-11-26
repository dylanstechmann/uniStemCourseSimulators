# Metrology, measurement systems, monitoring, capability and yield

**Status:** Original reading in partial Materials Engineering for Fabrication 0.1.0; unreviewed and formative-only. All gauges, processes, subgroups and values are fictional and synthetic. This lesson provides no instrument setup, acceptance-sampling plan, calibration procedure, standard-specific checklist or production disposition.

## Learning objectives

1. Distinguish resolution, bias and gauge R&R concepts, including repeated-reading dependence.
2. Apply rational subgrouping, control charts, Cp/Cpk and yield arithmetic only under declared conditions.
3. Assemble traceable inspection evidence while preserving unstable or unknown cases.

## Measurement is an evidence process

Resolution is the smallest displayed or detectable increment under a stated convention; it is not accuracy. Bias is a systematic difference between a measurement and a reference value under defined conditions. Repeatability concerns variation under similar measurement conditions, while reproducibility concerns changed conditions such as operators or setups in a measurement-system study. Gauge R&R concepts apportion selected measurement-system variance components, but the study design determines what those components represent.

A tolerance-to-resolution ratio can be a simple screening calculation. A 0.20 mm tolerance band and 0.01 mm displayed resolution give 20. This ratio does not prove the gauge is adequate: bias, repeatability, fixture effects, thermal conditions and the measured geometry still matter. Calibration status links equipment to reference evidence, but a current label alone does not establish that the full measurement method is suitable.

Repeated readings on one part help evaluate repeatability. They are not independent parts and cannot estimate part-to-part variation as if each reading were a new specimen. Ten readings of one part still represent one part. Likewise, measurements of parts from one lot do not automatically represent another lot. Preserve part ID, lot ID, gauge ID, reading sequence and subgroup structure in the evidence table.

## Rational subgrouping and control charts

Rational subgrouping organizes observations so within-subgroup variation reflects the intended short-term/common-cause reference and between-subgroup comparisons can reveal relevant changes. Time order, lot, machine, operator, material and process route may all matter. Subgrouping is not a cosmetic choice made to obtain attractive limits. Arbitrarily mixing lots or special-cause periods can inflate limits and hide shifts; overly narrow grouping can miss relevant variation.

Control charts distinguish routine variation from signals worth investigating under a chosen model. A point beyond a limit is a signal, not an automatic proof of root cause or nonconformance. Conversely, points inside limits do not prove that the process meets specifications. Control limits come from process behavior; specification limits come from requirements. They must never be interchanged. Investigation, disposition and corrective action require separate records and authorized decisions.

## Capability requires stability and appropriate pooling

For a declared stable process model with compatible within-process standard deviation, Cp = (USL−LSL)/(6σ). Using LSL = 9.8, USL = 10.2 and σ = 0.05 gives Cp = 1.333333…. Cp addresses spread relative to the specification width but ignores centering. Cpk uses the closer specification side: with mean 10.1 and σ = 0.04, Cpk = min[(10.2−10.1)/(3×0.04), (10.1−9.8)/(3×0.04)] = 0.833333…. A large Cp and small Cpk can coexist.

These calculations are not valid interpretations for an unstable or improperly pooled process. A special-cause shift must be investigated rather than averaged into a larger sigma. Pooling several lots with different means can create an impressive but meaningless number. Distribution shape, subgroup method, sampling independence and the meaning of σ also matter. This package reports synthetic arithmetic only and withholds interpretation wherever its declared stability gate fails.

## Yield and traceability

Observed accepted yield = accepted parts/inspected parts ×100 under a stated inspection rule. If 193 of 200 parts are accepted, synthetic yield is 96.5%. It is not a probability guarantee for the next lot, and inspection escapes can make observed yield differ from true conforming yield. Unknown inspection outcomes stay unknown rather than being counted as accepted. Reinspection and rework require explicit counting rules to prevent double counting.

Traceability connects each result to drawing/BOM revision, part and lot identity, material and process evidence, gauge/calibration record, subgroup, inspector or automated record, nonconformance and disposition. A capability value without this chain is not release evidence. First-article evidence and control plans should identify what is measured and how records are reviewed, but completing a template does not establish readiness.

## Common mistakes

Do not equate resolution with accuracy, call repeated readings independent parts, use specification limits as control limits, or calculate Cp/Cpk across an unexplained shift. Do not pool lots because a combined average looks better, interpret in-control as automatically acceptable, or use a one-lot yield as a guaranteed future rate. Missing calibration, qualification or nonconformance closure cannot be repaired by a high Cpk.

## Scope and sources

The [MIT 2.830J Control of Manufacturing Processes Spring 2008 calendar](https://ocw.mit.edu/courses/2-830j-control-of-manufacturing-processes-sma-6303-spring-2008/pages/calendar/) includes probability models, sampling, Shewhart SPC, capability, yield, variance components and broader experimental design. The [NIST/SEMATECH process monitoring and control handbook chapter](https://www.itl.nist.gov/div898/handbook/pmc/pmc.htm) is a link-only methods reference for monitoring, capability, charts and related boundaries. Existing statistics records supply prerequisite reasoning. No source exercise, dataset, table or prose is imported, and this partial survey remains unreviewed.
