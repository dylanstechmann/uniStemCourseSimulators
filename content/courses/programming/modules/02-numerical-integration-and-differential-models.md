# Numerical integration and differential models

Numerical integration estimates an accumulated quantity from a rate or density, while an ordinary differential equation (ODE) describes how a state changes over time. Both replace a continuous model with finite calculations, so the step size and numerical method affect the result. A plausible or visually smooth output still needs checks against known values, limiting cases and model assumptions.

## Integrating sampled rates

For sampled values of a function, the trapezoidal rule joins neighboring samples with straight segments and sums their areas. Simpson's rule fits quadratic pieces across paired intervals and can be more accurate for smooth curves, but its assumptions and sample spacing matter. Neither method repairs sparse, noisy or biased measurements; refinement estimates numerical sensitivity only when the underlying data and model justify it.

For $f(t)=t^2$ on $[0,2]$, the one-panel trapezoid rule gives $2(0+4)/2=4$. Simpson's rule using $t=0,1,2$ gives $\frac{2}{6}[f(0)+4f(1)+f(2)]=\frac{8}{3}$. The exact integral is also $8/3$, because Simpson's rule integrates a quadratic exactly. The difference makes the coarse trapezoid error visible. For a general function, compare refinements or a suitable error estimate and retain units: integrating a rate in mg/min over minutes produces mg.

## Forward Euler for a changing state

For $y'=g(t,y)$ with initial value $y_0$, forward Euler uses

$$
y_{n+1}=y_n+h\,g(t_n,y_n),
$$

where $h$ is the time step. This is a first-order approximation: each slope is sampled at the beginning of an interval. Reducing the step often reduces discretization error for a smooth, well-posed problem, but also requires more steps and does not remove measurement noise or model error.

For the decay equation $y'=-\lambda y$ with $\lambda>0$, the exact solution is $y(t)=y_0e^{-\lambda t}$. Euler instead multiplies the state at each step by $1-\lambda h$. Its magnitude must be below one for the discrete solution to decay without growing; this gives $0<\lambda h<2$. If $\lambda h>1$, the numerical values alternate in sign even while their magnitude may shrink.

For $\lambda=4$ and $h=0.6$, the multiplier is $1-4(0.6)=-1.4$. Starting at $y_0=1$ gives $y_1=-1.4$ and $y_2=1.96$: the computed magnitude grows although the true decay is positive and decreases. This is a numerical instability, not evidence that the modeled process physically reverses. At $h=0.4$, the multiplier is $-0.6$ and the discrete magnitude shrinks, though it alternates. The stability condition depends on the model's time scale; a step that works for a slow mode can fail for a faster one.

## Check the calculation and the model separately

Compare a solution at successively smaller steps, check units and initial conditions, and use an analytic solution or conservation relation when available. Solver tolerances control numerical work inside an algorithm; they do not certify that the equations describe the process or that observations are accurate. Stiff systems may require an appropriate implicit solver rather than arbitrarily tiny explicit steps. The examples here are constructed, and later lessons develop quadrature error and stability checks in more depth.
