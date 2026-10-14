# Valence bond theory and hybridization

The [bonding-geometry lesson](08-bonding-geometry-and-molecular-properties.md) predicted molecular shapes by counting electron domains (VSEPR) and described diatomic bonding with molecular orbitals. Neither answers a question chemists ask constantly: which atomic orbitals make the bonds of a particular molecule, and why are some bonds free to rotate while others are not? **Valence bond theory** answers by treating each bond as the overlap of two atomic orbitals sharing an electron pair. Matching the shapes from VSEPR requires **hybrid orbitals**, mixtures of an atom's s and p orbitals that point in the right directions. This lesson builds sp, sp² and sp³ hybrids, separates σ from π bonds, and uses a simple quantitative relation between bond angle and s-character. All molecules are generic or synthetic teaching examples, and the bond enthalpies are illustrative averages.

The undergraduate [MIT OCW 5.111SC Principles of Chemical Science (Fall 2014) Unit II](https://ocw.mit.edu/courses/5-111sc-principles-of-chemical-science-fall-2014/pages/unit-ii-chemical-bonding-structure/) ends its bonding sequence with VSEPR (Lecture 12), molecular orbital theory (Lecture 13), and valence bond theory and hybridization (Lecture 14). The repository's General Chemistry I/II scope crosswalk had recorded valence bond theory and hybridization as missing; this lesson adds them to the local bonding week. It uses 5.111SC as a scope comparator only and reproduces no MIT material.

## Learning objectives

By the end of this lesson, you should be able to:

1. Assign sp, sp² or sp³ hybridization from a central atom's steric number, and relate the hybrid set to the bond angles VSEPR predicts.
2. Distinguish σ from π bonds, count them in a structure, and explain restricted rotation and the illustrative energy of a π bond.
3. Use the angle relation cos θ = −1/λ² to estimate the s-character of hybrids from a bond angle, and explain where the hybrid model stops being useful.

## Bonds as overlapping orbitals

In valence bond theory, a covalent bond forms when an orbital on one atom overlaps an orbital on another, and the overlap region holds two electrons with opposite spins. Greater overlap means a stronger bond. The theory keeps the familiar picture of localized bonds and lone pairs from Lewis structures, but it gives each bond an orbital description.

A problem appears immediately. Carbon's valence orbitals are one 2s and three 2p orbitals, and the p orbitals point at 90° to one another. Yet methane has four identical C–H bonds at 109.5°. Bonding with the unmixed orbitals would give one odd bond and three at right angles. Hybridization resolves this.

## Hybrid orbitals

Mixing one s orbital with n p orbitals gives n + 1 equivalent **spⁿ hybrids**. The number of orbitals is conserved: four atomic orbitals mixed give four hybrids. Each hybrid has a large lobe pointing in one direction, which overlaps strongly with a partner orbital.

| Steric number | Hybrid set | Geometry of domains | Angle between equivalent hybrids | s-character |
| --- | --- | --- | --- | --- |
| 2 | sp | linear | 180° | 50% |
| 3 | sp² | trigonal planar | 120° | 33.3% |
| 4 | sp³ | tetrahedral | 109.47° | 25% |

The steric number counts bonded atoms plus lone pairs, the same count used in VSEPR. Lone pairs occupy hybrids too. In a molecule with four domains, two bonds and two lone pairs, all four can be described as approximately sp³.

The angles in the table are not separate rules. For two equivalent hybrids written as s + λp, requiring the hybrids to be orthogonal gives

**cos θ = −1/λ²,**

where λ² is the ratio of p to s contributions. For sp³, λ² = 3 and cos θ = −1/3, so θ = 109.47°. For sp², λ² = 2 gives 120°; for sp, λ² = 1 gives 180°. The **s-character** of each hybrid is 1/(1 + λ²).

## σ and π bonds

Overlap along the line between two nuclei makes a **σ bond**, cylindrically symmetric around the bond axis. Hybrids form σ bonds, as do s orbitals and end-on p orbitals. Side-by-side overlap of parallel p orbitals makes a **π bond**, with electron density above and below the axis and a node along it.

- A single bond is one σ bond.
- A double bond is one σ plus one π bond.
- A triple bond is one σ plus two π bonds.

In ethene, each carbon is sp²: three hybrids form σ bonds to two H atoms and to the other carbon, all in one plane at about 120°. The remaining unhybridized p orbital on each carbon lies perpendicular to that plane. The two p orbitals overlap side by side to make the π bond. In ethyne, each carbon is sp, with two perpendicular p orbitals left over to make two π bonds, and the molecule is linear.

**Counting.** In the synthetic molecule CH₂=CH–C≡N, there are three C–H σ bonds, the σ parts of C=C and C≡N, and the C–C single bond: **6 σ bonds**. The π bonds are one in C=C and two in C≡N: **3 π bonds**. The terminal CH₂ and CH carbons are sp²; the nitrile carbon is sp.

**Restricted rotation.** Rotating one end of a σ bond leaves the overlap unchanged, so single bonds rotate freely at room temperature in this simple picture. Twisting a double bond by 90° would destroy the side-by-side p overlap and break the π bond. That is why the two ends of a C=C bond cannot interconvert by rotation, and why cis and trans isomers exist as distinct compounds.

**An illustrative π-bond energy.** Using illustrative average bond enthalpies of 348 kJ/mol for C–C and 614 kJ/mol for C=C, the added π bond contributes about 614 − 348 = **266 kJ/mol**, less than the σ bond. With 839 kJ/mol for C≡C, the second π bond adds about 225 kJ/mol. Average bond enthalpies vary between sources and molecules, so these differences are estimates, not measured π-bond energies.

## Angles that are not ideal

Real bond angles often differ from 109.5°, 120° or 180°, especially when lone pairs are present. The angle relation turns this around: a measured angle gives an estimate of the hybrids. Take a bent AX₂ molecule with two bonds and two lone pairs and a bond angle of 104.5°. For the two equivalent bonding hybrids,

λ² = −1/cos 104.5° = **3.99**, so each has s-character 1/(1 + 3.99) = **20.0%**.

The central atom has one s orbital in total, shared among its four hybrids. If the two lone-pair hybrids are equivalent, each holds (1 − 2 × 0.200)/2 = **30.0%** s-character. The lone pairs take more s-character than the bonds, consistent with lone pairs being held closer to the nucleus. This tendency is often called **Bent's rule**: s-character concentrates in orbitals directed toward lone pairs or electropositive substituents.

For a bond angle of 100°, the same steps give λ² = 5.76 and s-character 14.8% in the bonding hybrids. Smaller angles mean more p-character in the bonds, approaching the 90° of pure p orbitals.

## Where the model stops

Hybridization is a description chosen to match a known geometry, not an independent prediction of it. Its uses and limits are clear:

- It pairs naturally with VSEPR. Use VSEPR to get the geometry, then describe the bonds with the matching hybrids.
- It does not explain paramagnetism in O₂ or delocalized bonding in benzene or the carbonate ion. Molecular orbital theory or resonance is needed there.
- Descriptions of five- and six-domain molecules with d-orbital hybrids (sp³d, sp³d²) are now generally regarded as poor physical pictures for main-group atoms. This lesson does not use them.
- Photoelectron spectra show that the lone pairs of some molecules are not equivalent, so "two identical sp³ lone pairs" is itself a simplification.

## Common mistakes

- Assigning hybridization from the number of bonded atoms alone and forgetting lone pairs.
- Counting a double bond as two σ bonds.
- Thinking hybrids exist before bonding and cause the geometry; the model describes the geometry.
- Expecting free rotation about a double bond.
- Reading average bond-enthalpy differences as exact π-bond energies.
- Applying sp³d or sp³d² hybrids as if they were established for main-group atoms.

## Worked example

**Problem.** A synthetic bent molecule AX₂ has two bonds and two lone pairs on A, and an X–A–X angle of 104.5°. Assign an approximate hybridization, estimate the s-character of the bonding and lone-pair hybrids, and explain why the angle is below 109.5°.

**Step 1: steric number.** Two bonds plus two lone pairs give a steric number of 4, so A is approximately sp³ with tetrahedral domains.

**Step 2: bonding hybrids.** λ² = −1/cos 104.5° = 3.99, so each bonding hybrid has s-character 20.0%, less than the sp³ value of 25%.

**Step 3: lone-pair hybrids.** The remaining s-character, 1 − 0.400 = 0.600, divides between two lone-pair hybrids at 30.0% each.

**Step 4: interpret.** The lone pairs carry more s-character and sit closer to A. The bonds carry more p-character, and p orbitals favour smaller angles. Both views explain why the angle closes below the ideal tetrahedral value. VSEPR gives the same qualitative answer from lone-pair repulsion.

## Limits of this lesson

All molecules are generic or synthetic, and bond enthalpies are illustrative averages. The angle relation assumes equivalent, orthogonal hybrids built only from s and p orbitals, and it treats a measured angle as if it fixed the hybrids exactly. Delocalized bonding, resonance energy, transition-metal bonding, quantitative overlap integrals and spectroscopic evidence are not developed; molecular orbital theory remains the more general model. Nothing here is a laboratory procedure or a property prediction for a real compound. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
