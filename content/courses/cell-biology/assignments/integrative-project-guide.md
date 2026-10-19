# Integrative project guide: linked evidence across layers

**Status:** optional, ungraded project practice. Milestone responses are saved privately in the Case studio and are never submitted, scored or graded. A separate inactive project candidate, its machine checks and its human rubric remain unreviewed.
**Introduced in:** course package version 0.62.0.
**Suggested pace:** milestones in weeks 10, 11, 13 and 14. These are planning bounds, not measured workload or deadlines.
**Lessons to use:** [Gene expression, controls and replicate-level reasoning](../modules/04c-expression-controls-and-replicate-reasoning.md), [RNA processing and isoform evidence](../modules/08a-rna-processing-and-isoform-evidence.md), [Signaling dynamics, feedback, and perturbation evidence](../modules/10b-signaling-dynamics-feedback-and-perturbations.md) and [Integrative regenerative-biology study design](../modules/13b-integrative-regenerative-study-design.md).
**Datasets:** the [project culture table](../assessment-specs/integrative-project-candidate-cultures.csv) (forms A and B) and the [rehearsal cultures](project-rehearsal-cultures.csv).

## Purpose

The project asks how a soluble signal and a matrix condition are associated with five measured layers in one synthetic culture experiment: RNA abundance, recovered protein, a short signaling trajectory, a marker-positive fraction and a separately defined function proxy. The goal is to carry evidence across layers without collapsing them. A good project asks a question the measurements can answer, keeps each layer's claim separate, names what the design cannot separate, and proposes a matched follow-up that could.

The values are deterministic synthetic teaching data. They are not draws from a biological distribution, so they do not support p-values or calibrated confidence intervals, and they say nothing about any real cell type, material or therapy.

## The experiment

Work with **form A**. Form B is a parallel set with different values for a second attempt or a comparison.

Each form has six conditions, four independently prepared cultures per condition, and two endpoint times (0 and 48 hours): 48 rows per form. The principal comparison is a two-by-two layout of **control**, **signal_high**, **matrix_high** and **both**. **signal_low** adds a second exposure level. **rescue** is a separately prepared comparison; its name does not establish that the intervention is specific or which pathway position it acts on.

The independent unit is the **culture**. Culture identifiers are unique, and matching numeric suffixes in different conditions do not pair cultures. A culture measured at 0 and 48 hours is still one unit. Cells, RNA counts, technical channels and aliquots are measurements within a culture. The three pERK columns come from a separate short experiment on matched aliquots at 0, 10 and 30 minutes; they repeat in both endpoint rows of the same culture, so use them once per culture and keep minutes distinct from hours.

## Columns and transformations

| Columns | What they record | How to use them |
| --- | --- | --- |
| `seeded_cells`, `viable_cells` | Cells seeded and viable cells recovered | Viable cells are the denominator for per-cell values; lost cells were not profiled, so report recovery as well |
| `rna_signal_eq`, `rna_background_eq`, `spike_input_eq`, `spike_recovered_eq` | A shared RNA-abundance signal, its background, and an external recovery reference | Corrected RNA = (signal − background) × spike input / spike recovered; divide by viable cells/1000 |
| `protein_signal_ug`, `protein_background_ug`, `protein_recovery_fraction` | Recovered protein in micrograms, background, and the extraction recovery fraction | Corrected protein = (signal − background) / recovery fraction; divide by viable cells/1000 |
| `marker_positive_viable` | Marker-positive cells among viable cells | Marker % = 100 × marker-positive / viable cells |
| `functional_events_viable` | A fictional function-associated event among viable cells | Function % = 100 × events / viable cells; joint marker-and-function identities are not supplied |
| `perk_0_au`, `perk_10_au`, `perk_30_au` | Background-corrected pERK at 0, 10 and 30 minutes, arbitrary units | Trapezoidal area = 5·y0 + 15·y10 + 10·y30, in AU·min |
| `matrix_modulus_pa`, `accessible_ligand_relative` | Assigned material modulus and relative accessible ligand | matrix_high changes both, so modulus and ligand effects cannot be separated by these comparisons |

**In words:** subtract background first; then correct for the stated recovery; then divide by the number of viable cells in thousands. Percentages divide a count of viable cells by all viable cells. The pERK area adds the two trapezoids between 0 and 10 minutes and between 10 and 30 minutes.

The RNA column is a shared abundance signal, not an isoform or transcription-rate assay. The protein column is a quantity, not a mature-function measurement. The marker is not a potency or permanence assay, and the function proxy is deliberately distinct from the marker.

**Order of operations.** Compute every per-culture quantity first. Then average the four cultures in each condition with equal weight, and report their spread descriptively. A pooled fraction (all marker-positive cells divided by all viable cells across cultures) weights cultures by their cell numbers and answers a different question. Use the integer counts supplied rather than a nominal percentage.

## Worked rehearsal: one culture

The rehearsal table uses the same columns with its own values. For rehearsal culture R-control-01:

- RNA: (420 − 20) × 100/80 = 500 corrected units, and 500/(8000/1000) = 62.5 per 1000 viable cells.
- Protein: (0.405 − 0.005)/0.80 = 0.50 μg, and 0.50/8 = 0.0625 μg per 1000 viable cells.
- Marker: 100 × 1600/8000 = 20.0%. Function: 100 × 400/8000 = 5.0%.
- pERK area: 5 × 0 + 15 × 60 + 10 × 20 = 1100 AU·min.

## Rehearse before using form A

The [rehearsal table](project-rehearsal-cultures.csv) holds eight cultures: control and signal_high, one 48-hour endpoint each. Open **Integrative project rehearsal: per-culture transformations (open, ungraded practice)** in the Practice gradebook, or answer the same items on this page. They check the culture-level transformations, the equal-culture means, a pooled-versus-equal comparison, and the boundaries between layers. The rehearsal values are not the form A or B results, and no software check scores your form A analysis.

## Five milestones in the Case studio

Open the course's **Case studio**. Each milestone below is a separate case with its own self-check list. Drafts are private, bound to this course version, included in your account export and never graded. The Case studio stores text only, so keep your CSV and figure files yourself.

| Milestone | Suggested week | Deliverable |
| --- | --- | --- |
| M1 Question and scope | 10 | A 150–250-word note: one answerable question, the principal comparison, the independent unit, the built-in limitations, and a data dictionary in your own words |
| M2 Analysis plan | 11 | Every transformation in order, the denominators, culture and time handling, controls present and absent, and two competing explanations with the readout that separates them |
| M3 Evidence summary | 13 | A working CSV with one row per culture and time, an equal-culture condition summary, and a labelled figure with a text alternative; paste the summary and alternative text into the case |
| M4 Interpretation and follow-up | 14 | A 400–700-word interpretation that keeps the layers separate, names two alternatives, and designs one factorial follow-up with the result that would distinguish them |
| M5 Methods note | 14 | A short note sufficient to reproduce your tables and figure, including tools, any AI assistance and limitations |

## Self-review guide

Before marking a milestone's self-checks, compare your draft with these descriptions of strong work.

| Criterion | Strong work | A common gap |
| --- | --- | --- |
| Question and scope | One specific question answerable from the named comparisons, layers and units, bounded to this synthetic in-vitro model | A broad aim such as "better tissue" with no comparison, or a clinical claim |
| Evidence summary | Correct culture and time accounting, equal-culture summaries across layers, raw and derived values labelled | Technical counts or times treated as extra cultures |
| Controls and alternatives | Present and absent controls named; two specific alternatives, including the ligand/modulus confound, each matched to a discriminating readout | A generic "more controls are needed" |
| Quantitative reasoning | Background, recovery and viable-cell corrections in the right order, with units, rounding and stated uncertainty limits | Pooled percentages, or a missing denominator |
| Inference and limits | RNA, protein, signaling, marker and function claims kept separate; cell loss and missing joint states stated | A marker change called a functional or clinical gain |
| Follow-up design | A factorial comparison with matched accessible ligand, measured material properties, independent cultures, controls and separate marker and function readouts | A single extra measurement with no comparison |
| Communication | Labelled scales, culture-level points, a complete text alternative and methods another learner could follow | A figure whose numbers appear nowhere in text |

More than one design is defensible. The aim is to state what your measurements can and cannot resolve.

## Accessibility

Every number and assumption needed for the project is available in text and tables. No step depends on color, an image without a text equivalent, or a mouse-only action. Your own figure should have a text alternative that states the comparison, the pattern and its limits.

## Limits and provenance

This is an original, optional exercise on constructed data. It is not a laboratory protocol, a measured result or evidence about any real cell type, material, pathway or treatment. No reviewer has piloted the project, the milestone weeks and lengths are unvalidated author estimates, and nothing here forms part of a course grade. The project tables come from a published deterministic generator, `assessment-specs/generate_project_dataset.py`, which contains no grading keys. This guide and the rehearsal dataset are original CC BY 4.0 content; no outside text, question, dataset or figure is reproduced or adapted.
