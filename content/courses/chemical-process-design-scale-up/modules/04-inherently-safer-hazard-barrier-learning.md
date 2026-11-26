**Status:** Original, explicitly partial advanced university/industry survey material; unreviewed and formative-only. All species, equipment, records, values and organizations are synthetic and fictional. This is a paper design-review exercise, not an operating, fabrication, safety, validation or release instruction.

# Inherently safer design, hazard evidence and barrier learning

## Learning objectives

- Apply inherently safer design and hierarchy-of-controls reasoning before adding protective complexity.
- Build provenance-linked what-if, FMEA, HAZOP and bow-tie records for a synthetic PFD while testing barrier independence and human factors.
- Perform bounded arithmetic without SIL, tolerable-risk or IPL approval claims, and connect MOC, PSSR and incident learning to HOLD decisions.

## Begin by reducing the hazard, not decorating it

Inherently safer design asks whether the fictional route can use less hazardous inventory, milder hazard categories, simpler connections or fewer failure-prone transfers before safeguards are proposed. Minimization, substitution, moderation and simplification are design directions, not labels that prove safety. Reducing one inventory may increase recycle, energy demand or another hazard; alternatives therefore require whole-system comparison. Passive engineered features generally precede active engineered protection, administrative controls and personal protective equipment in the hierarchy, but the selected combination still requires evidence and review.

The synthetic PFD contains feed buffer B-01, generic reactor R-01, separator S-01, recycle connection RC-01 and utility interface U-01. These labels exist only on paper. No real chemical identifier, recipe, startup/shutdown sequence, bypass/isolation method, emergency response or waste-transport instruction is provided. Hazard identity and consequence evidence must come from authoritative, current, application-specific sources outside this exercise. If such evidence is missing, the hazard review is unresolved and the associated design gate remains HOLD.

## Hazard evidence and provenance

Every hazard statement should link to its evidence type: property source, incident record, model, experiment, expert elicitation or assumption. A source’s date, scope, applicability and owner matter. An assumption cannot masquerade as measured compatibility or dispersion evidence. A previous HAZOP is historical input, not proof that the present revision is covered. Evidence gaps are recorded beside the affected node and action, not buried in a general disclaimer.

OSHA 29 CFR 1910.119 is a link-only official reference for process safety information, hazard analysis, mechanical integrity, MOC, pre-startup safety review and incident investigation. Applicability to any real facility is a legal and qualified-review question outside this course. The existing laboratory-safety OSHA record is a prerequisite link only; its historical adaptations in another package are not imported.

## What-if, FMEA and HAZOP on one fictional PFD

A what-if session begins with concise prompts: loss of utility, blocked path, reversed connection, sensor drift, wrong revision or delayed response. Each prompt identifies affected node, initiating condition, consequence hypothesis, existing evidence, proposed action and owner. It avoids turning vague anxiety into unranked action lists.

FMEA starts from a component or function. For sensor SE-01, a fictional drift failure mode may produce an incorrect control response and delayed detection. Severity, occurrence and detection rankings are ordinal conventions. Their product is not a failure probability. For rankings 6, 4 and 3, RPN=6×4×3=72. The number supports a local sorting conversation only; identical products can hide different severity profiles, and uncertainty or missing evidence cannot be averaged away.

HAZOP uses nodes and guide-word reasoning. At R-01, “more,” “less,” “reverse,” “other than” and “no” can structure questions about flow, composition label, thermal state or utility function without supplying real operating conditions. Causes, consequences, safeguards, independence, recommendations and evidence references remain separate columns. HAZOP attendance and expertise are evidence requirements themselves; an agent-generated table is not a qualified study.

## Bow-tie and barrier independence

A bow-tie places a hazardous event between threat pathways and consequence pathways. Preventive barriers sit on the left and mitigation barriers on the right. Each barrier needs a defined function, owner, performance evidence and degradation mechanism. Two lines on a diagram are not independent if they share a sensor, logic solver, actuator, utility, maintenance activity or human action. Barrier audits explicitly search for these common causes.

For a declared independent two-barrier arithmetic example with failure probabilities 0.10 and 0.20, probability that at least one fails is 1−(1−0.10)(1−0.20)=0.28. This is not an approval calculation. Independence is stipulated solely for the algebra, probabilities are fictional and no barrier is thereby qualified as an independent protection layer (IPL). Correlated failures require a different model and may make the simple product or complement invalid.

## LOPA arithmetic and its limits

Layer of protection analysis can organize an initiating event and claimed protective functions for a defined scenario. A fictional multiplication uses initiating frequency 0.20 per year and two declared conditional failure probabilities 0.10 and 0.05: 0.20×0.10×0.05=0.001 per year. This result is only arithmetic. It does not assign a safety integrity level (SIL), define tolerable risk, demonstrate frequency provenance, prove independence or approve any IPL. The scenario must also address enabling conditions, conditional modifiers, human response and common-cause failure without double counting.

Relief, containment and isolation have different role boundaries. Relief may limit a specified pressure challenge within an engineered system; containment limits release to surroundings; isolation changes connectivity or inventory. None is universally preventive or mitigating without scenario analysis. This course supplies no relief sizing, dispersion or explosion design, isolation instructions or equipment duty rating. Missing relief/containment/isolation evidence produces HOLD.

## Human factors, MOC and PSSR

Human-factors review examines displays, workload, alarm salience, procedure usability, maintenance access, communication and organizational incentives. Requiring an operator to diagnose a rare condition under ambiguous alarms is not a robust barrier merely because a response is written down. Competence and rehearsal claims need actual evidence. Administrative controls can degrade through staffing, time pressure and normalization of deviance.

MOC evaluates technical basis and downstream impacts for proposed changes, including apparently small substitutions of seals, sensors, software or acceptance criteria. Pre-startup safety review (PSSR) verifies that required construction/equipment evidence, procedures, training, hazard actions and change records are resolved before a real introduction decision. This course supplies no PSSR authorization. A synthetic checklist can only identify missing evidence; it cannot declare a facility ready.

## Incident learning and continued challenge

Incident learning includes near misses and weak signals. Investigation protects evidence, builds a timeline, examines technical and organizational contributors, and tracks actions to verified effectiveness. “Human error” is not a sufficient root cause. Lessons must reach related equipment and revisions while preserving local context. Recurring findings challenge earlier barrier claims and can reopen a previously completed synthetic review.

A good review ends with named uncertainties and owners rather than a risk-colored reassuring summary. Missing hazard, compatibility, inspection, safety or acceptance evidence is unresolved and never converted to zero or pass. Real readiness requires named qualified process-safety, engineering, operations, inspection, quality and regulatory reviewers using current authoritative standards.

## Common mistakes

- Adding barriers before considering inherent hazard reduction.
- Treating RPN as probability or LOPA output as SIL/tolerable-risk approval.
- Crediting shared-sensor or shared-human barriers as independent.
- Closing MOC, PSSR or incident actions without verification and current design evidence.

## Scope and sources

OSHA 1910.119 and the existing lab-safety source are official link-only references. MIT 10.490 Fall 2006 and 10.491 Spring 2006 provide link-only design/safety/project comparators. No regulation text, HAZOP worksheet, incident detail, standard table or procedure is imported. The PFD, frequencies, probabilities and rankings are synthetic and fictional; arithmetic does not demonstrate safety or authorize operation.
