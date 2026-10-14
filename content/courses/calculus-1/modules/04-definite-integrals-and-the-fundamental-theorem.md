# Definite integrals and the fundamental theorem

A definite integral accumulates a changing rate over an interval. It can be introduced as a limit of signed sums, calculated with an antiderivative when one is available, or approximated numerically from observations. These are connected views of the same quantity. A rate's units multiply by the independent variable's units, and the sign records whether the modeled state increases or decreases.

## From rate samples to accumulation

Divide the interval $[0,6]$ minutes into smaller pieces. On each piece, rate × duration estimates the state change. Adding these rectangles gives a Riemann sum; refining the partition gives the definite integral when the rate is integrable. If a rate $r(t)$ is measured in mg/min, then $r(t)\,dt$ has units mg and its integral is a net mass change.

Consider a synthetic transfer rate $r(t)=4-t$ mg/min for $0\le t\le6$ minutes. It begins at 4 mg/min, reaches zero at $t=4$ min, then reverses direction and ends at −2 mg/min. The signed accumulation is

$$
\int_0^6(4-t)\,dt=\left[4t-\frac{t^2}{2}\right]_0^6=24-18=6\text{ mg}.
$$

The positive triangular region from 0 to 4 contributes 8 mg; the negative triangular region from 4 to 6 contributes −2 mg. Their signed sum is 6 mg. If the initial state is 12 mg, the final state is $12+6=18$ mg. The integral gives the change, not the final state by itself. The total amount transferred in either direction is instead $\int_0^6|4-t|\,dt=8+2=10$ mg. Net change and total change answer different questions.

## Two parts of the Fundamental Theorem

For a continuous rate $r$, define its accumulated change from the start by

$$
F(t)=\int_0^t r(s)\,ds.
$$

The first part of the Fundamental Theorem says $F'(t)=r(t)$: the instantaneous slope of accumulated change is the rate at the current endpoint. The variable $s$ is a dummy integration variable; $t$ determines the moving upper bound. In this example $F(t)=4t-t^2/2$, so $F'(t)=4-t$. At $t=5$, accumulation is $F(5)=7.5$ mg and the instantaneous rate is −1 mg/min. A positive accumulated total can coexist with a negative current rate because the total reflects the entire prior interval.

The second part says that an antiderivative $A$ can evaluate the integral: $\int_a^b r(t)\,dt=A(b)-A(a)$. For the same rate, $A(t)=4t-t^2/2$, and the evaluation gives 6 mg. Any constant added to $A$ cancels when the endpoint values are subtracted. A definite integral is a number with units, not an indefinite family of antiderivatives, so no extra $+C$ belongs in its value.

The sign also depends on order: $\int_b^a r(t)\,dt=-\int_a^b r(t)\,dt$. Reversing the bounds reverses the direction of the reported net change. This is an algebraic property of signed accumulation, not a claim that physical time has run backward.

## Approximation and interpretation

For the linear rate $4-t$, a midpoint rectangle over the full six-minute interval uses the midpoint rate $r(3)=1$ mg/min and estimates 6 mg, exactly matching the integral. That agreement occurs because the midpoint rule integrates a linear function exactly over one interval. A single midpoint will not generally be exact for a curved rate. With sampled observations, subdividing the interval or using a justified quadrature rule can improve an approximation, but uncertainty, irregular timing and model assumptions still matter.

Before interpreting an integral, check what the integrand represents, its units, the bounds, and whether the question asks for net or total accumulation. For a rate that never changes sign, the absolute accumulated amount equals the magnitude of the net change. When the rate changes sign, split the interval at its zeros to calculate total change. If an initial condition is supplied, add net change to that initial state only after evaluating the integral.

These examples use a constructed rate curve for learning. Continuity supports the stated derivative form of the Fundamental Theorem; integrability is sufficient for the signed accumulation itself. A formula or numerical integral establishes no measured transfer or real process behavior.
