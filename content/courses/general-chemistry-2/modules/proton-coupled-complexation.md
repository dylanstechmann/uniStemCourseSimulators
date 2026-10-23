# Proton-coupled complexation with finite ligand pools

A binding constant uses the free binding species, not the analytical total ligand. If that species can also be protonated, binding and acid dissociation compete for the same finite pool. If pH is not externally fixed, electroneutrality couples those equilibria to the hydrogen concentration. This reading develops the complete selected model rather than inserting a pH-dependent constant without checking its boundary conditions. Review [acid/charge balance](09-coupled-acid-speciation-and-charge-balance.md) and [ligand balance](13-ligand-balance-and-coordination-models.md). All species labels, constants and totals are fictional teaching values.

## Species and conventions first

Use a neutral acid HL, its singly negative binding form L−, free metal M2+ and complex ML+. The reactions are HL ⇌ H+ + L− and M2+ + L− ⇌ ML+. Both conserve charge. Let h=[H+], l=[L−], m=[M2+] and x=[ML+]. Adopt an ideal concentration convention with Ka=h l/[HL], Kf=x/(m l) and Kw,c=h[OH−]. Here Ka has units mol/L, Kf has units L/mol and Kw,c has units (mol/L)². These concentration parameters are declared model inputs; real thermodynamic equilibrium constants use dimensionless activities.

Metal and ligand totals are MT=m+x and LT=[HL]+l+x. A ligand entity appears once in each of its chemical forms. Metal charge and ligand charge do not replace those amount counts. Let S be the concentration of fixed spectator-anion charge minus fixed spectator-cation charge, in equivalents per liter. Electroneutrality is

$$h+2m+x-l-K_{w,c}/h-S=0.$$

The factors two and one count free-metal and complex charge. The spectator difference can encode a declared background inventory but cannot be chosen independently after all other closed-solution conditions are fixed. No preparation or chemical-handling procedure is implied by these abstract inventories.

## Reduce the binding problem at a specified h

Acid dissociation implies l/[HL]=Ka/h. Among unbound ligand, the binding-form fraction is alpha=Ka/(Ka+h). Therefore l=alpha(LT−x), [HL]=(1−alpha)(LT−x), and m=MT−x. The single binding equation becomes

$$x=K_f\alpha(M_T-x)(L_T-x).$$

The conditional constant Kf alpha applies to the unbound ligand pool under the supplied h. It does not turn analytical LT into free l. Retain only roots satisfying 0≤x≤min(MT,LT), reconstruct all species, and check both totals and the original equilibrium quotient. An algebraic second root can violate the amount bounds. A numerical root search on the bounded x interval avoids accepting such a root and can reduce subtractive cancellation from a quadratic formula.

At fixed positive h and constants, the left-minus-right residual increases from a nonpositive value at x=0 to a nonnegative value at the upper bound; its derivative is positive in the admissible interval. Thus the selected one-complex model has one admissible root, apart from trivial zero-total boundary cases. That conclusion concerns this declared model, not every real metal/ligand system.

## Worked species and charge ledger

Stipulate h=0.000010 mol/L, Ka=0.000005 mol/L, MT=0.0010 mol/L, LT=0.0015 mol/L, Kf=5000 L/mol and Kw,c=10^−14 (mol/L)². Alpha is one third. The admissible complex concentration is x=0.0006 mol/L. This leaves m=0.0004, l=0.0003 and [HL]=0.0006 mol/L. The ligand total is 0.0006+0.0003+0.0006=0.0015, and x/(m l)=5000.

Hydroxide is 10^−9 mol/L. The compatible spectator difference is S=h+2m+x−l−[OH−]=1.109999×10^−3 equivalents/L. A claim that this same closed inventory also has an arbitrary S=0 would violate charge balance. If h is imposed by an external reservoir, the reservoir can provide charge/protons; if S is fixed in a closed calculation, h must be solved. Those are different boundary conditions.

## Solve the closed problem in positive variables

When MT, LT, S and constants are specified, evaluate alpha at a trial positive h, solve the bounded binding equation, then evaluate the charge residual. Search for its zero in log(h) or a carefully justified positive bracket. Reconstruct every species at the final h and test mass, charge and both equilibrium relations independently. A root-finder returning a small step is not a substitute for those residual checks. Report concentration scales and residual tolerances rather than adding unlike dimensional residuals without normalization.

For a distinct rehearsal, use h=0.000020 mol/L, Ka=0.000010 mol/L, MT=0.0015 mol/L, LT=0.0021 mol/L and Kf=3750 L/mol. The corresponding admissible state is x=0.0009, m=0.0006, l=0.0004 and [HL]=0.0008 mol/L. Check alpha, the metal bound fraction and the required spectator difference yourself. The tiny water contribution remains part of the declared charge equation even when it is numerically small.

## Approximation and interpretation checks

Treating all unbound ligand as L− assumes alpha near one. Treating LT as free ligand additionally assumes negligible binding depletion. Either approximation can fail independently. A large Kf does not guarantee full binding when protonation or finite ligand supply limits availability. Changing pH can change the conditional constant without changing the stipulated intrinsic Kf.

This model omits other complexes, metal hydrolysis, precipitation, activity corrections and additional acid states. A mathematically consistent root does not show those species are absent in a real solution. The [closed-solution assignment](../assignments/coursework-01-closed-solution-ledger.md) uses different totals and asks for residual, limiting-case and boundary-condition comparisons.

The [MIT OCW 5.111SC Fall 2014 syllabus](https://ocw.mit.edu/courses/5-111sc-principles-of-chemical-science-fall-2014/pages/syllabus/) is the shared local Chemistry I/II scope comparator. This original AI-assisted explanation and all inputs import no source exercise, prose or dataset. The local pair divides one comparator and establishes no two-course equivalence. Qualified chemical review and measured workload remain open; the package is partial and unreviewed.
