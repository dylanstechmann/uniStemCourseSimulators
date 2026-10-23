# Assignment 4: inference and prediction dossier

This cumulative open report compares likelihood, sampling uncertainty, posterior uncertainty and future prediction under separate supplied models. It also connects the earlier replication, testing, censoring and study-planning readings. All records and prior values are invented teaching inputs. Retain calculations, code, plots and report locally; selected checkpoints do not grade the complete dossier or establish any real study result.

## Part A: a censored-exposure likelihood

Use five independent event-time records: event at 1, event at 2, censor at 3, event at 4 and censor at 2 normalized time units. Stipulate a common positive exponential event rate and parameter-independent noninformative censoring. Record event indicators separately from observed times.

There are three events and total exposure twelve. The event-time likelihood is proportional to lambda³ exp(−12 lambda), so the interior maximum is lambda_hat=1/4 per time unit and its associated mean waiting time is four time units. The observed information at the maximum is 3/(1/4)²=48 squared time units. The inverse-curvature approximate rate standard error is 1/sqrt48, about 0.14433757 per time unit.

Derive the score and curvature and plot a relative likelihood over positive rates. Compare the correct likelihood with two deliberately wrong ledgers: treating censoring as an event and discarding censored exposure. Explain why neither alternative describes the stipulated experiment. A numerically precise maximum of a wrong ledger is still the wrong estimate for this model.

Discuss the small-event-count limit of a symmetric normal approximation and the distinction between changing time units and changing the parameterization to mean waiting time. Do not label a likelihood curve a posterior until a prior and normalization have been supplied.

## Part B: a separate normal posterior and future observation

The second dataset is unrelated to the event times. Conditional on a common mean mu, four independent measurements have known variance four and observed sample mean three. Use a prespecified normal prior for mu with mean zero and variance four.

Complete the square to obtain posterior variance 4/5=0.8 and mean 12/5=2.4. A single future measurement has predictive variance four plus 0.8, giving standard deviation sqrt4.8, about 2.1908902. Two future observations have covariance 0.8 after the shared mean uncertainty is integrated out, despite conditional independence given mu.

Calculate a central posterior interval for mu with the supplied rounded normal critical value 1.96. Separately calculate a predictive interval for one future measurement and for an average of four future measurements. Show the observation-variance and posterior-mean-variance terms in each. These targets are distinct from the sampling distribution of the original estimator at a fixed true mean.

## Part C: check a procedure through original simulation

Choose a clearly stated true model from the supplied families and specify one statistic and interval procedure before simulating repeated datasets. Record the seed, number of repeated datasets, estimand, event/censoring mechanism or known normal variance, and coverage counting rule. Estimate repeated-sampling coverage and give a binomial Monte Carlo standard error for that coverage estimate.

Compare at least two fixed true parameter values or a deliberately misspecified dependence condition. Do not interpret one high coverage estimate as a guarantee over all parameters or real populations. Keep Monte Carlo uncertainty, finite-sample approximation error, numerical tolerance and model misspecification separate in the report.

Use the exact n=4 binomial enumeration from Assignment 2 as a small check on your coverage-counting implementation. Reproducing that finite reference validates one code path; it does not certify the whole simulator or justify its empirical assumptions.

## Part D: design and evidence ledger

Write a brief plan specifying independent units, the target estimand, inclusion/exclusion and missingness conventions, a primary comparison, and which analyses would be exploratory. Describe allocation, controls, measurement blinding and censoring information that would be needed for the intended interpretation. These are features to identify in the synthetic reasoning exercise, not a real-world laboratory protocol.

For each reported quantity label it as an estimate, likelihood ratio, approximate standard error, frequentist interval, conditional credible interval, predictive quantity or p-value. Give one tempting but unsupported interpretation for each model and explain the missing assumption. Neither a small p-value nor concentrated posterior establishes biological relevance or a unique mechanism.

[MIT OCW 18.05 Spring 2022 syllabus](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/pages/syllabus/) and calendar provide link-only inference/computation scope. All examples and tasks are original and AI-assisted; no external assessment, software or data is imported. Broader theory, real model validation, measured workload and qualified review remain open; the course remains partial and unreviewed.
