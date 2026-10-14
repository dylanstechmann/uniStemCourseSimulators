# Protein purification as quantitative evidence: selectivity, recovery and specific activity

Protein purification is a sequence of decisions about which properties can separate the target from the material around it. A fraction that looks enriched is not automatically pure, and a step that loses activity is not automatically useless. This lesson combines the charge and isoelectric-point model from week 2 with protein-binding ideas and enzyme activity measurements. All fraction values below are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Choose a protein-separation method from evidence about charge relative to pI, molecular size or a selective binding interaction, and state its limits.
2. Calculate total protein, total activity, specific activity, recovery and fold enrichment from fraction data, and distinguish enrichment from a claim of homogeneity.

## Match the separation to the property

**Ion exchange** separates molecules by net charge under the chosen buffer conditions. A protein is usually net negative at pH above its isoelectric point (pI) and can bind a positively charged **anion exchanger**. Below its pI, it is usually net positive and can bind a negatively charged **cation exchanger**. The exchanger name describes the ions the matrix binds. If a fictional protein has pI 6.2 and remains stable at pH 7.5, an anion exchanger is a reasonable first choice. This does not guarantee binding: surface charge patches, salt concentration, the sample’s other proteins and the matrix all affect separation. A pH outside the protein’s stability range is a poor choice even if the predicted charge is favorable.

**Size-exclusion chromatography (SEC)** separates by hydrodynamic size. Within a column’s useful fractionation range, larger particles enter fewer pores and therefore elute earlier; smaller molecules enter more pore volume and elute later. SEC can separate proteins of sufficiently different sizes or remove small molecules from a protein fraction, but it has little resolving power for proteins of similar hydrodynamic size. Shape and oligomerization can change hydrodynamic size, so elution volume is not a direct molecular-mass measurement without an appropriate calibration.

**Affinity chromatography** uses a ligand that binds the target, such as a substrate-like ligand, antibody or engineered tag partner. The selective interaction can separate a target from many unrelated proteins in one step. Selectivity depends on the ligand and conditions: a buried tag, weak binding, nonspecific matrix interactions or a condition that disrupts target activity can reduce useful recovery. An affinity step is not evidence that all contaminants are gone.

These methods answer different questions. Ion exchange asks whether molecules differ in charge under the selected conditions; SEC asks whether they differ in hydrodynamic size; affinity asks whether one molecule binds a chosen ligand. A convincing purification strategy uses orthogonal properties rather than repeating the same weak separation. A denaturing SDS-PAGE gel can show an approximate subunit-size pattern and reveal some contaminants, but bands can co-migrate and the treatment does not preserve native complexes or demonstrate enzyme activity.

## Read a purification table

For an enzyme, define one activity unit (U) as 1 μmol of product formed per minute under one fixed, stated assay condition. For each fraction:

- Total protein (mg) = volume (mL) × protein concentration (mg/mL).
- Total activity (U) = volume (mL) × activity concentration (U/mL).
- Specific activity (U/mg) = total activity ÷ total protein.
- Activity recovery (%) = fraction total activity ÷ starting total activity × 100.
- Fold enrichment = fraction specific activity ÷ starting specific activity.

| Fraction | Volume (mL) | Protein (mg/mL) | Activity (U/mL) | Total protein (mg) | Total activity (U) | Specific activity (U/mg) | Recovery (%) | Fold enrichment |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Crude extract | 50 | 2.00 | 120 | 100 | 6,000 | 60 | 100 | 1.00 |
| Ion-exchange pool | 20 | 0.80 | 210 | 16 | 4,200 | 262.5 | 70 | 4.375 |
| Affinity pool | 8 | 0.10 | 420 | 0.8 | 3,360 | 4,200 | 56 | 70 |

The affinity pool contains much less total protein and has 70-fold higher specific activity than the crude extract, while retaining 56% of its measured activity. The rise in specific activity is evidence of enrichment only if the same assay remains comparable across fractions and the measured activity belongs to the target. It does not establish a single-protein preparation: an inhibitor removed during purification can raise measured activity, a target can lose activity, and a contaminant can contribute to the assay. Orthogonal evidence, such as a gel plus a target-specific assay, strengthens the claim but still has its own detection limits.

Recovery and enrichment are different goals. A step may sharply reduce total activity yet greatly increase activity per milligram. That trade-off may be acceptable if the goal is a clean mechanistic assay and enough active material remains; it may be unacceptable if the next experiment requires a large yield. When activity drops, consider target loss, denaturation, oxidation, inhibitor carryover, assay interference and dilution before deciding that the target protein was physically lost. Compare fractions using the same assay definition, blank correction and dilution range.

## Worked example

**Problem.** A synthetic affinity fraction has a volume of 12 mL, a total-protein concentration of 0.25 mg/mL, and an activity concentration of 90 U/mL. The starting extract had 6,000 U total activity and 60 U/mg specific activity. Calculate total protein, total activity, recovery and fold enrichment.

**Step 1: total protein.** 12 mL × 0.25 mg/mL = 3.0 mg.

**Step 2: total activity.** 12 mL × 90 U/mL = 1,080 U.

**Step 3: recovery.** 1,080/6,000 × 100 = 18%.

**Step 4: specific activity and enrichment.** 1,080/3.0 = 360 U/mg; 360/60 = 6-fold.

The result describes the activity recovered under the specified assay and the increase in activity per measured protein. It does not say that 18% of all target molecules remain, because inactive target molecules are not counted as activity.

## Common mistakes

- Calling an anion exchanger a negative matrix; it is positively charged and binds negatively charged species.
- Assuming SEC always separates by exact molecular mass, even when shape or aggregation changes hydrodynamic size.
- Treating specific activity as a direct purity measurement without checking assay comparability or co-migrating contaminants.
- Reporting recovery from protein mass when the table defines recovery from total enzyme activity.
- Concluding that lower activity proves the protein was lost instead of considering inactivation or assay interference.

## Practice boundaries and references

The accompanying items use the same synthetic fraction table and permit unlimited retries; they are not collected or graded. No laboratory procedure is provided. For optional method background, see Cytiva’s [protein purification strategies handbook](https://cdn.cytivalifesciences.com/api/public/content/digi-15680-pdf), [ion-exchange chromatography handbook](https://cdn.cytivalifesciences.com/api/public/content/digi-13101-original), and [size-exclusion chromatography handbook](https://cdn.cytivalifesciences.com/api/public/content/digi-11639-original). These are link-only technical references; no handbook text, table or figure is reproduced here.
