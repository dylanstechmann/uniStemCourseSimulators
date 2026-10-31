# Cell Culture Practice scope and source crosswalk

This crosswalk covers version 0.1.0, a one-lesson pilot. It was compiled with AI assistance on 2026-10-31. It is an agent-run comparison, not a review by the owner, a laboratory professional or any institution. Topic alignment establishes no equivalence, credit or endorsement.

## Planned topics and their status

The eight topics come from the layer-2 outline in the repository's wet-lab layer outlines. Status labels: **covered** means a local reading develops the topic with worked examples and practice; **absent** means no local instruction; **deferred** means absent by plan until a later batch.

| Outline lesson | Status in 0.1.0 | Notes |
| --- | --- | --- |
| 1. Aseptic technique | Absent, deferred | Cabinet working order is taught for biosafety, not sterility, in Laboratory Safety and Biosafety lesson 3 |
| 2. Media, supplements and reagent preparation | Absent, deferred | Solution preparation is in Laboratory Measurement; culture media are not taught |
| 3. Passaging adherent and suspension cells | Absent, deferred | Seeding arithmetic from a count is not taught |
| 4. Counting cells and viability | **Covered** | [Lesson 4](modules/04-counting-cells-and-viability.md) with 12 items, 4 cards, a case and the [bench simulation](#/bench/hemocytometer-cell-count-viability); automated counters are named, not taught |
| 5. Cryopreservation and thawing | Absent, deferred | |
| 6. Contamination, mycoplasma and authentication | Absent, deferred | Lesson 4 states only that trypan blue does not detect contamination |
| 7. Human pluripotent stem cells | Absent, deferred | ISSCR standards are reserved for this lesson and are not used as support for the counting exercise |
| 8. Records and traceability | Absent, deferred | |

## Course comparator

This batch did not find an MIT OpenCourseWare course devoted to cell culture, and the search was not exhaustive. [MIT OCW 20.109 Laboratory Fundamentals in Biological Engineering, Spring 2010](https://ocw.mit.edu/courses/20-109-laboratory-fundamentals-in-biological-engineering-spring-2010/pages/syllabus/) (CC BY-NC-SA 4.0, link only) places cell culture inside its Module 3, Cell-Biomaterial Engineering. Its calendar lists the labs "Initiate cell culture" (session 19) and "Testing cell viability" (session 20), and a lecture on cell viability (session 21). Only the syllabus and calendar titles were read on 2026-10-31; the lab handouts were not, so the method 20.109 uses is unknown. Lesson 4 corresponds to the viability-testing session at the level of topic only. The comparator's biomaterial, transcript and protein analyses are outside this package.

## Sources used by lesson 4

| Source | Used for | Reuse |
| --- | --- | --- |
| Paul Marienfeld GmbH & Co. KG, counting-grid description ("Counting grids", catalogue pp. 58–62, English PDF; no printed date, file metadata 2014) | Improved-Neubauer depth, ruling and volume per square; triple lines with the middle line as dimension line; Fuchs-Rosenthal 0.2 mm depth | Link only; facts paraphrased, no figure or table copied |
| Poly-Optik GmbH for Marienfeld Superior, *Instructions for use: Counting chambers according DIN 12847* (English PDF; no printed version or date, file metadata 2022) | That the manufacturer leaves filling and counting procedures to trained staff and the literature; handling cautions | Link only |
| Student (W. S. Gosset), "On the Error of Counting with a Haemacytometer", *Biometrika* 5(3):351–360, 1907, DOI 10.1093/biomet/5.3.351 | Two error sources; variance equal to the mean; standard deviation of a mean count; larger error with aggregates | Link only; derivation restated in original words |
| W. Strober, "Trypan Blue Exclusion Test of Cell Viability", *Curr Protoc Immunol* 111:A3.B.1–A3.B.3, 2015, DOI 10.1002/0471142735.ima03bs111, PMID 26529666 | Membrane-integrity principle, serum-free counting, 3–5 minute window, subjectivity, limits of the test | Link only; paraphrased |
| CDC and NIH, *Biosafety in Microbiological and Biomedical Laboratories*, 6th edition, Appendix H, pp. 466–468 | Risk factors and minimum BSL-2 handling for human and primate cells | US federal work, adapted with attribution |

## Sourced facts and simulation choices

The top/left inclusion convention, the corner rule and the loading steps are common practice taught as this course's convention; neither Marienfeld document prescribes them. The bench simulation's twofold dilution, its 20–80-cell field range, its 0.2% and 0.5% calculation tolerances and its use of all included cells for the uncertainty are declared simulation choices, labelled `simulation-typical` or `simulation-model` in the protocol file. They are not laboratory acceptance criteria.

## Remaining gaps

- Outline lessons 1–3 and 5–8, including aseptic technique, which every later culture procedure assumes.
- Automated cell counters, fluorescent and flow-cytometric viability assays, and comparisons between methods.
- A primary source for the boundary convention, and an open-protocol source for loading technique.
- Review by a qualified laboratory professional, measured workload and any graded assessment or project.
