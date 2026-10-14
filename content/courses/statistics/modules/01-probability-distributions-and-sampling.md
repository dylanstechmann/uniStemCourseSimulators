# Probability, distributions, and sampling

Statistics begins with a model of how observations could vary. A probability describes uncertainty relative to a stated population, experiment, and set of assumptions; it is not a guarantee about one result. This lesson connects conditional probability and Bayes' rule to distributions and to the variation of a sample mean across repeated samples. Throughout, keep the event, denominator, sampling unit, and independence assumption visible. A calculation can be arithmetically correct while answering the wrong probability question or treating dependent measurements as independent evidence.

## Events and conditional probability

An event is a set of possible outcomes. The probability `P(A)` describes the long-run fraction of outcomes in event `A` under the model. Conditional probability asks what fraction of outcomes in `A` remain among those where another event `B` is known to have occurred:

**P(A | B) = P(A ∩ B) / P(B), provided P(B) > 0.**

The condition changes the reference set. `P(test positive | condition)` is the fraction of people with the condition who test positive; `P(condition | test positive)` is the fraction of positive results that come from people with the condition. These probabilities answer different questions. Independence is another explicit relationship: events `A` and `B` are independent when learning that `B` occurred does not change the probability of `A`, so `P(A | B) = P(A)` when defined. Repeated readings from one specimen often share biological and technical causes, so they should not automatically be treated as independent replicates.

## Updating a probability with Bayes' rule

Bayes' rule reverses a conditional probability by combining the prior frequency of a condition with how likely the observed evidence is under each possible state:

**P(A | B) = P(B | A)P(A) / P(B).**

When `A` and its complement exhaust the possibilities, the denominator can be expanded as **P(B) = P(B | A)P(A) + P(B | not A)P(not A)**. In a diagnostic example, let 10% of a population have a condition. A test returns positive for 90% of people with the condition and for 5% of people without it. Among 1,000 people, the model predicts 100 with the condition, of whom 90 test positive; among 900 without it, 45 test positive. There are 135 positive results, 90 of which are true positives, so

**P(condition | positive) = 90/135 = 2/3 ≈ 0.667.**

The sensitivity is 90%, but the probability that a positive result identifies a person with the condition is about 66.7% under these stated assumptions. The difference comes from the base rate and false positives. The result depends on the population prevalence and on the test-performance estimates applying to that population; a change in either changes the posterior probability. It is not a clinical interpretation for any real test or person.

## Distributions summarize possible values

A random variable assigns a numerical value to each outcome of a probability model. Its distribution records which values are possible and how probability is allocated among them. For a discrete variable, probabilities attach to individual values and sum to one. For a continuous variable, probabilities are areas over intervals under a density; the probability of one exact value is zero in the ideal continuous model. The expected value is a probability-weighted long-run average, while the variance measures squared spread around that average. Neither quantity promises that one observation will equal the mean or lie near it.

For example, a Bernoulli variable records success or failure with success probability `p`; its mean is `p` and its variance is `p(1 − p)`. If `n` independent trials share the same probability, their success count follows a binomial model with mean `np` and variance `np(1 − p)`. Independence and a constant probability are part of that model. A normal distribution can approximate some sums or averages, but its use depends on the data-generating process and sample size; there is no universal cutoff that repairs a biased or dependent sample.

## Sampling distributions and the standard error

A sample statistic is itself random because a different sample would usually produce a different value. The distribution of that statistic across repeated samples from the same population is its sampling distribution. If observations are independent and have finite variance `σ²`, the sample mean `X̄` has expected value `μ` and variance `σ²/n`. Its standard deviation across repeated samples is therefore

**SE(X̄) = σ/√n.**

When `σ` is not known, the sample standard deviation `s` is commonly used to estimate that standard error: **estimated SE = s/√n**. The standard deviation `s` describes spread among individual observations; the standard error describes the expected spread of the estimated mean across repeated samples under the model. They are not interchangeable. If independent biological replicates have sample SD 10 units and `n = 25`, the estimated SE is `10/√25 = 2` units. With known population SD 12 and `n = 36`, the model SE is `12/√36 = 2` units. The units remain those of the measured variable.

Because the standard error scales as `1/√n`, quadrupling the number of independent observations halves the standard error. Doubling `n` does not halve it. This relationship describes sampling variability, not a reduction in instrument error, bias, or biological heterogeneity. If the observations are clustered within animals, batches, plates, or donors, treating every within-cluster measurement as independent can make the estimated standard error too small. The experimental unit and dependence structure determine what counts as an independent replicate.

For many independent observations with a common mean and finite variance, the central limit theorem explains why the sampling distribution of a mean can become approximately normal as sample size grows. The approximation concerns the distribution of the statistic, not a claim that the raw measurements themselves are normal. Strong skew, heavy tails, outliers, finite-sample size, dependence, and selection can matter. The theorem does not create random sampling, remove confounding, or turn a technical measurement into an independent biological replicate.

## A calculation and interpretation routine

1. Define the event or measured quantity and the population or experiment the model represents.
2. For a conditional probability, identify the conditioning event and use the matching denominator. Apply Bayes' rule only after naming the prior and the likelihoods.
3. For a sampling question, identify the experimental unit, whether observations are independent, and whether the population SD or sample SD is supplied.
4. Compute the probability, expected value, variance, or standard error with units where appropriate; check that probabilities lie between zero and one and that the standard error has the measured quantity's units.
5. State what the calculation does and does not establish. Sampling precision is not measurement accuracy, causal evidence, or clinical validity.

The exercises use synthetic examples to develop probability and sampling reasoning. Real analyses also need a defensible sampling frame, measurement process, study design, and model checks. Later lessons address confidence intervals, testing, regression, and nested designs; this introductory reading does not replace those analyses.

## Reference

MIT OpenCourseWare, **18.05 Introduction to Probability and Statistics**, Spring 2022, Reading 3: “Conditional Probability, Independence and Bayes' Theorem.” The course material is provided as a link-only technical reference; this reading does not copy or adapt its prose, examples, exercises, figures, or other assets.
