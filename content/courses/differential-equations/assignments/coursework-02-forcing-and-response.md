# Assignment 2: forcing, resonance and periodic error budgets

This open report connects constant-coefficient response, Laplace transforms, convolution and Fourier filtering. You will solve two distinct initial-value problems and construct a periodic approximation certificate. All inputs are invented normalized mathematical signals. These are paper and software exercises, not instructions for applying a physical impulse to a device or organism. Keep derivations, implementations and report locally; browser practice checks selected outputs only.

## Part A: resonance with initial conditions

Consider

$$x''+4x=\sin(2t),\qquad x(0)=x'(0)=0.$$

The forcing frequency equals the undamped natural frequency. An ordinary sinusoidal trial with the same frequency duplicates the homogeneous solution and cannot solve the forced equation. Derive a resonant particular solution, then add homogeneous terms to satisfy both initial data. Your full solution should be

$$x(t)=\frac18\sin(2t)-\frac t4\cos(2t).$$

Differentiate it carefully: the derivative terms in $\cos(2t)/4$ cancel, leaving $x'(t)=\tfrac t2\sin(2t)$. At $t=\pi/4$, $x=1/8$ and $x'=\pi/8$. At $t=\pi/2$, $x=\pi/8$. These point checks supplement the residual identity $x''+4x=\sin(2t)$; they do not replace it. Explain why the growing envelope prevents interpreting this as an attracting steady periodic response.

Solve the same IVP by a second route. With zero initial data the Laplace equation is $X(s)=2/(s^2+4)^2$. Alternatively convolve the unit impulse response $\tfrac12\sin(2t)$ with the forcing. Show how either route recovers the initial-value solution, including the homogeneous correction needed by a particular resonant trial. A transfer-function value at the resonant imaginary-axis pole is not a finite steady gain.

## Part B: a delayed impulse in a different system

Now solve

$$z''+2z'+2z=3\delta(t-1),$$

with the system at rest before $t=1$. Integrate across a shrinking interval around one. The state remains continuous and the derivative jumps by three. Afterward the homogeneous dynamics start with $z(1^+)=0$, $z'(1^+)=3$, yielding

$$z(t)=3H(t-1)e^{-(t-1)}\sin(t-1).$$

At $t=1+\pi/2$, $z=3e^{-\pi/2}\approx0.623639$. This impulse has prescribed area, not a finite value at one instant. If you approximate it by a rectangular pulse, retain its area as its width changes and solve both the finite-pulse and ideal-impulse problems as distinct approximations. Do not insert a huge unscaled sample at one grid point and assume the impulse size is correct.

Check the pre-event zero state, continuity, the derivative jump and the post-event residual separately. If the integrator crosses the event without an explicit jump update or resolved pulse, explain how its step sequence handles the discontinuity. Refinement should control both the event treatment and ordinary integration error. Plot position and derivative on separate axes with the event marked.

## Part C: a harmonic certificate for a stable first-order filter

Use the square input defined in the Fourier foundation and the separate filter $y'+y=u$. Derive its odd sine coefficients, then the sine/cosine output coefficients. For the fundamental, the output amplitude is $4/(\pi\sqrt2)$ and lag is $\pi/4$ radians. Use the exact half-cycle periodic value $y_{\rm per}(0)=-(1-e^{-\pi})/(1+e^{-\pi})$ as an independent starting state, rather than constructing both references from the same truncated sum.

Retain all odd harmonics with index at most $N=64$. The conservative uniform omitted-output bound $4/(\pi N)$ is $1/(16\pi)\approx0.0198944$. This is below 0.02. Derive the inequality, including why summing all omitted integers instead of only the odd ones gives a valid conservative bound. A sampled maximum below the certificate is a numerical consistency check, not a proof that the sampled maximum is the true supremum.

If the IVP instead starts at zero, add its homogeneous correction. At $t=1$ the magnitude of the omitted transient would be $|y_{\rm per}(0)|e^{-1}$. Compare this with the harmonic tail certificate. State a total bound that includes both when a periodic-only approximation is used for that IVP. Increasing the number of harmonics cannot remove a missing initial condition.

## What to retain

Submit locally a method-comparison derivation, event/jump ledger, harmonic coefficients, analytic truncation proof and numerical error study. Include one deliberately incorrect phase or impulse-area implementation and show the test that rejects it. Explain the roles of transients, poles, resonance and piecewise smoothness in your results. Selected browser checkpoints do not evaluate this retained evidence or certify mastery.

The link-only scope comparators are [MIT OCW 18.03SC Fall 2011 Unit II](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-ii-second-order-constant-coefficient-linear-equations/) and [Unit III](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/). All explanations, problems and parameters are original with substantial AI assistance. General distribution theory, nonlinear forced oscillations and experimental signal identification remain deferred. The course remains partial, unreviewed and ungraded; no measured workload or university equivalence is implied.
