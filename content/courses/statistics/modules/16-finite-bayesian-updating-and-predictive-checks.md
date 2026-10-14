# Finite Bayesian updating: likelihood, posterior and prediction

A probability for an event is not the same as a probability for an unknown model parameter. This lesson starts with a small, fully specified Bernoulli model and a finite prior over three possible success probabilities. Every number is synthetic. The goal is to calculate how the evidence reweights the candidate states, predict a separate holdout, and keep those statements distinct from a p-value.

## Learning objectives

1. Calculate a likelihood and normalize prior-weighted likelihoods into a posterior over a finite set of parameter values.
2. Compute posterior odds and posterior predictive probabilities, then compare a prediction with separately held-out data.
3. Distinguish likelihood, posterior probability, predictive probability and p-value; state the model assumptions behind each.

## A discrete prior over a Bernoulli parameter

Let θ be the success probability on each trial. Before seeing data, assign three candidate states:

| State | θ | Prior probability |
|---|---:|---:|
| H₁ | 0.2 | 0.5 |
| H₂ | 0.5 | 0.3 |
| H₃ | 0.8 | 0.2 |

Assume trials are conditionally independent given the same fixed θ. The observed training data are two successes, S,S. For a specified candidate state, the likelihood of this ordered sequence is P(D|Hᵢ)=θᵢ². The three likelihoods are 0.04, 0.25 and 0.64. A likelihood is a probability for the observed data conditional on a state; it is not the probability that the state is true.

Multiply each likelihood by its prior probability. The unnormalized weights are 0.5(0.04)=0.020, 0.3(0.25)=0.075 and 0.2(0.64)=0.128. Their sum, P(D)=0.223, is the model evidence. Divide each weight by this sum to normalize the posterior:

P(H₁|D)=20/223≈0.090, P(H₂|D)=75/223≈0.336, and P(H₃|D)=128/223≈0.574.

The posterior odds for H₃ against H₁ are 0.574/0.090=6.4 (exactly 128/20). H₃ has the largest likelihood and is the maximum-likelihood state, but it does not receive posterior probability 1: the prior and the alternatives still matter.

## Predicting a separate holdout

The posterior predictive probability for success on one new trial averages over parameter uncertainty:

P(S next|D)=Σᵢ P(S next|Hᵢ)P(Hᵢ|D)
=0.2(20/223)+0.5(75/223)+0.8(128/223)≈0.645.

Before viewing a separate two-trial holdout, consider the event K=1: exactly one success, with order ignored. For fixed θ this probability is 2θ(1−θ). Averaging that likelihood over the posterior gives

P(K=1 next|D)=0.32(20/223)+0.50(75/223)+0.32(128/223)≈0.381.

If the held-out pair contains one success, the observation is compatible with this prediction. One pair is a small check, not proof that the Bernoulli assumptions or prior are adequate. Do not update on the held-out values and then call them a prediction.

## Why this is not a p-value

Under the point null θ=0.5, two trials have probabilities 0.25, 0.50 and 0.25 for K=0,1,2. With K=2 observed, a two-sided exact p-value that sums outcomes no more likely than the observed outcome is 0.25+0.25=0.50. This is P(data at least this extreme | the fixed null), not P(the null is true | data). The posterior above answers a different question because it averages over a stated prior on candidate θ values. Neither calculation supplies a universal probability that a scientific claim is true.

## Limits and common mistakes

- Keep P(D|H) (likelihood) separate from P(H|D) (posterior).
- Normalize prior × likelihood by the total evidence before interpreting posterior probabilities.
- A maximum-likelihood state need not have posterior probability 1.
- A posterior predictive probability averages future outcomes over parameter uncertainty; holdout data must remain separate for a genuine predictive check.
- Do not interpret a p-value as a posterior probability of the null.
- The three-state prior and conditionally independent Bernoulli trials are stipulated teaching assumptions, not a fitted model for real data.

This bounded lesson covers the finite-prior strand in MIT 18.05, not its continuous priors, beta conjugacy, broader MLE theory or complete Bayesian unit. All values are synthetic; the lesson is not medical or research advice.
