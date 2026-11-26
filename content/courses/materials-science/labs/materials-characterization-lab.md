# Synthetic multi-technique materials-characterization lab

**Status:** Original zero-point lab in partial Materials Science 0.1.0; unreviewed and formative-only. Every material, observation and value in `materials-characterization.csv` is synthetic fictional data. No row is an experimental measurement, independent replication or validated material identification. This lab supplies no instrument operating procedure, acquisition settings or specimen-preparation protocol.

## Learning objectives

1. Recompute diffraction spacing, cubic lattice parameter and mass-loss relationships for every synthetic row.
2. Integrate structural, thermal and mechanical records as separate evidence channels rather than interchangeable identifiers.
3. Preserve unknown fields, fictional provenance and non-operational limits in a multi-technique interpretation.

## Evidence and data dictionary

Download [materials-characterization.csv](materials-characterization.csv). Preserve the original and work on a copy or in a simple table reader. No executable project code or physical instrument is needed. Every `data_status` field must remain `synthetic-original`, and every `fictional_material` is an invented label rather than a commercial or naturally occurring substance.

| Fields | Meaning and bounded use |
| --- | --- |
| `record_id`, `fictional_material` | Scenario identifiers only; they do not certify identity or independent provenance |
| `h`, `k`, `l` | Stipulated Miller indices for a fictional cubic-plane assignment |
| `two_theta_deg`, `wavelength_nm` | Supplied detector-angle convention and wavelength in consistent length units |
| `mass_start_mg`, `mass_end_mg` | Fictional initial and final masses for relative-change arithmetic |
| `thermal_event_c` | A supplied thermal-event label, not an instruction to heat anything; blank means unknown |
| `modulus_gpa`, `yield_mpa` | Separate fictional mechanical channels, not derivable from diffraction or mass loss |
| `evidence_status` | Declares complete supplied fields or a specific unknown; it is not a quality approval |

For each row, first halve the displayed 2θ to obtain θ. Under first-order Bragg geometry, compute d = λ/[2sin(θ)]. Then, only because the cubic assignment is stipulated, compute a = d√(h²+k²+l²). Keep enough intermediate precision to avoid changing the final result through premature rounding.

Independently compute mass loss = (mass start − mass end)/mass start × 100%. Use each row’s own initial mass, not a shared denominator. A percentage quantifies mass change only; it does not identify the evolved species, reaction mechanism or residual phase.

## Audit sequence

**1. Check provenance and structure.** Confirm six unique record IDs, fourteen expected columns, fictional names and synthetic labels. Verify that C05 has a blank thermal-event field with `thermal-event-unknown`. Do not convert that blank to zero, copy another row’s event or silently remove the record.

**2. Recompute every diffraction relationship.** For C02, 2θ = 40.0° and λ = 0.154 nm, so d = 0.154/[2sin(20.0°)] = **0.225133… nm**. For C04, 2θ = 44.0° and the stipulated plane is (111). Compute d with θ = 22.0°, then a = d√3 = **0.356021… nm**. Repeat the same independent process for C01, C03, C05 and C06 rather than checking only the public examples.

**3. Recompute every mass-loss relationship.** C03 changes from 100.0 mg to 96.5 mg, giving (100.0 − 96.5)/100.0 × 100 = **3.5%**. Calculate all other rows from their own values. Positive loss does not reveal why the mass changed, and agreement between two percentages would not create independent chemical evidence.

**4. Keep technique channels distinct.** Diffraction constrains geometric spacing under the stated model. Thermal-event fields provide separate observations requiring calibration and interpretation. Modulus and yield values describe mechanical channels and cannot be inferred from the diffraction arithmetic. Mass loss cannot select among chemical explanations without additional evidence.

**5. Write a joint but bounded interpretation.** For each fictional sample, list supplied observations, derived d and a, derived mass loss, mechanical values, unknowns and plausible alternatives. Explain whether channels are consistent, contradictory or simply unrelated. Consistency is not uniqueness: one cubic-consistent spacing and one thermal event do not prove complete phase identity, composition, texture or processing history.

## Common mistakes

- Using 2θ directly in the sine instead of θ.
- Applying cubic geometry before establishing the stipulated cubic assignment.
- Rounding d aggressively before calculating a.
- Dividing mass loss by final mass or by another row’s initial mass.
- Treating an empty thermal field as 0 °C.
- Inferring chemical species, fatigue life, corrosion compatibility or material approval from unrelated channels.
- Adding instrument settings or procedural steps that the dataset does not contain.

## Expected self-check

A complete handoff contains all six rows, both diffraction equations, all six d and a values, all six mass-loss percentages, the C05 unknown and a channel-by-channel interpretation. It distinguishes fictional data from physical measurements and includes no acquisition or operating instructions. Public practice checks C02 d, C03 mass loss and C04 a with independent arithmetic and misconception responses; package tests independently recompute all rows.

The official [MIT 3.091SC Fall 2010 syllabus](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/syllabus/) and [MIT 3.012 Fall 2005 calendar](https://ocw.mit.edu/courses/3-012-fundamentals-of-materials-science-fall-2005/pages/calendar/) remain link-only comparators for diffraction and broader material behavior. Existing mechanics and biomaterials records are prerequisite/application links only. No third-party figure, table, problem, data or operating procedure is imported.
