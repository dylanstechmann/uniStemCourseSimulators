# Protein-state project guide: charge, folding and ligand binding (optional, ungraded)

**Status:** open, optional and ungraded. Five milestone self-checks in the Case studio save responses privately; nothing is submitted, collected or scored. The separate inactive project candidate, its proposed human-review rubric and its private worked solution remain unreviewed and are not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 6–8 hours spread across weeks 5–8.
**Prerequisite lessons:** [Protein structure and molecular recognition](../modules/01-protein-structure-and-molecular-recognition.md), [Binding equilibria](../modules/07-binding-equilibria-and-cooperativity.md), [Amino acids, charge and pH](../modules/08-amino-acids-charge-and-isoelectric-points.md) and [Protein folding and stability](../modules/09-protein-folding-and-stability.md).
**Data:** the [project condition table](../assessment-specs/protein-state-binding-conditions.csv) for conditions A and B, and the [rehearsal condition table](protein-state-rehearsal-condition.csv) for condition C.

## Purpose

The project joins four first-half lessons into one calculation about a fictional protein. Charge is computed from ionizable groups. Folding stability then sets how much of the protein is folded, and only folded protein binds the ligand, so the folded amount becomes the input to an exact binding calculation. A last step compares the exact answer with a common shortcut and applies a stated modeling threshold. The aim is to practice carrying one result into the next while keeping every denominator and assumption visible.

## The model

Conditions A and B are two stipulated solution conditions for the same fictional protein. It has seven independent acidic groups with pKa 4.0, seven independent basic groups with pKa 10.0 and two histidines with pKa 6.0; its terminal charges are capped and omitted. Treat every pKa as fixed.

- **Charge.** Each acidic group contributes −1/(1 + 10^(pKa − pH)); each basic group or histidine contributes +1/(1 + 10^(pH − pKa)). Multiply by the group count and add.
- **Folding.** ΔG_unfold = ΔG_H₂O − m[D], K_u = exp(−ΔG_unfold/RT) and f_folded = 1/(1 + K_u), with T = 298.15 K and R = 0.008314 kJ/(mol·K). The stability values are supplied inputs; do not infer them from charge.
- **Active protein.** Only folded protein binds, so R_F = f_folded × R_T. In this staged model, binding does not change the folding equilibrium, and K_d applies to the folded population.
- **Binding.** [RL] = {(R_F + L_T + K_d) − √[(R_F + L_T + K_d)² − 4R_FL_T]}/2, with R_T = 50 nM and L_T = 100 nM from the table.
- **Decision.** A fictional target asks whether at least 0.70 of the total protein is both folded and bound, that is, whether [RL]/R_T ≥ 0.70.

## Milestones

| Milestone | Suggested week | Task | Where to check yourself |
| --- | --- | --- | --- |
| Rehearsal | 5 | Work condition C, then use the open rehearsal practice set | **Practice gradebook**: Protein-state project rehearsal |
| M1 | 5 | Net charge at pH 6 (condition A) and pH 8 (condition B); explain the sign change and what charge cannot tell you | Case studio: project milestone 1 |
| M2 | 6 | ΔG_unfold, K_u, f_folded and R_F for both conditions | Case studio: project milestone 2 |
| M3 | 7 | [RL], the bound fraction of folded protein and the folded-and-bound fraction of total protein | Case studio: project milestone 3 |
| M4 | 8 | Compare with the free-ligand shortcut and apply the 0.70 target | Case studio: project milestone 4 |
| M5 | 8 | Two assumptions whose failure would need a coupled or more detailed model | Case studio: project milestone 5 |

Each Case studio milestone lists self-review statements. Responses are saved privately in this application and are never scored.

## Worked example: condition C at a different denaturant concentration

Condition C uses a different fictional protein: 6 acidic groups (pKa 4.0), 8 basic groups (pKa 10.0) and 3 histidines (pKa 6.0), with ΔG_H₂O = 22 kJ/mol, m = 8 kJ/mol per M, K_d = 15 nM, R_T = 50 nM and L_T = 100 nM. This example uses pH 6.0 and 2.5 M denaturant. The rehearsal practice set asks for the same steps at the pH values and denaturant concentration listed in the rehearsal table, so the numbers below are a method check, not its answers.

1. **Charge at pH 6.0.** Acids: −6/(1 + 10^(4.0 − 6.0)) = −6/1.01 = −5.941. Bases: +8/(1 + 10^(6.0 − 10.0)) = +7.999. Histidines: +3/(1 + 10^0) = +1.500. Net charge = +3.56. The histidines, with pKa equal to the pH, change most across nearby pH values.
2. **Folding at 2.5 M.** ΔG_unfold = 22 − 8 × 2.5 = 2.0 kJ/mol. With RT = 2.479 kJ/mol, K_u = exp(−2.0/2.479) = 0.4463, so f_folded = 1/1.4463 = 0.6914 and R_F = 0.6914 × 50 = 34.6 nM.
3. **Binding.** R_F + L_T + K_d = 34.57 + 100 + 15 = 149.57 nM. The square root is √(149.57² − 4 × 34.57 × 100) = √8543 = 92.43, so [RL] = (149.57 − 92.43)/2 = 28.6 nM.
4. **Check.** Free protein = 34.57 − 28.57 = 6.00 nM and free ligand = 100 − 28.57 = 71.43 nM; 6.00 × 71.43/28.57 = 15.0 nM recovers K_d. [RL] is smaller than both R_F and L_T, so the physically possible root was chosen.
5. **Two denominators.** [RL]/R_F = 28.57/34.57 = 0.826 is the bound fraction of folded protein. [RL]/R_T = 28.57/50 = 0.571 is the fraction of all protein that is folded and bound. The target uses the second.
6. **Shortcut.** Treating 100 nM as free ligand gives θ = 100/115 = 0.870 and [RL] = 0.870 × 34.57 = 30.1 nM, or 0.601 of total protein. It overestimates binding because complex formation lowers free ligand. Here both values fall below the target, but near a threshold the overestimate can change the decision.
7. **Decision.** 0.571 < 0.70, so condition C at 2.5 M does not meet the fictional modeled threshold. That statement is about the model's inputs, not about any real protein.

Conditions A and B use the project protein, which has a different composition and different stability and binding inputs. Their results do not follow from these numbers.

## Reporting conventions

- Report final values to three significant figures with units, and keep at least four significant figures in intermediate values.
- Name the denominator of every fraction.
- Separate supplied inputs, calculated model quantities and interpretations.
- Disclose any software, spreadsheets or AI assistance you used.

## Self-review rubric

The inactive project candidate proposes five criteria for a future human reviewer. For self-review, give each criterion an anchor from 0 to 4: 0 absent, 1 major errors, 2 partial, 3 substantially correct with a limited error, 4 complete and consistent with the stated model.

| Criterion | Evidence of a complete response |
| --- | --- |
| Charge model | Correct signs and fractional charges at both pH values; no inference about binding or stability from charge alone |
| Folding thermodynamics | Correct ΔG_unfold, K_u, folded fraction and active folded protein for both conditions |
| Ligand-depletion analysis | Uses R_F in the quadratic; reports [RL] and both denominators with units |
| Approximation and decision | Compares the shortcut with the exact result, explains the direction of its error and applies 0.70 to total protein |
| Assumptions and communication | Names at least two consequential assumptions, explains when coupling is needed and states limits without biological overclaim |

These anchors describe evidence for self-review. They are not calibrated, carry no grade and do not stand in for an instructor's judgment.

## Limitations and provenance

The proteins, group counts, stability values, affinities and threshold are fictional teaching inputs. The staged model assumes independent ionizable groups with fixed pKa values, two-state folding, a single 1:1 binding site that only the folded state has, and equilibrium at the time of measurement. A real protein can violate each of these, and nothing here is evidence about a real protein, its function or any person. No laboratory protocol is given. Original guide and synthetic rehearsal data: CC BY 4.0.
