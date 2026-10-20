# Redox project guide: a fictional cell from electron balance to charge accounting (optional, ungraded)

**Status:** open, optional and ungraded. Five milestone self-checks in the Case studio save responses privately; nothing is submitted, collected or scored. The separate inactive project draft and its proposed review rubric remain unreviewed and are not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 2–4 hours across weeks 8 and 9.
**Prerequisite lessons:** [Redox and electrochemical cells](../modules/03-redox-and-electrochemical-cells.md), [Redox direction and metal centers](../modules/07-redox-potentials-and-metal-centers.md), [Free energy, equilibrium and reaction direction](../modules/08-free-energy-and-equilibrium.md) and [Electrochemical stoichiometry, composition and work](../modules/12-electrochemical-stoichiometry-and-work.md).

## Purpose

The project follows one fictional cell through the chain that weeks 2, 7 and 8 build: a balanced electron transfer, a standard cell potential, the standard Gibbs energy and equilibrium constant, a Nernst correction for a stated composition, and Faraday's-law amount accounting. Every step reuses the balanced equation from the first, so an error in the cathode choice or in n carries through to the end. The last step names what a paper calculation cannot say about a real cell.

## The project

The symbols A and B are fictional bookkeeping tokens, not elements or chemical species. Use these formal standard reduction reactions:

- A²⁺ + 2e⁻ ⇌ A(s), E°_A = −0.200 V
- B³⁺ + 3e⁻ ⇌ B(s), E°_B = +0.400 V

At T = 298.15 K, take R = 8.314 J/(mol·K) and F = 96,485 C/mol e⁻. For a separate nonstandard-state calculation, use dimensionless activities a(A²⁺) = 0.100 and a(B³⁺) = 0.0100; pure solids have activity one. For the charge-accounting part only, stipulate I = 0.200 A for 30.0 min with 100% Faradaic efficiency.

1. Select the cathode, reverse and scale the anode half-reaction, and write the balanced net reaction. Check both the electron count and the net charge.
2. Calculate E°cell, ΔG° = −nFE°cell and ln K = nFE°cell/(RT). State why a large K is consistent with the sign of ΔG°.
3. Form the reaction quotient, omitting pure solids. Use the Nernst equation, E = E°cell − (RT/nF) ln Q, for the supplied activities and compare its sign with the standard-state value.
4. Convert the current and time to total charge, moles of electrons and reaction extent. Use stoichiometry to find the amount of A consumed and of B³⁺ reduced.
5. State which assumptions, especially standard-state conventions, activity modeling, temperature and Faradaic efficiency, would need evidence in a real electrochemical system. Do not infer a real material or experimental procedure.

## Milestones

| Milestone | Suggested week | Task | Where to check yourself |
| --- | --- | --- | --- |
| Rehearsal | 8 | Work the rehearsal cell, then use the open rehearsal practice set | **Practice gradebook**: Redox project rehearsal |
| M1 | 8 | Cathode, balanced net reaction and n (task 1) | Case studio: project milestone 1 |
| M2 | 8 | E°cell, ΔG° and ln K (task 2) | Case studio: project milestone 2 |
| M3 | 8 | Reaction quotient and Nernst potential (task 3) | Case studio: project milestone 3 |
| M4 | 9 | Charge, electrons, extent and amounts (task 4) | Case studio: project milestone 4 |
| M5 | 9 | Assumptions that would need evidence (task 5) | Case studio: project milestone 5 |

Each Case studio milestone lists self-review statements. Responses are saved privately in this application and are never scored.

## Rehearsal cell

Before the project, work the same steps on a second fictional cell, then check yourself with the open rehearsal practice set. Tokens C and D have the formal reductions C⁺ + e⁻ ⇌ C(s), E° = +0.250 V, and D²⁺ + 2e⁻ ⇌ D(s), E° = −0.150 V, at 298.15 K. The Nernst step uses activities a(D²⁺) = 0.0500 and a(C⁺) = 0.0200, and the charge step stipulates 0.250 A for 15.0 min at 100% Faradaic efficiency. The practice set gives feedback on each number. Its tokens, potentials, activities and charge differ from the project's, so its answers are not the project's answers.

## Worked example: a third fictional cell

Take tokens X and Y with X³⁺ + 3e⁻ ⇌ X(s), E° = −0.100 V, and Y⁺ + e⁻ ⇌ Y(s), E° = +0.350 V, at 298.15 K.

1. **Balance.** Y⁺/Y has the higher reduction potential, so Y⁺ is reduced at the cathode and X is oxidized at the anode: X(s) → X³⁺ + 3e⁻. Tripling the Y reduction cancels the electrons: X(s) + 3Y⁺ → X³⁺ + 3Y(s), with n = 3. Each side carries a net charge of +3.
2. **Standard thermodynamics.** E°cell = 0.350 − (−0.100) = 0.450 V; the potential is not tripled. ΔG° = −3 × 96,485 × 0.450 ≈ −130,255 J/mol, or about −130.3 kJ/mol, and ln K = 3 × 96,485 × 0.450/(8.314 × 298.15) ≈ 52.55. A negative ΔG° and ln K > 0 say the same thing: products are favored at standard state.
3. **Composition.** With a(X³⁺) = 0.0200 and a(Y⁺) = 0.100, the solids drop out and Q = a(X³⁺)/a(Y⁺)³ = 0.0200/0.00100 = 20.0. Then RT/(3F) ≈ 0.008564 V and E = 0.450 − 0.008564 × ln 20.0 ≈ 0.4243 V: still positive, and slightly below E°cell because Q > 1.
4. **Charge.** A current of 0.300 A for 8.00 min passes 0.300 × 480 = 144 C, or 144/96,485 ≈ 0.001492 mol e⁻. Dividing by n = 3 gives an extent of about 0.0004975 mol of reaction, so about 0.0004975 mol X is consumed and three times as much, about 0.001492 mol Y⁺, is reduced, if every electron drives this reaction.
5. **Scope.** Every number above follows from stipulated values. A real cell would need measured activities or an activity model, a controlled temperature, and evidence that no side reaction consumed charge.

Writing the net reaction twice as large would double n, ΔG° and ln K and square Q, but E° and E would not change, because the doubled logarithm is divided by the doubled electron count.

## Reporting conventions

- Write every half-reaction as a reduction before choosing the cathode, and never multiply a potential by a stoichiometric coefficient.
- Keep at least four significant figures in intermediate values and round only the reported results. Give ΔG° with its units and say whether they are J/mol or kJ/mol.
- Use the natural logarithm in ΔG° = −RT ln K and in the Nernst equation, or convert explicitly if you work in log₁₀.
- Disclose any software, spreadsheets or AI assistance you used.

## Self-review rubric

The inactive project draft proposes five criteria for a future human reviewer and assigns them no points. For self-review, mark each criterion 0 (absent), 1 (partly correct) or 2 (complete and consistent with the stated model).

| Criterion | Evidence of a complete response |
| --- | --- |
| Redox balance | Chooses the correct cathode and anode directions and balances electrons and charge |
| Thermodynamics | Computes the cell potential and Gibbs-energy sign consistently |
| Equilibrium | Forms Q with the correct powers and applies the Nernst sign |
| Charge accounting | Converts current and time to charge, electron moles and reaction extent |
| Scope | Keeps fictional symbols separate from real chemical and laboratory claims |

These marks are a self-check. They are not calibrated, carry no grade and do not stand in for an instructor's judgment.

## Limitations and provenance

The tokens, potentials, activities, current and time are fictional teaching values. The calculations assume ideal standard-state conventions, stipulated activities, a fixed temperature and 100% Faradaic efficiency, and they ignore junction potentials, overpotentials, cell resistance and side reactions. Nothing here is a cell specification, battery design, laboratory procedure or claim about any real element or material. Original guide and rehearsal values: CC BY 4.0, developed with substantial AI assistance.
