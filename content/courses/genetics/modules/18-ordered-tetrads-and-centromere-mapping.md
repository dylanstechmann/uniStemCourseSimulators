# Ordered tetrads and centromere distance: first- and second-division segregation

Unordered tetrads, as in the three-point mapping and tetrad reading, tell you which four spores came from one meiosis but not where each spore sat. Ordered tetrads keep the spores in the sequence set by the meiotic divisions, and that sequence carries information the unordered classes cannot. For a gene linked to its centromere, the arrangement of alleles shows whether the two alleles separated at the first meiotic division or whether a crossover between the gene and the centromere delayed their separation to the second division. This lesson derives a centromere-distance estimate from that pattern, shows how to bound it when no crossover is seen, and states where the estimate fails.

## Learning objectives

By the end of this lesson, you should be able to:

1. Describe how four-spore and eight-spore ordered asci record the products of one meiosis, and which spores are sister products.
2. Classify a centromere-linked gene's ordered asci as first-division or second-division segregation.
3. Convert a count of second-division asci into a recombination frequency and a centromere distance in centimorgans, predict expected counts from a known distance, and bound the distance when no second-division ascus is seen.
4. Explain why the single-exchange estimate underestimates the distance of loci far from the centromere.

## Ordered asci and the meiotic products

An ascus is the sac that holds the products of one meiosis in ascomycete fungi. In budding yeast the four spores lie in no fixed order, which is why yeast tetrads are analysed as unordered classes. In fungi such as *Neurospora crassa* and *Sordaria*, the ascus is long and narrow, the division spindles do not overlap, and the spores stay in the order in which the divisions placed them. That order records how the chromosomes segregated.

In a linear four-spore ascus, the four spores are the four haploid products of meiosis. Meiosis I separates the homologs and sends one *dyad*, a pair of sister chromatids still joined at the centromere, to each end of the ascus. Meiosis II then separates the sisters within each dyad. The two products of one dyad therefore lie next to each other: spores 1 and 2 are sister products of one dyad, and spores 3 and 4 are sister products of the other.

In an eight-spore ascus, as in *Neurospora*, each of the four meiotic products divides once more by mitosis, so the spores come in adjacent pairs with the same genotype (1–2, 3–4, 5–6 and 7–8). Spores 1 to 4 derive from one dyad and spores 5 to 8 from the other. The two halves of the ascus correspond to the two dyads, which makes the first-division split easy to read.

## First-division segregation (FDS)

Suppose no exchange occurs between the gene and its centromere. Both chromatids of each dyad then carry the same allele, so one dyad is A|A and the other a|a. Meiosis I sends the A dyad to one end and the a dyad to the other. In an eight-spore ascus the pattern is A A A A a a a a, or the reverse, with one allele in each half. In a four-spore ascus it is A A a a or a a A A. The name refers to the division at which the alleles separated.

## Second-division segregation (SDS)

Now suppose one crossover occurs between the gene and the centromere, between two non-sister chromatids. The chromatids of each dyad then differ at the gene, so each dyad is A|a, and its alleles separate only at meiosis II. Each half of an eight-spore ascus therefore holds two A and two a spores in adjacent pairs, as in A A a a A A a a, a a A A a a A A, A A a a a a A A or a a A A A A a a. In a four-spore ascus spores 1 and 2 differ, as in A a A a or A a a A. Which order appears depends on how each dyad was oriented on its meiosis II spindle; every one of them counts as SDS.

The SDS pattern is the diagnostic signal. Read a four-spore ascus from one end: if spores 1 and 2 are identical, the gene showed first-division segregation; if they differ, at least one exchange occurred between the gene and the centromere. The estimate below treats each such ascus as the record of exactly one exchange.

## From SDS asci to centromere distance

Each meiosis with a single exchange in the interval gives an SDS ascus, so the SDS fraction estimates how often such exchanges occur. A single exchange involves only two of the four chromatids, so only half of the products of that meiosis are recombinant between the gene and the centromere. The recombination frequency between the gene and its centromere is therefore

r = ½ × (SDS asci ÷ total asci),

and the centromere distance in centimorgans is 100 × r. Substituting gives d = 50 × (SDS asci ÷ total asci). If 20% of asci are SDS, then r = 0.10 and the gene lies about 10 cM from its centromere.

The same relation runs in reverse. A gene 12 cM from its centromere should show an SDS fraction of about 2 × 0.12 = 0.24. Among 500 asci, that is about 120 SDS asci and 380 FDS asci.

## Counts are samples

An SDS fraction from a few hundred asci carries sampling error, so report the count behind every estimate. A count of zero gives a point estimate of 0 cM but does not show that the gene sits on the centromere, because a short interval can produce no SDS ascus by chance. When no SDS ascus appears among n asci, the rule of three gives a rough 95% upper bound of 3 ÷ n on the SDS fraction. For 200 asci with no SDS ascus, the bound is 3 ÷ 200 = 0.015, or 50 × 0.015 = 0.75 cM: a gene that far from its centromere would give no SDS ascus in only about 5% of such samples.

## Why the estimate underestimates distant genes

The formula assumes that each meiosis has at most one exchange between the gene and its centromere. A second exchange in the same interval can restore the first-division arrangement. Two exchanges involving the same pair of non-sister chromatids leave both dyads homozygous, which produces a first-division pattern, and so do two exchanges that between them involve all four chromatids; only two-exchange meioses that involve three chromatids still give SDS. Meioses that are restored in this way are invisible to the SDS count. As the distance grows, multiple exchanges become more frequent, so the SDS fraction grows more slowly than the distance and the estimate falls short of the true value.

There is also a ceiling. If exchanges occur independently and involve chromatids at random, a gene very far from its centromere ends up with its two A and two a alleles placed at random among the four chromatids. The two products of each dyad then match in only one-third of asci, so the SDS fraction levels off near two-thirds and 50 × (SDS asci ÷ total asci) levels off near 33 cM. An estimate near 33 cM is therefore a ceiling of the method, not a measured distance. Strong crossover interference, which suppresses second exchanges, can push the SDS fraction above two-thirds; that departure is itself evidence about how exchanges are distributed.

The estimate is most reliable for short intervals. For longer ones, analysts either limit the claim or fit a model of how exchanges are distributed. The map-function idea from the three-point mapping reading applies, but the correction for second-division counts differs from Haldane's two-point formula and is not derived here.

## Common mistakes

- Reading the SDS fraction as the distance itself. The recombination frequency is half the SDS fraction, and the distance in cM is 100 times the recombination frequency.
- Classifying an ascus without checking spore order. In four-spore asci, compare spores 1 and 2; in eight-spore asci, tell the 4:4 pattern (FDS) from the 2:2:2:2 pattern (SDS).
- Expecting a single SDS arrangement. All four 2:2:2:2 orders in an eight-spore ascus, and A a A a, A a a A and their reverses in a four-spore ascus, count as SDS.
- Treating a count of zero as proof that the gene sits on the centromere.
- Applying the single-exchange formula to a distant gene without noting that unseen multiple exchanges, and the two-thirds ceiling, make it an underestimate.

## Worked example

**Problem.** In 240 four-spore asci from a gene linked to its centromere, 18 have spores 1 and 2 that differ. Estimate the centromere distance.

**Step 1.** SDS fraction = 18 ÷ 240 = 0.075.

**Step 2.** Recombination frequency r = ½ × 0.075 = 0.0375.

**Step 3.** Centromere distance = 100 × 0.0375 = 3.75 cM.

**Step 4.** Check the regime and the precision. The SDS fraction is far below two-thirds and the interval is short, so the single-exchange estimate should be adequate; unseen double exchanges would make the true distance only slightly larger. With 18 SDS asci, the binomial standard error is about 50 × √(0.075 × 0.925 ÷ 240) ≈ 0.85 cM, so report roughly 3.8 ± 0.9 cM rather than 3.75 cM.

## Limits of this lesson

All counts are synthetic. Real ordered-tetrad analysis must handle gene conversion, which yields asci such as 6:2 or 5:3 that fit neither pattern, as well as inviable spores and occasional spindle overlap that scrambles spore order, and it usually pools many asci from several crosses. This lesson uses the single-exchange model with a rough sampling bound. It does not treat two-locus ordered-tetrad classes, the correction for multiple exchanges, chromatid interference or the cytology of centromere pairing. The broader course remains partial, unreviewed and formative-only.
