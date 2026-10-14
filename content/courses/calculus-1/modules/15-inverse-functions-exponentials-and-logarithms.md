# Derivatives of inverse functions, exponentials and logarithms

The [implicit-differentiation lesson](08-composite-implicit-and-related-rates.md) differentiated equations that relate x and y without solving for y. The same idea gives derivatives for functions defined as inverses: the natural logarithm undoes the exponential, arcsine undoes sine, and a cube-root-like function can undo a polynomial even without a formula. This lesson derives the inverse-function rule, then uses it for logarithms, general exponentials and inverse trigonometric functions. It adds **logarithmic differentiation** for products, quotients and variable powers, and checks results numerically. All functions and data are synthetic mathematical constructions.

The [MIT OCW 18.01SC Single Variable Calculus (Fall 2010) Unit 1](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/1.-differentiation/) places implicit differentiation and inverse functions, the derivative of aˣ, the exponential and its inverse, other exponential functions and a limit involving e together in Part B (Sessions 13–20). This lesson follows that grouping within the local implicit-differentiation week. It uses 18.01SC as a scope comparator only and reproduces no MIT material.

## Learning objectives

By the end of this lesson, you should be able to:

1. Apply the inverse-function rule (f⁻¹)′(b) = 1/f′(a), where f(a) = b, including at points where the inverse has no formula, and state when the inverse is differentiable.
2. Differentiate ln x, logarithms in other bases, aˣ, and arcsine and arctangent, and use the chain rule with them.
3. Use logarithmic differentiation for products, quotients and variable exponents, evaluate the limit that defines e, and use a logarithmic derivative to estimate a sensitivity.

## The inverse-function rule

If f is differentiable and strictly increasing or decreasing near a, it has an inverse g = f⁻¹ near b = f(a), with g(f(x)) = x. Differentiating both sides with the chain rule gives g′(f(x)) f′(x) = 1, so

**g′(b) = 1 / f′(a), where f(a) = b.**

Geometrically, the graph of g is the graph of f reflected across y = x, which turns a slope m into 1/m. The rule fails where f′(a) = 0: the reflected tangent is vertical and g is not differentiable there.

**Synthetic example.** f(x) = x³ + x is strictly increasing because f′(x) = 3x² + 1 > 0. It has no simple inverse formula, but f(1) = 2, so g′(2) = 1/f′(1) = 1/4 = **0.25**. A numerical check: solve x³ + x = 2.001 by bisection to get x ≈ 1.000250, so g changes by about 0.000250 per 0.001 change in b.

## Logarithms and exponentials

Let y = ln x, the inverse of eʸ = x. Differentiating eʸ = x implicitly gives eʸ y′ = 1, so y′ = 1/eʸ = 1/x. Hence

**d/dx ln x = 1/x for x > 0**, and **d/dx ln|x| = 1/x for x ≠ 0.**

With the chain rule, d/dx ln u = u′/u. For example, d/dx ln(x² + 1) = 2x/(x² + 1), which is **0.8** at x = 2.

For any base a > 0, write aˣ = e^(x ln a). Then

**d/dx aˣ = aˣ ln a**, and **d/dx log_a x = 1/(x ln a).**

At x = 3, d/dx 2ˣ = 8 ln 2 = **5.545**. Because ln 2 < 1, the function 2ˣ grows more slowly than eˣ at the same height; e is the one base whose exponential is its own derivative.

**The limit that defines e.** Since ln is differentiable at 1 with derivative 1, ln(1 + h)/h → 1 as h → 0. Setting h = 1/n gives n ln(1 + 1/n) → 1, so

**(1 + 1/n)ⁿ → e ≈ 2.71828.**

The convergence is slow. At n = 100 the value is **2.7048**, short of e by 0.0135, close to the estimate e/(2n) = 0.0136.

## Inverse trigonometric functions

Sine is not one-to-one, so arcsine is defined as the inverse of sine restricted to −π/2 ≤ y ≤ π/2. With y = arcsin x, sin y = x, and implicit differentiation gives cos y · y′ = 1. On the restricted range cos y ≥ 0, so cos y = √(1 − x²) and

**d/dx arcsin x = 1/√(1 − x²), for −1 < x < 1.**

At x = 0.6 this is 1/0.8 = **1.25**. The derivative blows up at x = ±1, where the tangent to the arcsine graph becomes vertical.

Similarly, y = arctan x with tan y = x and sec²y · y′ = 1 gives

**d/dx arctan x = 1/(1 + x²),** which is 0.5 at x = 1.

The restriction of the range is part of the definition. Choosing a different branch changes the sign of the square root and therefore the derivative.

## Logarithmic differentiation

Taking logarithms turns products into sums, quotients into differences and powers into products. For y > 0, differentiate ln y and then multiply by y.

**Variable exponent.** For y = xˣ with x > 0, neither the power rule nor the exponential rule applies, because both base and exponent vary. Take ln y = x ln x, so y′/y = ln x + 1 and

**y′ = xˣ(ln x + 1),** which is 4(ln 2 + 1) = **6.773** at x = 2.

**Product and quotient.** For y = (x + 1)²√(x + 3)/(x + 2)³ at x = 1, the value is 4 × 2/27 = 0.2963. Then

y′/y = 2/(x + 1) + 1/[2(x + 3)] − 3/(x + 2) = 1 + 0.125 − 1 = 0.125,

so y′ = 0.2963 × 0.125 = **0.0370**. Each factor contributes its own term, which is much cleaner than nested product and quotient rules.

**Logarithmic derivatives as sensitivities.** The quantity y′/y = d(ln y)/dx is the relative rate of change. For pH = −log₁₀ c, the derivative is d pH/dc = −1/(c ln 10). A relative change Δc/c therefore shifts pH by about −(Δc/c)/ln 10. A synthetic 10% increase in c lowers pH by about 0.043 in the linear estimate; the exact change is −log₁₀ 1.1 = −0.041. The linear estimate is good for small relative changes and degrades for large ones.

## Common mistakes

- Writing (f⁻¹)′(b) = 1/f′(b) instead of 1/f′(a), with a = f⁻¹(b).
- Forgetting the chain-rule factor: d/dx ln(3x) = 1/x, not 1/(3x).
- Treating aˣ like xⁿ and writing x·a^(x−1).
- Ignoring the range restriction that makes arcsine a function, and so the sign of its derivative.
- Applying the power rule to xˣ.
- Taking logarithms of a function that can be zero or negative without using absolute values.
- Reading (1 + 1/n)ⁿ at moderate n as equal to e.

## Worked example

**Problem.** The synthetic function f(x) = x³ + 2x has inverse g. Find g′(3). Then, for y = xˣ, find y′ at x = 3, and compare a linear estimate with the exact pH change for a synthetic 25% increase in concentration.

**Step 1: inverse slope.** f is increasing, since f′(x) = 3x² + 2 > 0, and f(1) = 3. So g′(3) = 1/f′(1) = 1/5 = 0.2.

**Step 2: variable power.** y′ = xˣ(ln x + 1) = 27(1.0986 + 1) = 56.66 at x = 3.

**Step 3: sensitivity.** The linear estimate is ΔpH ≈ −0.25/ln 10 = −0.109. The exact change is −log₁₀ 1.25 = −0.097. The linear estimate overstates the change by about 12%, because a 25% change is not small.

**Step 4: check.** A centred difference with step 10⁻⁵ reproduces 56.66 for the xˣ derivative. Solving x³ + 2x = 3.001 by bisection gives a change in x of about 0.0002 per 0.001 change, matching g′(3) = 0.2.

## Limits of this lesson

All functions and data are synthetic. The lesson assumes differentiable, strictly monotone functions near the points used, real-valued logarithms and the principal branches of arcsine and arctangent. Hyperbolic functions, the formal construction of eˣ and ln x, complex logarithms and inverse functions of several variables are not developed. Practice checks selected values and interpretations; it does not grade a derivation. The pH example is a mathematical sensitivity, not a laboratory procedure. Original explanation and examples were developed with substantial AI assistance. The course remains partial, unreviewed and formative-only.
