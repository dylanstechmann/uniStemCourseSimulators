# Beyond the octet: incomplete, odd-electron and expanded Lewis structures

The [bonding-geometry lesson](08-bonding-geometry-and-molecular-properties.md) built Lewis structures from a valence-electron count, assigned formal charges and used the octet as a check. Many common species fail that check. Boron trifluoride has six electrons around boron, nitrogen dioxide has an odd number of electrons, and sulfur hexafluoride has twelve around sulfur. This lesson keeps the same counting recipe, shows where each family of exceptions appears in it, and carries the structures through to shape and polarity with the electron-domain method. It supplies bookkeeping and shape predictions, not an account of why the bonds form.

The undergraduate [MIT OCW 5.111SC Principles of Chemical Science (Fall 2014) Unit II](https://ocw.mit.edu/courses/5-111sc-principles-of-chemical-science-fall-2014/pages/unit-ii-chemical-bonding-structure/) introduces Lewis structures in Lecture 10, and its [Lecture 11](https://ocw.mit.edu/courses/5-111sc-principles-of-chemical-science-fall-2014/pages/unit-ii-chemical-bonding-structure/lecture-11/) is titled for the breakdown of the octet rule, with radicals and expanded octets in its description. The published topic index of [UC Irvine Chem 1A General Chemistry](https://ocw.uci.edu/courses/chem_1a_general_chemistry.html) lists "Breaking the Octet Rule" examples in Lectures 8 and 9, among them SF₆, XeF₄, BH₃, POCl₃ and ClF₄⁻. The repository's General Chemistry I/II scope crosswalk had recorded only octet-obeying structures, and this lesson adds the exceptions. Both courses are link-only scope comparators; no text, figure or problem is reproduced.

## Learning objectives

By the end of this lesson, you should be able to:

1. Count valence electrons and build Lewis structures for species with an incomplete octet, an odd number of electrons, or more than eight electrons around a central atom.
2. Choose between competing structures with formal charge, and state what a structure does and does not claim.
3. Predict the electron-domain geometry, molecular shape and polarity of species with steric numbers from 3 to 6, including lone pairs on the central atom.

## The counting recipe still works

1. Add the valence electrons of every atom, subtract the charge of a cation and add it for an anion.
2. Join the atoms with single bonds, two electrons each.
3. Give each terminal atom lone pairs until it has eight electrons.
4. Place any electrons left over on the central atom as lone pairs.
5. Compute formal charges, valence electrons minus nonbonding electrons minus half the bonding electrons. They must sum to the net charge.

Octet-obeying molecules finish at step 4 with eight electrons around the central atom. The three families of exceptions differ in what step 4 leaves behind.

## Incomplete octets

Boron has three valence electrons. In BF₃ the count is 3 + 3 × 7 = 24: three B–F bonds use 6, and the three fluorines take 18 as lone pairs, so nothing is left for boron, which has only six electrons. Its formal charge is 3 − 0 − 6/2 = 0. A drawing with one B=F double bond would give boron eight electrons, but it puts −1 on boron and +1 on fluorine, the most electronegative atom, so the six-electron structure is preferred. The electron-poor boron explains the chemistry: BF₃ accepts a lone pair from ammonia to form H₃N–BF₃, completing boron's octet. A molecule that accepts an electron pair in this way is a Lewis acid.

## Odd-electron species

NO₂ has 5 + 2 × 6 = 17 valence electrons, an odd number, so the electrons cannot all be paired. A conventional structure places the single unpaired electron on nitrogen, with formal charges of +1 on nitrogen and −1 on the singly bonded oxygen. Such a species is a **radical**. Radicals are paramagnetic and often reactive: NO₂ pairs its unpaired electrons by joining another NO₂ to form N₂O₄. Any species with an odd electron count must have at least one unpaired electron, and no arrangement of full octets can describe it.

## Expanded valence shells

Central atoms from the third period down can be drawn with more than eight electrons, while carbon, nitrogen, oxygen and fluorine are not. Step 4 of the recipe then puts the leftover electrons on the central atom whatever their number. The results below follow from the count alone.

| Species | Valence electrons | Bonds | Lone pairs on centre | Electrons around centre | Steric number | Shape |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| SF₆ | 48 | 6 | 0 | 12 | 6 | octahedral, nonpolar |
| PCl₅ | 40 | 5 | 0 | 10 | 5 | trigonal bipyramidal, nonpolar |
| SF₄ | 34 | 4 | 1 | 10 | 5 | see-saw, polar |
| ClF₃ | 28 | 3 | 2 | 10 | 5 | T-shaped, polar |
| XeF₂ | 22 | 2 | 3 | 10 | 5 | linear, nonpolar |
| BrF₅ | 42 | 5 | 1 | 12 | 6 | square pyramidal, polar |
| XeF₄ | 36 | 4 | 2 | 12 | 6 | square planar, nonpolar |
| ICl₄⁻ | 36 | 4 | 2 | 12 | 6 | square planar, symmetric ion |

The **steric number** is the number of bonded atoms plus the lone pairs on the central atom, and a multiple bond counts once. Steric number 5 gives a trigonal bipyramid with angles of 90°, 120° and 180°. An equatorial position has two neighbours at 90° and an axial position has three, so lone pairs, which repel more strongly, take equatorial positions. That is why SF₄ is see-saw, ClF₃ T-shaped and XeF₂ linear. Steric number 6 gives an octahedron with angles of 90° and 180°, and two lone pairs sit opposite each other, which makes XeF₄ and ICl₄⁻ square planar.

## Choosing between structures

The sulfate ion has 6 + 4 × 6 + 2 = 32 valence electrons. Drawn with four S–O single bonds and an octet on every atom, sulfur has formal charge 6 − 0 − 8/2 = +2 and each oxygen −1. Drawn with two S=O double bonds, sulfur has twelve electrons and formal charge 0, two oxygens are neutral and two are −1. Both sum to −2 and both give a tetrahedron. The second minimizes the formal charges, the first keeps every octet. Formal charge is a bookkeeping assignment, so neither drawing measures the real charge on sulfur, and the choice does not change the bond count or shape you predict.

This course counts electrons around heavier central atoms without attributing the bonding to d-orbital hybrids. The counts, the steric numbers and the shapes are what the model supports.

## Worked example

**Problem.** Draw XeF₄ and ClF₃, and give each one's steric number, shape, polarity and formal charges.

**Step 1: XeF₄.** Xenon contributes 8 and four fluorines 28, so there are 36 electrons. Four Xe–F bonds use 8, and the fluorines take 24 as lone pairs. The remaining 36 − 32 = 4 electrons are two lone pairs on xenon, which therefore has 12 electrons.

**Step 2: formal charges.** Xenon: 8 − 4 − 8/2 = 0. Each fluorine: 7 − 6 − 2/2 = 0.

**Step 3: shape.** The steric number is 4 + 2 = 6, an octahedral arrangement of domains. The lone pairs go opposite each other, leaving the four fluorines in a plane: square planar, with F–Xe–F angles of 90° and 180°. The bond dipoles cancel, so XeF₄ is nonpolar.

**Step 4: ClF₃.** Chlorine contributes 7 and three fluorines 21, giving 28 electrons. Three bonds use 6 and the fluorines take 18, leaving 4 electrons, two lone pairs on chlorine. The steric number is 3 + 2 = 5, a trigonal bipyramid with both lone pairs equatorial. The molecule is T-shaped, with the F–Cl–F angle just under 90°, and the dipoles do not cancel, so it is polar.

## Common mistakes and checks

- Forgetting to add or subtract electrons for a charge.
- Putting more than eight electrons on carbon, nitrogen, oxygen or fluorine.
- Leaving the lone pairs on the central atom out of the steric number.
- Placing lone pairs in axial positions of a trigonal bipyramid.
- Calling every molecule with polar bonds polar, when symmetric arrangements cancel.
- Insisting on eight electrons around boron, or on full octets in an odd-electron species.
- Treating formal charge as the actual charge on an atom.

A check: the electrons placed must equal the valence-electron total, the formal charges must sum to the net charge, and an odd total must leave an unpaired electron.

## Limits of this lesson

All species are used as textbook examples of electron counting; no preparation, handling or reactivity advice is given, and several of these fluorides are hazardous. The counting treats lone pairs and bonds as localized pairs and ignores resonance beyond the sulfate comparison. VSEPR angles are ideal values, and real lone-pair repulsion compresses them. Molecular-orbital descriptions of electron-rich and electron-poor bonding are not developed. Original instruction has substantial AI assistance and uses link-only references without copied source text. The course remains partial, unreviewed and formative-only.
