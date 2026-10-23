# Assignment 3: population dynamics and linkage evidence

Develop two separate reproducible analyses using the [selection/inbreeding/linkage reading](../modules/selection-inbreeding-and-linkage-likelihood.md). One follows a one-locus population through a declared life cycle. The other compares recombination hypotheses using a known-phase cross. Retain equations, calculations or executable source, verification cases, results and an interpretation report locally. Browser items check selected outputs, not your implementation, proof, graph or written argument. All values are synthetic and establish no claim about a person or population.

## Part A: a declared population life cycle

Start with gamete allele frequency q0=0.25. Random union produces zygotes. The stipulated selection weights are wAA=1, wAa=0.9 and waa=0.4. Surviving contributors produce gametes with A→a mutation u=0.001 and a→A mutation v=0.002. Random union follows. The model is deterministic, with no migration, drift, sex differences or additional loci. Write the complete recurrence in this order and normalize each selection step. Calculate the first generation by hand before implementing iteration.

Record generation, pre-selection genotype proportions, mean fitness, post-selection allele frequency and post-mutation allele frequency. Iterate for 100 generations. Plot or tabulate selected generations and report whether every genotype vector sums to one and all frequencies stay in [0,1]. Define what you mean by numerical convergence rather than labeling a visually flat graph an exact equilibrium. Compare q100 with the starting state and retain the recurrence residual at the last iterate.

Create verification cases before interpreting the main trajectory: all weights equal and no mutation should preserve q; mutation alone should obey the linear recurrence; u=v=0 and an initial boundary q=0 should stay zero when mean fitness is positive. A state with zero mean fitness is undefined for the normalized model and should produce an explicit failure instead of NaN values interpreted as biological output. Reversing mutation and selection is a different life-cycle model; quantify its first-generation difference and state why neither ordering is universally correct without biological specification.

## Part B: genotype association and approximation limits

At q=0.25, replace random union for one generation with the identity-by-descent mixture F=0.1. Derive the three pre-selection genotype proportions from the mixture rather than adding a correction to just the rare homozygote. Verify the total and unchanged allele frequency, then apply the supplied selection weights. Compare the post-selection allele frequency with Part A. Explain why an allele-preserving mating step can change the next selective response.

In a separate recessive-only scenario use wAA=wAa=1, waa=0.5, u=0.000008 and v=0 with mutation after selection. Calculate the rare-allele approximation sqrt(u/s). Evaluate its residual in the exact declared recurrence. Iterate from both q=0.02 and q=0.002, retaining enough precision and generations to distinguish a slow approach from a coding error. The exact positive interior equilibrium for this particular order is a useful derivation challenge. Do not assume the same root applies to the heterozygote-disadvantage main scenario. Explain which real processes could make inference of mutation rate from an observed frequency unreliable.

## Part C: a separate linkage likelihood

A stipulated known-phase cross yields R=4 recombinant and NR=36 nonrecombinant informative, independent transmissions. Genotyping error and ascertainment are absent by assumption. Evaluate log10 likelihood ratios Z(θ) against θ=0.5 on θ values 0.05, 0.10, 0.20 and 0.50. Find the constrained maximum for 0≤θ≤0.5. Derive it by differentiating the log likelihood or comparing the full concave function; do not infer it from only the four grid points.

Specify how your implementation handles θ=0 when recombinants are present, and when R=0. Compare a positive Z value with an explicit posterior-probability calculation requiring prior model odds; explain why Z alone supplies no prior and no proof of causal gene identity. As a sensitivity check, misclassify one nonrecombinant as recombinant, keeping total transmissions fixed, and recompute the maximizing θ and evidence. Population selection weights from Part A do not enter this likelihood.

## Self-review after independent work

For Part A, initial genotype proportions are 0.5625, 0.375 and 0.0625. Weighted contributions sum to 0.925; the a-allele contribution is 0.19375. Thus qs=0.19375/0.925≈0.20945946 and q1=0.997qs+0.001≈0.20983108. Under F=0.1, the pre-selection proportions are 0.58125, 0.3375 and 0.08125; their allele frequency is still 0.25, while normalized selection now produces a different qs.

The separate rare-recessive approximation is 0.004. For this particular mutation-after-selection, zero-back-mutation, recessive-selection recurrence, the positive interior fixed point is exactly sqrt(u/s); q=1 is another boundary fixed point when surviving aa contributors remain possible. The report should derive this instead of assuming approximations are always inexact. Convergence can be very slow at small q, so iteration count and residual are essential evidence.

For the linkage sample, the maximum is at θ=4/40=0.10 and Z there is about 6.39394. Reclassifying one transmission gives θ=5/40=0.125. Neither value is a DNA base-pair distance, disease probability or expression effect. Compare your own ledger before using browser feedback.

## Completion standard and boundaries

Retain the first-generation hand calculation, tested recurrence, trajectory, probability/conservation checks, genotype-mixture derivation, exact-versus-approximate balance argument and log-likelihood sensitivity analysis. State assumptions and one discriminating extra observation for every biological interpretation. This original coursework was developed with substantial AI assistance; MIT OCW [7.03 Genetics Fall 2004](https://ocw.mit.edu/courses/7-03-genetics-fall-2004/pages/calendar/) supplies a link-only scope comparator. No university problem or real pedigree was imported. The course is partial and unreviewed; no measured workload, qualified approval or clinical interpretation is supplied.
