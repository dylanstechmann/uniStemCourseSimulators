# Records and traceability

**Status:** Original, partial, unreviewed, formative-only lesson 8 of the outlined cell-culture layer. All identifiers, observations and calculations below are synthetic teaching data. This lesson intentionally has **no bench protocol and no simulator model**; it develops record-joining and evidence reasoning rather than a physical workflow.

A culture vessel is not self-describing. “LUMO-A, passage 12” becomes useful only when records connect that vessel to its parent bank vial, earlier passages, population doubling level (PDL), medium and reagent preparations, matrix lot, operator, dates and storage locations. Traceability is the ability to follow those links in both directions: from a bank vial to every descendant, and from an unexpected observation back to all inputs that might explain it. It does not by itself prove that a record is correct or that a shared input caused an event.

## Learning objectives

By the end of this lesson, you should be able to:

1. Distinguish master and working cell-bank tiers and preserve parent–child provenance when banks, vials and culture vessels are derived from one another.
2. Reconcile passage and PDL ledgers from raw starting and harvested cell numbers, keeping passage events, calculations and corrections distinct.
3. Join vessel, preparation and lot tables across media, reagents and matrices to identify shared exposures and enumerate affected vessels without overclaiming causation.
4. Evaluate labels and record corrections using unique identifiers and the five ALCOA principles: attributable, legible, contemporaneous, original and accurate.
5. Outline a contamination-investigation chain of records and an incident/deviation handoff, while deferring detailed quality-system and regulatory instruction to layer 4.

## One outcome and its limits

The integrated outcome is to reconstruct an auditable synthetic culture history and defend a bounded contamination lead from linked records. This is information reasoning, not physical laboratory practice. A tidy ledger cannot rescue an ambiguous identifier, a missing parent link or an unrecorded lot. Neither can a database join replace direct laboratory evidence, local review or an authorised investigation.

## Master and working cell-bank tiers

A **master cell bank (MCB)** is a laboratory's designated reference stock for a particular cell line and banking history. A **working cell bank (WCB)** is derived from a specified master-bank culture or vial and supplies routine work, reducing repeated use of the master stock. The exact names, release specifications and number of permitted tiers are local decisions; the labels “master” and “working” do not themselves establish characterisation, sterility, identity or suitability.

The crucial distinction is provenance, not the freezer box alone. Suppose synthetic vial `LUMO-A-MCB-M07` is designated master stock at passage 8 and cumulative PDL 12.0. A derivative bank `LUMO-A-WCB-W03` records that vial as its parent. If its expansion started with 1.00 × 10⁶ viable cells and yielded 2.00 × 10⁶, its PDL increment is log₂(2.00/1.00) = 1 and its bank record starts at cumulative PDL 13.0. Routine vessels then name `W03`, not merely “LUMO-A”, as their immediate bank parent.

A working-bank vial does not silently become a new master vial because the original master inventory is inconvenient to retrieve. Creating or redesignating a tier is a controlled provenance event requiring the laboratory's own review. Conversely, a master-bank identifier alone is insufficient: vial ID, freeze date, passage and PDL at freeze, storage location and links to characterisation or release records must agree. Retain the parent ID when aliquoting or moving a vial; a location change is not a new biological derivation.

For every derivative, record the **event type** (expansion, aliquot, thaw, passage, relocation or redesignation), **parent ID**, **new ID**, **timestamp**, **operator**, and **supporting record ID**. This makes a directed chain rather than a list of disconnected names. Cycles, two parents for an ordinary single-parent expansion, or a WCB listed as ancestor of its own MCB are reconciliation failures, not details to hide.

## Passage and PDL ledgers

A passage number counts subculture events under the laboratory's convention. PDL estimates accumulated doublings from cell numbers. For one interval with `N0` viable cells at the start and `Nf` viable cells at harvest:

`PDL increment = log₂(Nf/N0) = log10(Nf/N0)/log10(2)`

`new cumulative PDL = previous cumulative PDL + PDL increment`

The raw `N0`, `Nf`, units, counting-record links and rounding convention belong in the ledger. Do not infer PDL from the passage-number difference: one passage may contain zero, one, two or a non-integer number of estimated doublings. Also do not overwrite a previous cumulative value with only the interval increment.

**Worked ledger.** Synthetic line LUMO-A enters passage 12 at cumulative PDL 8.0. Two linked entries follow:

| Event ID | Vessel | Passage | N0 (10⁶ viable cells) | Nf (10⁶ viable cells) | Increment | New cumulative PDL | Count record |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| E-212 | V-090 | 12 | 1.25 | 2.50 | log₂(2.50/1.25) = 1 | 9.0 | C-212 |
| E-213 | V-091 | 13 | 0.75 | 3.00 | log₂(3.00/0.75) = 2 | 11.0 | C-213 |

Passage 13 is one event after passage 12, yet it adds two PDL. The final value is **11.0**, not 10.0, 13.0 or 3.0. If the raw record for E-213 instead showed `Nf = 1.50`, the computed increment would be 1 and the cumulative value 10.0. A correction would retain the original entry, identify who changed it, when and why, and link the evidence. Silent replacement would destroy the discrepancy that needs investigation.

A ledger should also preserve skipped, discarded and terminated branches. Deleting an aborted passage because no descendant survived can make later identifiers inexplicable. Mark its disposition and reason rather than rewriting history. PDL is an estimate based on the declared viable-cell convention, not a direct count of every division and not a measure of identity, genetic stability or future performance.

## Lot tracking across media, reagents and matrices

Track a **received lot** separately from a **prepared batch** and an **aliquot**. A received container has a supplier/material identifier, supplier lot, internal lot ID, receipt and expiry information, storage condition and receiving record. A supplemented-medium preparation has its own batch ID and links to every component lot. An aliquot retains its source batch plus a unique aliquot ID. Copying only a product name into a culture ledger loses exactly the distinctions needed during an investigation.

The useful join keys differ by material:

- **Media:** basal-medium lot, supplement lots, preparation batch, preparer, preparation/expiry timestamps and vessels receiving that batch.
- **Reagents:** dissociation reagent, buffer, dye, cryoprotectant or other reagent lot; any dilution/preparation record; and each use event.
- **Matrices:** matrix material lot, coating/preparation batch, coating timestamp, storage history and coated-vessel IDs.

A certificate or release result can be linked as evidence, but its presence does not prove that the correct lot reached a vessel. The chain must include the actual use event. When space on a physical label is limited, a durable unique barcode or alphanumeric ID can point to the full ledger; the human-readable label still needs enough content and identity information to prevent selection errors under local rules.

## Labels and ALCOA record integrity

A useful vessel or vial label carries a **unique identifier**, cell-line/bank or preparation identity as appropriate, and the local minimum fields needed to distinguish passage, date and ownership. The ledger expands that ID into parent, PDL, lots, operator, location and disposition. “A. Lee, cells” is neither unique nor reproducible. Two vessels named `P12` are ambiguous unless their line, bank and event IDs are also distinguished. Never recycle a disposed vessel ID for a later culture.

ALCOA names five record-integrity properties:

- **Attributable:** the actor and later reviewer/corrector are identifiable.
- **Legible:** the original and later entries remain readable and interpretable.
- **Contemporaneous:** the observation is recorded when it occurs, not reconstructed from memory days later.
- **Original:** the first capture or a verified preserved copy remains available, including raw counts and source identifiers.
- **Accurate:** entries reflect the observation and calculations are checked; errors are corrected transparently.

For a paper correction, preserve the original and add the corrected value, date, attribution and reason under local procedure. For an electronic correction, preserve an audit trail rather than replacing the prior value without history. Backdating an entry, overwriting `PDL 11` with `PDL 10`, or copying a neighbour's lot because “they were probably the same” fails the reasoning even when the final value happens to be correct.

This lesson only names and applies these basics to synthetic records. The planned layer-4 **`lab-quality-systems`** package owns deeper documentation control, audit trails, deviations/investigations, corrective and preventive action, training records, GLP and CLIA. No CFR registry expansion or regulatory-compliance instruction belongs in this lesson.

## Worked synthetic trace: join three lot tables

On 2026-06-17, a synthetic review flags four cultures for the same confirmed contamination phenotype. The task is to find shared inputs, not to guess a culprit from memory. Table 1 joins each vessel to a preparation through `preparation_id`; Table 2 connects preparations to medium and matrix use; Table 3 resolves medium batch to basal-medium and supplement lots.

**Table 1 — culture observations**

| vessel_id | preparation_id | observation | record |
| --- | --- | --- | --- |
| V-101 | P-401 | positive | OBS-101 |
| V-102 | P-401 | positive | OBS-102 |
| V-103 | P-402 | positive | OBS-103 |
| V-104 | P-402 | negative | OBS-104 |
| V-105 | P-405 | positive | OBS-105 |
| V-106 | P-406 | negative | OBS-106 |

**Table 2 — preparation and matrix use**

| preparation_id | medium_batch_id | matrix_lot_id | dissociation_lot_id |
| --- | --- | --- | --- |
| P-401 | F-31 | MX-07 | D-12 |
| P-402 | F-32 | MX-07 | D-12 |
| P-405 | F-31 | MX-09 | D-13 |
| P-406 | F-33 | MX-09 | D-13 |

**Table 3 — medium formulation lots**

| medium_batch_id | basal_medium_lot | supplement_lot |
| --- | --- | --- |
| F-31 | BM-24-118 | S-08 |
| F-32 | BM-24-118 | S-09 |
| F-33 | BM-24-119 | S-10 |

Perform the joins explicitly:

1. Select the positive vessels: V-101, V-102, V-103 and V-105, so **four** vessels are in scope.
2. Join their preparation IDs: V-101/V-102 → P-401, V-103 → P-402 and V-105 → P-405.
3. Join medium batches: P-401/P-405 → F-31 and P-402 → F-32.
4. Resolve formulation lots: both F-31 and F-32 contain basal medium **BM-24-118**. That lot is therefore shared by all four positive vessels.
5. Test alternative joins. Matrix MX-07 misses V-105, which used MX-09. Supplement S-09 misses V-101/V-102/V-105, which used S-08. Dissociation lot D-12 also misses V-105. BM-24-119 belongs only to negative V-106 in this small dataset.
6. Preserve the negative comparisons. V-104 is negative despite receiving F-32/BM-24-118, so shared exposure is not perfectly associated with the outcome and is not proof of causation.

The defensible result is: “All four flagged vessels have a documented BM-24-118 exposure; investigate that common medium lot, its preparations and handling, while retaining other explanations and the discordant negative vessel.” It is not: “BM-24-118 is confirmed as the source.” Next steps can include checking retained samples and preparation records under local procedures, finding every other vessel joined to F-31/F-32 or the same received lot, and looking for differences in timing, operators and handling. A common lot is a **lead generated by a join**, not a causal assay.

If V-103's ledger said only “basal medium” and omitted P-402, the F-32 and BM-24-118 links could not be reconstructed from these tables. The repair is to locate the original preparation/use evidence by prep ID, not to borrow V-104's lot or assume that the newest delivery was used.

## Contamination investigation and incident/deviation outline

A chain of records should let an investigator move from **observation → vessel → event/preparation → component lots → other exposed vessels**, and back again. Preserve the observation timestamp, test record, raw evidence, containment/disposition entries and every join used. Include negative and unresolved records so the analysis is not restricted to convenient positives.

At this layer, an incident/deviation record is an **outline** with:

1. Immediate safety and containment actions under local procedures.
2. What happened, when it was detected, who detected it and which records are original evidence.
3. Initial scope: vessels, bank parents, passages, preparations, lots, equipment/locations and dates potentially connected.
4. The trace logic and competing hypotheses, including missing or conflicting evidence.
5. A handoff for authorised review, classification, investigation, actions and follow-up; closure is not self-declared by the person preparing the trace.

Do not convert this outline into instruction on root-cause tools, corrective-action effectiveness, GLP, CLIA or legal reporting. Those belong to layer 4 and institutional procedures. Here, the assessable skill is producing a complete, reproducible handoff and stating what the joined evidence cannot decide.

## Common mistakes

- Treating MCB/WCB as freezer locations rather than derivation tiers, or deriving a replacement master bank without a recorded parentage decision.
- Equating one passage with one doubling, dropping the previous cumulative PDL, or retaining only rounded results without raw `N0` and `Nf`.
- Recording “medium”, “reagent” or “matrix” without resolving the received lot through the actual preparation/use event.
- Assuming a lot shared by positives must be causal, ignoring negative comparisons or declaring every co-occurring input equally supported.
- Repairing a missing join by inference, overwriting an old value, backdating a correction or reusing a vessel ID.
- Writing a long deviation narrative without the keys needed to reproduce its scope.

## Scope and sources

The reading, schemas, examples, tables, items and feedback are original and developed with substantial AI assistance. All names and values are synthetic; no external dataset or problem is imported.

[ISBER Best Practices for Repositories, fifth edition](https://www.isber.org/page/BPR) was confirmed from its official landing page as published in December 2023. The page identifies the fifth-edition resource and its companion article, DOI [10.1089/bio.2023.0140](https://doi.org/10.1089/bio.2023.0140). Its [Terms of Use Agreement](https://cdn.ymaws.com/www.isber.org/resource/resmgr/website/ISBER_Terms.pdf), revision August 18, 2020, was opened and checked on 2026-11-15. ISBER grants limited access/use for personal study, teaching and non-commercial purposes while reserving other reproduction and distribution rights; its landing page also asks readers not to repost the PDF or direct download link. This lesson therefore uses the **landing page as a link-only biorepository scope reference**, does not reproduce ISBER text, tables or recommendations, and does not claim page-level alignment or endorsement. The complete Best Practices document was not imported into this package.

The [MIT OpenCourseWare 20.109 Laboratory Fundamentals in Biological Engineering, Spring 2010 syllabus/calendar](https://ocw.mit.edu/courses/20-109-laboratory-fundamentals-in-biological-engineering-spring-2010/pages/syllabus/) was reread on 2026-11-15. Its general notebook-keeping aim and cell-culture initiation/viability sessions provide only a limited comparator; they do not establish a master/working-bank or three-table traceability sequence. The page footer's [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) link was rechecked, but this package deliberately retains link-only comparator use and copies no OCW wording, assignments or assets.

Institutional procedures and qualified local review govern real record systems and investigations. This unreviewed formative lesson establishes no competency, professional credential, regulatory compliance or authorisation to handle cells.
