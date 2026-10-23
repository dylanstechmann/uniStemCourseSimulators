# Assignment 2: a genome and transcript evidence dossier

Use the [genome-structure reading](../modules/genome-structure-and-allelic-evidence.md), [controlled-perturbation lesson](../modules/08-designing-a-controlled-perturbation-experiment.md) and [expression-normalization lesson](../modules/14-measuring-gene-expression-normalization-and-false-discoveries.md) to compare competing explanations for an allelic signal. The dataset is synthetic and concerns no person. Produce a locally saved calculation table, causal diagram and proposed discriminating study. Browser checkpoints cover selected arithmetic and interpretations; they do not evaluate your report or establish a mechanism.

## Supplied model and counts

A fictional diploid-derived cell line has a duplicated genomic segment. A marker within it distinguishes homolog labels A and B. The following original table is available as [genome-evidence-counts.csv](genome-evidence-counts.csv). Each clone label identifies one independently maintained lineage for this teaching model. DNA and RNA counts measure alleles at the same marker. Junction counts come from a separate, stipulated two-isoform assay with equal detection probability and one informative count per mature molecule. Do not combine the two library totals.

| Clone | DNA A | DNA B | RNA A | RNA B | Included junction | Skipped junction |
| --- | --- | --- | --- | --- | --- | --- |
| C1 | 160 | 80 | 120 | 120 | 63 | 27 |
| C2 | 180 | 90 | 140 | 140 | 70 | 30 |
| C3 | 200 | 100 | 150 | 150 | 77 | 33 |

For this problem assume the DNA ratio accurately reflects dosage, marker mapping is unbiased, and samples have no contaminating cell population. The A-bearing segment has two genomic copies and B one. The included transcript contains 420 coding nucleotides; the skipped form omits a 90-nucleotide coding exon. The annotation is stipulated to be correct with complete codons across the supplied coding boundaries. These assumptions isolate the calculation; your study design must explain how real evidence would test them.

## Build the quantitative ledger

For each clone calculate DNA A fraction, RNA A fraction, raw RNA A:B odds and RNA odds normalized by DNA odds. Label the last quantity as an RNA-per-genomic-copy contrast. Explain why a raw 1:1 RNA signal does not imply equal expression per copy. Calculate these values per clone before pooling anything. State the unit of replication and why hundreds of reads are not hundreds of independent clones.

Next calculate the included-junction fraction separately for each clone. From the coding annotation, determine the skipped-form coding length, number of omitted codons and downstream frame-preservation result. Compute the abundance-weighted expected coding length under the two-isoform model. Explain why that expectation is not the length of a real fractional transcript and why preserving frame does not establish protein function.

Make a second table that tracks denominators: genomic allele copies, allele-informative DNA reads, allele-informative RNA reads, junction-informative RNA reads and clone count. At least three different denominators occur here. A ratio may be arithmetically correct yet answer the wrong biological question if its denominator changes silently.

## Challenge a mechanism claim

A fictional analyst concludes, “The A allele is normal because the RNA fraction is one half, and skipping cannot matter because the frame is retained.” Write a response using the calculated per-copy contrast and the actual scope of the frame calculation. Identify observations needed to connect DNA dosage, RNA regulation, splice choice, protein output and the scored cellular phenotype. Distinguish what the current data support from what they leave open. The table has no allele-resolved junction counts, so it cannot assign the skipping event to A or B.

Draw a causal diagram including candidate sequence, DNA dosage, transcript processing, RNA stability, protein function, clone history and cell-state composition. Choose two competing explanations that fit the supplied table. Design a follow-up comparison that would distinguish them. Consider matched DNA/RNA assays, phase-resolved junctions, independent edited/sham clones, reciprocal changes and a rescue with appropriate endogenous dosage. Explain one limitation of a reporter assay outside native chromatin. Do not write a laboratory protocol; specify the inferential comparison and endpoints.

## Self-review values and sensitivity work

All three clones have DNA A fraction 2/3, RNA A fraction 1/2 and normalized allelic odds R=0.5. All have inclusion fraction 0.7. The omitted coding segment contains 30 codons; the skipped form has 330 coding nucleotides and the average is 0.7×420+0.3×330=393 nucleotides. These exact common ratios were chosen for transparent checks and do not represent real replicate variability.

Recompute clone C1 if the RNA A count were 96 instead of 120 while DNA and B counts stay fixed. Recompute inclusion if ten included junction counts were misclassified as skipped. Then discuss what kinds of uncertainty these sensitivity changes illustrate and what they cannot estimate. Arbitrary perturbations are not confidence intervals. Pooling clones increases counts but can hide lineage effects; demonstrate the difference between a read-weighted pooled fraction and equal-weight averaging using an additional hypothetical clone with a different ratio.

## Completion standard and provenance

Your dossier should contain reproducible calculations, a copy/transcript/protein evidence ladder, explicit missing measurements, a causal diagram and a study whose possible outcomes separate at least two hypotheses. Include a short audit of mapping, phase and clone assumptions. A list of methods without a predicted contrasting outcome is insufficient. Any real peer feedback or human review must be identified honestly rather than inferred from passing browser items.

The assignment, counts and targets are original, developed with substantial AI assistance. The [MIT OCW 7.03 Fall 2004 calendar](https://ocw.mit.edu/courses/7-03-genetics-fall-2004/pages/calendar/) is a link-only scope comparator; no university sequence, problem or dataset was imported. This open practice supplies no validated assay, clinical inference or experimentally confirmed mechanism. The package remains partial and unreviewed, with workload and qualified review still open.
