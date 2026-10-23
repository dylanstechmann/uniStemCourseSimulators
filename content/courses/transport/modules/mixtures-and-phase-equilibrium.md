# Mixtures and phase equilibrium: activities, partitioning and stability

**Status:** original ungraded instruction developed with substantial AI assistance. The mixtures, energies and coefficients are synthetic. This reading extends the ideal-reaction foundation into phase partitioning and a declared nonideal mixing model. A thermodynamic condition specifies possible equilibrium; it does not supply a transport rate.

## Chemical potential must name its standard state

For a species i, write μ_i=μ_i°+RT ln a_i at fixed temperature and pressure. Activity a_i is dimensionless. In a chosen liquid-mixture convention one can write a_i=γ_i x_i, where x_i is mole fraction and γ_i is an activity coefficient. For an ideal solution in that convention γ_i=1. A concentration-based standard state uses a different expression and may assign a different numerical standard chemical potential.

Do not substitute a dimensional concentration directly into a logarithm. Likewise, do not set activity equal to mole fraction while also including an activity correction twice. The standard-state convention and γ model are part of the problem. Changing a convention consistently changes μ° and the activity representation while preserving physical chemical potentials.

For a binary ideal mixture of total amount n, the mixing Gibbs energy is ΔG_mix=nRT[x ln x+(1−x)ln(1−x)] relative to the separated ideal reference. The entropy of mixing is −nR[x ln x+(1−x)ln(1−x)] at the specified isothermal ideal conditions. At x=0.5 and n=1 mol, T=300 K with R=8.314 J/(mol K), ΔG_mix=−RT ln2≈−1728.8477 J and ΔS_mix=R ln2≈5.7628257 J/K. Negative mixing Gibbs energy here favors mixing; it does not establish a mixing time.

## Equal chemical potentials connect phases

Suppose one dilute solute partitions between phases α and β at common temperature and pressure. Equilibrium requires μ_α=μ_β. Thus

μ_β°−μ_α°+RT ln(a_β/a_α)=0,

so a_β/a_α=exp[−(μ_β°−μ_α°)/(RT)]. A concentration ratio equals this activity ratio only under the stated compatible activity conventions and corrections. If γ values differ, those factors must remain in the balance.

Define a synthetic ideal dilute distribution coefficient K_p=c_β/c_α=4. Two well-mixed phases have volumes V_α=0.003 m³ and V_β=0.001 m³, and contain a conserved total solute amount of 0.007 mol. The mass balance is n_total=c_α V_α+c_β V_β=c_α(V_α+K_p V_β). Hence c_α=1 mol/m³ and c_β=4 mol/m³. Their solute amounts are 0.003 and 0.004 mol, which sum to the supplied total.

The higher concentration phase does not necessarily have the higher chemical potential at equilibrium: its standard-state term can differ. This is why “diffusion always makes concentrations equal” fails across dissimilar phases. Equilibrium equalizes the relevant chemical potential, with other constraints included, rather than every raw concentration.

## Distinguish partitioning from phase fractions

In the preceding example the phases already exist with supplied volumes and a dilute solute redistributes between them. The problem does not solve whether the bulk material separates into phases. That is a different question involving the total Gibbs energy as a function of composition and the constraints on overall composition.

For two coexisting binary phases with compositions x_α and x_β and overall composition z, the lever balance is z=f_α x_α+(1−f_α)x_β. If x_α≠x_β, f_α=(x_β−z)/(x_β−x_α). For x_α=0.2, x_β=0.8 and z=0.35, f_α=0.75. These are amount fractions under a consistent molar basis, not automatically volume fractions. This balance requires that the coexistence compositions be independently established; it does not derive them.

## A nonideal free-energy model introduces local instability

Consider the stipulated dimensionless mixing free energy

g(x)=x ln x+(1−x)ln(1−x)+χx(1−x), 0<x<1.

The first two terms describe ideal mixing entropy; the last is a declared symmetric interaction model. Treat χ as a fixed dimensionless parameter for this exercise. Differentiating gives g′=ln[x/(1−x)]+χ(1−2x) and g″=1/x+1/(1−x)−2χ. Positive curvature means local stability against an infinitesimal composition split under the model; negative curvature means a local composition fluctuation can lower the free energy.

At x=0.5, g″=4−2χ. It is positive for χ<2 and negative for χ>2. At χ=3, the curvature is −2 at the center. Solving g″=0 gives x(1−x)=1/(2χ), so the two spinodal compositions are [1±sqrt(1−2/χ)]/2 when χ>2. At χ=3 they are approximately 0.21132487 and 0.78867513.

These spinodal boundaries are not the coexistence compositions. Coexistence requires matching the component chemical potentials, equivalently a common-tangent construction for this composition free energy. Regions with positive local curvature can still be metastable relative to a sufficiently large split. Do not label every locally stable composition globally stable without comparing the appropriate total Gibbs energies.

## Nonideal coefficients change an apparent concentration ratio

If the same concentration standard is used in both phases and a_α=γ_α c_α/c°, a_β=γ_β c_β/c°, the equality condition gives c_β/c_α=K_a γ_α/γ_β, where K_a is the equilibrium activity ratio implied by the standard potentials. With K_a=4, γ_α=0.5 and γ_β=2, the concentration ratio is one, despite the activity ratio being four.

This example stipulates constant coefficients at the relevant composition. A general γ(x) model must obey thermodynamic consistency requirements and be solved with the material balances; arbitrary independent corrections need not describe a realizable mixture. The toy calculation is a test of activity bookkeeping, not a characterization of a real solvent system.

## Rehearsal and independent checks

Use K_p=3, V_α=0.002 m³, V_β=0.001 m³ and total solute 0.010 mol. Solve both concentrations and amounts, then check conservation and the ratio independently. Separately use coexistence compositions 0.1 and 0.7 with z=0.4 to determine the lever fraction. For the regular-solution model at χ=2.5, derive the spinodal roots and evaluate g″ at x=0.5.

State which task assumes pre-existing phases, which uses supplied coexistence compositions, and which diagnoses local curvature. They require different evidence. Report standard states, temperature, composition basis and activity assumptions alongside every result.

## Scope and provenance

The [MIT OCW 20.110J Fall 2005 calendar](https://ocw.mit.edu/courses/20-110j-thermodynamics-of-biomolecular-systems-fall-2005/pages/calendar/) includes phase equilibrium, regular/nonideal solutions and partitioning. This original lesson develops selected classical-mixture calculations. Full phase-diagram construction, composition-dependent activity models and experimental phase identification remain further work. No source prose, figure, problem or data was copied. Original instruction is CC BY 4.0 with disclosed AI assistance; review and measured workload remain open.
