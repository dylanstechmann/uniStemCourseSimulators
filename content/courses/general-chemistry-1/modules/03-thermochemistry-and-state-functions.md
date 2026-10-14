# Thermochemistry and state functions

## Learning objectives

By the end of this lesson, you should be able to:

1. Use a stated first-law sign convention to interpret heat flow and reaction enthalpy.
2. Calculate reaction enthalpy from standard enthalpies of formation and balanced-equation coefficients.

## Define the system before assigning a sign

Thermochemistry tracks energy changes during chemical and physical processes. First choose a system, the part being studied, and identify its surroundings. For a reacting mixture, the reaction mixture is often the system; the solution, vessel and room may be part or all of its surroundings depending on the measurement model.

This lesson uses the convention ΔU = q + w. Heat q is positive when energy enters the system as heat. Work w is positive when the surroundings do work on the system. Expansion against an external pressure is work done by the system, so it contributes negative w under this convention. The first law is an energy balance: energy is conserved across the boundary even though it can move as heat or work. A sign has meaning only after the system and convention are stated.

Exothermic describes heat leaving the reacting system under the specified conditions; endothermic describes heat entering it. In an insulated calorimetry model, heat gained by the surroundings balances heat lost by the reaction. Thus q_reaction = −q_surroundings when the defined components account for the exchange. A thermometer usually reports the surroundings’ temperature change, not the sign of the reaction heat directly.

## Calorimetry connects temperature to heat

For a sample with mass m, specific heat capacity c, and temperature change ΔT, the simple model is q = m c ΔT. Here ΔT means final temperature minus initial temperature. If the solution warms, its q is positive; under the idealized isolated-cup assumption, the reaction released that heat and has negative q. If the solution cools, the signs reverse.

Consider explicitly synthetic values: 100.0 g of solution with c = 4.184 J/(g·°C) warms by 2.50 °C. The solution’s heat change is 100.0 × 4.184 × 2.50 = 1,046 J, or 1.05 kJ at the precision of the inputs. If heat exchange with the room is negligible and the cup absorbs negligible heat, the reaction heat is approximately −1.05 kJ. If the calorimeter itself absorbs appreciable heat, include its heat capacity; if the apparatus leaks heat, the simple balance is incomplete. These values illustrate unit and sign reasoning and are not measurements.

Mass and specific heat capacity must match the material whose temperature change is used. A solution’s mass is not automatically the same as the mass of solvent alone, and a coffee-cup calorimeter is not perfectly isolated. State which heat capacities and components are included rather than treating a measured temperature as a direct reaction enthalpy.

## Enthalpy is a state function

Internal energy U and enthalpy H are properties of a system’s state. Enthalpy is defined by H = U + PV. For a change at constant pressure with only pressure–volume work, the system’s heat flow equals its enthalpy change: q_p = ΔH. This connection makes enthalpy convenient for many reactions performed near constant atmospheric pressure. A constant-volume bomb-calorimeter measurement has different boundary conditions and does not simply report q_p as ΔH.

Because U and H are state functions, their changes depend on initial and final states, not on the route between them. Heat and work are path-dependent transfers: two different pathways between the same states can exchange different amounts of q and w while giving the same ΔU. Hess’s law is a practical consequence of the state-function property for reaction enthalpy. If balanced equations are reversed, scaled, and added to produce a target equation, reverse the sign of the corresponding ΔH, scale ΔH with every coefficient, and add the adjusted enthalpy changes.

Do not confuse the sign of ΔH with the speed of a reaction or with its spontaneity. Enthalpy change describes an energy difference under stated conditions. A negative value says the system’s enthalpy decreased; it does not say how fast the transformation occurs or whether it proceeds without other energetic and environmental considerations.

## Formation enthalpies calculate a reaction change

The standard enthalpy of formation, ΔH_f°, is the enthalpy change for forming one mole of a substance from its elements in their reference forms under the stated standard-state convention. An element in its standard reference form has ΔH_f° = 0 by definition. A balanced reaction’s standard enthalpy change can then be calculated as:

ΔH_rxn° = ΣνΔH_f°(products) − ΣνΔH_f°(reactants)

The coefficient ν weights each formation value. Keep the products-minus-reactants order visible; reversing it reverses the sign. The result corresponds to the balanced reaction as written. If every coefficient is doubled, the reaction enthalpy is doubled as well.

For the first practice calculation, the sum for products is −620 kJ/mol and the sum for reactants is −410 kJ/mol. Subtracting gives ΔH_rxn° = −620 − (−410) = −210 kJ/mol. The negative sign indicates an exothermic reaction in the stated standard-state convention.

For methane combustion as written, CH₄ + 2 O₂ → CO₂ + 2 H₂O(l), use ΔH_f° values of −74.8 kJ/mol for CH₄, −393.5 kJ/mol for CO₂, and −285.8 kJ/mol for liquid water; O₂ in its standard form contributes zero. The products sum to −393.5 + 2(−285.8) = −965.1 kJ/mol of reaction. The reactants sum to −74.8 + 2(0) = −74.8 kJ/mol of reaction. Their difference is −890.3 kJ/mol of reaction as written. The value is not a rate, and it does not apply unchanged to gaseous water or different reference states.

## Common errors and limits

- Do not use a heat sign without first naming the system and the sign convention.
- Do not assign the solution’s heat directly to the reaction; under the ideal isolated model their signs are opposite.
- Do not use q_p = ΔH for any boundary condition. The relation assumes constant pressure and only pressure–volume work.
- Do not treat heat or work as state functions; only the net state change is route-independent.
- Do not reverse products and reactants in the formation-enthalpy equation or omit stoichiometric coefficients.
- Do not infer rate, safety or spontaneity from a negative reaction enthalpy alone.
- Report the requested units and preserve guard digits during arithmetic; precision depends on the supplied data and reporting policy.

The calorimetry values above are synthetic. The lesson provides calculation models, not experimental instructions or a heat-source procedure.

## Further study

OpenStax, *Chemistry 2e*, provides the linked primary sections [5.2, Calorimetry](https://openstax.org/books/chemistry-2e/pages/5-2-calorimetry) and [5.3, Enthalpy](https://openstax.org/books/chemistry-2e/pages/5-3-enthalpy). These are link-only references; no source text, problem, figure or data set is reproduced here.
