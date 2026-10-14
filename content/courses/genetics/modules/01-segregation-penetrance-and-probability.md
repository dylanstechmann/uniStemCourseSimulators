# Segregation, penetrance, and probability

This lesson uses a small, synthetic pedigree to show how Mendelian segregation produces probabilities rather than promises about an individual family. A genotype is an allele combination at a locus; a phenotype is an observed trait. Connecting them requires an inheritance model and a penetrance assumption.

## Learning objectives

By the end of this lesson, you should be able to:

1. Apply segregation rules to a pedigree and update a genotype probability when an unaffected relative provides evidence.
2. Distinguish genotype frequency from phenotype frequency in a population under stated Hardy–Weinberg assumptions.

## Segregation is a probability model

For a single autosomal locus with alleles A and a, an individual with genotype Aa produces an A gamete with probability 1/2 and an a gamete with probability 1/2 under ordinary Mendelian segregation. When two Aa parents reproduce, multiply the gamete probabilities to obtain the four equally likely combinations: AA, Aa, aA, and aa. Because Aa and aA are the same unordered genotype, the offspring genotype probabilities are 1/4 AA, 1/2 Aa, and 1/4 aa.

Those fractions describe the chance for each conception under the model. They do not require a family of four children to contain exactly one child of each genotype. Each conception is modeled as a new draw; previous outcomes do not change the next child's probability when the parental genotypes and model remain the same.

For a fully penetrant autosomal recessive trait in this simplified model, only aa individuals express the trait. Two known carriers (Aa × Aa) therefore have a 1/4 probability of an affected child at each conception. The remaining 3/4 are unaffected: 1/4 are AA and 1/2 are Aa. An unaffected child is not automatically a non-carrier. Among the unaffected genotypes, two of the three equally likely genotype outcomes are Aa, so the probability that such a child is a carrier is 2/3.

The word “known” matters. If the parents are not known carriers, a pedigree may only assign probabilities to their genotypes. The offspring calculation then averages over those parental possibilities rather than treating the 1/4 result as universal.

## Worked example: update through an unaffected sibling

Assume two synthetic parents are both known heterozygous carriers (Aa × Aa), the condition is autosomal recessive, penetrance is complete, and there are no viability differences or other sources of the phenotype. One child is unaffected. Before seeing that child's phenotype, the three genotype classes have probabilities 1/4 AA, 1/2 Aa, and 1/4 aa. An unaffected phenotype rules out aa under the complete-penetrance assumption. The remaining probability is 3/4, so the conditional carrier probability is:

\[
P(Aa\mid\text{unaffected})=\frac{P(Aa)}{P(\text{unaffected})}=\frac{1/2}{3/4}=\frac{2}{3}.
\]

If that unaffected child later has a child with a partner who is independently known to be Aa, the synthetic affected-child probability is (2/3) × (1/4) = 1/6: first the parent must be a carrier, then that carrier must transmit a. This is a conditional teaching calculation, not an estimate for a real person. A confirmed genotype, a different inheritance model, or additional family evidence would change the calculation.

## Genotype and phenotype frequencies in a population

Pedigree probabilities concern transmission within families. Population frequencies ask a different question. Under Hardy–Weinberg proportions, let p and q be the frequencies of A and a among alleles, with p + q = 1. Random pairing of alleles predicts genotype frequencies p² for AA, 2pq for Aa, and q² for aa. If a phenotype is caused only by aa and has complete penetrance, its frequency estimates q². Taking the square root estimates q; then p = 1 − q and the carrier frequency is 2pq.

For example, a synthetic population has a recessive phenotype frequency of 0.04. Under the assumptions above, q = √0.04 = 0.20, p = 0.80, and the heterozygote frequency is 2(0.80)(0.20) = 0.32. Thus 4% with the phenotype corresponds to an estimated 32% heterozygous carriers in this model, not 4%. The estimate depends on the population model; it is not a way to infer any individual's genotype.

## Reading a pedigree carefully

Start by stating the candidate inheritance pattern and the observations that support it. Record which individuals are affected, unaffected, or unknown; mark obligate genotypes only when the stated model makes them necessary. Then write the genotype possibilities for the person of interest, their prior probabilities, and the likelihood of the observed phenotype under each genotype. Normalize the compatible probabilities to update the estimate. For simple complete-penetrance examples, a Punnett square often supplies the necessary probabilities. More complex pedigrees require carrying probabilities across each parent-to-child transmission.

Dominant and recessive labels describe how alleles relate to phenotype in a specified model; they do not, by themselves, state how common an allele is. Penetrance is the probability of the phenotype given a genotype, while expressivity describes variation in phenotype among people with a relevant genotype. If penetrance is incomplete, an unaffected person can still have a genotype associated with the trait, so “unaffected” no longer removes that genotype from the calculation. Age-dependent onset, phenocopies, genotyping error, and family ascertainment can also affect the likelihoods.

## Common reasoning errors

- Treating the 1/4 recessive risk as a fixed number of affected children in a four-child family, rather than a per-conception probability.
- Calling every unaffected child of two carriers a non-carrier; under complete penetrance, the conditional carrier probability is 2/3.
- Equating the recessive phenotype frequency q² with the heterozygote frequency 2pq.
- Using q = √(affected frequency) without checking that the phenotype is recessive, penetrance is complete, and Hardy–Weinberg assumptions are suitable.
- Treating an inheritance pattern in a small pedigree as proof of a causal genotype. Several models can fit sparse observations.

## Limits of this lesson

All families and population frequencies here are synthetic. The calculations assume a single autosomal locus, the stated parental genotypes, ordinary segregation, and the specified penetrance model; they omit real-world clinical complexity. Hardy–Weinberg calculations additionally assume a suitable population and random allele pairing. These examples teach probability and do not provide genetic counselling, medical advice, or information about any person's risk. The course is partial, unreviewed, formative-only, and not evidence of semester equivalence.
