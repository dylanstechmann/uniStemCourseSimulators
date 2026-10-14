# Experimental design for cell mechanics

Mechanobiology experiments often change a material property while cells also respond to ligand presentation, geometry, preparation batch, and their own state. A design must make those variables distinguishable. Crossing factors, measuring what cells actually experience, and defining the independent experimental unit before collecting observations turn a comparison into an interpretable test.

## Cross factors to separate their effects

Suppose the question is whether cell response changes with substrate stiffness, ligand density, or their combination. A 2×2 factorial design uses both low and high levels of each factor, with all four combinations represented:

| Stiffness | Low ligand density | High ligand density |
| --- | ---: | ---: |
| Soft | 10 | 14 |
| Stiff | 16 | 28 |

The values are synthetic response means in arbitrary units. The stiffness contrast is the average response on stiff substrates minus the average on soft substrates: $(16+28)/2-(10+14)/2=10$. The ligand-density contrast is the high-density average minus the low-density average: $(14+28)/2-(10+16)/2=8$. The interaction is a difference of differences: the stiffness effect at high ligand density, $28-14=14$, minus its effect at low ligand density, $16-10=6$, giving 8. A nonzero interaction means the observed stiffness contrast depends on ligand density in this example; it is not a claim that the same values apply to a real cell system.

If stiffness and ligand density always change together, their separate effects cannot be estimated from those observations alone. A crossed design prevents one factor from standing in for the other, although it does not automatically control every material property. Hydrogels can also differ in ligand coupling, swelling, pore structure, topography, and viscoelastic relaxation. Measure and report the material properties relevant to the cell-facing surface, and check whether the method used to change stiffness also changes ligand availability or mobility.

## Define assignment and replication

The **experimental unit** is the independently prepared unit that receives a condition. If stiffness and ligand density are assigned to independently fabricated gels or dishes, those gels or dishes provide the independent replication. Cells measured within a gel share its material preparation and environment. They provide subsamples that can describe within-gel heterogeneity, but counting each cell as an independent replicate would exaggerate the amount of independent evidence.

For example, three independently prepared gels per condition with twenty cells measured on each produce sixty cell observations per condition but only three independently assigned gels. One option is to summarize cells within each gel and compare gel-level values. A hierarchical model can retain cell-level observations while representing cells nested within gels and gels nested within preparation batches or donors. The analysis should reflect the actual assignment and sampling structure; a more complex model cannot create independent replication that the design did not collect.

Batch and donor variation can be handled in the design as well as in the analysis. When feasible, distribute all four conditions across each preparation batch so that batch is not identical to stiffness or ligand level. Randomize condition position and processing order within a batch, and record donor or cell-source information. If each batch receives only one condition, a batch effect can be indistinguishable from the condition effect.

## Verify the cue and measure a defined response

The nominal label “soft” or “high ligand” is not the measurement. Characterize stiffness using a stated method and relevant deformation range; quantify ligand density or coupling with a suitable measurement; and document other material features that may co-vary. Verify that the material remains comparable over the exposure and measurement window. A surface coating can change access to the underlying material, while swelling or relaxation can change the mechanics presented to cells.

Choose one primary endpoint before interpreting the results, state when and how it will be measured, and define the contrast of interest. Include controls that test the measurement range and biological responsiveness, and include negative or baseline comparisons appropriate to the question. Image fields with a prespecified selection rule and blinded analysis where practical. Representative images can illustrate a result but cannot substitute for the distribution of observations or for independent preparations.

**Worked design.** In the synthetic table, the stiffness contrast is 10 units on average, but it differs by ligand level: 6 units at low density and 14 at high density. Reporting only the average stiffness contrast would hide that the response pattern depends on the second factor. A suitable summary includes the four cell-condition means, the two main contrasts, the interaction contrast, and uncertainty based on the independent units. If twenty cells are nested within each gel, uncertainty should not be computed as though all cells were independent gels.

## Plan precision around independent units

More measured cells can improve the estimate of a gel's mean or describe its heterogeneity, but they do not replace more independent gels or batches. Plan the number of independent units from the smallest effect that matters, between-unit variability, and the intended interaction test. Interaction estimates often need more independent information than a large main effect. Report effect sizes and uncertainty intervals, not just a thresholded significance result, and show batch or donor variation when it is part of the design.

Keep the primary endpoint, exclusion rules, factor levels, randomization, and analysis plan explicit before looking at outcome differences. Record preparation, calibration, imaging, and analysis versions so a later comparison can distinguish biology from a changed measurement pipeline. These principles support experimental reasoning; this lesson is not a hydrogel fabrication, cell-handling, or measurement protocol. All displayed values are synthetic.

## Common mistakes

- Changing stiffness and ligand density together, then attributing the response to one factor.
- Treating cells sampled from the same gel as independent experimental units.
- Assuming a factorial design controls unmeasured changes in swelling, topography, or ligand coupling.
- Reporting only a main effect when the response varies across the other factor.
- Showing representative images without a predefined endpoint, independent replication, or uncertainty.
