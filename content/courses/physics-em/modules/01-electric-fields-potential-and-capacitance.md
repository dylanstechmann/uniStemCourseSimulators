# Electric fields, potential, and capacitance

## Learning objectives

After this reading, you should be able to:

1. Interpret potential difference as energy per charge and calculate energy stored by an ideal capacitor.
2. Relate parallel-plate geometry and electric field to capacitance and stored energy, while checking units and assumptions.

## Electric field describes force per charge

An electric field **E** describes the electric force that would act on a small positive test charge at a point, divided by that charge: **E = F/q**. The field is a vector; its direction is the force direction for a positive test charge. A negative charge feels a force in the opposite direction. The field is defined by the source charges and surrounding conditions, not by the particular test charge used to measure it.

The electric field gives a local force description. Electric potential gives a complementary energy description. For electrostatic fields, work depends on the start and end points rather than the path, so the change in electric potential energy is a state difference. Field and potential answer related but distinct questions: **E** is a vector that predicts force per charge, while V is a scalar related to potential energy per charge.

## Potential, voltage, and energy per charge

Electric potential at a point is potential energy divided by charge, V = U/q, with a chosen reference for zero potential. The potential difference between points A and B is ΔV = Vᴮ − Vᴬ = ΔU/q for a charge q moved from A to B. Rearranging gives **ΔU = qΔV**. One volt is one joule per coulomb (1 V = 1 J/C). Voltage is another name for potential difference; it is not a quantity of energy by itself.

For a positive charge moved toward higher potential, its electric potential energy increases. For a negative charge, the same potential difference produces an energy change with the opposite sign. This is why the sign of q matters when calculating a particle's ΔU. When describing the energy stored in a capacitor, we usually use the magnitude of its plate charge and the magnitude of the voltage between its plates; the stored energy is nonnegative.

In a uniform field directed along the x-axis, the potential difference over a displacement Δx is ΔV = −EₓΔx. Moving in the field direction takes a positive test charge toward lower potential. For a displacement perpendicular to the field, the potential difference is zero in this ideal uniform-field model. More generally, the potential difference is the negative line integral of the electric field along the path. For the present lesson, the key check is that a scalar voltage difference must be interpreted together with the direction of displacement and the sign of the charge before assigning a change in energy.

## Conductors and electrostatic equilibrium

In electrostatic equilibrium, mobile charge in an ideal conductor has settled so the field inside the conducting material is zero and the conductor is at one potential. Excess charge resides on its surface, with a distribution that depends on the conductor's shape and nearby charges. Two conducting plates separated by an insulating gap can therefore hold equal and opposite charges and establish a potential difference. The field between broad, closely spaced parallel plates is approximately uniform away from their edges; near the edges, fringing makes the field nonuniform.

These statements describe equilibrium electrostatics. They do not apply unchanged while charge is actively moving through a circuit or while fields vary rapidly in time. Circuit transients and switching are treated in later lessons.

## Capacitance connects charge to voltage

A capacitor is a pair of conductors arranged so charge can be separated between them. For an ideal linear capacitor, capacitance C is the magnitude of stored charge on either plate divided by the magnitude of the potential difference: **C = Q/|ΔV|**. Capacitance is measured in farads, where 1 F = 1 C/V. It describes how much charge corresponds to a given voltage in that capacitor; it is not itself the charge or stored energy.

For two large parallel plates of area A separated by a small distance d, with edge effects negligible and a uniform material of permittivity ε between the plates, **C ≈ εA/d**. For vacuum, ε = ε₀. Increasing plate area gives more capacitance in this model; increasing the separation gives less. The relation depends on the geometry and material, not on how much charge has already been placed on an ideal linear capacitor. The simple formula should not be applied to arbitrary shapes or when fringing and material boundaries are important.

## Energy stored in a capacitor

Separating charge requires work, and that work is stored in the electric field between the plates. During charging, the voltage rises as charge accumulates, so each additional small amount of charge requires work. Integrating that changing voltage gives the energy relation:

**U = ½ Q|ΔV| = Q²/(2C) = ½ C(ΔV)².**

These equivalent forms apply to the same ideal capacitor state. Choose the form that matches the known quantities. When capacitance is in farads and voltage in volts, energy is in joules because F·V² = C·V = J. If C is in microfarads and voltage is in volts, the answer from ½C(ΔV)² is in microjoules because 1 μF·V² = 1 μJ.

For a 10 μF capacitor at 3 V, U = ½(10 μF)(3 V)² = 45 μJ. The squared voltage matters: at fixed capacitance, doubling the voltage multiplies the energy by four. A separate example with C = 2.0×10⁻⁶ F and ΔV = 10 V gives U = ½(2.0×10⁻⁶)(10)² = 1.0×10⁻⁴ J. This also equals 100 μJ. Converting between units at the end provides a useful check.

The stored energy belongs to the electric configuration of the capacitor. It is not the same as instantaneous power, which is energy transfer per unit time, or charge, which is measured in coulombs. A real circuit may dissipate some energy in resistance or deliver it to another component; the capacitor formula alone does not describe that entire circuit history.

## A membrane analogy with limits

Biological membranes separate conductive ionic solutions with a thin, poorly conducting layer, so a membrane region can be modeled approximately as a capacitor. The separated charge and voltage are related through an effective capacitance, and stored electrical energy follows the same ideal relation when the model's assumptions hold. This analogy can organize reasoning about charge separation and field direction. Real membranes also contain channels, transporters, distributed geometry, changing conductance, and nonuniform composition; a single ideal capacitor does not describe all biological behavior or predict a particular cell's voltage by itself.

## Common checks

- Keep potential difference (J/C), potential energy (J), charge (C), and capacitance (F) distinct.
- Use the sign of charge in ΔU = qΔV; for stored capacitor energy, use a nonnegative energy and the plate-voltage magnitude.
- Use **C ≈ εA/d** only for the declared parallel-plate approximation, and state when edge effects or material details may matter.
- Use **U = ½C(ΔV)²** with consistent units. A microfarad multiplied by volts squared yields microjoules.
- Do not assume voltage is energy or that twice the voltage gives twice the stored energy.
- Treat the membrane example as a lumped model, not a complete physiological explanation.

## Further study

These link-only OpenStax University Physics Volume 2 sections give additional background: [7.2 Electric Potential and Potential Difference](https://openstax.org/books/university-physics-volume-2/pages/7-2-electric-potential-and-potential-difference), [8.1 Capacitors and Capacitance](https://openstax.org/books/university-physics-volume-2/pages/8-1-capacitors-and-capacitance), and [8.3 Energy Stored in a Capacitor](https://openstax.org/books/university-physics-volume-2/pages/8-3-energy-stored-in-a-capacitor). This lesson uses original wording and calculations; no source prose, figures, examples, problem wording, or datasets are reproduced.
