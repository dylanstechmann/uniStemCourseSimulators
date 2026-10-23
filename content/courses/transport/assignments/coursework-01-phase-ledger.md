# Assignment 1: a phase and free-energy ledger

**Open, ungraded paper/computation practice with substantial AI-assisted authoring.** Proposed placement: week 5. All mixtures and coefficients are invented. Save your derivation, calculations and report locally or keep notes in the lesson; the browser checks selected fields, not the written argument or an implementation. No real material or phase behavior is identified.

## Part A: a conserved partitioning problem

A dilute solute redistributes between two already-existing phases. Their fixed volumes are V_α=0.004 m³ and V_β=0.001 m³, with total solute amount 0.012 mol. At the common supplied temperature, the equilibrium activity ratio is K_a=4. The two phases use the same concentration standard and declared constant activity coefficients γ_α=0.8 and γ_β=1.6.

Derive the concentration ratio from equality of chemical potentials, then use the conserved total to solve both concentrations and solute amounts. Check the activity ratio and material balance independently. Explain why the numerical concentration ratio differs from K_a and why a higher concentration need not imply a higher chemical potential at equilibrium.

Repeat with ideal coefficients while keeping K_a and total amounts fixed. Determine how each concentration changes. Do not change the total amount or phase volumes while claiming to test only the effect of activity corrections. The stipulated coefficients are a local teaching model, not measured properties or a general thermodynamically consistent activity model for every composition.

## Part B: distinguish three different phase calculations

For a separate binary bulk mixture, assume coexistence compositions x_α=0.15 and x_β=0.75 have been supplied by an independent equilibrium calculation. With overall composition z=0.30, compute the amount fraction of each phase using the lever balance. Check that the reconstructed overall composition equals z.

Explain why this calculation does not establish the coexistence compositions. Contrast it with Part A, where phases already existed and one dilute solute partitioned between their fixed volumes. Give the additional information needed to convert molar phase fractions to volume fractions. Neither raw concentration ratios nor the lever balance alone provide phase densities.

## Part C: a declared regular-solution model

Use g(x)=x ln x+(1−x)ln(1−x)+3x(1−x). Derive its first and second derivatives. Calculate the spinodal compositions from g″=0 and determine the curvature at x=0.5. Then solve for symmetric coexistence compositions using g′(x)=0 with one root restricted to 0<x<0.2 and the other 1−x. The root at 0.5 is not the desired coexistence pair.

Explain the common-tangent condition. For symmetric coexistence, the common tangent is horizontal because the two free-energy values are equal by symmetry. Compare the homogeneous g(0.5) with the free energy of equal amounts of the two coexistence phases. Distinguish local instability, metastability and global coexistence. The spinodal roots are not the binodal/coexistence roots.

Use a bracketed root algorithm or a carefully documented hand iteration. Report the bracket, residual, convergence criterion and domain. Numerical residuals can verify a candidate for the stipulated equation, but they do not validate the regular-solution model as a description of a real mixture.

## Part D: connect to energy and entropy

At 300 K with R=8.314 J/(mol K), calculate ideal mixing Gibbs energy and entropy for one mole with x=0.25. Keep the ideal calculation separate from the χ=3 nonideal model. State which terms would be needed to separate the nonideal mixing Gibbs energy into enthalpy and entropy if χ depended on temperature.

Discuss why a favorable mixing or partitioning Gibbs-energy change does not supply the transport time. A kinetic model would need geometry, mobilities/diffusivities, interfacial transfer and evolving balances. An equilibrium algebraic solution does not determine those parameters.

## A separate worked balance

For K_p=2, V_α=0.002 m³, V_β=0.002 m³ and n_total=0.006 mol, c_α=0.006/(0.002+2×0.002)=1 mol/m³ and c_β=2 mol/m³. The solute amounts are 0.002 and 0.004 mol. This separate example demonstrates ratio plus conservation; it is not a solution to the main problem's coefficient and volume choices.

## Self-review and report

For Part A, the activity correction makes the concentration ratio two. The supplied amounts then give c_α=2 and c_β=4 mol/m³, with amounts 0.008 and 0.004 mol. For Part B, the α amount fraction is 0.75 and the β fraction 0.25. Derive the phase-stability results independently rather than substituting these partitioning values into a different model.

A report should label standard states, temperature, phase assumptions, conserved totals, composition bases and all units. Include residual/conservation checks, a free-energy graph with a text description and a clear account of what is assumed rather than measured. Disclose spreadsheets, code, references and AI assistance.

This original packet is CC BY 4.0. [MIT OCW 20.110J Fall 2005 calendar](https://ocw.mit.edu/courses/20-110j-thermodynamics-of-biomolecular-systems-fall-2005/pages/calendar/) is a link-only scope comparator for phase/nonideal thermodynamics. No external exercise, figure or dataset was reproduced. Qualified review and measured workload remain open.
