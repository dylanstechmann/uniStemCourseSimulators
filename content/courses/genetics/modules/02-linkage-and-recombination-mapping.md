# Linkage and recombination mapping

This lesson uses a synthetic two-locus testcross to estimate linkage from progeny. Linkage means that loci on the same chromosome tend to be inherited together; crossing over between them can create recombinant allele combinations. Recombination counts support a relative genetic map, not a direct measurement of DNA length.

## Learning objectives

By the end of this lesson, you should be able to:

1. Estimate recombination frequency from progeny counts.
2. Explain why recombination fraction is a distance proxy with limits.

## Identify parental phase before counting

Write both alleles at each locus on the two homologous chromosome copies. In a coupling (cis) arrangement, the heterozygote is AB/ab, so AB and ab are the parental combinations; Ab and aB are recombinant combinations. In a repulsion (trans) arrangement, the heterozygote is Ab/aB, so Ab and aB are parental, while AB and ab are recombinant. A class is called recombinant by comparing it with the parent's phase, not by whether it looks unusual or rare in isolation.

A testcross pairs the heterozygote with an individual homozygous recessive at both loci (ab/ab). That tester contributes only ab gametes. Under the simple model, each progeny's two-locus class therefore reports which gamete came from the heterozygous parent. This makes the progeny counts useful for estimating the fraction of recombinant gametes. If the tester is not informative or parental phase is unknown, the classes cannot be assigned reliably without additional evidence.

## Calculate the recombination fraction

Let R be the total number of progeny in the recombinant classes and N the total number scored. The sample estimate is:

\[
r=\frac{R}{N}=\frac{\text{recombinant progeny}}{\text{all progeny}}.
\]

For example, suppose a synthetic testcross yields 400 offspring and 72 are recombinant. Then r = 72/400 = 0.18, or 18%. For a sufficiently short interval, the conventional approximation is 1% recombination ≈ 1 centimorgan (cM), so this result is often reported as approximately 18 cM. The percent form of r and the approximate cM distance share the same number only under this short-interval approximation.

The estimate also varies from sample to sample. Treating the progeny as independent Bernoulli observations gives an approximate standard error of sqrt(r(1-r)/N). Here it is sqrt(0.18 × 0.82/400) ≈ 0.019, or about 1.9 percentage points. This describes sampling uncertainty under the model; it does not account for viability differences, scoring errors, or a poor cross design.

## When map units approximate distance

Crossovers between nearby loci are relatively uncommon, so a recombinant endpoint often indicates a crossover within the interval. In that short-interval setting, a recombination fraction of 0.06 is approximately 6 cM. For example, 12 recombinant offspring among 200 scored give r = 12/200 = 0.06 and an approximate distance of 6 cM.

The approximation breaks down as intervals grow. Double crossovers between the loci can restore the original parental arrangement at the endpoints, hiding the events from a two-locus count. The measured recombination fraction therefore undercounts crossover events and tends to underestimate map distance for larger intervals. Recombination fraction is bounded by 0.5: at that value, half the progeny appear recombinant and the two loci assort as if unlinked. A result near 0.5 cannot distinguish loci on different chromosomes from far-separated loci on the same chromosome using only this two-locus cross.

For longer intervals, geneticists use additional markers, multi-point crosses, or map functions that model the relationship between observed recombinant classes and crossover events. Those corrections depend on assumptions about crossover placement and interference. The present two-point calculation estimates a local relationship and should not be stretched into a precise physical distance or a reliable long-range map.

## A short analysis workflow

1. Record the heterozygote's phase and identify its two parental allele combinations.
2. Use the tester genotype or other design information to identify which progeny classes report the heterozygote's gametes.
3. Add the counts for all recombinant classes, then divide by the total number scored.
4. Report r as a fraction or percentage. Convert it to cM only with an explicit short-interval qualification.
5. Check whether the estimate is clearly below 0.5 and discuss sampling and design limitations.

## Common reasoning errors

- Counting the rarest classes as recombinant without first identifying parental phase.
- Dividing recombinant counts by the number of recombinant classes instead of by all scored progeny.
- Reporting 18% recombination as an exact 18 cM physical separation.
- Assuming a measured fraction near 0.5 proves the loci are on different chromosomes.
- Ignoring progeny viability, sampling variation, genotype-scoring error, or an uninformative tester.

## Limits of this lesson

All counts are synthetic. The examples assume correct phase, informative markers, accurate genotype calls, and no segregation distortion or class-specific viability difference. The standard-error calculation additionally treats progeny outcomes as independent binomial observations. A two-locus recombination fraction cannot reveal the number of hidden crossovers, and the short-distance conversion is not a physical-distance scale. These examples teach mapping concepts and say nothing about any real organism or person; the course remains partial, unreviewed, and formative-only.
