# Genomics, association, and variant interpretation

A genome-wide association study (GWAS) tests whether genetic markers covary with a measured trait in a study population. A well-supported association can identify a region worth investigating, but it does not automatically identify the causal variant, explain a mechanism, or predict what will happen to an individual. This lesson uses a synthetic case-control example to connect effect size, uncertainty, population context, and functional evidence.

## Learning objectives

By the end of this lesson, you should be able to:

1. Read an association effect with its uncertainty and population context.
2. Separate statistical association from functional causation.

## Read the effect, not only the p-value

For a binary case-control outcome, a simple 2-by-2 table can summarize the association between a marker and case status. An odds ratio (OR) compares the odds among people with one genotype to the odds among those with another. An OR above 1 means the marker is associated with higher case odds in this sample; it is not a direct measure of absolute probability or risk. For a quantitative trait, a regression coefficient instead describes the expected trait difference per allele under the fitted model and in the model's units.

Consider synthetic counts: among 500 cases, 250 carry a marker allele and 250 do not; among 500 controls, 200 carry it and 300 do not. The estimated OR is (250 × 300)/(250 × 200) = 1.50. A common large-sample standard error for the log OR is sqrt(1/250 + 1/250 + 1/200 + 1/300) ≈ 0.128. The approximate 95% interval is exp(log(1.50) ± 1.96 × 0.128), or about 1.17 to 1.93. Because this interval excludes 1, the synthetic sample is compatible with an association under the simple model. It does not say the marker caused the outcome.

Effect size and uncertainty answer different questions from a p-value. A small p-value can reflect a precisely estimated but modest effect in a large sample. A confidence interval shows the range of effect values reasonably compatible with the model and data; it does not measure the probability that the particular variant is causal. GWAS scan many markers, so the analysis must account for multiple comparisons. A threshold addresses false-positive statistical signals under the chosen testing procedure, not causal mechanism.

## Check population and study context

Association estimates can be distorted if cases and controls differ in ancestry, relatedness, recruitment, or measurement in ways that also correlate with allele frequencies. For example, if two sampled subpopulations differ in both a marker's frequency and the outcome's baseline prevalence, a pooled comparison can show an association even when the marker and outcome are unrelated within each subpopulation. Genetic ancestry and population structure are features of sampled data that require careful modeling; labels alone do not explain biology.

Quality control, appropriate covariates, principal-component or relatedness adjustments, and stratified sensitivity analyses can reduce specific sources of bias. They do not guarantee that every form of confounding has been removed. Replication in an independent, suitably matched cohort helps assess whether the signal is reproducible and whether its effect is similar in the new context. Differences across cohorts can reflect chance, measurement, environment, allele frequency, linkage structure, or genuine context dependence.

## Association points to a region, not necessarily a causal variant

Nearby variants may be inherited together because of linkage disequilibrium (LD). A marker can therefore correlate with a phenotype by tagging a different causal variant on the same haplotype. A significant SNP inside a large LD block supports the conclusion that one or more variants in the region are associated under the study model. It does not, by itself, establish that the reported SNP is causal or that the nearest gene is responsible.

Fine-mapping compares candidate variants using the association data and assumptions about the number of causal signals to form a credible set. A small set narrows the candidates, but each posterior probability is conditional on the model, variant list, and data quality. If the analysis assumes one causal variant when several exist, its ranking can be misleading. The week-14 follow-up lesson develops this step further.

Functional evidence addresses a different layer. A candidate variant may alter expression, splicing, chromatin accessibility, or protein sequence in a particular tissue or cell state. Expression associations and allele-specific measurements can support a molecular consequence but may still point to a linked haplotype. A controlled perturbation of the candidate variant or element, with appropriate controls and a molecular readout, tests whether changing it produces the proposed effect in that model. A perturbation result is strongest when the model matches the biological context and the result is replicated with an independent approach.

## A disciplined interpretation

For a synthetic GWAS result, state the estimated effect and interval, note the study population and model, and say whether the signal replicated. Then identify the region's LD structure and explain what the fine-mapping model can and cannot distinguish. Finally, name the next functional evidence needed to test a proposed mechanism. Keep each claim at its evidence level: association, localization, molecular consequence, and mechanism are related but distinct conclusions.

## Common reasoning errors

- Treating statistical significance as a measure of importance or proof of causality.
- Interpreting an odds ratio as an absolute probability or as the effect of changing the allele.
- Naming the nearest gene as causal without variant-level or functional evidence.
- Ignoring ancestry differences, relatedness, recruitment, or multiple comparisons.
- Assuming replication proves mechanism or that a result transfers unchanged to a different population or tissue.
- Calling a credible set a list of proven causal variants rather than candidates under a specified model.

## Limits of this lesson

All counts are synthetic and have no clinical meaning. The simple OR interval assumes independent observations and a large-sample approximation; real GWAS analyses require models suited to their design, covariates, and sampling. Association and functional evidence can each be biased or context-specific. This lesson does not interpret anyone's genetic data, estimate anyone's risk, recommend treatment, or provide medical advice. The course remains partial, unreviewed, formative-only, and not evidence of semester equivalence.
