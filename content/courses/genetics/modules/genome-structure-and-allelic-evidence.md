# Genome structure, transcript processing and allelic evidence

An association marker can identify a region without identifying the functional change. Before proposing a mechanism, decide what kind of object each assay measures: DNA copy number, RNA abundance, transcript structure, protein activity or phenotype. These quantities are connected, but none can freely substitute for another. This reading develops an original evidence problem in a fictional diploid cell line. It extends [cis/trans regulation](03-gene-regulation-and-causal-perturbation.md) and [expression normalization](14-measuring-gene-expression-normalization-and-false-discoveries.md); those readings supply experimental-unit and normalization prerequisites.

## A locus contains more than a coding interval

A eukaryotic locus can contain a promoter, regulatory elements, transcribed untranslated regions, introns and exons contributing to coding sequence. A primary RNA transcript is processed into mature RNA. Alternative splice choices can change which exon junctions appear without changing the DNA sequence or total number of RNA molecules. A sequence variant may alter protein sequence, transcript processing, RNA stability or regulation, depending on its location and context. Position alone does not prove its effect.

Consider a stipulated transcript with three coding exons of 120, 81 and 150 nucleotides, with complete codons aligned across their boundaries. The included coding segment contains 351 nucleotides. Skipping the middle 81-nucleotide exon removes 27 codons and preserves the downstream frame because 81 is divisible by three. It does not guarantee that the shortened protein folds or functions. If instead the omitted coding segment were 80 nucleotides, the net deletion would not preserve the downstream frame. This arithmetic assumes the supplied annotation, coding boundaries and splice products are correct; real transcript annotations and decay pathways require evidence. Do not divide an entire RNA length by three when untranslated regions are included.

## Copy number and allele dosage

At a heterozygous marker, alleles A and B may initially have one genomic copy each. A duplication of the A-bearing segment can produce dosage A:A:B. Under equal DNA sampling and mapping, the expected A fraction is then 2/3. An A RNA fraction of 2/3 could simply reflect equal expression per copy. Calling that a twofold regulatory effect from a 1:1 baseline would confuse dosage with expression per copy.

Read depth alone does not uniquely determine copy number. It depends on library normalization, GC composition, mappability, local repeats, sample mixture and the reference. A heterozygous base fraction adds information, but allele-specific alignment bias can imitate imbalance. Phase also matters: if two variants are on the same homolog they are in cis; if on opposite homologs they are in trans. Two heterozygous calls do not reveal which arrangement is present. Distinguishing a regulatory variant from a linked coding change requires phase-aware evidence and functional comparisons.

## Normalize RNA allelic odds by DNA allelic odds

For a simple teaching model, define allelic expression per genomic copy by

$$R = \frac{\mathrm{RNA}_A/\mathrm{RNA}_B}{\mathrm{DNA}_A/\mathrm{DNA}_B}.$$

This is a ratio of odds, not a ratio of allele fractions. Assume the DNA counts represent genomic dosage and that mapping biases are absent or cancel appropriately between the matched assays. R=1 means equal measured RNA per genomic allele copy under those assumptions. It does not prove identical transcription rates: RNA stability and processing also affect abundance. R below one indicates reduced measured A RNA per copy relative to B; it does not by itself locate the causal variant.

In a worked synthetic sample, DNA counts are A=120 and B=60; RNA counts are A=90 and B=90. DNA A fraction is 2/3, RNA A fraction is 1/2, and R=(90/90)/(120/60)=0.5. The raw RNA ratio is one, but expression per genomic copy is imbalanced. Repeated sequencing of that same library adds technical reads, not independent biological replicates. Three independently maintained clones may be closer to biological replication, but shared origin and culture effects still need an explicit design.

For a separate rehearsal, DNA A=150 and B=100; RNA A=60 and B=80. The DNA A fraction is 0.6, RNA A fraction is 3/7 and R=(60/80)/(150/100)=0.5. Dividing the fractions, (3/7)/0.6, gives about 0.714 and answers a different question. Use the defined odds ratio when the scientific estimand is RNA per genomic copy.

## Junction evidence tests transcript structure

Suppose a stipulated, bias-free junction assay has only two possible mature isoforms. The included form carries junction E1–E2; the skipped form carries junction E1–E3. Each molecule contributes one informative junction count with equal probability. If 72 counts support inclusion and 24 support skipping, the estimated inclusion fraction is 72/(72+24)=0.75. The denominator is the informative included-plus-skipped count, not all reads in the library. In real assays the two junctions can have unequal detection probabilities and additional isoforms; the simple estimate then needs correction or a different model.

The expected coding length averaged across these two forms is 0.75×351+0.25×270=330.75 nucleotides. This is an expectation over different molecules, not the sequence length of a fractional transcript. An abundance-weighted average cannot tell whether the shorter isoform is translated, stable or functional. With 54 included and 36 skipped counts in a rehearsal, inclusion is 0.6. If the included coding region is 300 nucleotides and the skipped coding exon is 60, the expected coding length is 276 nucleotides under the same two-isoform model.

## A causal design connects several evidence layers

Start by drawing the competing explanations. DNA duplication could change dosage; a cis change could affect RNA per copy; a splice change could alter junction use; cell-state composition could alter several genes simultaneously. Then choose comparisons that separate them. Matched DNA and RNA counts address dosage versus per-copy abundance. A phase-resolved marker can connect a splice product to one homolog. Multiple independent edited and sham-control clones, reciprocal allele changes and rescue comparisons can help distinguish a candidate variant from clonal artifacts. A reporter may isolate one regulatory segment but omit native chromatin and long-range context.

The strongest conclusion must match the endpoints. A change in RNA abundance after a controlled edit supports an effect on measured RNA in that cell model. It does not establish a particular protein activity or an organism-level phenotype. A rescue is stronger when it restores the relevant endogenous dosage and timing; overexpression can bypass the original defect. An absence of an observed difference can also reflect insensitive measurement or the wrong cell state. Report uncertainty and viable alternatives rather than translating an assay label directly into a mechanism.

## Practice and limits

Before opening feedback, reconstruct the two-isoform denominator, calculate genomic and RNA allele fractions, then normalize the allelic odds. List a control for mapping bias, a control for clone effects and an assay for the claimed downstream function. Explain why preserving a reading frame is insufficient evidence for normal protein function. The [genome-evidence assignment](../assignments/coursework-02-genome-evidence.md) supplies distinct copy/expression/junction counts and requires a causal diagram and discriminating follow-up.

MIT OCW [7.03 Genetics, Fall 2004 calendar](https://ocw.mit.edu/courses/7-03-genetics-fall-2004/pages/calendar/) and [lecture-note index](https://ocw.mit.edu/courses/7-03-genetics-fall-2004/pages/lecture-notes/) provide link-only scope references for gene structure and eukaryotic genome reasoning. This original reading uses no source sequence, dataset, problem or figure and was developed with substantial AI assistance. Full genome assembly, repeat annotation, chromatin models, gene targeting and cancer genetics remain incomplete. All counts are fictional, assumptions are simplified, and no result concerns a person or clinical interpretation. The package remains partial and unreviewed.
