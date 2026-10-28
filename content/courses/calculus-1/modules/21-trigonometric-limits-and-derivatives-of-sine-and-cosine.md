# Trigonometric limits and the derivatives of sine and cosine

The [derivative-rules lesson](02-derivative-rules-and-chain-rule.md) built a toolbox for products, quotients and nested functions, and the [limits lesson](07-limits-continuity-and-derivative-definition.md) defined the derivative as a limit of difference quotients. Neither differentiated a sine or a cosine, yet oscillating quantities such as pulsatile flow, a breathing signal or a vibrating sensor are modeled with them. Their derivatives need two special limits that cannot be found by substituting the limit point. This lesson proves those limits with the squeeze theorem, derives the derivatives of sine, cosine and tangent, and uses them to read the slope of a sinusoidal signal. Angles are in radians throughout, and every signal here is synthetic.

[MIT OCW 18.01SC Single Variable Calculus (Fall 2010), Unit 1 Part A](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/1.-differentiation/part-a-definition-and-basic-rules/) has sessions titled "Derivatives of Sine and Cosine" and "Limits of Sine and Cosine". The [Harvard Math 1a (Spring 2005) calendar](https://abel.math.harvard.edu/archive/1a_spring_05/calendar_mwf.html) has meetings on "Calculating Limits using the Limit Laws" and "Derivatives of Trigonometric Functions". Both are link-only scope comparators; no text, figure or problem is reproduced.

## Learning objectives

By the end of this lesson, you should be able to:

1. Prove and use the limits of (sin h)/h and (cos h − 1)/h with the squeeze theorem, and evaluate related trigonometric limits.
2. Differentiate sine, cosine and tangent, alone and combined through the product, quotient and chain rules.
3. Interpret the derivative of a sinusoidal model: its largest slope, its zero-slope points, the oscillator relation x″ = −ω²x, the factor that radians introduce, and the small-angle approximation.

## Why sine needs two special limits

The addition formula sin(x + h) = sin x cos h + cos x sin h turns the difference quotient into

\[
\frac{\sin(x+h) - \sin x}{h} = \sin x\cdot\frac{\cos h - 1}{h} + \cos x\cdot\frac{\sin h}{h}.
\]

So the derivative of sine exists exactly when both limits as h → 0 exist. Substituting h = 0 gives 0/0 each time, so numbers help first:

| h | (sin h)/h | (cos h − 1)/h |
| ---: | ---: | ---: |
| 0.5 | 0.9589 | −0.2448 |
| 0.1 | 0.9983 | −0.0500 |
| 0.01 | 0.99998 | −0.0050 |
| 0.001 | 0.9999998 | −0.0005 |

The first column appears to approach 1 and the second 0. A table suggests a limit, though, and a proof needs more.

## The squeeze theorem

If g(h) ≤ f(h) ≤ k(h) for all h near a point, and g and k both approach the same limit L at that point, then f is squeezed to the same limit L. The theorem turns a limit that cannot be found directly into two limits that can.

## The limit of (sin h)/h

For 0 < h < π/2, compare three areas in the unit circle: the small triangle with area ½ sin h, the circular sector of angle h with area ½h, and the larger triangle with area ½ tan h. The sector lies between the triangles, so

sin h < h < tan h.

Dividing by sin h > 0 gives 1 < h/sin h < 1/cos h, and taking reciprocals gives

\[
\cos h < \frac{\sin h}{h} < 1 .
\]

As h → 0⁺, cos h → 1 by continuity, so the squeeze theorem gives (sin h)/h → 1. The quotient is an even function, so the left-hand limit is the same. At h = 0.5 the bounds are cos 0.5 = 0.8776 and 1, and (sin 0.5)/0.5 = 0.9589 lies between them.

The sector area ½h is true only for angles in radians, so the limit, and everything built on it, depends on radian measure.

## The limit of (cos h − 1)/h

Multiply the numerator and denominator by cos h + 1:

\[
\frac{\cos h - 1}{h} = \frac{-\sin^2 h}{h(\cos h + 1)} = -\frac{\sin h}{h}\cdot\frac{\sin h}{\cos h + 1}\;\longrightarrow\; -1\cdot\frac{0}{2} = 0 .
\]

The same device gives related limits. (1 − cos x)/x² = ((sin x)/x)²/(1 + cos x) → 1/2, and at x = 0.1 the quotient is already 0.4996. A constant inside the sine rescales the variable: sin(3x)/x = 3·sin(3x)/(3x) → 3·1 = 3.

## The derivatives

With both limits in hand, the difference quotient for sine approaches sin x·0 + cos x·1, so

\[
\frac{d}{dx}\sin x = \cos x,\qquad \frac{d}{dx}\cos x = -\sin x .
\]

The cosine case uses cos(x + h) − cos x = cos x (cos h − 1) − sin x sin h in the same way. A numerical check at x = 1 gives a central-difference slope of the sine of 0.540302, which equals cos 1. The quotient rule gives d/dx tan x = sec²x = 1/cos²x, which is 2 at x = π/4.

The chain rule handles a signal with its own frequency and phase:

\[
\frac{d}{dt}\bigl[A\sin(\omega t + \varphi)\bigr] = A\omega\cos(\omega t + \varphi).
\]

The inner derivative ω multiplies the result, and a higher frequency means a steeper signal.

## Slope and the oscillator relation

A synthetic pulsatile flow is Q(t) = 5 + 2 sin(2πt/0.8) mL/s, with a period of 0.8 s. By the chain rule,

Q′(t) = (4π/0.8) cos(2πt/0.8) = 15.71 cos(7.854t) mL/s².

The largest slope is Aω = 15.71 mL/s², reached at t = 0 and every 0.8 s afterward, where the flow crosses its baseline of 5 going upward. The slope is zero at the peak (7 mL/s, at t = 0.2 s) and at the trough. At t = 0.1 s the flow is 6.41 mL/s and still rising at 11.11 mL/s².

Differentiating twice shows a relation that characterizes every sinusoid. For x(t) = A sin ωt, x′ = Aω cos ωt and

x″ = −Aω² sin ωt = −ω²x.

For x = 3 sin 2t this reads x″ = −12 sin 2t = −4x. The acceleration points back toward the baseline in proportion to the displacement, which is why this equation describes oscillation; the [second-order systems lesson](../../differential-equations/modules/02-second-order-systems-and-mechanical-response.md) of the Differential Equations course solves it in general.

## Radians matter

If x is measured in degrees, then sin(x°) = sin(πx/180), and the chain rule gives

\[
\frac{d}{dx}\sin(x^\circ) = \frac{\pi}{180}\cos(x^\circ) \approx 0.01745\cos(x^\circ).
\]

At x = 30° the slope is 0.01511 per degree, not 0.866. Using d/dx sin x = cos x with degrees would be wrong by a factor of 57.3, and the squeeze argument above fails outside radian measure, which is why calculus uses radians.

## The small-angle approximation

The tangent line to sine at 0 has slope cos 0 = 1, so sin x ≈ x near 0, a linear approximation of the kind in the [approximation lesson](12-local-approximations-newton-and-sensitivity.md). Its relative error is 0.67% at x = 0.2, 4.29% at x = 0.5 and 18.8% at x = 1.0, so the approximation is good only for small angles.

## Common mistakes

- Using degrees where the formulas need radians.
- Writing d/dx cos x = sin x, with the wrong sign.
- Forgetting the inner factor, so that d/dt sin(ωt) is written cos(ωt) instead of ω cos(ωt).
- Substituting h = 0 into (sin h)/h, or cancelling the "sin" as if it were a factor.
- Using the squeeze theorem when the two bounding functions have different limits.
- Differentiating sin²x as 2 cos x instead of 2 sin x cos x.

## Worked example

**Problem.** A synthetic sensor signal is S(t) = 10 + 4 sin(0.5t − 0.6), with t in seconds. Find S′(t), the largest rate of change and when it occurs, S′(2) and S″(2), and check the oscillator relation.

**Step 1: derivative.** By the chain rule, S′(t) = 4·0.5·cos(0.5t − 0.6) = 2 cos(0.5t − 0.6).

**Step 2: largest slope.** The cosine is 1 when 0.5t − 0.6 = 0, so t = 1.2 s. There S′ = 2 and S = 10, the baseline.

**Step 3: slope at 2 s.** S′(2) = 2 cos 0.4 = 1.842.

**Step 4: curvature.** S″(t) = −sin(0.5t − 0.6), so S″(2) = −sin 0.4 = −0.389. Since S(2) = 10 + 4 sin 0.4 = 11.558, the oscillator relation S″ = −ω²(S − 10) with ω² = 0.25 gives −0.25 × 1.558 = −0.389, as required.

**Step 5: check.** A central difference of S with step 0.00001 at t = 2 gives 1.8421, matching Step 3. The signal peaks at S = 14 where S′ = 0, at t = 2(π/2 + 0.6) = 4.34 s.

## Limits of this lesson

All signals and flows are synthetic mathematical models. The squeeze argument for (sin h)/h relies on the area of a circular sector in radians, and a fully formal treatment, which defines sine by a series or an integral, belongs beyond Calculus I. The lesson covers sinusoids of constant amplitude and frequency; damping, Fourier series and the derivatives of general periodic functions are not developed. Nothing here is a model of a real flow, sensor or measurement. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
