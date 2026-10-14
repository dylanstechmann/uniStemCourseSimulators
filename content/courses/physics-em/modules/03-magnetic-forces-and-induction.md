# Magnetic forces and induction

## Learning objectives

By the end of this reading, you should be able to:

1. Calculate induced-emf magnitude from a changing magnetic flux and account for the number of coil turns.
2. Apply Faraday's and Lenz's laws to relate changing flux to induced-emf magnitude and direction.

## Magnetic force on a moving charge

A charge q moving with velocity **v** through a magnetic field **B** experiences a magnetic force **F**ᵦ = q(**v** × **B**). The magnitude is |Fᵦ| = |q|vB sin θ, where θ is the angle between velocity and field. The force is zero when the velocity is parallel to the field and largest when it is perpendicular. The cross product determines direction: for a positive charge, use the right-hand rule for **v** × **B**; for a negative charge, reverse that direction.

The magnetic part of the Lorentz force is perpendicular to the particle's instantaneous velocity. Therefore **F**ᵦ · **v** = 0 and this force does no work on an isolated point charge. In a magnetic-only model it can change the direction of motion without changing speed or kinetic energy. This statement is about the magnetic force on a point charge. It does not imply that a motor, coil, or complete circuit cannot exchange energy; those systems include currents, electric forces, power supplies, and mechanical constraints.

A current is organized charge motion, so a straight wire segment in a uniform field also experiences a force. With vector **L** directed along conventional current, **F** = I(**L** × **B**), and |F| = ILB sin θ. The direction depends on current orientation and field orientation. The relation describes the selected segment; to find the net force on a complete loop, account for all segments and the field over them. A later week develops signed vector components and force/work distinctions more fully.

## Magnetic flux through a loop

Magnetic flux Φᵦ summarizes how much magnetic field passes through a chosen surface. For a uniform field and a flat loop of area A, **Φᵦ = BA cos θ**, where θ is the angle between **B** and the surface's area-normal vector. Flux is largest when the field is perpendicular to the loop and zero when the field lies in its plane. The SI unit is the weber (Wb), with 1 Wb = 1 T·m².

Flux depends on field strength, loop area, and orientation. It can change if the field's magnitude or direction changes, if the loop's area changes, or if the loop rotates relative to the field. A magnetic field can pass through a stationary loop without inducing an emf if the flux remains constant. It is change in flux that matters for Faraday's law.

## Faraday's law: changing flux induces emf

Faraday's law relates induced electromotive force (emf) to the time rate of change of magnetic flux. For a coil with N turns and the same flux through each turn,

**ε = −N dΦᵦ/dt.**

For a finite interval with an approximately uniform flux change, the average emf magnitude is **|ε| = N|ΔΦᵦ|/Δt**. The turn count multiplies the flux change per turn; do not multiply by N again if the supplied quantity is already flux linkage. Since Wb/s = V, the units provide a quick check.

For the first practice example, each turn's flux changes by 0.004 Wb in 0.02 s. The magnitude is |ε| = 50×0.004/0.02 = 10 V. A separate coil has N = 50, with flux change 2.0×10⁻³ Wb per turn over 0.10 s; its induced-emf magnitude is 50×(2.0×10⁻³)/0.10 = 1.0 V. These are voltage predictions. A sustained induced current also requires a closed conducting path and depends on the circuit's impedance.

The minus sign encodes Lenz's law. It sets a direction relative to the chosen surface normal and loop orientation. If a magnetic flux into the page is increasing, the induced current creates a field out of the page to oppose that increase. If the into-page flux is decreasing, the induced field points into the page to oppose the decrease. Thus Lenz's law opposes the **change in flux**, not necessarily the original field.

## Direction reasoning without losing the sign

To reason about direction, first choose a normal for the loop and state which direction counts as positive flux. Next decide whether that signed flux is increasing or decreasing. Lenz's law gives the direction of the induced field that resists the change. A right-hand rule then gives the current direction that would create that field, if the loop is closed. Finally, the chosen orientation determines the sign of ε in Faraday's equation. A numerical question asking only for emf magnitude needs the absolute value; dropping the minus sign is not a mistake when direction is not requested.

This sequence separates three ideas that are easy to conflate: the externally applied field, the flux through the loop, and the field created by the induced current. The induced effect does not erase the external source; it resists the change that produced it. Energy conservation is consistent with this opposition: sustaining a changing flux against an induced response requires energy transfer from the external agent or source.

## What induction does and does not tell you

A changing flux can induce a voltage even when a loop is open, but a steady current requires a closed path. The Faraday calculation alone does not provide the total current, heating, or mechanical response; those require the circuit elements and boundary conditions. Likewise, force direction on a moving charge and induced-emf direction are different calculations. The first uses q(**v** × **B**); the second uses a signed flux change and Lenz's law.

Pickup coils, generators, and inductive sensors use these relations to convert relative motion or changing fields into voltage. Their real output depends on coil geometry, the time course of the field, winding resistance, connected loads, and measurement circuitry. This introductory model establishes the physical relation but does not predict a particular device's performance. The later induction lessons treat moving conductors, Lenz signs, inductor energy, flow measurement, and current limits in more detail.

## Common checks

- For a negative charge, reverse the positive-charge right-hand-rule force direction.
- Use the angle between the field and the surface normal in Φᵦ = BA cos θ.
- Check whether the question gives flux per turn or total flux linkage before multiplying by N.
- Calculate Wb/s to confirm the induced-emf unit is volts.
- Use an absolute value for a requested magnitude; use the chosen orientation and Lenz's law when direction or sign is needed.
- Oppose a flux **change**, not automatically the direction of the external magnetic field.
- Do not infer a current from an induced emf without knowing whether a conducting path is closed and what impedance it contains.

## Further study

These link-only OpenStax University Physics Volume 2 sections provide more detail: [11.3 Motion of a Charged Particle in a Magnetic Field](https://openstax.org/books/university-physics-volume-2/pages/11-3-motion-of-a-charged-particle-in-a-magnetic-field), [11.4 Magnetic Force on a Current-Carrying Conductor](https://openstax.org/books/university-physics-volume-2/pages/11-4-magnetic-force-on-a-current-carrying-conductor), and [13.1 Faraday's Law](https://openstax.org/books/university-physics-volume-2/pages/13-1-faradays-law). This lesson uses original wording and calculations; no source prose, figures, examples, problem wording, or datasets are reproduced.
