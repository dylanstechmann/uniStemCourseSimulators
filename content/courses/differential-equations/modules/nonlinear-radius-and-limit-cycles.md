# Nonlinear radius, invariant sets and a limit cycle

Linearization is a local tool. The existing toggle-switch lesson classifies isolated equilibria using Jacobian eigenvalues; it does not derive a periodic orbit or settle a zero-real-part case. An exactly reducible planar system gives a useful next step. It lets us prove which amplitudes grow or decay, distinguish an attracting cycle from an attracting equilibrium, and verify a numerical phase portrait against an analytic radius. The system is invented and dimensionless, not a calibrated biological oscillator.

## Separate amplitude from rotation

Consider

$$x'=(\mu-r^2)x-\omega y,\qquad y'=\omega x+(\mu-r^2)y,\qquad r^2=x^2+y^2,$$

where $\omega>0$. Multiplying by $x$ and $y$ and adding cancels the rotation terms:

$$\frac{d(r^2)}{dt}=2\mu r^2-2r^4.$$

For $r>0$, this implies $r'=\mu r-r^3$. The angular formula $(xy'-yx')/r^2$ gives $\theta'=\omega$. At the origin the angle is undefined, but the Cartesian equation remains smooth. An implementation should not divide by zero there.

Set $w=r^2$. Then $w'=2w(\mu-w)$, a scalar logistic equation. Nonnegative initial $w$ remains nonnegative; the origin and any positive equilibrium cannot be crossed by distinct solutions of this smooth scalar IVP. This invariance claim belongs to the differential equation. A large forward-Euler step can still create a negative squared radius, exposing a numerical failure.

## Positive parameter: an attracting periodic orbit

If $\mu>0$, the radius equilibria are zero and $r_* =\sqrt{\mu}$. Below $r_*$, a positive radius grows; above it, the radius shrinks. Thus every positive initial radius approaches the same circle, while the origin remains an equilibrium and is unstable. On that circle the angular speed is $\omega$, so the period is $T=2\pi/\omega$.

This circle is an isolated periodic orbit and a limit cycle. Nearby trajectories approach the orbit as a set. They do not necessarily converge to one specified point moving around it, because an initial angular shift persists. That distinction is orbital attraction versus pointwise convergence to one chosen periodic trajectory. The radial linearization has derivative $\mu-3r_*^2=-2\mu$, giving a radial decay exponent; the tangential phase direction is neutral. General two-dimensional systems need not permit this radial reduction.

The exact positive-radius solution follows by separating the $w$ equation:

$$w(t)=\frac{\mu}{1+(\mu/w_0-1)e^{-2\mu t}},\qquad r(t)=\sqrt{w(t)}.$$

Keep the positive square root for a radius. The Cartesian solution is $r(t)(\cos(\theta_0+\omega t),\sin(\theta_0+\omega t))$. If the initial state is exactly zero, use the separate zero solution rather than substituting $w_0=0$ into a formula that divides by it.

## Worked orbit and a distinct rehearsal

Use $\mu=1$, $\omega=3$ and $(x_0,y_0)=(1/2,0)$. The attracting radius is one, its period is $2\pi/3\approx2.09440$, and the radial decay exponent is $-2$. The exact squared radius is $1/(1+3e^{-2t})$. At $t=(\ln3)/2$, $w=1/2$ and $r=1/\sqrt2\approx0.707107$. The trajectory has reached that radius, not the final cycle exactly; the angular position has simultaneously advanced by $3t$.

The rehearsal changes to $\mu=4$, $\omega=2$ and $r_0=1$. Now $r_*=2$, $T=\pi$ and the radial exponent is $-8$. The squared radius is $4/(1+3e^{-8t})$. At $t=(\ln3)/8$, it equals two, so the radius is $\sqrt2$. Do not copy the worked case's radius, period or time constant after changing the parameters.

## The nonhyperbolic boundary

At $\mu=0$, the linearized eigenvalues at the origin are $\pm i\omega$. Linearization alone cannot establish attraction or repulsion. The nonlinear radius equation gives $r'=-r^3$, and for $r_0>0$,

$$r(t)=\frac{r_0}{\sqrt{1+2r_0^2t}}.$$

For forward time the radius decreases to zero algebraically. The origin is asymptotically stable even though the linear system consists of closed circles. With $r_0=1$, $r(1)=1/\sqrt3$. This is a concrete reason to mark a zero-real-part linearization as inconclusive rather than stable or unstable by analogy.

The scalar function $V=(x^2+y^2)/2$ provides another check: $V'=\mu r^2-r^4$. At $\mu=0$, $V'<0$ for every nonzero state, while $V$ is positive and radially unbounded. This supports global forward attraction to zero for this particular smooth system. For $\mu<0$, the same expression is also strictly negative away from zero. For $\mu>0$, it changes sign at the cycle, so it cannot be used to claim global attraction to the origin.

## Verification study

Implement the Cartesian and scalar-radius equations independently. Compare their radii at common times, check the exact solution, and halve the integration step. Test a start inside and outside the attracting circle and the exact origin. At $\mu=0$, compare against the algebraic solution rather than fitting an exponential tail. To measure a period numerically, detect crossings with a specified direction and refine the crossing time; counting samples near the axis can miss or double count events.

Report radius error separately from phase error. A nearly circular plot can hide a steadily accumulating phase discrepancy. State whether a result concerns a particular trajectory, an invariant set, local linear behavior or a global argument. These distinctions matter more than visual similarity. The [MIT OCW 18.03SC Fall 2011 Unit IV limit-cycle session](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iv-first-order-systems/limitations-of-the-linear-limit-cycles-and-chaos/) is a link-only scope comparator; no source problem or instructional asset is copied. This original AI-assisted treatment does not develop chaos, general bifurcation theory or a general limit-cycle existence theorem. It remains partial and unreviewed.
