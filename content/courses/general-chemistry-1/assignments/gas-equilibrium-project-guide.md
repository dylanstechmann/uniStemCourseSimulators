# Gas-equilibrium ledger project guide (optional, ungraded)

**Status:** open, optional practice. You can save milestone responses privately in the Case studio; this route is ungraded.
**Introduced in:** course package 0.5.0.
**Suggested time (unvalidated author estimate):** 2–4 hours across weeks 10–14.

## Start here

The equilibrium problem is not finished when a quadratic produces a number. This project joins four independent checks: species inventories define a domain, the reaction quotient selects a direction, mass action selects an equilibrium state, and the conserved-unit ledger tests the result. An enthalpy calculation then requires an explicit extent basis and a separate boundary before it can be called heat. The tokens deliberately isolate those foundations from real compound identity or procedures.

Work through the supplied project after the related course readings. First close the model or evidence ledger on paper, then use the separate rehearsal to test your method. The worked example uses different inputs and is a demonstration of the reasoning, not a response to the project. Keep definitions, units, denominators, signs and assumptions visible in your own response. If a check fails, return to the model rather than adjusting a number to match an option.

## Project brief and supplied information

Use fictional stoichiometric tokens A(g) ⇌ 2B(g), where each A carries two conserved units and each B one. Initially n_A = 1.00 mol and n_B = 0.500 mol. Define extent ξ in mol so n_A = 1.00−ξ and n_B = 0.500+2ξ. Both species must stay nonnegative; the full inventory domain is −0.250≤ξ≤1.00 mol. Negative extent is not intrinsically forbidden: here it would consume some initial B. The initial quotient determines whether the actual net tendency is forward or reverse.

For this abstract case, activities are defined as a_i = beta n_i with beta = 0.200 mol⁻¹, and the dimensionless constant is K = a_B²/a_A = 1.80 at the fixed temperature. Beta is a stipulated normalization, not a real vessel model. Use reaction enthalpy +20.0 kJ/mol of extent and report ΔH_total = ξΔH. For a **separate stipulated heat ledger**, assume constant pressure and only pressure-volume work so q = ΔH_total, positive into the system. Fixed temperature alone would not establish that equality, and the abstract beta model does not identify a physical path. No real compound, vessel, rate law or operating condition is specified.

## Milestones and self-review

### Milestone 1: Extent domain and conservation

For the project’s initial 1.00 mol A and 0.500 mol B, write the extent table and the complete inventory-feasible interval, including reverse extent. Verify that 2n_A+n_B is conserved. Explain why a forward direction must be inferred separately from Q versus K.

- Derives both bounds from species nonnegativity.
- Uses the 1:2 stoichiometry consistently rather than conserving total molecule count.
- Distinguishes an inventory-feasible domain from the subsequently selected direction.

### Milestone 2: Activities and the initial quotient

Compute the project’s initial quotient with beta = 0.200 mol⁻¹ and compare it with K = 1.80. Show the activity units explicitly and keep the same convention throughout the equilibrium calculation.

- Includes the remaining beta factor after simplifying the quotient.
- Uses the initial composition to compute Q before solving equilibrium.
- Does not confuse a dimensionless activity convention with an unnormalized concentration quotient.

### Milestone 3: Admissible equilibrium solution

Substitute the project extent table into K = beta n_B²/n_A, solve the resulting quadratic, and evaluate both roots against the feasible domain. Report equilibrium amounts with intermediate precision retained.

- Shows the quadratic and both roots with their units.
- Rejects a root by its species inventories rather than by sign alone.
- Substitutes the accepted root into the original quotient.

### Milestone 4: Energy ledger and boundary conditions

Use the project’s +20.0 kJ/mol-of-extent enthalpy to calculate ΔH_total. For the separately stipulated constant-pressure, pressure-volume-work-only heat ledger, state the sign of q. Explain why the artificial activity model does not itself specify a real vessel or heat-transfer path.

- Multiplies by moles of extent rather than moles of arbitrarily chosen species.
- Keeps heat into the system positive and reports kJ consistently.
- Names the extra boundary needed before equating heat with enthalpy change.

### Milestone 5: Perturbation and inference limits

Assemble the extent, activity, conservation and enthalpy ledgers in one report. Add a hypothetical composition perturbation with temperature and beta held fixed, then state which direction follows and which rate, identity and physical-process claims remain unsupported.

- Keeps Q responsive to composition while holding the stipulated K and convention fixed.
- Includes a conservation or reverse-substitution check independent of the quadratic solver.
- Separates a model equilibrium result from kinetics, identity and chemical handling.

## Worked example: a separate case

Take different initial amounts A = 1.50 mol and B = 0, beta = 0.500 mol⁻¹ and K = 1. The extent domain follows from 1.50−ξ≥0 and 2ξ≥0: 0≤ξ≤1.50 mol. Initial Q is zero, so the model tends forward. Substituting the table gives 1 = 0.500(2ξ)²/(1.50−ξ), or 2ξ²+ξ−1.50 = 0.

The roots are (−1±√13)/4 mol. The positive root is 0.65138782 mol and the negative root is outside the domain because it would make B negative. The accepted amounts are A = 0.84861218 mol and B = 1.30277564 mol. Verify 2n_A+n_B = 3.000000 mol of conserved units. Total species moles change, which is permitted: the conserved quantity is the declared unit count, not n_A+n_B.

An independent check evaluates beta n_B²/n_A using those final amounts and recovers 1. A numerical solver should also search only the interval where the original quotient exists; the A = 0 endpoint is an inventory boundary but makes this quotient singular. Substituting an inadmissible root into a multiplied-out polynomial does not repair a negative amount.

For an enthalpy of +12.0 kJ/mol of extent, ΔH_total = 7.8166538 kJ. Under a separately stated constant-pressure boundary with no non-pressure-volume work, the heat into the system equals that positive enthalpy change. The sign describes an energy ledger, not an assertion that the artificial activity normalization corresponds to a real pressure-controlled vessel. Without that boundary, report the enthalpy change and leave heat unresolved.

Finally, doubling all reaction coefficients would square the equilibrium constant under the same activity convention and change the extent basis. The composition cannot be recomputed consistently by changing coefficients while retaining an incompatible constant or molar enthalpy. This check links bookkeeping to the reaction definition rather than treating K and ΔH as labels that can be moved between equations.

## Rehearsal: practice before the project

The [rehearsal input table](gas-equilibrium-rehearsal.csv) supplies A = 2.00 mol, B = 0, beta = 0.250 mol⁻¹ and K = 1.00 for the same written relation A ⇌ 2B. The reaction enthalpy is −8.00 kJ/mol of extent. Determine the domain, initial activities, direction, both quadratic roots, equilibrium amounts, conservation and enthalpy change. Then remove half the equilibrium B while holding beta and temperature fixed, and compute the immediate quotient before further reaction. These inputs differ from both the project and worked example.

Open **Practice gradebook** and choose **Gas-equilibrium ledger rehearsal**. Each numeric field names its reporting unit. Enter continuous quantities as bare numbers to three significant figures, using scientific notation when trailing zeros would otherwise hide the intended precision; enter exact counts as whole numbers. Keep extra digits in intermediate calculations. Interpretation choices test the declared model and evidence limits; a correct choice does not demonstrate a complete written argument. The public feedback explains each field and permits unlimited retries.

## Finish and check your report

Include the supplied inputs, your equations or evidence map, intermediate quantities with units, a final table with clearly labelled rows and a short interpretation. For every numerical result, include a second check: substitute into the original relation, verify a conservation balance, compare a limiting case or independently recompute it. For evidence interpretations, name the comparison, design, endpoint, uncertainty and the conclusion that remains unsupported. A diagram or plot needs a plain-text description that preserves its scientific meaning; colour alone must not carry a distinction.

Use the Case studio checklist only after finding the corresponding evidence in your response. Marking a box records your own review; it does not score prose, certify mastery or establish an institutional grade. Disclose spreadsheets, code, references and AI assistance so another reader can distinguish your reasoning from external calculations. Keep a copy of your report and review any discrepancy between your calculation and the public rehearsal feedback before moving on.

| Stage | Focus | Where to work |
| --- | --- | --- |
| Rehearsal | Separate synthetic inputs and public feedback | Practice gradebook: Gas-equilibrium ledger rehearsal |
| M1 | Extent domain and conservation | Case studio: project milestone 1 |
| M2 | Activities and the initial quotient | Case studio: project milestone 2 |
| M3 | Admissible equilibrium solution | Case studio: project milestone 3 |
| M4 | Energy ledger and boundary conditions | Case studio: project milestone 4 |
| M5 | Perturbation and inference limits | Case studio: project milestone 5 |

## Scope and provenance

Scope comparator: MIT OCW 5.111SC Principles of Chemical Science, Fall 2014 syllabus, https://ocw.mit.edu/courses/5-111sc-principles-of-chemical-science-fall-2014/pages/syllabus/. The local energy and equilibrium readings cover selected Unit III ideas, and this project integrates stoichiometric extent, dimensionless activities and energy accounting. Broader coupled equilibria, real activity models and the paired General Chemistry II material remain outside this one exercise; the two local packages divide one comparator sequence.

The original authoring draft remains a separate proposal for future qualified review; this guide supplies an open practice route without activating that draft as a graded assessment. Workload, scientific quality, assessment design and accessibility have not received independent approval. Original guide, synthetic inputs and rehearsal problems: CC BY 4.0, developed with substantial AI assistance as part of this personal hobby and learning project. No third-party prose, exercise, figure or dataset is reproduced.
