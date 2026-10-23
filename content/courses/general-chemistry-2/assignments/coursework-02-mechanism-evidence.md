# Assignment 2: a mechanism-evidence and reduction report

Develop a kinetics report using [ligand-exchange discrimination](../modules/ligand-exchange-and-mechanism-discrimination.md), [mechanism inference](../modules/10-rate-laws-and-mechanism-inference.md) and [reversible/sequential kinetics](../modules/11-reversible-and-sequential-kinetics.md). Retain derivations, parameter comparisons, any implementation and interpretation locally. Browser items check selected reduced-model outputs, not your code, experimental competence or a uniquely established mechanism. Species and coefficients are synthetic; this is an evidence-analysis exercise without a chemical-handling procedure.

## A distinct parameter set

Candidate D releases L from ML with kd=0.0006 s^−1. The intermediate M recombines with the fixed free leaving-ligand pool with effective coefficient kr[L]=0.04 s^−1 and is captured by fixed free entering ligand Y with kc=80 L mol^−1 s^−1. Under the stated steady-intermediate/small-pool, low-conversion assumptions, use kobs approximately kd kc[Y]/(kr[L]+kc[Y]). Interpret kobs as initial product rate per approximately unconverted metal total, not a microscopic elementary coefficient.

Candidate A instead has rapid ML+Y ⇌ I equilibrium with KA=2000 L/mol, followed by slow conversion with kturn=0.0006 s^−1. Its unconverted total includes ML and I, and its reduced kobs is kturn KA[Y]/(1+KA[Y]). Free Y is held constant and the fast equilibration assumption must be stated. These are alternative reduced schemes; do not combine their intermediate balances into one mechanism without defining a new network.

## Derive and compare observation equations

Derive each rate expression from its own intermediate equation and total-pool definition. For D, state exactly where steady state and [ML] approximately CT enter. For A, show why including I in CT generates the saturation denominator. Compare their low-Y slopes, high-Y plateaus and half-plateau concentrations. Determine whether the selected parameters give the same reduced curve for every positive Y, not just one tested point.

Evaluate both models at free Y values 0.00025, 0.0005, 0.001 and 0.002 mol/L. Retain an unrounded table and separate the common curve's identifiable parameter combinations from the original microscopic parameters. Explain why four exact points with no noise do not resolve a structural ambiguity. Adding statistical precision to an observation equation cannot create distinctions that the equation itself lacks.

The reading's [reference CSV](ligand-exchange-reference.csv) uses a different worked parameter set. Reconstruct its values with its own coefficients and declared rounding, then generate your assignment table separately. Do not fit the assignment coefficients to that different table and label the resulting mismatch a failed mechanism. Both tables are analytic teaching outputs rather than independent experimental replicates.

## A discriminating comparison

At free Y=0.0005 mol/L, double free L in candidate D, changing kr[L] from 0.04 to 0.08 s^−1 while holding the other declared parameters fixed. Compute the predicted rate before and after. For candidate A, use its stipulated expression without a leaving-ligand effect. Give the contrasting predictions and state which comparison would support or challenge each reduced model if its assumptions held.

List alternative reasons why an observed L effect could differ from these simple predictions, including changed speciation, activity or an additional pathway. Identify an independent measurement or control addressing at least two alternatives. Write predicted contrasting outcomes rather than a list of technique names. No practical procedure or claim about an actual complex is supplied.

## Test the reduction against a full model

For D with fixed reservoirs, write differential equations for ML, M and accumulated product MY. Include every transfer consistently and verify total metal conservation. Choose and state an initial distribution, then integrate the full network or solve its linear system. Compare the early transient with the reduced-rate estimate in a low-conversion window. Quantify the intermediate fraction and relevant time-scale ratio instead of calling the approximation exact because a graph appears close.

For A, supply fast on/off coefficients consistent with KA and compare them with kturn before invoking pre-equilibrium. Explain why KA alone does not specify equilibration time. If full-model curves differ slightly while reduced hyperbolas coincide, distinguish approximation error from observational noise or a logically unique mechanistic assignment. Explore which additional time-resolved endpoint could carry information lost by the reduced model.

## Self-review and completion standard

Both reduced curves have plateau 0.0006 s^−1 and half-plateau Y=0.0005 mol/L. At that Y, kobs is 0.0003 s^−1. Doubling free L in D lowers its prediction to 0.0006×0.04/(0.08+0.04)=0.0002 s^−1, while the stipulated A expression stays at 0.0003. These are distinct predictions only under the stated schemes and reservoir assumptions.

Your report should contain derivations, both tables with provenance/rounding, parameter-identifiability reasoning, a discriminating prediction, a conserved full-network comparison and a limitation audit. Browser feedback does not evaluate the proposed study or prove a real mechanism. This original assignment was developed with substantial AI assistance. [MIT OCW 5.111SC Fall 2014](https://ocw.mit.edu/courses/5-111sc-principles-of-chemical-science-fall-2014/pages/syllabus/) and the ligand-substitution strand in [5.112 Fall 2005](https://ocw.mit.edu/courses/5-112-principles-of-chemical-science-fall-2005/pages/calendar/) are link-only scope references; no source problem, code or data was imported. The course remains partial and unreviewed; actual workload and qualified chemical review remain open.
