# Monte Carlo estimates: what the samples estimate and what the seed preserves

**Status:** original instruction and ungraded practice with substantial AI assistance. All distributions, outputs and thresholds are invented teaching models. Work locally in your own Python environment; no learner code runs on the server. This reading extends the probability foundations into computational estimation in week 12.

## Write the estimand first

For a random input U with a specified probability distribution and output Y=g(U), the target μ=E[g(U)] is a mathematical expectation. Monte Carlo replaces it with an average of N simulated outputs: μ_hat=(1/N)sum g(U_i). For independent identically distributed inputs with finite variance, the estimator is unbiased and Var(μ_hat)=Var(Y)/N. Its standard deviation decreases like N^(−1/2). Four times as many independent samples halve this standard deviation; doubling them reduces it by sqrt(2), not two.

An integral can be written as an expectation. If U is uniform on [a,b], then integral_a^b f(x) dx=(b−a)E[f(U)]. Consequently the Monte Carlo estimator is (b−a) times the sample mean. Leaving out the interval width changes its units and numerical value. Sampling from a different distribution without the appropriate weights changes the target as well.

For U uniform on [0,1], estimate the integral of U². The exact expectation is 1/3, E[U⁴]=1/5, and Var(U²)=1/5−1/9=4/45. With N=4000, the exact model standard error is sqrt((4/45)/4000)≈0.00471405. This is the standard deviation of repeated simulated estimates under the declared distribution. It is not a measurement error in a physical system.

## Estimate uncertainty from a finite run

When Var(Y) is unknown, use sample variance s²=sum(Y_i−Y_bar)²/(N−1), then estimated standard error s/sqrt(N). The N−1 correction concerns the sample variance, while the mean still divides by N. With sufficient regularity and a large enough effective sample, a normal approximation gives Y_bar ±1.96 s/sqrt(N) for an approximate 95% interval. It is not a guaranteed bound, and its approximation may be poor for small samples, rare events, strong dependence or heavy tails.

For a hand-checkable illustration, take outputs [0,1,1,2]. Their mean is 1, sample variance is 2/3, and estimated standard error is sqrt(1/6)≈0.408248. These four values demonstrate the arithmetic only. They do not justify a normal confidence interval merely because the formula can be evaluated.

Distinguish the scatter of individual outputs s from uncertainty in their mean s/sqrt(N). Reporting the latter as the spread of possible individual outcomes understates variability. Conversely, a reproducible average does not show that the simulated input distribution represents the real population.

## Indicators estimate probabilities

To estimate P(g(U)>c), define I_i=1 when the event occurs and zero otherwise. Then p_hat=sum I_i/N. Under independent draws, the model variance of p_hat is p(1−p)/N. A common estimated standard error is sqrt(p_hat(1−p_hat)/N), but it collapses to zero after observing no events. Zero observed events do not prove p=0.

For zero events in N independent Bernoulli trials, a one-sided exact 95% upper bound solves (1−p)^N=0.05, giving p_upper=1−0.05^(1/N). At N=1000 it is about 0.00299125. The approximation 3/N is useful here, but name the one-sided confidence convention. If simulation draws are dependent or the event definition changes after inspection, this calculation no longer supplies that bound.

For a different run with 30 events in 200 independent trials, p_hat=0.15 and the plug-in standard error is approximately 0.025249. A normal approximation is an instructional calculation, not an automatic endorsement for every event-count regime. An exact or better-calibrated interval may be preferable for a reported analysis.

## Reproducibility is a contract, not a repeated result by itself

A pseudorandom generator is a deterministic algorithm with state. Recording a seed lets a compatible implementation reconstruct a stream; it does not establish randomness quality, independence, correct code or model truth. Record the generator and software version, seed or state, draw distribution, sample size, batching order and estimator. Different libraries can use different generators even when they accept the same integer seed.

Do not reset the generator to the same seed inside every replicate. That can create identical outputs and destroy the assumed independence between replicates. Give independent runs distinct documented streams, or use a justified stream-splitting mechanism. A sequence that looks irregular in a plot is not evidence that it meets a theorem's assumptions.

```python
import math
import random
import statistics


def estimate_square_mean(count, seed):
    if isinstance(count, bool) or not isinstance(count, int) or count < 2:
        raise ValueError("at least two simulated draws are required")
    generator = random.Random(seed)
    values = [generator.random() ** 2 for _ in range(count)]
    mean = statistics.fmean(values)
    standard_error = math.sqrt(statistics.variance(values) / count)
    return mean, standard_error
```

This small reference uses a private generator rather than mutating global random state. It intentionally stores the outputs to keep the arithmetic visible. A streaming implementation can reduce memory while preserving the estimator; it must implement a stable variance update and test it against the two-pass version. Reproducing this code's numeric output requires the same relevant software behavior, not only the seed label.

## Variance reduction changes the sampling design

For f(U)=U², pair each independent U with 1−U and form Z=[U²+(1−U)²]/2. Then E[Z]=1/3. Direct integration gives E[Z²]=7/60 and Var(Z)=7/60−1/9=1/180. For M independent pairs, standard error is sqrt(1/(180M)). This antithetic construction uses 2M function evaluations, so compare costs against an ordinary estimator with 2M independent evaluations.

At the same evaluation budget, ordinary variance is (4/45)/(2M)=2/(45M), whereas antithetic variance is 1/(180M), eight times smaller for this particular function. The improvement follows from its negative paired covariance. It is not universal: another function can receive no benefit or a different benefit. The M pairs are independent sampling units; the two outputs within a pair are not independent observations for a naive standard-error calculation.

A control variate or importance sampler likewise requires an estimator derivation and a variance/cost comparison. A biased shortcut can look precise. Validate against an analytically solvable problem before using a method where truth is unavailable.

## Separate three sources of uncertainty

Sampling error comes from a finite number of simulated draws. Numerical approximation error comes from computing g, such as discretizing an ODE inside each draw. Model uncertainty comes from assumptions about input distributions, parameters and structure. Increasing N addresses the first, and can reveal rather than remove bias from the second. It does not validate the third.

If g is approximated on a time grid, run both a grid-refinement comparison and a sample-size comparison. Prefer matched random inputs when comparing two numerical solvers so input variability does not obscure their difference, but account for that dependence when analyzing the paired comparison. Record whether the same random draws were intentionally reused.

## Rehearsal and reporting

Use outputs [1,2,3,4,5] for an arithmetic rehearsal: calculate the sample mean, unbiased sample variance and estimated standard error. Separately estimate the model standard error for f(U)=U² with 10000 independent draws. Decide how many draws would reduce that standard error by a factor of three. For zero events among 500 draws, calculate the stated exact one-sided upper bound rather than reporting impossibility.

A report should identify the target expectation or event, its units, sampling distribution, draw count, generator provenance, estimator, uncertainty convention and known-answer checks. Show a convergence comparison without selecting the seed that gives the prettiest answer. A discrepancy with a known integral should trigger diagnosis of sampling, implementation and approximation error; changing the reference truth to match the run is not validation.

## Scope and provenance

[MIT OCW 2.086 Fall 2014 calendar](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-fall-2014/pages/calendar/) places probability, estimation and Monte Carlo in its second unit. This original local lesson covers independent sampling, simple estimators and one variance-reduction calculation; MCMC, rare-event algorithms and general stochastic differential equations remain beyond it. All examples and code are original, CC BY 4.0, developed with AI assistance. No comparator assessment or text was imported. Tests are agent-run consistency checks; qualified review and measured workload remain open.
