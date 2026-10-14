# Microbial genetic exchange: transfer, mapping, and complementation

Bacteria and their phages provide compact systems for asking how genes move, whether two loci are close on a chromosome, and which gene may underlie a mutant phenotype. The transfer event itself does not prove that a transferred gene causes a phenotype. This lesson compares the major routes of genetic exchange and develops two kinds of evidence: entry or co-transfer patterns for linkage, and plasmid complementation for gene function. All strains and counts are fictional teaching examples; the lesson describes inference rather than laboratory procedures.

## Three routes move DNA between cells

**Conjugation** transfers DNA through cell-to-cell contact. An F plasmid can move from an F+ donor to an F− recipient. If F DNA has integrated into the donor chromosome, the strain is called Hfr; transfer then begins at the integrated origin and can carry chromosomal genes in a characteristic order. Mating is often interrupted before the entire chromosome enters, so early-arriving markers are more likely to be recovered in recipients than late markers. Entry time is a map in minutes of transfer under that donor's orientation and conditions, not a distance in base pairs.

**Transformation** occurs when a cell takes up free DNA from its surroundings. A transformed cell can recombine part of that DNA into its genome, but survival or uptake alone does not show which sequence caused a later phenotype. **Transduction** is phage-mediated DNA transfer. In generalized transduction, a phage particle occasionally packages a fragment of bacterial chromosome; genes close enough to fit on the same fragment may be co-transduced. In specialized transduction, imprecise excision of a prophage carries particular bacterial genes adjacent to its insertion site. These mechanisms differ in the source and packaging of the DNA, so the right interpretation depends on which route the experiment used.

## Infer order from entry and linkage from co-transfer

Imagine an Hfr donor in which selected markers first appear at median times of 4 minutes for `ilv`, 9 minutes for `leu`, 15 minutes for `azi`, and 22 minutes for `ton`. The supported entry order is `ilv → leu → azi → ton`; the adjacent entry intervals are about 5, 6 and 7 transfer-minutes. A later marker can appear less often because mating was interrupted before it entered, so absence from a selected colony is not automatically evidence that the allele is nonfunctional. Selection, recombination, donor orientation and sampling can all shape the observed frequencies.

For transduction, compare co-transduction among recipients that received a focal marker. In a synthetic sample of 120 transductants carrying allele `x`, 72 also carry marker `b`, while 18 carry marker `c`. Since `b` accompanies `x` more often than `c` does, `b` is likely closer to `x` than `c` is under comparable sampling and recovery conditions. This is relative linkage evidence, not a direct base-pair distance: the size of packaged fragments, recombination, selection and viability influence recovery. Pairwise co-transduction rates alone may not determine a unique order; an additional marker or a designed ordering experiment can resolve ambiguity.

## Complementation tests a functional hypothesis

Suppose a bacterial mutant fails to grow when compound Q is the only supplied nutrient. Introduce an empty vector, a plasmid with a wild-type copy of candidate gene `A`, or a plasmid with candidate gene `B`. If only the `A` plasmid restores growth, the result supports the hypothesis that the original defect disrupts `A` function. It does not show which DNA change occurred, whether `A` directly catalyzes the relevant reaction, or whether the plasmid reproduces normal expression.

The comparison needs controls matched to the claim. A wild-type strain shows that the growth condition can support the phenotype; the empty vector checks for effects of the vector itself; and the mutant without a complementing insert defines the unrescued baseline. A known functional copy can serve as a positive control. Independent transformants reduce the chance that one unusual clone explains the result. Expression level and plasmid copy number matter: rescue from strong overexpression can bypass a defect indirectly, while failure to rescue may reflect a missing promoter or an incompatible gene product rather than the wrong candidate. Complementation narrows a functional hypothesis; sequence and expression analyses answer different questions.

## Worked example

In a synthetic interrupted-mating study, marker `m1` enters at 3 minutes, `m2` at 8 minutes, and `m3` at 14 minutes. The supported order is `m1 → m2 → m3`, with approximate intervals of 5 and 6 transfer-minutes. In a separate transduction study, 72/120 co-transfer of `x` with `b` versus 18/120 with `c` supports closer linkage of `b` to `x`, but gives no exact physical distance. A wild-type `A` plasmid that rescues a mutant while an empty vector does not supports an `A`-function hypothesis, subject to expression and vector controls.

## Common reasoning errors

- Confusing transformation, conjugation and phage-mediated transduction because each can move DNA.
- Treating an Hfr entry time as an exact physical distance or ignoring which direction the donor transfers.
- Converting co-transduction frequency directly to base pairs without a model for fragment size and recovery.
- Treating rescue by a plasmid as proof of the exact mutation or a direct biochemical mechanism.
- Interpreting no rescue as evidence against a candidate without checking expression and vector controls.

## Limits of this lesson

All strains, marker names, entry times and counts are synthetic. The unit samples microbial transfer and functional complementation; it does not cover all phage life cycles, transposition, or recombinant-DNA methods, and it is not a protocol for handling microbes. These examples establish no evidence about any clinical isolate or person. The broader course remains partial, unreviewed and formative-only.
