# Phage functional maps: complementation, recombination and suppression

The microbial-transfer lesson asks how DNA moves between cells. A different question is whether two mutations disrupt the same functional unit. A third question is how far apart two DNA changes lie. Phages make these distinctions especially clear: genomes sharing one host can supply products to one another, while recombination can produce a new genome with a new combination of alleles. Growth restored during a mixed infection and a heritable wild-type recombinant are different observations.

This is an inference lesson using fictional counts and stipulated host restrictions. It gives no culture, infection or genetic-engineering procedure. Review the [microbial exchange reading](16-microbial-genetic-exchange-and-complementation.md) and [gene-interaction reading](10-gene-interaction-epistasis-and-complementation.md) first.

## What does the assay observe?

Suppose a permissive host supports either mutant and a restrictive host supports a functional wild-type genotype but not either mutant alone. Under a declared complementation assay, two mutants share a host and the observable is restoration of the missing function in that shared environment. If mutant U lacks product X but supplies Y, and mutant V lacks Y but supplies X, their products can act together. Each genome can retain its original mutation. This is complementation in trans.

For a clean recessive, diffusible-product model, failure to complement suggests mutations in the same functional unit. Complementation supports different units. The interpretation needs controls: each mutant alone, wild type, matched host background and evidence that the assay does not merely amplify rare recombinants. A dominant interfering product, a cis-acting DNA requirement, polar effects on another gene or intragenic complementation can break the simple grouping rule. A negative result is not automatically a physical statement that both lesions occupy the same stretch of DNA.

Consider four fictional mutants with a symmetric result table. A plus means the pair restores the specified function during the shared-host assay; a minus means it does not.

| Pair | Result |
| --- | --- |
| A with B | + |
| A with C | − |
| A with D | + |
| B with C | + |
| B with D | − |
| C with D | + |

Under the simple model, the functional groups are {A,C} and {B,D}. Check every pair against that partition instead of grouping only the first two rows. The table identifies two groups; it does not order A relative to C on a chromosome or prove that their proteins never interact. If a new mutant E failed with A and B but A complemented B, a forced partition would hide a model failure. A deletion spanning two genes is one possible explanation worth testing.

## Recombinants are inherited combinations

Let two parental haploid genomes carry mutations at different sites: one is `a +`, the other `+ b`. A reciprocal exchange between the sites can yield `+ +` and `a b`. On the permissive host all four classes are recoverable under the stipulated equal-recovery model; only `+ +` has the selected wild-type function on the restrictive host. If W counts that one recombinant class out of N total progeny, then

$$\widehat r = \frac{2W}{N}.$$

The factor two accounts for the unobserved reciprocal double-mutant class. It is justified only when that class is equally frequent and comparably viable. If both recombinant classes were measured, use their sum and do not double again. If restrictive and permissive counts come from different sample volumes or dilutions, scale them to the same population before dividing. Here all supplied counts already share the same denominator.

For a short interval, 100r gives approximate map units. This is not a base-pair conversion. Multiple exchanges, unequal recovery, selection and background wild-type contamination can change the estimate. A recombination event can occur between two sites in the same gene, so recombination does not require complementation. Conversely, complementation can restore function without creating a wild-type genome.

## Worked mapping and uncertainty example

A fictional normalized progeny sample contains W=18 wild-type recombinants among N=2400 total progeny. The measured class fraction is 0.0075. With the reciprocal-class assumption, r=0.015, or about 1.50 short-interval map units. Reporting 0.75 map units would omit the second recombinant class; reporting 3.00 would double twice.

For a simple binomial count model on the observed class, let f=W/N. Its approximate standard error is sqrt[f(1−f)/N]. Because r=2f, the standard error of r is twice this value, about 0.00352. This approximation treats counted particles as independent and N as fixed; shared infection ancestry and normalization error may invalidate it. A normal interval is also poor with very small W. If W is zero, the observed count is zero, but the underlying probability need not be zero. The approximate rule-of-three upper bound for the observed class is 3/N; after doubling, the corresponding bound for r is 6/N. It remains a model-based bound, not evidence that an interval contains no DNA.

At a hypothetical second pair with W=6 and N=1200, compute f=0.005, r=0.010 and approximately 1.00 map unit. If zero wild-type progeny were found in a separate N=1500 sample, the rule-of-three bound on total r would be approximately 0.004, or 0.400 map units. Do not substitute that upper bound for an observed distance.

## Reversion and suppression answer different questions

A restored phenotype can arise by precise reversal of the original mutation, another change within the same gene, or an alteration in a different gene that compensates for the defect. The second and third possibilities are intragenic and extragenic suppression. Phenotypic rescue alone cannot identify which happened. A cross or segregation analysis that separates the original lesion from the suppressor can help; sequence evidence answers whether the original base change remains.

For a stipulated coding sequence, an insertion of one nucleotide changes the downstream reading frame. A later deletion of one nucleotide restores the original frame after the second site because the net length change is zero modulo three. The segment between the lesions can still encode different amino acids, contain a stop, or disrupt folding. Restoring frame is therefore weaker evidence than restoring the original protein. A nonsense-suppressor change in a translation component can affect many transcripts and has a different interpretation from repairing one DNA site. Do not infer a general benefit from rescue of one fictional phenotype.

## Build an evidence ledger

For each claim, name the observation, its assumptions and the alternative it leaves open. Shared-host rescue supports functional complementation under the assay model. Recovery of a heritable `+ +` genome supports recombination or another heritable correction and requires background controls. A surviving original lesion plus a second change supports suppression rather than precise reversion. A short recombination interval supports close genetic linkage, not a protein-domain boundary or exact physical separation.

Common errors include using a complementation table as a linear map, forgetting the hidden reciprocal class, calling no observed recombinants a zero distance, and calling a suppressor a repaired original sequence. The [functional-genetics assignment](../assignments/coursework-01-functional-genetics.md) asks for a new table, a differently sized count sample and a report separating these claims.

## Sources and boundaries

MIT OCW [7.03 Genetics, Fall 2004 calendar](https://ocw.mit.edu/courses/7-03-genetics-fall-2004/pages/calendar/) and [lecture-note index](https://ocw.mit.edu/courses/7-03-genetics-fall-2004/pages/lecture-notes/) are link-only scope/concept references for phage fine structure and mutation/suppressor reasoning. The prose, labels, tables and inputs here are original, developed with substantial AI assistance. No source exercise, diagram or experimental procedure was imported. The reciprocal-recovery and binomial assumptions are stipulated. Detailed phage life cycles, deletion mapping, transposition and molecular recombination mechanisms remain outside this selected reading; the course remains partial and unreviewed.
