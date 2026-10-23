# Selection, inbreeding and linkage likelihood

The [Hardy–Weinberg reading](05-allele-frequencies-and-hardy-weinberg.md) counts alleles and compares genotype proportions at one sampling stage. Population change requires a model connecting stages. A separate linkage question asks how a series of informative transmissions compares with independent assortment. Both problems require normalized probabilities, but their denominators and assumptions differ. This reading develops each model before using fictional examples. It makes no claims about human populations or anyone's genetic risk.

## Follow the life cycle before writing a recurrence

Let q be the frequency of allele a in gametes, p=1−q, and assume random union produces zygotes AA, Aa and aa at frequencies p², 2pq and q². Assign relative survival/reproductive weights wAA, wAa and waa for the transition from those zygotes to the contributing adult gene pool. The unnormalized adult contributions are p²wAA, 2pqwAa and q²waa. Their sum is mean fitness

$$\bar w=p^2w_{AA}+2pqw_{Aa}+q^2w_{aa}.$$

When this sum is positive, normalize each contribution by it. The frequency of a after selection is

$$q_s=\frac{pq w_{Aa}+q^2w_{aa}}{\bar w}.$$

The heterozygote term contributes one a copy per two alleles, which cancels the factor two in its genotype frequency. Leaving out normalization makes the genotype frequencies sum to less than one and confuses loss of individuals with change of frequency. Relative weights may combine survival and reproduction in this ideal model; they are stipulated coefficients, not moral or medical values.

If mutation occurs after selection with probability u for A→a and v for a→A in gamete production, the next generation has

$$q' = q_s(1-v)+(1-q_s)u.$$

Changing the order of mutation and selection changes the exact recurrence. Write the life-cycle order in the report, especially when comparing an approximation with a simulation. Random mating then regenerates the next zygote proportions from q′. In a finite population, sampling produces additional drift that this deterministic recurrence does not include.

## Worked normalized selection example

Take q=0.2, wAA=1, wAa=0.9 and waa=0.6. Initial genotype proportions are 0.64, 0.32 and 0.04. Weighted contributions are 0.64, 0.288 and 0.024, giving mean fitness 0.952. The weighted a-allele contribution is 0.144+0.024=0.168, so qs=0.168/0.952≈0.17647059. For u=0.001 and v=0, q′≈0.17729412. Mutation raises the post-selection frequency slightly; it does not undo the full selective change in this example.

A rehearsal uses q=0.3, weights 1, 0.8 and 0.5, followed by u=0.002 and v=0.001. The genotype contributions are 0.49, 0.336 and 0.045, with sum 0.871. The a contribution is 0.168+0.045=0.213. Compute qs=0.213/0.871 and then q′=0.997qs+0.002. Check all values stay between zero and one and the adult genotype proportions sum to one.

## Mutation–selection balance is an approximation with a boundary

For a fully recessive disadvantage with wAA=wAa=1 and waa=1−s, rare a alleles are mostly sheltered in heterozygotes. Under small u, no back mutation, random mating and a rare-allele approximation, loss is approximately sq² while input is approximately u. Equating these gives q≈sqrt(u/s). If heterozygotes are also selected against with a nonzero dominance parameter h and q is sufficiently rare for the heterozygote term to dominate, the approximation instead scales as q≈u/(hs). Do not apply the recessive square root to a dominant model.

For u=0.000008 and s=0.5, the recessive approximation gives q≈0.004. It is not an exact root of every life-cycle recurrence. Iterate the declared exact recurrence, calculate its residual at that approximation and explain the difference. A measured allele frequency cannot by itself identify mutation input, selective coefficients, migration and demographic history; several processes can produce a similar snapshot. This lesson uses no disease-specific selection estimates or historical population claims.

## Inbreeding changes genotype association before it changes allele counts

In a simple identity-by-descent mixture, two alleles are copies of one ancestral draw with probability F. Otherwise they are independent draws from the allele pool. This gives

$$P(AA)=p^2+Fpq,\quad P(Aa)=2pq(1-F),\quad P(aa)=q^2+Fpq.$$

The three probabilities sum to one and P(aa)+P(Aa)/2=q, so this mating model changes genotype proportions without changing the allele frequency. It increases homozygosity for both alleles, not just one. The F here is a stipulated ancestry-mixture parameter; a heterozygote-deficit statistic from a pooled sample does not uniquely estimate actual ancestry. Population structure, genotyping error and other mechanisms can create a similar deficit.

For q=0.2 and F=0.125, the genotype proportions become 0.66, 0.28 and 0.06. The unchanged allele frequency is 0.06+0.28/2=0.2. For rehearsal q=0.1 and F=0.2, compute 0.828, 0.144 and 0.028. An incorrect approach adds Fq only to aa and leaves the other classes unchanged; its total exceeds one. If selection is then applied, use these actual pre-selection genotype proportions, not the original Hardy–Weinberg ones. Inbreeding can expose recessive effects and thereby alter subsequent selection, even though this mating step alone preserves q.

## Linkage evidence uses informative transmissions

Suppose phase is known in a stipulated cross, each scored meiosis is independent, genotypes are error-free and recombinant versus nonrecombinant transmissions are unambiguous. For R recombinants and NR nonrecombinants, the likelihood at recombination fraction θ is proportional to θ^R(1−θ)^NR. Compare it with independent assortment θ=0.5 using

$$Z(\theta)=\log_{10}\frac{\theta^R(1-\theta)^{NR}}{0.5^{R+NR}}
=R\log_{10}(2\theta)+NR\log_{10}[2(1-\theta)].$$

The common binomial coefficient cancels. With R=2 and NR=18, Z(0.1)≈3.19697. This is evidence comparing two explicitly specified models; it is not a posterior probability that a gene causes a phenotype. A larger positive value favors the proposed θ over 0.5 under the model. Searching over markers or θ, uncertain phase, shared family structure, incomplete penetrance and genotyping errors complicate interpretation. Conventional evidence thresholds are not a guarantee of causality or a substitute for a declared analysis plan.

For R=3 and NR=17, the constrained likelihood is maximized at θ=R/(R+NR)=0.15; evaluate Z there. If an observed fraction exceeds 0.5, the constrained model's maximum is at 0.5 rather than an allowed map fraction greater than one half. Computing the log likelihood directly avoids underflow from multiplying many small probabilities. At θ=0 or 1, handle zero exponents and impossible observations explicitly instead of taking an undefined logarithm in code.

## Work across the models

The [population/linkage assignment](../assignments/coursework-03-population-and-linkage.md) asks for a declared life cycle, exact iteration, approximation comparison, genotype conservation check and separate linkage likelihood calculation. Keep the models separate: a population allele frequency is not a recombination fraction, mean fitness is not a likelihood, and a linkage log ratio is not an expression effect size.

MIT OCW [7.03 Genetics, Fall 2004 calendar](https://ocw.mit.edu/courses/7-03-genetics-fall-2004/pages/calendar/) and [lecture-note index](https://ocw.mit.edu/courses/7-03-genetics-fall-2004/pages/lecture-notes/) are link-only references for mutation/selection, inbreeding and linkage evaluation scope. Derivations and all inputs here are original, developed with substantial AI assistance; no source exercise, disease example or dataset was imported. These idealized one-locus and known-phase models omit drift, migration, multi-locus interactions and real pedigree ascertainment. Workload and qualified review remain open; the course remains partial and unreviewed.
