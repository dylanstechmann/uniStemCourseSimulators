# Cell Culture Practice scope and source crosswalk

This crosswalk covers version 0.2.0, a two-lesson partial package. It was compiled with AI assistance on 2026-10-31 and updated on 2026-11-15. It is an agent-run comparison, not a review by the owner, a laboratory professional or any institution. Topic alignment establishes no equivalence, credit or endorsement.

## Planned topics and their status

The eight topics come from the layer-2 outline in the repository's wet-lab layer outlines. Status labels: **covered** means a local reading develops the topic with worked examples and practice; **absent** means no local instruction; **deferred** means absent by plan until a later batch.

| Outline lesson | Status in 0.2.0 | Notes |
| --- | --- | --- |
| 1. Aseptic technique | **Covered** | [Lesson 1](modules/01-aseptic-technique.md) with 12 items, 4 cards, a case and the [aseptic medium-change simulation](#/bench/aseptic-medium-change-with-hidden-contamination); cabinet certification and spill response remain in Laboratory Safety and Biosafety |
| 2. Media, supplements and reagent preparation | Absent, deferred | Solution preparation is in Laboratory Measurement; lesson 1 uses medium labels and filtration but does not teach media preparation |
| 3. Passaging adherent and suspension cells | Absent, deferred | Seeding arithmetic from a count is not taught |
| 4. Counting cells and viability | **Covered** | [Lesson 4](modules/04-counting-cells-and-viability.md) with 12 items, 4 cards, a case and the [hemocytometer simulation](#/bench/hemocytometer-cell-count-viability); automated counters are named, not taught |
| 5. Cryopreservation and thawing | Absent, deferred | |
| 6. Contamination, mycoplasma and authentication | Absent, deferred | Lesson 1 teaches aseptic contamination prevention, sterility-control incubation, mollicute filtration limits and dedicated mycoplasma testing, but organism identification, broader contamination management and cell-line authentication remain absent |
| 7. Human pluripotent stem cells | Absent, deferred | ISSCR standards are reserved for this lesson and are not used as support for these synthetic exercises |
| 8. Records and traceability | Absent, deferred | |

## Course comparator

This batch did not find an MIT OpenCourseWare course devoted to cell culture, and the search was not exhaustive. [MIT OCW 20.109 Laboratory Fundamentals in Biological Engineering, Spring 2010](https://ocw.mit.edu/courses/20-109-laboratory-fundamentals-in-biological-engineering-spring-2010/pages/syllabus/) (CC BY-NC-SA 4.0, link only) places cell culture inside its Module 3, Cell-Biomaterial Engineering. Its calendar lists the labs "Initiate cell culture" (session 19) and "Testing cell viability" (session 20), and a lecture on cell viability (session 21). The syllabus and calendar titles were reread on 2026-11-15 and do not name aseptic technique as a separate topic; aseptic practice is treated here as prerequisite bench training implicit in initiating cell culture. Only the syllabus and calendar titles were read; the lab handouts were not, so the method 20.109 uses is unknown. Lesson 1 corresponds to the cell-culture initiation session at the level of prerequisite technique only, and lesson 4 corresponds to the viability-testing session at the level of topic only. The comparator's biomaterial, transcript and protein analyses are outside this package.

## Sources used by lesson 1

| Source | Used for | Reuse |
| --- | --- | --- |
| FDA, *Guidance for Industry: Sterile Drug Products Produced by Aseptic Processing — Current Good Manufacturing Practice*, September 2004, printed pp. 6, 13–14, 21, 25, 34–35 | ISO 5 critical zone and 0.45 m/s ±20% airflow; intervention risk; sterile-to-sterile contact; glove sanitization; slow movement; side approach; avoiding talking near critical zone; process-simulation incubation for at least 14 days within 20–35 °C; dual-temperature rules; sterile disinfectants, contact time and the non-sporicidal limit of 70% isopropyl alcohol | US federal work, adapted with attribution |
| Geraghty RJ et al., "Guidelines for the use of cell lines in biomedical research", *Br J Cancer* 111:1021–1046, 2014, DOI 10.1038/bjc.2014.166, PMID 25117809, sections 1.5, 3.3.2, 3.4.1, 3.4.2, 4.2, 4.2.2–4.2.4 | Cabinet swabbing and 70% alcohol; no rapid movements or burner; one cell line; no overcrowding; clear grilles and opening; clean-to-dirty organization; post-session cleaning; limited UV; cross-contamination and misidentification; dedicated media/reagents; 0.22 µm filtration; mycoplasma size, filter passage, invisible growth, antibiotic resistance and routine dedicated testing; disposal of infected flasks | Link-only scientific reference; no text, table or figure copied; CC BY-NC-SA terms not selected for this CC-BY-4.0 package |
| CDC and NIH, *Biosafety in Microbiological and Biomedical Laboratories*, 6th edition, current Appendix H, printed pp. 471 and 473 (current PDF pp. 501 and 503) | Risk assessment before eukaryotic cell culture; BSL-2 minimum for human and other primate cells; biological safety cabinet as accepted best practice; PPE; waste culture material decontaminated before disposal | US federal work, adapted with attribution |

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

## Remaining gaps

- Outline lessons 2–3 and 5–8, including media preparation, passaging, cryopreservation, full contamination management and authentication, pluripotent stem cells and records.
- Organism identification, cell-line authentication methods, quarantine workflows and a complete contamination-response procedure; lesson 1 teaches prevention and evidence interpretation only.
- Automated cell counters, fluorescent and flow-cytometric viability assays, and comparisons between methods.
- A primary source for lesson 4's boundary convention, and an open-protocol source for loading technique.
- Review by a qualified laboratory professional, measured workload and any graded assessment or project.
