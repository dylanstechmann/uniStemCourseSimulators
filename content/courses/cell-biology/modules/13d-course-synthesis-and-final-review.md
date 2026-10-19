# Week 14 synthesis: one evidence chain from molecule to cell state

This reading closes the course. It connects the week 9–14 lessons to the quantitative and evidence frameworks of weeks 1–8, then works one synthetic case through every layer. Use it with the **Week 14 cumulative final review practice** set in the Practice gradebook. That set is public, ungraded practice with unlimited retries; it is not a final exam, and the separate final-exam candidate remains an inactive, unreviewed draft.

## The chain the course has built

Across fourteen weeks, each lesson measured one link in a longer chain:

`chemistry and structure → compartment → catalysis and energy → DNA and chromatin → RNA → protein → genotype → signal → force and matrix → cell cycle and state → lineage marker → function`

**In words:** the course moved from molecular chemistry through compartments, enzymes, the genome, RNA and protein, to genotype, signaling, mechanics, cell state, lineage markers and finally function.

Every arrow is a hypothesis that needs its own measurement. The table lists what a typical measurement at each layer reports and what that measurement does not establish by itself.

| Layer (weeks) | Typical measured quantity | Does not by itself establish |
| --- | --- | --- |
| Chemistry and structure (1–2) | Protonation state, interaction type, residue environment | Activity, localization or phenotype |
| Compartments and traffic (3, 5) | Marker-normalized fraction, protease protection, image signal | Molecular function or the in-cell mechanism |
| Catalysis and energy (4) | Initial rate, Km, Vmax, ΔG | A binding constant, a binding site, or a shifted equilibrium |
| DNA, chromatin and transcription (6–7) | Lesion signal, accessibility, ChIP percent input, reporter activity | Repair flux, transcription rate or endogenous causation |
| RNA (9) | Precursor, mature and junction-specific signals | Transcription rate or protein output |
| Protein (9) | Short-pulse synthesis, half-life, steady-state amount | Activity, localization or degradation route |
| Genotype (10) | Transmission and penetrance under a model; isogenic contrasts | A molecular mechanism or a population risk |
| Signaling (11) | Occupancy estimate, phospho-protein trajectory | A cell response or fate |
| Matrix and force (12) | Modulus, traction index, YAP localization | A lineage outcome or a unique force pathway |
| Cell cycle and state (13) | EdU fraction, DNA content, marker panels, caspase signal, recovery | Permanence of a state or the cause of cell loss |
| Lineage and function (14) | Marker-defined fraction, function-assay fraction | Stable identity or clinical benefit |

## Three quantitative patterns that recur

### Production and removal

Week 9 used the same balance for RNA and for protein:

`dP/dt = s − k_deg·P`, so at steady state `P_ss = s / k_deg`, and for first-order removal `k_deg = ln 2 / t½`.

**In words:** the amount changes at the synthesis rate minus a removal constant times the current amount; at steady state the amount equals synthesis divided by the removal constant, and the removal constant equals ln 2 divided by the half-life.

A steady-state change cannot say by itself which term moved. Synthesis falling to one third, or removal becoming three times faster with synthesis unchanged, produces the same new steady state. A short-pulse synthesis measurement and a pulse-chase or decay measurement are both needed, with matched recovery and viable-cell denominators.

### Saturation

Week 4 used `v = Vmax[S] / (Km + [S])`; week 11 used `θ = [L]free / (Kd + [L]free)`.

**In words:** the initial rate equals the maximal rate times substrate concentration divided by Km plus that concentration; occupied-site fraction equals free ligand divided by Kd plus free ligand.

Both relations are hyperbolas that reach half of their maximum when the concentration equals the constant in the denominator. Their meanings differ. Km is a kinetic parameter that equals a dissociation constant only under extra assumptions. θ is a binding fraction; the measured cell response can reach half of its maximum at a different concentration because of spare receptors, amplification, thresholds or feedback. Matching algebra is not matching biology.

### Denominators

State what each fraction divides by. Suppose 60 EdU-positive cells are found among 300 recovered viable cells: that is 20% of viable cells. If 400 cells were seeded, the same count is 15% of seeded cells, and the 100 unrecovered cells were never profiled. A change from 30% to 41% is 11 percentage points in absolute terms and about 36.7% relative to the 30% baseline. An equal-culture mean and a pooled fraction weight cultures differently and answer different questions. Week 5 recovery, week 13 cell-state percentages and the integrative project's per-1000-viable-cell values all depend on this habit.

## Carry the evidence forward

The [week-8 controls synthesis](07d-controls-replicates-and-bounded-claims.md) covered weeks 5–7. This table extends the same transfer to weeks 9–14.

| Earlier evidence example | Independent unit and useful comparison | Claim boundary to carry forward |
| --- | --- | --- |
| Week 9 translation and turnover ([lesson](08b-translation-and-protein-turnover.md), [homework 5](../assignments/homework-05-rna-and-protein-layers.md)) | Four independent cultures; matched mRNA, short-pulse synthesis and pulse-chase half-life | Lower synthesis per measured mRNA in this system; not a demonstrated initiation mechanism |
| Week 10 isogenic clones ([lesson](09b-variant-mechanism-and-isogenic-evidence.md), [homework 6](../assignments/homework-06-genotype-and-phenotype.md)) | Independently derived, sequence-checked clones; a mock-edited reference and a correction | A variant-associated protein-amount change and its reversibility in these clones; not an organism-level phenotype |
| Week 11 signaling lab ([lesson](10b-signaling-dynamics-feedback-and-perturbations.md), [lab 2](../labs/02-signaling-dynamics-inhibitor-rescue.md)) | Independent culture preparations; vehicle, inhibitor and rescue at matched times | A pathway contribution to the measured phospho-signal; not a cell fate |
| Week 12 matrix mechanics ([lesson](11b-matrix-mechanics-and-mechanotransduction.md), [homework 7](../assignments/homework-07-matrix-perturbation-design.md)) | Independent culture preparations on measured matrices with matched accessible ligand | An association with the measured modulus; not a unique force pathway or lineage outcome |
| Week 13 cell state ([lesson](12b-senescence-apoptosis-and-cell-fate.md), [homework 8](../assignments/homework-08-cell-state-evidence.md)) | Independent cultures with recovery, EdU, a marker panel and a caspase signal | A bounded state description for the tested window; not a permanent senescent state |
| Week 14 lineage and design ([lesson](13b-integrative-regenerative-study-design.md), [lab 3](../labs/03-lineage-time-course-and-state-inference.md)) | Independent differentiation batches as blocks; marker and function measured separately | A marker-defined change in one model; not mature function or clinical benefit |

## Worked integration: a variant that shortens a phosphatase's lifetime

The final review practice uses one [synthetic clone dataset](../assignments/final-review-feedback-variant-clones.csv). A cultured cell model expresses a fictional phosphatase, F, that can remove activating phosphate from ERK. A candidate missense variant in F was introduced into reference cells by knock-in, and corrected clones were derived from knock-in clones. Four independently derived, sequence-checked clones per genotype were measured under matched conditions. F mRNA, short-pulse F synthesis and pulse-chase F half-life were measured in unstimulated cultures, along with steady-state F protein. A pERK time course was collected under continued ligand exposure and normalized to total ERK and time-matched vehicle. A short EdU pulse was scored among recovered viable cells, and viable recovery was recorded. All values are synthetic teaching data and describe no real gene, variant or person.

| Clone-mean readout | Reference | Knock-in | Corrected |
| --- | ---: | ---: | ---: |
| F mRNA, relative units | 100 | 98 | 100 |
| Short-pulse F synthesis, relative units | 100 | 98 | 100 |
| F half-life (h) | 6.0 | 2.0 | 5.8 |
| Steady-state F protein, relative units | 100 | 33 | 97 |
| pERK at 60 min (fold over vehicle) | 3.4 | 5.2 | 3.5 |
| EdU-positive recovered viable cells (%) | 30 | 41 | 31 |
| Viable recovery (%) | 93 | 92 | 94 |

Work through the layers in order.

1. **RNA and synthesis.** F mRNA and short-pulse synthesis are similar across genotypes, so these assays give no support for a large change in transcription or translation.
2. **Turnover.** The half-life falls threefold. Because `P_ss = s / k_deg` and `k_deg = ln 2 / t½`, the steady state is proportional to synthesis times half-life. The model predicts knock-in F at about `0.98 × 2.0 / 6.0`, roughly one third of reference, close to the measured 33. Faster removal with similar synthesis is enough to account for the lower F protein under this model. The chase does not identify the degradation route.
3. **Signaling.** The pERK trajectory stays higher in knock-in clones. Less F is one explanation. Receptor abundance, remaining ligand or a different feedback node could also prolong the signal, and none was measured here.
4. **Cell state.** The EdU-positive fraction is 11 percentage points higher with similar recovery. That is a higher fraction of recovered cells synthesizing DNA during the pulse. It is not a division rate for each cell, and it is not a disease phenotype.
5. **Correction.** Corrected clones move back toward reference at every layer that had differed (half-life, F protein, pERK and EdU), which supports involvement of the variant in these clones. Correction shows reversibility; it does not prove direct catalysis on ERK or any effect in an organism.

The weakest link runs from lower F protein to the sustained pERK. A discriminating next experiment restores F to reference-matched abundance in knock-in clones with an empty-vector control. It confirms the restored F level and measures surface receptor, remaining ligand and the full pERK time course in independent clones.

## A final-review scratch pad

The [week-8 quantitative synthesis](07c-quantitative-models-and-assumptions.md) used four lines. For a cumulative item, write five short lines before reading the feedback:

1. **Layer:** Which layer did the measurement report?
2. **Quantity and denominator:** What was calculated, in which unit, and divided by what?
3. **Comparison and unit:** Which conditions are compared, and what is the independent biological unit?
4. **Alternative and control:** Which explanation remains, and which control or measurement would address it?
5. **Boundary and next step:** What does the result support, and which measurement would test the next claim?

## Using the final review practice

The set combines 13 new integrative items on the clone dataset and cross-week scenarios with 12 earlier items from weeks 9–14. Open it from the Practice gradebook. Its answers and feedback are public authoring material, retries are unlimited, and the points never enter a course grade. To review first, revisit [RNA processing](08a-rna-processing-and-isoform-evidence.md), [translation and turnover](08b-translation-and-protein-turnover.md), [inheritance](09a-inheritance-penetrance-and-pedigree-evidence.md), [variant mechanism](09b-variant-mechanism-and-isogenic-evidence.md), [receptors](10a-receptor-signaling-and-network-logic.md), [signaling dynamics](10b-signaling-dynamics-feedback-and-perturbations.md), [cytoskeleton and matrix](11a-cytoskeleton-adhesion-and-extracellular-matrix.md), [matrix mechanics](11b-matrix-mechanics-and-mechanotransduction.md), [the cell cycle](12a-cell-cycle-checkpoints-and-mitosis.md), [cell state](12b-senescence-apoptosis-and-cell-fate.md), [potency and lineage](13a-developmental-potency-and-lineage-evidence.md) and [integrative study design](13b-integrative-regenerative-study-design.md). For weeks 1–7, start from the two week-8 synthesis readings.

## Limits of this reading

This synthesis introduces no new experimental claim. The phosphatase case is constructed to exercise reasoning across layers; it does not describe a real protein, variant, pathway or patient. Completing the review practice does not establish course mastery, and the course remains partial and unreviewed. The reading and its dataset are original CC BY 4.0 content; MIT OpenCourseWare comparators in the source registry are link-only, and no outside text, figure, question or dataset is copied or adapted.
