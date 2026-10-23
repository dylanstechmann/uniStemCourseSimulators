# Ligand-exchange kinetics and mechanism discrimination

A saturating rate curve can arise from more than one microscopic scheme. To distinguish candidate mechanisms, derive their observation equations, identify the approximations and choose a comparison on which their predictions differ. This reading extends [mechanism inference](10-rate-laws-and-mechanism-inference.md), [reversible/sequential kinetics](11-reversible-and-sequential-kinetics.md) and the coordination strand with two original reduced models. Species are fictional and the discussion concerns mathematical evidence, not an experimental procedure.

## A dissociation-and-capture candidate

Let ML release ligand L to form a reactive intermediate M with first-order coefficient kd. The intermediate can recombine with free L at rate kr[M][L] or be captured by free entering ligand Y at rate kc[M][Y], forming MY. Treat free L and Y as independently held constant over a short low-conversion observation window. In a steady-intermediate approximation,

$$0\approx k_d[ML]-(k_r[L]+k_c[Y])[M].$$

Then the product rate is kc[Y][M]. If the intermediate pool is small so that [ML] approximately equals the unconverted metal total CT, the reduced observed rate per CT is

$$k_{obs}\approx \frac{k_dk_c[Y]}{k_r[L]+k_c[Y]}.$$

This result follows from the selected scheme plus the reservoir, time-scale and small-intermediate assumptions. It is not a universally valid rate law for every ligand substitution. Immediately after a different initial preparation, before intermediate relaxation, the steady-state expression can fail. At substantial conversion, product reversal, ligand release and changing pools may also matter.

The relaxation scale of the intermediate is approximately 1/(kr[L]+kc[Y]), and its predicted ratio to ML is kd/(kr[L]+kc[Y]). Compare those scales with the slower conversion and report the ratio before invoking the approximation. A small derivative and a small concentration are related assumptions here but are not identical mathematical statements.

## A distinct association candidate

Now let ML bind Y rapidly and reversibly to form I, followed by slow conversion of I to MY plus L. Let KA=[I]/([ML][Y]) for that fast pre-equilibrium and kturn the conversion coefficient. Here the unconverted metal pool is CT=[ML]+[I], not just [ML]. Solving the partition gives [I]=CT KA[Y]/(1+KA[Y]), and hence

$$k_{obs}\approx k_{turn}\frac{K_A[Y]}{1+K_A[Y]}.$$

Free Y is again held constant and the rapid pre-equilibrium needs its own time-scale justification. A substantial intermediate fraction is permitted in this derivation because it is included in CT. Neglecting it while using this saturation expression would mix inconsistent assumptions. The thermodynamic binding parameter KA does not alone specify the speed of association and dissociation.

## Two schemes can give the same reduced curve

For a worked fictional dissociation model, stipulate kd=0.0004 s^−1, kr[L]=0.06 s^−1 and kc=100 L mol^−1 s^−1. Algebra gives the same reduced hyperbola as the association model with kturn=0.0004 s^−1 and KA=100/0.06 L/mol. At free Y=0.0006 mol/L both predict kobs=0.0002 s^−1. At twice that Y the rate is about 0.00026667 s^−1, and the high-Y plateau is 0.0004 s^−1.

The original [ligand-exchange-reference.csv](../assignments/ligand-exchange-reference.csv) provides four reduced-model values rounded to eight decimal places. They are analytic teaching outputs, not independent experimental replicates and not exact integration of both microscopic schemes. A perfect fit to this table therefore cannot establish a unique mechanism. In the dissociation approximation, even at Y=0 the intermediate/ML ratio is at most 0.0004/0.06, about 0.00667; it is small but not identically zero. A full kinetic model can differ slightly from the reduced observation equation.

## Find a comparison that separates predictions

At fixed Y=0.0006 mol/L, double free L in the dissociation model so kr[L] rises from 0.06 to 0.12 s^−1. Its reduced kobs becomes 0.0004×0.06/(0.12+0.06), about 0.00013333 s^−1. In the stipulated simple association candidate, free L is absent from the reduced rate law, so that same change leaves kobs unchanged. This is a discriminating prediction under the declared schemes, not proof that all real associative paths ignore leaving ligand.

A proposed study should name an endpoint, a controlled comparison and the contrasting possible results. Measuring only more points on the already shared Y hyperbola does not resolve a structural ambiguity. Effects of L on activity, speciation or additional reactions could invalidate the simple comparison, so a mechanistic conclusion would need independent checks on those assumptions. Distinguish identification of a reduced parameter combination from identification of each microscopic coefficient.

## Low and high concentration limits

When kc[Y] is much smaller than kr[L], the dissociation model gives kobs approximately kd kc[Y]/(kr[L]), linear in Y and inverse in L. When capture dominates, kobs approaches kd. The association model is likewise linear at KA[Y] much smaller than one and approaches kturn at high Y. A plateau alone therefore does not reveal whether an intermediate formed by dissociation or association.

The half-plateau occurs at Y=kr[L]/kc in the first model and Y=1/KA in the second. Their matching numerical values are another expression of the same reduced-curve ambiguity. Report both the algebra and the boundary conditions. A formation constant from an equilibrium measurement, a relaxation time and a conversion rate are different data types and should not be freely substituted for one another.

## Verify the reduction

For a computational extension, integrate the full intermediate equations with reservoirs held fixed, compare early transient and low-conversion windows with the reduced expression, and track metal conservation. Then relax the reservoir assumptions and state how the equations change. The [mechanism-evidence assignment](../assignments/coursework-02-mechanism-evidence.md) supplies a new parameter set and asks for this approximation/identifiability audit.

The [MIT OCW 5.111SC Fall 2014 syllabus](https://ocw.mit.edu/courses/5-111sc-principles-of-chemical-science-fall-2014/pages/syllabus/) and [5.112 Fall 2005 calendar](https://ocw.mit.edu/courses/5-112-principles-of-chemical-science-fall-2005/pages/calendar/) are link-only scope references for kinetics, coordination and ligand substitution. The schemes, derivations, parameter sets and table are original and developed with substantial AI assistance; no source problem, prose or data was imported. Real mechanism assignment, full coordination kinetics, qualified review and measured workload remain outside this selected model. The package is partial and unreviewed.
