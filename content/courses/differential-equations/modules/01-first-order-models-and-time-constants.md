# First-order models and time constants

A first-order model describes how one state changes from its current value. In the common relaxation model

$$\frac{dx}{dt}=-k(x-x^*),$$

$x^*$ is an equilibrium and $k$ is a rate constant. The rate is proportional to the distance from equilibrium: a larger gap gives a larger initial rate of change. When $k>0$, the state approaches the equilibrium without crossing it in this ideal model.

## Solve by shifting to the equilibrium

Define the deviation $y=x-x^*$. If the equilibrium and $k$ are constant, then $dy/dt=-ky$. Separating variables gives $dy/y=-k\,dt$, so $\ln|y|=-kt+C$ and

$$x(t)=x^*+(x_0-x^*)e^{-kt}.$$

The initial condition $x(0)=x_0$ selects one trajectory from the family of solutions. Without it, the differential equation gives a rule for the slope but not a unique prediction. If the initial state equals the equilibrium, the deviation is zero and the state remains there. For $k>0$, deviations above and below equilibrium both shrink toward zero; $k=0$ gives no relaxation, and $k<0$ makes small deviations grow rather than decay.

The same constant-equilibrium equation can be written as a first-order linear equation $x'+kx=kx^*$. More generally, for $x'+p(t)x=q(t)$, an integrating factor $m(t)=e^{\int p(t)\,dt}$ gives $(mx)'=mq$. Integrating and applying an initial condition solves the linear equation. For a separable equation $x'=f(x)g(t)$, separate state and time terms where division is valid, and check constant solutions separately because division can remove equilibria.

## Interpret the time constant

Writing the exponential as $e^{-t/\tau}$ defines the characteristic time or time constant

$$\tau=\frac{1}{k}.$$

Because $kt$ must be dimensionless, $k$ has units of inverse time and $\tau$ has units of time. At $t=\tau$, the remaining distance to equilibrium is $e^{-1}\approx0.368$ of its initial value, so about 63.2% of a step change is complete. At $2\tau$ about 86.5% is complete; at $3\tau$ about 95.0%; and at $5\tau$ about 99.3%. The state reaches equilibrium only asymptotically in the continuous model, so one time constant is not “the time to equilibrium.”

**Worked example.** For $\dot{x}=-0.25x$ with $x(0)=8$, the equilibrium is zero and $k=0.25$ time-unit$^{-1}$, hence $\tau=4$ time units. At $t=4$, $x=8e^{-1}\approx2.94$, leaving 36.8% of its initial distance to equilibrium. If instead $\dot{x}=-0.5(x-4)$ with time in seconds, the equilibrium is 4 and $\tau=2$ s; starting at 10 gives $x(2)=4+6e^{-1}\approx6.21$. The second state has completed about 63.2% of its change from 10 toward 4.

For a constant external input, $\dot{x}=-kx+u$ has equilibrium $x^*=u/k$ when $k>0$; shifting by that equilibrium gives the same exponential approach. This pattern appears in idealized sensor response, charging, washout, relaxation, and some population models. In each case, the state, equilibrium, and rate constant must be defined for the process being modeled.

## Check the model before interpreting its fit

The single time constant assumes a constant rate coefficient and a fixed equilibrium. It predicts a monotone exponential approach with no delay or overshoot. If the data show multiple phases, adaptation, changing input, or a non-exponential tail, one first-order model may be too simple. A fitted $k$ summarizes the chosen interval and conditions; it is not automatically a permanent property of the sensor, cell, or system.

Keep time units consistent: if $k$ is in s$^{-1}$, substitute time in seconds. A negative sign in the model makes deviations decay when $k>0$; changing it to a positive sign reverses the stability. When estimating parameters from measurements, report the equilibrium, initial condition, time unit, fitted interval, and uncertainty so a reader can see what the rate describes.

## Common mistakes

- Treating $1/k$ as a time to reach exact equilibrium rather than a characteristic time.
- Forgetting that the initial condition selects the particular solution.
- Omitting the equilibrium offset and applying $x=x_0e^{-kt}$ to a nonzero-equilibrium process.
- Mixing hours and seconds in $kt$, or giving $k$ units of time instead of inverse time.
- Assuming a single exponential remains valid when the equilibrium or rate changes during the observation.
