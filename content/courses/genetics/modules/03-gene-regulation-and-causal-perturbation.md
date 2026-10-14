# Gene regulation and causal perturbation

Gene-expression evidence can show that a sequence is associated with a trait without proving that the sequence caused the trait. This lesson uses synthetic allele-specific expression and perturbation examples to separate regulatory hypotheses from causal conclusions. It focuses on reasoning and experimental design, not on a laboratory protocol.

## Learning objectives

By the end of this lesson, you should be able to:

1. Interpret cis-regulatory and trans-acting effects.
2. Choose perturbations that distinguish correlation from mechanism.

## Cis and trans describe where an effect acts

A cis-regulatory element acts on the same DNA molecule as the sequence that contains it. Promoters and enhancers are common cis-regulatory elements: sequence differences can alter the transcription of a linked allele. A trans-acting regulator is a diffusible product, such as a transcription factor or regulatory RNA, that can influence targets on either homolog and at multiple genomic locations. “Cis” and “trans” describe the relationship between the regulator and its target; they do not, by themselves, identify a variant as causal.

Allele-specific expression can help distinguish these models. In a heterozygous cell, both alleles share most of the same trans environment. If one allele contributes fewer RNA molecules than the other, that imbalance supports a cis-linked effect. Equal expression does not rule out every cis effect, and imbalance can also arise from imprinting, allele-specific chromatin, mapping bias, or technical noise. Calibrating RNA allelic counts against genomic DNA and using appropriate controls helps identify technical bias. Even a validated imbalance localizes an effect to a haplotype; it does not necessarily identify the causal nucleotide.

## Synthetic example: an allelic imbalance

Suppose a synthetic heterozygous cell sample has 100 normalized RNA reads from a reference-linked allele and 60 from an alternate-linked allele at a transcribed marker. Matched genomic DNA reads are balanced at 100 and 100, so a simple DNA calibration does not explain the RNA imbalance. The alternate-to-reference RNA ratio is 60/100 = 0.60. Since both alleles are measured in the same trans environment, this pattern supports a cis-linked regulatory difference in this sample.

That observation does not establish that the nearby variant caused the difference. Another linked change on the same haplotype, allele-specific epigenetic regulation, or an unrecognized measurement artifact could explain it. A population-level expression association can likewise arise because a marker tags a causal variant through linkage disequilibrium. Stronger evidence requires a perturbation that changes the candidate sequence or regulatory element while holding the surrounding genetic background as constant as practical.

## Choose a perturbation that tests the hypothesis

The appropriate intervention depends on the proposed mechanism. If a promoter or enhancer allele is suspected, a precise edit or a targeted repression of that element can test whether changing it alters the target transcript. If the hypothesis concerns a diffusible regulator, changing the regulator's abundance or activity can test whether target expression responds. A reporter construct can compare candidate sequences in a controlled context, but it may omit native chromatin, genomic distance, and enhancer–promoter contacts; reporter activity alone cannot establish how the element works at its endogenous locus.

CRISPR interference (CRISPRi) uses a catalytically inactive Cas protein to target a regulatory region and reduce transcription without making a DNA cut. A deletion or knockout asks a different question and can disrupt neighboring elements or coding sequence. These tools are not interchangeable: one reduces activity, another removes sequence, and each can affect additional targets or local chromatin. Select the perturbation and readout from the biological hypothesis, and interpret the result in the tested cell type and context.

## Controls and an evidence ladder

A useful design compares the candidate perturbation with a matched control in the same genetic background and cellular context. Independent guides or independently derived edits can reveal sequence-specific off-target effects or clone-specific behavior. A non-targeting guide or sham edit controls for delivery and handling effects. Confirm that the intended sequence or regulator changed, and measure the predicted molecular readout as well as the relevant phenotype. When feasible, a rescue provides a second test: restoring the missing gene product or regulatory activity should reverse the phenotype if the loss caused it.

Consider a synthetic example in which a promoter edit reduces target RNA and protein and changes a cell-state readout. An independently designed edit that produces the same pattern strengthens the result. If a promoter-independent, edit-resistant cDNA restores protein and the readout, the rescue supports a causal link between reduced gene product and phenotype. It does not prove that the candidate promoter variant is the only causal sequence, that the effect is direct, or that the same mechanism operates in another cell type or organism. A rescue can also mislead if the added product is expressed at an unrealistic level, so the size and context of the restoration matter.

The evidence ladder therefore has several steps: an association nominates a region; allele-specific or expression measurements connect the region to a molecular phenotype; targeted perturbation tests whether changing the candidate element changes that phenotype; and an independent perturbation or rescue checks specificity. Each step answers a different question. Repeating an association or obtaining a smaller p-value can strengthen evidence that a locus is associated, but does not substitute for testing the mechanism.

## Common reasoning errors

- Calling every promoter or enhancer association a proven causal variant.
- Treating allele-specific expression as proof of the exact nucleotide rather than evidence about a linked haplotype.
- Assuming a trans regulator must affect every allele equally, even when target sequences differ in responsiveness.
- Treating reporter activity as proof of native genomic regulation.
- Calling a rescue definitive when expression is far above the normal range or the perturbation has not been confirmed.
- Generalizing a result from one cell type or model to every tissue or organism.

## Limits of this lesson

All read counts and examples are synthetic. Gene regulation is context-dependent, and allele-specific measurements, targeted perturbations, and rescues each have distinct assumptions and failure modes. The lesson does not prescribe experimental procedures, claim that a particular variant causes a human trait, or provide medical advice. The course remains partial, unreviewed, formative-only, and not evidence of semester equivalence.
