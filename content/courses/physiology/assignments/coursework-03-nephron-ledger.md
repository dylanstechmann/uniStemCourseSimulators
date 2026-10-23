# Assignment 3: nephron delivery, concentration and pool balance

Prepare a conserved-quantity report using [nephron segments](../modules/nephron-segments-and-regulated-transport.md), [clearance/tubular handling](../modules/06-renal-clearance-and-tubular-handling.md) and [homeostatic balance](../modules/08-homeostasis-balance-and-feedback-gain.md). Save segment tables, independent checks and interpretation locally. Browser checkpoints assess selected outputs, not the full report, actual renal function or a person's health. All fractions and numerical inputs are invented for this exercise, not reference ranges or measured transport data.

## Supplied serial model

Filtration flow is 90 mL/min and plasma sodium concentration 120 mmol/L. In four successive aggregated stages, sodium reabsorption fractions of delivered load are 0.5, 0.75, 0.8 and 0.9. Water recovery fractions of delivered flow are 0.6, 0.5, zero and 0.9. No sodium secretion, additional input or leak is included. The fractions are independent stipulated parameters; the stages do not reproduce every anatomical nephron process or a complete hormonal perturbation.

Convert filtration to liters per minute before computing filtered sodium amount. Build separate sodium and water tables showing each stage's incoming, removed and outgoing rates. State every denominator. Prove that final retained fractions multiply, while stage removal fractions generally cannot be added because their delivery denominators differ. Verify that removed plus outgoing equals incoming at each stage and that the complete ledger returns the original filtered load and flow.

Calculate final sodium excretion, fractional excretion, urine volume flow and sodium concentration. Recover sodium clearance from excretion/plasma concentration and compare its ratio to filtration with fractional excretion. Explain why clearance, urine volume and amount excretion have different dimensions and meanings even when all are described as renal outputs.

## Perturb water and solute handling separately

Change only final water recovery from 0.9 to 0.5. Recompute flow, concentration and sodium amount excretion. State precisely which outputs change and which are fixed by the selected independent ledgers. Explain how a lower urine sodium concentration can coexist with the same sodium amount loss. This is a mathematical isolation, not a claim that a real ADH perturbation leaves every other renal process unchanged.

Restore the original water fractions and change only final sodium recovery from 0.9 to 0.8. Recompute excretion, fractional excretion and concentration. Compare this with the water-only case and identify which measurements distinguish them. State why a real endocrine interpretation would need evidence on several segment, filtration and osmotic effects rather than using one urine concentration as a unique hormonal readout.

## Connect to a changing body pool

Let body sodium amount be N(t) and water volume W(t), with concentration C=N/W. Derive Cdot=Ndot/W−N Wdot/W². Explain how constant C can coexist with changing N and W, and identify the proportional relationship needed between their changes. Write separate amount and volume input/output balances, retaining other losses if modeled. A steady concentration is not equivalent to zero turnover or unchanged reserve.

Under a hypothetical amount input that exceeds the modeled excretion, determine the sign of Ndot without assigning a diagnosis. Then identify what water balance would be needed to hold C fixed. Conversely, explain why a concentration change alone does not uniquely determine the sign of total sodium change. Keep these qualitative conclusions tied to the stated balance equations and avoid interpreting the toy fractions as actual whole-body control gains.

## Test limits and omitted coupling

Check a no-reabsorption limit and a very small final urine-flow limit. If finite sodium excretion is paired with exactly zero water output, a finite urine concentration cannot be computed. Explain why such an extreme challenges the independently assigned fractions and omitted osmotic/transport constraints rather than defining a real infinite concentration. Mark any computational domain failure explicitly instead of returning a plausible number.

If adding secretion, place a signed amount term at a specific stage and recompute downstream delivery. Show that a reabsorption fraction cannot substitute for a source term without changing its meaning. If modeling water permeability mechanistically, identify the osmotic gradients and properties needed; an ADH label alone does not supply them. The related [feedback assignment](coursework-04-feedback-and-reserve.md) uses a normalized controller, not an inferred human hormone response.

## Self-review and completion evidence

Filtered sodium load is 0.09×120=10.8 mmol/min. Final excretion is 0.027 mmol/min and fractional excretion 0.0025. Urine flow is 1.8 mL/min, so sodium concentration is fifteen mmol/L. Sodium clearance is 0.225 mL/min, and its ratio to 90 mL/min is again 0.0025 under the supplied assumptions.

Changing final water recovery to 0.5 gives nine mL/min and three mmol/L while keeping sodium excretion 0.027 mmol/min. Changing final sodium recovery to 0.8 with original water instead gives excretion 0.054 mmol/min and concentration thirty mmol/L. Reconstruct these from your stage tables rather than using them as inputs. A complete report retains unit/amount/volume ledgers, perturbations, concentration derivatives, limiting cases and model-boundary reasoning.

This original assignment was developed with substantial AI assistance. [MIT OCW HST.542J Organ Transport Systems Spring 2004](https://ocw.mit.edu/courses/hst-542j-quantitative-physiology-organ-transport-systems-spring-2004/pages/calendar/) is a link-only scope comparator; no source problem, table or experimental data was imported. Qualified review and measured workload remain open. The course is partial and unreviewed and supplies no personal health interpretation or treatment target.
