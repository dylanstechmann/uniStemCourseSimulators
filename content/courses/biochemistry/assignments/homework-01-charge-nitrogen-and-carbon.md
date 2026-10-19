# Homework 1 practice: protein charge, nitrogen disposal and carbon fate

**Status:** open formative practice; this packet and its answer specifications are public and are not suitable for a protected or summative exam. It does not contribute to a course grade. The separate inactive Homework 1 review candidate is not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 2–3 hours
**Prerequisite lessons:** [Protein structure and molecular recognition](../modules/01-protein-structure-and-molecular-recognition.md), [Amino acids, charge and pH](../modules/08-amino-acids-charge-and-isoelectric-points.md), [Amino-acid nitrogen and the urea cycle](../modules/20-amino-nitrogen-and-urea-cycle.md) and [Amino-acid carbon skeletons](../modules/21-amino-acid-carbon-skeletons.md).
**Dataset:** [synthetic nitrogen ledger](homework-01-nitrogen-ledger.csv).

## Purpose

Weeks 1 and 2 introduce two kinds of bookkeeping that the rest of the course depends on. One is the charge of a protein, built group by group from pKa values and pH; it predicts which ion-exchange resin binds the protein. The other is the separate fate of an amino acid's nitrogen and carbon: nitrogen can be routed to urea at a fixed energy cost, while the carbon skeleton enters metabolism at a point that decides whether it can become glucose. This problem set practises both, using fictional molecules and synthetic numbers.

## Learning objectives

After working through the packet, learners should be able to:

1. Sum fractional charges over a protein's ionizable groups and use the sign of the net charge to choose an ion exchanger.
2. Convert a nitrogen load into urea and high-energy phosphate equivalents, and normalize each culture before averaging.
3. Distinguish ATP molecules from phosphoanhydride bonds and name the immediate donors of urea's atoms.
4. Separate the appearance of label in glucose from a net glucose-carbon contribution.
5. Read a change in Kd as equilibrium affinity and plan a test that separates folding from binding-site effects.

## Part A — the charge of Protein K

Fictional Protein K has 10 aspartate or glutamate side chains (pKa 4.0), a C-terminus (pKa 3.5), 2 histidines (pKa 6.0), an N-terminus (pKa 8.0), 6 lysines (pKa 10.5) and 2 arginines (pKa 12.5). Treat the groups as independent with fixed pKa values. For each acid, the charge contribution is −n/(1 + 10^(pKa − pH)); for each base it is +n/(1 + 10^(pH − pKa)).

**In words:** an acidic group carries more negative charge as the pH rises above its pKa, and a basic group carries more positive charge as the pH falls below its pKa.

Calculate the net charge at pH 6.0 and pH 8.0. Protein K is stable from pH 6 to 9; decide which first ion-exchange step fits pH 8.0.

## Part B — the nitrogen ledger

A synthetic hepatocyte culture model routes amino nitrogen to urea. Four independently prepared cultures were measured in each of two conditions over the same interval.

| Column | Meaning |
| --- | --- |
| `condition` | `basal` or `amino_load` |
| `culture` | Culture identifier; each is one independent preparation |
| `amino_nitrogen_to_urea_umol` | Nitrogen atoms routed to urea during the interval, in μmol, under a closed balance |
| `viable_cells_million` | Viable cells in the culture, in millions |

Under the course accounting, each urea carries two nitrogen atoms and costs 3 ATP molecules, which equal 4 high-energy phosphate equivalents. For each culture calculate urea, phosphate equivalents and urea per million viable cells; then average the four cultures in each condition.

To use the software checks, open **Practice gradebook** and select **Homework 1: protein charge, nitrogen disposal and carbon fate (open, ungraded practice)**. Upload one UTF-8 CSV with exactly this header and column order, one row per condition:

```text
condition,culture_count,mean_urea_umol,mean_phosphate_equivalents_umol,mean_urea_umol_per_million_cells
```

Make your own calculations from the linked file. The software scores the summary cells only.

## Part C — what the ledger can and cannot say

Use the structured check to explain why 3 ATP molecules are 4 phosphate equivalents, which molecule donates urea's second nitrogen, and what a closed-balance ledger establishes. A ledger converts a stipulated nitrogen amount into a demand; it contains no times, rates or ATP-pool measurements.

## Part D — label in glucose

In a synthetic hepatocyte tracer model, label from uniformly ¹³C-labeled alanine appears in 18% of newly made glucose carbon, and label from uniformly ¹³C-labeled leucine appears in 3% of glucose carbon and 22% of ketone-body carbon. Compare the glucose labeling and decide what the leucine result supports. Leucine's carbon products are acetyl-CoA and acetoacetate; ask whether label can reach glucose without a net gain of oxaloacetate.

## Part E — a buried substitution

A buried leucine in fictional Protein M is replaced by aspartate. Under matched conditions the ligand's Kd rises from 15 nM to 120 nM, and the same ligand binds an unrelated protein with Kd 2 μM. Decide what the Kd change shows, how to describe the substitution structurally, and which measurement would test whether part of the variant is simply unfolded.

## Worked calculation

Take a culture that routes 20.0 μmol nitrogen to urea and contains 2.5 million viable cells. It forms 20.0/2 = 10.0 μmol urea, spending 3 × 10.0 = 30.0 μmol ATP molecules and 4 × 10.0 = 40.0 μmol high-energy phosphate equivalents, and its urea per million viable cells is 10.0/2.5 = 4.00 μmol. Averaging cultures after this normalization weights each culture equally. Dividing a condition's mean urea by its mean cell count is a different calculation and gives a different answer whenever cell numbers differ.

## Analytic instructor rubric

For instructor-led discussion, use 0–2 points for each criterion: 0 for absent or incompatible evidence, 1 for a partly correct response that omits a key assumption, 2 for the evidence described. This guide is not connected to the software gradebook.

| Criterion | Evidence for full credit |
| --- | --- |
| Charge model | Sums the six group types at each pH with the correct sign conventions and links the net-negative charge above the pI to an anion exchanger. |
| Nitrogen ledger | Converts nitrogen to urea and phosphate equivalents per culture and normalizes each culture before averaging. |
| Energy and donors | Explains the ATP-to-AMP step, names aspartate as the second nitrogen donor and keeps the ledger a demand, not a rate. |
| Carbon fate | Keeps label appearance separate from net glucose carbon and keeps leucine exclusively ketogenic. |
| Binding evidence | Reads Kd as equilibrium affinity, does not infer rates or specificity, and proposes a folded-fraction measurement. |

The autograded practice covers a subset of these criteria with deterministic numeric, CSV and structured-choice rules. Its keys are open in this repository. Written explanations are not scored automatically.

## Limitations and provenance

Original exercise with constructed values. Protein K, Protein M, the cultures and the tracer percentages are fictional; nothing here describes a real protein, cell line, person or experiment, and no laboratory protocol or medical interpretation is given. Real pKa values shift inside folded proteins, and real nitrogen disposal involves other products and pools. Original packet and synthetic dataset: CC BY 4.0.
