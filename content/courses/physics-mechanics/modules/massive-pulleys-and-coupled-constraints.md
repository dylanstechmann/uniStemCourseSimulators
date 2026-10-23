# Massive pulleys and coupled constraints

A massless rope can have equal tension along one freely suspended segment without having equal tension on opposite sides of a massive pulley. The pulley needs a net torque to accelerate, so its rotational equation matters alongside the translating masses. This reading develops the coupled equations, a constraint and an independent energy check. Review [force/contact balances](08-free-body-diagrams-contact-and-friction.md) and [torque/rotation](10-torque-angular-momentum-and-rolling.md). Every mass, dimension and motion is stipulated; no equipment construction or operation is requested.

## Define the system before choosing equations

Two hanging point masses m1 and m2 are connected by a light inextensible rope over a fixed-axis pulley of radius R and moment of inertia I. The rope remains taut and does not slip relative to the rim. The axis has no dissipative torque. The rope's moving mass, air resistance and deformation are neglected. Take m2>m1, with positive acceleration a downward for m2 and upward for m1. Both coordinates therefore increase in their respective motion directions. Positive pulley angular acceleration is the sense associated with m2 descending.

The accessible text free-body description is: mass one has upward rope tension T1 and downward weight m1g; mass two has upward rope tension T2 and downward weight m2g. The pulley has tangential rim forces from the two rope segments, plus forces at its axle and its own weight. The axle and weight produce no torque about the central fixed axis in this model. They still matter in a complete force balance for the pulley support; zero axis torque does not mean zero axle force.

The inextensible rope gives equal magnitudes of the two linear accelerations. No slip at the rim gives alpha=a/R. Neither relation is a force law. A rope that stretches, slips or goes slack needs a different constraint. Write the geometry and signs before substituting a shared symbol a; otherwise two downward-positive coordinates can accidentally be assigned the same signed acceleration.

## Solve translation and rotation together

The mass equations are T1−m1g=m1a and m2g−T2=m2a. The pulley torque equation is (T2−T1)R=I alpha. Combining with alpha=a/R gives T2−T1=(I/R²)a. Add the equations to eliminate both tensions:

$$a=\frac{(m_2-m_1)g}{m_1+m_2+I/R^2}.$$

The extra I/R² has units of mass and represents rotational inertia reflected through the no-slip constraint. It is not an additional translating object. Recover tensions separately: T1=m1(g+a), T2=m2(g−a). They differ whenever I and a are nonzero. Assuming equal tensions at the outset would force zero net pulley torque and contradict its acceleration.

The rope is light, but it changes direction while interacting with the pulley. Static contact forces between rope and rim transmit tangential force; an ideal axle means no dissipative bearing torque, not an absence of rim traction. Adequate traction is stipulated here. If a finite traction limit were supplied, its feasibility would require another check. An observed slip would invalidate alpha=a/R rather than justify retaining the same solution with a different label.

## Worked coupled solution

Take m1=2 kg, m2=4 kg, R=0.20 m and I=0.040 kg m², with g=9.81 m/s². Then I/R²=1 kg and a=2g/7≈2.8028571 m/s². T1≈25.225714 N and T2≈28.028571 N. The pulley angular acceleration is a/R≈14.014286 rad/s². The tension difference times radius is about 0.56057143 N m, agreeing with I alpha. Keep full precision until reporting a chosen number of significant figures.

As I tends to zero with the other assumptions fixed, the denominator loses I/R² and the tension difference tends to zero. If m1=m2 and both start at rest, the solution has zero acceleration even when I is nonzero. As I becomes very large, acceleration tends to zero while the tensions approach their static weights. These are algebraic limiting checks, not a claim that a real pulley can have unlimited inertia without other changes.

## Energy checks the same coupled model

Start from rest and let m2 descend a distance s while m1 rises the same distance. The gravitational potential reduction is (m2−m1)gs. Both masses have speed v and the pulley has angular speed v/R. The kinetic energy gain is

$$\frac12(m_1+m_2)v^2+\frac12I(v/R)^2.$$

Equating these yields v²=2as with the acceleration derived from the force/torque system. This agreement is an independent balance check. Tensions transfer energy among the subsystems; they do not disappear from each subsystem's work merely because their net work cancels in the complete ideal system. The axle remains fixed, so its force has zero power in this frame.

For a distinct rehearsal take m1=3 kg, m2=5 kg, R=0.10 m, I=0.020 kg m² and s=0.40 m from rest. The effective total mass is 10 kg, giving a=1.962 m/s², T1=35.316 N and T2=39.24 N. The speed squared is 1.5696 m²/s². Gravitational release and total kinetic energy are both 7.848 J. Omitting pulley rotation would assign all that energy to only eight kilograms of translating mass and overestimate speed.

## Constraint failure is a new problem

If the descending mass hits a stop, the following motion may include rope slack, impact or a changed contact state. The constant-acceleration solution applies only before that event. If the rope is cut, equal-acceleration coupling vanishes. If the pulley radius changes, the geometry may no longer be represented by a constant R. A consistent report names the interval and state over which the supplied equations apply.

Use a separate force diagram for every subsystem, a written constraint ledger and one energy/limiting-case check before accepting a numerical result. The [constrained-motion assignment](../assignments/coursework-02-constrained-motion.md) supplies new masses and asks for an independently solved linear system, energy accounting and a boundary-state discussion.

MIT OCW [8.01SC Classical Mechanics Fall 2016 syllabus](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/syllabus/) provides a link-only comparator for pulley constraints and rotational dynamics. This explanation, diagram description, derivation and all inputs are original, developed with substantial AI assistance; no source problem or figure was imported. Rigid, light-rope, no-slip and ideal-axis assumptions are stipulated. Support design, real traction, elastic ropes and apparatus validation remain outside the model. The course remains partial and unreviewed, with workload unmeasured.
