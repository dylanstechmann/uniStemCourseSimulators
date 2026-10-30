# Genetics & Genomics scope crosswalk

This crosswalk compares the local package, version 0.9.0, with two published genetics courses: MIT OpenCourseWare 7.03 Genetics, Fall 2004 ([calendar](https://ocw.mit.edu/courses/7-03-genetics-fall-2004/pages/calendar/), 35 lectures), and Columbia University BIOL UN3031/GR5031 Genetics, Spring 2023 ([lecture and assignment schedule](https://biology.columbia.edu/sites/default/files/content/Syllabi/UN3031%20Genetics%20Sp23.pdf), 24 lectures in four units). It was compiled with AI assistance on 2026-10-30 from the lecture titles and the local readings and practice. It is an agent-run comparison, not a review by the owner or by a genetics instructor. It does not compare lecture content beyond those titles, problem sets, exams or workload, and topic alignment establishes no equivalence, credit or endorsement.

Two scope notes apply. MIT 7.03 is the closer match in sequence and gives seven lectures (25–31) to population, human and statistical genetics, against about two at Columbia. Columbia UN3031 spends a unit on genetic approaches to biological problems (allelic classes, screens, mosaics and pathways), which widens the topic list toward model-organism genetics. Status labels: **covered** means a local reading develops the topic with a worked example and practice; **shallow** means a local reading teaches part of the topic; **absent** means no local instruction; **local extension** means the package teaches a topic neither comparator names. Local numbers are lesson IDs (genetics-N), and each links to its reading.

## Comparator map

| Topic | MIT 7.03 | Columbia UN3031 | Local lessons | Status |
| --- | --- | --- | --- | --- |
| Mendelian inheritance, probability and penetrance | Lec 3–4 | Lec 1 | [1](modules/01-segregation-penetrance-and-probability.md) | Covered |
| Complementation, Mendelian extensions, epistasis and pathway order | Lec 2 | Lec 2, 21–22 | [10](modules/10-gene-interaction-epistasis-and-complementation.md) | Covered, including the ordering of genes in a pathway by double mutants |
| Sex linkage, chromosome theory and pedigrees | Lec 4–5 | Lec 3, 9–10 | [11](modules/11-sex-linkage-pedigrees-and-bayesian-carrier-risk.md) | Covered |
| Linkage, recombination maps and three-factor crosses | Lec 6–7 | Lec 4 | [2](modules/02-linkage-and-recombination-mapping.md), [7](modules/07-three-point-mapping-and-interference.md) | Covered |
| Tetrad analysis and mapping in fungi | Lec 8 | Lec 5 | [7](modules/07-three-point-mapping-and-interference.md), [18](modules/18-ordered-tetrads-and-centromere-mapping.md) | Covered |
| Mechanism of homologous recombination | — | Lec 6 | [18](modules/18-ordered-tetrads-and-centromere-mapping.md) | Shallow: gene conversion is named; the molecular mechanism is not developed |
| Nondisjunction and aneuploidy | Lec 32–33 (Chromosome Anomalies) | Lec 6–7 | [12](modules/12-nondisjunction-aneuploidy-and-maternal-age.md) | Covered |
| Chromosome rearrangements | Lec 32–33 (Chromosome Anomalies) | Lec 7–9 (Rearrangements in model systems and humans) | [28](modules/28-chromosome-rearrangements.md) | Covered in 0.9.0; previously absent |
| Population genetics | Lec 25–27 | Lec 11–12 | [5](modules/05-allele-frequencies-and-hardy-weinberg.md), [21](modules/selection-inbreeding-and-linkage-likelihood.md) | Covered for one-locus deterministic models; drift is named but not modelled |
| Statistical evaluation of linkage and positional cloning | Lec 29–30 | Lec 11 | [21](modules/selection-inbreeding-and-linkage-likelihood.md) | Covered for known-phase LOD scores; positional cloning is absent |
| Human polymorphisms, complex traits and association | Lec 28, 31 | — | [4](modules/04-genomics-association-and-variant-interpretation.md), [6](modules/06-heritability-and-polygenic-scores.md), the [association lab](labs/01-association-study-and-population-structure.md) | Covered |
| Bacterial and phage genetics, transposition | Lec 9, 12–15 | Lec 13 | [16](modules/16-microbial-genetic-exchange-and-complementation.md), [19](modules/phage-functional-maps.md), [25](modules/25-transposable-elements-and-insertion-mutagenesis.md) | Covered |
| Mutation mechanisms, mutation types and suppressors | Lec 11 (Mutations and Suppressors) | Lec 14 | [13](modules/13-mutation-rates-fluctuation-test-and-somatic-mutation.md), [19](modules/phage-functional-maps.md) | Shallow: mutation rates, the fluctuation test and frameshift reversion are taught; chemical mechanisms and classes of mutation are not |
| The genetic code | — | Lec 15 | [20](modules/genome-structure-and-allelic-evidence.md) | Shallow: codons and reading frame are used; the experiments that established the code are not taught |
| Prokaryotic regulation and bacterial defense systems | Lec 16–18 | Lec 16 | [17](modules/17-prokaryotic-regulatory-circuits.md) | Covered for operon circuits; bacterial defense systems are absent |
| Eukaryotic genes, genomes and expression | Lec 19–22 | Lec 10 (the human genome), 16 | [3](modules/03-gene-regulation-and-causal-perturbation.md), [14](modules/14-measuring-gene-expression-normalization-and-false-discoveries.md), [20](modules/genome-structure-and-allelic-evidence.md) | Covered |
| Transgenes, gene targeting, genome editing and conditional alleles | Lec 23–24 | Lec 17, 20 | [26](modules/26-transgenes-and-homologous-gene-targeting.md), [8](modules/08-designing-a-controlled-perturbation-experiment.md) | Covered |
| Muller's allelic classes | — | Lec 18 | — | Absent |
| Genetic screens | — | Lec 19 | [25](modules/25-transposable-elements-and-insertion-mutagenesis.md) | Shallow: insertion-mutagenesis coverage is quantified; the design of a forward screen is not taught |
| Genetic mosaic analysis | — | Lec 20 | [11](modules/11-sex-linkage-pedigrees-and-bayesian-carrier-risk.md), [26](modules/26-transgenes-and-homologous-gene-targeting.md) | Shallow: X-inactivation mosaics and chimeras are described; clonal analysis is absent |
| Small RNAs and reverse genetics | — | Lec 23 | [8](modules/08-designing-a-controlled-perturbation-experiment.md) | Shallow: RNA interference is taught as a perturbation tool with controls; small-RNA pathway biology is absent |
| Genetics of cancer | Lec 34–35 | Lec 24 | [29](modules/29-genetics-of-cancer-two-hits-and-age.md), [13](modules/13-mutation-rates-fluctuation-test-and-somatic-mutation.md) | Covered in 0.9.0; previously named only in passing |
| Mendelian randomization and locus follow-up | — | — | [9](modules/09-mendelian-randomization.md), [15](modules/15-from-association-to-mechanism-follow-up-design.md) | Local extension (optional) |
| Problem sets and exams | Six problem sets, three quizzes and a final | Graded problem-solving assignments, ungraded problem sets and four exams | Open practice and four ungraded assignments | Absent by design: all practice is ungraded and formative-only |

## What 0.9.0 changed

Both comparators teach chromosome rearrangements and the genetics of cancer, and the package had neither as a reading. The aneuploidy lesson covered whole-chromosome errors only, and cancer appeared only in passing in the transposition and genome lessons. A new week-6 reading, lesson 28, follows the aneuploidy lesson. It classifies deletions, duplications, inversions and translocations, maps a recessive mutation by pseudodominance over overlapping deletions, derives unequal crossing over, traces inversion-loop crossovers to their unbalanced products, computes translocation semisterility and pseudolinkage, and reads copy number and mosaic fraction from log₂ ratios. A new week-8 reading, lesson 29, follows the somatic-mutation lesson. It separates oncogenes from tumor suppressors, works Knudson's two-hit argument with Poisson statistics, relates the slope of log incidence against log age to the number of steps in the multistage model, quantifies mutators and clonal expansion, and distinguishes the routes to loss of heterozygosity. Together they add eight objectives, 24 practice items and eight retrieval cards.

## Remaining gaps

- Mechanisms and classes of mutation, Muller's allelic classes and the design of forward genetic screens (Columbia Lec 14, 18–19; MIT Lec 11).
- Genetic mosaic analysis and the biology of small-RNA pathways (Columbia Lec 20, 23).
- The molecular mechanism of homologous recombination and positional cloning (Columbia Lec 6, 11).
- Bacterial defense systems and the experiments that established the genetic code (Columbia Lec 15–16).
- Drift and multi-locus population models, and cancer genomics beyond the two-hit, multistage and loss-of-heterozygosity foundations.
- Graded homework and exams, measured workload, and review by a qualified person.
