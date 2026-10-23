# Bioreactors & Tissue Culture Engineering

**Maturity: partial. Version: 0.6.0.**

Scale cell culture and tissue maturation through mass transfer, shear, process monitoring, control, sterile-boundary reasoning, and design-of-experiments principles.

## Prerequisites

Cell biology; Statistics; Transport recommended. Structured required, recommended, and concurrent relationships appear in the manifest and remain subject to author review. This package establishes no university prerequisite equivalency.

## Authored outcomes

- Write a cell-culture mass balance.
- Estimate oxygen-transfer, mixing, shear, and scale-up constraints.
- Interpret growth kinetics and process data.
- Design controls and acceptance criteria for a reproducible process.

## Proposed 14-week schedule

This is a proposed scope, not a measured or reviewed semester. Each week lists its readings; weeks 1, 2, 5, 9 and 12 now have expanded instruction in growth/process balance, elemental biomass/product yields, oxygen transfer, mixing/scale-up, and process monitoring/control/quality. Week 4 now places fed-batch operation, with its volume-change balances and substrate-holding feed, between the batch-exhaustion lesson and continuous culture. Week 12 includes conceptual sterile-boundary mapping and limits of simplified log-reduction and sample evidence. All four original compact prototype readings have expanded primers beside the original lessons. Current inventory: 24 reading/activity routes, 132 public practice items, 82 retrieval cards and six Case studio prompts. Counts do not establish semester depth.

Every lesson has public formative items and retrieval cards.

| Week | Readings and activities |
| --- | --- |
| 1 | [Growth kinetics and process mass balance](modules/01-growth-kinetics-and-process-mass-balance.md) |
| 2 | [Growth kinetics: Monod saturation, yield and what limits a batch](modules/07-growth-kinetics-monod-and-yield.md); [Element-balanced biomass and product yields](modules/14-element-balanced-biomass-and-product-yields.md) |
| 3 | [Writing a cell-culture mass balance: substrate use, product accumulation and when a batch runs out](modules/06-cell-culture-mass-balance.md) |
| 4 | [Fed-batch culture: changing volume, dilution and feeding to hold a substrate](modules/15-fed-batch-culture-volume-change-and-feeding.md); [Continuous and perfused culture: chemostat steady states, washout and cell-specific perfusion](modules/08-continuous-culture-washout-and-perfusion.md); [Retention, maintenance and viable-state balances](modules/retention-maintenance-and-viable-balances.md) |
| 5 | [Oxygen transfer and consumption](modules/02-oxygen-transfer-and-consumption.md); [Assignment 1: retained-state and substrate ledger](assignments/coursework-01-retained-state-ledger.md) |
| 6 | [Sizing oxygen supply in a culture: kLa, driving force and the cell density a reactor can support](modules/05-sizing-oxygen-supply-and-cell-density.md) |
| 7 | [Virtual lab 1: measuring kLa by dynamic gassing-out](labs/01-measuring-kla-by-dynamic-gassing-out.md); [Oxygen-probe dynamics and parameter identification](modules/oxygen-probe-dynamics-and-identifiability.md) |
| 8 | [Controlling dissolved oxygen: the required kLa, the capacity limit and the control cascade](modules/11-dissolved-oxygen-control-and-the-capacity-limit.md); [Oxygen project guide: transfer capacity against a growing demand (optional, ungraded)](assignments/oxygen-capacity-project-guide.md); [Assignment 2: probe and process evidence](assignments/coursework-02-probe-and-process-evidence.md) |
| 9 | [Mixing, shear, and scale-up](modules/03-mixing-shear-and-scale-up.md) |
| 10 | [Mixing and scale-up: power, tip speed and what cannot be kept constant](modules/09-mixing-and-scale-up.md); [Two-zone transfer and local exposure](modules/two-zone-transfer-and-local-exposure.md) |
| 11 | [Shear, eddies and cells: the Kolmogorov scale and when stirring becomes damage](modules/10-shear-eddies-and-cell-damage.md); [Assignment 3: local exposure and exchange](assignments/coursework-03-local-exposure-and-exchange.md) |
| 12 | [Process monitoring, control, and quality](modules/04-process-monitoring-control-and-quality.md) |
| 13 | [Design of experiments: factorial designs, effects, interactions and replication](modules/12-factorial-design-of-experiments.md) |
| 14 | [Separating a mixing limitation from cell-line instability: designing a scale-down experiment](modules/13-designing-a-scale-down-experiment.md); [Assignment 4: process evidence and factorial interpretation](assignments/coursework-04-process-evidence-and-factorials.md) |

## Assessment and study policy

Every lesson has public formative items (numeric, single-choice, multiple-select, data-interpretation, structured-response and CSV-upload) mapped to its objectives, plus retrieval cards for the review queue; each practice assessment also lists the course outcomes its items assess. Week 7 is a synthetic-data virtual lab, week 8 adds an optional oxygen-capacity project guide with rehearsal practice, and week 14 pairs a lesson on designing a scale-down experiment with the course case and its self-assessment checklist. These are practice activities with unlimited retries and no institutional grade, university credit or transferable credit. Workload has not been measured.

## Connected coursework (open, ungraded)

Four original reports require retained viable/substrate/dead-state ledgers and domain checks (week 5), process/probe fit and identifiability evidence (week 8), local/total two-zone exposure and exchange bounds (week 11), and a synthetic factorial/process-evidence analysis (week 14). Foundations in weeks 4, 7 and 10 supply the added derivations. Two analytic/arithmetic CSVs are invented normalized tables, not measured data or biological replication. Retain code, derivations and reports locally; checkpoints evaluate selected outputs and choices. The existing gassing-out lab and oxygen project remain available. Workload and qualified review are open.

## Optional oxygen-capacity project (ungraded)

The [oxygen project guide](assignments/oxygen-capacity-project-guide.md) makes the project below usable as open practice. It restates the project's model, parameters and tasks, works a separate normalized model, and pairs a rehearsal model with open practice items in week 8. Five milestones, suggested for weeks 8–9, are Case studio self-checks whose responses can be saved privately and are not submitted for grading.

## Inactive integrative project draft

The [oxygen-capacity portfolio](assessment-specs/oxygen-capacity-project-draft.md) uses a normalized growing-demand model to compare initial transfer capacity, a quasi-steady threshold and the transient dissolved-oxygen threshold crossing. It extends the course's mass-balance and control lessons without repeating the existing gassing-out `kLa` fit. All parameters are synthetic; the paper-only draft itself is not scheduled, assigned, submitted or graded, the open project guide above does not submit work to it, and the draft gives no real process specification.

## Current limitations

The schedule above is proposed, not measured, and has not been reviewed by a qualified instructor. There are no graded homework sets, midterm or final; the optional project guide and its rehearsal are ungraded practice, and the project draft remains inactive. The former compact prototype readings have expanded primers, but that does not resolve the broader workload, assessment, laboratory, and review gaps. The package cites no new papers: the lessons teach standard first-order relations with synthetic data, and the typical values they quote (power numbers, dimensionless mixing times, saturation concentrations, specific uptake rates) are textbook-level and vary between sources. All cultures, vessels, cell lines and numbers are synthetic; the new biomass formula and product are stipulated bookkeeping surrogates, not measured compositions or yields. No lesson gives a laboratory protocol, process recipe or medical advice, and nothing here asserts anything about a real cell line, vessel or process. Qualified human review is required before this course could meet the complete-course standard.

## Sources and licensing

The MIT OCW 10.442 Spring 2005 undergraduate calendar assigns sessions 11–12 to stoichiometry of growth and product formation and session 22 to media and air sterilization. The local additions address a narrower elemental-balance example and a conceptual sterile-boundary/evidence strand; they do not reproduce source materials or provide process instructions. Read source-map.json for module provenance and content/SOURCES_AND_LICENSES.md for the software/content license boundary. Listed source courses are public curriculum comparators; no affiliation or equivalency is implied.

The 0.6.0 expansion compares actual growth, continuous-culture, oxygen/control, mixing and factorial readings with [MIT OCW 10.442 Spring 2005 calendar](https://ocw.mit.edu/courses/10-442-biochemical-engineering-spring-2005/pages/calendar/) and [syllabus](https://ocw.mit.edu/courses/10-442-biochemical-engineering-spring-2005/pages/syllabus/): growth/stoichiometry/models/continuous lectures 9–16, design/transfer 17–21 and scale/animal-cell 23–26. The source includes six problem sets and four quizzes and a broader microbial/enzyme curriculum; four local open reports do not reproduce that sequence. New phenomenological laws require explicit admissibility boundaries; an observed probe curve or passing bulk mean does not establish every process parameter or local state. All text/problems/tables are original and AI-assisted; no source asset or measured dataset is imported. Experimental competence, validated process models, broader coursework and qualified review remain open.
