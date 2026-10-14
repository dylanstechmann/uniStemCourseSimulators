# Reading an aging-intervention paper: design, power and what a result is worth

Claims about slowing aging come with a headline, a graph and a p-value. Whether to believe the claim depends on design details that are easy to skip: how many animals, whether the analysis was planned, what else was measured and whether the result held in both sexes. This lesson turns those details into a checklist and practices the arithmetic that two of them need.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute a per-group sample size for a two-group comparison from a standardized effect size and state its assumptions.
2. Evaluate a summary of a lifespan or healthspan study for multiplicity, sex and strain, blinding and endpoint choice.
3. Distinguish statistical significance, effect size and importance when reporting an intervention effect.
4. Compare the mechanistic reach and measured outcomes of distinct mouse longevity interventions without treating them as a head-to-head trial or evidence of human benefit.

## A checklist for a lifespan or healthspan study

- **A primary endpoint stated in advance.** If the paper tested many outcomes and reports the ones that worked, the first question is what the pre-specified endpoint was.
- **Randomization and blinding.** Animals assigned by a random process, and outcome assessors who do not know the group, reduce bias in subjective measures such as frailty scores.
- **Sample size chosen for a purpose.** A study that is too small misses real effects and exaggerates the ones it finds.
- **Both sexes, and more than one genetic background.** Effects of interventions often differ by sex and strain. A multi-site design with genetically heterogeneous animals, as used by the Interventions Testing Program, tests whether a result holds across sites and backgrounds.
- **Control animals that are fair.** Free-fed controls may be shortened by obesity; husbandry, diet and housing should be matched.
- **Appropriate survival analysis.** Animals that die accidentally or are removed are *censored*, not counted as deaths; analysis should use methods that handle censoring (see the time-to-event lesson in the statistics package).
- **Effect sizes with intervals,** not only a p-value.
- **Replication.** One lab, one cohort and one result is a hypothesis.

## Sample size for a two-group comparison

For a comparison of two group means with a standardized effect size *d* (the difference divided by the standard deviation), a two-sided significance level α and a power 1 − β, a common normal-approximation formula gives the number of animals per group:

**n = 2 (z₁₋α/₂ + z₁₋β)² / d²**

With α = 0.05 (z = 1.96) and power 80% (z = 0.84), (z + z)² = 7.84, so n = 15.68 / d². The size of the standardized effect dominates: halving *d* quadruples *n*. For d = 0.5, n = 62.7, rounded up to 63 per group. For d = 0.8, n = 24.5, rounded up to 25. The formula assumes roughly normal outcomes, equal groups and a known standard deviation; it is a planning approximation, not a guarantee. Lifespan outcomes are usually analyzed with survival methods, which need different calculations based on expected numbers of deaths.

## Multiplicity: many endpoints, one headline

If a study tests *k* independent endpoints each at α = 0.05 and no true effect exists, the probability of at least one false positive is 1 − (1 − α)^k. For k = 12 that is 0.460, close to a coin flip. Healthspan studies often measure grip strength, gait, glucose tolerance, cognition, body composition and more. Honest reporting names a primary endpoint, treats the rest as secondary or exploratory, and either adjusts for multiple comparisons or says that it did not.

## Significance, size and importance

A small p-value says that data like these would be unusual if there were no effect under the model; it does not say the effect is large or important. A large study can find a statistically significant effect that is too small to matter, and a small study can find a large effect with an interval so wide that it includes no effect. Report the estimate and its interval, say what size of effect would matter for the purpose, and compare the two.

## Comparative evidence case: targeted cell clearance and rapamycin

Two published mouse studies illustrate how different interventions can produce survival evidence while supporting different mechanistic claims. This comparison is a reading exercise; the studies did not compare their interventions directly.

| Feature | Baker et al. (2016) | Harrison et al. (2009) |
|---|---|---|
| Intervention | Inducible INK-ATTAC clearance of p16(Ink4a)-expressing cells, activated with AP20187 twice weekly from one year of age | Rapamycin supplied in food from 600 days of age |
| Model and comparison | Wild-type mice carrying the clearance system, compared with vehicle; two genetic backgrounds and both sexes were included | Genetically heterogeneous UM-HET3 mice, compared with control food at three testing sites; both sexes were included |
| Reported outcomes | Median lifespan increased in males and females; clearance also delayed tumorigenesis and preserved measures of function in several organs | Median and maximal lifespan increased in both sexes; age at 90% mortality increased 14% in females and 9% in males |
| Strongest local inference | Removing cells reached by this p16-driven genetic tool can change lifespan and age-related phenotypes in these mouse settings | Late-life dietary rapamycin can change survival in this heterogeneous mouse population |

The first design has more direct leverage on whether a p16-driven cell population contributes to the measured mouse phenotypes, but the promoter does not label every senescent cell and clearance is incomplete and tissue-selective. The second uses a drug that inhibits mTOR signaling, but target engagement plus a survival effect does not show which downstream process mediated the effect. The paper discusses delaying cancer, changing aging mechanisms, or both as possible explanations. The endpoints also differ: Baker et al. report organ-function measures as well as lifespan, while the 14% and 9% figures in Harrison et al. refer specifically to age at 90% mortality, not a percentage reduction in hazard or a human effect.

Do not rank the two interventions by these percentages. The ages, models, background structure, interventions and survival summaries differ, and there was no shared protocol or head-to-head allocation. Both papers support bounded claims about mice; neither establishes a human anti-aging benefit. Their results motivate different follow-up questions: whether the p16-driven cell subset is necessary for a specific phenotype, and which mTOR-dependent or independent processes account for rapamycin's survival effect.

Primary studies: [Baker et al. (2016)](https://pubmed.ncbi.nlm.nih.gov/26840489/) and [Harrison et al. (2009)](https://pubmed.ncbi.nlm.nih.gov/19587680/). MIT OpenCourseWare [2.787J syllabus](https://ocw.mit.edu/courses/2-787j-tissue-engineering-and-organ-regeneration-fall-2024/pages/syllabus/) and [calendar](https://ocw.mit.edu/courses/2-787j-tissue-engineering-and-organ-regeneration-fall-2024/pages/calendar/), Fall 2024, describe a graduate course on tissue engineering and organ regeneration. Its scope includes regeneration and aging-associated impediments, so it is a selective comparator for this package's regeneration unit rather than a full geroscience match. The evidence comparison here is original and uses link-only primary studies; it does not reproduce the MIT course.

## Synthetic example

A hypothetical paper reports that a compound "improves healthspan in mice" with p = 0.03 for grip strength. The methods list twelve healthspan endpoints, no stated primary endpoint, males only, one strain, and ten animals per group. Reading against the checklist: multiplicity is unaddressed (twelve endpoints), the p-value for one is not convincing evidence of an effect on healthspan, sex and strain are limited, and ten animals per group would detect only a very large standardized effect.

## Common mistakes

- Accepting one p-value among many endpoints as a finding, when the chance of at least one false positive is 1 − (1 − α)^k.
- Equating a small p-value with a large or important effect.
- Using the normal-approximation sample-size formula for lifespan outcomes that need survival methods.
- Forgetting that halving the standardized effect quadruples the sample size.
- Overlooking sex and strain limitations, or controls that are not fair.
- Counting censored animals as deaths.
- Comparing effect percentages from unlike studies as though they came from one randomized experiment.
- Treating target engagement or a survival benefit as proof of the mechanism that produced it.

## Worked example

To detect d = 0.5 with 80% power at α = 0.05, n = 2 × (1.96 + 0.84)² / 0.5² = 62.72, so 63 animals per group. With ten per group the study can detect only effects of about d = 1.3 or larger. For twelve independent endpoints at α = 0.05 each, the chance of at least one false positive with no true effects is 1 − 0.95¹² = 0.460.

## Limits of this lesson

The worked paper is synthetic; Baker et al. and Harrison et al. are linked primary references summarized in original wording. The lesson gives planning arithmetic, not advice about any product or practice, and the sample-size formula is a normal-approximation sketch for two-group means.
