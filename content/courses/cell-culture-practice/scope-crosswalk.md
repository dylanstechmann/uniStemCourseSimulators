# Cell Culture Practice scope and source crosswalk

This crosswalk covers version 0.3.0, a four-lesson partial package. It was compiled with AI assistance on 2026-10-31 and updated on 2026-11-15. It is an agent-run comparison, not a review by the owner, a laboratory professional or any institution. Topic alignment establishes no equivalence, credit or endorsement.

## Planned topics and their status

The eight topics come from the layer-2 outline in the repository's wet-lab layer outlines. Status labels: **covered** means a local reading develops the topic with worked examples and practice; **absent** means no local instruction; **deferred** means absent by plan until a later batch.

| Outline lesson | Status in 0.3.0 | Notes |
| --- | --- | --- |
| 1. Aseptic technique | **Covered** | [Lesson 1](modules/01-aseptic-technique.md) with 12 items, 4 cards, a case and the [aseptic medium-change simulation](#/bench/aseptic-medium-change-with-hidden-contamination); cabinet certification and spill response remain in Laboratory Safety and Biosafety |
| 2. Media, supplements and reagent preparation | **Covered** | [Lesson 2](modules/02-media-supplements-and-reagent-preparation.md) with 12 items, 4 cards, a case and the [supplemented-medium simulation](#/bench/filter-sterilize-and-qc-a-supplemented-medium); all formulation values and QC windows are simulation choices, not laboratory acceptance criteria |
| 3. Passaging adherent and suspension cells | **Covered** | [Lesson 3](modules/03-passaging-adherent-and-suspension-cells.md) with 12 items, 4 cards, a zero-point case and the [adherent target-density simulation](#/bench/passage-an-adherent-line-to-a-target-density); suspension passaging is conceptual only |
| 4. Counting cells and viability | **Covered** | [Lesson 4](modules/04-counting-cells-and-viability.md) with 12 items, 4 cards, a case and the [hemocytometer simulation](#/bench/hemocytometer-cell-count-viability); automated counters are named, not taught |
| 5. Cryopreservation and thawing | Absent, deferred | |
| 6. Contamination, mycoplasma and authentication | Absent, deferred | Lesson 1 teaches aseptic contamination prevention, sterility-control incubation, mollicute filtration limits and dedicated mycoplasma testing, but organism identification, broader contamination management and cell-line authentication remain absent |
| 7. Human pluripotent stem cells | Absent, deferred | ISSCR standards are reserved for this lesson and are not used as support for these synthetic exercises |
| 8. Records and traceability | Absent, deferred | |

## Course comparator

This batch did not find an MIT OpenCourseWare course devoted to cell culture, and the search was not exhaustive. [MIT OCW 20.109 Laboratory Fundamentals in Biological Engineering, Spring 2010](https://ocw.mit.edu/courses/20-109-laboratory-fundamentals-in-biological-engineering-spring-2010/pages/syllabus/) (CC BY-NC-SA 4.0, link only) places cell culture inside its Module 3, Cell-Biomaterial Engineering. Its calendar lists the labs "Initiate cell culture" (session 19) and "Testing cell viability" (session 20), and a lecture on cell viability (session 21). The syllabus and calendar titles were reread on 2026-11-15 and do not name aseptic technique as a separate topic; aseptic practice is treated here as prerequisite bench training implicit in initiating cell culture. Only the syllabus and calendar titles were read; the lab handouts were not, so the method 20.109 uses is unknown. Lesson 1 corresponds to the cell-culture initiation session at the level of prerequisite technique only, and lesson 4 corresponds to the viability-testing session at the level of topic only. The comparator's biomaterial, transcript and protein analyses are outside this package. The syllabus/calendar was reread for lessons 2 and 3 on 2026-11-15. Session 19, “Initiate cell culture,” is the closest listed session for media preparation and passaging; neither that title nor “Testing cell viability” establishes a separately titled media or passaging lesson or the depth of this package's formulation and target-density arithmetic. No lab handout was read, and no equivalence is inferred. The page footer's CC BY-NC-SA 4.0 licence was rechecked and link-only comparator mode retained.

## Sources used by lesson 1

| Source | Used for | Reuse |
| --- | --- | --- |
| FDA, *Guidance for Industry: Sterile Drug Products Produced by Aseptic Processing — Current Good Manufacturing Practice*, September 2004, printed pp. 6, 13–14, 21, 25, 34–35 | ISO 5 critical zone and 0.45 m/s ±20% airflow; intervention risk; sterile-to-sterile contact; glove sanitization; slow movement; side approach; avoiding talking near critical zone; process-simulation incubation for at least 14 days within 20–35 °C; dual-temperature rules; sterile disinfectants, contact time and the non-sporicidal limit of 70% isopropyl alcohol | US federal work, adapted with attribution |
| Geraghty RJ et al., "Guidelines for the use of cell lines in biomedical research", *Br J Cancer* 111:1021–1046, 2014, DOI 10.1038/bjc.2014.166, PMID 25117809, sections 1.5, 3.3.2, 3.4.1, 3.4.2, 4.2, 4.2.2–4.2.4 | Cabinet swabbing and 70% alcohol; no rapid movements or burner; one cell line; no overcrowding; clear grilles and opening; clean-to-dirty organization; post-session cleaning; limited UV; cross-contamination and misidentification; dedicated media/reagents; 0.22 µm filtration; mycoplasma size, filter passage, invisible growth, antibiotic resistance and routine dedicated testing; disposal of infected flasks | Link-only scientific reference; no text, table or figure copied; CC BY-NC-SA terms not selected for this CC-BY-4.0 package |
| CDC and NIH, *Biosafety in Microbiological and Biomedical Laboratories*, 6th edition, current Appendix H, printed pp. 471 and 473 (current PDF pp. 501 and 503) | Risk assessment before eukaryotic cell culture; BSL-2 minimum for human and other primate cells; biological safety cabinet as accepted best practice; PPE; waste culture material decontaminated before disposal | US federal work, adapted with attribution |

## Sources used by lesson 2

| Source | Used for | Reuse |
| --- | --- | --- |
| Eagle H, *Science* 122(3168):501–504 (1955), DOI 10.1126/science.122.3168.501 | Bibliographic citation only; no methods, results or historical-role claim | Link only; Crossref metadata verified; article body neither retrieved nor read; no text or assets copied |
| Thermo Fisher, “Cell Culture Media Preparation from Powder” | Modern basal-medium formulation, powder/concentrate context, formulation-specific pH and heat-labile filtration | Copyrighted; link only |
| Thermo Fisher, “Cell Culture Environment” | Bicarbonate/CO₂ buffering and cell-line-specific conditions | Copyrighted; link only |
| Thermo Fisher, Newborn Calf Serum FAQs 26010066/26010074 | Application-dependent heat-inactivation and cold, light-minimized storage context | Copyrighted; link only; synthetic expiry not sourced here |
| Geraghty et al. (2014), §§1.5.1, 3.3, 3.3.2, 3.3.4, 3.5.1 and 4.2 | Modern basal-medium components, glutamine, aliquots, serum-free distinctions, filtration, cold dark storage, records and mollicute limits | CC BY-NC-SA 3.0 link-only reference; terms not selected |
| FDA aseptic-processing guidance (September 2004), printed pp. 21, 25 and 35 | Fourteen-day lower-then-higher-temperature sterility-control teaching schedule | US federal work, adapted with attribution; no compliance claim |
| MIT OCW 20.109 Spring 2010 syllabus/calendar | Scope comparator, session 19 | CC BY-NC-SA 4.0; link only |

## Sources used by lesson 3

| Source | Used for | Reuse |
| --- | --- | --- |
| Thermo Fisher Scientific, Gibco Cell Culture Basics, “Adherent Cell Culture Protocol” | General adherent inspection, wash, dissociation/detachment, neutralization, collection, counting and cell-line-specific seeding workflow | Copyrighted; link-only reference; original wording; no protocol text or figure copied |
| Thermo Fisher Scientific, Gibco Cell Culture Basics, “Suspension Cell Culture Protocol” | Suspension sampling, direct dilution or transfer of a portion, and absence of substrate detachment | Copyrighted; link-only reference; conceptual comparison only |
| Thermo Fisher Scientific, Gibco Cell Culture Basics, “Seeding, Subculturing, and Maintaining Cells” | Cell-number/final-volume seeding arithmetic, growth-phase context, records and repeated-subculture risks | Copyrighted; link-only reference; original wording |
| MIT OCW 20.109 Spring 2010 syllabus/calendar | Nearest listed cell-culture initiation and viability sessions; not a passaging-depth comparator | CC BY-NC-SA 4.0 confirmed 2026-11-15; link-only comparator |

## Sources used by lesson 4

| Source | Used for | Reuse |
| --- | --- | --- |
| Paul Marienfeld GmbH & Co. KG, counting-grid description ("Counting grids", catalogue pp. 58–62, English PDF; no printed date, file metadata 2014) | Improved-Neubauer depth, ruling and volume per square; triple lines with the middle line as dimension line; Fuchs-Rosenthal 0.2 mm depth | Link only; facts paraphrased, no figure or table copied |
| Poly-Optik GmbH for Marienfeld Superior, *Instructions for use: Counting chambers according DIN 12847* (English PDF; no printed version or date, file metadata 2022) | That the manufacturer leaves filling and counting procedures to trained staff and the literature; handling cautions | Link only |
| Student (W. S. Gosset), "On the Error of Counting with a Haemacytometer", *Biometrika* 5(3):351–360, 1907, DOI 10.1093/biomet/5.3.351 | Two error sources; variance equal to the mean; standard deviation of a mean count; larger error with aggregates | Link only; derivation restated in original words |
| W. Strober, "Trypan Blue Exclusion Test of Cell Viability", *Curr Protoc Immunol* 111:A3.B.1–A3.B.3, 2015, DOI 10.1002/0471142735.ima03bs111, PMID 26529666 | Membrane-integrity principle, serum-free counting, 3–5 minute window, subjectivity, limits of the test | Link only; paraphrased |
| CDC and NIH, *Biosafety in Microbiological and Biomedical Laboratories*, 6th edition, Appendix H, pp. 466–468 of the copy read on 2026-10-31 | Risk factors and minimum BSL-2 handling for human and primate cells | US federal work, adapted with attribution |

## Sourced facts and simulation choices

Lesson 1's T-75 working volume of 10–15 mL, clean-to-dirty zones, one medium or waste bottle at a time, expired-label scenario, hidden-event probabilities, three-day visible-growth threshold and simplified mycoplasma assay are teaching choices labelled `simulation-typical` or `simulation-model` in the protocol file. They are not laboratory acceptance criteria, a validated sterility method or regulatory compliance. Lesson 4's top/left inclusion convention, corner rule and loading steps are common practice taught as this course's convention; neither Marienfeld document prescribes them. Its bench simulation's twofold dilution, 20–80-cell field range, 0.2% and 0.5% calculation tolerances and use of all included cells for uncertainty are likewise declared simulation choices.

Lesson 2's 500 mL final batch, 10% serum, 100×/200 mM to 1×/2 mM glutamine, pH 7.10–7.30, 280–310 mOsm/kg, volume-weighted approximation, 98% recovery, 10 mL control, dates and 14-day expiry, event probabilities and simplified assays are simulation choices. They are not physical validation or acceptance criteria.

Lesson 3's 70–85% routine window, 95% refusal scenario, T-75 area and exact volumes, five-minute dissociation bound, fixed two-flask target, 6.0 mL resuspension, tally transformations, viable-yield PDL convention, 0.5% seed-volume tolerance and 0.01-PDL tolerance are simulation choices. The source-derived volume scalings do not make the resulting T-75 protocol physically validated. The model does not simulate suspension culture or predict post-incubation biology.

## Remaining gaps

- Outline lessons 5–8: cryopreservation, full contamination management and authentication, pluripotent stem cells and records.
- Organism identification, cell-line authentication methods, quarantine workflows and a complete contamination-response procedure; lesson 1 teaches prevention and evidence interpretation only.
- Automated cell counters, fluorescent and flow-cytometric viability assays, and comparisons between methods.
- A primary source for lesson 4's boundary convention, and an open-protocol source for loading technique.
- Review by a qualified laboratory professional, measured workload and any graded assessment or project.
