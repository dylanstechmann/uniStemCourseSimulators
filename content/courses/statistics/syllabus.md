# Probability, Biostatistics & Experimental Design

**Maturity: partial. Version: 0.6.0.**

Probability, estimation, hypothesis testing, regression, and design principles for biological and engineering experiments, with reproducibility and uncertainty at the center.

## Prerequisites

Algebra; calculus recommended. Structured required, recommended, and concurrent relationships appear in the manifest and remain subject to author review. This package establishes no university prerequisite equivalency.

## Authored outcomes

- Distinguish sampling variability from measurement error.
- Choose an analysis matched to design and outcome.
- Interpret confidence intervals, p-values, and effect sizes.
- Design controls, replication, randomization, and blinding.
- Create a labeled quantitative graph using an explicit scale and the units of the measured variables.
- Use conditional probability and Bayes' rule to update an event probability from evidence.
- Update a finite prior over model parameters with likelihoods, normalize a posterior, and compute posterior predictive probabilities distinct from p-values.
- Update a continuous Beta prior with binomial observations and compute posterior predictive probabilities under stated assumptions.
- Derive supported joint, marginal and conditional laws and verify covariance and total-variance relationships.
- Construct a likelihood from observed data and exposure, solve selected maximum-likelihood estimates and qualify curvature and boundary conclusions.
- Update a normal mean with known observation variance and distinguish posterior, predictive and shared-parameter uncertainty.
- Fit and diagnose a multiple linear model, verify rank and residual structure and distinguish mean-response from new-observation uncertainty.

## Proposed 14-week schedule

This is a proposed scope, not a measured or reviewed semester. Each week lists its readings; weeks 1, 4, 6, 8 and 13 combine focused instruction with related original lessons.

| Week | Readings and activities | Practice items | Cards |
| --- | --- | ---: | ---: |
| 1 | [Probability, distributions, and sampling](modules/01-probability-distributions-and-sampling.md) | 3 | 2 |
| 2 | [Sources of variability: biological variation, technical error and the standard error](modules/09-variability-technical-error-and-pseudoreplication.md); [Joint laws, conditioning and total variance](modules/joint-laws-conditioning-and-total-variance.md) | 11 | 8 |
| 3 | [Descriptive differences and inferential limits](modules/05-descriptive-evidence-and-causal-limits.md); [Assignment 1: probability ledgers](assignments/coursework-01-probability-ledgers.md) | 4 | 5 |
| 4 | [Estimation, confidence intervals, and effect sizes](modules/02-estimation-confidence-intervals-and-effect-sizes.md); [Effect sizes, confidence intervals and regression to the mean: reading a result for what it can support](modules/08-effect-sizes-intervals-and-regression-to-the-mean.md); [Likelihood estimation and censored exposure](modules/likelihood-estimation-and-censored-exposure.md) | 12 | 10 |
| 5 | [Comparing two groups: the t statistic, Welch's test, paired designs and confidence intervals for a difference](modules/10-comparing-two-groups-t-tests-and-pairing.md) | 7 | 4 |
| 6 | [Hypothesis tests and multiple comparisons](modules/03-hypothesis-tests-and-multiple-comparisons.md); [Many tests at once: family-wise error, Bonferroni and the false discovery rate](modules/07-multiple-testing-and-false-discovery-rate.md); [Assignment 2: exact coverage and randomization](assignments/coursework-02-exact-coverage-and-randomization.md) | 11 | 8 |
| 7 | [Power and sample size: what an experiment can detect, and what a non-significant result means](modules/11-power-sample-size-and-small-studies.md) | 7 | 4 |
| 8 | [Experimental design, regression, and reproducibility](modules/04-experimental-design-regression-and-reproducibility.md) | 3 | 2 |
| 9 | [Regression and calibration: least squares, residuals, R² and prediction](modules/12-regression-calibration-and-residuals.md); [Multiple regression and prediction](modules/multiple-regression-residualization-and-prediction.md) | 11 | 8 |
| 10 | [Resampling and rank-based methods: permutation tests, the bootstrap and the Mann–Whitney test](modules/13-resampling-permutation-and-rank-tests.md); [Assignment 3: regression and design evidence](assignments/coursework-03-regression-and-design-evidence.md) | 9 | 6 |
| 11 | [Time-to-event data: censoring, Kaplan–Meier estimates and hazard ratios](modules/06-time-to-event-data-and-kaplan-meier.md) | 5 | 4 |
| 12 | [Virtual lab 1: pseudoreplication and nested designs](labs/01-pseudoreplication-and-nested-designs.md) | 7 | 4 |
| 13 | [From p-values to evidence: base rates, positive predictive value and replication](modules/14-base-rates-positive-predictive-value-and-replication.md); [Finite Bayesian updating: priors, likelihood and prediction](modules/16-finite-bayesian-updating-and-predictive-checks.md); [Continuous Bayesian updating: Beta–Binomial conjugacy and prediction](modules/17-beta-binomial-conjugacy-and-prediction.md); [Normal conjugacy and shared prediction](modules/normal-conjugacy-and-shared-prediction.md) | 29 | 16 |
| 14 | [Planning a confirmatory study: what a pilot with one p = 0.04 can and cannot support](modules/15-planning-a-confirmatory-study.md); [Confirmatory-protocol dossier project guide (optional, ungraded)](assignments/confirmatory-protocol-project-guide.md); [Assignment 4: inference and prediction dossier](assignments/coursework-04-inference-and-prediction-dossier.md) | 16 | 11 |

## Assessment and study policy

Current practice inventory: 27 lesson/activity routes, 135 public practice items, 92 retrieval cards and 6 Case studio prompts, including five project milestones. Counts do not measure semester depth or independently reviewed quality.

The package has 27 lesson/activity routes: 21 topic readings, four connected reports, one synthetic lab and the optional project guide, with 135 public practice items and 92 retrieval cards. Lessons use short formative checks, including numeric, choice, structured-response, CSV-upload and graph items mapped to provisional objectives. Week 12 is a synthetic-data virtual lab; week 14 pairs the planning lesson with an inactive course-case draft. Activities are open, ungraded practice with no institutional or transferable credit. Workload has not been measured.

## Connected coursework (open, ungraded)

Four original foundations develop joint laws/total variance (week 2), selected censored likelihood/MLE (week 4), multiple-regression residualization/prediction (week 9), and known-variance normal conjugacy/shared prediction (week 13). Four reports require finite counting and joint-density ledgers (week 3), exact coverage/boundary resampling and randomization enumeration (week 6), regression/design evidence (week 10), and a cumulative inference/prediction dossier with original simulation (week 14). Twenty-four checkpoints/cards assess selected values and interpretations. Continuous fields request three significant figures; exact counts have no precision penalty. Retain proofs, plots, code and reports locally; the browser does not evaluate them. The existing nested lab and protocol project remain available. Proposed scheduling and counts do not establish a measured semester workload.

## Optional confirmatory-protocol dossier project (ungraded)

The [confirmatory-protocol dossier project guide](assignments/confirmatory-protocol-project-guide.md) makes the planned project usable as open practice. Week 14 includes the guide, a separate worked example and five rehearsal items; Five Case studio milestones save private self-check responses without submission or grading. The inactive review draft below remains separate.

## Inactive study-design project

An [inactive confirmatory-study protocol draft](assessment-specs/confirmatory-study-protocol-project-draft.md) turns the week-14 planning lesson into a fuller protocol portfolio. It is not scheduled, submitted or graded; the pilot is synthetic, and the draft provides no real-world research guidance.

## Current limitations

The proposed schedule is unmeasured and unreviewed. There are no graded homework sets, midterm, cumulative final or graded integrative project. Bayesian coverage includes finite-prior, Beta–Binomial and one known-variance normal conjugate model. General unknown-variance and hierarchical models, broad likelihood theory and wider distribution/model-selection scope remain outside this selected treatment. References support selected statistical and experimental-unit concepts; all learner examples remain synthetic. Sample-size calculations use normal approximations with rounded critical values unless an exact calculation is stated. No lesson gives a laboratory protocol or medical advice. Qualified human review is required before this course could meet the complete-course standard.

## Sources and licensing

The source map links MIT OCW 18.05 Spring 2022 as a curriculum comparator. Its Reading 15 is a link-only technical reference for the conjugate-prior topic; no source assets are copied or adapted. Read [content/SOURCES_AND_LICENSES.md](../../SOURCES_AND_LICENSES.md) for the software/content license boundary. No affiliation or equivalency is implied.

The 0.6.0 expansion compares actual introductory probability, estimation, simple-regression and finite/Beta-prior readings with [MIT OCW 18.05 Spring 2022 calendar](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/pages/calendar/) and [syllabus](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/pages/syllabus/): classes 1–7 counting/joint laws, 10 likelihood, 14–16 continuous-data/prior/conjugacy, 17–24 tests/intervals/bootstrap and 26 multiple regression. The existing conditional-probability and simple-regression examples were covered; explicit joint-density, likelihood, normal-conjugacy and multiple-regression derivations were absent or shallow. The local algebra/calculus-recommended prerequisite differs from the source's required 18.02. Four open reports do not reproduce its eleven problem sets, two midterms, R quiz, comprehensive final or group/studio format. No source text, problem, figure, code or data is imported. Broader distribution families, unknown-variance/hierarchical inference, coursework depth, qualified review and measured workload remain open.
