# Comparing several groups: one-way analysis of variance

A dose-response experiment, a comparison of three culture media or four donor lines all compare more than two groups. Running a t test for every pair inflates the chance of a false positive and ignores information shared across groups. One-way analysis of variance (ANOVA) asks one question first: is there more variation between the group means than variation within the groups would produce by chance? This lesson builds the ANOVA table, reads its F statistic, and follows a significant F with planned comparisons. All data are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Partition the total variation into between-group and within-group sums of squares, and compute the mean squares, the F statistic and its degrees of freedom.
2. State the null hypothesis of one-way ANOVA and its assumptions, and interpret η² as an effect size.
3. Explain why separate pairwise t tests inflate the family-wise error rate, and compute pairwise comparisons that use the pooled within-group variance with a Bonferroni adjustment.
4. Compute an ANOVA from group means, standard deviations and sizes alone.

## Partitioning variation

Eighteen cultures are randomized to vehicle, a low dose and a high dose, six per group, and a viability index is measured:

| Group | Values | Mean |
| --- | --- | --- |
| Vehicle | 48, 52, 50, 55, 47, 48 | 50.0 |
| Low dose | 53, 58, 51, 57, 55, 56 | 55.0 |
| High dose | 60, 57, 63, 59, 62, 59 | 60.0 |

The grand mean is 55.0. Each value's deviation from the grand mean splits into its group mean's deviation from the grand mean and its own deviation from its group mean, and the squared parts add up:

- **Between groups:** SS_B = Σ nⱼ(ȳⱼ − ȳ)² = 6(−5)² + 6(0)² + 6(5)² = 300, with k − 1 = 2 degrees of freedom.
- **Within groups:** SS_W = Σ Σ (yᵢⱼ − ȳⱼ)² = 104, with N − k = 15 degrees of freedom.

| Source | SS | df | Mean square | F |
| --- | --- | --- | --- | --- |
| Between | 300 | 2 | 150.0 | 21.6 |
| Within | 104 | 15 | 6.93 | |
| Total | 404 | 17 | | |

The mean squares are SS/df. The within-group mean square, MS_W = 6.93, is the pooled variance, the same quantity the [two-group lesson](10-comparing-two-groups-t-tests-and-pairing.md) pools for two groups. Under the null hypothesis that all group means are equal, MS_B also estimates that variance, so F = MS_B/MS_W should be near 1. Here F = 150.0/6.93 = 21.6 on 2 and 15 degrees of freedom, with p = 3.8 × 10⁻⁵.

The effect size η² = SS_B/SS_total = 300/404 = 0.743: about three quarters of the variation in these data lies between groups.

## What a significant F does and does not say

The null hypothesis is that every group mean is equal; the alternative is only that at least one differs. F does not say which. ANOVA assumes independent observations (one per culture, not repeated measurements from the same well), approximately normal residuals within groups and similar group variances. With equal group sizes it is fairly robust to moderate departures; with very unequal variances, Welch's version of ANOVA is safer.

## Following up without inflating error

Three pairwise t tests at α = 0.05 each would, if the tests were independent and every null were true, give a family-wise chance of at least one false positive of 1 − 0.95³ = 0.143, as in the [multiple-testing lesson](07-multiple-testing-and-false-discovery-rate.md). Better follow-up comparisons use the pooled MS_W, which has more degrees of freedom than any pair alone, and adjust for the number of comparisons.

For a pair of groups, SE = √(MS_W(1/nᵢ + 1/nⱼ)) = √(6.93 × 2/6) = 1.52 and t has 15 degrees of freedom:

- high versus vehicle: t = 10.0/1.52 = 6.58, p = 8.8 × 10⁻⁶;
- low versus vehicle and high versus low: t = 5.0/1.52 = 3.29, p = 0.0050.

With a Bonferroni adjustment for three comparisons, each p is multiplied by 3, giving 2.6 × 10⁻⁵ and 0.015, so all three differences remain below 0.05. Tukey's procedure, designed for all pairwise comparisons, is a common alternative. A comparison planned before seeing the data, such as high dose against vehicle, is the strongest evidence; comparisons chosen after looking are exploratory.

## ANOVA from summary statistics

Published papers often give only means, standard deviations and sizes, which are enough. SS_B = Σ nⱼ(ȳⱼ − ȳ)² as before, and SS_W = Σ (nⱼ − 1)sⱼ², because each group's sum of squared deviations is (nⱼ − 1)sⱼ².

## Common mistakes

- Running every pairwise t test and reporting the significant ones.
- Treating replicate wells from one culture as independent observations.
- Concluding from a significant F that every group differs from every other.
- Reading a non-significant F as proof that the means are equal; see the [power lesson](11-power-sample-size-and-small-studies.md).
- Using one-way ANOVA when the groups are ordered doses and a trend is the real question; a regression on dose answers that more directly.

## Worked example

**Problem.** Four media are each tested on five independent cultures. The means are 10.0, 12.0, 13.0 and 15.0, with variances 4.0, 5.0, 3.0 and 4.0. Build the ANOVA table and compute F.

**Step 1: grand mean.** With equal group sizes, ȳ = (10.0 + 12.0 + 13.0 + 15.0)/4 = 12.5.

**Step 2: between groups.** SS_B = 5[(−2.5)² + (−0.5)² + (0.5)² + (2.5)²] = 5 × 13.0 = 65.0, with 3 degrees of freedom, so MS_B = 21.7.

**Step 3: within groups.** SS_W = 4 × (4.0 + 5.0 + 3.0 + 4.0) = 64.0, with 20 − 4 = 16 degrees of freedom, so MS_W = 4.00.

**Step 4: F.** F = 21.7/4.00 = 5.42 on 3 and 16 degrees of freedom, p = 0.0092. At least one medium differs; planned comparisons say which.

## Limits of this lesson

All data are synthetic. Two-way and repeated-measures ANOVA, random effects, Tukey's procedure in detail, Welch's ANOVA, rank-based alternatives such as the Kruskal–Wallis test and the regression formulation of ANOVA are not covered.
