# Assignment 1: probability ledgers and conditional laws

This open report connects finite counting with a continuous joint model. It requires original derivations and independent numerical or enumeration checks before selected browser responses. All urn labels, densities and normalized coordinates are invented mathematical inputs. Keep the report, diagrams and code locally; checkpoints do not evaluate their quality or establish a course grade.

## Part A: count the actual finite experiment

An urn contains five distinguishable objects, two marked and three unmarked. Draw two without replacement, with every unordered pair equally likely. Let K be the number marked. List or systematically enumerate the ten possible pairs. Group them by K before calculating probabilities.

The counts are three pairs with zero marked, six with one and one with two, giving probabilities 0.3, 0.6 and 0.1. Verify that their sum is one. Compute E[K]=0.8 and E[K²]=1.0, hence Var(K)=0.36. State why a binomial model with two independent draws and p=0.4 would instead give variance 0.48 and does not describe the same experiment.

Represent K as I1+I2 for the two ordered draw indicators. Each has mean 0.4 and variance 0.24, but their covariance is -0.06. Derive the joint marked probability as (2/5)(1/4), then subtract the product of the marginals. The variance-of-a-sum ledger is 0.24+0.24+2(-0.06)=0.36. The negative covariance reflects depletion, not a measurement artifact.

Explain why ordered draws give twenty equally likely ordered pairs while the unordered experiment gives ten pairs. A consistent calculation obtains the same probabilities from either representation. Mixing an ordered numerator with an unordered denominator is an error even if the resulting number lies between zero and one.

## Part B: change the density, not just one summary

For a separate continuous model use joint density f(x,y)=6y on 0<y<x<1, zero elsewhere. This differs from the foundation's constant triangular density. Verify normalization from the original double integral, then derive fX(x)=3x² and fY(y)=6y(1−y).

Compute E[X]=3/4 and E[Y]=1/2. For Y<1/2, integrate the marginal to obtain probability one half. For a fixed interior x the conditional density is 2y/x² on 0<y<x, so E[Y|X=x]=2x/3. At x=0.6 its value is 0.4. The unconditional mean and this conditional mean refer to different reference sets.

Derive both second moments and E[XY], then calculate variances, covariance and correlation. Verify a total-variance decomposition for Y using the conditional density. Retain the integrals rather than reporting only the final decimal values; another reader should be able to reconstruct the bounds from your support diagram.

## Part C: compare methods and assumptions

Implement exact finite enumeration for the urn and a numerical integral or a correctly generated simulation for the density. If simulating, explain how the generated points follow 6y over the triangle rather than a uniform square or uniform triangle. Check normalization and moments under increasing sample sizes, and report Monte Carlo error separately from a quadrature tolerance.

Compare an independence approximation with the actual joint law in each case. For the urn, show which covariance term it removes. For the density, compare a joint event with the product of its marginals and identify support combinations that cannot occur. A marginal histogram alone cannot establish a joint independence relationship.

Use the foundation's discrete X and X² example to give a separate counterexample to “zero correlation implies independence.” Keep that logical counterexample distinct from the two assignment models, whose covariance need not vanish. A valid special case does not prove a general equivalence.

For the continuous model, compare a conditional event such as Y<X/2 at fixed X with the corresponding unconditional event probability. Derive each reference set explicitly. This additional comparison checks that the program uses the conditional density rather than reusing the marginal distribution by mistake.

## Deliverable and self-review

Retain the sample-space enumeration, probability table, support diagram with a verbal description, marginal and conditional integrals, moment and variance ledgers, and independent computational checks. State all units or normalized scales. Label count, probability, density, expectation and standard deviation correctly; a density can exceed one while a probability cannot.

A successful computation checks the stipulated models. It does not describe a measured population or establish random sampling, causal direction or biological independence. [MIT OCW 18.05 Spring 2022 calendar](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/pages/calendar/) classes 1–7 provide link-only counting/random-variable/joint-law scope. This original AI-assisted assignment imports no source exercise, code, figure or data. General probability theory, measured workload and qualified review remain open; the package stays partial and unreviewed.
