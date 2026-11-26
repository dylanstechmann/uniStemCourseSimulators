# Optional integrative project guide: bounded habitat evidence package

**Status:** Original optional project in partial version 0.1.0; unreviewed, ungraded, zero-point and formative-only. It produces a paper/data evidence package, not an operational agricultural or habitat design. All values are synthetic.

## Learning objectives

1. Integrate site boundaries, lighting and resource balances into a traceable synthetic concept dossier.
2. Combine correction-aware biological evidence, conceptual load paths, dependencies and human decision gates without operational plans.
3. Rehearse outage and audit calculations and communicate assumptions, unresolved evidence and non-operational status in a final handoff.

## Project brief

Prepare five linked milestone records for a fictional controlled-environment concept. The aim is to show what can and cannot be concluded from public synthetic evidence. Use the six earlier lesson readings, the [audit CSV](../labs/habitat-audit.csv) and the [rehearsal CSV](habitat-project-rehearsal.csv). The project does not require physical work, software execution, plant material or contact with a site.

The rehearsal file marks every row `synthetic-original`. It supplies PPFD and photoperiod, fixture power, water terms, critical load, outage duration and simple schedule values. Values in different rows are alternatives, not measurements to pool. `predecessor_days` and `review_days` support a finish-to-start check: earliest finish = predecessor + review when there is one predecessor. If you create parallel branches, use the longest required predecessor.

| Row | PPFD (µmol m⁻² s⁻¹) | Hours | Water: start + new + recovered − consumed (L) | Critical load × outage |
| --- | ---: | ---: | --- | --- |
| R01 | 180 | 12 | 100 + 24 + 30 − 54 = 100 | 0.25 kW × 4 h = 1.0 kWh |
| R02 | 220 | 14 | 110 + 26 + 34 − 60 = 110 | 0.30 kW × 5 h = 1.5 kWh |
| R03 | 200 | 16 | 90 + 20 + 28 − 46 = 92 | 0.28 kW × 7 h = 1.96 kWh |
| R04 | 160 | 10 | 96 + 18 + 24 − 42 = 96 | 0.30 kW × 6 h = 1.8 kWh |

The public practice uses R02 DLI = 220 × 14 × 3600/10⁶ = **11.088 mol m⁻² d⁻¹**, R03 closing stock **92 L**, and R04 outage energy **1.8 kWh before reserves or losses**. These are worked checks, not operating setpoints.

## Milestone 1: concept and site boundaries

Define production and support zones, resource inputs, waste routes and external dependencies. Reconcile one area ledger and one water-stock ledger from lesson 1. Create a human-gate register for local land-use, safety, environmental and community questions. Mark every item unresolved unless the supplied synthetic record explicitly says reviewed; a calculation cannot change that status.

## Milestone 2: light, time, water and control evidence

Calculate R02 DLI and R03 closing water. Explain how timer commands would be reconciled with actual on/off state and measured power. Specify spatial PPFD, calibration and missing-data evidence. State why DLI, energy and inventory arithmetic do not establish plant response and why the project includes no nutrient formulation or dosing recipe.

## Milestone 3: biological evidence and structural work logic

Write a short evidence memo using Zong 2017 with its 2025 correction and Jin 2019 as distinct link-only records. Include comparator, independent-lineage, background-variant and assay-limit questions. Do not add sequences, laboratory steps or operational parameters. Then draw a conceptual load path to the foundation boundary and a WBS/dependency table. Include a longest-path calculation and gates for qualified design, permission, inspection and change control, without physical construction instructions.

## Milestone 4: outage and audit test

Compute R04 outage energy and recompute all six audit rows. Confirm A03 residuals of **+1.2 kWh** and **+2 L**, A04's missing-temperature status and the separate 6 h and 8 h outage scenarios. Explain why A01/A06 template reuse is not independent replication and why the audit does not support a pooled reliability claim.

## Milestone 5: bounded handoff

Assemble the five records with a common identifier scheme and links to the relevant reading, practice, CSV row and source. Include assumptions, residuals, missing evidence, unresolved comparator questions and named human gates. Finish with an explicit statement that the work is optional, zero-point, formative and non-operational. Do not claim field performance, construction readiness, habitability or life-support capability.

## Self-review and submission

Use the six Case studio entries: one integrative case and five project milestones. Each rubric is a zero-point checklist, not automated grading or expert review. A useful final package lets another reader reproduce every number from the displayed synthetic inputs and distinguish sourced facts, model assumptions and unresolved evidence. Keep third-party and owner repositories as links; do not paste their content into the handoff.

## Limits

This survey cannot settle crop performance, nutritional requirements, structural adequacy, local permission, treatment quality, emergency performance or human safety. Rehearsal success demonstrates arithmetic and evidence-boundary reasoning only. Qualified scientific, engineering and local review remains necessary for any real decision.
