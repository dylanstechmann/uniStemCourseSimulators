# Assignment 3: an estimator with a reproducible uncertainty study

**Open, ungraded implementation practice with substantial AI-assisted authoring.** Proposed placement: week 12 after Monte Carlo instruction. The distributions are synthetic mathematical inputs. Run your own program locally; the browser's selected arithmetic checks do not grade the program or establish statistical validity.

## Define two targets

Let U be uniform on [0,1]. Estimate μ=E[U²]=1/3 and p=P(U²>0.64)=0.2. The probability identity follows from U>0.8 on this domain. State both targets before generating samples. Draw one sequence of independent U values for each run and use it to compute both outputs; the two estimates from a run are then correlated and should not be treated as independent replicate results.

Compare ordinary sampling with the antithetic estimator Z=[U²+(1−U)²]/2 for μ. Use an equal number of function evaluations, not an equal number of pairs versus individual draws. Explain why the antithetic variance reduction derived for U² need not transfer unchanged to the event indicator.

## Part A: implement the estimator contract

Write separate functions for drawing inputs, transforming outputs and calculating summaries. Let a caller supply a private generator or documented seed. Reject an inadequate sample count for estimating sample variance. Return count, mean, sample variance and estimated standard error; do not return a bare average without its sampling basis.

Use hand-calculated output lists to test the summary function independently of the generator. For [0,0,1,1], the mean is 0.5 and the unbiased sample variance is 1/3. Its estimated standard error is sqrt(1/12). For a constant list, the computed sample variance is zero, but explain why an all-zero rare-event run does not prove the unknown event probability is zero.

## Part B: compare cost and sampling error

Choose ordinary sample counts 100,400,1600 and 6400. Declare a documented collection of distinct seeds or streams for repeated runs at each count. For each count, compare empirical scatter across independent estimates with the theoretical standard error sqrt((4/45)/N). Display the individual run estimates rather than only the best-looking one.

A squared error from a single run is noisy and need not decrease monotonically with N. Do not choose the seed after seeing agreement with 1/3. If you reuse nested streams to compare increasing counts, record that the estimates across counts are dependent. That dependence can be useful for comparison, but it changes the interpretation of any pooled summary.

For the antithetic method, compare M pairs against 2M ordinary evaluations. Derive Var(Z)=1/180 and ordinary mean variance 2/(45M), then test whether the empirical comparison is compatible with that model. The analytical ratio is eight for μ in this construction. Counting two outputs inside one pair as two independent pairs gives the wrong standard error.

## Part C: investigate interval behavior

For μ, construct a clearly labeled approximate normal interval using the sample standard error. Across many independent runs, count how often the interval contains the known target. Estimate uncertainty in that empirical coverage fraction rather than reporting it as exact. A single interval either contains or misses the fixed target; the repeated-run procedure is what has a coverage property.

For p, compare a plug-in normal interval with a method that remains meaningful near zero or one. You may implement a justified binomial interval or use a documented library, but state the method and version. For a separate zero-event run with N=1000, derive the one-sided exact 95% upper bound 1−0.05^(1/1000). Do not mix that one-sided convention with a two-sided 95% interval without explanation.

## Part D: separate sampling and model approximation

Pretend the model output is evaluated by an approximate numerical routine g_h(U)=U²+h rather than exactly. Its expectation is 1/3+h. For h=0.01, increasing N concentrates the estimate near the wrong target if the scientific aim remains E[U²]. Compare this deterministic bias with the sampling standard error at N=4000.

Then halve h while keeping the intended distribution fixed. Explain why a two-axis study—sample count and approximation parameter—is more informative than increasing N alone. This deliberately simple bias model stands in for an approximate inner numerical calculation; it makes no claim about a real measurement instrument.

## A worked budget calculation

At N=4000, ordinary model standard error for U² is sqrt((4/45)/4000)≈0.00471405. To halve that value under the same design requires 16000 draws. To reduce it by ten requires 400000 draws. These are mathematical scaling calculations, not measured runtimes. Vectorization, hardware and generator implementation affect elapsed cost.

For zero events among 1000 independent Bernoulli draws, the stated upper bound is approximately 0.00299125. The approximation 3/N gives 0.003. Name both the model and the one-sided confidence convention when reporting this result.

## Self-review and reproducibility record

A complete report includes targets, distributions, generator/software, seeds or stream identifiers, sample counts, independent-run definition, cost metric, estimator formulas, interval conventions, known-answer tests and all prespecified comparison plots. Provide a plain-text description of the same numerical findings. Disclose reused random inputs and AI assistance.

Check your program on the hand lists, verify the analytical expectation and variance independently, and inspect the estimator cost comparison. A matching seed output is evidence of reproducibility, not evidence that a generator models a real population. This assignment introduces no human-subject or biological sampling.

The original packet is CC BY 4.0. [MIT OCW 2.086 Fall 2014 calendar](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-fall-2014/pages/calendar/) is a link-only comparator for Monte Carlo coursework; no assessment or code was copied. Qualified review and workload measurement remain open.
