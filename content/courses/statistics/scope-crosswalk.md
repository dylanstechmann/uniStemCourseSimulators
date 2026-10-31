# Probability, Biostatistics & Experimental Design scope crosswalk

This crosswalk compares the local package, version 0.7.0, with two published courses: MIT OpenCourseWare 18.05 Introduction to Probability and Statistics, Spring 2022 ([calendar](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/pages/calendar/)), and the University of South Carolina STAT 205 Elementary Statistics for the Biological and Life Sciences, Fall 2011 ([syllabus and schedule](https://people.stat.sc.edu/hansont/stat205/SyllabusF11.pdf), taught by Dr. Tim Hanson). It was compiled with AI assistance on 2026-10-31 from session titles and the syllabus's topic list. It is an agent-run comparison, not a review by the owner or a statistics instructor, and topic alignment establishes no equivalence, credit or endorsement.

18.05 is a calculus-based course with a strong Bayesian unit. STAT 205 is a non-calculus course for life-science students, with a unit on 2 × 2 tables and diagnostic testing. Status labels: **covered** means a local reading develops the topic with a worked example and practice; **shallow** means part of it is taught; **absent** means no local instruction; **local extension** means neither comparator names it.

| Topic | MIT 18.05 Spring 2022 | USC STAT 205 Fall 2011 | Local lessons | Status |
| --- | --- | --- | --- | --- |
| Probability rules, random variables, distributions | Classes 1–6b | Sep 6–15 | [1](modules/01-probability-distributions-and-sampling.md) | Covered |
| Joint distributions, covariance, conditioning | Class 7 | — | [18](modules/joint-laws-conditioning-and-total-variance.md) | Covered |
| Likelihood and maximum likelihood | Class 10 | — | [19](modules/likelihood-estimation-and-censored-exposure.md) | Covered |
| Bayesian updating, conjugate priors, normal conjugacy | Classes 11–16 | — | [16](modules/16-finite-bayesian-updating-and-predictive-checks.md), [17](modules/17-beta-binomial-conjugacy-and-prediction.md), [20](modules/normal-conjugacy-and-shared-prediction.md) | Covered |
| Confidence intervals, effect sizes, sample size | Classes 22–23 | Sep 27–29 | [2](modules/02-estimation-confidence-intervals-and-effect-sizes.md), [8](modules/08-effect-sizes-intervals-and-regression-to-the-mean.md), [11](modules/11-power-sample-size-and-small-studies.md) | Covered |
| Significance testing, t tests, paired designs | Classes 17–18, 20 | Oct 4–18 | [3](modules/03-hypothesis-tests-and-multiple-comparisons.md), [10](modules/10-comparing-two-groups-t-tests-and-pairing.md), [14](modules/14-base-rates-positive-predictive-value-and-replication.md) | Covered |
| Rank tests, permutation and bootstrap | Classes 24 and Studio 10 | Oct 4, 13 | [13](modules/13-resampling-permutation-and-rank-tests.md) | Covered |
| χ² tests and 2 × 2 tables; risk difference, risk ratio and odds ratio; Fisher's exact test | Class 19 (χ²) | Nov 1–3 | [26](modules/26-categorical-outcomes-two-by-two-tables.md) | Covered in 0.7.0; previously absent |
| Stratified 2 × 2 tables, Mantel–Haenszel, Simpson's paradox | — | Nov 8 | [26](modules/26-categorical-outcomes-two-by-two-tables.md) | Covered in 0.7.0 for the Mantel–Haenszel odds ratio; the Cochran–Mantel–Haenszel test statistic is not developed |
| One-way analysis of variance | Class 19 (ANOVA) | Nov 10 | [27](modules/27-one-way-analysis-of-variance.md) | Covered in 0.7.0; previously absent |
| Simple and multiple linear regression | Class 26 | Nov 15–17 | [12](modules/12-regression-calibration-and-residuals.md), [21](modules/multiple-regression-residualization-and-prediction.md) | Covered |
| Logistic regression | — | Nov 22 | — | Absent |
| Survival analysis | — | Nov 29 | [6](modules/06-time-to-event-data-and-kaplan-meier.md) | Covered |
| Sensitivity, specificity, predictive values | — | Dec 1 | [14](modules/14-base-rates-positive-predictive-value-and-replication.md) | Covered for predictive values; ROC curves are absent |
| Multiple testing and false discovery rate; experimental design and pseudoreplication | — | — | [7](modules/07-multiple-testing-and-false-discovery-rate.md), [4](modules/04-experimental-design-regression-and-reproducibility.md), [the nested-designs lab](labs/01-pseudoreplication-and-nested-designs.md) | Local extension |
| Computing in R | Class 25, studios | Throughout | — | Absent by design: calculations are by hand or calculator |
| Problem sets and exams | Eleven problem sets, two exams and a final | Weekly homework and three exams | Open practice and four ungraded assignments | Absent by design: formative only |

## What 0.7.0 changed

Both comparators teach χ² methods; STAT 205 also teaches 2 × 2 tables in depth and ANOVA, and 18.05 pairs χ² with ANOVA in one class. The package had neither. A new week-5 reading, lesson 26, develops the 2 × 2 table, the three measures of association with an interval for the odds ratio, the χ² test with its expected-count rule, Fisher's exact test from the hypergeometric distribution, and Simpson's paradox with the Mantel–Haenszel odds ratio. A new week-6 reading, lesson 27, develops one-way ANOVA from the partition of sums of squares, the F test and η², follow-up comparisons with pooled variance and a Bonferroni adjustment, and ANOVA from summary statistics.

## Remaining gaps

- Logistic regression and ROC curves (STAT 205, Nov 22 and Dec 1).
- The Cochran–Mantel–Haenszel test, McNemar's test, and tables larger than 2 × 2.
- Tukey's procedure, two-way and repeated-measures ANOVA.
- Statistical computing in R, graded work, measured workload and review by a qualified person.
