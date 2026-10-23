# Confirmatory-protocol dossier project guide (optional, ungraded)

**Status:** open, optional practice. You can save milestone responses privately in the Case studio; this route is ungraded.
**Introduced in:** course package 0.5.0.
**Suggested time (unvalidated author estimate):** 2–4 hours across weeks 14–14.

## Start here

A confirmatory analysis begins with a question and design, not with a favourable p-value. This project converts the course’s planning lesson into a complete paper protocol: the experimental unit, target contrast, sample-size assumptions, multiplicity policy, data structure and interpretation must agree before new observations exist. Its rehearsal checks selected calculations and decisions; the written protocol still requires the learner to explain why its pieces are coherent.

Work through the supplied project after the related course readings. First close the model or evidence ledger on paper, then use the separate rehearsal to test your method. The worked example uses different inputs and is a demonstration of the reasoning, not a response to the project. Keep definitions, units, denominators, signs and assumptions visible in your own response. If a check fails, return to the model rather than adjusting a number to match an option.

## Project brief and supplied information

A fictional exploratory pilot tested 18 markers in two conditions. It used six independent units per condition and three technical readings per unit. No primary outcome was named in advance, and a selected p = 0.04 was reported after all 36 readings were treated as independent. This pilot can motivate a question; it cannot retrospectively become confirmatory evidence.

Write a **new, independent paper protocol**, with no data collection. Choose one question, system, primary outcome and timepoint, arm contrast and smallest effect of interest before new observations exist. Define independent and technical units, allocation, any blocking or pairing, blinding where meaningful and controls. Declare the sample-size approximation, effect, variance, alpha, sidedness, power, independent-unit requirement, attrition allowance and a sensitivity table.

Predeclare the primary analysis, assumption checks, missingness and exclusions, stopping rule and secondary-outcome family policy. Plan a tidy table retaining both unit and replicate IDs, an independent-unit plot with labelled units and uncertainty, a text alternative and reproducibility materials. Explain what the pilot and any future synthetic result could establish. This is a teaching exercise in internal consistency and evidence, not a plan for actual animal, human or clinical research.

## Milestones and self-review

### Milestone 1: Independent units and observations

For the project pilot with six independent units per condition and three readings per unit, separate unit and observation counts. Define the new study’s randomization unit and how technical repeats enter its analysis without inflating independent replication.

- Labels independent units and technical readings with separate IDs and denominators.
- Matches the analysis unit to allocation rather than to the number of rows.
- Keeps the exploratory pilot distinct from a new confirmatory dataset.

### Milestone 2: Question and estimand before new data

Write the project’s new primary question, population or synthetic system, outcome, timepoint, arm contrast and smallest effect of interest. State a rationale independent of the pilot’s selected p-value, and identify the primary model before new data.

- Specifies outcome, timing and contrast together.
- Justifies the effect scale without treating a selected pilot estimate as unbiased.
- Distinguishes the primary analysis from exploratory secondary work.

### Milestone 3: Sample size, sensitivity and attrition

For your project protocol, declare target effect, variance, alpha, sidedness and power. Show the calculation and a sensitivity row for a second variance assumption. Distinguish retained independent units from initially allocated units and justify any attrition allowance.

- Names the sample-size model and every input, including effect and variance units.
- Shows at least two variance assumptions and integer rounding.
- Keeps attrition, missing-data handling and technical replication conceptually separate.

### Milestone 4: Multiplicity and the pilot’s selected result

For the project’s 18-marker exploratory pilot, explain the selection/multiplicity problem. In the new protocol, define a secondary family and a suitable error-control aim, distinguish it from the single primary question, and state whether any displayed probability assumes independent tests.

- Defines the family and error-control goal rather than adjusting only a selected p-value.
- Keeps probability of any error distinct from expected error count.
- States which claims rely on independence and which do not.

### Milestone 5: Analysis, data and interpretation plan

Complete the project’s analysis, missingness, exclusion, stopping, data-integrity and reporting plans. Describe a labelled independent-unit plot and a text alternative. Finish with the strongest claim a future result could support and the mechanism or generalization claims it would not establish.

- Analysis and recordkeeping preserve unit IDs, technical repeats and denominators.
- The plot plan has a numerical scale, units, uncertainty and an accessible text description.
- The interpretation separates statistical evidence from effect importance, mechanism and external validity.

## Worked example: a separate case

A separate fictional score study has two independently allocated arms, a predeclared target difference of 2 assay points and assumed common standard deviation 3 points. Use two-sided alpha 0.05, target power 0.80 and stipulated approximate normal critical values 1.96 and 0.84. Under the equal-sized independent-group approximation, the difference-of-means standard error is sigma√(2/n). Requiring the target difference in standard-error units to reach approximately z_alpha/2+z_power gives n ≈ 2(z_alpha/2+z_power)² sigma²/delta² per arm.

Substitution gives 2(1.96+0.84)²(3²)/(2²) = 35.28. Round up to 36 retained independent units per arm. With planned 20% attrition, ceil(36/0.80) = 45 units per arm are allocated. At sigma = 4 points, the same calculation gives 62.72, rounded to 63 retained and ceil(63/0.80) = 79 allocated. The table therefore exposes sensitivity to variance instead of disguising a single pilot estimate as certainty. The approximation assumes the stated model and variance; it does not establish realized power or remove the need for design review.

Suppose a separately declared family has ten secondary comparisons and the aim is family-wise error no larger than 0.05. Bonferroni uses 0.005 per comparison. Under independent true nulls, testing every one at unadjusted 0.05 would instead give probability 1−0.95^10 ≈ 0.4013 of at least one false positive. The expected number is 0.5, which can be fractional even though the realized count is an integer. Keep this family distinct from the single primary contrast and state the chosen reporting policy.

The resulting paper protocol would retain unit IDs and technical-replicate IDs, summarize repeats under a justified within-unit model, and display independent-unit observations on a labelled assay-point scale. Missingness, exclusions and stopping are specified before new outcomes. A future interval and effect estimate would address the declared contrast; neither significance nor a planning calculation would establish a mechanism, universal relevance or authorization to conduct a real study.

## Rehearsal: practice before the project

The [rehearsal planning inputs](confirmatory-protocol-rehearsal.csv) describe a different pilot with eight independent units per arm, four technical readings each and twenty explored markers. For a new independent-arm mean contrast, the target effect is 3 assay points, assumed sigma 6 points with a sensitivity row at 7.5, two-sided alpha 0.05 and power 0.80. Use the stipulated approximate z values 1.96 and 0.842 in n ≈ 2(z_alpha/2+z_power)² sigma²/delta²; round retained per-arm units up, then divide by retention 0.90 and round again. A separately declared twenty-test secondary family uses FWER target 0.05. Use whole numbers for unit counts; probabilities and thresholds are continuous quantities.

Open **Practice gradebook** and choose **Confirmatory-protocol dossier rehearsal**. Each numeric field names its reporting unit. Enter continuous quantities as bare numbers to three significant figures, using scientific notation when trailing zeros would otherwise hide the intended precision; enter exact counts as whole numbers. Keep extra digits in intermediate calculations. Interpretation choices test the declared model and evidence limits; a correct choice does not demonstrate a complete written argument. The public feedback explains each field and permits unlimited retries.

## Finish and check your report

Include the supplied inputs, your equations or evidence map, intermediate quantities with units, a final table with clearly labelled rows and a short interpretation. For every numerical result, include a second check: substitute into the original relation, verify a conservation balance, compare a limiting case or independently recompute it. For evidence interpretations, name the comparison, design, endpoint, uncertainty and the conclusion that remains unsupported. A diagram or plot needs a plain-text description that preserves its scientific meaning; colour alone must not carry a distinction.

Use the Case studio checklist only after finding the corresponding evidence in your response. Marking a box records your own review; it does not score prose, certify mastery or establish an institutional grade. Disclose spreadsheets, code, references and AI assistance so another reader can distinguish your reasoning from external calculations. Keep a copy of your report and review any discrepancy between your calculation and the public rehearsal feedback before moving on.

| Stage | Focus | Where to work |
| --- | --- | --- |
| Rehearsal | Separate synthetic inputs and public feedback | Practice gradebook: Confirmatory-protocol dossier rehearsal |
| M1 | Independent units and observations | Case studio: project milestone 1 |
| M2 | Question and estimand before new data | Case studio: project milestone 2 |
| M3 | Sample size, sensitivity and attrition | Case studio: project milestone 3 |
| M4 | Multiplicity and the pilot’s selected result | Case studio: project milestone 4 |
| M5 | Analysis, data and interpretation plan | Case studio: project milestone 5 |

## Scope and provenance

Scope comparator: MIT OCW 18.05 Introduction to Probability and Statistics, Spring 2022 calendar, https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/pages/calendar/. Its inference sequence includes hypothesis tests, confidence intervals, bootstrap work and regression. The local study-planning lesson applies selected inference and replication foundations in this protocol dossier. This project does not supply the comparator’s full probability, Bayesian, regression or studio breadth, or validate an actual research protocol.

The original authoring draft remains a separate proposal for future qualified review; this guide supplies an open practice route without activating that draft as a graded assessment. Workload, scientific quality, assessment design and accessibility have not received independent approval. Original guide, synthetic inputs and rehearsal problems: CC BY 4.0, developed with substantial AI assistance as part of this personal hobby and learning project. No third-party prose, exercise, figure or dataset is reproduced.
