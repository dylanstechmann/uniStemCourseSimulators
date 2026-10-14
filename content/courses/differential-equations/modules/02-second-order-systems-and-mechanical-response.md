# Second-order systems and mechanical response

A mass–spring–damper model is a second-order differential equation because acceleration is the second derivative of position. It describes an idealized mechanical degree of freedom with inertia, elastic restoring force, viscous damping, and an applied load. A free-body diagram determines the signs; the coefficients then determine the natural time scale and the qualitative form of the transient.

## Derive the force balance

Let $x$ be displacement from a chosen equilibrium, positive in one specified direction. For mass $m$, spring stiffness $k$, damping coefficient $c$, and applied force $F(t)$, Newton's second law gives

$$m\ddot{x}=F(t)-c\dot{x}-kx,$$

or equivalently

$$m\ddot{x}+c\dot{x}+kx=F(t).$$

The spring force $-kx$ opposes displacement from equilibrium, and the viscous damper force $-c\dot{x}$ opposes velocity. Moving those terms to the left gives them positive coefficients. This sign convention assumes positive $x$ in the direction of the applied force; choosing the opposite direction changes the signs consistently, not the physical prediction.

The units also check the model: $m$ is kg, $c$ is N·s/m, $k$ is N/m, and each term on the equation's left has units of newtons. If the coordinate is measured from a reference that is not the static equilibrium, a constant load can shift the equilibrium position. Analyze motion about that equilibrium to isolate the transient response.

## Natural frequency and damping ratio

For the unforced system, set $F(t)=0$ and divide by $m$:

$$\ddot{x}+\frac{c}{m}\dot{x}+\frac{k}{m}x=0.$$

The undamped natural angular frequency and damping ratio are

$$\omega_n=\sqrt{\frac{k}{m}}, \qquad \zeta=\frac{c}{2\sqrt{km}}=\frac{c}{2m\omega_n}.$$

$\omega_n$ is measured in rad/s when the time unit is seconds; $\zeta$ is dimensionless. With these definitions the equation becomes $\ddot{x}+2\zeta\omega_n\dot{x}+\omega_n^2x=0$. The frequency describes the inertia–stiffness time scale, while $\zeta$ compares damping to the critical value for that mass and spring.

**Worked example.** For $m=2$ kg, $k=50$ N/m, and $c=3$ N·s/m, $\omega_n=\sqrt{50/2}=5$ rad/s and $\zeta=3/(2\sqrt{100})=0.15$. The response is underdamped. For the separate system in the practice force-balance question, $m=2$ kg and $k=8$ N/m give $\omega_n=2$ rad/s; with $c=3$ N·s/m, $\zeta=3/(2\sqrt{16})=0.375$. The values are synthetic and illustrate classification, not a measured tissue or device.

## Classify the unforced transient

Seeking solutions of the form $x=e^{st}$ gives the characteristic equation $s^2+2\zeta\omega_ns+\omega_n^2=0$. Its roots determine the transient:

- **Underdamped, $0\le\zeta<1$:** the roots are $-\zeta\omega_n\pm i\omega_d$, with $\omega_d=\omega_n\sqrt{1-\zeta^2}$. The response oscillates while its envelope decays when damping is positive. At $\zeta=0$ it oscillates without decay in the ideal model.
- **Critically damped, $\zeta=1$:** there is a repeated real root $-\omega_n$. The response returns without oscillation; for the ideal linear model it is the boundary between oscillatory and nonoscillatory responses.
- **Overdamped, $\zeta>1$:** there are two distinct negative real roots. The response is a sum of decaying exponentials and does not oscillate; the slower mode often dominates later behavior.

For $\zeta=0.15$ and $\omega_n=5$ rad/s, the damped frequency is $5\sqrt{1-0.15^2}\approx4.94$ rad/s. It is lower than the undamped natural frequency because damping changes the oscillation rate. The response still needs initial displacement and initial velocity: a second-order equation requires both to select one trajectory. The same coefficients with different initial conditions can produce different amplitudes and phases.

## Forced response to an applied force

When $F(t)$ is nonzero, the solution combines a transient determined by the initial state with a particular response determined by the forcing. For sinusoidal forcing, the long-time response oscillates at the forcing frequency, with amplitude and phase set by the frequency ratio and damping. In the linear model, the displacement amplitude relative to the static deflection $F_0/k$ is

$$\frac{1}{\sqrt{(1-r^2)^2+(2\zeta r)^2}}, \qquad r=\frac{\omega}{\omega_n},$$

where $F_0\cos(\omega t)$ is the applied force. Near $r=1$, a lightly damped system can respond strongly; damping limits the peak. The free transient and forced steady response are different parts of the solution, so the initial oscillation should not be mistaken for the long-time behavior under periodic loading.

## Know where the model applies

The constant-coefficient model assumes a linear spring, a viscous damper, a fixed mass, and one coordinate with the stated boundary conditions. It can be a useful local approximation for small motions or a limited frequency range. Biological tissues and robotic mechanisms can have nonlinear stiffness, viscoelastic memory, changing contact, multiple coupled modes, or active control. In those cases a fitted $m$, $c$, or $k$ may summarize one test regime rather than remain valid under another loading condition.

Before interpreting a measured response, state the coordinate, reference equilibrium, force direction, initial position and velocity, units, loading frequency, and regime used to identify parameters. A free-body diagram checks force signs; units check dimensions; and comparing observed decay or oscillation with the predicted response checks whether the model is plausible over the interval of interest.

## Common mistakes

- Giving the spring or damping term a negative coefficient after already moving its opposing force to the left side.
- Confusing natural angular frequency with damping ratio, or assigning units to the dimensionless ratio $\zeta$.
- Classifying the response from $\omega_n$ alone without computing or interpreting $\zeta$.
- Forgetting that a second-order model needs both initial displacement and initial velocity.
- Applying a linear viscous model outside the deformation or frequency range it represents.
