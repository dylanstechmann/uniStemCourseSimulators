# Three-point mapping project guide: gene order, interference and penetrance (optional, ungraded)

**Status:** open, optional and ungraded. Five milestone self-checks in the Case studio save responses privately; nothing is submitted, collected or scored. The separate inactive project draft and its proposed review rubric remain unreviewed and are not served to learners.
**Introduced in:** course package version 0.6.0.
**Suggested time (unvalidated author estimate):** 4–6 hours across weeks 6 and 7.
**Prerequisite lessons:** [Segregation, penetrance and probability](../modules/01-segregation-penetrance-and-probability.md), [Sex linkage, pedigrees and Bayesian carrier risk](../modules/11-sex-linkage-pedigrees-and-bayesian-carrier-risk.md), [Linkage and recombination mapping](../modules/02-linkage-and-recombination-mapping.md) and [Three-point mapping and interference](../modules/07-three-point-mapping-and-interference.md).
**Data:** the project counts in Part A below, and the [rehearsal gamete counts](three-point-rehearsal-counts.csv) for the open practice set.

## Purpose

The project takes one fictional testcross from raw offspring counts to an ordered map with an interference estimate, then applies penetrance and Bayes' rule in a separate family model. The two parts share probability reasoning but not data: nothing in the family model says that any mapped marker is real or associated with a trait. The aim is to practice reading phase from counts, carrying each count into the right fraction, and stating what a finite sample and a stipulated model can and cannot show.

## The project

### Part A: map three linked markers

A phase-known heterozygote with haplotypes ABC/abc is testcrossed to abc/abc. The tester contributes only abc, so each offspring class reports the haplotype its heterozygous parent transmitted. Uppercase and lowercase letters are alternative alleles at three fictional markers, and every progeny class is assumed to be complete and equally viable. The table lists the classes alphabetically, not by type.

| Gamete | Count |
| --- | ---: |
| ABC | 381 |
| ABc | 46 |
| AbC | 4 |
| Abc | 69 |
| aBC | 69 |
| aBc | 4 |
| abC | 46 |
| abc | 381 |

There are 1,000 offspring in total.

1. Identify the parental and double-crossover classes, infer the middle marker and state the gene order.
2. Classify all eight classes as parental, single crossover in each interval or double crossover, and show the phase logic.
3. Calculate the recombination fraction and map distance for each adjacent interval, including the double crossovers in each interval's recombinant count.
4. Calculate the recombination fraction between the outer markers directly from the classes. Compare it with the sum of the adjacent map distances and explain the double-crossover contribution.
5. Under independence, calculate the expected double crossovers, the coefficient of coincidence and interference. State why these sample estimates do not establish a molecular mechanism or a universal crossover pattern.

### Part B: conditional genotype probability under penetrance

In a separate fictional family model, one parent is D/d and the other is d/d. Only D/d offspring can show a specified phenotype, with penetrance 0.80; d/d offspring are always unaffected, and there are no phenocopies.

6. Calculate the prior genotype probabilities, the probability that an offspring is affected and P(D/d | unaffected) with Bayes' rule. Keep the family model separate from the marker map.

## Milestones

| Milestone | Suggested week | Task | Where to check yourself |
| --- | --- | --- | --- |
| Rehearsal | 6 | Work the rehearsal counts and family model, then use the open rehearsal practice set | **Practice gradebook**: Three-point project rehearsal |
| M1 | 6 | Gene order and the classification of all eight classes (tasks 1–2) | Case studio: project milestone 1 |
| M2 | 6 | Adjacent-interval recombination fractions and map distances (task 3) | Case studio: project milestone 2 |
| M3 | 6 | Outer-marker fraction, expected double crossovers, coincidence and interference (tasks 4–5) | Case studio: project milestone 3 |
| M4 | 7 | Priors, P(affected) and P(D/d \| unaffected) (task 6) | Case studio: project milestone 4 |
| M5 | 7 | What the calculations do and do not show | Case studio: project milestone 5 |

Each Case studio milestone lists self-review statements. Responses are saved privately in this application and are never scored. The rehearsal uses different markers, counts and penetrance, so its answers are not the project's answers.

## Worked example: the lesson's three-point cross

The three-point mapping lesson's synthetic cross shows every step of Part A with different numbers.

1. **Parental and double-crossover classes.** The most frequent classes, + + + (395) and a b c (387), are parental. The rarest, + b + and a + c (4 each), are double crossovers.
2. **Order.** + b + differs from + + + only at b, and a + c differs from a b c only at b, so b is in the middle and the order is a–b–c.
3. **Intervals.** r(a–b) = (52 + 54 + 8)/1000 = 0.114, or 11.4 cM; r(b–c) = (50 + 54 + 8)/1000 = 0.112, or 11.2 cM. The 8 double crossovers enter both intervals.
4. **Outer markers.** The double crossovers keep a and c in their parental combination, so r(a–c) = (106 + 104)/1000 = 0.210. That is 0.016 below the interval sum of 0.226, twice the double-crossover fraction of 0.008.
5. **Interference.** Under independence, 0.114 × 0.112 × 1000 = 12.8 double crossovers are expected. With 8 observed, the coefficient of coincidence is 8/12.8 = 0.63 and interference is 1 − 0.63 = 0.37.

In the lesson's cross the listed order a b c happened to be the map order. The rehearsal lists its markers as E, F and G, and that column order need not be the map order, so let the rarest classes decide.

For Part B, take a different penetrance of 0.90 in the same family structure. The affected probability is 0.5 × 0.90 = 0.45. Bayes' rule weighs each hypothesis by prior × likelihood of being unaffected:

| Hypothesis | Prior | P(unaffected \| genotype) | Joint |
| --- | ---: | ---: | ---: |
| D/d | 0.5 | 0.10 | 0.05 |
| d/d | 0.5 | 1 | 0.50 |

P(unaffected) = 0.05 + 0.50 = 0.55, so P(D/d | unaffected) = 0.05/0.55 = 0.0909. The unaffected phenotype lowers the probability from 0.5 without removing it.

## Reporting conventions

- Report fractions as decimals to three significant figures, and map distances in centimorgans, where 1 cM corresponds to 1% recombination.
- Keep each fraction's count and total visible.
- Separate observed counts, calculated quantities and interpretations.
- Disclose any software, spreadsheets or AI assistance you used.

## Self-review rubric

The inactive project draft proposes five criteria for a future human reviewer and assigns them no points. For self-review, mark each criterion 0 (absent), 1 (partly correct) or 2 (complete and consistent with the stated model).

| Criterion | Evidence of a complete response |
| --- | --- |
| Gene order | Uses parental and double-crossover classes to identify the middle marker |
| Mapping | Classifies all progeny and computes adjacent and outer-marker recombination correctly |
| Interference | Distinguishes observed from expected double crossovers and qualifies the sample estimate |
| Probability | Applies penetrance and Bayes' rule with the stated model assumptions |
| Scope | Keeps linkage distinct from causation and synthetic family probabilities distinct from real risk |

These marks are a self-check. They are not calibrated, carry no grade and do not stand in for an instructor's judgment.

## Limitations and provenance

The markers, counts and family model are fictional teaching inputs. The calculations assume complete and equally viable progeny classes, error-free scoring, a single phase-known heterozygote and, in Part B, a single locus with the stated penetrance and no phenocopies. One cross of 1,000 offspring gives estimates with sampling uncertainty, and linkage between markers does not identify a causal variant. Nothing here is genetic-counselling or medical advice, and nothing describes any person's risk. Original guide and synthetic rehearsal data: CC BY 4.0.
