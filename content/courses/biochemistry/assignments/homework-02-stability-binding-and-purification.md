# Homework 2 practice: stability, ligand depletion and replicate purification

**Status:** open formative practice; this packet and its answer specifications are public and are not suitable for a protected or summative exam. It does not contribute to a course grade. The separate inactive Homework 2 review candidate is not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 2–3 hours
**Prerequisite lessons:** [Protein folding and stability](../modules/09-protein-folding-and-stability.md), [Binding equilibria](../modules/07-binding-equilibria-and-cooperativity.md), [Protein purification as quantitative evidence](../modules/14-protein-purification-and-activity-data.md) and the [virtual purification lab](../labs/02-protein-purification-from-fractionation-data.md).
**Dataset:** [synthetic replicate purifications](homework-02-replicate-purifications.csv).

## Purpose

Weeks 3 and 4 treat a protein as a population: some molecules are folded and some are not, some binding sites are occupied and some are free, and a purification keeps some activity while discarding most protein. Each question below asks for a population quantity and then for the limit of what it shows. A protein that is 99.9% folded can still supply many more unfolded molecules than its parent; a shortcut binding equation can overstate occupancy when receptor and ligand are comparable; and a fold enrichment is not a purity certificate.

## Learning objectives

After working through the packet, learners should be able to:

1. Convert stability and denaturant data into a midpoint, a folded fraction and a ratio of unfolded populations.
2. Calculate complex formation with the exact ligand-depletion solution and quantify the error of the free-equals-total shortcut.
3. Compare cooperative and non-cooperative occupancy over a ligand range.
4. Summarize replicate purification runs by computing recovery and fold enrichment within each run before averaging.
5. Choose an orthogonal separation step and state what specific activity does and does not establish.

## Part A — two stabilities

Fictional enzyme E1 has ΔG_H₂O = 30 kJ/mol and an m-value of 12 kJ/mol per M; its variant E1* has ΔG_H₂O = 21 kJ/mol and the same m-value. Use the two-state model at 25 °C, RT = 2.479 kJ/mol: ΔG_unfold([D]) = ΔG_H₂O − m[D], K_u = exp(−ΔG_unfold/RT) and f_N = 1/(1 + K_u).

**In words:** stability falls linearly with denaturant; the unfolded-to-folded ratio grows exponentially as stability falls; and the folded fraction is one over one plus that ratio.

Find E1*'s midpoint, its folded fraction at 1.0 M denaturant, and the factor by which its unfolded population in water exceeds E1's.

## Part B — ligand depletion and a cooperative switch

A fictional receptor binds its ligand 1:1 with K_d = 20 nM; receptor total is 40 nM and ligand total 60 nM. Use [RL] = {(R_T + L_T + K_d) − √[(R_T + L_T + K_d)² − 4R_TL_T]}/2 and compare it with R_T·L_T/(K_d + L_T), the shortcut that treats total ligand as free. Then consider a fictional cooperative sensor with n_H = 2.0 and K₀.₅ = 10 μM and find how much its occupancy rises between 5 and 20 μM ligand.

## Part C — three purification runs

Three independent runs purified the same fictional enzyme from separate extracts. Each run has a crude extract and a final pool.

| Column | Meaning |
| --- | --- |
| `prep` | Purification run P1, P2 or P3; each is one independent preparation |
| `fraction` | `crude` or `final_pool` |
| `volume_ml` | Fraction volume in mL |
| `protein_mg_per_ml` | Protein concentration in mg/mL |
| `activity_u_per_ml` | Activity in U/mL, one U being 1 μmol product per minute under one fixed assay |

For each run compute total protein (volume × concentration), total activity, specific activity, activity recovery (final ÷ crude activity × 100) and fold enrichment (final ÷ crude specific activity). Then average the three runs with equal weight.

To use the software checks, open **Practice gradebook** and select **Homework 2: stability, ligand depletion and replicate purification (open, ungraded practice)**. Upload one UTF-8 CSV with exactly this header and column order, with rows `crude` and `final_pool`; report 100 and 1 for the crude recovery and fold:

```text
fraction,prep_count,mean_specific_activity_u_per_mg,mean_recovery_pct,mean_fold_enrichment
```

## Part D — what the purification shows

Use the structured check to name the independent unit, say what roughly 40-fold enrichment supports, and choose the next separation step after an affinity column.

## Worked calculation

Take a run whose crude extract is 30 mL at 3.0 mg/mL and 100 U/mL, and whose final pool is 4 mL at 0.30 mg/mL and 450 U/mL. Crude totals are 90 mg and 3,000 U (33.3 U/mg); final totals are 1.2 mg and 1,800 U (1,500 U/mg). Recovery is 1,800/3,000 = 60%, and fold enrichment is 1,500/33.3 = 45. Computing these within the run before averaging runs keeps each independent preparation as one unit; dividing a mean final specific activity by a mean crude specific activity weights runs differently.

## Analytic instructor rubric

For instructor-led discussion, use 0–2 points for each criterion: 0 for absent or incompatible evidence, 1 for a partly correct response, 2 for the evidence described. This guide is not connected to the software gradebook.

| Criterion | Evidence for full credit |
| --- | --- |
| Stability arithmetic | Uses the linear denaturant model and the exponential population relation with the stated RT and units. |
| Population reasoning | Explains why a nearly fully folded variant can still raise the unfolded population many-fold and what that does and does not imply. |
| Depletion | Uses the quadratic, checks the result by mass balance and states when the shortcut is adequate. |
| Replicate summary | Computes recovery and fold enrichment within each run and summarizes runs as independent units. |
| Purification claims | Keeps specific activity separate from purity and proposes an orthogonal separation. |

The autograded practice covers a subset of these criteria with deterministic numeric, CSV and structured-choice rules. Its keys are open in this repository. Written explanations are not scored automatically.

## Limitations and provenance

Original exercise with constructed values. The enzymes, receptor, sensor and purification runs are fictional; no laboratory protocol or real material is described. Two-state and single-site models are simplifications, and the stated RT applies only at 25 °C. Original packet and synthetic dataset: CC BY 4.0.
