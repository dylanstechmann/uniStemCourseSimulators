# Assignment 3: stoichiometry, energy and pressure

## The coupled ledger

A closed vessel contains fictional species A2 and A related by A2 ⇌ 2A. Begin with 1.00 amount units of A2 and 0.500 amount units of A. Let forward extent be xi in those amount units. At fixed temperature and volume, stipulate RT=2.00 energy units per amount unit and V=4.00 volume units, giving RT/V=0.500 pressure units per amount unit. The reference pressure is one pressure unit. All parameters are constructed, not a real gas identification or a handling protocol.

The purpose is to connect species amounts, atom conservation, dimensionless equilibrium and a correctly defined energy balance. The earlier reaction-extent and calorimeter readings provide the separate ingredients; this report requires one consistent state and boundary throughout. Save equations, plots, calculations and assumptions locally. The selected browser fields do not evaluate the full ledger or computational method.

## Task A: derive the feasible domain

Write n_A2=1−xi and n_A=0.5+2xi. Determine the complete extent interval from both species' nonnegativity conditions: −0.25≤xi≤1. Explain the meaning of negative extent for this initial mixture. A negative extent is a reverse reaction direction, not automatically an invalid root. A root outside the interval is invalid even if it solves a multiplied equilibrium polynomial.

Show that 2n_A2+n_A=2.5 atom-amount units at every feasible extent. Contrast this invariant with total molecular amount 1.5+xi, which changes because the stoichiometric molecular count changes. Derive total pressure from the changing total molecular amount. Fixed temperature and volume do not imply fixed pressure when a reaction changes the number of molecules.

## Task B: solve a dimensionless equilibrium

For ideal partial pressures and the declared reference, Kp=[(p_A/p°)²]/(p_A2/p°). Set Kp=2/3. Substitute the amounts and pressure scale, obtaining 0.5(0.5+2xi)²/(1−xi)=2/3. Solve the resulting quadratic and test every algebraic candidate in the original expression and feasible domain.

The accepted forward extent is xi=0.25. It gives n_A2=0.75, n_A=1.00 and total amount 1.75. Total pressure is 0.875 in the named pressure units. Report each partial pressure as an independent check and recompute Kp from them. Do not erase p° from the conceptual derivation because its numerical value happens to equal one in this scale. An equilibrium constant's dimensionless definition and a convenient concentration-form parameter are distinct objects.

Plot the reaction quotient across the interior feasible interval, showing its limiting behavior at the species-exhaustion boundaries. Determine the initial direction from Q versus K before solving. A polynomial method can return roots at or beyond a boundary where the original ratio is undefined; the original equation and species domain decide admissibility.

## Task C: use the actual mechanical boundary

Stipulate a constant reaction enthalpy of +6 energy units per extent unit and ideal-gas behavior at the same temperature. Since the stoichiometric change in gas amount is +1 per extent unit, reaction internal energy is Delta_r U=Delta_r H−RT=4 energy units per extent unit. For the actual rigid, closed, isothermal vessel, assume only pressure–volume work and negligible kinetic, potential and mixing internal-energy changes. Then boundary work is zero and required heat into the vessel is q_V=xi Delta_r U=1.00 energy unit.

A claim q=xi Delta_r H would instead give 1.50. Explain the boundary assumptions under which heat can equal an enthalpy change. A hypothetical constant-pressure path reaching the same composition has a different volume/work ledger; its equilibrium constraints must be solved afresh if it is also required to equilibrate. Do not silently impose fixed pressure on the same fixed-volume process. Positive heat here maintains the stipulated temperature during endothermic dissociation, rather than predicting a temperature rise.

## Task D: sensitivity and model limits

Perturb the input Kp and pressure scale separately in a local numerical study. Solve the original equation with bracketing inside the feasible interval and record quotient residuals and conserved atom totals. Explain why changing temperature while keeping Kp fixed would generally be a different stipulated model: equilibrium constants and enthalpies are temperature dependent for real systems.

Check dimensions at each step and distinguish a species amount, total molecular amount, atom-amount invariant and extent. The packet should contain the physical-domain proof, both algebraic roots with rejection reasons, partial/total pressure table, signed energy/work balance and an explicit distinction between the actual rigid vessel and the hypothetical constant-pressure comparison. Three-significant-figure checkpoints assess selected values. Every species and number is synthetic original AI-assisted instruction; the linked MIT OCW 5.111SC Fall 2014 Units I–III guide scope without supplying this exercise or certifying its chemical review.
