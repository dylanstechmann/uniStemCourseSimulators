# Assignment 3: a sliding-to-rolling transition study

Produce an analytic and numerical study using the [contact-power reading](../modules/sliding-to-rolling-and-contact-power.md) and [rolling-constraint reading](../modules/10-torque-angular-momentum-and-rolling.md). Retain equations, source or calculation tables, event records and an interpretation report locally. Browser items assess selected responses; they do not execute or evaluate the simulation, verify a friction law or assess your written explanation. All bodies and surfaces are ideal teaching models.

## Primary slipping state

Stipulate a rigid body with mass 1.5 kg, radius 0.12 m and I=0.4mR². It initially translates right at u=2.8 m/s with no spin on a fixed horizontal surface. During slip, kinetic friction has magnitude mu mg with mu=0.25 and g=9.81 m/s². There are no other horizontal forces, no rolling resistance and maintained contact. Rightward center velocity is positive; clockwise angular velocity is positive. The bottom-point relative slip is s=v−R omega.

Draw the force and torque directions for the initial phase. Derive equations for v and R omega, then calculate transition time, transition center speed and angular speed. Integrate center motion to determine the transition distance. Show that the no-slip event s=0 is a state condition, not a time chosen from a plot by eye. Derive the mechanical-energy loss by both endpoint energies and the time integral of contact power.

Explain why friction impulse changes center momentum while also generating rotation. Demonstrate that force times center displacement alone is not the total mechanical-energy loss. Identify the point at which force is applied and calculate its instantaneous laboratory velocity. Relate that contact velocity to the sign of frictional power throughout the slipping phase.

## A contrasting overspin state

Use the same body and surface, but start with center speed u=0.8 m/s and clockwise rim speed R omega0=2.0 m/s. Determine the sign of the initial slip before selecting friction direction. Calculate the new transition time and rolling speed. Compare the center's speed change with the total mechanical-energy change. Explain how the center can speed up while friction still removes total mechanical energy. Treat center velocity, angular velocity, slip and energy as separate recorded variables.

Derive a general final-speed expression for arbitrary u and initial rim speed w0 under the stipulated model. Check the already-rolling limit u=w0. Analyze the zero-friction limit carefully: the final algebraic transition state may be formally expressible, but with nonzero initial slip it is never reached in finite time when mu=0. State which limit concerns a possible state and which concerns its attainability.

## Simulate phases with an event

Choose a numerical integrator and resolve the slipping phase until the first zero of s. If one step crosses the event, estimate its time within the step or solve the constant-acceleration event exactly. Restart with the ideal rolling phase: on this unforced horizontal surface, zero friction is sufficient and v and omega remain constant. Do not keep applying the previous kinetic friction sign after slip has ended.

Compare at least three time-step sizes. Report errors in event time, center position, final velocity and energy loss against the analytic reference. Record a deliberately incorrect run that continues the old friction direction beyond the event. Explain its slip reversal and energy behavior using the violated force law; do not describe a numerical artifact as a new physical effect. A passing implementation should preserve the declared phase conditions, not merely produce a smooth curve.

As a model variation, change mu while keeping all other initial conditions fixed. Predict final rolling speed and transition-time scaling before running the calculation. Then change the inertia ratio and explain why the speed and energy partition do change. Distinguish sensitivity to a stipulated parameter from empirical identification of that parameter. No observed data are supplied to validate a real friction coefficient or inertia distribution.

## Self-review after your derivation

For the primary state, final rolling speed is u/(1+0.4)=2.0 m/s. The transition time is 2.8/[0.25×9.81×3.5], about 0.32619776 s. Initial energy is 5.88 J and final translation-plus-rotation energy is 4.2 J, a loss of 1.68 J. Compute center distance and angular speed independently, with units and the shared no-slip check.

For the overspin state, initial slip is −1.2 m/s. Friction points right and the center accelerates. Final rolling speed is (0.8+0.4×2.0)/1.4=8/7 m/s. The loss is 0.5×1.5×[0.4/1.4]×1.2² joules, positive despite that center acceleration. Retain the unrounded expression when comparing numerical results. These are model references, not measured mechanical behavior.

Your study should include sign-resolved diagrams, two phase histories, event handling, independent endpoint/power energy checks, refinement evidence and a deliberately exposed failure. This original AI-assisted assignment uses [MIT OCW 8.01SC Fall 2016 rolling scope](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/syllabus/) as a link-only comparator and imports no source problem or figure. Written reasoning, simulation quality, measured workload and qualified review remain open. The course is partial and unreviewed.
