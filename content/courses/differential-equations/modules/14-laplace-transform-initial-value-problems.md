# Laplace transforms for initial-value problems: initial data and delayed steps

Laplace transforms turn a constant-coefficient linear differential equation into an algebraic equation in a new variable, (s). The initial values enter that algebra directly, and a shifted unit step represents a force that begins after a delay. This lesson develops those tools for first- and second-order initial-value problems, then checks the answers against direct solutions and initial conditions. All numerical examples are synthetic.

This is one bounded part of the broader transform unit in MIT OpenCourseWare's undergraduate [18.03SC, Differential Equations (Fall 2011), Unit III](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/). The linked course is a curriculum comparator only; this lesson does not reproduce its text or problems. Fourier series, impulse inputs, convolution, and a full transfer-function treatment remain outside this lesson; the companion week-6 reading takes up impulses, convolution and transfer functions.

## Learning objectives

By the end of this lesson, you should be able to:

1. Transform first and second derivatives while retaining the initial values.
2. Solve a constant-coefficient initial-value problem by algebra and partial fractions, then check it in the original equation.
3. Represent a delayed step input and verify the response's initial conditions and continuity at the delay.

## Transform rules used here

For a function (y(t)), write its Laplace transform as (Y(s)=\mathcal{L}\{y(t)\}). For piecewise-continuous functions that do not grow faster than an exponential, the transform is defined for sufficiently large (s) by

\[
Y(s)=\int_0^\infty e^{-st}y(t)\,dt.
\]

The derivative rules follow from integration by parts:

\[
\mathcal{L}\{y'\}=sY(s)-y(0),\qquad
\mathcal{L}\{y''\}=s^2Y(s)-s y(0)-y'(0).
\]

The initial values are part of these formulas. Dropping either term changes the initial-value problem. A small transform table is enough for the examples below:

| Time function | Laplace transform |
|---|---|
| (1) | (1/s) |
| (e^{at}) | (1/(s-a)) |
| \(\sin(\omega t)\) | \(\omega/(s^2+\omega^2)\) |
| \(\cos(\omega t)\) | \(s/(s^2+\omega^2)\) |
| (H(t-a)g(t-a)), (a\geq0) | (e^{-as}G(s)), where (G=\mathcal{L}\{g\}) |

Here (H(t-a)) is zero before (t=a) and one after it. The shift formula applies when the delayed part is written as a function of the elapsed time (t-a). For example, (H(t-3)(t-3)e^{-2(t-3)}) transforms to (e^{-3s}/(s+2)^2). Writing the delay this way keeps the response zero before the input begins.

## Worked example: nonzero initial data

Solve

\[
y''+3y'+2y=0,\qquad y(0)=1,\quad y'(0)=0.
\]

Let (Y=\mathcal{L}\{y\}). Transform each term and insert the initial values:

\[
(s^2Y-s)+3(sY-1)+2Y=0,
\]

so

\[
Y(s)=\frac{s+3}{(s+1)(s+2)}=\frac{2}{s+1}-\frac{1}{s+2}.
\]

Taking the inverse transform gives

\[
y(t)=2e^{-t}-e^{-2t}.
\]

The initial checks are (y(0)=2-1=1) and (y'(0)=-2+2=0). Directly, the characteristic equation is ((r+1)(r+2)=0), so the general homogeneous solution is (A e^{-t}+B e^{-2t}). Applying the same initial values gives (A=2), (B=-1), matching the transform result. This independent solution check catches algebra and sign errors.

## Worked example: a delayed constant input

Consider a normalized second-order system initially at rest:

\[
x''+3x'+2x=H(t-2),\qquad x(0)=0,\quad x'(0)=0.
\]

The transform of the delayed step is (e^{-2s}/s), so

\[
X(s)=\frac{e^{-2s}}{s(s+1)(s+2)}
=e^{-2s}\left(\frac{1}{2s}-\frac{1}{s+1}+\frac{1}{2(s+2)}\right).
\]

First invert the expression in parentheses, then apply the time shift:

\[
x(t)=H(t-2)\left[\frac12-e^{-(t-2)}+\frac12e^{-2(t-2)}\right].
\]

Before (t=2), the response is zero. At the switching time, the bracket equals zero. Its derivative with respect to elapsed time is (e^{-\tau}-e^{-2\tau}), also zero at \(\tau=0\). Thus displacement and velocity are continuous across the delayed force; the acceleration changes when the force turns on.

As a direct check after the switch, set \(\tau=t-2\). The response (g(\tau)=\tfrac12-e^{-\tau}+\tfrac12e^{-2\tau}\) has (g(0)=g'(0)=0), and substituting it into (g''+3g'+2g) gives (1). Before the switch, (x=0) and the forcing is zero. The piecewise solution therefore satisfies the original equation and initial data on both intervals.

## Partial fractions and checks

After isolating (Y(s)), factor its denominator and write a sum of simpler terms. For distinct linear factors, coefficients can be found by clearing the denominator and substituting each root, or by equating polynomial coefficients. A factor (1/s) represents a constant steady response; factors such as (1/(s+a)) represent decaying exponentials. Keep the initial-value terms in the numerator until the algebra is complete.

Before accepting an inverse transform, check:

- The result has the correct initial value and, for a second-order problem, the correct initial slope.
- Substitution into the differential equation recovers the stated forcing on each time interval.
- A delayed response stays zero before the stated switch and has the required continuity at the switch.
- The long-time behavior agrees with the poles and any constant-forcing steady state.

## Limits of this lesson

The examples use ordinary step forcing and constant-coefficient equations. They do not introduce Dirac impulses, convolution integrals, Fourier series, or transfer-function analysis. Those topics appear in the broader 18.03SC unit; the companion week-6 reading on impulse response, convolution and transfer functions introduces the delta function, convolution and transfer functions, while Fourier series remain limited to the week-3 harmonic example. All variables here are mathematical teaching examples, not fitted models of a real device or organism.
