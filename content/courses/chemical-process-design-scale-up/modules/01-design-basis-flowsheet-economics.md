**Status:** Original, explicitly partial advanced university/industry survey material; unreviewed and formative-only. All species, equipment, records, values and organizations are synthetic and fictional. This is a paper design-review exercise, not an operating, fabrication, safety, validation or release instruction.

# Design basis, flowsheets, integration and decision economics

## Learning objectives

- Translate requirements and role accountabilities into a design basis, BFD/PFD and stream-table evidence chain.
- Recompute bounded integration and economic/lifecycle scenarios while preserving convergence and equipment-rating boundaries.
- Compare multiobjective alternatives without allowing a preferred score to erase a missing requirement or unresolved review.

## Start with a design basis, not a drawing

A design basis records the question before a flowsheet supplies an answer. For the fictional generic process in this package, the basis names the desired product-service function, feed and product stream definitions on a mass-accounting basis, operating envelope categories without plant targets, required evidence, lifecycle boundaries and decision owners. It distinguishes fixed requirements from preferences and assumptions. Process engineering owns model coherence; operations reviews operability; mechanical and materials reviewers own containment and compatibility evidence; instrumentation and control reviewers own measurement and actuation claims; safety, quality and regulatory reviewers retain independent challenge and disposition roles. A project manager coordinates but cannot absorb those accountabilities.

Requirements need acceptance evidence, not adjectives. “Robust” becomes a list of disturbances, measurements and review questions. “Scaleable” becomes phenomena that must remain in a declared similarity regime and evidence that must transfer. “Low emissions” becomes a boundary, inventory and functional unit. If a required input or reviewer is absent, its state is **unresolved**, never zero, pass or silently waived. The design-basis revision is therefore a controlled record: changes identify their technical reason, affected downstream artifacts and required human re-review.

## BFD, PFD and stream tables answer different questions

A block flow diagram (BFD) groups the synthetic route into feed preparation, reaction, separation, recycle and utility blocks. It supports scope and responsibility discussions but suppresses detail. A process flow diagram (PFD) adds named generic equipment, stream identifiers, major connectivity and selected design-basis information. Neither is a fabrication drawing, pressure-containment design, controller configuration or safe-work procedure. A stream table carries the same stream IDs as the PFD and records the basis, total and component flows, state-model references, data provenance and uncertainty. Generic species A, B and S are accounting labels, not substances with inferred properties.

Every stream should be traceable in both directions: table row to diagram connection and diagram connection to source or calculation. A converged simulator report does not repair an inconsistent label or an unsupported property model. Missing fields stay blank or “unknown” in an authoring table and trigger an evidence gap; they are not replaced by zero. When an equipment datasheet references a stream, the reference identifies the revision used. Later changes require impact review rather than manual edits to one convenient artifact.

## Convergence, rating and utility boundaries

Flowsheet convergence is a numerical property of declared equations and solver settings. Material closure, residual tolerances, recycle tear convergence and physical-domain checks are separate diagnostics. A recycle may converge to a nonphysical root, a local solution or a model whose assumptions fail outside the observed region. Independent hand balances around each block and the overall process provide useful checks. Sensitivity analysis then varies uncertain inputs within a stated scenario range; it does not prove robustness or validate the model.

An equipment rating boundary separates performance-model outputs from an actual duty specification. A calculated heat-removal term or mixing trend is not an exchanger, vessel, agitator, pump or separator rating. Detailed duty, mechanical containment, materials, fabrication and inspection require named qualified reviewers and current authoritative standards. This course intentionally supplies no equipment duty rating or procurement decision.

Utilities are modeled as services with demands, availability, quality attributes and evidence owners. Heat integration begins with declared source and sink terms. For a fictional source, 120 kW-capacity-equivalent multiplied by a 4 availability factor gives 480 kW of available model duty; a sink term is 90×5=450 kW. The bounded recoverable term is min(480,450)=450 kW. This arithmetic does not establish temperature feasibility, exchanger area, hydraulic behavior or operability. Heat–water integration similarly reconciles energy and generic water-utility demands, recovery potential, quality constraints and storage interactions rather than maximizing recovery at any cost.

## Capital, operating scenarios and NPV uncertainty

A comparison states whether capital is a screening allowance, a quoted value or an actual commitment; here it is always a synthetic allowance. Annual operating scenarios separate fixed and variable terms and identify downtime, yield and utility assumptions. Discounted cash flow uses a declared rate and horizon. With initial investment 1,000 cost units, annual net cash 300, rate 0.08 and four years,

NPV = −1000 + 300[1−(1.08)^−4]/0.08 = −6.36194799 cost units.

The result is not a business case. Taxes, financing, working capital, construction schedule, residual value, price escalation and correlated uncertainties are deliberately absent. A second scenario can change one assumption at a time, but one-at-a-time sensitivity misses interactions. Scenario narratives should preserve joint uncertainties and avoid treating a fan of deterministic NPVs as a probability distribution.

Lifecycle accounting uses a functional unit and explicit boundary. If a synthetic alternative has 120 units of an upstream inventory at 8 emission units each, 300 use-phase units at 0.5 each and a stipulated −40 end-of-life credit, total is 120×8+300×0.5−40=1,070 emission units. The credit is an accounting assumption, not measured recovery. Different boundaries cannot be ranked as if comparable.

## Multiobjective review

Cost, emissions, generic water use, safety evidence, operability and technical maturity are not automatically commensurable. Hard constraints screen first. A low-NPV option with missing compatibility or safety evidence remains on HOLD even if a weighted score is attractive. Within the eligible set, normalized indicators can support discussion if weights, directions and normalization references are shown. Pareto comparisons are often more honest: one option is preferred only when it is no worse on every declared criterion and better on at least one. Uncertainty can reverse rankings, so report sensitive weights and boundary choices.

The owner’s habitat-resource-sandbox and rural-florida-agriculture repositories are link-only application references for resource-ledger and scenario-governance patterns. They are personal hobby and learning projects; no code, scenario, parameter or validation claim is imported. They do not provide chemical-process evidence.

## Common mistakes

- Treating a polished PFD as proof of requirements, safe operation or equipment design.
- Reporting solver convergence without independent balances and model-domain checks.
- Turning heat recovery into a duty rating, or an NPV sensitivity into a probability.
- Ranking options before evidence gates, or treating missing lifecycle and compatibility fields as zero impact.

## Scope and sources

The official MIT 10.490 Fall 2006 and 10.491 Spring 2006 pages are link-only comparators for design projects, simulation, economics, safety and team review. The requested 10.490 Fall 2005 page returned HTTP 404 and is not cited as an existing edition. NIST/SEMATECH is a link-only monitoring reference used later. No source prose, figure, table, problem, dataset, code or operating instruction is imported. Arithmetic closure is not proof of safe or feasible operation; real design requires named qualified engineering, operations, safety, quality and regulatory review against current authoritative standards.
