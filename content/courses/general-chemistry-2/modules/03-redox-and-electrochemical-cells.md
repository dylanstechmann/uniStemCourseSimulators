# Redox and electrochemical cells

## Learning objectives

By the end of this lesson, you should be able to:

1. Relate a standard cell potential and electron count to a redox reaction's standard free-energy change.
2. Calculate a standard cell potential from reduction potentials and infer the direction favored under standard conditions.

## Oxidation and reduction in a cell

Oxidation is electron loss and an increase in oxidation number; reduction is electron gain and a decrease in oxidation number. A redox reaction couples the two changes, so electrons lost by the reductant must equal electrons gained by the oxidant. In a galvanic, or voltaic, cell, the two half-reactions occur in separate compartments. Their separation forces electron transfer through an external conducting path, where the flow can do electrical work.

The **anode** is where oxidation occurs, and the **cathode** is where reduction occurs. Electrons travel through the external wire from the anode to the cathode. These definitions apply to all electrochemical cells; in a galvanic cell the anode is negative and the cathode is positive. The signs reverse for an electrolytic cell driven by an external power supply. A salt bridge or porous separator permits ions to move and maintain approximate electrical neutrality as oxidation and reduction change each compartment's composition. It completes the ionic part of the circuit; electrons do not travel through the salt bridge.

For the familiar zinc/copper example, the half-reactions in the spontaneous galvanic direction are:

- Anode, oxidation: Zn(s) → Zn²⁺(aq) + 2e⁻
- Cathode, reduction: Cu²⁺(aq) + 2e⁻ → Cu(s)
- Net reaction: Zn(s) + Cu²⁺(aq) → Zn²⁺(aq) + Cu(s)

The electrons cancel when the half-reactions are added. The two-electron count, n = 2, belongs to each mole of the net reaction as written. The inert ions in a salt bridge are not reactants in that net equation.

## Reduction potentials and cell voltage

Tables list standard **reduction** potentials, E°, for half-reactions written as reductions under specified standard-state conditions. Individual half-cell potentials are relative quantities; their tabulated values are established against a reference electrode, conventionally the standard hydrogen electrode assigned E° = 0 V. More positive reduction potential means a stronger thermodynamic tendency for the listed oxidized form to accept electrons relative to that reference.

For a galvanic cell assembled from two standard reduction potentials,

**E°cell = E°cathode − E°anode.**

The cathode is the reduction half-reaction. The anode is the oxidation site, but the table still gives that couple's reduction potential, so subtract it. This sign convention avoids a common double reversal: either reverse the half-reaction and change its potential's sign, then add, or keep tabulated reduction potentials and subtract the anode value. Do not do both.

For the Zn/Cu cell, E°(Cu²⁺/Cu) = +0.34 V and E°(Zn²⁺/Zn) = −0.76 V. Thus E°cell = +0.34 − (−0.76) = +1.10 V. A positive value predicts the net reaction as written is thermodynamically favored under standard conditions. Reversing the cell reaction reverses the sign of E°cell. Voltage is energy per charge (1 V = 1 J/C), so an electrode-potential difference has units of volts.

When writing cell notation, a single vertical line marks a phase boundary and a double line conventionally marks the salt bridge. The Zn/Cu cell can be written Zn(s) | Zn²⁺(aq) || Cu²⁺(aq) | Cu(s), with the anode on the left and cathode on the right in this conventional notation. Notation records the cell arrangement; it does not replace checking which electrode is oxidized or reduced.

The word **standard** refers to specified reference activities: dissolved solutes are at unit activity (often approximated by 1 M in introductory problems), gases at the standard pressure, and pure solids and liquids at unit activity. A temperature must also be specified; many tabulated values use 298.15 K. Standard potential is not automatically the measured voltage in a cell whose composition or temperature differs from these conditions.

## Connecting electrical work and free energy

Moving charge q across a potential difference E transfers electrical energy qE. One mole of electrons carries charge F ≈ 96,485 C mol⁻¹; therefore n moles of electrons per mole of reaction correspond to nF coulombs. Under reversible standard-state conditions, the maximum electrical work relation gives:

**ΔG° = −nFE°cell.**

If E°cell is measured in volts, the product F E°cell has units C·V/mol = J/mol. Convert joules to kilojoules by dividing by 1000 when needed. The minus sign means that positive E°cell corresponds to negative ΔG° and a spontaneous forward reaction at standard state. A negative cell potential has positive ΔG° for the written direction, so its reverse is favored under those same conditions. Neither sign states how quickly equilibrium will be approached; kinetics is a separate question.

For the Zn/Cu example, E°cell = +1.10 V and n = 2, so ΔG° = −(2)(96,485 C/mol)(1.10 J/C) = −212,267 J/mol, or about −212 kJ/mol of reaction as written. If the balanced equation were doubled, E°cell would remain +1.10 V, but n and ΔG° per doubled reaction would also double. Potential is an intensive quantity; free-energy change is extensive with the amount of reaction.

As a separate check matching this lesson's practice item, a cell with n = 2 and E°cell = +0.30 V has ΔG° = −(2)(96,485)(0.30) = −57,891 J/mol ≈ −57.9 kJ/mol. Keep the electron count, potential, sign and energy conversion together. If n is missing, a potential alone does not determine the reaction's free-energy change.

## Standard conditions and actual cell conditions

The thermodynamic relation also holds away from standard state when actual quantities are paired: ΔG = −nFEcell. Composition changes the reaction quotient Q and hence the cell potential. For a reaction at temperature T, the Nernst form is Ecell = E°cell − (RT/nF) ln Q, using activities in Q. Under standard-state conditions Q = 1, ln Q = 0, and Ecell = E°cell. In simple aqueous calculations concentrations may stand in for activities, but concentrated or nonideal solutions require more careful treatment.

This lesson emphasizes the standard cell calculations in its preserved practice. A later lesson treats Nernst calculations in greater detail and distinguishes biochemical transformed standard potentials, often written E°′ at fixed pH, from ordinary chemical E°. A biological redox couple's actual potential depends on its oxidized/reduced ratio and environment. A tabulated standard potential alone does not predict the behavior of an entire cell or organism.

## Worked reasoning and common errors

When given two reduction potentials, first assign the cathode as the reduction site and anode as the oxidation site. Subtract the anode's listed reduction potential from the cathode's. Then check whether the sign matches the stated spontaneous galvanic direction. To find ΔG°, balance electrons in the half-reactions, identify n per net reaction, calculate −nFE°cell and convert units. Scaling a half-reaction to balance electrons never scales its tabulated potential.

Common errors include reversing the electron-flow direction, confusing anode with the positive electrode in a galvanic cell, adding the anode reduction potential instead of subtracting it, multiplying potential by a stoichiometric coefficient, omitting n from ΔG°, and reporting joules as kilojoules. Another error is to interpret positive E° as “fast”: potential indicates a thermodynamic direction under stated conditions, not a reaction rate.

## Further study

These link-only OpenStax Chemistry 2e sections give further background: [17.2 Galvanic Cells](https://openstax.org/books/chemistry-2e/pages/17-2-galvanic-cells), [17.3 Electrode and Cell Potentials](https://openstax.org/books/chemistry-2e/pages/17-3-electrode-and-cell-potentials), and [17.4 Potential, Free Energy, and Equilibrium](https://openstax.org/books/chemistry-2e/pages/17-4-potential-free-energy-and-equilibrium). This lesson uses original wording and calculations; no source prose, figures, examples, problem wording, or datasets are reproduced.
