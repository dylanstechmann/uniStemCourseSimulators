# Structure, resonance, and acid-base reactivity

Organic reactions depend on where electrons are concentrated and how readily a molecule can reorganize them. A reliable first step is to draw a valid structure, track formal charge and electron pairs, and identify which species would form after proton transfer. Resonance helps compare some structures without changing which atoms are connected; acidity compares an acid with its conjugate base after a hydrogen ion is removed.

## Learning objectives

By the end of this lesson, you should be able to:

1. Rank acidity using conjugate-base stabilization.
2. Use resonance without moving atoms or violating valence.

## Read a structure before predicting reactivity

Start with connectivity, bond order, lone pairs, and formal charges. A neutral oxygen with two bonds has two lone pairs in a typical Lewis structure; a singly bonded oxygen with three lone pairs carries a negative formal charge. Nitrogen and carbon have different usual valence patterns, so a plausible-looking arrow can still create an invalid product if the electron count is not checked.

Curved arrows represent movement of an electron pair. The tail begins at an electron source—a lone pair or bond—and the head points to the atom or bond receiving that pair. For example, a base can use a lone pair to form a bond to a proton while the original bond to that proton supplies the pair to the atom left behind. Both arrows are needed to show the proton transfer and preserve the total electron count. Moving a proton is a change in connectivity and is an actual reaction step, not a resonance operation.

## Conjugate bases connect structure to acidity

In a Brønsted–Lowry reaction, an acid donates a proton and becomes its conjugate base; a base accepts a proton and becomes its conjugate acid. To compare two acids, first remove the same type of proton from each and draw the resulting conjugate bases. The stronger acid is generally the one whose conjugate base is more stable relative to the neutral acid, under the same solvent and temperature conditions.

A useful comparison order is:

1. **Atom:** Is the negative charge on an atom that can accommodate it? Across a row, greater electronegativity often stabilizes negative charge; down a group, larger atoms can spread charge over more volume.
2. **Resonance:** Can valid contributors delocalize charge over multiple atoms, especially onto electronegative atoms?
3. **Induction:** Do nearby electronegative groups withdraw electron density through sigma bonds? This effect usually weakens with distance.
4. **Hybridization:** For carbon acids with otherwise comparable structures, greater s character can stabilize negative charge; the usual trend is sp more than sp² more than sp³.
5. **Solvation and context:** Can the solvent stabilize the acid and conjugate base differently? Are the compared pKa values measured on a compatible scale?

These are comparison tools, not a universal ranking algorithm. Several effects can compete, and a measured pKa belongs to specified conditions. A table value should not be moved between solvents as if acidity were independent of environment. [OpenStax Organic Chemistry, “2.8 Acid and Base Strength”](https://openstax.org/books/organic-chemistry/pages/2-8-acid-and-base-strength) summarizes the relation between pKa and acid strength; [“2.10 Organic Acids and Organic Bases”](https://openstax.org/books/organic-chemistry/pages/2-10-organic-acids-and-organic-bases) discusses organic conjugate bases.

## A pKa comparison is logarithmic

For an acid (HA), \(pK_a=-\log_{10}K_a\). A lower pKa corresponds to a larger acid-dissociation constant and a stronger acid on the same scale. A difference of one pKa unit represents a tenfold difference in (K_a); a difference of four units represents a factor of (10^4).

For the hypothetical proton-transfer reaction

\[
HA+B^-\rightleftharpoons A^-+HB,
\]

an approximate equilibrium relation is

\[
K\approx10^{pK_a(HB)-pK_a(HA)}.
\]

If (HA) has pKa 5 and (HB) has pKa 9 on the same reference scale, the approximate equilibrium constant is \(10^{9-5}=10^4\), favoring the side with the weaker acid and weaker base. This is a constructed teaching example, not a measured chemical pair. The relation is only as useful as the pKa values, solvent, and standard-state assumptions supplied with it. It predicts an equilibrium preference, not a reaction rate or a complete mechanism.

## Resonance changes electron placement, not atom positions

Resonance contributors are alternative electron-bookkeeping structures for one delocalized species. The atom skeleton and sigma-bond framework stay fixed; only electrons move. Valid contributors preserve the total charge and use plausible valence. For common second-row atoms such as carbon, nitrogen, and oxygen, check that a curved arrow does not create a fifth bond to carbon or otherwise exceed the allowed octet in an ordinary Lewis structure.

The carboxylate ion illustrates the idea. One contributor places a double bond between carbon and the first oxygen and a negative charge on the second oxygen. A second contributor moves a lone pair from the negatively charged oxygen to form the second C–O pi bond while moving the original pi pair onto the first oxygen. The two arrows must be drawn together: moving only one pair would give carbon an invalid valence or leave an electron count inconsistent with the ion's charge. [OpenStax Organic Chemistry, “2.5 Rules for Resonance Forms”](https://openstax.org/books/organic-chemistry/pages/2-5-rules-for-resonance-forms) is a link-only conceptual reference.

The actual carboxylate is not switching back and forth between two separate molecules. It is a single resonance hybrid with electron density shared across the O–C–O unit; the two C–O bonds are equivalent in the idealized ion. The contributors are not equally important in every molecule: structures with complete octets, fewer charge separations, and negative charge on more electronegative atoms are often more stable. But contributor drawings are not observed populations, and no single contributor is the molecule by itself.

## Why resonance can affect acidity

Acetic acid loses a proton to form acetate. Its conjugate base has two important contributors that place negative charge on either oxygen while preserving the same atom positions. By comparison, deprotonating an alcohol produces an alkoxide with its negative charge localized on one oxygen and no adjacent carbonyl pi system for the same delocalization. The resonance stabilization of acetate helps explain why a carboxylic acid is more acidic than a typical alcohol. The atoms, solvent, and other structural features still matter; resonance is one contributor to the comparison, not an isolated numerical rule.

This connection also explains why the most acidic bond is not identified by looking only for a visibly polarized hydrogen. Compare the conjugate bases that would result from removing candidate protons. A proton on a carbon adjacent to a carbonyl may be more acidic than an ordinary alkane proton because its conjugate base can delocalize charge into the carbonyl system; however, the equilibrium and the reaction conditions still determine how much deprotonation occurs.

## A structure and arrow audit

Before accepting a resonance or proton-transfer proposal, check:

- Did the atom connectivity remain fixed for resonance, and change only for an actual reaction step?
- Does each arrow begin at a lone pair or bond that contains the electrons being moved?
- Are all formal charges shown, and does their sum match the species charge?
- Does every atom retain a plausible valence and electron count?
- Are the compared acids and pKa values defined under compatible conditions?
- Does the conclusion concern equilibrium, rate, or product formation? Those are different claims.

This bookkeeping is a filter for plausible structures and mechanisms. It does not by itself predict a reaction rate, selectivity, or product yield; steric effects, solvent, temperature, concentration, and competing pathways may also matter.

## Common reasoning errors

- Moving atoms or sigma bonds between resonance contributors.
- Treating resonance contributors as separate molecules in equilibrium.
- Drawing one arrow of a coupled carboxylate electron shift and violating carbon valence.
- Ranking acidity from the atom bearing hydrogen without comparing the conjugate bases.
- Treating a one-unit pKa difference as an additive rather than tenfold change in (K_a).
- Applying a pKa value measured in one solvent as though it were universal.
- Treating an equilibrium preference as a statement about reaction speed.

## Limits of this lesson

The pKa example uses hypothetical values, and structural trends are qualitative. Real values depend on molecular structure, solvent, temperature, and reference scale. This reading develops conceptual electron accounting; it includes no chemical handling, synthesis procedure, or experimental safety protocol.
