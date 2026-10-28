# Averages, weighted averages and probability densities

The [accumulation lesson](05-integrals-as-accumulation-and-numerical-error.md) turned a rate into a total, and the [improper-integrals lesson](08-improper-integrals-and-comparison.md) let a total run to infinity. Dividing a total by its extent gives an **average**. Weighting that average by a density gives the position or value that a distribution centers on, and a density whose total is exactly 1 is a **probability density**. This lesson develops these three uses of the integral together, because they are one operation. All rates, densities and distributions here are synthetic teaching constructions.

[MIT OCW 18.01SC Single Variable Calculus (Fall 2010), Unit 3 Part C](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-3-the-definite-integral-and-its-applications/part-c-average-value-probability-and-numerical-integration/) has sessions titled "Integrals and Averages", "Integrals and Weighted Averages", "Integrals and Probability" and "Bell Curve, Conclusion". The [Harvard Math 1b (Spring 2004) syllabus](https://abel.math.harvard.edu/archive/1b_spring_04/syllabus.html) has blocks on "Density and slicing", "Average value" and "Probability". Both are link-only scope comparators; no text, figure or problem is reproduced.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the average value of a function or a rate over an interval, locate where a continuous function attains it, and check it against the function's extreme values.
2. Total a quantity from a linear or population density by slicing, and compute a density-weighted average position.
3. Use a probability density: find a normalizing constant, interval and tail probabilities, the mean and the median, and decide with an improper integral whether a density's total and mean are finite.

## Average value

The average value of f over [a, b] is the total divided by the length,

\[
\bar f = \frac{1}{b - a}\int_a^b f(x)\,dx ,
\]

the height of the rectangle on [a, b] with the same area as the region under f. Since the integral lies between (least value)(b − a) and (greatest value)(b − a), the average lies between the least and greatest values of f. For a continuous f, the intermediate value theorem then gives a point c in [a, b] with f(c) = f̄, the **mean value theorem for integrals**.

Take f(x) = x² + 1 on [0, 3]. The integral is 9 + 3 = 12, so f̄ = 12/3 = 4. Solving c² + 1 = 4 gives c = √3 = 1.73, which lies in [0, 3] but is not the midpoint 1.5, because f is not linear.

An average rate is a total over a time. A synthetic assay takes up substrate at the rate r(t) = 6e^(−0.5t) µmol/min over 0 ≤ t ≤ 4 min. The total is ∫₀⁴ 6e^(−0.5t) dt = 12(1 − e^(−2)) = 10.38 µmol, so the average rate is 10.38/4 = 2.59 µmol/min. It lies between the initial rate 6 and the final rate 6e^(−2) = 0.81, and the rate equals its average at t = −2 ln(2.594/6) = 1.68 min. The average is neither the rate at the midpoint, r(2) = 2.21, nor the mean of the endpoint rates, 3.41: for a curved rate only the integral gives it.

## Density and weighted averages

A **linear density** λ(x), in mass per length, assigns a mass λ(x)dx to each slice of length dx, so the total mass of a rod on [a, b] is M = ∫ₐᵇ λ(x)dx. A **population density** in cells per length totals the same way. The rod with λ(x) = 2 + x kg/m on [0, 3] has M = 6 + 4.5 = 10.5 kg, and its average density M/3 = 3.5 kg/m lies between λ(0) = 2 and λ(3) = 5. A capillary segment whose cell density is n(x) = 400e^(−x/2) cells/mm for 0 ≤ x ≤ 6 mm holds N = 800(1 − e^(−3)) = 760 cells.

When a density w(x) ≥ 0 weights each position, the **weighted average** of x is

\[
\bar x = \frac{\int x\,w(x)\,dx}{\int w(x)\,dx}.
\]

For the rod, ∫₀³ x(2 + x) dx = 9 + 9 = 18, so x̄ = 18/10.5 = 1.71 m. That lies between 0 and 3 and to the right of the midpoint 1.5, toward the end where the rod is denser. This is the one-variable form of the center of mass that the [multivariable course](../../calculus-3/modules/23-mass-average-value-and-moments-of-inertia.md) extends to plates and solids.

## Probability densities

A **probability density** on an interval, or on the whole line, is a function f with f(x) ≥ 0 and total area 1. Then

\[
P(a \le X \le b) = \int_a^b f(x)\,dx ,
\]

and the probability of any single exact value is 0, because a single point has no width. The value f(x) is a density, not a probability, so it may exceed 1: the uniform density on [0, 0.5] is f = 2, with total area 2 × 0.5 = 1.

To **normalize**, find the constant that makes the total 1. For f(x) = kx² on [0, 3], ∫₀³ kx² dx = 9k, so k = 1/9.

The exponential density f(t) = (1/4)e^(−t/4) for t ≥ 0 models a synthetic waiting time with a mean of 4 minutes. Its total is an improper integral, lim over b of (1 − e^(−b/4)) = 1, so it is a valid density. Then P(T ≤ 2) = 1 − e^(−0.5) = 0.393, and the tail is also an integral to infinity, P(T > 8) = e^(−2) = 0.135.

The **mean** is the weighted average of the values with the density as the weight; the total weight is 1, so μ = ∫ x f(x) dx. For the waiting time, integration by parts gives μ = ∫₀^∞ (t/4)e^(−t/4) dt = 4 min. The **median** m satisfies ∫₀^m f = 1/2, which gives 1 − e^(−m/4) = 1/2 and m = 4 ln 2 = 2.77 min. The median is below the mean because the long right tail pulls the mean up.

## When the improper integral decides

A density can be valid and still have an infinite mean. The function f(x) = 1/x² for x ≥ 1 has total lim (1 − 1/B) = 1, but its mean is ∫₁^B x·(1/x²) dx = ln B, which grows without bound as B grows. The boundary case p = 1 of the p-test decides it. By contrast f(x) = 2/x³ for x ≥ 1 also has total 1, and a finite mean, ∫₁^∞ 2/x² dx = 2, yet the integral ∫₁^∞ x²·(2/x³) dx = ∫₁^∞ 2/x dx diverges, so the second moment that measures spread does not exist. A normalizing integral can converge while the integrals built from it do not, and each needs its own comparison with a p-integral.

## The bell curve and numerical integration

The standard bell curve is φ(z) = e^(−z²/2)/√(2π). It has no elementary antiderivative, so its probabilities come from numerical integration with the rules of the accumulation lesson. Simpson's rule with 4000 panels gives P(−1 ≤ Z ≤ 1) = 0.6827, P(−2 ≤ Z ≤ 2) = 0.9545 and P(−3 ≤ Z ≤ 3) = 0.9973. The constant 1/√(2π) = 0.399 is the one that makes the total area 1, and integrating over [−8, 8] returns 1 to twelve decimal places because the area beyond 8 is negligible. The density's peak, 0.399, is below 1 here, but, as the uniform density showed, nothing requires it to be.

## Common mistakes

- Forgetting to divide by the length of the interval, or dividing by the wrong one, for an average.
- Averaging the endpoint values, or using the value at the midpoint, instead of integrating.
- Treating a density value as a probability, or requiring a density to be at most 1.
- Computing probabilities before checking that the total area is 1.
- Ending a tail integral at a finite bound instead of at infinity.
- Assuming a density with total 1 must have a finite mean.
- Using the mean where the median is meant, for a skewed density.

## Worked example

**Problem.** A synthetic measurement has the density f(x) = (3/32)x(4 − x) on 0 ≤ x ≤ 4 and f = 0 elsewhere. Check that it is a density, then find P(1 ≤ X ≤ 3), the mean, the peak value, and the average value of f on [0, 4].

**Step 1: normalization.** f ≥ 0 on [0, 4]. ∫₀⁴ x(4 − x) dx = 32 − 64/3 = 32/3, and (3/32)(32/3) = 1.

**Step 2: interval probability.** P(1 ≤ X ≤ 3) = (3/32)[2x² − x³/3] from 1 to 3 = (3/32)(9 − 5/3) = 22/32 = 0.6875.

**Step 3: mean.** ∫₀⁴ x²(4 − x) dx = 256/3 − 64 = 64/3, so μ = (3/32)(64/3) = 2, the center of the symmetric interval, and by the same symmetry the median is also 2.

**Step 4: peak and average.** The peak is f(2) = 3·2·2/32 = 0.375. The average value of f on [0, 4] is (1/4)∫f = 0.25. Any density supported on an interval of length L has average value 1/L, so the peak must be at least 1/L = 0.25, and 0.375 is.

**Step 5: check.** The probability 0.6875 lies between 0 and 1, and it exceeds the 0.5 that a uniform density would give for the middle half of the interval, because this density concentrates near the center.

## Limits of this lesson

All rates, densities and distributions are synthetic constructions, in one variable. Variance and spread, named distributions beyond the exponential and the bell curve, joint densities, estimation and statistical inference are not developed here; the [Probability, Biostatistics and Experimental Design course](../../statistics/modules/01-probability-distributions-and-sampling.md) takes up distributions. The bell-curve values are numerical results, not a derivation of the normalizing constant. Nothing here is a model of a real assay, capillary or measurement. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
