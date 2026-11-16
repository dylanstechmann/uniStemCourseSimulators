# Human pluripotent stem cells: maintenance, morphology and quality control

**Status:** original scratch draft for outline lesson 7, developed with substantial AI assistance on 2026-11-15. The package remains **partial, unreviewed and formative-only**. This lesson uses an entirely synthetic hPSC-like line, synthetic microscopy panels and categorical QC results. **The synthetic maintenance loop does not authorize or certify hPSC work.** It does not establish hand skill, morphological diagnostic ability, biosafety or ethics approval, competency, a professional credential, or permission to handle human cells. Real work requires the receiving institution's approved procedures, risk assessment, ethics and governance review, and supervised training.

This lesson covers feeder-free culture on a defined matrix, daily observation and feeding, differentiated-area removal, routine clump passaging, intake and periodic QC, consent boundaries and traceable records. It does not teach hPSC derivation, embryo research, gene editing, directed differentiation, clinical manufacturing or donor recruitment. Practise only in the [synthetic hPSC maintenance simulation](#/bench/maintain-an-hpsc-culture-without-spontaneous-differentiation).

## Learning objectives

By the end of this lesson, you should be able to:

1. Explain how a defined matrix supports feeder-free hPSC maintenance, and evaluate coating coverage, cold-liquid handling, drying and lot traceability without treating a matrix as a feeder layer.
2. Interpret synthetic colony morphology and density, selectively remove displayed differentiated areas, and use observation, feeding and density evidence to make a passage decision.
3. Justify gentle small-clump rather than default single-cell passaging and calculate a clump allocation across destination wells.
4. Distinguish intake and periodic mycoplasma, STR-identity, karyotype and undifferentiated-marker QC, including quarantine until intake clearance and the limited meaning of each assay.
5. Evaluate consent and transfer restrictions, permissible-use boundaries, privacy and the records needed to connect maintenance actions, materials, deviations and QC evidence.

## 1. Feeder-free does not mean substrate-free

A feeder-free system removes the living feeder-cell layer; it does not remove the need for a suitable culture surface. In this lesson, a **defined matrix** is a characterized substrate used under a defined culture system to support attachment and colony maintenance. It is not a feeder cell, not a generic coating that can be swapped without evaluation, and not proof that the whole medium–matrix–line combination is defined or compatible.

The maintenance decision begins before cells reach the destination vessel. Confirm the matrix identity and lot against the line's approved local procedure, inspect the coating for complete and even coverage, and prevent drying. A temperature-sensitive liquid matrix also needs handling that avoids premature gelation or uneven deposition. Record the actual lot used rather than copying a planned lot into the record after the fact.

The simulation uses only `MAT_SYNTH_NEW` and `MAT_SYNTH_OLD`, with cold-liquid handling, complete/even coverage and a moist coating as its teaching rule. These aliases and choices do not reproduce a manufacturer's matrix protocol. Some runs hide a **degrading source matrix**. Even after all visible differentiated areas are removed, a larger differentiated area recurs on the next synthetic day. That pattern should trigger matrix investigation and a documented deviation, not an assumption that more aggressive removal will solve the underlying problem.

## 2. Read colonies as changing evidence

An undifferentiated hPSC culture is commonly assessed through a combination of compact colony organization, comparatively distinct boundaries and a consistent appearance across the culture. Differentiation may instead produce irregular edges, spreading cells, dark or heterogeneous regions, or a morphology that differs from the line's established reference. These are cues for closer assessment, not a universal visual diagnosis. Line history, culture system, magnification, imaging conditions and observer training all affect interpretation.

Use a repeatable daily observation routine:

1. Inspect the culture before disturbing it and compare with the line's reference images and prior observations.
2. Record estimated culture density and the location and extent of atypical or differentiated areas.
3. Mark and selectively remove the displayed differentiated areas when the local procedure calls for manual removal, avoiding unnecessary damage to neighbouring colonies.
4. Record what was removed and any residual or recurrent pattern. Manual removal is a local maintenance action, not proof that the culture is genetically stable, uncontaminated or functionally pluripotent.

**Worked example: residual differentiated area.** A synthetic 240 mm² colony panel contains 18 mm² judged differentiated. The initial fraction is 18/240 × 100 = 7.50%. Manual removal addresses 15 mm², leaving 3 mm². Residual differentiated area = (18 − 15)/240 × 100 = **1.25%**, not 5.00% and not zero merely because most of the affected area was removed.

## 3. Feeding, observation and density are linked decisions

A maintenance rhythm combines fresh medium, direct observation and a timely passage decision. Feeding without looking misses changes in morphology; looking without replenishing medium ignores the culture's changing needs. A fixed calendar reminder cannot substitute for either one, and an actual line's approved culture system determines the exact rhythm.

Density informs timing but is not a universal number. Colony merging, recurrent central changes, persistent atypical morphology and the line's previous growth pattern can matter alongside a percentage estimate. Passing too early may leave an unnecessarily sparse destination culture; delaying despite overgrowth can increase differentiation pressure. Record the reason for the decision, not just the percentage.

The simulator deliberately uses a simple three-day sequence. Before each `score_culture` action, the public current-observation panel displays that day’s density and differentiated area; no private server state is needed. The displayed density path is **42% → 60% → 78%**, with a routine-passage teaching window of **70–85%**. Continue on days 1 and 2 and passage on day 3. These numbers are simulation choices, not hPSC acceptance criteria. The model does not predict biological growth.

A complete medium change is required on each simulated day. An omitted feed, or `complete_medium_change=false`, creates one stress event and subtracts **8 points** from an arbitrary synthetic viability index, including on a terminal passage day. It adds **5 percentage points** only when another synthetic differentiated-area panel actually exists; day-3 or early-passage misses create no later panel and receive no morphology increment. These are visible, deterministic missed-feeding consequences for formative feedback—not measured hPSC responses. Real weekend, holiday or unexpected-delay decisions belong to the local approved plan and must be documented rather than improvised from this model.

## 4. Passage routine hPSCs as clumps, not automatically as single cells

The ordinary adherent-line habit of making a single-cell suspension is not the default in this hPSC maintenance exercise. Routine maintenance here uses **small clumps**, gentle handling and enough aggregate integrity to support the synthetic colony-based workflow. Excess trituration defeats that intention just as surely as selecting `single_cells`. A line-specific, validated single-cell method can exist for particular purposes, but it is not inferred to be routine from general cell-culture practice.

Prepare the destination matrix before the clump passage, distribute the suspension evenly, and record the method and allocation. Counting clumps for this exercise is an arithmetic panel, not an estimate of cell number, viability or future colony formation.

**Worked example: clump allocation.** A synthetic harvest panel contains 156 small clumps for six destination wells. An even allocation is 156/6 = **26 clumps per well**. Twelve wells at 26 clumps per well would require 312 clumps and is impossible with the displayed panel. The simulator's 2–3 triturations and six-well allocation are teaching choices, not a transferable reagent protocol.

## 5. Intake QC controls release from quarantine

An incoming line starts in **quarantine**. Consent/transfer review and the full intake QC bundle must clear before any maintenance or passaging action. Good-looking colonies cannot override missing permission, an incomplete bundle or a detected contamination result. The simulator makes downstream actions unreachable until those conditions are met.

The four assessments answer different questions:

| Assessment | Question it addresses | Important limit |
| --- | --- | --- |
| Mycoplasma testing | Is there evidence of this often non-obvious contamination at the tested point? | A result is tied to the sample, method and time; clear medium is not a substitute. |
| STR profiling | Does the human line's identity match its reference? | Identity does not establish genomic stability, sterility or pluripotency. The simulator stores only `match`, never a profile. |
| Karyotype assessment | Does the sampled material show the expected large-scale chromosomal pattern within the method's resolution? | It does not detect every genetic variant and is not an identity test. |
| Undifferentiated-state marker panel, often loosely called a pluripotency-marker panel | Is the observed marker pattern consistent with the undifferentiated state in context? | Marker expression alone does **not** prove functional pluripotency or differentiation capacity. |

Periodic QC complements intake testing because culture conditions, contamination events, misidentification and genomic change can arise later. Intervals should follow the institution's risk-based plan, culture history, bottlenecks and intended use. The exercise schedules the next bundle five passages after passage 8: 8 + 5 = **13**. That five-passage interval is a synthetic scheduling device, not a universal ISSCR or ATCC requirement.

Requested intake and periodic results use categorical teaching values: `not_detected` (or `detected` for a requested positive intake branch), `match`, `expected`, and `consistent_not_functional_proof`. Every unrequested assay is shown as `not_requested` in event data, event text and visible panels; it is not described as performed and reveals no underlying outcome. Marker interpretation cannot pass without requested marker evidence. These values are not laboratory reports and must not be imported into a real release decision.

## 6. Consent, ethics and records are independent of technical QC

Scientific quality does not create permission to use human-derived material. Before acquisition, verify the documented provenance, donor-consent scope and transfer conditions that apply to the intended work and jurisdiction. Keep restrictions accessible to the people using the line, and do not broaden the use because the cells appear healthy. The existing ISSCR *Guidelines for Stem Cell Research and Clinical Translation* record is a governance/ethics reference distinct from the 2023 basic-research Standards.

Use the minimum information necessary for traceability. This package accepts only synthetic aliases such as `SYNTH_HPSC_A`, `MTA_SYNTH_01` and `MED_SYNTH_01`; it does not accept donor names or identifiers, clinical details, actual consent documents, STR allele tables or genomic data. Real privacy and governance systems need more than an alias: access control, retention rules and institutional review remain outside the simulator.

A useful maintenance record connects:

- the approved line identifier and provenance/transfer reference;
- the actual medium and matrix lots and destination vessel;
- passage number, date/time, operator and applicable procedure version;
- daily density, morphology observations, feeding and selective-removal actions;
- deviations, including missed feeds, drying, uneven coating and recurrent differentiation;
- intake and periodic QC requests, categorical results, dates and linked reports;
- the rationale for release, continued maintenance, investigation or passage.

The simulation asks for only the synthetic subset of these fields. It does not simulate an electronic laboratory notebook, access-controlled consent store or validated QC information system.

## 7. Practise the synthetic maintenance loop

Open the [hPSC maintenance bench simulation](#/bench/maintain-an-hpsc-culture-without-spontaneous-differentiation). The action sequence is:

`review_intake` → `submit_intake_qc` →, for each of three days, `score_culture` → optional `remove_differentiated` → `feed_culture` → `decide_passage` → `complete_day` → `coat_destination_matrix` → `passage_clumps` → `submit_periodic_qc` → `record_maintenance` → `finish`.

The feed action may be omitted to explore the missed-feeding consequence; selective removal is required whenever the displayed area is nonzero. `complete_day` locks the current record, cannot be repeated, and is required before destination-matrix coating even after an early-passage decision; later score/removal/feed/decision mutations for that completed day are rejected. A consent failure, incomplete intake bundle or detected intake mycoplasma result finishes in quarantine with downstream checkpoints not applicable. Otherwise, a correct stable or degrading-matrix run can meet all **17 checkpoints**. In a degrading-matrix run, use the recurrent morphology evidence to select `matrix_investigation` and record a deviation. Finish only after acknowledging the synthetic-only boundary. The debrief reveals hidden conditions; the initial panels and public protocol do not reveal the current seed's hidden values.

## Common misconceptions

- **“Feeder-free means no attachment substrate is needed.”** The living feeder layer is gone, but the defined matrix and its handling remain central.
- **“Removing most atypical areas resets the culture to zero differentiation.”** Residual area is calculated from what remains; recurrent patterns require investigation.
- **“A calendar alone proves maintenance.”** Observation, feeding, density and the recorded rationale must agree.
- **“Single-cell suspension is always the safest default.”** This routine synthetic hPSC workflow deliberately preserves small clumps and limits handling.
- **“One QC result answers every quality question.”** Contamination, identity, genomic pattern and undifferentiated state are distinct; consent is a further independent gate.
- **“Markers prove functional pluripotency.”** They support a contextual undifferentiated-state assessment, not functional differentiation capacity by themselves.

## Sources, rights and simulation choices

All instruction, examples, questions and model rules are original synthetic work. No source text, table, figure, checklist or dataset is reproduced.

| Source | Use in this lesson | Rights evidence and package choice |
| --- | --- | --- |
| Ludwig TE et al., “ISSCR standards for the use of human stem cells in basic research”, *Stem Cell Reports* **18**(9):1744–1752 (2023), DOI [10.1016/j.stemcr.2023.08.003](https://doi.org/10.1016/j.stemcr.2023.08.003), PMCID [PMC10545481](https://pmc.ncbi.nlm.nih.gov/articles/PMC10545481/), PMID 37703820 | Perspective for material acquisition, consent/transfer context, authentication, genomic monitoring, marker interpretation and reporting | PMC page opened 2026-11-15 confirms bibliographic details and **CC BY-NC-ND 4.0**. This package deliberately selects **link-only-reference** anyway: no perspective text is adapted, reproduced or redistributed. |
| ISSCR, [*Standards for Human Stem Cell Use in Research* official page](https://www.isscr.org/basic-research-standards), English [December 2023 update](https://www.isscr.org/s/ISSCR_Standards_Dec23_Update.pdf) | High-level scope for characterization and reporting | Official page opened 2026-11-15 links `ISSCR_Standards_Dec23_Update.pdf` and states that the full Standards are strictly copyrighted and require written permission for reproduction. The full document, online sections and checklist remain **link-only**; no Standards text is adapted or reproduced. New ID `isscr-hpsc-standards-2023` is distinct from `isscr-stem-cell-guidelines`. |
| ISSCR, [*Guidelines for Stem Cell Research and Clinical Translation*](https://www.isscr.org/resources/guidelines-for-stem-cell-research) | Separate governance and permissible-use reference | Existing registry record remains link-only; it is not relabelled as the Standards and no guideline text is copied. |
| ATCC, [*Stem Cell Culture Guide*](https://www.atcc.org/resources/culture-guides/stem-cell-culture-guide) | General feeder-free matrix, daily maintenance, morphology, selective-removal, aggregate-passaging and QC context | Guide and [Website Terms of Use](https://www.atcc.org/policies/website-terms-of-use) opened 2026-11-15. Footer says all rights reserved; Scope of Use prohibits modification, display or distribution without written permission. **Link-only-reference**; no source procedure, threshold, wording or image is used. |
| NIST, [*Cell Line Identification and Authentication: Human Cell Lines Standards and Protocols*](https://www.nist.gov/programs-projects/cell-line-authentication/cell-line-id-and-authentication-human-cell-lines), updated 2025-08-14 | STR identity testing and its specific role | Page and NIST [Copyrights & Disclaimers](https://www.nist.gov/copyrights-disclaimers) plus [research licensing statement](https://www.nist.gov/open/license) opened 2026-11-15. Unmarked NIST web information is public information; non-SRD NIST works are generally US public domain with a worldwide reuse grant. Original paraphrase only, with attribution; linked ASN/ATCC and ICLAC material remains separate and is not copied. |
| MIT OpenCourseWare, [*20.109 Laboratory Fundamentals in Biological Engineering*, Spring 2010 syllabus and embedded calendar](https://ocw.mit.edu/courses/20-109-laboratory-fundamentals-in-biological-engineering-spring-2010/pages/syllabus/) | Non-equivalent scope comparator only | Reread 2026-11-15; footer rechecked as **CC BY-NC-SA 4.0**. Sessions 19–21 concern initiating cell culture, viability and analysis. No hPSC maintenance, defined-matrix, clump-passaging or hPSC-specific QC topic appears. **hPSC maintenance is beyond this comparator's demonstrated scope, not equivalent to it.** Link only; lab handouts were not read. |

The 42→60→78% path, 70–85% window, differentiation areas and penalties, three-day loop, 156-clump panel, 2–3 triturations, six wells, five-passage interval, hidden-event probabilities and all lot aliases are simulation choices. They are not sourced hPSC protocols or laboratory acceptance criteria. No FDA manufacturing guidance or revoked 21 CFR 610.30 mycoplasma method is used as an hPSC research protocol. The simulation does not predict growth, viability, future morphology, functional pluripotency, genomic stability or experimental success.
