# Multistep synthesis: work backward, audit forward and test compatibility

**Status:** original ungraded paper instruction developed with substantial AI assistance. The route rules and yields below are stipulated teaching inputs. A proposed route is an argument about bond changes and competing reactivity, not a verified preparation. No operational procedure or experimental selectivity is supplied.

## A target is a structure, not a reagent list

Retrosynthesis asks which simpler precursors could supply a target's bonds and functional groups. A disconnection is a planning operation on a drawing; it is not a reverse chemical mechanism that happens automatically in a flask. After proposing a disconnection, audit a forward transformation using actual nucleophile/electrophile roles, functional-group compatibility, atom conservation and stereochemical consequences.

Begin by marking the target bond that is new relative to the proposed starting material. Identify which carbon provides the nucleophilic component and which is the electrophile. Then inspect every other functional group exposed to that transformation. A reaction that works on an isolated ketone may fail to select that ketone in a molecule also containing a more reactive aldehyde or an acidic hydrogen.

An acid–base reaction can consume a strongly basic carbon nucleophile before its intended carbonyl addition. A free alcohol therefore requires attention in a route using such a reagent. A protecting group can sometimes address an incompatibility, but protection, survival and removal each need their own selectivity argument. Adding a protecting-group label does not establish those facts experimentally.

## An original two-carbonyl target

Use the paper starting structure 4-acetylbenzaldehyde: a para-substituted ring bearing an aldehyde and a methyl ketone. The target retains the aldehyde while the ketone carbon becomes a tertiary alcohol bonded to the ring, methyl and ethyl groups. The target new bond joins an ethyl carbon to the former ketone carbonyl carbon.

An unprotected addition-capable carbon nucleophile can also attack the aldehyde. The target requires a route that controls that competition, rather than a claim that “the reagent adds to carbonyls” is sufficient. Stipulate a selective masking operation P for the aldehyde, an ethyl-addition/protonation operation N at the exposed ketone, and an operation D that restores the aldehyde while retaining the new alcohol. These selectivities are paper assumptions to be reviewed, not experimentally demonstrated conditions.

Under those rules, the required order is P then N then D. Applying N before P leaves both carbonyls exposed; removing the mask before N recreates that incompatibility. Applying D before a mask exists does not perform the intended restoration. A forward audit can reject an order even when each named reaction is individually familiar.

## Connect the mask to a mechanism

A carbonyl can be masked as an acetal: alcohol addition gives a hemiacetal stage, and replacement of the hydroxyl-derived leaving group after appropriate activation leads to a carbon bearing two ether-like oxygen substituents. These changes are reversible under suitable conditions. The carbonyl electrophile is absent while the complete acetal mask is present.

The conceptual reason an acetal can protect during a basic/nucleophilic step is that its reactivity differs from that of the original carbonyl. Acid-promoted restoration of the carbonyl supplies a later compatibility question. Other groups, including the newly formed alcohol, might undergo unwanted reactions under deprotection conditions. The route therefore needs evidence that P is selective, the mask survives N, and D restores the desired group without damaging the rest of the structure.

A paper compatibility matrix might declare these properties to isolate sequencing logic. A real synthesis must establish them or choose another strategy. Do not turn a stipulated matrix into a universal claim that every acetal survives every condition or that every deprotection is harmless.

## An atom and unsaturation ledger

The starting para-disubstituted structure is C9H8O2: six ring carbons with four ring hydrogens, one aldehyde carbon/hydrogen/oxygen, and two carbons/three hydrogens/one oxygen in the acetyl group. Its DBE is six, accounting for the aromatic ring system and two carbonyls.

The net target transformation adds an ethyl fragment and a proton to the ketone addition product, giving C11H14O2. The final DBE is five: the aromatic contribution remains four and the retained aldehyde contributes one, while the reacted ketone carbonyl no longer contributes a double bond. A temporary protecting group is not part of the final target formula; every atom it adds must be accounted for again when it is removed.

For a conceptual ethylene-glycol acetal bookkeeping exercise, protection adds C2H6O2 and loses H2O, a net C2H4O. Deprotection reverses that net temporary contribution. This formula ledger does not establish oxygen-atom identity through reversible exchange. Isotope-resolved atom tracking needs more information than a total molecular formula.

## Stereochemistry survives the forward audit

The new alcohol carbon has four distinct substituents: aryl, methyl, ethyl and hydroxyl. It is one stereogenic center. The precursor ketone carbon is planar, and the paper route supplies no chiral catalyst, reagent, auxiliary or prior stereogenic influence. Therefore a claim of one assigned absolute configuration is unsupported.

Under an explicitly achiral, unbiased model the two enantiomeric addition paths are symmetry related. An ordinary achiral spectrum or total yield cannot distinguish their amounts. Evidence for enantiomeric composition needs an appropriate chiral measurement and response/assignment controls, as developed in the course's existing lab. A protecting-group step does not automatically create an enantioselective route.

## Yield is multiplicative only under its stated definitions

For synthetic isolated fractional yields P=0.85, N=0.80 and D=0.90, the overall isolated target fraction is 0.85×0.80×0.90=0.612. From 2.00 mmol starting material, the model target amount is 1.224 mmol. Do not add yields or multiply a purity fraction again if it is already built into the isolated-yield definition.

More steps often add loss, but step count alone is not a ranking. A four-step route at 90% per step gives 0.6561, while a two-step route at 80% and 75% gives 0.60. These declared numbers favor the longer route on this one metric. Cost, hazards, selectivity, stereochemistry, scale and evidence quality are separate dimensions; the example supplies no operational comparison.

## Rehearsal and report

Draw the starting and target structures in words or a labeled graph. Mark the new bond, the preserved group and the temporary mask. Audit all six permutations of P,N,D against the supplied rules. Then repeat the yield calculation with P=0.90, N=0.75, D=0.80 and 3.00 mmol initial material. Identify which claims follow from arithmetic, which follow from the stipulated compatibility matrix and which remain experimentally unsupported.

The [MIT OCW 5.12 Spring 2005 calendar](https://ocw.mit.edu/courses/5-12-organic-chemistry-i-spring-2005/pages/calendar/) places multistep synthesis after its reaction families. [OpenStax section 19.10](https://openstax.org/books/organic-chemistry/pages/19-10-nucleophilic-addition-of-alcohols-acetal-formation) is a link-only reference for the general acetal-protection principle. The target, route constraints, arithmetic and explanation here are original CC BY 4.0 material with disclosed AI assistance. No source problem, figure or procedure was imported. Qualified review and measured workload remain open.
