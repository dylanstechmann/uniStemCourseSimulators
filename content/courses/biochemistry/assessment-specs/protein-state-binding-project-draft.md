# Protein state and ligand binding: inactive project candidate

**State: inactive human-review candidate.** This project is not scheduled, assigned, submitted, collected or graded. A private unreviewed worked-solution and scoring guide is stored outside the public package; it is not approved or active. All proteins, group counts, assay parameters and observations are fictional teaching inputs, not real measurements or recommendations.

The candidate proposes five deliverables and 100 human-review points across four linked lessons. The proposed rubric is published separately so learners can see the intended evidence before any future assignment. It is an authoring draft, not approved for a course grade, and it is not an automatic grader. No free-text response is scored by software.

## Model and data

Compare conditions A and B in the [condition table](protein-state-binding-conditions.csv). They represent two stipulated solution conditions for the same fictional protein. The protein has seven independent acidic groups with `pKa=4.0`, seven independent basic groups with `pKa=10.0`, and two histidines with `pKa=6.0`; terminal charges are stipulated to be capped and omitted. Treat the pKa values as fixed for this exercise.

For each condition, the table supplies a modeled `ΔG_H2O`, denaturant slope `m`, denaturant concentration `[D]` and `K_d`. Use `ΔG_unfold([D])=ΔG_H2O−m[D]`, `K_u=exp(−ΔG_unfold/RT)`, and `f_folded=1/(1+K_u)`, with `T=298.15 K` and `R=0.008314 kJ/(mol·K)`. Treat these stability parameters as independent supplied inputs; do not infer them from the net charge.

Treat only folded protein as ligand-binding competent. Under this staged model, ligand binding does not change the folding equilibrium, and `K_d` applies to the folded population. Thus the active folded-protein total is `R_F=f_folded R_T`. For total ligand `L_T`, calculate complex concentration from

`[RL] = {(R_F + L_T + K_d) − sqrt[(R_F + L_T + K_d)^2 − 4 R_F L_T]}/2`.

Use `R_T=50 nM` and `L_T=100 nM` from the table. This calculation accounts for ligand depletion by the active protein population.

## Deliverables

1. **Charge analysis — 15 points:** calculate net charge at pH 6 and pH 8 from the fractional ionization of the three stipulated group types. Explain the sign change and why charge alone does not determine `K_d` or folding stability.
2. **Folding analysis — 20 points:** for each condition, calculate `ΔG_unfold`, `K_u`, folded fraction and active folded-protein total.
3. **Binding analysis — 25 points:** calculate `[RL]` with the quadratic relation, the fraction of folded protein bound and the fraction of total protein both folded and bound. State each denominator.
4. **Decision analysis — 20 points:** compare the exact result with the `L_free≈L_T` approximation, state the direction of its error and apply the fictional `0.70` target for total protein folded and bound.
5. **Model limitations — 20 points:** identify two assumptions whose failure would require a coupled or more detailed model. Do not interpret the calculation as evidence about any real protein, function or person.

See the [draft human-review rubric](protein-state-binding-project-rubric.md) for criteria and scoring anchors. Report numeric answers to three significant figures, retain units and intermediate values, and distinguish modeled quantities from biological measurements.

## Limits and review needed

The point weights, workload and rubric calibration have not been approved. Before activation, an independent reviewer must recalculate the full analysis; qualified biochemical and assessment reviewers must examine the exact version; accessibility and fairness need review; workload must be measured; protected delivery must be verified; and an operator must approve grading and retake policy. The project remains outside the live manifest. No reviewer is identified or implied by this authoring.

## Provenance

Original authoring and fictional parameters, CC BY 4.0. No real protein, personal, clinical or third-party dataset is included.
