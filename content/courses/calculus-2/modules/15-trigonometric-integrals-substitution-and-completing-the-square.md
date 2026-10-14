# Trigonometric integrals, trigonometric substitution and completing the square

The [integration-methods lesson](07-integration-methods-and-domain-checks.md) chose substitution, parts or partial fractions from an integrand's structure, and it stated that it gave no catalog of trigonometric substitutions. This lesson fills that gap with three connected tools. Powers of sine and cosine are integrated by saving one factor or by halving the angle. Radicals such as √(a² − x²) are removed by substituting a trigonometric function whose Pythagorean identity matches the radical. A general quadratic is reduced to one of those forms by completing the square. Each result is checked by differentiation, by geometry or numerically. All functions and intervals are synthetic mathematical constructions.

The [MIT OCW 18.01SC Single Variable Calculus (Fall 2010) Unit 4 Part A](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-4-techniques-of-integration/part-a-trigonometric-powers-trigonometric-substitution-and-completing-the-square/) groups odd and even powers of sine and cosine, integrals of secant and its relatives, trigonometric substitution and completing the square before partial fractions and integration by parts. This lesson follows that grouping within the local week-2 methods block. It uses 18.01SC as a scope comparator only and reproduces no MIT material.

## Learning objectives

By the end of this lesson, you should be able to:

1. Integrate products of powers of sine and cosine by the odd-power substitution or by half-angle reduction, and integrate tangent and secant forms.
2. Choose and carry out a sine, tangent or secant substitution for the square root of a quadratic, convert the bounds, and return to x with a reference triangle and the correct branch.
3. Complete the square to reduce a general quadratic to an arctangent or arcsine form, and check results by differentiation, geometry or numerical integration.

## Powers of sine and cosine

For ∫ sinᵐx cosⁿx dx, look first for an **odd exponent**. Save one factor of the function with the odd power, convert the remaining even power with sin²x + cos²x = 1, and substitute for the other function.

**Odd example.** In ∫₀^(π/2) sin³x cos²x dx the sine power is odd. Write sin³x = (1 − cos²x) sin x and let u = cos x, du = −sin x dx. The bounds become u = 1 and u = 0:

∫₁⁰ −(1 − u²)u² du = ∫₀¹ (u² − u⁴) du = 1/3 − 1/5 = **2/15 ≈ 0.1333**.

The saved sin x dx is exactly what du needs. Without it, the substitution would leave an unmatched factor.

When **both exponents are even**, no factor can be saved. Lower the powers with the half-angle identities

**sin²x = (1 − cos 2x)/2, cos²x = (1 + cos 2x)/2.**

**Even example.** ∫₀^π sin²x dx = ∫₀^π (1 − cos 2x)/2 dx = **π/2**, because cos 2x integrates to zero over a whole number of its periods. For ∫₀^(π/2) sin²x cos²x dx, first use sin x cos x = ½ sin 2x to get ¼ ∫ sin²2x dx, then halve again: ¼ ∫₀^(π/2) (1 − cos 4x)/2 dx = **π/16 ≈ 0.1963**. Each half-angle step halves an exponent and doubles the angle, so the process terminates.

## Tangent and secant

Two building blocks come from logarithms. Writing tan x = sin x/cos x with u = cos x gives

**∫ tan x dx = −ln|cos x| + C.**

Multiplying sec x by (sec x + tan x)/(sec x + tan x) puts the derivative of the denominator in the numerator:

**∫ sec x dx = ln|sec x + tan x| + C.**

Over [0, π/4], these give ln √2 ≈ 0.3466 and ln(1 + √2) ≈ **0.8814**. Products of tangent and secant follow the same idea as sine and cosine: d(tan x) = sec²x dx and d(sec x) = sec x tan x dx. Thus ∫₀^(π/4) sec²x tan x dx becomes ∫₀¹ u du = ½ with u = tan x. The differentiation check is quick. The derivative of −ln|cos x| is sin x/cos x, so the formula is confirmed wherever cos x ≠ 0. That condition matters: an interval containing π/2 crosses a singularity and needs the improper-integral analysis of week 3.

## Trigonometric substitution

A radical of a quadratic resists ordinary substitution because no matching derivative factor is present. Instead, choose x so that a Pythagorean identity collapses the radical:

| Radical | Substitution | Identity used | Range of θ |
| --- | --- | --- | --- |
| √(a² − x²) | x = a sin θ | 1 − sin²θ = cos²θ | −π/2 ≤ θ ≤ π/2 |
| √(a² + x²) | x = a tan θ | 1 + tan²θ = sec²θ | −π/2 < θ < π/2 |
| √(x² − a²) | x = a sec θ | sec²θ − 1 = tan²θ | 0 ≤ θ < π/2 for x ≥ a |

The θ ranges are chosen so that the substitution is one-to-one and the square root simplifies without an absolute value. On −π/2 ≤ θ ≤ π/2, √(a² − a² sin²θ) = a|cos θ| = a cos θ because cos θ ≥ 0 there.

**Sine substitution and a geometric check.** For ∫₀³ √(9 − x²) dx, set x = 3 sin θ, dx = 3 cos θ dθ, with θ from 0 to π/2. The integral becomes 9 ∫₀^(π/2) cos²θ dθ = 9 × π/4 = **9π/4 ≈ 7.069**. The graph y = √(9 − x²) is the upper half of a circle of radius 3, so the integral over [0, 3] is a quarter of the disk, 9π/4. The geometry agrees.

**Tangent substitution.** For ∫₀¹ dx/(1 + x²)^(3/2), set x = tan θ, dx = sec²θ dθ, and θ runs from 0 to π/4. The integrand becomes sec²θ/sec³θ = cos θ, so the integral is sin(π/4) = **√2/2 ≈ 0.7071**. The same integral with a parameter d, ∫ d dx/(x² + d²)^(3/2), arises when contributions from points along a line are summed at a perpendicular distance d. Over −1 ≤ x ≤ 1 with d = 1 it gives 2/√2 ≈ 1.414.

**Secant substitution.** For ∫₂⁴ dx/(x√(x² − 4)), set x = 2 sec θ, dx = 2 sec θ tan θ dθ and √(x² − 4) = 2 tan θ on 0 ≤ θ < π/2. The integrand reduces to ½ dθ, and θ runs from 0 (x = 2) to π/3 (x = 4). The value is **π/6 ≈ 0.5236**. Although the integrand is unbounded at x = 2, the singularity is integrable, as the finite value shows.

**Returning to x.** For an indefinite integral, draw a reference triangle. With x = a sin θ, the opposite side is x, the hypotenuse a and the adjacent side √(a² − x²). Every trigonometric function of θ can then be read off in terms of x. For a definite integral, converting the bounds as above avoids the back-substitution.

## Completing the square

A quadratic with a linear term becomes one of the forms above after completing the square:

- x² + 4x + 13 = (x + 2)² + 9, so ∫ dx/(x² + 4x + 13) = (1/3) arctan((x + 2)/3) + C. Over [−2, 1] this is (1/3) arctan 1 = **π/12 ≈ 0.2618**.
- 5 + 4x − x² = 9 − (x − 2)², so ∫ dx/√(5 + 4x − x²) = arcsin((x − 2)/3) + C. Over [2, 3.5] this is arcsin(0.5) = **π/6**.

The shift u = x + 2 or u = x − 2 is an ordinary substitution with du = dx. A negative leading coefficient must be factored out first, and the square-root form needs the quadratic to be positive on the interval. Here 9 − (x − 2)² > 0 for −1 < x < 5.

## Common mistakes

- Forgetting to save one factor in the odd-power method, leaving no du.
- Using half-angle reduction with the wrong sign: sin²x = (1 − cos 2x)/2, cos²x = (1 + cos 2x)/2.
- Writing √(cos²θ) = cos θ without checking that θ lies where cos θ ≥ 0.
- Converting the integrand to θ but keeping the x bounds.
- Choosing x = a sin θ for √(a² + x²), which produces √(1 + sin²θ) and no simplification.
- Completing the square incorrectly when the leading coefficient is not 1.
- Integrating tan x or sec x across π/2 as if the antiderivative were continuous there.

## Worked example

**Problem.** Evaluate ∫₀^1.5 x²/√(9 − x²) dx and check the result numerically.

**Step 1: choose the substitution.** The radical has the form √(a² − x²) with a = 3, so set x = 3 sin θ, dx = 3 cos θ dθ and √(9 − x²) = 3 cos θ.

**Step 2: convert the bounds.** x = 0 gives θ = 0. x = 1.5 gives sin θ = 0.5, so θ = π/6.

**Step 3: simplify.** The integrand becomes 9 sin²θ × 3 cos θ/(3 cos θ) = 9 sin²θ, an even power.

**Step 4: integrate.** With the half-angle identity, 9 ∫₀^(π/6) (1 − cos 2θ)/2 dθ = 9 [θ/2 − sin 2θ/4]₀^(π/6) = 9 (π/12 − √3/8) ≈ **0.4076**.

**Step 5: check.** A midpoint sum with 200,000 panels gives 0.407637, agreeing to six digits. The integrand is positive and grows toward the upper end, so a small positive value on an interval of length 1.5 is reasonable.

## Limits of this lesson

All integrands and intervals are synthetic. The lesson covers the three standard substitutions, low powers of sine, cosine, tangent and secant, and completing the square. It does not develop reduction formulas for high powers, the Weierstrass t = tan(x/2) substitution, hyperbolic substitutions or integrands without elementary antiderivatives. Practice checks selected numerical values and method choices; it does not grade a written derivation, a reference triangle or the branch argument. Original explanation and examples were developed with substantial AI assistance. The course remains partial, unreviewed and formative-only.
