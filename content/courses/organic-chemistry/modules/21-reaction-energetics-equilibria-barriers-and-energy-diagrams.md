# Reaction energetics: equilibria, barriers and energy diagrams

The structure and acid–base lessons ask where electrons move. Two further questions decide what a reaction actually does: how far it goes, and how fast it gets there. Two different energies answer them. The free-energy difference between reactants and products, ΔG°, sets the equilibrium. The barrier to the highest transition state, ΔG‡, sets the rate. Mixing the two up is one of the most common errors in mechanism reasoning. General Chemistry II develops the general relations in its [free-energy and equilibrium lesson](../../general-chemistry-2/modules/08-free-energy-and-equilibrium.md) and its [rate-law and Arrhenius lesson](../../general-chemistry-2/modules/06-rate-laws-half-lives-and-arrhenius.md); this lesson applies them to organic mechanisms. All energies here are synthetic teaching values, the temperature is 298 K unless stated, and R = 8.314 J/(mol·K), so RT = 2.48 kJ/mol.

The [MIT OCW 5.12 Organic Chemistry I (Spring 2005) calendar](https://ocw.mit.edu/courses/5-12-organic-chemistry-i-spring-2005/pages/calendar/) gives sessions 8–11 to an overview of chemical reactions, thermodynamics, kinetics and reaction coordinate diagrams, and names the Hammond postulate in session 14. [UCI OpenCourseWare Chem 51A (Fall 2009)](https://open.uci.edu/courses/chem_51a_organic_chemistry_nowick.html) gives lectures 18–20 to understanding organic reactions, energy diagrams, transition states and reaction rates, and the energetics of reactions. Both are link-only scope comparators; no text, figure or problem is reproduced.

## Learning objectives

By the end of this lesson, you should be able to:

1. Relate a standard free-energy difference to an equilibrium constant and to populations for conformer, acid–base and reaction equilibria, separate the enthalpy and entropy contributions, and estimate a reaction enthalpy from stipulated bond dissociation energies.
2. Read a reaction energy diagram: identify transition states, intermediates and the rate-determining step, convert barrier differences into rate ratios, and match the diagram to a rate law.
3. Apply the Hammond postulate and the distinction between kinetic and thermodynamic control to predict which product dominates under stated conditions, and explain why a catalyst changes rates but not the equilibrium constant.

## How far: free energy and the equilibrium constant

For any equilibrium,

\[
\Delta G^\circ = -RT\ln K .
\]

At 298 K, RT ln 10 = 5.7 kJ/mol, so every 5.7 kJ/mol of ΔG° changes K by a factor of ten. A negative ΔG° means K > 1; it says nothing about how quickly equilibrium is reached.

The relation covers equilibria you have already met. The [conformations lesson](08-conformations-fischer-maps-and-stereochemical-labels.md) weighted a higher conformer by exp(−ΔE/RT); that weight is the equilibrium constant between the two conformers. Stipulate a substituent whose axial chair lies 7.0 kJ/mol above its equatorial chair. Then K = e^(−7.0/2.48) = 0.059, and about 5.6% of molecules are axial at any moment. The chairs interconvert quickly because the barrier between them is low; their ratio is still an equilibrium ratio. The proton transfer in the [acid–base lesson](07-structure-electron-flow-and-acid-base-balance.md) had K = 10⁴, which corresponds to ΔG° = −RT ln 10⁴ = −22.8 kJ/mol.

Free energy has an enthalpy part and an entropy part,

\[
\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ .
\]

Joining two molecules into one usually lowers entropy. Stipulate an association with ΔH° = −40 kJ/mol and ΔS° = −120 J/(mol·K). At 298 K, ΔG° = −40 + 35.8 = −4.2 kJ/mol and K = 5.5, but at 350 K, ΔG° = +2.0 kJ/mol and K = 0.50; the sign changes at 333 K. The reverse logic applies to steps that make more molecules than they consume: their positive ΔS° gains weight as the temperature rises. That is one reason elimination, which releases an extra molecule, competes better with substitution when a reaction is heated, as the [substitution and elimination lesson](09-substitution-elimination-and-competing-pathways.md) describes.

**Bond dissociation energies** estimate ΔH°. A bond dissociation energy is the enthalpy to break a bond homolytically, each atom keeping one electron. For a gas-phase step R–H + Br–Br → R–Br + H–Br, with stipulated values C–H 415, Br–Br 190, C–Br 285 and H–Br 365 kJ/mol, the bonds broken cost 605 kJ/mol and the bonds formed return 650 kJ/mol, so ΔH° ≈ −45 kJ/mol. Such a sum is a gas-phase enthalpy estimate. It is not a free energy, and it does not describe heterolysis into ions in solution, where solvation dominates.

## How fast: barriers and rates

The rate depends on the barrier ΔG‡ from the starting point to the highest transition state. For two competing pathways from the same reactants,

\[
\frac{k_1}{k_2} = e^{(\Delta G^\ddagger_2 - \Delta G^\ddagger_1)/RT} .
\]

A barrier 5.7 kJ/mol lower means a tenfold faster pathway; 10 kJ/mol lower means about 57 times faster. Transition-state theory supplies an absolute scale, k = (k_B T/h) e^(−ΔG‡/RT), with k_B T/h = 6.21 × 10¹² s⁻¹ at 298 K, taking every crossing of the transition state as reactive. In this model a first-order step with an 80 kJ/mol barrier has a half-life of about 12 s, one with 90 kJ/mol about 11 minutes, and one with 100 kJ/mol about 10.5 hours.

A large K does not make a reaction fast. A strongly downhill reaction with a high barrier can sit unchanged for years, which is why so many thermodynamically unstable organic compounds can be stored.

## Reading an energy diagram

An energy diagram plots free energy along the reaction path. **Transition states** are maxima: fleeting arrangements with partly formed and partly broken bonds that cannot be isolated. **Intermediates** are local minima: real species with finite lifetimes, such as carbocations or tetrahedral adducts.

An SN2 reaction has one step and one transition state that contains both the substrate and the nucleophile, so rate = k[RX][Nu]. Consider instead a synthetic SN1 profile, with energies relative to the reactants: ionization through TS₁ at 96 kJ/mol to a carbocation intermediate at 60 kJ/mol, then capture through TS₂ at 68 kJ/mol to products at −20 kJ/mol. The highest point is TS₁, so ionization is the **rate-determining step**. Only the substrate is involved up to that point, so rate = k[RX], and the nucleophile's concentration does not appear. TS₂ is only 8 kJ/mol above the intermediate, so the carbocation is captured far faster than it forms.

If the same substrate also has an SN2 pathway with a 92 kJ/mol barrier, with the nucleophile at its 1 M standard concentration, the SN2 route is faster by e^(4/2.48), about five times. Halving the nucleophile concentration halves the SN2 rate but leaves the SN1 rate unchanged, which is how rate laws distinguish the two mechanisms.

## The Hammond postulate

A transition state resembles the species nearest to it in energy. For an endergonic step such as ionization to a carbocation, the transition state lies late and resembles the carbocation, so whatever stabilizes the carbocation also stabilizes the transition state. In a stipulated linear model, if a substitution pattern stabilizes the carbocation by 30 kJ/mol and the late transition state feels 70% of that, the barrier drops by 21 kJ/mol and ionization becomes about 4800 times faster. The 70% fraction is a teaching assumption, not a measured value. This is why SN1 reactivity and Markovnikov addition in the [alkene-addition lesson](15-alkene-addition-regiochemistry-and-stereochemistry.md) both follow carbocation stability. For a strongly exergonic step the transition state lies early, resembles the reactants, and is much less sensitive to the stability of the product.

## Kinetic versus thermodynamic control

Suppose one reactant can form two products. Product P_K forms through a 75 kJ/mol barrier and lies at −10 kJ/mol; product P_T forms through an 85 kJ/mol barrier but lies lower, at −25 kJ/mol. If both reactions are irreversible under the conditions, as at low temperature or short times, the product ratio equals the rate ratio, e^(10/2.48) ≈ 57 in favor of P_K: **kinetic control**. If the products can re-form the reactant and equilibrate, as at higher temperature or long times, the ratio becomes e^(15/2.48) ≈ 430 in favor of P_T: **thermodynamic control**. The same diagram supports both outcomes; the conditions decide which ratio applies.

A **catalyst** provides a pathway with a lower barrier. Because it lowers the forward and reverse barriers by the same amount, it leaves ΔG° and K unchanged and only brings the system to equilibrium sooner. Lowering both barriers by 20 kJ/mol speeds both directions by about 3200 times.

## Common mistakes

- Confusing ΔG° (how far) with ΔG‡ (how fast).
- Calling an intermediate a transition state, or the reverse.
- Taking the rate-determining step to be the step with the largest single climb instead of the one whose transition state is highest on the diagram.
- Putting the nucleophile into an SN1 rate law.
- Treating a bond-energy sum as a free energy in solution.
- Dropping the T in TΔS°, or mixing J and kJ.
- Assuming a catalyst shifts the equilibrium, or that the most stable product always dominates.

## Worked example

**Problem.** A synthetic substrate reacts by the SN1 profile above: TS₁ at 96 kJ/mol, carbocation at 60 kJ/mol, TS₂ at 68 kJ/mol and products at −20 kJ/mol. Find the overall equilibrium constant, the rate-determining step and rate law, the first-order half-life from the transition-state-theory prefactor, and the new half-life if a substituent stabilizes the carbocation by 30 kJ/mol with 70% of that felt at TS₁.

**Step 1: equilibrium.** ΔG° = −20 kJ/mol, so K = e^(20/2.48) ≈ 3.2 × 10³; the products are strongly favored.

**Step 2: rate-determining step.** TS₁ is the highest point, so ionization is rate-determining and rate = k[RX].

**Step 3: rate constant.** k = 6.21 × 10¹² × e^(−96/2.48) = 9.2 × 10⁻⁵ s⁻¹, so the half-life is ln 2/k ≈ 7500 s, about 2.1 hours.

**Step 4: Hammond estimate.** The barrier falls by 0.70 × 30 = 21 kJ/mol to 75 kJ/mol, the rate rises about 4800 times, and the half-life falls to about 1.6 s.

**Step 5: check.** The capture barrier, 8 kJ/mol above the intermediate, gives a pseudo-first-order rate constant near 2.5 × 10¹¹ s⁻¹ at 1 M nucleophile, so the carbocation never accumulates and ionization alone controls the rate. Neither substituent change alters the overall ΔG° unless it also changes the product's energy.

## Limits of this lesson

All energies, barriers and bond dissociation energies are synthetic. The analysis uses one temperature, ideal 1 M standard states, a transition-state-theory prefactor with every crossing counted as reactive, and no solvent dynamics, tunnelling or separate activation enthalpy and entropy. Bond-energy sums are gas-phase enthalpy estimates, and the 70% Hammond transfer is a teaching assumption. Nothing here describes a real compound, procedure or measured rate. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
