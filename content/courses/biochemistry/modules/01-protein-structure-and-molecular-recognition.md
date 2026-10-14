# Protein structure and molecular recognition

Proteins are chains whose sequence constrains a changing three-dimensional ensemble. Their shape and dynamics arise from interactions among the backbone, side chains, solvent, and sometimes other protein subunits or ligands. A binding calculation is easiest to interpret when structure, equilibrium, and kinetics are kept distinct.

## Structural levels and stabilizing interactions

The **primary structure** is the amino-acid sequence. Local backbone geometry produces recurring **secondary structures**, including alpha helices and beta sheets, whose hydrogen bonds form between backbone groups. The **tertiary structure** describes the overall arrangement of one chain; **quaternary structure** describes an assembly of multiple chains. These levels are useful descriptions, not separate forces that act independently.

Folding reflects the free-energy balance between protein-protein, protein-solvent, and solvent-solvent interactions. Hydrophobic side chains are often more favorable in a buried environment than exposed to water; hydrogen bonds, electrostatic interactions, van der Waals packing, and covalent disulfide bonds can also contribute. No single interaction explains every fold. A buried polar group, an unsatisfied charge, or a packing defect can offset favorable contacts.

The native state is not necessarily one rigid shape. Proteins occupy an ensemble of conformations whose populations depend on conditions such as temperature, pH, ionic strength, solvent, and binding partners. A mutation can alter folding stability, flexibility, or the fraction of protein in an active conformation without changing a ligand-contact atom directly. A structure is therefore a model of states and interactions under specified conditions, not a complete description of all dynamics.

## Binding as an equilibrium

For a simple reversible 1:1 interaction, $P+L\rightleftharpoons PL$, the dissociation constant is

$$K_d=\frac{[P][L]}{[PL]}.$$

If free ligand concentration is known and ligand depletion is negligible, fractional occupancy is

$$\theta=\frac{[PL]}{[P]+[PL]}=\frac{[L]}{K_d+[L]}.$$

At $[L]=K_d$, occupancy is one half. At concentrations well below $K_d$, occupancy is low; well above $K_d$, it approaches one. **Worked example:** with $K_d=4$ µM and free $[L]=12$ µM, $\theta=12/(4+12)=0.75$, or 75%. This result assumes equilibrium, one class of independent sites, and that free ligand is close to the stated concentration; if binding depletes ligand, a mass-balance calculation is needed.

A smaller $K_d$ means tighter equilibrium binding in this model. It does not say how quickly the complex forms or dissociates. For the elementary two-state mechanism, $K_d=k_{off}/k_{on}$: a small value can arise from a faster association rate, a slower dissociation rate, or both. Two interactions with the same $K_d$ can have different time courses.

## Affinity, specificity, and cooperativity

**Affinity** describes the equilibrium strength of binding for a particular pair. **Specificity** describes discrimination among possible ligands; it requires comparing binding to more than one ligand and depends on the tested alternatives and conditions. **Cooperativity** describes how occupancy at one site changes binding at another. These are separate properties: a protein can bind one ligand tightly but distinguish poorly among similar ligands, or bind cooperatively without having the tightest midpoint.

For a cooperative response, an empirical Hill form is $\theta=[L]^{n_H}/(K_{0.5}^{n_H}+[L]^{n_H})$. Here $K_{0.5}$ is the concentration giving half response in this model, and $n_H$ describes response steepness. A Hill coefficient above one is evidence of a steeper cooperative response over a concentration range; it is not a literal count of binding sites or proof of a particular molecular mechanism.

For the practice comparison, Protein X has $K_d=1$ µM and $n_H=1$, while Protein Y has apparent $K_{0.5}=10$ µM and $n_H=3$. At 5 µM ligand, the simple X model gives occupancy $5/(1+5)=0.833$. The empirical Y curve gives $5^3/(10^3+5^3)=0.111$. This example illustrates why a larger Hill coefficient alone does not mean higher affinity: compare the midpoint and the response shape separately.

## Conformational selection and induced fit

In conformational selection, a ligand binds a conformation that the unbound protein already visits, shifting the ensemble toward that state. In induced fit, initial binding is followed by a structural adjustment that improves complementarity. Both descriptions can contribute to real binding pathways, and an equilibrium occupancy measurement alone generally cannot decide which sequence of events dominates. Structural changes can also alter activity after binding, so affinity does not by itself determine catalytic rate or function.

## What a structure can and cannot say

A structure is an experimentally constrained model of a sample prepared under stated conditions. A ligand-free and a ligand-bound structure can reveal different endpoint conformations, but the pair alone does not show whether the ligand selected a pre-existing state, caused a later adjustment, or participated in both parts of the pathway. Crystal packing, temperature, pH, ligand occupancy, resolution and model refinement can affect what is visible. Solution methods such as NMR can detect conformations and exchange processes that a single crystal model does not show, although each method observes a limited range of time scales and populations.

The glucose/galactose-binding protein of *E. coli* is a useful case. Its apo and ligand-bound structures show different domain arrangements. Unione and colleagues combined paramagnetic NMR with molecular-dynamics simulations and reported open-like and closed-like apo populations of about 68% and 32%, respectively; their simulations estimated exchange near 25 ns. In that specific system, the ligand shifted the ensemble toward the closed state, consistent with a substantial conformational-selection contribution. These values describe one protein under one study's conditions; they are not universal fractions or rates for ligand binding.

This reading introduces affinity, specificity and cooperativity to interpret molecular recognition. The week-4 [binding-equilibria lesson](07-binding-equilibria-and-cooperativity.md) is the main quantitative treatment of ligand depletion, Hill-response comparisons and binding measurements.

**Synthetic ensemble check.** Suppose an apo sample has 30% closed molecules and a matched ligand condition has 90% closed molecules. The closed-to-open odds change from $0.30/0.70$ to $0.90/0.10$, a factor of $21$. This calculation describes an ensemble shift. It does not give a $K_d$ because the free ligand concentration, binding stoichiometry and full state-binding model have not been supplied.

To test a binding claim, match the method to the question. A concentration-dependent equilibrium titration estimates affinity and stoichiometry under its model; it does not provide association and dissociation rates. A time-resolved or relaxation measurement can help resolve exchange and binding steps. A mutation can test whether a residue or hinge contributes to the observed behavior, but the comparison needs controls showing that the variant still folds and remains in the relevant assembly. Koshland's induced-fit proposal and later ensemble measurements motivate useful models; no one structure or equilibrium readout settles the mechanism by itself.

## Common mistakes

- Treating a protein as a single rigid structure independent of its environment.
- Calling every favorable contact a hydrogen bond or assuming one force alone determines folding.
- Using total ligand concentration in the simple occupancy equation when ligand depletion is substantial.
- Interpreting low $K_d$ as fast association or high catalytic efficiency.
- Equating specificity with affinity, or cooperativity with a number of sites.
- Claiming that an equilibrium binding curve alone distinguishes conformational selection from induced fit.
- Reading a crystal-model occupancy or a pair of structures as a direct solution-state population, rate, or dissociation constant.

## Check your model

Before using an occupancy equation, identify the binding stoichiometry, equilibrium assumption, free-ligand concentration, and whether sites are independent. Then report $K_d$ or $K_{0.5}$ with units and distinguish the midpoint from response steepness. The public practice item gives 0.75 occupancy for 12 µM free ligand and $K_d=4$ µM. The second item separates affinity, specificity, and cooperativity; its answer key is unchanged. These are formative biochemical models, not measurements of a real molecule.

## Selected primary research connections

- Koshland, D. E. (1958). [Application of a Theory of Enzyme Specificity to Protein Synthesis](https://doi.org/10.1073/pnas.44.2.98). *Proceedings of the National Academy of Sciences*, 44, 98–104.
- Unione, L. et al. (2016). [Unraveling the Conformational Landscape of Ligand Binding to Glucose/Galactose-Binding Protein by Paramagnetic NMR and MD Simulations](https://doi.org/10.1021/acschembio.6b00148). *ACS Chemical Biology*, 11, 2149–2157.

These are link-only references; no article text, figure, table, or data are reproduced here.
