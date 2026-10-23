# Assignment 2: a coupled-motion and constraint report

Use the [massive-pulley reading](../modules/massive-pulleys-and-coupled-constraints.md), [free-body reading](../modules/08-free-body-diagrams-contact-and-friction.md) and [work/energy reading](../modules/02-work-energy-and-power.md) to analyze a complete ideal motion before a boundary event. Produce a locally saved report with free-body descriptions, constraints, equations and an independent energy check. Browser checkpoints assess selected values; they do not assess your diagrams, derivations or any real mechanism.

## Supplied system

Two point masses m1=2 kg and m2=6 kg hang from a light inextensible rope over a fixed-axis pulley. Radius is 0.20 m and moment of inertia is 0.080 kg m². The rope stays taut and does not slip on the rim. The axis has no dissipative torque. Both masses start at rest; mass two can descend 0.25 m before reaching a stipulated stop. Use g=9.81 m/s² and restrict the requested coupled solution to the interval before impact. Rope stretch, air resistance and contact deformation are absent by assumption.

Define positive motion upward for mass one, downward for mass two and the corresponding angular sense for the pulley. Write a verbal or drawn free-body diagram for each mass and the pulley. Include axle forces in the pulley diagram even if they disappear from its central-axis torque equation. Explain why the pulley's mass need not be known to solve the supplied rotational motion when I is given, yet would be needed for its complete support-force balance.

## Solve the coupled equations independently

Derive the two translational equations, the torque equation and the geometric no-slip relation. First solve for acceleration and tensions by elimination. Then solve the same linear system with a matrix method or a separately organized substitution, retaining the residual of each original equation. State why light rope does not justify equal tensions across the massive pulley. Identify where a finite rim-traction limit would enter if one were supplied.

Calculate angular acceleration, the two tensions, and the time and speed when mass two reaches the stop. Integrate constant acceleration from rest rather than assuming a terminal speed. Check that each tension remains positive and that the assumed downward acceleration sign is consistent with the result. If a computed sign were negative, explain whether the algebra would be invalid or the actual direction would simply oppose your initial positive direction.

Use gravitational potential reduction to calculate the endpoint speed independently. Partition the kinetic energy between the two translating masses and the rotating pulley. Compare the sum with the potential reduction and explain how tension work transfers energy among the subsystems. A fixed axle can exert force while doing zero power in this laboratory frame; explain why this does not remove its role from a force diagram.

## Vary a constraint or an assumption

Repeat symbolically as I tends to zero and as m2 approaches m1. Describe both acceleration and tension difference in each limit. Then compare the supplied pulley with another having twice the moment of inertia and the same radius. Predict the direction of the acceleration and endpoint-speed changes before calculating them. A parameter change that slows the motion need not change the available gravitational energy at a fixed drop; explain where the energy partition changes.

At the stop, the ideal pre-impact solution ends. List at least two physically different continuations consistent with the limited information given, such as slack-rope or continuing contact behavior, and identify missing assumptions needed to choose one. Do not extend constant acceleration through the event or invent a restitution coefficient. Distinguish a boundary-state uncertainty from arithmetic error in the valid pre-impact phase.

For a computational extension, integrate the translating and rotating equations with a shared constraint variable. Track the differences between the two rope displacements and between rope speed and rim speed. Compare an algebraically constrained formulation with one that independently integrates all coordinates; explain why numerical constraint drift can occur in the latter. Refine the time step and retain error/conservation evidence, without treating a matching graph as real apparatus validation.

## Self-review and completion standard

The reflected pulley inertia is I/R²=2 kg, so the effective total mass is 10 kg. Acceleration is 3.924 m/s², with T1=27.468 N and T2=35.316 N. Angular acceleration is 19.62 rad/s². At the 0.25 m drop, speed squared is 1.962 m²/s². The potential reduction is 4×9.81×0.25=9.81 J, matching the total kinetic energy 0.5×10×1.962. Calculate speed and time with full precision before reporting them.

The tension difference is 7.848 N and produces torque 1.5696 N m, equal to I alpha. Energy assigned to the pulley is 1.962 J and to the translating masses 7.848 J. Your report should recover these values from its own independent balances, not use them as substituted input.

Retain signed diagrams, the original linear system, residuals, constraint and energy checks, limiting cases and an explicit stopping event. The report is original, developed with substantial AI assistance, and uses [MIT OCW 8.01SC Fall 2016](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/syllabus/) as a link-only scope comparator. No source problem or diagram was imported. The model establishes no real support, traction or equipment specification; qualified review and measured workload remain open, and the course stays partial and unreviewed.
