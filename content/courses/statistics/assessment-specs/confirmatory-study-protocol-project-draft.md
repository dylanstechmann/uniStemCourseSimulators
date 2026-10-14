# Confirmatory-study protocol project draft

**Inactive authoring draft for Probability, Biostatistics & Experimental Design 0.4.5.** This is a paper protocol exercise, not a scheduled assignment or a real study plan. It collects no data and carries no points or course grade. The pilot described below is entirely synthetic. It is not animal, human-subject, clinical or regulatory guidance. Qualified statistical review, workload measurement, accessibility review and activation decisions remain open.

## Project scenario

A fictional exploratory pilot compared two conditions across 18 measured markers. It used six independent units per condition and three technical readings per unit, named no primary outcome in advance, and reported one $p=0.04$ after treating all 36 readings as independent. The course's [week-14 lesson](../modules/15-planning-a-confirmatory-study.md) works through why that analysis does not make the selected marker confirmatory evidence.

Prepare a protocol for a new, independent confirmatory study of one question motivated by the pilot. Treat the pilot as hypothesis-generating only. The new protocol must choose its primary outcome, target effect and analysis before new observations exist; it cannot promote the pilot's smallest p-value into a pre-specified result after the fact.

## Required protocol deliverables

1. **Question and estimand:** state one answerable question, the population or system to which it refers, the primary outcome and timepoint, the contrast, and the smallest effect of interest with a substantive rationale.
2. **Design and units:** define the independent experimental unit and technical observations, allocation/randomization, blocking or pairing if used, blinding of measurement/analysis where feasible, and controls. Explain how the design prevents technical readings from inflating the independent sample size.
3. **Sample-size plan:** declare the target effect, variance assumptions, two-sided or one-sided test, alpha, power, independent-unit count, treatment of technical repeats, attrition allowance and calculation method/software version. Include a sensitivity table for at least two plausible variance values. Do not use the observed pilot effect as an unbiased planning target.
4. **Analysis plan:** specify one primary model and contrast, effect estimate and interval, assumption checks, missing-data handling, exclusion rules and a stopping rule. List the secondary outcomes as a family and choose a family-wise or false-discovery control appropriate to the stated goal.
5. **Data and reporting plan:** define a tidy row structure with unit IDs and technical-replicate IDs, a de-identified recordkeeping plan, a plot that displays independent-unit observations, the denominator for each summary, reproducibility materials and a text alternative for figures.
6. **Interpretation limits:** explain what the pilot and proposed future result can and cannot establish. Separate statistical evidence from biological mechanism, generalization and practical importance.

The protocol should be internally consistent: the randomization unit, analysis unit and sample-size unit must agree. The planned primary question must be distinguishable from any exploratory secondary analysis. No synthetic result in this draft is evidence about an actual system.

## Draft human rubric

No weights, points, cut scores, submission rules or course-grade policy are assigned.

| Criterion | Strong evidence | Developing evidence | Little or no evidence |
| --- | --- | --- | --- |
| Question and estimand | Primary outcome, time, contrast and effect of interest are specified before new data. | Most are specified but one remains broad or ambiguous. | The protocol adopts the pilot's selected result without a new question. |
| Unit and design | Independent units, technical repeats, controls and allocation are explicit and aligned. | Design is plausible but a unit, control or allocation detail is unclear. | Technical observations are counted as independent units. |
| Sample-size reasoning | Effect, variance, alpha, power, independent-unit count, method and sensitivity are transparent. | Calculation is present but an assumption or sensitivity is missing. | Pilot p-value or technical-read count is used as a sample-size justification. |
| Analysis and multiplicity | One primary model/contrast is fixed; checks, missingness and secondary-family policy are coherent. | Core analysis is specified with one unresolved handling or multiplicity choice. | Outcome selection or multiplicity is ignored. |
| Data integrity | IDs, denominators, exclusions, provenance and reproducibility are planned. | Most are present but a detail impedes reproduction. | Data structure would merge units or hide exclusions. |
| Figure and communication | Independent-unit data, effect scale, interval and units are clearly labelled with a text alternative. | Figure plan is useful but misses a label or accessible alternative. | Summary bars or unclear denominators obscure the design. |
| Bounded interpretation | Claims distinguish hypothesis generation, confirmatory evidence and generalization. | Limits are noted but one claim is too broad. | The protocol treats statistical significance as proof of mechanism or importance. |

Before activation, a qualified reviewer must assess statistical and subject-matter correctness, rubric fairness and accessible alternatives. Course owners must define workload, collaboration and feedback policy. This draft is not part of the course manifest's assessment schedule; it creates no grade and authorizes no real-world research.
