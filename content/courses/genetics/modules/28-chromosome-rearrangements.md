# Chromosome rearrangements: deletions, duplications, inversions and translocations

The [aneuploidy lesson](12-nondisjunction-aneuploidy-and-maternal-age.md) dealt with whole chromosomes gained or lost. A chromosome can also break and rejoin wrongly, losing a segment, copying it, turning it round or attaching it to another chromosome. These **rearrangements** change the genetics in ways that are easy to predict once the products of meiosis are traced: deletions uncover recessive alleles, inversions seem to suppress recombination, and translocations make some gametes unbalanced and make genes on different chromosomes behave as if linked. This lesson works through each with synthetic numbers and ends with how copy number is read from sequencing or array data, and what such data cannot see.

## Learning objectives

By the end of this lesson, you should be able to:

1. Classify deletions, duplications, inversions and translocations by the change in segment order or copy number, and use pseudodominance over overlapping deletions to place a recessive mutation.
2. Trace a single crossover inside a paracentric or pericentric inversion loop to its products, and compute the fraction of unbalanced gametes and the apparent recombination among viable progeny.
3. Trace alternate and adjacent segregation in a reciprocal translocation heterozygote, compute the balanced fraction of gametes, and explain pseudolinkage.
4. Infer copy number and mosaic fraction from a normalized log₂ ratio, and state why balanced rearrangements are invisible to copy-number data.

## Four kinds of change

| Rearrangement | What happens | Copy number | Balanced? |
| --- | --- | --- | --- |
| Deletion | a segment is lost | one copy fewer | no |
| Duplication | a segment is present twice, often in tandem | one copy more | no |
| Inversion | a segment is turned through 180° on the same chromosome | unchanged | yes |
| Translocation | a segment moves to a non-homologous chromosome | unchanged if reciprocal | yes, if reciprocal |

An inversion is **paracentric** if the inverted segment excludes the centromere and **pericentric** if it includes it. A **balanced** rearrangement keeps every segment in the right number of copies, so its carrier usually has no phenotype from dosage; its genetic consequences appear in meiosis.

## Deletions uncover recessive alleles

A deletion heterozygote has only one copy of the deleted segment, so a recessive allele on the intact homolog is expressed. This **pseudodominance** maps genes. Suppose three overlapping deletions remove bands 1–4 (Df1), 3–6 (Df2) and 5–8 (Df3) of a chromosome arm. A recessive mutation *m* shows its phenotype over Df1 and over Df2 but not over Df3. It must lie in a band that both Df1 and Df2 remove and Df3 does not: bands 3–4. The logic is the same as deletion mapping in the [phage lesson](phage-functional-maps.md), applied to a chromosome.

## Duplications and unequal crossing over

Tandem copies of a sequence can pair out of register in meiosis. A crossover between misaligned copies, **unequal crossing over**, gives one product with more copies and one with fewer. If a chromosome has 3 tandem copies and the homologs pair offset by one copy, a crossover gives products with 4 and 2. In general, n copies offset by k give n + k and n − k. Repeated rounds can expand or contract gene families, and the same mechanism produces the deletion and duplication alleles of genes that lie between repeats.

## Inversions: loops and missing recombinants

In an inversion heterozygote the normal and inverted homologs can pair along their length only by forming a loop. Crossing over inside the loop still happens. What changes is the products.

- **Paracentric inversion.** A single crossover in the loop produces one **dicentric** chromatid, which is pulled to both poles at anaphase I and breaks, and one **acentric** fragment, which is lost. Of the four chromatids, the two that did not take part are balanced (one normal, one inverted) and the two crossover products are unbalanced.
- **Pericentric inversion.** A single crossover in the loop produces two monocentric chromatids, each carrying a duplication of one end and a deletion of the other. Again two of four products are balanced and two are unbalanced.

Either way, if a fraction f of meioses have a single crossover in the loop, the fraction of unbalanced products is f × 2/4 = f/2, and the viable products are the ones that did not recombine within the loop. With f = 0.40, 20% of products are unbalanced, and among the viable progeny, markers inside the inverted region show essentially no recombination. In a standard homozygote under the same single-exchange model, those markers would recombine in about 20% of products. The inversion did not stop crossing over; it removed the recombinant products. In a paracentric heterozygote the same fraction f appears directly as anaphase-I bridges with fragments. Two-strand double crossovers inside the loop give balanced products and are the rare way recombinant chromosomes escape.

Map length gives an expectation. Under the single-exchange model, a segment that is 15 cM long in standard homozygotes carries a crossover in about 2 × 0.15 = 0.30 of meioses (two of the four chromatids take part in each exchange). A heterozygote for an inversion of that segment would then show bridges in about 30% of meiocytes and lose about 15% of its products.

## Reciprocal translocations: segregation and semisterility

A heterozygote for a reciprocal translocation has two normal chromosomes, N1 and N2, and their two translocated partners, T1 and T2. The four pair as a cross-shaped quadrivalent and can segregate three ways:

- **Alternate** (N1 + N2 to one pole, T1 + T2 to the other): both gametes are balanced, one normal and one carrying the balanced translocation.
- **Adjacent-1** (non-homologous centromeres together, such as N1 + T2): both gametes carry a duplication and a deficiency.
- **Adjacent-2** (homologous centromeres together): both gametes are unbalanced; this mode is usually rare.

If alternate segregation occurs in a fraction a of meioses, the balanced fraction of gametes is a. With a = 0.55, adjacent-1 = 0.40 and adjacent-2 = 0.05, 55% of gametes are balanced: the **semisterility** of translocation heterozygotes. Among the viable offspring of a carrier and a standard parent, half carry the balanced translocation and half have the standard chromosome arrangement, because alternate segregation makes the two balanced gametes in equal numbers.

Because only alternate segregation gives viable offspring, alleles near the breakpoints on the two different chromosomes are transmitted together far more often than independent assortment predicts. This **pseudolinkage** links genes that lie on non-homologous chromosomes in the standard arrangement.

A **Robertsonian translocation** fuses the long arms of two acrocentric chromosomes. A carrier has 45 chromosomes and is balanced, but meiosis can produce gametes with the fused chromosome plus a free copy of one partner, giving a zygote trisomic for that arm. This is one route to the trisomies of the aneuploidy lesson that does not involve nondisjunction of a free chromosome. Rearrangements in somatic cells matter too: a translocation can join two genes into a fusion gene, one of the ways an oncogene is activated in the [cancer genetics lesson](29-genetics-of-cancer-two-hits-and-age.md).

## Reading copy number, and what it cannot show

Sequencing read depth or array signal, normalized as in the [expression lesson](14-measuring-gene-expression-normalization-and-false-discoveries.md), gives a ratio R of observed to expected copies for each region of a diploid genome, usually reported as log₂ R. A one-copy deletion in every cell gives log₂(1/2) = −1; a one-copy duplication gives log₂(3/2) = 0.585; a homozygous deletion gives no reads at all.

If only a fraction m of cells carry a one-copy loss, the average is 2 − m copies and log₂ R = log₂((2 − m)/2). A mosaic loss in 40% of cells gives log₂(0.8) = −0.322. For a one-copy gain in a fraction m of cells, log₂ R = log₂(1 + m/2), so a ratio of 0.263 gives 2^0.263 = 1.20 and m = 0.400. The same arithmetic sizes the mosaic chromosomal changes found in blood samples, the chromosomal counterpart of the clonal expansion described in the [geroscience lesson on clonal hematopoiesis](../../geroscience/modules/03b-clonal-hematopoiesis-and-circulating-factors.md).

Inversions and reciprocal translocations change no copy number, so depth and array ratios cannot detect them. Finding them needs breakpoints: reads that span the junction, long reads, or cytogenetic methods such as banding and fluorescence in situ hybridization.

## Common mistakes

- Concluding that an inversion stops crossing over, when it removes the recombinant products.
- Counting all four products of an inversion-loop crossover as unbalanced; two of the four did not take part.
- Expecting balanced rearrangements to show up as copy-number changes.
- Reading a mosaic ratio as a smaller deletion in every cell.
- Treating genes near translocation breakpoints as unlinked because they lie on different standard chromosomes.

## Worked example

**Problem.** In a synthetic paracentric inversion heterozygote, 30% of meiocytes show an anaphase-I bridge and fragment. What fraction of products are unbalanced, what fraction are viable, and what recombination will markers inside the inversion show among viable progeny?

**Step 1: crossover meioses.** Each bridge marks a meiosis with a single crossover in the loop, so f = 0.30.

**Step 2: unbalanced products.** Two of the four chromatids took part, so the unbalanced fraction is 0.30 × 2/4 = 0.15, and 0.85 of products are balanced.

**Step 3: recombination among viable progeny.** The balanced products are the non-crossover chromatids, so markers inside the inversion show essentially no recombinants, although a standard homozygote under the same model would show about 15%.

**Step 4: reading the result.** Low recombination with reduced fertility and bridges points to an inversion, not to tight linkage. Tight linkage would give low recombination without the bridges or the lost products.

## Limits of this lesson

All rates and fractions are synthetic. The inversion arithmetic assumes single exchanges and no chromatid interference, ignores two- and multiple-strand double crossovers except to name them, and treats every unbalanced product as inviable; real viability depends on the size and content of the segments. The translocation segregation frequencies are invented. Copy-number ratios assume clean normalization and diploid reference regions. The lesson describes mechanisms, not the risk to any person or family, and gives no genetic-counselling or medical advice.
