# Media, supplements and reagent preparation

**Status:** Original, unreviewed formative instruction with synthetic examples and simulation choices. It assesses reasoning and arithmetic only; it does not establish laboratory competency, validate a physical preparation, or replace a cell-line-specific formulation, product instructions, risk assessment or institutional procedure.

A supplemented medium is a connected record as much as a liquid: a basal formulation, calculated additions, component lots, a sterilizing step, quality-control (QC) evidence, a container label and a storage history. A clear bottle can still have the wrong concentration, an unsuitable pH or osmolality, degraded glutamine or undetected mollicutes. This lesson follows those links for one deliberately generic batch, then rehearses them in the [filter-sterilization and QC bench simulation](#/bench/filter-sterilize-and-qc-a-supplemented-medium).

This is lesson 2 of the outlined cell-culture layer. It uses lesson 1's aseptic technique and sterility-incubation rules without re-teaching cabinet manipulation. Later lessons address passaging, cryopreservation, contamination investigation, stem-cell culture and records; none is assumed here.

## Learning objectives

By the end of this lesson, you should be able to:

1. Explain the purposes of basal-medium nutrients, osmolality, pH, bicarbonate/CO₂ buffering and phenol red, and distinguish serum-containing, serum-free and fully defined systems.
2. Calculate supplement and basal-medium volumes from stock concentration, target concentration and **final** batch volume using C₁V₁ = C₂V₂.
3. Evaluate supplement handling, including L-glutamine instability, frozen single-use aliquots, serum heat-inactivation decisions and media dedicated to one cell line.
4. Plan a 0.22 µm filter-sterilization and filter-integrity workflow and explain why filtration and visible clarity do not exclude mollicutes.
5. Specify QC, sterility-control incubation, labelling, aliquoting, expiry, light-protected 2–8 °C storage and quarantine decisions for a traceable supplemented-medium batch.

## Basal medium is a formulation, not just food

Only Crossref bibliographic metadata were retrieved for Eagle's 1955 *Science* article, “Nutrition Needs of Mammalian Cells in Tissue Culture”; the article body was neither retrieved nor read, so no methods, results or historical-influence claim is made from it here. The modern basal-medium description in this lesson is instead grounded in the already-read Thermo Fisher and Geraghty references: a basal formulation supplies balanced inorganic salts, a carbohydrate source, amino acids, vitamins and other formulation-specific precursors. The exact recipe matters: two media with similar names can differ in glucose, glutamine, pyruvate, bicarbonate, HEPES or phenol red. Serum or defined supplements may add attachment factors, hormones, binding proteins and growth signals, but they do not make an unsuitable basal formulation universally suitable.

Osmolality describes solute concentration per mass of solvent. Cells respond to water movement across their membranes, so a large departure from the formulation's intended osmolality can cause osmotic stress even when every ingredient name is correct. pH is a different quantity: it describes hydrogen-ion activity. A medium can have an acceptable pH and an unacceptable osmolality, or vice versa. Measure each with an appropriate method; neither a colour nor a nutrient calculation substitutes for both.

The simulation uses a synthetic pre-filtration QC window of pH 7.10–7.30 and 280–310 mOsm/kg. These are **simulation choices**, not universal mammalian-cell acceptance limits. Thermo Fisher's environment overview emphasizes that required conditions are cell-line and product specific; its medium-preparation page gives formulation-specific pH examples rather than one universal range.

## Bicarbonate, CO₂ and phenol red

In a bicarbonate/CO₂-buffered medium, dissolved CO₂, carbonic acid, hydrogen ions and bicarbonate are linked by equilibrium. The gas atmosphere is therefore part of the buffer system. A formulation needs its specified bicarbonate concentration and CO₂ tension; transferring it blindly between a CO₂ incubator and room air changes the equilibrium and can shift pH. HEPES can provide additional non-volatile buffering, but adding it changes composition and can change osmolality.

Phenol red is an indicator, not the buffer. Yellow suggests relatively acidic conditions and purple relatively alkaline conditions in this teaching example. Colour is a prompt to investigate handling, CO₂ equilibration, metabolism or contamination; it is not a calibrated pH result, and it does not report osmolality or sterility. Some experiments omit phenol red because an indicator can interfere with an assay or have biological activity. Follow the selected formulation rather than treating its presence as mandatory.

## Serum, serum-free and defined systems

Serum can support attachment and growth, but its complex composition and lot variation can confound a mechanistic experiment. A serum-free formulation omits serum; it may still contain poorly defined protein or tissue extracts. A fully defined formulation has known components at known concentrations. “Serum-free,” “protein-free,” “animal-origin-free” and “chemically defined” are not interchangeable claims.

Select a system for the biological question and the cell line's documented requirements. Defined systems can improve reproducibility and reduce exposure to some reagent-associated contaminants, but they can be expensive, cell-line specific and less forgiving of water quality or preparation error. Do not assume that a serum-free label means supplement-free, contamination-free or suitable for every line.

Heat-inactivating serum is also a decision, not a ritual. It can reduce complement activity for particular immunological applications, but it is unnecessary for many routine cultures and heating can alter other serum properties. It is not a reliable substitute for supplier controls, aseptic handling or dedicated mycoplasma testing. The simulation therefore asks whether the selected procedure calls for heat-inactivated serum; it does not heat a generic serum lot by default.

## Work the supplement arithmetic from the final volume

For a stock of concentration C₁ and required final concentration C₂, use C₁V₁ = C₂V₂, where V₂ is the **finished batch volume**, not the basal volume before supplementation. Then calculate basal volume by subtraction after accounting for every addition.

**Worked example 1: two independent stock calculations.** For 250 mL final medium at 8% (v/v) serum from undiluted serum, V₁ = (0.08 × 250)/1 = **20 mL serum**. Separately, for 400 mL final medium at 2 mM L-glutamine from a 200 mM stock, V₁ = (2 mM × 400 mL)/(200 mM) = **4 mL stock**. The 100× description gives the same result: 400/100 = 4 mL. A common error is to divide the basal volume by 100 and then add stock on top; that produces a slightly different final concentration because the final volume has changed.

**Worked example 2: one complete synthetic batch.** The bench exercise prepares **500 mL final volume** with 10% (v/v) serum and 1× glutamine from a 100× stock. Serum = 0.10 × 500 = **50 mL**. Glutamine stock = 500/100 = **5 mL**. Basal medium = 500 − 50 − 5 = **445 mL**. If the stock is 200 mM and the target is 2 mM, the final glutamine calculation is again 2 × 500/200 = 5 mL. These values are teaching choices, not a recommended recipe for an actual cell line.

**Worked example 3: an osmolality estimate with an explicit approximation.** Suppose the same synthetic components have measured osmolalities of 290 mOsm/kg for basal medium, 300 for serum and 400 for the glutamine stock. A simple volume-weighted teaching estimate is

(445 × 290 + 50 × 300 + 5 × 400)/500 = 146,050/500 = **292.1 mOsm/kg**, reported to three significant figures as **292 mOsm/kg**.

Real mixing need not be perfectly volume-additive, solutes interact, and pipetting and instrument uncertainty remain. Use this expression only to audit the synthetic model; use the measured complete-medium result and the product-specific procedure for a real batch.

## Handle supplements as controlled reagents

Read identity, concentration, lot, expiry, storage and thaw history before opening a supplement. Reject an expired or unidentifiable lot rather than inferring suitability from a clear appearance. Keep dedicated medium and reagent bottles for one cell line to reduce cross-contamination and misidentification, continuing lesson 1's one-cell-line rule.

L-glutamine degrades in aqueous medium at a rate influenced by temperature and other formulation conditions. Geraghty et al. discuss cold degradation, faster degradation at culture temperature and the option of stabilized dipeptide forms. Do not copy the article's example discard interval into an unrelated product: follow the actual formulation and validated local procedure. For this simulation, concentrated L-glutamine is supplied as frozen, single-use aliquots. Select an aliquot with a documented frozen/cold history, thaw and mix it according to its product instructions, avoid repeated freeze–thaw cycles, and record its lot and thaw details. A stabilized dipeptide is a different formulation choice, not something to substitute silently in the same arithmetic.

Serum is also commonly aliquoted to avoid repeated freeze–thaw cycles and to support lot comparison. By contrast, freezing a finished medium is not a generic preservation strategy because precipitation and formulation changes can occur. In this lesson, the finished batch is refrigerated, not frozen.

## Filter sterilization and its evidence boundary

Heat-labile complete media are filtered rather than autoclaved. The simulation uses a **0.22 µm** filter and a protein-compatible membrane, with an aseptic receiving train, a pre-rinse/priming step and a post-use **bubble-point or pressure-hold integrity check**. Geraghty et al. identify 0.22 µm filtration for bacteria and fungi and note the membrane selection issue when protein is present; Thermo Fisher's manufacturer protocol uses a 0.2 µm system for its own examples. The lesson deliberately does not conflate those values or copy a brand-specific filtration protocol.

A pore-size label alone does not demonstrate that the membrane was intact, correctly assembled or used without bypass. Record filter identity and lot, inspect the setup, follow the device instructions, and perform the supported integrity check. Collect the filtrate in a sterile, labelled receiving vessel. An unlabelled bottle cannot be rescued by writing “medium” on it later: its prior contents and traceability are unknown.

Most importantly, 0.22 µm filtration does not establish absence of mollicutes or viruses. Geraghty et al. explain that mycoplasmas can pass pores larger than 0.1 µm and recommend dedicated testing rather than an assumption from filtration. A visibly clear filtrate and a negative standard sterility control still leave that separate evidence need.

## QC, controls, labels and release

For this simulation, measure pH and osmolality after mixing and before filtration, retain the readings with the batch record, and use the synthetic windows stated above. The model's volume-weighted osmolality is an approximation. It also uses a fixed 98% filtrate-recovery fraction solely to make aliquot accounting visible; it is not a measured membrane recovery or a physical fluid model.

Draw a representative filtrate sterility-control sample with a fresh sterile pipette. Apply lesson 1's FDA-derived teaching schedule: **at least 7 days at 20–25 °C, followed by at least 7 days at 30–35 °C**, for at least 14 days within 20–35 °C. This adapts process-simulation guidance for instruction; it is not a claim that this simplified control is a validated pharmacopoeial sterility test. Submit a dedicated mycoplasma lot test independently of whether a filtrate control was drawn. An absent or inadequately incubated control is pending/indeterminate, not a no-growth result; only a complete valid schedule supports a no-visible-growth observation. Until the required evidence is available and acceptable, keep the batch in quarantine rather than releasing it because it looks clear.

The synthetic label and linked record must contain:

- medium/formulation name and the intended cell line;
- preparation date and a calculated expiry;
- batch ID and the basal, serum, glutamine and filter lots;
- final volume, actual additions, pH, osmolality and integrity-test outcome;
- sterility-control and mycoplasma submission/status;
- storage condition and quarantine/release status.

Copy the exact original synthetic basal, selected serum, selected glutamine and filter lot IDs from the inspected supply/filter evidence into the batch record; a “lots linked” assertion without those IDs does not pass. The bench uses preparation date **2026-11-15** and a **14-day supplemented-medium expiry**, giving **2026-11-29**. That expiry is a simulation choice, not a shelf-life claim. Aliquot only the available filtrate after reserving QC volume; do not allocate more than was recovered. Store aliquots at **2–8 °C**, protected from light, with the same traceable label. These storage bounds follow the handling pattern discussed by Geraghty et al., while the actual product label always governs.

## Practise the connected batch record

Open the [supplemented-medium preparation simulation](#/bench/filter-sterilize-and-qc-a-supplemented-medium) and inspect the two serum lots, glutamine aliquots and receiving bottles. Add 50 mL serum and 5 mL 100× glutamine to enough basal medium for 500 mL final volume; measure pH and osmolality; select and use the 0.22 µm protein-compatible filter; test its integrity; reserve and incubate controls; submit the mycoplasma test; label and account for aliquots; then store the batch cold, dark and quarantined.

The simulation has 14 checkpoints. Its composition, QC windows, 98% recovery, dates, 14-day expiry, event probabilities, simplified assays and visible-growth threshold are synthetic model choices. Its sterility and mycoplasma outcomes are deterministic evidence scenarios, not physical validation of a filter, product or preparation.

## Common mistakes

- Treating “basal,” “complete,” “serum-free” and “chemically defined” as synonyms.
- Using phenol red as a pH meter, or assuming correct pH proves correct osmolality.
- Calculating 100× stock volume from the initial basal volume and then increasing the final volume.
- Forgetting one supplement when calculating the basal volume by subtraction.
- Repeating freeze–thaw cycles, using an expired lot, or accepting an unlabelled receiving bottle.
- Heat-inactivating serum by habit, or expecting that step to replace contamination testing.
- Autoclaving a heat-labile complete medium, or assuming a 0.22 µm label proves integrity and mollicute removal.
- Releasing clear medium before valid sterility incubation and dedicated mycoplasma evidence.
- Printing an expiry without component lots, or storing supplemented medium in light or outside its specified temperature range.

## Scope and sources

| Statement in this lesson | Basis |
| --- | --- |
| Eagle bibliographic citation only; no article methods, results or historical-role claim | Crossref metadata for Eagle H, *Science* 122(3168):501–504 (1955), DOI 10.1126/science.122.3168.501; metadata only—article body neither retrieved nor read (link only) |
| Modern basal-medium formulation context; formulation-specific preparation, pH adjustment and membrane filtration; supplement categories | Thermo Fisher Scientific, “Cell Culture Media Preparation from Powder,” sections “Media preparation from powder and concentrates” and “Media sterilization and supplementation” (copyrighted, link only) |
| CO₂/bicarbonate buffering and cell-line-specific environment | Thermo Fisher Scientific, “Cell Culture Environment,” sections “Cell Culture pH levels” and “Cell Culture CO₂ levels” (copyrighted, link only) |
| Heat-inactivation is application-dependent; refrigerated, light-minimized storage | Thermo Fisher Scientific, Newborn Calf Serum FAQs 26010066/26010074 (copyrighted, link only) |
| Modern basal-medium components; glutamine instability, aliquoting proteinaceous reagents, defined/serum-free distinctions, dedicated media, 0.22 µm filtration, protein-compatible membranes, cold dark storage and mollicute limits | Geraghty et al. (2014), §§1.5.1, 3.3, 3.3.2, 3.3.4 and 4.2 (CC BY-NC-SA 3.0; link-only reference, terms not selected for this package) |
| Fourteen-day, dual-temperature sterility-control teaching schedule | FDA aseptic-processing guidance (September 2004), printed pp. 25 and 35 (US federal work, adapted with attribution) |
| Scope comparator only | MIT OCW 20.109 Spring 2010 syllabus/calendar, session 19 “Initiate cell culture” (CC BY-NC-SA 4.0; link only) |
| 500 mL batch; 10% serum; 100× glutamine; pH 7.10–7.30; 280–310 mOsm/kg; osmolality estimate; 98% recovery; 14-day expiry; hidden events and simplified QC assays | Simulation choices, not laboratory acceptance criteria or a validated preparation |

All lots, readings, labels and outcomes are synthetic. No source text, protocol table or figure is reproduced. Full links, access dates and reuse permissions are maintained in the integrated package source map and source registry.
