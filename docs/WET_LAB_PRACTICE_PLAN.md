# Wet-lab practice track: plan

Status: drafted with AI assistance on 2026-10-30. Nothing here has been reviewed by a laboratory professional, a biosafety officer or a certifying body.

Built so far (2026-10-30, agent-run, unreviewed): the replay engine and API, the protocol schema, three protocols and a React bench view. These are items 1–3 of the first milestone below. The protocols are `micropipette-gravimetric-verification` (layer 0), `decimal-dilution-aerobic-plate-count` (layer 0, adapted from FDA BAM Chapter 3, January 2026 edition) and `class-ii-bsc-session-with-spill` (layer 1, adapted from BMBL 6th edition, Appendix A). Item 4, the layer-0 course package, is next.

## Goal

A layered bench-practice track that lets a learner rehearse real laboratory procedures, with their real volumes, speeds, times, temperatures and acceptance criteria, before doing them at a physical bench, and that covers the written scope of recognised laboratory credentials closely enough to make later study for them short.

What it can and cannot do:

- It can teach the knowledge, calculations, decision-making and order of operations that written exams and supervised bench training test.
- It cannot train hand skill (pipetting technique, aseptic handling, cell morphology by eye), and it confers no credential. Certifications such as the ASCP Board of Certification exams set their own eligibility routes, which include education and documented laboratory experience; simulator time does not count toward them.
- The track is not affiliated with or endorsed by ASCP, CDC, NIH, OSHA, ISSCR or any other body named below. Their outlines and documents set scope only, cited by link, except where a source is a US federal work in the public domain.

## Layers

Each layer is a course package in `content/courses/` with lessons, practice items and cards, like the existing packages, plus protocol simulations described below. Later layers assume the earlier ones.

| Layer | Package (working name) | Scope set by | What it covers |
| --- | --- | --- | --- |
| 0 | `lab-measurement` | General Chemistry I solutions lesson; manufacturer-neutral pipette and balance practice | Units, molarity and percent solutions, serial and parallel dilutions, micropipette selection and gravimetric verification, balances, pH meter calibration, significant figures and propagated error at the bench |
| 1 | `lab-safety-biosafety` | CDC/NIH *BMBL* 6th ed. (2020); OSHA 29 CFR 1910.1030 (bloodborne pathogens), 1910.1450 (laboratory standard), 1910.1200 (hazard communication) | Risk assessment, BSL-1/BSL-2 practices, biosafety cabinet classes, set-up, work and certification, PPE, spills and exposures, decontamination and autoclave verification, sharps, waste streams, chemical hygiene, SDS and GHS labels, awareness of Division 6.2 shipping rules |
| 2 | `cell-culture-practice` | BMBL; ISSCR *Standards for Human Stem Cell Use in Research* (2023, link only) | Aseptic technique, media and reagent preparation, passaging adherent and suspension cells, counting with a hemocytometer and trypan blue, freezing and thawing, contamination diagnosis, mycoplasma testing, cell-line authentication, feeder-free human pluripotent stem cell culture and its quality checks |
| 3 | `molecular-lab-practice` | ASCP BOC MB(ASCP) examination content guideline (molecular science, molecular techniques, laboratory operations, applications of molecular testing) | Nucleic acid isolation and quality control, gel and capillary electrophoresis, blotting and hybridization, PCR design and optimization, qPCR and RT-qPCR, melt curves, Sanger and next-generation sequencing basics, restriction analysis, contamination control and one-way workflow, assay validation and troubleshooting |
| 4 | `lab-quality-systems` | ASCP MB laboratory-operations section; 21 CFR Part 58 (GLP); CLIA (42 CFR Part 493) | Documentation and notebooks, SOP control, controls and proficiency testing, equipment calibration and maintenance records, deviations and corrective action, competency assessment, test-system categories (RUO, ASR, IVD, LDT) |
| 5 (optional extensions) | as needed | to be scoped per topic | Protein methods (SDS-PAGE, western blot, ELISA), microscopy and flow cytometry, a CRISPR editing workflow from guide design to genotyping, organoid culture, and an awareness lesson on cell-therapy manufacturing rules (21 CFR Part 1271 and Part 211) |

The applications section of the MB outline (infectious disease, oncology, genetic disorders, histocompatibility, identity, engraftment and pharmacogenomics) is about a third of that exam. It would be a later package after layer 3, reusing the genetics course where it can.

## Sources and reuse

- **Public domain (US federal works):** BMBL 6th edition, OSHA and FDA regulations, and CLIA regulations can be quoted and adapted with attribution. Each gets a registry record with `reuse_mode` set to allow adaptation, and the URL and access date.
- **Link only:** ASCP content guidelines and reading lists, ISSCR standards (the society reserves reproduction rights), ATCC and vendor manuals, textbooks. These set scope and are cited, never pasted.
- **Openly licensed protocols:** protocols from protocols.io or other repositories may be adapted only under the license each one carries, recorded per protocol in the registry.
- Every numeric protocol parameter (a speed, a time, a temperature, a tolerance) needs a cited sentence or table in its source, checked as the citation-check skill describes, or a label saying it is a typical value chosen for the simulation.

## The protocol simulator

The repository's existing labs are data-analysis exercises. Practising a procedure needs a new piece: an interactive bench state that the learner changes by choosing actions.

**Protocol definitions** live with each package as JSON (`protocols/*.json`), validated by a new schema. A definition holds:

- the bench state: containers with volumes and contents, instrument settings, a clock, temperatures, and hidden variables such as sterility and nucleic-acid carry-over;
- the actions available at each point, with parameters (a volume, a speed, a time);
- effects: how each action changes the state, including realistic error models (for example pipetting inaccuracy, or contamination when a tip is reused);
- checkpoints: rules on the state or the action history, each marked critical, major or minor, with an explanation and a citation;
- readouts the learner sees: a gel image, an absorbance ratio, a cell count, a standard curve, a colony on a sterility plate.

**Engine.** A deterministic Python module in the backend applies actions to state with a seeded random generator, so every run can be replayed and tested. The full definition, including checkpoints and expected values, stays on the server, in line with the rule that solutions never reach learners. The browser sends actions and receives the new visible state and any consequences.

**Modes:**

- *Guided*: each step is prompted and explained as it is done.
- *Practice*: no prompts. Consequences appear when they would at a real bench: a contaminated culture is found days later, and a failed PCR shows up on the gel.
- *Assessed run*: the protocol is run without help, then a debrief lists every checkpoint met or missed. Results are formative-only, like the rest of the site.

**Scenario variation.** Seeds vary sample concentrations, instrument faults and starting conditions, so a protocol cannot be passed by memorising one run.

**Mock exams.** Item banks are tagged to the outline headings of each scope source. A mock exam for layer 3 mirrors the published MB format (100 single-best-answer questions in 2 h 30 min, adaptive). The adaptive selection is only approximate, because the items are not calibrated on real examinees.

**Interface.** Version 1 is a two-dimensional React bench view: a bench, racks, instruments and a timeline. Three-dimensional assets (for example glTF models made in Blender and rendered with three.js) can come later. They make the bench more realistic to look at but add no knowledge, and Blender cannot run in this container.

## First milestone

1. Protocol schema, engine, API routes and engine tests with fixed seeds.
2. Three protocols from layers 0–1: gravimetric verification of a micropipette, a tenfold serial dilution with a plate count, and setting up and working in a Class II biosafety cabinet, including a spill.
3. A minimal React bench view for those three.
4. Layer 0 as a course package with lessons, items and cards that pass the content validator.

Later milestones follow the layer order. Each one ends with a scope crosswalk against its source, built like the existing `scope-crosswalk.md` files, saying what is covered, shallow or absent.

## Open questions

- Package names and whether layers 0 and 1 should be one package.
- Which openly licensed protocols to adapt for cell culture and molecular work, checked one by one for license and parameters.
- Whether to add a printable competency checklist per protocol for a supervisor to sign off at a real bench. This would be a practice aid only, not a record of competency.

## References (scope; accessed 2026-10-30)

- ASCP Board of Certification, *Technologist and International Technologist in Molecular Biology, MB(ASCP) and MB(ASCPi): Examination Content Guideline*, revised March 2023, read from an archived copy ([current page](https://www.ascp.org/boc/explore-credentials/view-all-credentials/MB)). A later revision exists and must be compared before layer 3 is scoped.
- CDC and NIH, [*Biosafety in Microbiological and Biomedical Laboratories*, 6th edition](https://www.cdc.gov/labs/bmbl/index.html), 2020.
- ISSCR, [*Standards for Human Stem Cell Use in Research*](https://www.isscr.org/standards-document), 2023.
- OSHA, 29 CFR 1910.1030, 1910.1450 and 1910.1200; FDA, 21 CFR Part 58; CMS, 42 CFR Part 493.
