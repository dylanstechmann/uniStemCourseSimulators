# Cell Culture Practice scope and source crosswalk

This crosswalk covers version 0.5.0, an eight-lesson partial package. It was compiled with AI assistance on 2026-10-31 and updated on 2026-11-16. It is an agent-run comparison, not a review by the owner, a laboratory professional or any institution. Topic alignment establishes no equivalence, credit or endorsement.

## Planned topics and their status

The eight topics come from the layer-2 outline in the repository's wet-lab layer outlines. Status labels: **covered** means a local reading develops the topic with worked examples and practice; **absent** means no local instruction; **deferred** means absent by plan until a later batch.

| Outline lesson | Status in 0.5.0 | Notes |
| --- | --- | --- |
| 1. Aseptic technique | **Covered** | [Lesson 1](modules/01-aseptic-technique.md) with 12 items, 4 cards, a case and the [aseptic medium-change simulation](#/bench/aseptic-medium-change-with-hidden-contamination); cabinet certification and spill response remain in Laboratory Safety and Biosafety |
| 2. Media, supplements and reagent preparation | **Covered** | [Lesson 2](modules/02-media-supplements-and-reagent-preparation.md) with 12 items, 4 cards, a case and the [supplemented-medium simulation](#/bench/filter-sterilize-and-qc-a-supplemented-medium); all formulation values and QC windows are simulation choices, not laboratory acceptance criteria |
| 3. Passaging adherent and suspension cells | **Covered** | [Lesson 3](modules/03-passaging-adherent-and-suspension-cells.md) with 12 items, 4 cards, a zero-point case and the [adherent target-density simulation](#/bench/passage-an-adherent-line-to-a-target-density); suspension passaging is conceptual only |
| 4. Counting cells and viability | **Covered** | [Lesson 4](modules/04-counting-cells-and-viability.md) with 12 items, 4 cards, a case and the [hemocytometer simulation](#/bench/hemocytometer-cell-count-viability); automated counters are named, not taught |
| 5. Cryopreservation and thawing | **Covered** | [Lesson 5](modules/05-cryopreservation-and-thawing.md) with 12 items, 4 cards, a zero-point case and the [same-run freeze/thaw simulation](#/bench/freeze-and-thaw-with-viability-outcomes); one synthetic DMSO pathway only |
| 6. Contamination: bacteria, fungi, mycoplasma and cross-contamination | **Covered** | [Lesson 6](modules/06-contamination-mycoplasma-and-authentication.md) with 12 items, 4 cards, a zero-point case and the [contamination-diagnosis simulation](#/bench/diagnose-a-contaminated-culture-from-clues); organism behaviour, full assay performance and real authentication are not modelled |
| 7. Human pluripotent stem cells | **Covered** | [Lesson 7](modules/07-human-pluripotent-stem-cells.md) with 12 items, 4 cards, a zero-point case and the [synthetic hPSC maintenance simulation](#/bench/maintain-an-hpsc-culture-without-spontaneous-differentiation); physical technique, functional pluripotency assays and real release decisions remain outside scope |
| 8. Records and traceability | **Covered** | [Lesson 8](modules/08-records-and-traceability.md) with 12 items, 4 cards and a zero-point case; master/working banks, passage/PDL, three-lot-table trace, labels, ALCOA basics and outline-only incident handoff; **no protocol by design** |

## Course comparator

This batch did not find an MIT OpenCourseWare course devoted to cell culture, and the search was not exhaustive. [MIT OCW 20.109 Laboratory Fundamentals in Biological Engineering, Spring 2010](https://ocw.mit.edu/courses/20-109-laboratory-fundamentals-in-biological-engineering-spring-2010/pages/syllabus/) (CC BY-NC-SA 4.0, link only) places cell culture inside its Module 3, Cell-Biomaterial Engineering. Its calendar lists the labs "Initiate cell culture" (session 19) and "Testing cell viability" (session 20), and a lecture on cell viability (session 21). The syllabus and calendar titles were reread on 2026-11-15 and do not name aseptic technique as a separate topic; aseptic practice is treated here as prerequisite bench training implicit in initiating cell culture. Only the syllabus and calendar titles were read; the lab handouts were not, so the method 20.109 uses is unknown. Lesson 1 corresponds to the cell-culture initiation session at the level of prerequisite technique only, and lesson 4 corresponds to the viability-testing session at the level of topic only. The comparator's biomaterial, transcript and protein analyses are outside this package. The syllabus/calendar was reread for lessons 2 and 3 on 2026-11-15. Session 19, “Initiate cell culture,” is the closest listed session for media preparation and passaging; neither that title nor “Testing cell viability” establishes a separately titled media or passaging lesson or the depth of this package's formulation and target-density arithmetic. No lab handout was read, and no equivalence is inferred. The page footer's CC BY-NC-SA 4.0 licence was rechecked and link-only comparator mode retained. The syllabus/calendar was reread for lessons 5 and 6 on 2026-11-15. “Initiate cell culture” (session 19) and “Testing cell viability” (session 20) remain the closest listed activities; their titles do not establish stand-alone cryopreservation, contamination-response, mycoplasma-method or STR-authentication lessons or equivalent depth. Link-only comparator mode is retained.

The MIT 20.109 Spring 2010 syllabus/calendar was reread for lesson 7 on 2026-11-15. Its listed cell-culture initiation, viability and analysis sessions do not demonstrate hPSC maintenance, defined-matrix culture, clump passaging or hPSC-specific QC. Lesson 7 is therefore beyond the comparator's demonstrated scope, not equivalent to it. It was reread for lesson 8 on the same date; the general notebook-keeping aim and cell-culture sessions do not establish master/working-bank instruction, PDL-ledger reconciliation or a three-table contamination-lot trace. The CC BY-NC-SA 4.0 footer/deed was rechecked and link-only comparator mode retained.

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

## Sources used by lesson 5

| Source | Used for | Reuse |
| --- | --- | --- |
| Thermo Fisher Scientific, Gibco “Cell Freezing Protocols” | Harvest/count context, cold medium, controlled/passive cooling, vapour storage and seed/working-stock contrast | Copyrighted; link-only reference; original wording; no protocol text or figure copied |
| Thermo Fisher Scientific, Gibco “Thawing Cells” | Fast 37 °C thaw, gradual dilution, collection and DMSO-containing supernatant removal | Copyrighted; link-only reference; original wording |
| Mazur, *Science* 168:939–949 (1970), DOI 10.1126/science.168.3934.939 | Corrected classic primary freezing-framework citation | Copyrighted AAAS; no-access landing metadata read, full text unavailable; link-only |
| Lovelock & Bishop, *Nature* 183:1394–1395 (1959), DOI 10.1038/1831394a0 | Permeating DMSO and electrolyte-concentration context | Copyrighted Springer Nature; publisher abstract read, subscription full text unavailable; link-only |
| Murray & Gibson, *Nature Reviews Chemistry* 6:579–593 (2022), DOI 10.1038/s41570-022-00407-4 | Cryoprotectant classes, two-factor injury and thaw/osmotic cautions | Copyrighted Springer Nature; full text read on PMC; time-limited PMC permission not treated as current; link-only |
| MIT OCW 20.109 Spring 2010 syllabus/calendar | Nearest listed initiation and viability sessions; not a cryopreservation-depth comparator | CC BY-NC-SA 4.0 confirmed 2026-11-15; link-only comparator |

## Sources used by lesson 6

| Source | Used for | Reuse |
| --- | --- | --- |
| Drexler & Uphoff (2002), DOI 10.1023/A:1022913015916, PMCID PMC3463982 | Mycoplasma sources/effects, culture/PCR/DNA-stain evidence and limits, prevention, elimination and antibiotic caveats | © Kluwer 2002; complete 16-page PDF read 2026-11-15; link-only, original wording |
| Geraghty et al. (2014), DOI 10.1038/bjc.2014.166, PMCID PMC4453835 | Visible bacterial/fungal clues, quarantine/intake, disposal/rescue, HeLa-era misidentification, STR and provenance | CC BY-NC-SA 3.0; full text reread 2026-11-15; link-only |
| ANSI/ATCC ASN-0002-2022 and ATCC public STR analysis/matching pages | Current standard scope, STR loci/alleles and bounded match interpretation | Official record and public pages read; full paid standard not accessed; ATCC rights checked; link-only |
| ICLAC Register v14, 2026-02-15 | Lookup resource for known misidentification; absence is not authentication | CC BY-NC-ND 4.0; strictly link-only; no copied register rows, counts or dataset |
| MIT OCW 20.109 Spring 2010 syllabus/calendar | Nearest cell-culture initiation and viability sessions only | CC BY-NC-SA 4.0 confirmed 2026-11-15; link-only comparator |

## Sources used by lesson 7

| Source | Used for | Reuse |
| --- | --- | --- |
| Ludwig et al., *Stem Cell Reports* 18(9):1744–1752 (2023), DOI 10.1016/j.stemcr.2023.08.003, PMCID PMC10545481 | Acquisition, consent/transfer context, authentication, genomic monitoring, undifferentiated-state interpretation and reporting | CC BY-NC-ND 4.0 confirmed; link-only by package choice; no text adapted or reproduced |
| ISSCR, *Standards for Human Stem Cell Use in Research*, official page and December 2023 update | High-level characterization/reporting scope | Strictly copyrighted; link-only; distinct ID `isscr-hpsc-standards-2023`; no Standards text adapted or reproduced |
| ISSCR, *Guidelines for Stem Cell Research and Clinical Translation* | Separate governance and permissible-use reference | Existing `isscr-stem-cell-guidelines`; link-only |
| ATCC, *Stem Cell Culture Guide* | Feeder-free matrix, morphology, daily maintenance, selective removal, aggregate passaging and QC context | Copyrighted link-only after guide and Website Terms of Use checks; no source protocol or asset used |
| NIST, *Cell Line Identification and Authentication: Human Cell Lines Standards and Protocols*, updated 2025-08-14 | STR identity testing and its limits | Public-information/reuse pages checked; original paraphrase with attribution; no ASN/ATCC or ICLAC rows imported |
| MIT OCW 20.109 Spring 2010 syllabus/calendar | Non-equivalent comparator | CC BY-NC-SA 4.0 confirmed; hPSC maintenance beyond demonstrated scope; link-only |

## Sources used by lesson 8

| Source | Used for | Reuse |
| --- | --- | --- |
| ISBER, *Best Practices: Recommendations for Repositories*, fifth edition, December 2023; companion update DOI 10.1089/bio.2023.0140 | Biorepository scope context for linked bank, specimen and repository records; no page-level alignment claimed | Copyrighted; official landing page and Terms opened 2026-11-15; link-only reference; no text, tables, PDF or direct download asset copied |
| MIT OCW 20.109 Spring 2010 syllabus/calendar | General notebook-keeping context and nearest cell-culture sessions only | CC BY-NC-SA 4.0 confirmed 2026-11-15; link-only comparator |

## Sourced facts and simulation choices

Lesson 1's T-75 working volume of 10–15 mL, clean-to-dirty zones, one medium or waste bottle at a time, expired-label scenario, hidden-event probabilities, three-day visible-growth threshold and simplified mycoplasma assay are teaching choices labelled `simulation-typical` or `simulation-model` in the protocol file. They are not laboratory acceptance criteria, a validated sterility method or regulatory compliance. Lesson 4's top/left inclusion convention, corner rule and loading steps are common practice taught as this course's convention; neither Marienfeld document prescribes them. Its bench simulation's twofold dilution, 20–80-cell field range, 0.2% and 0.5% calculation tolerances and use of all included cells for uncertainty are likewise declared simulation choices.

Lesson 2's 500 mL final batch, 10% serum, 100×/200 mM to 1×/2 mM glutamine, pH 7.10–7.30, 280–310 mOsm/kg, volume-weighted approximation, 98% recovery, 10 mL control, dates and 14-day expiry, event probabilities and simplified assays are simulation choices. They are not physical validation or acceptance criteria.

Lesson 3's 70–85% routine window, 95% refusal scenario, T-75 area and exact volumes, five-minute dissociation bound, fixed two-flask target, 6.0 mL resuspension, tally transformations, viable-yield PDL convention, 0.5% seed-volume tolerance and 0.01-PDL tolerance are simulation choices. The source-derived volume scalings do not make the resulting T-75 protocol physically validated. The model does not simulate suspension culture or predict post-incubation biology.

Lesson 5's 4 °C dropwise rule, exact volumes and cell numbers, 0.8–1.2 °C/min tolerance, 16 h hold, storage temperature and IDs, viability baselines and multipliers, 95% DMSO-solute removal, 80% threshold and 0.2% recount tolerance are simulation choices. They do not physically validate a freeze/thaw protocol. Liquid-phase selection fails a conceptual safety checkpoint without changing synthetic viability; no future growth or QC release is modelled.

Lesson 6's five condition permutations, visible pH values and structures, simplified binary tests, four-locus synthetic alleles, dispositions, five source assignments and handoff fields are simulation choices. The lesson-defined 100 × shared calls/reference calls arithmetic is not the Tanabe or Masters algorithm or a universal match threshold. No test output is a sterility certificate or a physically validated biological result. Real ASN-0002 interpretation, assay controls/coverage, reference provenance and privacy review remain outside the simulator.

The 42→60→78% density path, 70–85% window, three-day loop, differentiation penalties, arbitrary viability index, hidden matrix and intake events, 156-clump panel, 2–3 triturations, six wells and five-passage QC interval are simulation choices. They are not ISSCR, ATCC, NIST or FDA laboratory criteria. No FDA manufacturing guidance or revoked 21 CFR 610.30 method is used. The maintenance loop does not authorize or certify hPSC work.

Every MCB/WCB, vessel, preparation, lot, count, observation and correction in lesson 8 is synthetic. The passage/PDL equations are recomputed from the displayed raw numbers. BM-24-118 is the only basal-medium lot shared by the four positive vessels in the authored trace, but exposed negative V-104 makes causal overclaiming invalid. ALCOA is named only as attributable, legible, contemporaneous, original and accurate; full quality-system records, GLP/CLIA and detailed investigations remain deferred to layer 4. No CFR sources are added.

## Remaining gaps

- Real morphology training, validated manual removal and aseptic hand skill; functional pluripotency/differentiation assays, detailed karyotype or genomic interpretation and actual assay validation.
- Institution-specific ethical provenance, privacy/access controls, validated QC release and supervised hPSC work.
- Full quality-system records and investigations; lesson 8's synthetic join does not establish real-world traceability or causal identification.
- Species identification, real diagnostic performance, a complete ASN-0002 implementation and physical rescue efficacy. Contamination response, mycoplasma evidence and bounded synthetic STR authentication are taught in lesson 6.
- Vitrification, cell-specific cryopreservation optimisation, full QC release and complete cell-banking SOPs; lesson 5 teaches one synthetic DMSO slow-freeze/vapour-storage pathway.
- Automated cell counters, fluorescent and flow-cytometric viability assays, and comparisons between methods.
- A primary source for lesson 4's boundary convention, and an open-protocol source for loading technique.
- Review by a qualified laboratory professional, measured workload and any graded assessment or project.
