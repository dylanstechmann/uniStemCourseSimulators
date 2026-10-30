# Genetics of cancer: oncogenes, tumor suppressors, two hits and age

Cancer is a genetic disease of somatic cells. A lineage of cells acquires changes, in its own DNA, that free it from the controls on division and death, and its descendants inherit those changes. Inherited alleles can raise the chance that this happens, but most of the changes arise during life, in the way the [somatic mutation lesson](13-mutation-rates-fluctuation-test-and-somatic-mutation.md) describes. This lesson separates the two kinds of cancer gene, follows Knudson's two-hit reasoning with Poisson statistics, uses the multistage model to connect the number of required changes to the steep rise of cancer incidence with age, and lists the ways the second copy of a gene is lost.

## Learning objectives

By the end of this lesson, you should be able to:

1. Distinguish oncogenes from tumor suppressor genes by the effect of a mutation in one cell, and explain why an inherited tumor suppressor allele behaves as a dominant predisposition with incomplete penetrance in families.
2. Use Poisson statistics to compute the fractions of carriers with no, unilateral and bilateral tumors from a mean number of tumors, and compare one-hit with two-hit kinetics.
3. Use the multistage model to relate the slope of log incidence against log age to the number of rate-limiting steps, and show how a mutator phenotype or clonal expansion raises the expected number of completed lineages.
4. List the routes to loss of heterozygosity and use copy number and marker patterns to distinguish them.

## Two kinds of cancer gene

An **oncogene** is a gene whose gain of function drives division or survival. One mutant copy is enough, so the mutation is dominant at the level of the cell. Activation can come from a point mutation that locks a signalling protein on, from amplification of the gene, or from a [translocation](28-chromosome-rearrangements.md) that places it next to a strong promoter or fuses it to another gene. A **tumor suppressor gene** restrains division, repairs damage or triggers death. A cell must lose both copies before the restraint is gone, so the mutation is recessive at the level of the cell. Genes that maintain the genome, such as [DNA repair genes](../../cell-biology/modules/06b-dna-damage-and-repair-evidence.md), act indirectly: losing them raises the rate of every later mutation.

The cell-level and family-level views differ. A person who inherits one inactive copy of a tumor suppressor gene has it in every cell, and with millions of cells each at risk of losing the second copy, the chance that at least one does is high. In a pedigree the predisposition therefore looks dominant with incomplete [penetrance](01-segregation-penetrance-and-probability.md), although in the cell it is recessive.

## Knudson's two hits

From observations on 48 cases of retinoblastoma and published reports, Knudson (1971) proposed that the tumor requires two mutational events. In the inherited form one is inherited and the second occurs in a somatic cell; in the non-inherited form both occur in somatic cells. He estimated that carriers develop an average of three tumors, and showed with Poisson statistics that this one number accounts for carriers with no tumor, with tumors in one eye and with tumors in both.

The arithmetic is short. If tumors arise independently with mean m = 3 per carrier, the fraction of carriers with none is e^(−3) = 0.0498, so about 95% develop at least one. Splitting the mean equally between two eyes gives 1.5 per eye, so each eye is tumor-free with probability e^(−1.5) = 0.223. Then both eyes are affected in (1 − 0.223)² = 0.604 of carriers, one eye in 2 × 0.223 × 0.777 = 0.347, and neither in 0.223² = 0.0498. Run backwards, a tumor-free fraction p₀ gives m = −ln p₀, the same zero-class reasoning as the mutation-rate lesson.

**One hit against two.** Model the target as N = 10⁶ cells, each losing a given copy at rate μ = 10⁻⁶ per year during a three-year window. In a carrier, one hit per cell is needed, so the expected number of tumors is Nμt = 10⁶ × 10⁻⁶ × 3 = 3, matching the mean above. In a non-carrier, both copies must be hit in the same cell, and each is hit with probability about μt, so the expected number is about N(μt)² = 10⁶ × (3 × 10⁻⁶)² = 9 × 10⁻⁶, or 9.00 per million people. One-hit expectations grow in proportion to t and two-hit expectations in proportion to t², which is why non-inherited cases are rare, usually have a single tumor and tend to appear later. These parameters are invented to reproduce the mean of three; they are not Knudson's estimates.

## Many hits and the rise of cancer with age

Most adult cancers need more than two changes. Armitage and Doll (1954) proposed a multistage theory to account for the age distribution of cancer. In its standard form, if a lineage must pass through k rate-limiting steps, each occurring at a small constant rate, the probability that it has completed all of them by age t grows as t^k, and the incidence (the rate of new cases at age t) grows as t^(k−1). On a plot of log incidence against log age the slope is k − 1.

**Synthetic incidence:** a cancer with 12 new cases per 100,000 people per year at age 40 and 384 at age 80 rises by a factor of 32 when age doubles. Since 2^5 = 32, the slope is 5 and the model infers k = 6 steps. Under the same model, incidence at age 70 is (70/50)^5 = 5.38 times that at age 50. A process with five steps would give a factor of 2^4 = 16 per doubling of age. This is one way to read the strong age dependence of many cancers: not that aging itself is a step, but that each lineage needs time to accumulate several changes.

Two features speed the process. A **mutator phenotype**, such as loss of mismatch repair, multiplies the rate of every mutational step. Raising μ by a factor F multiplies a k-step probability by F^k; for two hits, an eightfold rise in μ gives a 64-fold rise. **Clonal expansion** multiplies the number of cells at risk. If the first hit gives a clone that grows as e^(rt), the expected number of second hits by time t is μ(e^(rt) − 1)/r instead of μt for a single cell that does not expand. With r = 0.3 per year over 20 years this is (e^6 − 1)/0.3 = 1341 cell-years of exposure instead of 20, about 67 times as many. The expansions of [clonal hematopoiesis](../../geroscience/modules/03b-clonal-hematopoiesis-and-circulating-factors.md) are this process caught in a tissue where most clones never become cancers.

## How the second copy is lost

The second hit to a tumor suppressor gene often removes the remaining normal allele by a route that leaves a signature. At markers where the person is heterozygous, the tumor becomes homozygous or hemizygous: **loss of heterozygosity (LOH)**. Copy number and the extent of the loss distinguish the routes:

| Route | Copy number in the region | Markers |
| --- | --- | --- |
| Point mutation of the second allele | 2 | heterozygosity kept |
| Interstitial deletion | 1 over the deleted segment | LOH over the segment only |
| Mitotic recombination | 2 | LOH distal to the exchange, heterozygosity proximal |
| Chromosome loss (nondisjunction) | 1 for the whole chromosome | LOH along the whole chromosome |
| Loss followed by reduplication | 2 | LOH along the whole chromosome, copy-neutral |

The mechanisms are those of the [aneuploidy](12-nondisjunction-aneuploidy-and-maternal-age.md) and [rearrangement](28-chromosome-rearrangements.md) lessons occurring in a somatic cell, in a division followed by [checkpoint failure](../../cell-biology/modules/12a-cell-cycle-checkpoints-and-mitosis.md) rather than in meiosis.

## Common mistakes

- Calling an inherited tumor suppressor allele dominant at the level of the cell.
- Expecting every carrier of a predisposing allele to develop a tumor; with a Poisson mean of three, about 5% develop none.
- Reading a straight line on a log–log incidence plot as proof that exactly k mutations are required; other processes can produce similar slopes.
- Forgetting that a mutator raises a k-step probability by F^k, not by F.
- Treating loss of heterozygosity as one mechanism; copy number separates deletion and chromosome loss from mitotic recombination and reduplication.

## Worked example

**Problem.** In a synthetic family study, 8% of carriers of an inherited allele never develop a tumor. Assuming tumors arise independently, what is the mean number per carrier, and what fraction have tumors in both eyes if the mean divides equally between them?

**Step 1: mean.** m = −ln 0.08 = 2.53 tumors per carrier.

**Step 2: per eye.** The mean per eye is 1.26, so each eye is tumor-free with probability e^(−1.26) = 0.283.

**Step 3: bilateral.** Both eyes are affected in (1 − 0.283)² = 0.514 of carriers, and one eye in 2 × 0.283 × 0.717 = 0.406.

**Step 4: reading the result.** A lower mean gives more unaffected and unilateral carriers. In a pedigree this is lower penetrance, but the cellular mechanism, two hits with the first inherited, is unchanged.

## Limits of this lesson

All rates, counts and incidence figures are synthetic. The retinoblastoma numbers follow the summary of Knudson's 1971 paper, which was checked for its record and abstract; the 1954 multistage paper was checked for its record and title, but its scanned text was not read for this lesson, which states the model in its standard textbook form. Real incidence curves also reflect exposures, detection and competing causes of death, and a power-law slope does not by itself identify the number or nature of the steps. The lesson describes mechanisms, not the risk to any person or family, and gives no genetic-counselling or medical advice.
