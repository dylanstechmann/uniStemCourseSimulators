# Assignment 1: impulse, capture and system boundaries

Develop a report comparing a discrete collision with continuous retained-mass capture. Use [momentum/system boundaries](../modules/09-work-momentum-and-system-boundaries.md) and [variable-mass momentum](../modules/14-variable-mass-momentum-and-mass-flow.md). Retain derivations, signed ledgers and any source code locally. Browser practice checks selected outputs and choices, not your full reasoning, figures or implementation. All masses, motions and rates are constructed; no apparatus operation is requested.

## A discrete sticking collision

Two fictional point carts move on a horizontal line. Cart A has mass 0.8 kg and velocity +2 m/s; cart B has mass 1.2 kg and velocity −1 m/s. They stick together. External horizontal impulse over the event is stipulated negligible. Draw the initial and final states with a common rightward-positive axis. Calculate total initial momentum, final velocity, initial and final kinetic energy and their difference. Explain why kinetic energy conservation cannot be imposed along with sticking for these initial conditions.

Repeat the momentum bookkeeping in a frame moving right at 0.5 m/s. Transform every velocity, including the final one. Verify that the predicted final laboratory velocity is unchanged after transforming back. Compare kinetic energies between frames: their individual numerical values can differ, while the energy loss is the same here because the system's mass and total momentum are conserved during the ideal event. Derive that cancellation instead of treating kinetic energy as a frame-independent scalar.

Now allow a stipulated external impulse J during the collision. Express the final velocity as a function of J and identify the assumption that the original calculation removed. Explain why an average contact force cannot be determined from impulse alone without an interaction time. If a time were supplied, distinguish average net force from a particular contact-force component; other forces may contribute to the net impulse.

## A continuously capturing body

An initially 2 kg point body moves at 3 m/s while retaining incoming material at a constant rate q=0.5 kg/s. The incoming stream is at rest in the laboratory before capture. There is no external horizontal force and no outgoing material. Define the system as the growing body and write its mass m(t). Derive the momentum balance from a short time interval, including the incoming momentum. Use it to obtain v(t) rather than substituting a changing mass into fixed-mass F=ma without the flux term.

Calculate mass, velocity and kinetic energy at t=4 s. Show that total momentum of the retained body is constant even though its kinetic energy decreases. Derive the instantaneous mechanical-energy loss rate for capture from rest and integrate it over the interval. Explain what the point-body model does and does not say about where that loss goes. It supplies no temperature, deformation or damage model.

As a transfer check, suppose the incoming stream instead has a constant nonzero laboratory velocity u. Write the short-time momentum equation again and derive the corresponding relation between m, v and u when external force remains zero. Test the special case where the body's initial velocity equals u. Describe why assuming the incoming material always moves at the body's current speed is a different model from a stream at fixed u.

## A force changes the energy ledger

Return to the resting incoming stream and add a constant external force F=3 N in the positive direction. Derive m(t)v(t)=m0v0+Ft and compute v(4). Integrate Fv over the interval to find the external work. Compare initial energy plus work with final kinetic energy, keeping the capture loss as a separate nonnegative term. Do not infer energy conservation merely from a closed momentum equation. A control-volume momentum balance and an energy balance ask different questions.

Provide an implementation or a reproducible calculation table for both capture scenarios at t=0,1,2,4 seconds. Check m>0, dimensional consistency, the zero-capture limit and the equal-stream/body-velocity limit. Explain why numerical agreement with a stipulated analytic model does not validate a real particle-capture mechanism. If you solve the balance numerically, compare two step sizes and retain the momentum and energy residuals.

## Self-review after attempting the report

The sticking collision has initial momentum 0.4 kg m/s, final velocity 0.2 m/s and kinetic energies 2.2 J before and 0.04 J after, a loss of 2.16 J. With no external force in the resting-stream capture model, mass at four seconds is 4 kg and velocity 1.5 m/s. Kinetic energy falls from 9 J to 4.5 J while momentum stays 6 kg m/s.

With the added 3 N force, momentum at four seconds is 18 kg m/s and velocity 4.5 m/s. The external work is 3[24−12 ln(2)] joules. Use your own energy ledger to evaluate the capture loss and verify its sign. The incoming resting material carries zero laboratory kinetic energy; adding it does not make the capture process mechanically lossless.

A complete report includes a declared boundary, flux terms, a frame comparison, separate momentum/energy ledgers, limiting cases and evidence of reproducibility. This original coursework was developed with substantial AI assistance. The [MIT OCW 8.01SC Fall 2016 syllabus](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/syllabus/) provides a link-only comparator for momentum, collisions and mass transfer; no source problem, figure or dataset was imported. The course remains partial and unreviewed; written work and workload require actual review.
