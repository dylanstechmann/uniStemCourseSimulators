# Assignment 1: a closed-solution equilibrium ledger

Build a reproducible speciation report using [proton-coupled complexation](../modules/proton-coupled-complexation.md), [acid/charge balances](../modules/09-coupled-acid-speciation-and-charge-balance.md) and [free-energy direction](../modules/08-free-energy-and-equilibrium.md). Retain derivations, solver or calculation tables, residuals and interpretation locally. Browser practice checks selected quantities, not your complete solver, written argument or a real solution. All species and constants are fictional teaching models.

## The declared closed system

Use the model HL ⇌ H+ + L− and M2+ + L− ⇌ ML+. The metal total is MT=0.0012 mol/L and ligand total LT=0.0018 mol/L. Stipulate Ka=0.000004 mol/L, Kf=2500 L/mol and Kw,c=10^−14 (mol/L)² under the ideal concentration convention. The fixed spectator difference S, defined as anion minus cation background charge, is 0.00080099 equivalents/L. No external pH or free-ligand reservoir is imposed.

List all modeled species and their charges. Derive metal and ligand conservation, acid dissociation, complex formation, water equilibrium and electroneutrality. State how pH is interpreted in this ideal convention: minus the base-ten logarithm of h divided by the standard concentration one mol/L. Distinguish the dimensional concentration parameter Ka from a fully thermodynamic activity constant.

## Reduce and solve without overconstraining

For a trial positive h, derive alpha and the bounded complex equation. Prove or justify uniqueness of its admissible root in 0≤x≤min(MT,LT). Reconstruct free metal, free binding ligand, protonated ligand and hydroxide. Then form the charge residual using the supplied S. Solve for h in a declared positive bracket, preferably working in log(h) or another method that prevents negative concentrations.

Keep full intermediate precision. Report all species, pH, the metal bound fraction, both analytical-total residuals, charge residual and original equilibrium-quotient residuals. State units and normalization for each residual. Do not add a concentration residual to a dimensionless logarithmic error without defining a scale. Retain enough digits to show conservation before formatting a final three-significant-figure table.

Verify the result with a second approach: solve the original equations in another set of variables, substitute a candidate state directly into every relation, or independently bracket the reduced charge equation. Two calls to the same formula with different printed precision are not independent checks. A solver's convergence flag alone does not guarantee an admissible chemical state.

## Compare approximations and boundaries

First assume the total ligand equals free binding ligand. Quantify the resulting error and identify which omitted pools cause it. Then make the weaker approximation of negligible binding depletion while retaining protonation. Compare both with the complete selected model and state whether a large Kf by itself justifies either simplification.

Now change the mathematical boundary condition: impose the solved h externally instead of specifying S. Calculate the S required for the same composition and explain what a reservoir changes about the closed charge/proton inventory. Conversely, keep the original S and perturb Ka or Kf; solve h again rather than silently holding pH fixed. A change in conditional binding constant can arise from protonation even when the intrinsic Kf is unchanged.

Test the zero-metal limit, a vanishing binding constant and a ligand-deficient case. Explain how the maximum possible complex concentration follows from totals regardless of affinity. If you include an additional precipitate or hydrolyzed species, rewrite balances and equilibria explicitly instead of calling the old positive root a complete real-solution prediction. No such additional equilibrium data are supplied by this problem.

Document the numerical tolerance separately from displayed digits. Rounded species need not satisfy the residual equations as precisely as their unrounded values.

## Interpretation and self-review

The selected solution has h=0.000001 mol/L and alpha=0.8. Complex concentration is 0.0008 mol/L, free metal 0.0004, free L− 0.0008 and HL 0.0002 mol/L. Metal bound fraction is two thirds, and ideal-model pH is six. Hydroxide is 10^−8 mol/L. Substitution gives S=0.000001+0.0008+0.0008−0.0008−0.00000001=0.00080099 equivalents/L.

Reconstruct Kf as 0.0008/(0.0004×0.0008)=2500 L/mol and Ka as 0.000001×0.0008/0.0002=0.000004 mol/L. The agreement of mass, charge and equilibria is the reference; a single matching bound fraction is insufficient. Explain what unmodeled activities, additional complexes or precipitation could change before interpreting an actual sample. No experimental observations or preparation procedure are provided here.

A complete report contains explicit species/charge inventory, an admissible solved state, independent checks, approximation comparisons, boundary-condition reasoning and limiting cases. This original assignment was developed with substantial AI assistance. [MIT OCW 5.111SC Fall 2014](https://ocw.mit.edu/courses/5-111sc-principles-of-chemical-science-fall-2014/pages/syllabus/) is the shared local Chemistry I/II scope comparator; no source problem, prose or dataset was imported. The course remains partial and unreviewed, and actual workload and qualified chemical review remain open.
