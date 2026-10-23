# Renal-clearance ledger project guide (optional, ungraded)

**Status:** open, optional practice. You can save milestone responses privately in the Case studio; this route is ungraded.
**Introduced in:** course package 0.5.0.
**Suggested time (unvalidated author estimate):** 2–4 hours across weeks 11–14.

## Start here

A urine concentration is not a mass rate, and a clearance is not a direct label for a transport mechanism. This project connects the renal reading’s quantities in one consistent steady-state ledger. It asks what a reference establishes, how water flow enters excretion, and why a net handling result leaves gross opposing transport unresolved. The project complements the course’s tissue-closure lab rather than repeating its kinetics question.

Work through the supplied project after the related course readings. First close the model or evidence ledger on paper, then use the separate rehearsal to test your method. The worked example uses different inputs and is a demonstration of the reasoning, not a response to the project. Keep definitions, units, denominators, signs and assumptions visible in your own response. If a check fails, return to the model rather than adjusting a number to match an option.

## Project brief and supplied information

The [project ledger data](renal-clearance-ledger.csv) describe a fictional steady state with urine flow 1.0 mL/min for every row. The reference is freely filtered, neither reabsorbed nor secreted. A–C are freely filtered and not metabolized. Plasma and urine concentrations are in mg/mL.

| Substance | Plasma | Urine | Supplied assumption |
| --- | ---: | ---: | --- |
| Reference | 0.25 | 30.0 | Filtration only |
| A | 0.020 | 1.20 | Possible net tubular handling |
| B | 0.002 | 0.24 | Possible net tubular handling |
| C | 0.010 | 1.80 | Possible net tubular handling |
| Glucose | 4.0 | 105.0 | Ideal transport maximum 375 mg/min; ignore splay |

Define clearance C_x = U_x V_dot/P_x, filtered load = GFR×P_x, excretion = U_x V_dot and fractional excretion = excretion/filtered load. Use excretion − filtered load as the **net tubular addition** sign convention: a positive value is net secretion, a negative value is net reabsorption. The distinction concerns a net balance, not the identity or separate rates of transporters. For glucose use excretion = max(GFR×P − Tm,0). The concentration labels and steady-state model are stipulated inputs, not observations from any person.

## Milestones and self-review

### Milestone 1: Reference clearance

Use the project reference marker (plasma 0.25 mg/mL, urine 30.0 mg/mL, flow 1.0 mL/min) to infer model GFR. Write the excretion rate before dividing by plasma concentration, and list the handling assumptions.

- Tracks mg/mL, mL/min and mg/min through the calculation.
- Uses the reference rather than a transported solute as the model filtration standard.
- States freely filtered, steady-state and no net reference transport assumptions.

### Milestone 2: Filtered and excreted ledgers

For project solutes A and B, calculate clearance, filtered load, excretion and fractional excretion using the reference GFR. Show the net rate needed to close each ledger and distinguish zero net transport from proof that no transport occurred.

- Uses the same reference GFR and stated flow for both solutes.
- Reports each mass rate separately before classifying handling.
- Labels fractional excretion as a fraction or percentage consistently.

### Milestone 3: Net secretion and identifiability

For project solute C, compare excreted and filtered mass rates and calculate the net tubular contribution. State which alternative gross secretion/reabsorption pairs would leave the same net result, and which model assumptions are essential.

- Infers the sign of net transport from a mass-rate difference.
- Keeps net secretion distinct from gross transporter-specific flux.
- Identifies freely filtered and no-metabolism assumptions before interpreting clearance.

### Milestone 4: Transport maximum

For the project glucose row (plasma 4.0 mg/mL, urine 105 mg/mL, flow 1.0 mL/min), compare filtered load minus the stipulated 375 mg/min Tm with observed excretion. Explain the sharp-threshold assumption and one reason not to export it to a real person.

- Computes filtered load on the same mass/time basis as Tm.
- Checks predicted excretion against urine concentration times flow.
- States that no splay or nephron heterogeneity is represented.

### Milestone 5: Report a bounded physiological inference

Assemble the complete project ledger, with units, net-transport sign convention and a text description of any diagram. Add an independent conservation check and a short scope note distinguishing this invented steady-state model from a physiological measurement.

- Every row has a named denominator and consistent units.
- The scope note distinguishes model assumptions, observations and inferred net handling.
- No result is presented as a diagnosis, clinical measurement or handling protocol.

## Worked example: a separate case

Take a separate invented reference with plasma concentration 0.10 mg/mL, urine concentration 4.5 mg/mL and urine flow 2.0 mL/min. Its excreted mass rate is 4.5×2.0 = 9.0 mg/min. Dividing by 0.10 mg/mL gives clearance 90 mL/min. Only after applying the stated filtration-only assumption may that clearance stand for the model GFR.

A freely filtered solute has plasma concentration 0.020 mg/mL and urine concentration 0.45 mg/mL at the same flow. Its filtered load is 90×0.020 = 1.8 mg/min, while excretion is 0.45×2.0 = 0.9 mg/min. Thus excretion − filtration = −0.9 mg/min: the **net** transport is reabsorptive. Clearance is 0.9/0.020 = 45 mL/min and fractional excretion is 0.9/1.8 = 0.50. As an independent identity check, clearance/GFR = 45/90 must equal fractional excretion under these assumptions. A hypothetical gross secretion of 0.2 mg/min plus gross reabsorption of 1.1 mg/min would have the same net rate, showing why the ledger cannot identify each opposing flux.

For a third solute using an ideal glucose-like transport maximum, let plasma concentration be 2.0 mg/mL and Tm = 150 mg/min. Filtered load is 180 mg/min, so the model predicts excretion 30 mg/min. At flow 2.0 mL/min that corresponds to urine concentration 15 mg/mL. Multiplying that concentration back by flow must recover the predicted mass rate. The threshold plasma concentration would be 150/90 ≈ 1.67 mg/mL; it is a sharp mathematical threshold, not a universal physiological cutoff.

None of these values estimates kidney function in a real organism. A real interpretation would need evidence about the reference, filtration fraction, steady state, binding, metabolism and measurement conditions. The exercise isolates conservation and inference so those missing elements are visible rather than quietly assumed.

## Rehearsal: practice before the project

Use the [separate rehearsal ledger](renal-clearance-rehearsal.csv). Urine flow is 1.5 mL/min in each row. Plasma/urine concentrations in mg/mL are reference 0.50/24, A 0.040/0.96, B 0.003/0.144, C 0.015/1.08 and glucose 3.0/24. The reference is filtration-only; other solutes are freely filtered and not metabolized. The rehearsal glucose-like Tm is 180 mg/min, with splay omitted. Rebuild the reference GFR, the A–C mass-rate balances and the glucose excretion check before answering the interpretation fields. Use the fractional rather than percent convention when a numeric field asks for fractional excretion.

Open **Practice gradebook** and choose **Renal-clearance ledger rehearsal**. Each numeric field names its reporting unit. Enter continuous quantities as bare numbers to three significant figures, using scientific notation when trailing zeros would otherwise hide the intended precision; enter exact counts as whole numbers. Keep extra digits in intermediate calculations. Interpretation choices test the declared model and evidence limits; a correct choice does not demonstrate a complete written argument. The public feedback explains each field and permits unlimited retries.

## Finish and check your report

Include the supplied inputs, your equations or evidence map, intermediate quantities with units, a final table with clearly labelled rows and a short interpretation. For every numerical result, include a second check: substitute into the original relation, verify a conservation balance, compare a limiting case or independently recompute it. For evidence interpretations, name the comparison, design, endpoint, uncertainty and the conclusion that remains unsupported. A diagram or plot needs a plain-text description that preserves its scientific meaning; colour alone must not carry a distinction.

Use the Case studio checklist only after finding the corresponding evidence in your response. Marking a box records your own review; it does not score prose, certify mastery or establish an institutional grade. Disclose spreadsheets, code, references and AI assistance so another reader can distinguish your reasoning from external calculations. Keep a copy of your report and review any discrepancy between your calculation and the public rehearsal feedback before moving on.

| Stage | Focus | Where to work |
| --- | --- | --- |
| Rehearsal | Separate synthetic inputs and public feedback | Practice gradebook: Renal-clearance ledger rehearsal |
| M1 | Reference clearance | Case studio: project milestone 1 |
| M2 | Filtered and excreted ledgers | Case studio: project milestone 2 |
| M3 | Net secretion and identifiability | Case studio: project milestone 3 |
| M4 | Transport maximum | Case studio: project milestone 4 |
| M5 | Report a bounded physiological inference | Case studio: project milestone 5 |

## Scope and provenance

Scope comparator: MIT OCW HST.542J Quantitative Physiology: Organ Transport Systems, Spring 2004 calendar, https://ocw.mit.edu/courses/hst-542j-quantitative-physiology-organ-transport-systems-spring-2004/pages/calendar/. Lectures 20–23 cover renal physiology before integrative case studies. This project develops selected clearance and conservation reasoning within the local renal lesson; full renal regulation, the comparator’s cardiovascular/respiratory breadth and laboratory work remain beyond this exercise.

The original authoring draft remains a separate proposal for future qualified review; this guide supplies an open practice route without activating that draft as a graded assessment. Workload, scientific quality, assessment design and accessibility have not received independent approval. Original guide, synthetic inputs and rehearsal problems: CC BY 4.0, developed with substantial AI assistance as part of this personal hobby and learning project. No third-party prose, exercise, figure or dataset is reproduced.
