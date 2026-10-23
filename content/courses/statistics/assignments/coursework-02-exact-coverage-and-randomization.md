# Assignment 2: exact coverage, resampling and randomization

A procedure's name does not establish its small-sample behavior. This open report enumerates two finite experiments so coverage and a randomization tail can be verified exactly. All outcomes and true-model values are stipulated teaching inputs. Keep the derivations, code and report locally; selected practice responses do not evaluate your full statistical argument.

## Part A: enumerate a confidence procedure

Let K be binomial with n=4 and fixed true probability p=1/2. For each possible observed k, construct the untruncated Wald interval

$$\hat p\pm1.96\sqrt{\hat p(1-\hat p)/4},\qquad\hat p=k/4.$$

The critical value 1.96 is a supplied rounded normal value; this interval is a normal approximation. List its five possible intervals and the binomial probabilities 1,4,6,4,1 divided by sixteen. Mark which intervals contain the fixed value one half.

At k=0 or four the estimated standard error vanishes and the interval collapses to zero or one. Those two outcomes miss one half. The other three cover it. Therefore actual repeated-sampling coverage at this particular p is fourteen/sixteen=0.875, and miss probability is 0.125. Clipping endpoints into [0,1] would not repair these failures. Coverage at one p is not the procedure's coverage function over the whole parameter space.

## Part B: a boundary bootstrap and an exact alternative

For the observed all-failure sample, every ordinary nonparametric bootstrap resample also has zero successes. The bootstrap distribution of the sample proportion is degenerate at zero, so its percentile interval collapses too. More resamples cannot create unobserved successes or fix this plug-in boundary problem. Zero estimated sampling spread does not establish that the true probability is known.

For comparison define the central equal-tail exact binomial interval with 0.025 in each tail, including the natural parameter boundaries. At k=0 its upper endpoint solves P_p(K=0)=(1−p)^4=0.025, giving 1−0.025^(1/4), about 0.60236464. Distinguish this two-sided 95% endpoint from the one-sided 95% endpoint that uses 0.05.

For each of the five observed counts, check whether the exact interval contains one half by the corresponding binomial tail conditions. All five do, so its coverage at p=1/2 is one. Exact refers to the finite sampling model, and discrete intervals can be conservative. It does not mean their pointwise coverage equals exactly 0.95 everywhere or that an observed interval has a frequentist parameter probability.

## Part C: an exact randomization distribution

In a separate experiment four units have fixed outcomes (0,1,3,4) under a sharp no-effect null. Exactly two units are assigned to treatment, uniformly among the six possible allocations, with the rest controls. Observed treatment outcomes are (3,4). Define the statistic as treatment mean minus control mean, so its observed value is three.

Enumerate all six allocations and their statistics: -3,-1,0,0,1,3. Define the two-sided tail by absolute statistic at least as large as the observed absolute statistic, including ties. Two allocations meet that rule, giving exact p=2/6=1/3. Keep the two zero-statistic allocations separate; equal statistic values do not merge their probabilities.

The reference distribution comes from the specified random assignment and sharp null, with outcomes fixed across those assignments. It is not automatically appropriate for arbitrary observational groups, dependent units or a weak null involving only equal means. The p-value is a probability of this tail under the reference experiment, not a probability that the null is true.

Distinguish the two probability spaces in this report. Binomial coverage repeats new outcomes at a fixed true probability. The randomization calculation repeats assignments of the same fixed sharp-null outcomes. Combining their denominators would change the experiment and give no justified inference for either supplied model.

## Deliverable and checks

Retain the complete coverage table, interval/tail convention, boundary-resampling explanation, all assignment labels and statistics, and exact enumeration code or arithmetic. Show how a strict rather than inclusive tail would change this example and explain why the convention must be prespecified. Distinguish finite enumeration from simulation; a Monte Carlo estimate needs an error budget and a declared counting convention.

Connect the results to the existing t-test, bootstrap and study-design readings. Approximation choice, experimental unit, randomization and an explicit estimand remain necessary even when arithmetic is exact. [MIT OCW 18.05 Spring 2022 calendar](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/pages/calendar/) classes 17–24 provide link-only testing/interval/resampling scope. These original examples import no source problem or data. They establish no real study conclusion, measured workload or qualified review; the course remains partial and unreviewed.
