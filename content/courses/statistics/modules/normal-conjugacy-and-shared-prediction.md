# Normal conjugacy and shared predictive uncertainty

The existing Beta–Binomial lesson updates a probability from binary observations. A continuous measured outcome needs a different likelihood. Here an unknown normal mean receives a normal prior while the observation variance is explicitly known. Completing the square derives the posterior, and a separate variance ledger distinguishes uncertainty about the mean from variation of future observations. All numerical inputs are invented teaching values.

## Declare the conditional model and prior

Let Y1,...,Yn be independent conditional on a common mean mu, each normally distributed with mean mu and known variance sigma². Put a normal prior on mu with mean m0 and variance v0>0, specified before these observations. The shared unknown mean is not assumed to change independently between observations.

As a function of mu the likelihood is proportional to exp[−n(mu−ybar)²/(2sigma²)]. Multiplying by the prior adds (mu−m0)²/(2v0) in the exponent. Collect the quadratic and linear terms and complete the square:

$$v_n=\left(\frac1{v_0}+\frac n{\sigma^2}\right)^{-1},\qquad
m_n=v_n\left(\frac{m_0}{v_0}+\frac{n\bar y}{\sigma^2}\right).$$

The posterior is normal with mean mn and variance vn. Precision is inverse variance, not inverse standard deviation. The mean is a precision-weighted combination of the prior mean and sample mean. A stronger prior precision pulls the posterior mean more strongly toward its center under this model; it does not make a misspecified prior scientifically correct.

## Worked posterior and a new observation

Choose prior mean 5 and variance 9, known observation variance 9, n=4 and sample mean 8. Posterior precision is five/nine, variance 9/5=1.8 and mean (5+32)/5=7.4. A new observation has posterior predictive mean 7.4 and variance sigma²+vn=10.8. The posterior standard deviation of mu is sqrt1.8, while the predictive standard deviation of one observation is sqrt10.8.

The extra term follows from total variance: conditional future variance is sigma², and variance of the conditional mean is vn. An interval for mu and an interval for a future noisy value therefore have different widths, even though their centers agree.

## Distinct rehearsal and a future average

Use prior mean 4 and variance 4, known observation variance 16, n=3 and sample mean 6. Posterior precision is seven/sixteen. The posterior variance is 16/7 and mean 34/7. A single new observation has variance 128/7 and standard deviation about 4.27618.

For an average of two future observations, conditional observation variance is 16/2, so predictive variance is 8+16/7=72/7. Its standard deviation is about 3.20713. This is uncertainty for a future average before seeing those observations. It is not the posterior variance after actually collecting and updating with them.

A central approximate 95% credible interval for mu uses mn plus or minus 1.96 sqrt(vn), with the rounded normal critical value explicitly supplied. Its conditional posterior probability is approximately 0.95 under this prior and likelihood. This statement is distinct from a repeated-sampling coverage claim for a fixed true mean.

## Future observations share parameter uncertainty

Conditional on mu, two future observations are independent. After mu is integrated out, their covariance is vn, because both conditional means equal that same uncertain mu. In the rehearsal the covariance is 16/7 and correlation is (16/7)/(128/7)=1/8. Marginal independence would incorrectly remove that covariance and overstate how much a future average reduces uncertainty.

For m future observations the average has variance sigma²/m+vn. The observation-noise term shrinks with m, while the currently unresolved mean uncertainty remains. Once new data are observed, a subsequent posterior update can reduce vn. Averaging prospective values under the current posterior and updating on realized values are different operations.

## Model checks and boundaries

Known sigma² is a substantial stipulation. Replacing it with a sample variance and silently keeping the same normal posterior is a different procedure that needs justification. Unknown variance, unequal conditional variances, clustering, covariates and changing means require richer models. The existing nested-design lab explains why repeated measurements do not automatically become independent units.

Retain the completed-square coefficients, variance units and a sensitivity comparison with another prespecified prior. A simulation can check conditional predictive moments, but simulated coverage under an invented model does not validate that model for real measurements. Neither posterior concentration nor a narrow interval proves causality, unbiased sampling or scientific importance.

[MIT OCW 18.05 Spring 2022 calendar](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/pages/calendar/) classes 14–16 identify continuous-data/prior, conjugacy and probability-interval scope. This is an original selected normal case, not the full Bayesian curriculum; no source text, exercise or data is imported. The course remains partial and unreviewed.
