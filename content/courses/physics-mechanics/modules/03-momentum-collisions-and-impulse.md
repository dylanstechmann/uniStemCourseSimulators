# Momentum, collisions, and impulse

## Learning objectives

By the end of this reading, you should be able to:

1. Apply signed momentum conservation to a one-dimensional sticking collision when external impulse is negligible.
2. Calculate impulse as signed area under a force–time curve and relate it to momentum change with units.

## Momentum keeps direction

For a body of mass \(m\) moving with velocity \(\vec v\), linear momentum is

\[
\vec p=m\vec v.
\]

Momentum is a vector. In one dimension, choose a positive direction and retain the sign of each velocity. A negative velocity means momentum points opposite the positive direction. The SI unit is \(\mathrm{kg\,m/s}\). Unlike kinetic energy, momentum is not found by squaring speed, and equal speeds in opposite directions produce opposite momenta.

For the preserved collision item, a 0.10 kg cart moves at +5 m/s and sticks to a stationary 0.40 kg cart. Treat both carts together as the system during the brief collision. Their initial momentum is \((0.10)(+5)+(0.40)(0)=+0.50\,\mathrm{kg\,m/s}\). If net external impulse during contact is negligible, total momentum before and after is the same. After they stick, their combined mass is 0.50 kg, so

\[
v_f=\frac{+0.50\,\mathrm{kg\,m/s}}{0.50\,\mathrm{kg}}=+1.0\,\mathrm{m/s}.
\]

The positive sign indicates motion in the initial cart's direction. Adding speed magnitudes instead would lose the directional information needed to conserve momentum.

## When is momentum conserved?

Momentum conservation is a statement about a system, not an isolated object in every circumstance. The system's total mass is assumed fixed here, and net external impulse must be zero or negligible over the collision interval. Forces the two carts exert on one another are internal to the combined system; their impulses cancel in the total. A net external force acting for a non-negligible time changes the system momentum.

The more general relation is

\[
\Delta\vec p_{\mathrm{system}}=\vec J_{\mathrm{external}}.
\]

The conservation approximation is useful for a short collision when external effects, such as track friction or gravity along an incline, contribute little impulse compared with the interaction being studied. If that comparison is not justified, keep the external impulse in the balance instead of declaring momentum conserved. Later work develops system boundaries and separate force contributions in greater detail.

## Impulse is accumulated force over time

The impulse delivered to a body over an interval is the time integral of net force:

\[
\vec J=\int_{t_i}^{t_f}\vec F_{\mathrm{net}}(t)\,dt=\Delta\vec p.
\]

This is the impulse–momentum theorem. It applies to a changing force as well as a constant one. On a force-versus-time graph, signed area gives impulse: area above the zero-force line contributes positive impulse for the chosen direction; area below contributes negative impulse. The net signed area determines the momentum change.

For a force that remains constant, \(\vec J=\vec F\Delta t\). For a varying force, a force-time integral or a geometric area may be needed. The average net force over a specified interval is \(\vec F_{\mathrm{avg}}=\vec J/\Delta t\); average force preserves total impulse but does not specify the force at each instant. This lesson introduces that distinction without using an average as a peak-load or safety estimate.

For the preserved triangular pulse, force rises linearly from zero to 200 N over 0.020 s and then returns to zero. Its area is

\[
J=\frac12(0.020\,\mathrm s)(200\,\mathrm N)=2.0\,\mathrm{N\,s}.
\]

The pulse points in the positive direction, so the impulse is +2.0 N·s. If that is the only significant impulse on a body, momentum increases by +2.0 kg·m/s. The average force over the 0.020 s pulse is 100 N, even though the peak force is 200 N. The unit check is \(\mathrm{N\,s}=(\mathrm{kg\,m/s^2})\mathrm s=\mathrm{kg\,m/s}\), matching momentum.

Read the graph's axes before computing its area: force is on the vertical axis and time on the horizontal axis, so area has units N·s. A rectangular pulse of height \(F_0\) and duration \(T\) has area \(F_0T\); a triangular pulse with peak \(F_{max}\) over the same width has area \(\frac12F_{max}T\). Treating a triangular peak as if it acted constantly for the whole interval doubles the impulse. If a force later points in the opposite direction, subtract that below-axis area from the earlier positive area. The final momentum is the initial momentum plus the signed net impulse.

## A change of direction can make impulse larger

Suppose a 0.15 kg ball changes velocity from +8 m/s to −4 m/s. Its momentum change is

\[
\Delta p=m(v_f-v_i)=0.15(-4-8)=-1.8\,\mathrm{kg\,m/s}=-1.8\,\mathrm{N\,s}.
\]

The negative sign indicates an impulse opposite the positive direction. The speed changed by 4 m/s, but the velocity changed by 12 m/s because the ball reversed direction. Subtract final and initial velocities in that order. Using only the difference in speed would miss the reversal and give an incorrect impulse.

## Momentum and kinetic energy answer different questions

In the sticking-cart example, total momentum is conserved under the stated approximation. Yet the initial kinetic energy is \(\frac12(0.10)(5^2)=1.25\,\mathrm J\), while the final translational kinetic energy is \(\frac12(0.50)(1^2)=0.25\,\mathrm J\). The translational kinetic-energy decrease is 1.0 J. Momentum conservation does not imply kinetic-energy conservation.

An elastic collision conserves both total momentum and kinetic energy for the selected system. In an inelastic collision, total momentum can still be conserved while some organized translational kinetic energy changes into deformation, thermal energy, sound, rotation, or other internal forms. A collision where objects remain together is perfectly inelastic. Total energy remains conserved when all stores and transfers are counted; the kinetic-energy change alone does not identify where energy went.

## Common checks and limits

- Choose a positive direction before adding momenta or integrating force.
- Use \(v_f-v_i\), not a difference of speed magnitudes, for \(\Delta p\).
- Conserve the total momentum of the declared system only when external impulse is negligible for the accuracy needed.
- Treat force-time area as signed area; a force pulse below zero reduces momentum in the positive direction.
- Distinguish impulse, measured in N·s, from force, measured in N.
- An average force and impulse do not reveal a unique peak-force history or predict tissue injury.

This reading uses one-dimensional, fixed-mass examples and stated collision boundaries. Real force histories can be irregular, and measured external forces may not be negligible. The later impact unit compares stopping-time and stopping-distance models, but neither simple average alone is a validated injury model.

## Further study

These link-only OpenStax University Physics Volume 1 sections provide more detail on [linear momentum](https://openstax.org/books/university-physics-volume-1/pages/9-1-linear-momentum), [impulse and collisions](https://openstax.org/books/university-physics-volume-1/pages/9-2-impulse-and-collisions), and [conservation of linear momentum](https://openstax.org/books/university-physics-volume-1/pages/9-3-conservation-of-linear-momentum). This lesson uses original wording and calculations; no source prose, examples, problems, figures, or datasets are reproduced.
