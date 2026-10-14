# Draft physical laboratory candidate: potato catalase kinetics

**Status: instructor and safety review draft only.** This activity is not in the course manifest or learner schedule. It has not been locally risk-assessed, piloted, or reviewed for accessibility. Do not use it with students until the institution's laboratory supervisor and environmental health and safety office approve the exact materials, concentrations, apparatus, waste route, and emergency plan.

This candidate would complement the two synthetic-data virtual labs with one supervised, non-microbial experiment. Students would measure oxygen formation as potato catalase decomposes hydrogen peroxide, then estimate initial rates across a proposed substrate-concentration series. All expected results are to be collected locally; this document contains no experimental observations.

## Learning aims

Students would:

1. collect time-series data from separate replicate reactions and distinguish repeated readings from independent reaction replicates;
2. estimate an initial oxygen-production rate from the early linear part of each time course and compare rates across stated substrate concentrations;
3. compare a saturating model with the observed data while explaining why crude potato extract is not a purified single-enzyme preparation;
4. identify which assay controls, safety controls, and uncertainty measurements are needed before interpreting the result.

## Proposed design for local piloting

Potato extract supplies crude catalase. The proposed substrate series is 0.10%, 0.20%, 0.40%, and 0.80% hydrogen peroxide by mass in the final reaction mixture, plus a substrate-only blank. These are starting points for an instructor pilot, not validated working conditions. The instructor must confirm that the selected potato-extract dilution yields a measurable early linear interval without excessive gas production or rapid substrate depletion, then freeze the exact preparation and concentrations for the class.

Each reaction would use a fixed final volume, the same buffer and recorded room temperature. Students would prepare three independent reaction vessels per substrate level, randomize or interleave the run order to limit extract-aging bias, and include a no-enzyme blank. A common prepared extract batch would be kept cold between runs. The instructor would prepare the extract and all substrate solutions; students would not handle concentrated peroxide or prepare stock dilutions.

For each run, students would connect the reaction vessel to a water-displacement gas collector before starting, add the instructor-prepared enzyme aliquot to the substrate, mix consistently, start a timer, and record collected gas volume at short fixed intervals. The gas path must remain open to the collector throughout; the apparatus must not be clamped shut or used as a pressure vessel. The exact sampling interval and reaction volumes require a bench pilot with the locally available apparatus.

Students would plot gas volume against time, select and justify an early linear interval, and use its slope as the operational initial rate in mL O₂/min. They would compare the blank with enzyme-containing reactions and plot replicate mean rate against the stated initial substrate concentration, displaying individual replicate values. A fitted Michaelis–Menten curve may be explored as a model, but parameters from this crude extract are descriptive assay estimates, not constants for purified catalase or values for a cell or organism.

If converting oxygen evolution to peroxide consumption, use the balanced reaction, 2 H₂O₂ → 2 H₂O + O₂, and state the gas conditions and assumptions. Oxygen dissolves in water, so water-displacement volume is an operational measurement; it should not be presented as an exact molar flux without accounting for gas temperature, pressure, water vapor, and dissolved oxygen.

For this candidate, do not treat collected oxygen alone as a verified substrate-conversion measurement: dissolved oxygen, leaks, and gas-transfer delays can make the collected volume underestimate oxygen produced. If converting a collected-gas amount to a conversion estimate, record temperature and pressure, account for water vapor, and label the result a lower bound unless the local pilot validates corrections for dissolved and uncollected oxygen. An instructor may adopt a proposed starting quality criterion such as less than 10% substrate conversion during the fitted interval only if the pilot uses a validated way to measure remaining peroxide or otherwise validates a conservative correction. This is a local assay-quality proposal, not a universal biochemical standard. Without that validation, select an early linear interval empirically and report its slope as an operational rate; do not claim that substrate depletion was below a stated percentage. A short early interval also does not prove that the enzyme remained stable or that product effects were absent.

## Draft student record

The student worksheet should record the extract batch and dilution, final peroxide concentration, total reaction volume, temperature, blank readings, vessel/run identifier, time points, gas volumes, excluded readings with reasons, and the interval used for each rate estimate. Keep each reaction replicate as its own row. Repeated time points within one vessel are not independent replicates.

The report should include a plot of each time course, the selected initial-rate intervals, a replicate-level rate plot, the blank comparison, the rate-versus-substrate plot, and a short limitations section. Students should distinguish observed oxygen evolution from peroxide disappearance, and measured specific-assay behavior from a claim about physiology. No grade weight or scoring rubric is proposed here.

## Safety and implementation gates

The cited LabChem safety data sheet for its specific 3% w/w laboratory hydrogen peroxide product classifies that product for skin irritation and serious eye damage, and specifies gloves and eye protection. The candidate therefore assumes only instructor-prepared working solutions and no student access to concentrated stock. Those controls do not substitute for reviewing the actual product and its current, concentration-matched safety data sheet. Local EHS must approve the working concentrations, PPE, eyewash access, spill response, storage, and waste handling. Keep the reaction away from flames and ignition sources, and do not release waste to a drain unless the institution authorizes that route.

Before scheduling, an instructor must document a successful pilot that checks the apparatus for leaks and blockage, verifies the blank and time resolution, selects an extract dilution and substrate range, confirms the initial-rate criterion, and records actual preparation time and cleanup. The school must also review potato handling and allergies, accessible alternatives for timing and data recording, accommodation procedures, supervision ratios, reagent labeling, and waste collection. A physical demonstration alone does not document that students can independently perform or interpret the method.

## Reference links

These are link-only background references. The draft is independently written; the linked procedures and figures are not reproduced.

- [Cornell Institute for Biology Teachers: catalase activity with crude potato extract](https://blogs.cornell.edu/cibt/labs-activities/labs/catalase/)
- [MIT OpenCourseWare: undergraduate catalase kinetics laboratory](https://ocw.mit.edu/courses/5-310-laboratory-chemistry-fall-2019/resources/mit5_310f19_lab5/)
- [UW–Madison Demonstration Lab: catalase extract kinetics and listed precautions](https://demolab.chem.wisc.edu/biochemistry-enzyme-kinetics-experiments-with-catalase-extract/)
- [LabChem: Safety Data Sheet for hydrogen peroxide, 3% w/w, product LC15450](https://www.labchem.com/ASSETS/DOCUMENTS/ITEMS/EN/LC15450_SDS.pdf)
- [University of Georgia Environmental Safety Division: use the SDS for the actual product and concentration](https://esd.uga.edu/programs/right-to-know/safety-data-sheets/)

This proposal does not satisfy the course's physical-laboratory completion or safety-review gates until a local instructor has revised and tested it and the responsible institutional reviewers have recorded approval.

The companion [blank instructor pilot log](biochemistry-physical-lab-pilot-log-0.4.79.md) can capture local materials, approvals, observations, workload, and a review decision. It contains no pilot results and is not an authorization for student use.
