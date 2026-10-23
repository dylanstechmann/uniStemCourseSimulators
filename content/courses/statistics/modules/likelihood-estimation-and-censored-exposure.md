# Likelihood estimation and censored exposure

Probability describes possible observations under a specified parameter. Likelihood holds the observed data fixed and compares parameter values through that same sampling model. It is a function of the parameter, but it is not automatically a probability distribution over that parameter. This original foundation develops maximum likelihood through an exponential waiting-time model and explicitly includes right-censored exposure.

## Start with a complete waiting-time sample

Stipulate independent exponential waiting times with constant positive rate lambda. The density is lambda exp(−lambda t) for t>=0. Its survival probability beyond t is exp(−lambda t). Both statements belong to a supplied mathematical model; constant hazard is an assumption, not a conclusion from the word “survival.”

For complete times t1,...,tn, the likelihood is lambda^n exp(−lambda T), where T is their sum. The log likelihood is n ln(lambda)−lambda T plus a parameter-independent constant. Differentiating gives score n/lambda−T, so the interior maximum is n/T when T>0. The second derivative −n/lambda² is negative.

In the worked complete sample (1,2,3,4) normalized time units, n=4 and T=10, so the rate estimate is 0.4 per time unit and the corresponding estimated mean waiting time is 2.5 time units. That estimate does not assert that any observed time equals the mean or that a small sample verifies exponential behavior.

## Include censored observations through their actual contribution

If an observation ends without an event at time c, it contributes the probability of surviving beyond c, not an event density at c. Under independent, noninformative censoring with a parameter-independent censoring mechanism, the event-time likelihood is proportional to

$$L(\lambda)=\lambda^d\exp(-\lambda T),$$

where d is the number of observed events and T is total observed exposure, including the censored durations. A fixed observation horizon is one example for which this contribution is appropriate. Informative stopping or censoring that depends on the hidden event process needs a different joint model.

For a distinct rehearsal use four records: event at 2, censor at 3, event at 5 and censor at 6. The total is 16 and d=2, giving rate 1/8 per time unit and estimated mean 8. Treating the two censored records as events would incorrectly use four rather than two in the numerator. Discarding them would incorrectly remove their exposure from the denominator.

## Curvature, approximation and a boundary

The observed information at the positive maximum is d/lambda_hat². For the rehearsal it is 128 squared time units, so the inverse-curvature approximate standard error of the rate is 1/sqrt128, about 0.08838835 per time unit. This is an asymptotic local approximation. Two events do not establish its coverage or justify a symmetric interval that extends into negative rates.

When d=0 and T>0, the likelihood decreases as positive lambda increases. Over the strictly positive parameter space it has a supremum as lambda approaches zero, not an attained positive interior maximum. If a model explicitly extends the parameter space to zero as a no-event limit, the boundary can be included. State the parameter space before calling a boundary a maximum.

## Compare likelihoods without inventing posterior probabilities

At lambda=1/4 versus the rehearsal maximum 1/8, the likelihood ratio is four exp(−two), about 0.54134113. Its log is two ln2−two. It compares how those fixed parameter choices weight the observed records under the model. It is neither a posterior probability of one rate nor a p-value.

A likelihood density may have units, and changing the measurement unit can multiply it by a data-transformation factor independent of the parameter. Such a factor does not change the maximizing physical model. Reparameterizing by mean waiting time m=1/lambda gives maximum m_hat=T/d for d>0; it does not permit treating the likelihood as a normalized density in either coordinate without a prior and appropriate transformation.

For a second sampling family, seven successes in ten independent common-probability Bernoulli trials give likelihood proportional to p^7(1−p)^3. Its interior maximum is p=0.7. Comparing p=0.5 with 0.7 gives a likelihood ratio, while a Beta prior would give a separate normalized posterior. The MLE and posterior mean need not coincide.

## Retain the evidence that the calculation needs

A report should show observed durations, event indicators, exposure total, score, second derivative, parameter domain and units. Compare the full likelihood with a deliberately wrong event-count or exposure ledger and explain the discrepancy. A finite optimizer output without those checks cannot establish that it solved the intended model. Keep empirical model assessment, censoring assumptions and numerical accuracy separate.

[MIT OCW 18.05 Spring 2022 calendar](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/pages/calendar/) class 10 supplies link-only likelihood/MLE scope. The censored example is an original extension connecting the existing survival reading. No source problem or dataset is imported. All records are invented; this is not an empirical survival analysis. The course remains partial and unreviewed.
