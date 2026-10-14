# Robot dynamics, actuators, and energy

Kinematics describes where a mechanism can move; dynamics asks what torques and forces produce that motion. For one rigid rotor about a fixed axis with constant moment of inertia $I$, Newton's rotational law is

$$
\tau_{\mathrm{net}}=I\alpha.
$$

This simple equation is useful for building intuition, but a robot arm has configuration-dependent inertia, gravity, friction and coupled joints. Its full model requires more terms; a later lesson develops a two-joint mass matrix and energy ledger. Do not treat a single-rotor calculation as a complete actuator specification.

## Torque, work, and mechanical power

Torque is measured in newton-metres. If torque acts through an angular displacement $\theta$, the work is

$$
W=\int_{\theta_0}^{\theta_1}\tau(\theta)\,d\theta.
$$

For constant torque, this reduces to $W=\tau\Delta\theta$. Instantaneous mechanical power is $P=\tau\omega$, where $\omega=d\theta/dt$. Radians are dimensionless in SI, so $(\mathrm{N\,m})(\mathrm{rad/s})$ has units of watts. Torque and energy share the same base units but describe different quantities: one is a moment that changes rotation, the other is transferred energy.

Consider a constructed rotor with $I=0.02$ kg·m², initial speed $\omega_0=2$ rad/s, and constant net torque $\tau=0.10$ N·m applied for 0.40 s. Its angular acceleration is $\alpha=\tau/I=5$ rad/s², so final speed is 4 rad/s and angular displacement is 1.2 rad. The kinetic energy rises from

$$
K_0=\tfrac12 I\omega_0^2=0.04\ \mathrm{J}
\quad\text{to}\quad
K_1=\tfrac12 I\omega_1^2=0.16\ \mathrm{J}.
$$

The increase is 0.12 J, matching the applied work $\tau\Delta\theta=0.10\times1.2=0.12$ J. Power rises from 0.20 W to 0.40 W during this constant-torque acceleration. This balance assumes the stated net torque is the only work contribution; friction, gravity or another load would add terms.

## A gearbox trades speed for torque

Let a reduction gearbox have ratio $N=\omega_{\mathrm{motor}}/\omega_{\mathrm{out}}>1$ and efficiency $0<\eta\le1$. Under the stated convention,

$$
\omega_{\mathrm{out}}=\frac{\omega_{\mathrm{motor}}}{N},
\qquad
\tau_{\mathrm{out}}\approx\eta N\tau_{\mathrm{motor}}.
$$

The approximation treats efficiency as a single supplied value. If a motor supplies 0.10 N·m at 20 rad/s through a 20:1 reduction with $\eta=0.80$, the output is about 1.6 N·m at 1 rad/s. Input mechanical power is 2.0 W and output mechanical power is 1.6 W, consistent with the stated 80% efficiency. The gearbox increases torque while reducing speed; it does not create power.

## Ratings and model limits

An actuator's peak rating, continuous rating, speed range and thermal limits answer different questions. A short acceleration can require more torque than steady motion, while sustained torque can heat a motor even when it remains below a brief peak rating. A load model should state its inertias, gravity direction, speed and acceleration, and any efficiency or friction assumptions. Static holding torque alone does not establish dynamic performance.

The numbers here are constructed examples for mechanics practice. They establish no motor, gearbox, biological contact or safety limit. The later actuator lesson adds a conditional torque and sensing budget; the multijoint dynamics lesson includes configuration, coupling and gravity explicitly.
