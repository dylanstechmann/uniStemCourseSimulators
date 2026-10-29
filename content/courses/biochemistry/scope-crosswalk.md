# Biochemistry I scope crosswalk

This crosswalk compares the local package, version 0.7.0, with two published biochemistry courses: MIT OpenCourseWare 7.05 General Biochemistry, Spring 2020 ([calendar](https://ocw.mit.edu/courses/7-05-general-biochemistry-spring-2020/pages/calendar/), 32 sessions in two parts), and the University of Guelph BIOC*3560 Structure and Function in Biochemistry, Winter 2023 ([course outline](https://www.uoguelph.ca/mcb/system/files/BIOC3560_W23_SG_Final_0.pdf), six lecture parts). It was compiled with AI assistance on 2026-10-29 from the MIT session titles, the Guelph outline's learning outcomes and lecture topic titles, and the local readings and practice. It is an agent-run comparison, not a review by the owner or by a biochemistry instructor. It does not compare lecture content beyond those titles, problem sets, exams or workload, and topic alignment establishes no equivalence, credit or endorsement.

Two scope notes apply. MIT 7.05 is a one-semester survey of biomolecules and metabolism. BIOC*3560 is a third-year course that follows Guelph's introductory BIOC*2580 and concentrates on regulation: oxygen-binding proteins, enzyme regulation, carbohydrate and lipid metabolism, membranes and signalling. It therefore sets topic scope for those strands only, not sequence or depth. Status labels: **covered** means a local reading develops the topic with a worked example and practice; **shallow** means a local reading teaches part of the topic; **absent** means no local instruction; **elsewhere** means another local course teaches it; **local extension** means the package teaches a topic neither comparator names. Local numbers are lesson IDs (biochemistry-N or a named lesson), and each links to its reading.

## Comparator map

| Topic | MIT 7.05 | Guelph BIOC*3560 | Local lessons | Status |
| --- | --- | --- | --- | --- |
| pH, buffers and titration | Session 1 | — | [8](modules/08-amino-acids-charge-and-isoelectric-points.md) | Covered for amino-acid and protein charge; general buffer chemistry is in General Chemistry II [1](../general-chemistry-2/modules/01-acid-base-equilibria-and-buffers.md) |
| Amino acids and protein structure | Sessions 2, 4–5 | Learning outcome 1 | [1](modules/01-protein-structure-and-molecular-recognition.md), [8](modules/08-amino-acids-charge-and-isoelectric-points.md) | Covered |
| Protein purification | Sessions 3–4 | — | [Protein purification](modules/14-protein-purification-and-activity-data.md) and the [purification lab](labs/02-protein-purification-from-fractionation-data.md) | Covered |
| Protein folding and stability | Session 5 | — | [9](modules/09-protein-folding-and-stability.md) | Covered |
| Ligand binding, myoglobin, hemoglobin and cooperativity | Session 6 | Part A (protein–ligand interactions, myoglobin, hemoglobin, Hill equation) | [7](modules/07-binding-equilibria-and-cooperativity.md) | Covered for dissociation constants, depletion, Hill binding and cooperative unloading; the structural T/R account of hemoglobin allostery is shallow |
| The Bohr effect and O₂, H⁺ and CO₂ transport | Session 7 | Part A | [7](modules/07-binding-equilibria-and-cooperativity.md) | Shallow: one sentence names the rightward P₅₀ shift caused by lower pH, higher CO₂ and 2,3-bisphosphoglycerate; the mechanism and CO₂ transport are not developed |
| Enzyme chemistry, catalysis and mechanisms | Sessions 8–10 | Part B (enzyme review) | [2](modules/02-enzyme-mechanisms-and-inhibition.md) | Covered |
| Enzyme kinetics and inhibition | Session 11 | Part B (enzyme review) | [5](modules/05-enzyme-kinetics-from-data-and-inhibition-modes.md) and the [kinetics lab](labs/01-enzyme-kinetics-and-inhibition-from-data.md) | Covered |
| Allosteric enzymes and reversible covalent modification | Session 6 (allostery) | Part B | [4](modules/04-pathway-regulation-and-metabolic-integration.md), [10](modules/10-glycolysis-energy-charge-and-amp-signal.md), [12](modules/12-flux-control-and-layers-of-regulation.md), [Glycogen](modules/17-glycogen-storage-and-mobilization.md) | Covered inside pathway lessons; concerted and sequential allosteric models are not developed |
| Proteolytic activation of enzymes | — | Part B | — | Absent; named only by Guelph |
| Cyclin-dependent kinases | — | Part B | Cell Biology [12a](../cell-biology/modules/12a-cell-cycle-checkpoints-and-mitosis.md) | Elsewhere; named only by Guelph |
| Carbohydrate structure and polysaccharides | Sessions 12, 19 | — | [Glycogen](modules/17-glycogen-storage-and-mobilization.md) | Shallow: glycogen's glycosidic links and branches only |
| Membrane lipids, bilayer organization, membrane proteins and dynamics | Session 12 (introduction to membranes) | Part E | [33](modules/33-membrane-lipids-bilayers-and-membrane-proteins.md) | Covered in 0.7.0; previously absent |
| Channels, transporters and pumps | Session 13 | Learning outcome 4 | [28](modules/alternating-access-and-coupled-transport-cycles.md); Cell Biology [2](../cell-biology/modules/02-membranes-transport-and-compartmentalization.md) | Covered |
| Hormones, receptors, G proteins and second messengers | Sessions 14–15 | Part F (introduction to biosignaling, receptor enzymes, G protein-coupled receptors, steroid hormone receptors) | [34](modules/34-receptors-g-protein-switches-and-second-messengers.md); network logic in Cell Biology [10a](../cell-biology/modules/10a-receptor-signaling-and-network-logic.md) | Covered in 0.7.0; previously shallow, with cAMP and protein kinase A named only inside the glycogen and fatty-acid lessons |
| Gated ion channels | Session 13 (channels) | Part F | [34](modules/34-receptors-g-protein-switches-and-second-messengers.md), [28](modules/alternating-access-and-coupled-transport-cycles.md) | Shallow: named with their timescale; gating mechanisms are not developed |
| Nucleic acid structure | Session 16 | — | Cell Biology [6a](../cell-biology/modules/06a-dna-structure-and-replication.md) | Elsewhere |
| tRNA charging and translation | Sessions 17–18 | — | [29](modules/translation-charging-proofreading-and-energy.md) | Covered |
| Introduction to metabolism and bioenergetics | Sessions 19–20 | — | [3](modules/03-bioenergetics-and-central-carbon-metabolism.md), [6](modules/06-free-energy-coupling-and-redox.md) | Covered |
| Glycolysis and its regulation | Sessions 20–21 | Part C | [10](modules/10-glycolysis-energy-charge-and-amp-signal.md) | Covered |
| Gluconeogenesis and reciprocal regulation | Session 22 | Part C | [Gluconeogenesis](modules/16-gluconeogenesis-bypass-and-reciprocal-control.md) | Covered |
| Glycogen storage, phosphorylase and synthase | Session 22 | Part B | [Glycogen](modules/17-glycogen-storage-and-mobilization.md) | Covered |
| Citric acid cycle | Sessions 22–23 | — | [Citric acid cycle](modules/15-citric-acid-cycle-carbon-and-redox.md) | Covered |
| Fatty-acid oxidation and ketone bodies | Session 24 | Part D | [Beta-oxidation](modules/19-fatty-acid-beta-oxidation.md), [ketone bodies](modules/22-ketone-body-synthesis-and-use.md) | Covered |
| Oxidative phosphorylation | Sessions 25–26 | — | [11](modules/11-mitochondrial-bioenergetics-and-atp-yield.md) | Covered |
| Photosynthesis and CO₂ assimilation | Sessions 26–27 | — | [30](modules/photosynthetic-electrons-carbon-and-atp-balance.md) | Covered as a bounded electron, carbon and ATP ledger |
| Pentose phosphate pathway | Session 28 | — | [Pentose phosphate](modules/18-pentose-phosphate-pathway.md) | Covered |
| Fatty-acid synthesis, triacylglycerol metabolism and cholesterol | Session 29 | Part D | [Fatty-acid synthesis](modules/23-fatty-acid-synthesis.md), [cholesterol](modules/24-cholesterol-and-lipoproteins.md) | Covered |
| Amino-acid and nitrogen metabolism | Sessions 30–31 | — | [Urea cycle](modules/20-amino-nitrogen-and-urea-cycle.md), [carbon skeletons](modules/21-amino-acid-carbon-skeletons.md) | Covered |
| Nucleotide metabolism | Session 32 | — | [Nucleotides](modules/25-nucleotide-biosynthesis-and-salvage.md) | Covered |
| Tissue- and organism-level integration | — | Learning outcome 3 | [4](modules/04-pathway-regulation-and-metabolic-integration.md), [13](modules/13-reading-a-metabolic-perturbation.md) | Covered |
| Flux control coefficients | — | — | [12](modules/12-flux-control-and-layers-of-regulation.md) | Local extension |
| Reading a research article and writing a lay summary | — | Sections 5.2–5.3 | — | Absent; the Geroscience package has a [paper-reading lesson](../geroscience/modules/09-reading-an-aging-intervention-paper.md) |
| Problem sets and exams | Problem sets and four exams on the calendar | Quizzes and a final exam in the outline | Open homework and review practice; inactive candidates | Absent by design: all practice is ungraded and formative-only |

## What 0.7.0 changed

Both comparators teach membranes and signalling, and the local package had neither as a reading. A transport lesson existed, but no reading explained what a membrane is made of, and cyclic AMP and protein kinase A appeared inside the glycogen and fatty-acid lessons without an account of how a hormone produces them. A new week-8 reading, lesson 33, precedes the transport lesson. It derives aggregate shape from the packing parameter, relates chain length, unsaturation and cholesterol to the bilayer's physical state, classifies membrane proteins, tests a sequence with a stipulated hydropathy window and helix geometry, and quantifies lateral diffusion, FRAP mobile fraction and the decay of leaflet asymmetry. A new week-12 reading, lesson 34, precedes the glycogen lesson. It separates occupancy from response with a stipulated transducer model and spare receptors, treats the G protein as a GTP-timed switch, computes cascade amplification and steady-state cyclic AMP with its termination steps, and compares the phospholipase C, insulin-receptor PI3K–Akt and nuclear-receptor routes. Together they add six objectives, 25 practice items and eight retrieval cards.

## Remaining gaps

- The mechanisms of the Bohr effect and of 2,3-bisphosphoglycerate binding, and CO₂ transport (MIT session 7; Guelph Part A), which lesson 7 names in one sentence, and the structural T/R account of hemoglobin allostery.
- Concerted and sequential allosteric enzyme models, and proteolytic activation of enzymes (Guelph Part B).
- Carbohydrate structure beyond glycogen (MIT sessions 12 and 19).
- Gating mechanisms of ion channels.
- Reading a primary research article within this package (Guelph only).
- Graded homework and exams, measured workload, and review by a qualified person.
