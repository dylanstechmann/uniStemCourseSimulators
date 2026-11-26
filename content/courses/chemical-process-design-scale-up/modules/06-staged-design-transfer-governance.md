**Status:** Original, explicitly partial advanced university/industry survey material; unreviewed and formative-only. All species, equipment, records, values and organizations are synthetic and fictional. This is a paper design-review exercise, not an operating, fabrication, safety, validation or release instruction.

# G0–G7 design-transfer and evidence governance

## Learning objectives

- Apply G0–G7 gates to design basis, model verification, scale and equipment evidence, safety/MOC, measurement/control, pilot readiness and transfer/continued verification.
- Distinguish arithmetic model checks from engineering validation and assign responsible human roles without manufacturing sign-offs.
- Recompute gate, residual and CAPA evidence while enforcing HOLD for every missing, open or unauthorized requirement.

## Gates are evidence contracts, not ceremonial dates

The fictional G0–G7 ladder structures a design-transfer review. It does not reproduce a company standard or authorize release. Every gate has an evidence contract, named responsible role, unresolved-state behavior and downstream impact. Evidence must refer to the current design-basis and model revisions. A signed meeting invitation is not technical acceptance, and a complete-looking template does not make evidence valid.

G0 is **design basis**: requirements, roles, BFD/PFD, stream table, lifecycle boundary and controlled revisions. Responsible roles include process engineering, operations and project leadership, with independent quality/safety challenge where required. G1 is **model verification**: equations, units, solver convergence, independent balances, domain tests and residual review. Verification asks whether the implemented model solves the declared equations correctly; validation asks whether those equations represent reality adequately. This package can practice the former only in synthetic form.

G2 is **scale evidence**: similarity choices, unmatched groups, scale-down hypotheses, DOE unit structure, uncertainty and pilot comparisons. Reaction/transport and scale-review specialists must decide whether evidence supports a particular transfer hypothesis. G3 is **equipment evidence**: datasheets, conceptual load paths, all-wetted-component compatibility, traveler/joint traceability, inspection/NDE records, nonconformance and repair/rerating/MOC. Mechanical, materials, fabrication and authorized inspection roles are essential.

G4 is **safety and MOC**: inherent-safety alternatives, hazard provenance, HAZOP/FMEA/bow-tie actions, barrier independence, relief/containment/isolation role evidence, MOC and PSSR requirements. Only qualified process-safety and operations reviewers can resolve a real gate. G5 is **measurement and control**: sensors, actuators, FOPDT limits, saturation, alarm/control/interlock separation, PAT inference, calibration and monitoring plans. Instrumentation, control, operations and quality reviewers share defined parts of this evidence.

G6 is **pilot readiness**: authorized evidence package, unresolved-action review, measurement readiness, personnel competency records and safe-work/regulatory approvals required outside the course. This package supplies no pilot run sheet and cannot declare readiness. G7 is **transfer and continued verification**: receiving-site equivalence, transferred models and records, deviations/OOS/OOT, CAPA effectiveness, change history and ongoing monitoring. Quality, regulatory, receiving operations and engineering owners remain active after transfer.

## HOLD is the default for unresolved evidence

Each gate uses only three synthetic learning states: `complete-synthetic`, meaning the fictional record fields are present; `open`, meaning an action or review is not resolved; and `missing`, meaning evidence is absent. `unauthorized` identifies a missing or inappropriate role. None of these labels is a real approval. Any open, missing, stale or unauthorized required item produces **HOLD** and `evidence_gaps_remain`. There is no weighted average across safety, compatibility, inspection or acceptance requirements.

A descriptive coverage ratio may help locate work. Six complete gate packages out of eight gives 6/8×100=75%, but two unresolved gates still prevent even `synthetic_review_complete`. The ratio cannot become zero risk or a conditional pass. When evidence is unavailable, record its absence and impact rather than inventing a zero measurement.

## Residuals and model verification evidence

A synthetic residual vector can support numerical verification review. For residuals [0.2,−0.1,0.1], RMS = sqrt((0.2²+(−0.1)²+0.1²)/3)=0.14142136 model units. This is a descriptive residual statistic against a declared numerical comparison, not an acceptance threshold or validation result. Residuals should be inspected by stream, time and scenario, and convergence criteria must match the equations. Small residuals can coexist with wrong connectivity or physical assumptions.

Independent hand calculations, conservation checks and domain-limit tests provide additional evidence. A model that returns an answer outside its correlation or phase domain is invalid for that scenario even if numerically converged. Verification records identify code/model version, inputs, solver settings, output digest and reviewer. Those software details do not replace engineering review.

## CAPA and continued verification

Deviation, OOS and OOT records feed investigation without predetermined conclusions. CAPA distinguishes containment, correction, corrective action and preventive/system action. Each action has a rationale and effectiveness check tied to the failure mechanism. If eight of ten actions are verified effective, descriptive closure is 80%; the other two remain unresolved and G7 stays HOLD. Reopened or overdue items cannot be counted as verified.

Continued verification monitors whether assumptions remain valid after scale, equipment, material, software or organization changes. Autocorrelated records require appropriate time-series reasoning, and repeated readings do not add independent units. PAT surrogate models need drift and applicability review. No regulated batch disposition, process validation conclusion or commercial release is part of this survey.

## Worked gate walkthrough

A fictional dossier R06 has complete G0–G5 records but an open G6 independent readiness review. Its NPV and model residuals may be reproducible, yet the required state is HOLD. R07 has a named reviewer list but an obsolete equipment revision linked to G3; the gate is unresolved until impact review is complete. R08 has complete transfer documents but two unverified CAPA actions; G7 remains open. R09 contains all fictional fields and named role placeholders and may be labeled `synthetic_review_complete`, a phrase that explicitly denies real readiness or release.

Review order matters. Begin at G0 to establish the basis, then inspect model and scale claims, equipment and safety evidence, measurement/control and pilot readiness before transfer. A later artifact cannot retroactively supply an earlier requirement without revision and re-review. Changes at any gate propagate both backward to the basis and forward to dependent artifacts.

## Responsible humans and source boundaries

Real readiness requires named qualified process, mechanical/materials, control, safety, inspection, quality and regulatory reviewers appropriate to the application, using current authoritative standards. The course author and automated tests cannot fill those roles. MIT design courses, OSHA 1910.119, NIST/SEMATECH, ASME’s public catalog record and FDA’s 2011 guidance are link-only comparators/references, not approvals or compliance checklists.

## Common mistakes

- Calling numerical verification physical validation, or document completeness real readiness.
- Advancing with missing compatibility, inspection, safety or acceptance evidence because other gates score highly.
- Treating CAPA task completion as verified effectiveness or repeated instrument readings as independent campaigns.
- Omitting receiving-site, quality and regulatory owners from transfer governance.

## Scope and sources

The G0–G7 ladder and all dossiers are original synthetic teaching constructions. FDA 2011 supplies link-only lifecycle context; OSHA and NIST supply official public scope references; ASME remains proprietary link-only. No process validation, regulated release, operating qualification or professional sign-off is supplied. Every case remains zero-point self-assessment.
