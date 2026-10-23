# Piecewise rates, signed accumulation and integral hypotheses

A negative rate subtracts from a state. It still contributes positively to total travel or total throughput when direction is ignored. A discontinuity in a rate can leave accumulation continuous while destroying its derivative at one instant. These distinctions matter before choosing an antiderivative or a numerical rule. This reading strengthens the [fundamental-theorem sequence](10-accumulation-ftc-and-substitution.md) with explicit sums, sign changes and a proof of the local theorem. All rates are constructed mathematical functions, with no device or biological interpretation.

## Derive an integral from a finite sum

Let v(t)=2t−2 on 0≤t≤3, with time in seconds and velocity in meters per second. The coefficients carry the corresponding units. Divide the interval into n equal pieces of width h=3/n. A right-endpoint sum is

$$R_n=\frac{3}{n}\sum_{i=1}^n\left(\frac{6i}{n}-2\right)
=3+\frac{9}{n}.$$

Use the finite identity sum of i from 1 to n = n(n+1)/2 to obtain the second equality. The limit as n grows is 3 meters. The left-endpoint sum is 3−9/n. Because v increases, the left and right rectangles bracket the signed integral. At n=6 the bounds are 1.5 and 4.5 meters. A negative rectangle below the axis contributes a negative quantity; drawing it as positive area silently changes the question.

The trapezoidal average of these two sums equals 3 for every n because v is affine. Its exactness is a property of this function class, not a general accuracy guarantee for curved or discontinuous data. The midpoint sum is also exact here. Derive the sum before relying on software; it gives a reference for checking an implementation. If the right-sum absolute error must be at most 0.1 meter, 9/n≤0.1 requires n≥90. The inequality is non-strict because the tolerance allows equality.

## Net displacement and total distance

The rate changes sign at t=1. An antiderivative is P(t)=t²−2t. The signed integral from zero to three is P(3)−P(0)=3. The negative contribution from zero to one is −1 and the positive contribution from one to three is 4. Total distance is their absolute sum, 1+4=5 meters. It is also the integral of |v|. Taking the absolute value only after the full signed integral would give 3, which loses the reversal.

For initial position x(0)=10 meters, x(t)=10+P(t). The minimum position is 9 at t=1, and the final position is 13. These are a state minimum, an initial-plus-net-change result and a total-travel result, respectively. None can replace another. If the initial value were instead a cumulative meter reading that only increases, integrating signed velocity would model the wrong state; the meter would accumulate speed |v|.

To integrate an absolute value, locate all sign changes on the interval, split at them, and reverse the sign of negative pieces. A zero that does not change sign does not require a sign reversal. This procedure uses the actual rate model; a sparse table can miss a narrow sign change between samples. Numerical refinement helps only under assumptions about what lies between the observations.

## Why continuity gives the derivative of accumulation

Define A(t)=integral from a to t of v(s) ds. For nonzero h with both endpoints in the domain,

$$\frac{A(t+h)-A(t)}{h}-v(t)
=\frac{1}{h}\int_t^{t+h}[v(s)-v(t)]\,ds.$$

The absolute value is bounded by the largest |v(s)−v(t)| on the small interval between t and t+h, with the same argument for negative h after accounting for orientation. If v is continuous at t, this largest local difference becomes arbitrarily small as h tends to zero. Thus A′(t)=v(t). This is a local statement: continuity of v at the evaluation point supplies the limiting step. It does not require memorizing an antiderivative.

Continuity everywhere is a convenient sufficient assumption for applying the result at every interior point. It is stronger than necessary in many integrable examples, but removing it blindly is invalid. At a discontinuity, check the difference quotient of A itself. An integrable rate can have a jump and still define a continuous accumulation function. Integration and differentiation therefore have different requirements.

## A jump that accumulation does not erase

Define q(t)=−1 for 0≤t<1 and q(t)=2 for 1≤t≤3. Its accumulation from zero is A(t)=−t for t≤1 and A(t)=2t−3 for t≥1. Both expressions give −1 at t=1, so A is continuous there. The left derivative is −1 and the right derivative is 2; A has no two-sided derivative at that point. Setting the value q(1) to zero, two or any other finite number does not alter the integral, because a single-point contribution has zero width. It also cannot make those one-sided derivatives agree.

The integral over the whole interval is −1+4=3. The integral of |q| is 1+4=5. The same net and absolute totals as the earlier smooth model do not imply the same trajectory or differentiability. A cumulative endpoint alone cannot identify the rate history. Construct a third rate with the same net total to test that underdetermination.

## Changing bounds and sign-aware checks

For a continuous rate v and differentiable bounds a(t), b(t), differentiation gives v(b(t))b′(t)−v(a(t))a′(t). It is an endpoint-rate formula with chain factors. For v(s)=s²−1, a(t)=t and b(t)=2t, the result is 2(4t²−1)−(t²−1)=7t²−1. Direct integration gives 7t³/3−t and confirms it. If an endpoint passes through a jump of the integrand, the continuity argument used for the local theorem is unavailable; calculate the one-sided derivatives rather than applying a memorized formula without checking its hypotheses.

Before accepting a result, check units, endpoint orientation, sign-change locations and whether the requested quantity is state, net change or absolute accumulation. Verify an exact model by both a finite-sum limit and an antiderivative when possible. The [cumulative accumulation assignment](../assignments/coursework-04-accumulation-and-synthesis.md) uses different rates and asks for all these checks.

## Provenance and boundary

MIT OCW [18.01SC Single Variable Calculus Fall 2010, Unit 3](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-3-the-definite-integral-and-its-applications/) is a link-only scope comparator for integral definitions, fundamental-theorem reasoning and accumulated quantities. This original explanation, proof and input set were developed with substantial AI assistance; no source problem, diagram or prose was imported. Advanced integration, geometry and series remain in the paired Calculus II package; the pair shares one comparator and claims no two-course equivalence. Broader integration theory, real measurement validation, qualified review and measured workload remain outside this selected lesson. The package is partial and unreviewed.
