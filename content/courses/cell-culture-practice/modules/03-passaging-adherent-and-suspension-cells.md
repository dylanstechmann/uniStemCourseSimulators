# Passaging adherent and suspension cells

**Status:** Original, unreviewed formative instruction for outline lesson 3 of the partial Cell Culture Practice package. All cultures, observations, counts and outcomes are synthetic; the simulation rehearses decisions and arithmetic, not physical technique or laboratory validation.

Passaging, or subculturing, transfers cells from an actively growing culture into fresh medium so that space and nutrients do not become limiting. The decision begins with the culture's growth state, not with a calendar entry. It ends with a traceable new culture whose identity, passage history and intended starting density are known. This lesson compares adherent and suspension workflows conceptually; its [adherent target-density bench simulation](#/bench/passage-an-adherent-line-to-a-target-density) models only the adherent workflow with a generic, non-human mammalian cell line.

This is lesson 3 of the outlined cell-culture layer, scheduled as week 4 after lesson 2 in week 3. The hemocytometer lesson (outline lesson 4, scheduled in week 2) is the counting prerequisite: dilution factors, two-chamber tallies, dye-exclusion limits and sampling error are applied here rather than retaught. Nothing in this reading or simulation establishes competency, physical skill, institutional authorisation or a validated culture protocol. Cell-line instructions and institutional procedures govern real work.

## Learning objectives

By the end of this lesson, you should be able to:

1. Evaluate confluence or suspension density, morphology and viability evidence to decide whether a synthetic culture should be passaged, held for investigation or discarded under the scenario's rule.
2. Explain adherent detachment, washing, dissociation-reagent neutralization and resuspension, and contrast them with suspension passaging by direct dilution or transfer of a culture portion.
3. Calculate viable-cell concentration, required cell-suspension volume and fresh-medium volume for a specified viable-cell target and final culture volume.
4. Distinguish split ratio from target-density seeding, and calculate population doubling level (PDL) and cumulative PDL from starting and harvested cell numbers.
5. Evaluate passage records and the risks of repeated subculture, including the need for later authentication and the limits of numerical or simulated evidence.

## Read the culture before choosing a workflow

Adherent cells need a suitable surface; suspension cells grow without attaching to one. For either format, passaging is intended to maintain active growth rather than rescue a culture whose identity, sterility or growth behaviour is already doubtful. Thermo Fisher's Gibco maintenance guidance links subculture timing to growth phase and recommends following the cell line's own instructions. Its adherent protocol also uses viability and detachment observations during the workflow.

**Confluence** is the fraction of available adherent growth surface covered by cells. It is an estimate made alongside morphology, medium appearance, recent growth and viability, not a universal biological switch. This course uses **70–85% confluence** as its synthetic routine-passage window. A separate **95%** scenario is deliberately outside that window: the correct simulation disposition is to refuse routine passaging and select the over-confluent discard/investigation branch. These thresholds are simulation choices, not laboratory acceptance criteria; they are not taken from Thermo Fisher, and they must not be transferred to a real cell line.

A high dye-exclusion value does not cancel an unfavourable growth state, and a favourable confluence estimate does not establish identity or sterility. Unexpected morphology, an abnormal growth rate or a turbid culture calls for the contamination reasoning from lesson 1 and the later contamination lesson, not automatic passaging. Suspension cultures have no surface-confluence percentage. Their density, clumping, medium condition and cell-line-specific growth range serve the corresponding role.

## Adherent passaging: preserve a representative, viable suspension

The Thermo Fisher adherent page presents the general sequence used here: inspect the culture, remove spent medium, wash with calcium- and magnesium-free balanced salt solution, add a dissociation reagent, observe detachment, add complete medium, collect and resuspend the cells, count them and seed at the cell line's recommended density. The wash reduces carry-over of serum, calcium and magnesium that can interfere with dissociation. The lesson uses the generic name **enzyme-based dissociation reagent**; the source names trypsin and TrypLE as examples, but this course does not select a product or claim interchangeable formulations.

The source gives approximate scaling of 2 mL wash per 10 cm² and 0.5 mL dissociation reagent per 10 cm². For the simulation's **75 cm² T-75** these proportional calculations are:

  wash volume = 75/10 × 2 = **15 mL**

  dissociation-reagent volume = 75/10 × 0.5 = **3.75 mL**

Those exact flask volumes are declared simulation choices derived from the linked general protocol, not a reproduced manufacturer SOP. The model also fixes a **2 min** default incubation, checks detachment before neutralization, and treats **1–5 min** as its teaching bound. The source instead describes an approximately two-minute start followed by short checks because actual dissociation varies by cell line. In the model, at least **90% detachment** is required before proceeding, and exposure beyond five minutes lowers synthetic viability. This simple penalty demonstrates why “longer is better” is false; it is not a kinetic or physical cell-damage model.

When detachment is sufficient, complete growth medium is added to stop or dilute the dissociation activity as appropriate for the reagent system. The simulation requires **7.5 mL**, twice its 3.75 mL reagent volume, following the general source's two-volume relationship. Missing or inadequate neutralization lowers the model's viability. It then models collection at **200 × g for 5 min**, followed by resuspension in **6.0 mL**. The source gives 200 × g for 5–10 min while stressing cell-type dependence. Resuspend gently until the sample is representative; unresolved clumps and settling can bias the count even when the arithmetic is correct.

## Suspension passaging: dilution without substrate detachment

A suspension culture is already dispersed in medium, so there is no substrate-detachment step. Thermo Fisher's suspension page describes taking a representative sample after mixing, determining density and viability, and either adding medium directly or transferring a portion before dilution to the desired starting density. Some workflows concentrate and replace medium first; vessel mixing, gas exchange and cell-line-specific limits still matter.

The arithmetic is the same conservation relationship used for adherent seeding. If a suspension is at 1.6 × 10⁶ viable cells/mL and the intended starting concentration is 0.4 × 10⁶ viable cells/mL in 20 mL, the culture needs 0.4 × 10⁶ × 20 = 8.0 × 10⁶ viable cells, hence 8.0/1.6 = 5.0 mL of original suspension and 15.0 mL fresh medium. This is a synthetic example, not a recommended suspension density. **The bench simulator does not model suspension vessels, shaking, centrifugation choices or suspension growth.**

## Target-density seeding with C₁V₁ = C₂V₂

For seeding, interpret C₂V₂ as the **total number of viable cells wanted in a new vessel**, not necessarily a concentration. If C₁ is viable cells/mL in the harvested suspension and N_target is viable cells wanted per flask,

  V_cell suspension per flask = N_target / C₁.

Fresh medium is then the final culture volume minus the cell-suspension volume. Do not add a full final volume of medium to the inoculum: that makes the final volume too large. For several identical flasks, calculate the per-flask inoculum first, then multiply both cells and volume by the flask count. Check that the plan is feasible: the inoculum must fit within the final volume and the harvested suspension must contain enough viable cells.

**Worked example 1: two T-75 flasks.** A 10 µL + 10 µL trypan-blue preparation gives a twofold dilution. The displayed tallies are chamber A 58 unstained + 5 stained and chamber B 63 unstained + 4 stained. With one 10⁻⁴ mL large square per chamber:

  viable concentration = (58 + 63)/2 × 10,000 × 2 = **1.21 × 10⁶ viable cells/mL**

  viability = 121/(121 + 9) × 100 = **93.1%**

  viable harvest in 6.0 mL = 1.21 × 10⁶ × 6.0 = **7.26 × 10⁶ cells**

Each of two flasks is to receive 5.00 × 10⁵ viable cells in a **12.0 mL final volume**:

  V_cells = 5.00 × 10⁵ / (1.21 × 10⁶) = **0.413223 mL per flask**

  V_fresh medium = 12.0 − 0.413223 = **11.586777 mL per flask**

The simulation accepts a 0.5% numerical rounding allowance for seed volume; this is a grading tolerance, not pipetting accuracy or an acceptance limit. The two flasks together need 1.00 × 10⁶ viable cells and 0.826446 mL suspension. Use unrounded intermediates for subsequent calculations.

## Split ratio is not a target density

A split ratio records a proportional transfer, such as 1:4. It does not by itself establish how many viable cells enter a vessel, because harvest concentration, viability, transferred volume and final volume can change. Target-density seeding begins with a count and a required cell number. The two descriptions can be recorded together, but neither should be inferred from the other without the missing volumes.

If a harvest contains 8.0 × 10⁶ viable cells and 2.0 × 10⁶ are seeded in total, the yield-based split denominator is 8.0/2.0 = 4, described here as **1:4**. This convention must be written explicitly because people use “split ratio” language for related but non-identical ratios. The simulation uses target-density planning rather than assuming a fixed split ratio.

## Population doubling level and the passage record

**Passage number** counts subculture events; it is not the number of cell doublings. Population doubling level uses the starting and final cell numbers for an interval:

  PDL increment = log₁₀(Nf/N0) / log₁₀ 2 = log₂(Nf/N0).

For the simulation's previous interval, N0 = 1.815 × 10⁶ viable cells and Nf = 7.26 × 10⁶ viable cells, so Nf/N0 = 4 and the increment is log₂4 = **2.00**. If the previous cumulative PDL was 18.00, the new value is 18.00 + 2.00 = **20.00**. This model deliberately uses viable-cell yield for its synthetic PDL exercise; a laboratory must state its own counting convention and account for any cells discarded during intermediate steps. A ratio below one gives a negative increment and signals that the interval cannot be described as exponential expansion without investigation.

A useful record includes line and vessel identifiers, date, operator, starting confluence or density, morphology, dissociation and neutralization details, dilution and raw chamber tallies, viable concentration, viability, total yield, target and actual seed numbers, final volume, medium and reagent lots, previous and new passage number, PDL increment and cumulative PDL. The simulator checks the arithmetic fields, not whether a free-text record is complete.

Thermo Fisher's maintenance guidance warns that repeated subculture can alter cell characteristics and genomic stability and recommends detailed logs. A high passage number alone neither proves drift nor identifies its mechanism. Use earlier, well-characterised stocks where appropriate and carry forward unusual morphology, growth or marker evidence to the planned lesson 6 discussion of contamination, mycoplasma and authentication. Authentication and periodic quality checks are not replaced by a PDL ledger or a high viability reading.

## Practise in the adherent bench simulation

Open the [adherent target-density simulation](#/bench/passage-an-adherent-line-to-a-target-density). Inspect the synthetic confluence, choose the culture disposition, complete washing and dissociation, confirm detachment, neutralize, collect and resuspend, enter the two-chamber count, plan two flasks and complete the passage/PDL record before incubation. The debrief has **16 checkpoints** and reports your concentration, viability, harvest, per-flask inoculum, fresh-medium volume and PDL. A normal run uses the worked values above. Some seeded runs instead show 95% confluence and should end at the disposition decision.

The hidden confluence and detachment draws, 70–85% routine window, 95% refusal scenario, five-minute teaching bound, viability penalties, two-flask target, 6.0 mL resuspension, 0.5% seed-volume tolerance and 0.01-PDL tolerance are explicit simulation choices. The final 37 °C, 5% CO₂, 24 h incubation is only a record of simulated conditions; the model does not predict attachment, growth, phenotype, sterility or future viability. No checkpoint is a physical validation or competency record.

## Common mistakes

- Passaging by date alone, or treating 95% confluence as equivalent to the synthetic routine window.
- Washing with complete medium, extending enzyme exposure indefinitely, or counting before neutralization.
- Applying an adherent detachment workflow to cells already growing in suspension.
- Using total rather than viable cells for a viable-cell target, or forgetting the dye dilution.
- Adding 12 mL medium to the inoculum instead of bringing the combined volume to 12 mL.
- Treating a 1:4 split as proof of a known viable seeding density.
- Confusing passage number with PDL, or treating either as authentication evidence.
- Reading a successful simulation as evidence of hand skill, sterility or future culture growth.

## Scope and sources

| Statement in this lesson | Basis and reuse |
| --- | --- |
| General adherent sequence; calcium/magnesium-free wash; dissociation observation; two volumes of complete medium; collection, counting and cell-line-specific seeding | Thermo Fisher Scientific, Gibco Cell Culture Basics, “Adherent Cell Culture Protocol”, opened 2026-11-15; copyrighted, link-only reference; no source text or figure reproduced |
| Suspension sampling, direct dilution or transfer of a portion, density/viability assessment and cell-line-specific vessel considerations | Thermo Fisher Scientific, Gibco Cell Culture Basics, “Suspension Cell Culture Protocol”, opened 2026-11-15; copyrighted, link-only reference |
| Seeding-volume relationship, final-volume adjustment, growth-phase context, detailed logs and repeated-subculture risks | Thermo Fisher Scientific, Gibco Cell Culture Basics, “Seeding, Subculturing, and Maintaining Cells”, opened 2026-11-15; copyrighted, link-only reference |
| Scope comparison only: MIT 20.109 Spring 2010 lists initiating cell culture and viability work within a broader biological-engineering course, not a stand-alone passaging course | MIT OpenCourseWare syllabus/calendar, opened 2026-11-15; CC BY-NC-SA 4.0 confirmed in the page footer; link-only comparator, no equivalence claimed |
| Exact T-75 volumes, confluence window and refusal scenario, time bound, count fields, target densities, viability penalties, PDL convention and numerical tolerances | Synthetic simulation choices documented in the protocol; not laboratory acceptance criteria |

All examples and results are original synthetic data developed with substantial AI assistance. Source URLs, licence decisions and access dates are recorded in the integrated package's `source-map.json` and source registry. No text, table, image, problem or dataset was copied from a linked source.
