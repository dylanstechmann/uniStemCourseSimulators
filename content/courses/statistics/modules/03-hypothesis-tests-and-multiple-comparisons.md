# Hypothesis tests and multiple comparisons

A hypothesis test compares observed data with a probability model specified under a null hypothesis. It can summarize how unusual the data would be under that model, but it cannot by itself tell us whether a scientific claim is true, whether an effect matters, or whether a study was designed well. Interpret the test together with the question chosen before analysis, the sampling and measurement process, the effect estimate, and the uncertainty around that estimate.

## State the question before calculating

The null hypothesis, H0, describes a reference condition such as no mean difference in a defined population. An alternative, HA, describes the departures that count as evidence against that reference. A two-sided alternative includes deviations in either direction; a one-sided alternative has a direction that must be justified before the data are examined. The test statistic summarizes a feature of the observed data, and its null distribution describes that statistic under H0 and the assumptions of the analysis.

For a two-sided test of a mean difference, one possible statistic is the estimated difference divided by its standard error. If the null model says the difference is zero, a result far from zero in either direction is less compatible with that model. The statistic and reference distribution depend on the design: paired observations call for a paired analysis, independently sampled groups need an independent-group analysis, and nested measurements do not become independent merely because they appear as separate rows. The chosen model should follow the unit randomized or sampled and the target quantity, not the software menu that is easiest to select.

A p-value is calculated under H0, the specified analysis, and its assumptions. It is the probability of obtaining data at least as incompatible with H0 as the observed data, using the chosen test statistic and tail direction. For example, if a prespecified two-sided analysis gives p = 0.03, then data this incompatible or more incompatible would occur in about 3% of repetitions under H0 and the model assumptions. It does not mean there is a 3% probability that H0 is true. It also is not the probability that the finding will fail to replicate, a measure of the effect's size, or the chance that the result arose “by chance” without specifying a probability model.

The p-value is conditional on choices and assumptions. Changing the outcome, exclusions, stopping rule, transformation, subgroup, or direction after looking at the results changes the procedure that produced it. A nominal p-value does not account for unreported attempts. Planning the primary outcome, comparison, sample, and analysis before seeing results makes the inferential target clearer; a protocol still cannot fix a biased sample, poor measurement, dependence, or a misspecified model.

## A threshold is a decision rule, not a scientific boundary

If a test uses α = 0.05, that threshold is a rule for rejecting H0 in repeated use under the stated procedure. When the null is true and assumptions hold, α is the long-run probability of a Type I error for that single test. Rejecting means the observation crossed the specified threshold; it does not prove the alternative or show that the effect is practically important. A tiny effect can produce a small p-value with a very large sample. Report the estimate in its scientific units and an interval or other uncertainty summary so readers can assess the plausible magnitude.

When p is above α, the data do not meet that decision rule. “Fail to reject” is not proof of no effect. The result might be compatible with no effect, with a useful effect, or with a harmful effect because the interval is wide. Type II error is failure to reject for a specified alternative; its probability depends on the true effect, variability, sample size, design and analysis. Power is one minus that probability for the specified alternative. Increasing sample size can improve precision and power, but cannot remove systematic bias or turn an irrelevant outcome into a meaningful one.

## Repeating tests changes the chance of a false positive

Suppose m independent tests are run, every null hypothesis is true, and each test uses α. Each test has probability 1 − α of avoiding a false positive. Under independence, the probability of avoiding false positives in all m tests is (1 − α)^m, so the family-wise error rate (FWER)—the probability of one or more false positives in the family—is

**FWER = 1 − (1 − α)^m.**

At α = 0.05 across ten independent true nulls, this is 1 − 0.95¹⁰ ≈ 0.401, or about 40%. This is the calculation in the preserved ten-test check. Across twenty independent true nulls, it is 1 − 0.95²⁰ ≈ 0.642. These values rely on independence and all nulls being true; for tests with correlated outcomes the product formula changes. The broader lesson remains: testing a family of questions and reporting only whichever pass an unadjusted threshold can mislead, even when each individual calculation is correct.

Bonferroni provides a simple way to control FWER for a family of m tests: use α/m for each test. With a family-wise target of 0.05 and twenty tests, the per-test threshold is 0.05/20 = 0.0025. The union bound ensures the chance of at least one false rejection is no greater than the target, without requiring independence. The method can be conservative, especially when tests are numerous or correlated, so the tradeoff is fewer false alarms at the cost of reduced power. The preserved twenty-test item asks for this threshold, not for a claim that every p-value is a posterior probability.

False-discovery-rate (FDR) procedures answer a different question: they aim to control the expected fraction of false findings among the findings called positive, under the procedure's conditions. This can suit a broad exploratory screen where many candidates will be followed up. It is not the probability that each named hit is false, and it is not a guarantee that a fixed maximum number of hits is false. A confirmatory decision with a costly consequence may instead prioritize family-wise control. The course's later multiple-testing lesson compares Bonferroni with Benjamini–Hochberg and develops that choice in detail.

## Separate confirmatory tests from exploration

A confirmatory analysis starts with a defined primary question, outcome, contrast, direction when justified, exclusion rules, and error-control plan. If several endpoints or contrasts can each support the same headline claim, define the family and choose an error criterion before examining results. A correction cannot rescue selective reporting if the family itself was hidden. Transparent reporting should list the planned tests and disclose deviations or additional analyses.

Exploration is useful for discovering patterns, checking data quality, and generating hypotheses. It should be labeled as exploratory rather than presented as if every choice had been fixed in advance. The same data can inspire a hypothesis, but evidence from an independent confirmatory sample or a design with valid selective-inference procedures is needed to evaluate that hypothesis without treating discovery and confirmation as independent steps. Optional stopping, repeated interim looks, unplanned subgroup searches, and many alternative outcomes all enlarge the analysis process and may need explicit adjustment or a sequential design.

## A disciplined reading of a result

For a reported test, identify the population and experimental unit; state H0, HA, the direction and test family; verify that the sampling and model assumptions match the design; read p as a conditional tail probability; and identify the threshold and any adjustment. Then examine the effect estimate and its interval in meaningful units, compare them with a prespecified practical threshold if one exists, and distinguish confirmatory evidence from exploratory follow-up. If the result is not significant, ask whether the interval rules out effects worth detecting or is simply too imprecise. If many tests were run, ask which ones were planned and which error criterion fits the decision.

All numerical examples in this reading are synthetic. The formulas illustrate idealized error control under their stated assumptions; they do not certify a real study or establish causation. MIT OpenCourseWare readings and problem solutions are optional link-only technical references. No outside exercise, wording, figure, table, or dataset has been copied or adapted.
