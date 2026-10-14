# Continuous Bayesian updating: Beta–Binomial conjugacy and prediction

The finite-prior lesson updates a short list of candidate rates. Here the unknown success probability is continuous: let \(\theta\) be the probability of a positive result on one trial, and represent uncertainty about it with a Beta distribution. This is a conjugate model because binomial data update the two Beta parameters directly.

## Learning objectives

By the end of this lesson, you should be able to:

1. Update a Beta prior after binomial observations and identify the posterior parameters.
2. Compute a posterior mean and integrate over posterior uncertainty for a future count.
3. Explain how prior concentration and the conditional-independence assumptions affect the result.

## Why a Beta prior is conjugate to binomial data

For positive \(\alpha,\beta\), the Beta density is

\[
  f(\theta)=\frac{\theta^{\alpha-1}(1-\theta)^{\beta-1}}{B(\alpha,\beta)},\qquad 0<\theta<1,
\]

where \(B(\alpha,\beta)\) is the normalizing Beta function. If \(s\) successes and \(f\) failures are observed in \(n=s+f\) conditionally independent Bernoulli trials, the likelihood is proportional to \(\theta^s(1-\theta)^f\). Multiplying prior and likelihood gives

\[
  f(\theta\mid D)\propto \theta^{\alpha+s-1}(1-\theta)^{\beta+f-1},
  \qquad \theta\mid D\sim\operatorname{Beta}(\alpha+s,\beta+f).
\]

The binomial coefficient does not depend on \(\theta\), so it cancels when the posterior is normalized. The prior is a distribution over plausible rates; it is not a claim that the unknown rate itself varies from trial to trial.

## Worked example: a continuous prior and ten outcomes

Suppose a teaching assay has prior \(\theta\sim\operatorname{Beta}(2,2)\), with prior mean \(2/(2+2)=0.5\). In a synthetic set of ten independent trials, eight are positive and two are negative. The updated distribution is

\[
  \theta\mid D\sim\operatorname{Beta}(2+8,2+2)=\operatorname{Beta}(10,4).
\]

Its posterior mean is \(10/14=5/7\approx0.714\). Its mode is \((10-1)/(10+4-2)=0.75\), while the observed fraction is \(8/10=0.8\); these are different summaries. The mean is pulled toward the prior mean. With a uniform \(\operatorname{Beta}(1,1)\) prior and the same data, the posterior would instead be \(\operatorname{Beta}(9,3)\), with mean \(0.75\). This small sensitivity comparison makes the prior's contribution visible.

## Prediction averages over parameter uncertainty

For one new Bernoulli trial, the posterior predictive success probability is the posterior mean:

\[
  P(X_{new}=1\mid D)=E[\theta\mid D]=\frac{10}{14}=\frac57.
\]

For three future trials, the probability of exactly two successes integrates the binomial probability over the posterior:

\[
  P(K=2\mid D)=\binom32\frac{B(10+2,4+1)}{B(10,4)}
  =3\frac{10\cdot11\cdot4}{14\cdot15\cdot16}
  =\frac{11}{28}\approx0.393.
\]

This is a Beta–Binomial predictive probability. It differs from plugging the posterior mean into a binomial model, which gives \(3(5/7)^2(2/7)\approx0.437\). Integrating over the shared uncertain rate matters: future trials are dependent marginally after \(\theta\) is averaged out.

## Assumptions and limits

- The observations are exchangeable Bernoulli trials conditional on one common \(\theta\); the model has no treatment covariate, time trend or subgroup effect.
- The Beta prior is specified before seeing these data. Different prior concentration can change the posterior, especially with small samples.
- Extra variation from subjects or batches may make a single-rate binomial model too narrow; a hierarchical model or a different likelihood may be needed.
- A posterior probability is conditional on the model and prior. It is not a p-value, a guarantee about an individual, or proof that the assumptions fit a real assay.
- All values here are synthetic teaching examples, not medical, laboratory or research advice.

MIT OCW 18.05 includes continuous-prior updating and Beta conjugacy in its undergraduate Bayesian unit. This original lesson develops one Beta–Binomial case only; the course does not cover the full Bayesian sequence, normal conjugacy or a broad treatment of maximum likelihood.
