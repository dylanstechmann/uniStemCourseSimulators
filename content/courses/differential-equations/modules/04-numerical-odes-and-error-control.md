# Numerical ODEs and error control

An initial-value problem specifies a differential equation and the state at a starting time. A numerical method replaces the continuous trajectory with a sequence of approximations. The step size controls how far the method advances before using the model again; a step can be stable yet too inaccurate, or accurate for a short interval yet unstable over repeated updates.

## Forward Euler uses the slope at the start

For $\dot{x}=f(t,x)$ with current approximation $x_n$ at time $t_n$, forward Euler takes the tangent slope at the beginning of the step:

$$x_{n+1}=x_n+h f(t_n,x_n), \qquad t_{n+1}=t_n+h.$$

The step $h$ has units of time, so $h f$ has the units of the state. The update is an explicit calculation: the next state is obtained from known current values without solving an equation for $x_{n+1}$. It is also a first-order method: for a sufficiently smooth solution over a fixed time interval, its global error generally scales like $O(h)$ as the step shrinks, while the local one-step truncation error scales like $O(h^2)$.

**Worked step.** If $\dot{x}=2$ and $x_0=3$, one Euler step of $h=0.25$ gives $x_1=3+0.25(2)=3.5$. Because the slope is constant, this step is exact for this particular equation. For a changing slope, Euler extrapolates the starting slope across the whole interval, so the approximation has error.

## Stability is not the same as accuracy

Consider the decay equation $\dot{y}=-\lambda y$ with $\lambda>0$. Its exact solution multiplies the state over one step by $e^{-\lambda h}$. Euler instead multiplies by

$$g=1-\lambda h.$$

Repeated numerical steps decay in magnitude only when $|g|<1$, which gives the strict interval $0<h<2/\lambda$. The upper boundary $2/\lambda$ is a supremum, not an included decaying step: at $h=2/\lambda$, $g=-1$ and the numerical value alternates sign without shrinking. Above the boundary, $|g|>1$ and errors or states grow. For a nonnegative physical quantity that must also remain nonnegative at each step, require $g\ge0$, giving the more restrictive condition $0<h\le1/\lambda$.

**Boundary example.** With $\lambda=50$ s$^{-1}$, the strict stability interval ends at $2/50=0.04$ s. At $h=0.04$ s, Euler's factor is $1-50(0.04)=-1$: the magnitude is unchanged and the sign flips. At $h=0.02$ s the factor is zero, so this scalar Euler update reaches zero in one step and remains nonnegative. These conditions describe the numerical method for this equation; they do not establish accuracy for another model or step size.

Stability asks whether numerical perturbations remain bounded or decay under repeated updates. Accuracy asks how close the approximation is to the desired solution. A stable step can still accumulate substantial error, and a visually smooth numerical curve can still violate the equation or a physical constraint. Stability limits should therefore be checked alongside error and domain checks.

## Step refinement: test the result

For a fixed interval, compare solutions computed with $h$, $h/2$, and if needed $h/4$. In a first-order convergent regime, halving $h$ should reduce the global error by roughly a factor of two once the step is small enough. Compare with an exact solution when available or with a more accurate reference calculation. Agreement under refinement is evidence about numerical error, not proof that the differential-equation model describes the real process.

Check units at every update, preserve any known positivity or conservation constraints, and record the time span, solver, step size, tolerances, and refinement evidence. If a state becomes negative when the model requires nonnegative values, determine whether the cause is a step-size violation, a method limitation, an incorrect equation, or incompatible initial data. Do not silently clip values without analyzing how that operation changes the model.

## Stiff systems and solver choice

A system is stiff when its dynamics contain substantially different time scales and an explicit method is constrained by a fast decaying mode even though the behavior of interest changes slowly. For a stable linear system, explicit Euler must satisfy a stability condition for every relevant eigenvalue; the fastest mode can force a very small step. Implicit methods can have a wider stability region for such problems, but they still need accuracy checks, suitable tolerances, and checks of the quantities that matter.

Higher-order Runge–Kutta methods can reduce error per step for smooth nonstiff problems, but higher order does not remove all stability limits and does not replace convergence checks. Select a method based on the equation, its time scales, required accuracy, and constraints rather than convenience alone. Solver tolerance is not the same as measured model uncertainty.

## Common mistakes

- Applying the starting slope as if it were the exact average slope over a long step.
- Calling the Euler stability boundary a step that strictly decays; the boundary factor has magnitude one.
- Confusing the stability interval with the stricter positivity interval.
- Treating stability as evidence of accuracy or model validity.
- Increasing the number of sampled output points without reducing the integration step.
- Using an implicit solver for a stiff equation and skipping accuracy, positivity, or convergence checks.
