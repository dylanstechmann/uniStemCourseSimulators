# Electrochemical driving forces, coupled reactions and solvent flux

**Status:** original ungraded instruction with substantial AI assistance. Ions, gradients, energy supplies and membrane coefficients are fictional teaching inputs. The aim is a consistent thermodynamic/transport ledger, not a prediction about a cell, tissue or device. Work with an explicit positive direction before interpreting signs.

## Chemical and electrical terms share an energy basis

For an ion of charge number z, the electrochemical potential is μ_tilde=μ°+RT ln a+zFψ, with absolute temperature T, gas constant R, Faraday constant F and electric potential ψ. R has units J/(mol K), F has units C/mol and a is dimensionless, so each term has units J/mol. One volt times one coulomb is one joule.

Define positive transfer from side A to side B. In the same standard state, the change per mole transferred is Δμ_tilde=RT ln(a_B/a_A)+zF(ψ_B−ψ_A). The two terms can reinforce or oppose one another. A positive value makes this transfer uphill under the declared reservoir conditions; reversing the transfer changes its sign.

At equilibrium for that permeant ion, Δμ_tilde=0. Therefore Δψ=−RT/(zF) ln(a_B/a_A). This is a single-species equilibrium condition. A general membrane potential with several mobile ions, pumps or imposed currents need not equal every ion's separate equilibrium potential. Conservation, electroneutrality/charge storage, permeability and kinetics provide additional constraints.

## A sign-checked example

Use T=300 K, R=8.314 J/(mol K), F=96485 C/mol and z=+1. Let the ideal activity ratio a_B/a_A=0.1. The chemical contribution is RT ln0.1≈−5743.1077 J/mol, favoring A-to-B transfer. A positive B-minus-A voltage opposes that cation transfer. The equilibrium voltage is about +0.059523 V.

If B is instead 0.020 V above A, the electrical contribution is +1929.7 J/mol, leaving a negative total around −3813.41 J/mol. Reversing the potential difference would reinforce the chemical term. Replacing a cation by an anion changes the electrical sign, so memorizing a voltage formula without its transfer direction is unsafe even for a paper calculation.

## Couple reactions using actual Gibbs-energy changes

Suppose an auxiliary process releases a declared ΔG_aux per mole of coupling events. If one event drives ν moles of an ion uphill with cost Δμ_tilde per mole, the coupled change is ΔG_total=ΔG_aux+νΔμ_tilde. A negative total is thermodynamically favorable under those stated conditions. It does not prove a mechanism exists or give its speed, efficiency or coupling fidelity.

Use a separate synthetic uphill transfer with activity ratio two and Δψ=+0.020 V for a monovalent cation at 300 K. Its cost is RT ln2+F×0.020≈3658.5477 J/mol. If ΔG_aux=−14000 J/mol of coupling events, three ions cost about 10975.64 J and leave negative total energy; four cost about 14634.19 J and leave positive total energy. Thus three is the largest integer stoichiometry with a strictly favorable ledger here.

The auxiliary value is an actual declared reaction Gibbs energy for this model, not an unstated standard biochemical constant. Reservoir composition, pH, voltage and product/reactant activities can change the actual driving force. At equality the net thermodynamic driving force vanishes; a strictly negative energy budget is different from a reversible limiting equality.

## From potential gradients to a flux model

For an isothermal ideal dilute ion, a local mobility model gives j_diff+elec=−(Dc/RT)∂μ_tilde/∂x. Substituting μ_tilde and using a proportional to c yields

j=−D[∂c/∂x+(zF/RT)c∂ψ/∂x]+v c.

The first term is diffusion, the second electrical migration and the third transport with a declared fluid velocity. The model assumes a compatible dilute mobility/diffusivity relation and specified local fields; it does not by itself determine ψ or a self-consistent multi-ion composition.

For D=10^−9 m²/s, c=2 mol/m³, ∂c/∂x=−100 mol/m⁴, ∂ψ/∂x=50 V/m, z=1 and v=0 at 300 K, diffusion contributes +10^−7 mol/(m² s). Electrical migration contributes approximately −3.86837×10^−6 mol/(m² s), so the total is negative. The ion can move against its concentration-driven direction because the electrical contribution dominates. Check units and sign of each contribution before adding them.

At zero flux with v=0, integrating the ideal equation over a specified potential difference recovers the equilibrium activity-ratio relation. This limiting check links transport to thermodynamics without claiming that every transient profile is at equilibrium.

## Osmotic pressure requires a solvent/solute model

For a dilute ideal solution of independent solute particles, osmotic pressure relative to the pure-solvent reference is Π≈RT c_total with concentration in mol/m³. A concentration of one mM equals one mol/m³. Count dissolved particles according to the declared dissociation model; summing species concentrations and then multiplying by a second dissociation factor would double-count.

A stipulated linear solvent-flux relation is J_v=L_p(ΔP−σΔΠ), with both differences defined as A minus B. Positive flux is A to B. L_p has units m/(Pa s), σ is a declared reflection coefficient, and ΔΠ is Π_A−Π_B. With ΔP=5000 Pa, ΔΠ=3000 Pa, σ=1 and L_p=2×10^−12 m/(Pa s), J_v=4×10^−9 m/s. The pressure difference exceeds the opposing osmotic contribution on this sign convention.

If solute crosses freely or concentrations evolve, the reflection/transport model and reservoir balances matter. The relation is an assumed near-linear constitutive law, not a general validation of membrane performance. A pure thermodynamic equilibrium condition contains no L_p and cannot determine an equilibration time.

## Rehearsal and reporting

For a new rehearsal, use an ideal monovalent cation at 300 K with a_B/a_A=2 and Δψ=−0.010 V. Calculate the chemical, electrical and total contributions independently. Determine the equilibrium Δψ and compare the sign with the supplied voltage. With a fictional energy supply −9000 J/mol of coupling events, determine the largest strictly favorable integer stoichiometry if the total transfer cost is positive.

For a separate solvent calculation, use an ideal particle-concentration difference 2 mol/m³, ΔP=8000 Pa, σ=1 and L_p=10^−12 m/(Pa s). Compute ΔΠ and signed J_v. Label every direction, concentration convention and constitutive assumption. Explain which result concerns equilibrium, which concerns instantaneous flux and which would require a dynamic reservoir model.

The [MIT OCW 20.110J Fall 2005 calendar](https://ocw.mit.edu/courses/20-110j-thermodynamics-of-biomolecular-systems-fall-2005/pages/calendar/) supplies a link-only electrolyte/osmotic scope comparator; [20.330J Spring 2007 syllabus](https://ocw.mit.edu/courses/20-330j-fields-forces-and-flows-in-biological-systems-spring-2007/pages/syllabus/) includes ion-transport foundations. All explanations and values are original CC BY 4.0 material. No comparator exercise or data was imported; qualified review and workload measurement remain open.
