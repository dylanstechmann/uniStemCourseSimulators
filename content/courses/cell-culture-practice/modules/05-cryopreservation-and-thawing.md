# Cryopreservation and thawing

**Status:** Original, unreviewed formative instruction for outline lesson 5 of the partial Cell Culture Practice package. Every cell, count, storage location and outcome is synthetic. The simulation rehearses decisions and arithmetic; it is not a validated laboratory protocol or evidence of physical technique.

Cryopreservation pauses a cell culture's need for continuous passage by taking a characterised, viable stock through a controlled freezing and recovery workflow. The useful result is not merely a cold vial: it is a traceable bank entry whose location, contents, quality status and relationship to other stocks remain interpretable. This lesson links harvest and counting to a same-run freeze, storage, thaw and recount in the [freeze-and-thaw bench simulation](#/bench/freeze-and-thaw-with-viability-outcomes).

This is outline lesson 5, scheduled as week 5. Lessons 1 and 4 supply aseptic and counting prerequisites; lesson 3 supplies harvest arithmetic. Lesson 8 will develop bank-tier and chain-of-records detail. Nothing here establishes competency, institutional authorisation or physical validation. Cell-specific instructions, risk assessments and institutional procedures govern actual work.

## Learning objectives

By the end of this lesson, you should be able to:

1. Distinguish permeating from non-permeating cryoprotectants, and relate DMSO concentration, cold dropwise handling and removal to freezing protection, osmotic stress and toxicity.
2. Explain the two-factor account of freezing injury and use it to justify controlled cooling, an appropriate passive container or controlled-rate device, and rapid thawing.
3. Calculate freeze-medium component volumes, vial counts and concentrations, post-thaw dilution and residual DMSO fractions, and viable-cell recovery.
4. Evaluate vapour- versus liquid-phase nitrogen storage, fast-thaw and recount decisions, including the safety rationale and limits of dye-exclusion viability.
5. Evaluate quarantine, quality-control status, storage-location records and bank-tier links without treating a simulation result as a release decision.

## Cryoprotectants change the freezing problem, not just the freezing point

A **permeating cryoprotectant** crosses the cell membrane and distributes between intracellular and extracellular compartments. DMSO and glycerol are standard examples. Lovelock and Bishop's 1959 *Nature* report established DMSO as a protective permeating solute in their experimental systems; it did not establish one universal formulation for every cultured cell. Permeating solutes can limit damaging electrolyte concentration and alter ice formation, but their protective concentration window is bounded by toxicity and osmotic consequences.

A **non-permeating cryoprotectant** remains predominantly extracellular. Examples discussed by Murray and Gibson include trehalose, poly(vinyl pyrrolidone) and hydroxyethyl starch. These materials can alter extracellular ice behaviour, solution properties and osmotic stresses. They are not inert “external DMSO equivalents”: their mechanisms differ, some are used in combination with permeating agents, and suitability is cell- and process-specific. Liquid nitrogen is the storage refrigerant, not a cryoprotectant.

The simulator uses a simple **10% v/v DMSO** teaching formulation. That number is consistent with one general option on Thermo Fisher's freezing page, but the exact medium, density and procedure here are simulation choices, not a reproduced product protocol or a universal recommendation. No serum-containing, serum-free or commercial formulation is implied to be interchangeable.

### Cold, dropwise DMSO handling

DMSO protection during freezing does not make prolonged exposure harmless at culture temperature. The simulation therefore prepares the freezing medium cold, keeps it at **4 °C**, and adds DMSO by the **`cold_dropwise`** method with mixing rather than as a room-temperature single bolus. This conservative teaching rule limits abrupt local concentration gradients and warm exposure. The linked Thermo page supports cold freezing medium and cell-line-specific handling; the precise 4 °C, dropwise implementation is a declared simulation choice rather than a quoted manufacturer requirement.

The same distinction matters after thawing. Rapid warming limits time spent with changing ice, while subsequent slower dilution avoids asking cells to tolerate an abrupt osmotic transition and continued high DMSO exposure. “Fast everything” is therefore the wrong summary: **thaw fast, then dilute gradually and remove DMSO promptly according to the selected workflow**.

## Two routes to freezing injury

Mazur's 1970 review, *Cryobiology: The Freezing of Biological Systems*, is the classic primary reference for the physical basis of freezing responses. The correct citation is *Science* **168**, 939–949, DOI **10.1126/science.168.3934.939**. The later two-factor account distinguishes two competing dangers:

- **Cooling too slowly** prolongs exposure to the concentrated, dehydrated solution environment created as extracellular water becomes ice. These “solution effects” include osmotic and chemical stresses; extracellular ice is not simply harmless because it is outside the cell.
- **Cooling too rapidly** leaves too little time for intracellular water to leave before internal ice forms. Intracellular ice and its later growth can be lethal.

A favourable intermediate rate balances these risks; it is not identical for every cell and suspension. Thermo Fisher's general protocol uses approximately **1 °C/min**, either with a controlled-rate freezer or with a passive freezing container placed at **−80 °C overnight**. This simulation accepts `controlled_rate` or `passive_container` at 0.8–1.2 °C/min for a 16 h hold. `uncontrolled_freezer` represents the missing-container mistake: merely putting an uncovered vial into a freezer does not establish the intended cooling history. The rate tolerance, hold time and viability penalty are synthetic, not equipment specifications or cell-line acceptance criteria.

Warming reverses the journey through hazardous temperature zones. The general thawing reference calls for prompt transfer to **37 °C** and a rapid thaw until only a small amount of ice remains. The model uses **45 s**, accepts no more than 60 s at 37 °C with that endpoint, and assigns a synthetic viability penalty to a slow thaw. A slow thaw is not “gentler”: it can extend exposure to recrystallisation and concentrated solutes.

## Vapour-phase nitrogen and the location record

The freezing reference directs transfer after the initial cooling hold to the **gas (vapour) phase above liquid nitrogen**, below −135 °C, and explains that vapour storage reduces vial-explosion risk relative with liquid immersion. Liquid phase is colder in a simple temperature comparison, but “coldest is safest” ignores nitrogen entry, leakage and pressure hazards. This lesson therefore selects `vapour` at a synthetic **−150 °C** display. Liquid-phase storage fails the simulation's storage-safety checkpoint even when its numerical post-thaw viability is unchanged. Real dewar design, vial closure, biohazard controls, personal protection and local rules remain outside the model.

A vial without a retrievable address is not a usable bank. The simulator requires a dewar, rack, box and position plus a bank-tier field. Its example record is **CRYO-A / R-02 / B-07 / D4**, `working_stock`. These identifiers are invented and contain no person, donor, patient or site information. Do not replace them with personal or sensitive source identifiers.

## Worked freeze-medium and aliquot arithmetic

A synthetic harvest has **2.00 × 10⁶ viable cells/mL**, **95.0%** dye-exclusion viability and **5.00 mL** suspension:

  viable harvest = 2.00 × 10⁶ × 5.00 = **1.00 × 10⁷ viable cells**

Four vials each contain **2.50 × 10⁶ viable cells in 1.00 mL**, so the batch requires 4 × 1.00 = **4.00 mL** final freezing suspension and has 1.00 × 10⁷/4.00 = **2.50 × 10⁶ viable cells/mL**. At 10% v/v DMSO:

  DMSO = 4.00 × 0.10 = **0.400 mL**

  base medium = 4.00 − 0.400 = **3.60 mL**

The calculation uses final volume, not “add 0.400 mL to 4.00 mL”; the latter would produce 4.40 mL and 9.09% v/v. The simulator checks component conservation, four equal aliquots and the viable-cell target. In a real procedure, losses, dead volume and the selected resuspension sequence must be reconciled rather than silently ignored.

## Thaw, dilute, remove DMSO and recount

For one vial, adding its **1.00 mL of 10% DMSO suspension to 9.00 mL** prewarmed complete medium gives 10.00 mL total:

  DMSO after dilution = 10% × 1.00/10.00 = **1.00% v/v**

The model then uses a synthetic **200 × g for 5 min** collection step, removal of supernatant with **95% of the DMSO solute removed**, and resuspension in **2.00 mL**. The original vial contained 0.100 mL DMSO. If 0.005 mL remains:

  residual DMSO = 0.005/2.00 × 100 = **0.250% v/v**

That 95% solute-removal value is an accounting assumption, not a measured extraction efficiency. Centrifugation does not “destroy DMSO”; the supernatant carries it away, while residual solute and any cell losses need separate consideration.

For the worked recovery panel, suppose the post-thaw count reports **92.0% viability**. Under the model's explicit assumption that total cell number is conserved from the vial's pre-freeze count:

  viable cells recovered = 2.50 × 10⁶ × (92.0/95.0) = **2.421053 × 10⁶ cells**

  viable concentration in 2.00 mL = 2.421053 × 10⁶/2.00 = **1.210526 × 10⁶ cells/mL**

  recovery relative to initially viable cells = 2.421053/2.50 × 100 = **96.8421%**

The 92/95 ratio is necessary because 95% was viability, not a statement that every cell in the vial was viable. In the simulator, a seeded baseline of 92% or 93% varies the panel, and incorrect handling multiplies synthetic factors. These transformations are not measured survival curves, heat-transfer calculations or predictions of attachment, growth, phenotype or sterility.

A recount is an observation at one time. Dye exclusion reports membrane integrity, not long-term recovery or identity. The model checks entered recovered viable cells, viability and concentration to a 0.2% rounding allowance; this is an arithmetic tolerance, not assay precision.

## Quarantine, QC and bank tiers

A newly produced stock remains **`quarantine_pending_qc`** until required quality evidence is reviewed. The simulation uses pending sterility status and an existing identity-reference record. A high post-thaw viability result cannot substitute for sterility, mycoplasma, identity or other required QC. “Release to routine use because the vial thawed” is therefore a mistake. Quarantine is a status and physical/record separation decision, not an assertion that the synthetic stock has actually been tested.

Thermo Fisher distinguishes seed stocks, protected from general use, from working stocks used and replenished for routine work. This lesson uses the more general **master-seed / working-stock** comparison as a forward link to lesson 8: preserve provenance and minimise unnecessary generations when expanding a replacement working stock from an earlier-tier stock. The lesson does not teach a complete banking SOP, release specifications, audit trail or chain of custody.

## Practise the complete freeze–thaw loop

Open the [freeze-and-thaw simulation](#/bench/freeze-and-thaw-with-viability-outcomes). Record the harvest/count, prepare the 10% DMSO medium, add it cold and dropwise, aliquot four vials, select controlled cooling, transfer to vapour storage and record the address. Then thaw one vial in the same run, dilute and remove DMSO, enter the recount, quarantine the stock pending QC and finish. The debrief has **15 checkpoints** and a structured result containing composition, aliquots, cooling/storage records, post-thaw DMSO, viability, viable recovery and quarantine/bank fields.

Hidden baseline recovery and all multipliers are synthetic. Room-temperature DMSO, a missing cooling container and slow thaw reduce synthetic viability; liquid-phase storage fails a separate safety checkpoint. No output establishes physical validation, competency, future growth, identity, sterility or suitability for release.

## Common mistakes

- Calling every cryoprotectant “DMSO”, or treating liquid nitrogen as a cryoprotectant.
- Adding DMSO rapidly at room temperature because toxicity matters only after thawing.
- Adding 10% of the starting volume instead of calculating 10% of the final volume.
- Assuming any time in a −80 °C freezer gives a controlled 1 °C/min history.
- Treating extracellular ice as harmless or very fast cooling as always protective.
- Choosing liquid immersion because a lower temperature must be safer overall.
- Thawing slowly, then adding a large medium volume abruptly or leaving DMSO in the culture.
- Comparing post-thaw viable cells only with the initial viable count without accounting for pre-freeze viability.
- Releasing a new stock because it has high membrane-integrity viability, or recording only “in the nitrogen freezer”.
- Reading a checkpoint debrief as evidence of hand skill, long-term recovery or QC release.

## Scope and sources

| Statement in this lesson | Basis and reuse |
| --- | --- |
| Permeating/non-permeating categories; extracellular versus intracellular ice; competing solution and intracellular-ice injury; thaw and formulation cautions | Murray & Gibson, “Chemical approaches to cryopreservation”, *Nature Reviews Chemistry* 6:579–593 (2022), DOI 10.1038/s41570-022-00407-4; full text opened on PMC 2026-11-15; copyright Springer Nature; time-limited PMC permission not treated as current; link-only reference |
| Foundational freezing framework and primary citation | Mazur, *Science* 168:939–949 (1970), DOI 10.1126/science.168.3934.939; publisher no-access landing metadata and DOI record opened 2026-11-15; full text unavailable; copyrighted AAAS; link-only reference |
| DMSO as a permeating protective solute and mitigation of electrolyte concentration | Lovelock & Bishop, *Nature* 183:1394–1395 (1959), DOI 10.1038/1831394a0; publisher abstract and rights/permissions information opened 2026-11-15; subscription full text; copyrighted Springer Nature; link-only reference |
| Harvest/count context; cold freezing medium; approximate 1 °C/min and passive-container alternatives; vapour-phase storage; seed/working-stock contrast | Thermo Fisher Scientific, Gibco “Cell Freezing Protocols”, opened 2026-11-15; all rights reserved; link-only reference |
| Immediate 37 °C fast thaw; gradual post-thaw dilution; collection and DMSO removal; cell-specific cautions | Thermo Fisher Scientific, Gibco “Thawing Cells”, opened 2026-11-15; all rights reserved; link-only reference |
| Scope comparison only: cell-culture initiation and viability activities occur inside a broader biological-engineering course, not as a stand-alone cryopreservation course | MIT OCW 20.109 Spring 2010 syllabus/calendar, reread 2026-11-15; CC BY-NC-SA 4.0 footer confirmed; link-only comparator |
| Exact 4 °C dropwise rule, all volumes and counts, 0.8–1.2 °C/min tolerance, hold, location IDs, penalties, 95% DMSO removal, thresholds and tolerances | Original synthetic simulation choices; not laboratory acceptance criteria |

All instruction, examples, items and outcomes are original and were developed with substantial AI assistance. No source wording, table, figure, problem or dataset is copied. Exact URLs and dated rights evidence are in the integration registry and source-research log.
