# Categorical outcomes: proportions, 2 × 2 tables and confounding

Many outcomes are counts of yes or no: whether a mouse developed a lesion, whether a culture was contaminated, whether a patient responded. Comparing two groups on such an outcome means comparing proportions. This lesson sets out the 2 × 2 table, three ways of measuring the difference (risk difference, risk ratio and odds ratio), the χ² test and Fisher's exact test, and what happens when a third variable is ignored. All data are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Arrange binary outcomes for two groups in a 2 × 2 table and compute the risk difference, risk ratio and odds ratio, with a confidence interval for the odds ratio.
2. Compute expected counts and the Pearson χ² statistic for independence, and state when it is unreliable.
3. Compute an exact p-value with Fisher's test from the hypergeometric distribution for a small table.
4. Recognize Simpson's paradox, and combine strata with the Mantel–Haenszel odds ratio.

## The 2 × 2 table and three measures

In a synthetic study, 40 aged mice receive a treatment and 40 receive vehicle, and lesions are counted at the end:

| | Lesion | No lesion | Total |
| --- | --- | --- | --- |
| Treated | a = 12 | b = 28 | 40 |
| Vehicle | c = 24 | d = 16 | 40 |
| Total | 36 | 44 | 80 |

The risks are p₁ = 12/40 = 0.30 and p₂ = 24/40 = 0.60.

- **Risk difference:** p₁ − p₂ = −0.30, thirty fewer lesions per hundred mice. Its approximate 95% interval uses SE = √(p₁(1 − p₁)/n₁ + p₂(1 − p₂)/n₂) = 0.106, giving −0.51 to −0.09.
- **Risk ratio:** p₁/p₂ = 0.50, half the risk.
- **Odds ratio:** (a × d)/(b × c) = (12 × 16)/(28 × 24) = 0.286. The odds of a lesion are 12/28 = 0.43 with treatment and 24/16 = 1.5 with vehicle.

The odds ratio is close to the risk ratio only when the outcome is rare; here, with a common outcome, 0.286 overstates the risk ratio's halving. Odds ratios are still widely used because they are what logistic regression and case-control studies estimate. A confidence interval is computed on the log scale: SE(ln OR) = √(1/a + 1/b + 1/c + 1/d) = 0.472, so the 95% interval is exp(ln 0.286 ± 1.96 × 0.472) = 0.113 to 0.721. The interval excludes 1, the value for no association.

## The χ² test of independence

If treatment and outcome were independent, each cell would be expected to hold row total × column total ÷ grand total: 40 × 36/80 = 18 lesions in each group, and 22 without. Pearson's statistic compares observed with expected counts:

  χ² = Σ (O − E)²/E = (12 − 18)²/18 + (28 − 22)²/22 + (24 − 18)²/18 + (16 − 22)²/22 = 7.27.

A 2 × 2 table has (2 − 1)(2 − 1) = 1 degree of freedom, and χ² = 7.27 on 1 df gives p = 0.0070. For one degree of freedom, χ² is the square of a z statistic, so p = erfc(√(χ²/2)).

The χ² distribution is an approximation that needs adequate expected counts. A common rule asks for every expected count to be at least 5; when it fails, use an exact test.

## Fisher's exact test

A small pilot gives a lesion in 1 of 8 treated mice and 6 of 8 vehicle mice. The expected counts are 3.5, below 5. Fisher's test conditions on the margins: with 7 lesions among 16 mice and 8 mice treated, the number of treated lesions X follows a hypergeometric distribution,

  P(X = x) = C(7, x) × C(9, 8 − x)/C(16, 8).

P(X = 1) = 7 × 36/12,870 = 0.0196 and P(X = 0) = 1 × 9/12,870 = 0.0007, so the one-sided p-value is 0.0203. The two-sided p-value sums the probabilities of all tables at least as unlikely as the one observed, which here adds the mirror-image tables X = 6 and X = 7: p = 0.0406.

## Simpson's paradox and stratification

A third variable can reverse an association when it is ignored. In a synthetic observational dataset, a drug is used more often in severe cases, and severity affects improvement:

| Stratum | Drug improved | Placebo improved | Odds ratio |
| --- | --- | --- | --- |
| Mild | 81/87 = 93.1% | 234/270 = 86.7% | 2.08 |
| Severe | 192/263 = 73.0% | 55/80 = 68.8% | 1.23 |
| Pooled | 273/350 = 78.0% | 289/350 = 82.6% | 0.75 |

The drug does better in each stratum, yet worse in the pooled table, because most drug-treated cases are severe. Severity is a **confounder**: associated with both treatment and outcome. The **Mantel–Haenszel** estimator combines the strata into one adjusted odds ratio:

  OR_MH = Σ(aᵢdᵢ/nᵢ)/Σ(bᵢcᵢ/nᵢ) = 1.45,

where the sums run over strata. It weights strata by size and is appropriate when the odds ratio is similar across strata; when the stratum odds ratios differ a lot, report them separately. Randomization prevents this kind of confounding in experiments, which is one reason randomized designs are preferred.

## Common mistakes

- Reporting an odds ratio as if it were a risk ratio when the outcome is common.
- Using the χ² test with expected counts well below 5.
- Building the table from individual measurements when the unit is the animal or the culture, which is the pseudoreplication of the [nested-designs lab](../labs/01-pseudoreplication-and-nested-designs.md).
- Pooling across a confounder and reading the pooled association as causal.
- Computing a confidence interval for an odds ratio symmetrically on the ratio scale instead of the log scale.

## Worked example

**Problem.** In a synthetic screen, 9 of 60 treated cultures and 21 of 60 control cultures became contaminated. Compute the risk ratio and odds ratio, the χ² statistic, and decide whether χ² is appropriate.

**Step 1: risks.** p₁ = 9/60 = 0.150, p₂ = 21/60 = 0.350, so RR = 0.429.

**Step 2: odds ratio.** (9 × 39)/(51 × 21) = 351/1071 = 0.328.

**Step 3: expected counts.** Contaminated: 60 × 30/120 = 15 per group; clean: 45 per group. All exceed 5, so χ² is appropriate.

**Step 4: χ².** (9 − 15)²/15 + (51 − 45)²/45 + (21 − 15)²/15 + (39 − 45)²/45 = 2.40 + 0.80 + 2.40 + 0.80 = 6.40, on 1 df, p = 0.011.

## Limits of this lesson

All data are synthetic. Continuity corrections, exact intervals for proportions, tables larger than 2 × 2, McNemar's test for paired binary data, tests of homogeneity of odds ratios and logistic regression are not covered.
