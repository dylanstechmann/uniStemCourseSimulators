# Dynamic feedback and the limits of a DC gain calculation

The finite-feedback reading derives $A_0/(1+\beta A_0)$ for a static amplifier. A dynamic amplifier must also have a stable closed-loop trajectory. Negative feedback in a block diagram is not by itself that stability proof. This original three-state example makes the distinction exact using invented pole/gain coefficients rather than a real op-amp specification.

## Add a declared dynamic model

Stipulate open-loop response $A(s)=A_0/(1+s/\omega)^3$ with $A_0,\omega>0$ and a constant nonnegative feedback fraction $\beta$. With input error $v_{in}-\beta v_o$, the closed-loop transfer is $T=A/(1+\beta A)$. Define loop coefficient $G=\beta A_0$. Its characteristic equation is

$$\left(1+\frac{s}{\omega}\right)^3+G=0.$$

The three equal open-loop poles are stable at $-\omega$. The closed-loop roots depend on feedback. For $q=\sqrt[3]{G}$, the real root is $-\omega(1+q)$ and the conjugate pair has real part $\omega(-1+q/2)$ and imaginary magnitudes $\omega\sqrt3 q/2$. Derive them from the cube roots of -G or verify their polynomial product.

For $0\leq G<8$, all roots have negative real parts. At eight the pair lies on the imaginary axis, and above eight it has positive real parts. This threshold belongs to the stipulated identical-pole model; it is not a universal op-amp gain limit. A different pole distribution or feedback network needs a new characteristic equation.

## Formal equilibrium and attracting response differ

The formal DC transfer remains $A_0/(1+G)$ for nonnegative G. That algebraic value does not establish that a trajectory approaches it. When a closed-loop pole grows, the equilibrium can exist while perturbations depart from it. Real output limits, slew and additional nonlinear states would eventually matter; the linear model does not describe that eventual behavior.

A compatible state realization is

$$x_1'=\omega[A_0(v_{in}-\beta v_o)-x_1],\quad x_2'=\omega(x_1-x_2),\quad v_o'=\omega(x_2-v_o).$$

It supplies independent initial-derivative and numerical checks. Do not add a post-step hard clamp and then claim the same linear differential equations were solved. If an assumed linear range is violated, report an event boundary or explicitly define a different nonlinear model.

## Worked stable comparison

Choose $A_0=100,\beta=0.04,\omega=1000$ rad/s. Then G=4 and the DC gain is 20, while the infinite-static-gain approximation would be 25. The poles are approximately -2587.40105 and $-206.299474\pm1374.72964i$ per second. All decay, but their different rates and oscillatory pair mean a single static error estimate does not describe the transient.

The formal gain error and the decay modes answer separate questions. A configuration can have a modest static error yet a poor transient; another can be stable but have substantial finite-gain error. Numerical plots should be compared with the actual characteristic roots and original state equations.

## Distinct rehearsal and unstable variant

The rehearsal uses $A_0=200,\beta=0.005,\omega=1000$. Here G=1 and DC gain is 100. Its real pole is -2000 per second, and the pair is $-500\pm500\sqrt3 i$ per second. The imaginary magnitude is about 866.025404. These roots describe the homogeneous deviations around the equilibrium, not a direct specification of every response peak.

For a separate variant keep the same open-loop coefficients but set $\beta=0.135$, giving G=27. The real root is -4000 and the pair has real part +500 and imaginary magnitudes $1500\sqrt3\approx2598.07621$ per second. This model is unstable despite its negative feedback sign and stable open-loop poles. Its finite formal DC gain $200/28$ is not an attracting steady response.

At the boundary G=8 the imaginary pair neither decays nor grows in the ideal linear model. Do not label that boundary asymptotically stable, and do not infer a real sustained oscillator amplitude from it. Amplitude selection and actual oscillation require nonlinear device and circuit information absent here.

## Verification and model-specific compensation reasoning

Construct the three-state matrix and compare its eigenvalues with the characteristic equation. Integrate a small perturbation for stable and unstable G, halve the step and compare growth or decay before a declared linear-range event. Use a zero-input perturbation to distinguish homogeneous modes from a forced equilibrium.

A compensation study can change a pole or feedback law and recompute the characteristic equation, but the equal-pole threshold cannot simply be carried across that change. Stability, bandwidth, settling, input/output range and noise are separate constraints. A manufacturer's device data and loading could alter all of them.

[MIT OCW 6.002 Spring 2007 calendar](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/calendar/) lecture 23 identifies feedback stability and oscillators. [Texas Instruments SLOA020A, March 2001](https://www.ti.com/lit/an/sloa020a/sloa020a.pdf) provides link-only loop/stability/compensation concept support. The model, derivation and parameters here are original, not a copied TI circuit or a particular product's poles. No source figure, table or assessment is imported. Full compensation design, physical validation and qualified review remain open; the course stays partial and unreviewed.
