# Forced linear equations: exponential response, complex replacement and undetermined coefficients

The [second-order systems lesson](02-second-order-systems-and-mechanical-response.md) solved unforced constant-coefficient equations through the characteristic equation. Most models are forced: a drive, a feed or a load appears on the right-hand side. The [resonance lesson](08-resonance-and-damping-of-a-spring-mass-damper.md) states the steady amplitude of a driven mass and spring; this lesson shows where that formula comes from, and gives methods that find a particular solution for exponential, sinusoidal and polynomial forcing, including the resonant cases where the usual guess fails. The [Laplace-transform lesson](14-laplace-transform-initial-value-problems.md) later solves the same problems another way. All equations and numbers are synthetic teaching examples.

The [MIT OCW 18.03SC Differential Equations (Fall 2011) Unit II](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-ii-second-order-constant-coefficient-linear-equations/) gives sessions to the exponential response, undetermined coefficients, linear operators and pure resonance, after Unit I's sessions on complex arithmetic and sinusoidal functions, and the [Harvard Math 21b (Spring 2015) syllabus](https://people.math.harvard.edu/archive/21b_spring_15/syllabus.html) gives a lecture to inhomogeneous differential equations. Both are link-only scope comparators; no text, figure or problem is reproduced.

## Learning objectives

By the end of this lesson, you should be able to:

1. Write a constant-coefficient linear equation as p(D)x = f(t), split its general solution into a particular and a homogeneous part, and fit the homogeneous constants to initial conditions.
2. Find particular solutions for exponential, sinusoidal and polynomial forcing with the exponential response formula, complex replacement and undetermined coefficients, using superposition for sums of forcing terms.
3. Handle the resonant cases in which the forcing exponent is a characteristic root, and read the amplitude and phase of a steady-state response.

## Operators and the shape of every solution

Write D for d/dt. The equation x″ + 3x′ + 2x = f(t) becomes p(D)x = f with the characteristic polynomial p(D) = D² + 3D + 2. Because p(D) is linear, two facts follow at once. If x_p is any one solution of the forced equation and x_h solves the unforced one, then x_p + x_h is also a solution; and every solution has this form. So

\[
x(t) = x_p(t) + x_h(t),
\]

where x_h carries the arbitrary constants. Here p(r) = r² + 3r + 2 has roots −1 and −2, so x_h = c₁e^(−t) + c₂e^(−2t). Linearity also gives **superposition**: if the forcing is a sum, find a particular solution for each term and add them.

## The exponential response formula

The key identity is p(D)e^(rt) = p(r)e^(rt): differentiating an exponential only multiplies it by r. So for forcing A e^(rt), with p(r) ≠ 0,

\[
x_p = \frac{A\,e^{rt}}{p(r)} .
\]

For x″ + 3x′ + 2x = 6e^(−3t), p(−3) = 9 − 9 + 2 = 2, so x_p = 3e^(−3t). No unknowns need solving.

**Fitting initial conditions.** The constants belong to the homogeneous part, so fit them only after adding x_p. Starting from rest, with x(0) = 0 and x′(0) = 0, the full solution x = 3e^(−3t) + c₁e^(−t) + c₂e^(−2t) needs 3 + c₁ + c₂ = 0 and −9 − c₁ − 2c₂ = 0, giving c₁ = 3 and c₂ = −6. Fitting the constants to x_p alone, or before adding it, is a common error.

## Complex exponentials

Write j for √−1, as the second-order and phase-portrait lessons do; many mathematics texts write i. **Euler's formula**, e^(jθ) = cos θ + j sin θ, ties exponentials to sinusoids: cos ωt is the real part of e^(jωt) and sin ωt its imaginary part. A complex number a + jb has magnitude √(a² + b²) and an angle whose tangent is b/a, taken in the quadrant of the point (a, b). Dividing by a complex number divides by its magnitude and subtracts its angle. The damped oscillator's complex roots −ζωn ± jωd use the same idea, since e^((−ζωn + jωd)t) = e^(−ζωn t)(cos ωd t + j sin ωd t).

## Complex replacement for sinusoidal forcing

A cosine is the real part of an exponential, F cos ωt = Re(F e^(jωt)). Solve the complex equation p(D)z = F e^(jωt) with the exponential response formula and take the real part:

\[
x_p = \operatorname{Re}\frac{F e^{j\omega t}}{p(j\omega)} = \frac{F}{|p(j\omega)|}\cos(\omega t - \phi), \qquad \phi = \arg p(j\omega).
\]

The complex number p(jω) carries both the gain and the phase lag. For the driven mass, spring and damper m x″ + c x′ + k x = F cos ωt, p(jω) = k − mω² + jcω, so the steady amplitude is F/√((k − mω²)² + (cω)²). Dividing top and bottom by k turns this into the resonance lesson's (F/k)/√((1 − r²)² + (2ζr)²). That lesson's synthetic balance pan (m = 0.2 kg, k = 80 N/m, c = 1.2 N·s/m, F = 0.5 N) driven at ω = 20 rad/s has p(j20) = j24, so the amplitude is 0.5/24 m = 20.83 mm with a 90° lag, the values it states. At ω = 10 rad/s, p(j10) = 60 + j12, giving 8.17 mm and an 11.3° lag.

Complex replacement works for sines too: F sin ωt = Im(F e^(jωt)), so take the imaginary part instead.

## Undetermined coefficients for polynomial forcing

For a polynomial right-hand side, guess a polynomial of the same degree with unknown coefficients and match powers of t. For x″ + 3x′ + 2x = 4t + 2, try x_p = at + b. Substituting gives 3a + 2(at + b) = 4t + 2, so 2a = 4 and 3a + 2b = 2: a = 2, b = −2, and x_p = 2t − 2. By superposition, the forcing 6e^(−3t) + 4t + 2 has x_p = 3e^(−3t) + 2t − 2. The same matching handles a product such as t e^(rt): try (at + b)e^(rt).

## When the forcing matches a characteristic root

If p(r) = 0, the exponential response formula divides by zero: the forcing already solves the unforced equation, so no multiple of e^(rt) can produce it. The fix is one extra factor of t. When p(r) = 0 but p′(r) ≠ 0,

\[
x_p = \frac{A\,t\,e^{rt}}{p'(r)} .
\]

For x″ + 3x′ + 2x = 5e^(−t), p(−1) = 0 and p′(r) = 2r + 3 gives p′(−1) = 1, so x_p = 5t e^(−t). Substituting confirms it: the t e^(−t) terms cancel and 5e^(−t) remains.

**Pure resonance** is the undamped version. For x″ + 16x = 0.8 cos 4t, the forcing frequency equals the natural frequency, p(j4) = 0, and p′(r) = 2r gives p′(j4) = j8. Then x_p = Re(0.8 t e^(j4t)/(j8)) = 0.1 t sin 4t: the amplitude grows linearly without bound in the model. With any damping, p(jω) is never zero for real ω, and the response stays finite, which is why the resonance lesson's peak amplitude depends on ζ.

## Steady state and transient

With damping, every homogeneous term decays, so the particular solution for sinusoidal forcing is the **steady state** the system settles into, and x_h is the **transient** that carries the initial conditions. The decay rate of x_h, not the forcing, sets how long the transient lasts.

## Worked example

**Problem.** A synthetic mount has m = 0.5 kg, c = 2.0 N·s/m and k = 50 N/m and starts at rest. A force 1.0 cos 8t N is applied. Find the steady amplitude and phase lag, check them against the resonance lesson's formula, and describe the transient.

**Step 1: complex gain.** p(j8) = 50 − 0.5 × 64 + j(2.0 × 8) = 18 + j16, so |p(j8)| = √580 = 24.08 N/m and the lag is arctan(16/18) = 41.6°.

**Step 2: steady state.** x_p = (1.0/24.08) cos(8t − 41.6°) m, an amplitude of 41.5 mm.

**Step 3: check.** ωn = √(50/0.5) = 10 rad/s, ζ = 2.0/(2√(50 × 0.5)) = 0.2 and r = 0.8. Then (F/k)/√((1 − r²)² + (2ζr)²) = 0.020/√(0.1296 + 0.1024) = 41.5 mm, the same value.

**Step 4: transient.** The characteristic roots are −2 ± j9.80, so x_h = e^(−2t)(A cos 9.80t + B sin 9.80t). Starting from rest fixes A = −31.0 mm and B = −28.9 mm. The envelope e^(−2t) falls to 0.7% of its starting size by 2.5 s, after which the 41.5 mm steady oscillation is essentially all that remains.

## Common mistakes

- Fitting initial conditions to the particular solution alone, or before adding it.
- Using A e^(rt)/p(r) when p(r) = 0; the resonant case needs t e^(rt)/p′(r).
- Taking the real part before solving the complex equation, or dropping the phase.
- Guessing a polynomial of the wrong degree, or omitting lower-degree terms from the guess.
- Treating the steady state as the whole solution while the transient is still large.
- Applying superposition to a nonlinear equation, where it does not hold.

## Limits of this lesson

All equations and parameters are synthetic. The methods cover linear equations with constant coefficients and exponential, sinusoidal or polynomial forcing, and their products and sums. Variation of parameters, variable coefficients, forcing that is not of these forms and partial differential equations are not developed. Nothing here is an equipment specification or a design rule. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
