# Assignment 4: nonlinear behavior and numerical claims

This final open report connects local linearization, nonlinear invariant sets and numerical verification. It uses the invented planar radius model from the foundation with different parameters. Its purpose is to test how much a Jacobian, a plot or an observed error can actually establish. Keep your arguments, code, plots and results locally. Practice checkpoints assess selected values and choices; the software does not evaluate a mathematical proof or a completed computational study.

## Part A: a distinct attracting cycle

Set

$$x'=(\mu-r^2)x-\omega y,\qquad y'=\omega x+(\mu-r^2)y,\qquad r^2=x^2+y^2,$$

with $\mu=1/4$, $\omega=2$ and $(x_0,y_0)=(1/4,0)$. Derive $r'=\mu r-r^3$ and $\theta'=\omega$ directly from the Cartesian equations. Mark the domain restriction in the formula for the angle and show that the Cartesian field itself is smooth at the origin.

Find the attracting cycle radius $r_*=1/2$, period $T=\pi$ and radial decay exponent $-2\mu=-1/2$. Explain why the tangent phase direction does not contract in the same way as radial disturbances. An attracting cycle is not an asymptotically stable fixed point. The exact origin remains an equilibrium and does not move onto the cycle despite its instability.

For the stated positive start, use $w=r^2$ to derive

$$w(t)=\frac{1/4}{1+3e^{-t/2}}.$$

At $t=2\ln3$, $w=1/8$ and $r=1/(2\sqrt2)\approx0.353553$. Compute the angular advance at that time and reconstruct the Cartesian state. Do not assume the crossing of a selected radius is one full period or the time at which the final cycle has been reached exactly.

## Part B: where linearization is inconclusive

For a separate run set $\mu=0$, keep $\omega=2$, and start at radius $r_0=1/2$. The origin's linearization has purely imaginary eigenvalues. Classifying it as an attracting or repelling equilibrium from that linearization would be unjustified. Derive instead

$$r(t)=\frac{1/2}{\sqrt{1+t/2}}.$$

At $t=2$, the radius is again $1/(2\sqrt2)$, but the long-time behavior differs completely from Part A: it tends to zero rather than a nonzero cycle. The same observed radius at selected times does not identify the asymptotic behavior or parameter regime.

Use $V=(x^2+y^2)/2$ and show that $V'=-r^4$ in this zero-parameter case. State how positivity, radial boundedness and the exact radius equation support forward attraction. A derivative evaluated along a numerical path is a check; the symbolic identity and its domain establish the argument. Contrast the algebraic decay with the exponential decay of a hyperbolic stable linear mode.

## Part C: separate phase, radius and integration errors

Implement the Cartesian equation with a documented method and the scalar radius equation independently. Compare both with the exact radius at common target times. Use at least three successively halved steps and report absolute error, observed order and any event-location rule. A period estimate based on upward axis crossings needs a consistent direction and interpolation or event refinement; counting the nearest sample can introduce an error of the same size as a step.

Report phase error separately from radius error. Unwrap an angle only away from zero and explain the convention. A numerical trajectory can have an accurate radius yet rotate at the wrong rate because of accumulated phase error. Conversely, an apparently correct phase portrait can conceal the wrong equilibrium or a slow amplitude drift. Plot error against step size rather than merely overlaying visually similar curves.

## Part D: stability versus accuracy and invariance

Use the separate scalar equation $q'=-4q$, $q(0)=1$. Forward Euler with $h=0.4$ has amplification $1-4h=-0.6$. Its magnitude is below one, but its sign is negative, so the numerical solution alternates sign while the exact solution $e^{-4t}$ stays positive. At $h=0.2$, amplification is positive 0.2; positivity still does not guarantee a small trajectory error. Derive the nonnegative and stable step intervals and compare them with the closed-transfer counterexample in Assignment 3.

Propose an acceptance table that keeps equation residuals, invariant/domain checks, reference error, refinement and event accuracy distinct. A solver's successful termination should not substitute for these criteria. Identify one intentionally incorrect implementation and retain the test that catches it. Use a counterexample to reject an overbroad claim rather than drawing universal conclusions from a single successful simulation.

## Scope and evidence

Your locally retained report should contain radial/angle derivations, the nonlinear zero-parameter argument, cycle-versus-equilibrium interpretation and reproducible numerical error tables. The [MIT OCW 18.03SC Fall 2011 syllabus](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/syllabus/syllabus/) and [Unit IV limit-cycle session](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iv-first-order-systems/limitations-of-the-linear-limit-cycles-and-chaos/) are link-only scope comparators. All problems and explanations are original and AI-assisted. This is not a general theory of bifurcations, chaos or physiological oscillation, and it does not establish experimental validity, measured workload, qualified review or university equivalence. The package remains partial, unreviewed and formative-only.
