# Impulse response, convolution and transfer functions

The [Laplace lesson](14-laplace-transform-initial-value-problems.md) solved initial-value problems with step inputs and explicitly left out impulses, convolution and transfer functions. Those three ideas belong together. An **impulse** is an idealized blow, such as a hammer strike or a rapid injection, delivered in an instant. The response of a system at rest to a unit impulse, its **impulse response**, turns out to contain everything needed to predict its response to any input, through an integral called a **convolution**. The Laplace transform of the impulse response is the **transfer function**. Its poles decide stability, and its values on the imaginary axis give the amplitude and phase of the steady response to sinusoidal forcing. All systems and numbers here are synthetic teaching examples.

This lesson follows the sequence of step and delta functions, impulse response, convolution, transfer functions and poles in MIT OpenCourseWare's undergraduate [18.03SC, Differential Equations (Fall 2011), Unit III](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/). That course is a scope comparator only; no text or problem is reproduced.

## Learning objectives

By the end of this lesson, you should be able to:

1. Represent an impulsive input with the delta function, find the unit impulse response of a first- or second-order constant-coefficient equation, and interpret an impulse as a sudden jump in velocity.
2. Compute a response from rest as the convolution of the impulse response with the input, and check it with the convolution theorem.
3. Form the transfer function, judge stability from its poles, and compute the gain, phase lag and peak-gain frequency of the steady response to sinusoidal input.

## The delta function as an ideal blow

Consider a pulse of height 1/h lasting from t = 0 to t = h. Its area is always 1. As h shrinks, the pulse grows taller and narrower, but its total effect on a slow system approaches a fixed limit. That limit is written δ(t), the **unit impulse**. It is not an ordinary function; it is defined by what it does inside an integral:

**∫ f(t) δ(t − a) dt = f(a)** for any continuous f and an interval containing a.

This **sifting property** gives its Laplace transform directly: L{δ(t − a)} = e^(−as), and L{δ(t)} = 1.

Physically, an impulse of size J applied to a mass m changes its momentum by J in an instant. For mx″ + bx′ + kx = J δ(t) starting at rest, the position stays continuous but the velocity jumps from 0 to **J/m**. After the blow the forcing is zero, so the motion is a free response that starts from x(0) = 0 and x′(0⁺) = J/m. This is an equivalent way to solve impulse problems without transforms.

## Impulse responses

The **unit impulse response** w(t) is the solution of p(D)w = δ(t) with the system at rest before t = 0, where p(D) is the differential operator.

**First order.** For y′ + ky = δ(t), transforming gives (s + k)W = 1, so W(s) = 1/(s + k) and **w(t) = e^(−kt)** for t ≥ 0. The impulse sets y(0⁺) = 1, and the response then decays freely.

**Second order.** For x″ + 4x′ + 13x = δ(t), W(s) = 1/(s² + 4s + 13) = 1/((s + 2)² + 9), so

**w(t) = (1/3) e^(−2t) sin 3t** for t ≥ 0.

Check: w(0) = 0, so position is continuous, and w′(0⁺) = 1, the unit jump in velocity. A hammer blow of 0.5 N·s on this unit-mass system gives 0.5 w(t). Its largest displacement occurs where tan 3t = 1.5, at t ≈ 0.328 s, and equals **0.0720** in the system's length units.

The step response, the response to a unit step from rest, is the integral of the impulse response. For y′ + 2y it is ∫₀ᵗ e^(−2u) du = (1 − e^(−2t))/2, which is **0.432** at t = 1.

## Convolution: building any response from impulses

Any input f can be viewed as a sequence of thin slices, each a small impulse of size f(u) du delivered at time u. A linear, time-invariant system answers each slice with f(u) du × w(t − u). Adding all slices up to time t gives the response from rest:

**y(t) = ∫₀ᵗ w(t − u) f(u) du = (w ∗ f)(t).**

**Synthetic example.** For y′ + 2y = t from rest, w(t) = e^(−2t), so

y(t) = ∫₀ᵗ e^(−2(t − u)) u du = t/2 − 1/4 + e^(−2t)/4.

At t = 1 this is 0.5 − 0.25 + 0.0338 = **0.2838**. Substituting confirms it: y′ + 2y = (1/2 − e^(−2t)/2) + (t − 1/2 + e^(−2t)/2) = t, and y(0) = 0.

The **convolution theorem** states that L{w ∗ f} = W(s)F(s). Here W = 1/(s + 2) and F = 1/s², and partial fractions on 1/(s²(s + 2)) return the same y(t). The theorem turns a convolution in time into multiplication in s, and it explains why the Laplace solutions of the previous lesson worked: with zero initial conditions, Y(s) = W(s)F(s).

Convolution handles inputs that are awkward to transform, including measured inputs available only as samples. It requires the system to be linear and time-invariant and to start at rest. Nonzero initial conditions add a separate free response.

## Transfer functions and poles

For p(D)x = f with constant coefficients, the **transfer function** is W(s) = 1/p(s). Its **poles** are the roots of the characteristic polynomial p(s). Here they are −2 ± 3i.

- If every pole has a negative real part, w(t) decays, every bounded input gives a bounded response, and the free response dies out. The system is **stable**.
- A pole with positive real part means a growing exponential. A pole on the imaginary axis gives an undamped oscillation, and an input at that frequency produces a response that grows without bound.

The imaginary parts of the poles set the oscillation frequency of w(t), and the real parts set its decay rate.

## Sinusoidal input: gain and phase

For a stable system driven by cos ωt, the steady periodic response is

**x_p(t) = |W(iω)| cos(ωt − φ), with φ = arg p(iω).**

The **gain** |W(iω)| = 1/|p(iω)| scales the amplitude, and the response lags the input by φ. For x″ + 4x′ + 13x, p(3i) = 13 − 9 + 12i = 4 + 12i. Its magnitude is √160 = 12.65, so the gain at ω = 3 is **0.0791** and the phase lag is arctan(12/4) = **71.6°**. At ω = 0 the gain is 1/13 = 0.0769, the DC value.

The gain peaks where |p(iω)|² = (13 − ω²)² + 16ω² is smallest. Setting its derivative to zero gives 13 − ω² = 8, so **ω_r = √5 ≈ 2.236** and the peak gain is 1/12 = 0.0833. For x″ + bx′ + kx with light enough damping, ω_r = √(k − b²/2). The peak lies below the undamped natural frequency √13 ≈ 3.61 and below the impulse response's oscillation frequency of 3. With heavier damping, specifically b² ≥ 2k, there is no peak and the gain only falls.

The same W(s) therefore describes three responses: to an impulse through w(t), to any input through convolution, and to sinusoids through W(iω). This is why engineers characterize systems by their transfer functions.

## Common mistakes

- Treating δ(t) as an ordinary function with value 1 at t = 0; it is defined only by its integral.
- Expecting an impulse to make the position jump; for a second-order mechanical system it makes the velocity jump.
- Writing the convolution as ∫ w(u) f(u) du without the shift t − u.
- Applying convolution with nonzero initial conditions and forgetting the free response.
- Calling a system stable because its impulse response oscillates within bounds; a pole on the imaginary axis is not asymptotically stable and resonates without bound.
- Using the undamped natural frequency as the peak-gain frequency for a damped system.
- Using the transfer-function gain to predict a transient; it describes the steady periodic response.

## Worked example

**Problem.** A synthetic system x″ + 2x′ + 10x = f(t) is at rest. Find its impulse response, its response at t = 0.5 to a unit impulse, its gain and phase lag at ω = 3, and its peak-gain frequency.

**Step 1: transfer function and poles.** p(s) = s² + 2s + 10 = (s + 1)² + 9, with poles −1 ± 3i. Both have negative real parts, so the system is stable.

**Step 2: impulse response.** W(s) = 1/((s + 1)² + 9), so w(t) = (1/3) e^(−t) sin 3t. At t = 0.5, w = (1/3)(0.6065)(0.9975) = 0.2017.

**Step 3: gain and phase.** p(3i) = 10 − 9 + 6i = 1 + 6i, with magnitude √37 = 6.083. The gain is 0.1644 and the lag is arctan 6 = 80.5°.

**Step 4: peak gain.** ω_r = √(10 − 2²/2) = √8 = 2.828, below the undamped √10 = 3.16.

**Step 5: check.** The gain at ω = 0 is 0.1, and the gain at ω_r is 1/|p(i√8)| = 1/√(4 + 32) = 1/6 = 0.167. That is larger than both the DC gain and the 0.1644 at ω = 3, as a peak should be.

## Limits of this lesson

All systems and numbers are synthetic. The lesson treats linear, time-invariant, constant-coefficient equations of first and second order with zero initial conditions unless stated. The delta function is introduced through its sifting property without distribution theory. Fourier series, Bode plots, higher-order and multi-input systems, time-varying coefficients and nonlinear systems are not developed. Practice checks selected values and interpretations; it does not grade a derivation. Original explanation and examples were developed with substantial AI assistance. The course remains partial, unreviewed and formative-only.
