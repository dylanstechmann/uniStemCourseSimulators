# Renal clearance ledger (inactive draft)

**Status: authoring draft only.** This fictional, ungraded paper exercise is not an assessment used by the course platform. All measurements are synthetic. The task is a mass-balance exercise, not a clinical test, diagnosis or treatment recommendation.

## Purpose

Track filtration and tubular handling from one consistent set of synthetic steady-state measurements. This applies the renal-clearance reading in a short integrative report; it does not repeat the scratch-assay closure lab or the compensation-and-reserve case.

## Synthetic dataset

Assume urine flow is 1.0 mL/min for each row. The inulin-like reference is freely filtered and neither reabsorbed nor secreted, so use it to estimate the model's GFR. Solutes A–C are freely filtered and not metabolized; their simplified net handling can be inferred by comparing excretion with filtered load. Glucose follows the lesson's idealized transport-maximum model with Tm = 375 mg/min; ignore splay.

| Substance | Plasma concentration (mg/mL) | Urine concentration (mg/mL) | Model assumption |
|---|---:|---:|---|
| Reference marker | 0.25 | 30.0 | Filtration only |
| Solute A | 0.020 | 1.20 | Freely filtered; possible net tubular transport |
| Solute B | 0.002 | 0.24 | Freely filtered; possible net tubular transport |
| Solute C | 0.010 | 1.80 | Freely filtered; possible net tubular transport |
| Glucose | 4.0 | 105.0 | Freely filtered; idealized Tm = 375 mg/min |

## Learner task

1. Calculate the reference clearance and report the synthetic GFR in mL/min.
2. For A, B and C, calculate clearance, filtered load, urinary excretion and fractional excretion. Use the supplied GFR and the common urine flow.
3. Classify each solute as net reabsorbed, net filtered with no net tubular handling, or net secreted. Show the mass-rate comparison that supports each classification.
4. For glucose, calculate filtered load and excretion, then use the idealized Tm to reconcile why urinary excretion is nonzero. State one limitation of the sharp-threshold model.
5. Write a brief scope note explaining why these invented values cannot estimate anyone's kidney function or support a health decision.

## Author reference calculations

- Reference marker: C = 30.0 × 1.0 / 0.25 = 120 mL/min, so model GFR = 120 mL/min.
- Solute A: clearance = 1.20 × 1.0 / 0.020 = 60 mL/min; filtered load = 120 × 0.020 = 2.40 mg/min; excretion = 1.20 mg/min; net reabsorption = 1.20 mg/min; fractional excretion = 0.50.
- Solute B: clearance = 0.24 × 1.0 / 0.002 = 120 mL/min; filtered load and excretion are both 0.24 mg/min; no net tubular handling in this model; fractional excretion = 1.00.
- Solute C: clearance = 1.80 × 1.0 / 0.010 = 180 mL/min; filtered load = 1.20 mg/min; excretion = 1.80 mg/min; net secretion = 0.60 mg/min; fractional excretion = 1.50.
- Glucose: filtered load = 120 × 4.0 = 480 mg/min; excretion = 105 × 1.0 = 105 mg/min; 480 − 375 = 105 mg/min, matching the idealized Tm prediction.
- All values are invented teaching quantities. The sharp glucose threshold omits nephron-to-nephron variation and splay. These calculations do not constitute a clinical clearance protocol or refer to a real person.

## Inactive-draft boundary

This paper-only proposal has no score, rubric, gradebook mapping, platform activation, required status or effect on course completion. A qualified instructor should review the arithmetic, units, assumptions, accessibility and workload before any future adoption. Course maturity remains partial.
