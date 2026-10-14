# Three-point mapping and penetrance: inactive project draft

**Status:** authoring draft only. It is not scheduled, assigned, submitted, collected or graded. The marker names, offspring counts and family model are fictional teaching data. They establish neither causation nor the risk of any real person.

## Part A: map three linked markers

A phase-known heterozygote with haplotypes `ABC/abc` is testcrossed to `abc/abc`. Assume complete, equally observed progeny classes and use the supplied [gamete count table](three-point-testcross-counts.csv). Each offspring's tester chromosome is `abc`, so its scored gamete reports the heterozygote's transmitted haplotype. Uppercase and lowercase letters denote alternative alleles at three fictional markers.

1. Identify the parental classes from the most frequent progeny and the double-crossover classes from the least frequent progeny. Use their pattern to infer the middle marker and state the gene order.
2. Classify all eight classes as parental, single crossover in each interval, or double crossover. Show the phase logic, not just the labels.
3. Calculate the recombination fraction and map distance for each adjacent interval, including double crossovers in each interval's recombinant count.
4. Calculate the recombination fraction between the outer markers directly from offspring classes. Compare it with the sum of adjacent map distances and explain the double-crossover contribution.
5. Under the simple independence approximation, calculate the expected double-crossover count, coefficient of coincidence and interference. State why these sample estimates do not prove a molecular mechanism or a universal crossover pattern.

## Part B: conditional genotype probability under penetrance

In a separate fictional family model, one parent is `D/d` and the other is `d/d`. Only `D/d` offspring can show a specified phenotype; assume their penetrance is `0.80`, while `d/d` offspring are always unaffected. There are no phenocopies in this stipulated model.

6. Calculate the prior genotype probabilities, the probability that an offspring is affected, and `P(D/d | unaffected)` using Bayes' rule. Keep the family scenario separate from the marker map: the data provide no evidence that marker `D` is real or associated with a trait.

## Author calculation key

The parental classes are `ABC` and `abc`; the double crossovers are `AbC` and `aBc`, so `B` is the middle marker and the order is `A-B-C`. The A-B single crossovers are `Abc` and `aBC`; the B-C single crossovers are `ABc` and `abC`.

There are 1,000 offspring. A-B recombinants total `69+69+4+4=146`, giving `r_AB=0.146` and `14.6 cM`. B-C recombinants total `46+46+4+4=100`, giving `r_BC=0.100` and `10.0 cM`. Between the outer markers, the single-crossover classes total `69+69+46+46=230`; the double crossovers restore the parental outer-marker arrangement. Thus `r_AC=0.230`, below the adjacent map-distance sum `24.6 cM` by `2×0.8%=1.6` percentage points.

Under independence, the expected double-crossovers are `0.146×0.100×1000=14.6`. The observed count is 8, so the coefficient of coincidence is `8/14.6≈0.548` and the sample interference estimate is `1−0.548≈0.452`. Counts are finite-sample observations; the estimate alone does not establish a mechanism.

For the separate family model, `P(D/d)=P(d/d)=0.5`; `P(affected)=0.5×0.80=0.40`. The joint probability of `D/d` and unaffected is `0.5×0.20=0.10`, while `P(unaffected)=0.10+0.50=0.60`, so `P(D/d | unaffected)=0.10/0.60=1/6≈0.1667`.

## Proposed unweighted review rubric

| Criterion | Evidence for future human review |
|---|---|
| Gene order | Uses parental and double-crossover classes to identify the middle marker |
| Mapping | Classifies all progeny and computes adjacent and outer-marker recombination correctly |
| Interference | Distinguishes observed from expected double crossovers and qualifies the sample estimate |
| Probability | Applies penetrance and Bayes' rule with the stated model assumptions |
| Scope | Keeps linkage distinct from causation and synthetic family probabilities distinct from real risk |

The rubric has no point weights or automatic prose grader. Mathematical accuracy, instructional design, accessibility and workload need qualified review. Do not activate this draft or describe it as a course assessment until those reviews and the course's missing homework, exams and laboratory sequence are addressed.

## Provenance

Original authoring and synthetic data, CC BY 4.0, developed with substantial AI assistance. No personal or third-party genetic data are included.
