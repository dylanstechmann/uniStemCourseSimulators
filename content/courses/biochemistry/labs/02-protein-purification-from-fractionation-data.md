# Virtual purification lab: fraction recovery and enrichment

**Activity type:** synthetic-data analysis with public, ungraded formative checks  
**Data status:** all fraction measurements are fictional and constructed for instruction. They describe no real protein, preparation or experiment.  
**Dataset:** [synthetic fraction table (CSV)](protein-purification-fractions.csv).

## Question

A fictional enzyme activity is tracked through four fractions. The purpose of this virtual lab is to determine how the amount of protein and measured activity change across the sequence, then decide what the data support about enrichment. The exercise uses an already-provided table. It gives no experimental procedure or laboratory protocol.

## Learning objectives

1. Calculate total protein and activity, specific activity, recovery and fold enrichment from fraction data.
2. Choose an orthogonal separation property and explain why higher specific activity does not by itself prove homogeneity.

## Data dictionary and observations

`volume_ml` is the measured fraction volume; `protein_mg_per_ml` is protein mass per volume; and `activity_U_per_ml` is activity under one fixed synthetic assay definition. One unit (U) means one micromole of product per minute in this fictional assay. The values are deliberately simple teaching data, not reference values.

| Fraction | Volume (mL) | Protein (mg/mL) | Activity (U/mL) |
|---|---:|---:|---:|
| Crude extract | 50 | 2.00 | 120 |
| Salt fraction | 25 | 1.20 | 160 |
| Ion-exchange pool | 10 | 0.80 | 300 |
| Size-exclusion pool | 5 | 0.30 | 400 |

## Analysis

For every fraction calculate:

- Total protein = volume × protein concentration.
- Total activity = volume × activity concentration.
- Specific activity = total activity ÷ total protein.
- Recovery = fraction total activity ÷ crude total activity × 100%.
- Fold enrichment = fraction specific activity ÷ crude specific activity.

Keep units visible while calculating. A value in U/mL is not total activity until it is multiplied by volume. A value in U/mg reports activity per measured mass; it is not a direct measurement of purity.

## Work sequence

1. Build a table with total protein, total activity, specific activity, recovery and enrichment for each fraction.
2. Compare the ion-exchange and size-exclusion pools. State which metrics improve and which measure the amount of activity retained.
3. Explain why a size-exclusion step uses hydrodynamic size and why it can be orthogonal to a charge-based ion-exchange step. The data do not include a calibrated molecular-size standard, so they cannot show how well a particular pair of proteins would resolve.
4. State what additional evidence could test homogeneity, and name a limitation of that evidence. For example, a band pattern can miss co-migration, while a target-specific activity assay can be affected by substrate specificity or inhibitors.

## Worked calculation

The crude fraction contains 50 mL × 2.00 mg/mL = 100 mg total protein and 50 mL × 120 U/mL = 6,000 U total activity. Its specific activity is 60 U/mg and defines 100% recovery and 1-fold enrichment for this comparison. Every later fraction is compared with this same baseline. If the assay conditions differ between fractions, the recovery and enrichment comparison is not valid without a correction.

## Worked comparison across all fractions

Use the crude extract as the common baseline for every row. The displayed values are rounded to three significant figures; calculate with unrounded products before rounding.

| Fraction | Total protein (mg) | Total activity (U) | Specific activity (U/mg) | Activity recovery (%) | Fold enrichment |
|---|---:|---:|---:|---:|---:|
| Crude extract | 100 | 6,000 | 60.0 | 100 | 1.00 |
| Salt fraction | 30.0 | 4,000 | 133 | 66.7 | 2.22 |
| Ion-exchange pool | 8.00 | 3,000 | 375 | 50.0 | 6.25 |
| Size-exclusion pool | 1.50 | 2,000 | 1,330 | 33.3 | 22.2 |

For example, the salt fraction has 25 mL × 160 U/mL = 4,000 U total activity and 4,000 U ÷ 30.0 mg = 133 U/mg. Relative to crude extract, it retains 4,000 ÷ 6,000 × 100% = 66.7% of the measured activity and has 133 ÷ 60.0 = 2.22-fold specific-activity enrichment. By the size-exclusion pool, specific activity is higher while activity recovery is lower. These are separate measurements; neither value alone says how much target protein remains or whether it is homogeneous.

There is only one synthetic observation per fraction, so the table cannot estimate replicate variability, a standard deviation or a confidence interval. Repeat independent preparations and assay replicates would be needed to describe measurement variability. The present exercise keeps the arithmetic separate from that unmeasured uncertainty.

## Interpretation and limits

A sequence can retain less total activity while increasing activity per milligram. That pattern is compatible with removing some contaminants, but it does not prove that all measured activity comes from one protein or that every target molecule remains active. Apparent activity can change when inhibitors are removed, the target is inactivated, a contaminant contributes to the signal, or dilution moves a sample into a more reliable assay range. Compare only measurements made under the same stated assay definition.

Size-exclusion chromatography separates by hydrodynamic size within a useful range. It may add a different separation property after charge-based ion exchange, but this synthetic table contains no elution profile and makes no claim that an actual separation occurred. A staged table is a way to reason about evidence, not a recipe for performing chromatography.

## Common mistakes

- Multiplying protein concentration by activity concentration instead of calculating each total from volume.
- Calculating recovery from protein mass rather than total activity.
- Calling a rise in specific activity a purity measurement.
- Assuming that a lower recovery means the target protein was physically lost.
- Claiming a separation from a table that contains no elution or resolution data.

## Practice boundaries

The seven associated questions are public formative checks with unlimited retries. They are not collected or graded. All observations are synthetic; no laboratory protocol, medical advice or inference about a real protein is provided. Workload has not been measured.
