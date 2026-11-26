# Service requirements and constraints-based material/process selection

**Status:** Original reading in partial Materials Engineering for Fabrication 0.1.0; unreviewed and formative-only. This advanced university/industry design-review survey uses fictional components and synthetic values. Fabrication readiness is a review objective, never an achieved claim. No supplier approval, production release, machine settings or standard-specific compliance checklist is provided.

## Learning objectives

1. Translate loads, temperature, media, wear and lifecycle context into explicit hard constraints and evidence needs.
2. Compare cost, throughput and lifecycle trade-offs without allowing weighted scores to erase failed constraints.
3. Document evidence uncertainty, sensitivity and unresolved engineering and safety review.

## Start with function and failure context

A material name or a preferred fabrication route is not a requirement. Begin with the function the fictional component must perform, the interfaces it must maintain and the consequences of failing to perform them. Describe mechanical loads by type, direction, duration, cycling and plausible combinations. Separate a nominal operating narrative from overload, misuse, transport and maintenance narratives. Temperature includes both the surrounding medium and internally generated excursions. Media includes contact fluids, cleaning agents, humidity, particulates and galvanic neighbors. Wear may involve abrasion, adhesion, fretting or erosion; choosing a harder nominal material without identifying the contact pair and debris pathway is an unsupported shortcut.

Convert this narrative into a requirement table with a measurable definition, units, evidence source and confidence. A maximum-temperature field copied from a generic material sheet is not proof that a particular fiber orientation, joint, surface treatment or lot will survive the actual history. Loads require structural review using the prerequisite mechanics courses; this lesson does not duplicate those derivations. The output is a design-review question set, not a service approval. Where loads or media are unknown, write “unknown” and identify the observation or qualified analysis needed rather than substituting an optimistic number.

## Hard constraints before preferences

Hard constraints determine whether a candidate remains in the comparison. Examples include minimum stiffness, a temperature envelope, compatibility evidence, a required joining method, geometric feasibility, inspection access and a lifecycle restriction. A candidate that fails one mandatory condition leaves the eligible set even if its cost is attractive. Soft preferences such as lower mass, reduced embodied energy, shorter lead time or easier disassembly can then be compared among eligible candidates. Keep the two categories visually separate.

A weighted score is useful only after this screen and only with declared weights and scales. Ordinal scores are not automatically physical measurements. A corrosion-evidence score of four does not mean twice the corrosion resistance of two, and a cost index is not a quotation. Sensitivity analysis changes one plausible preference or uncertain input at a time and records whether the preferred candidate changes. It must not silently change a hard constraint to rescue a favorite.

## Cost and throughput as declared models

The public practice uses an annual accounting identity: annual cost = fixed allocation + annual quantity × variable cost per part. With fixed allocation 12,000 and 4,000 parts at 3 cost units each, the synthetic result is 24,000 cost units. This is not a quote; tooling amortization, inventory, quality escapes, maintenance and logistics may require additional terms. State the accounting boundary before comparing two routes.

Throughput requires a bottleneck and a yield definition. If three fictional steps have capacities 80, 60 and 100 units/day, the nominal route limit is 60 units/day before losses. Multiplying by a declared route yield of 0.95 gives 57 good units/day. Choosing 100 because it is the largest capacity ignores the bottleneck. Real scheduling also depends on changeovers, downtime, labor, inspection and shared resources, none of which is inferred from this arithmetic.

Lifecycle accounting similarly needs a boundary. A fictional batch of 500 good parts with material, use-phase and end-of-life terms of 40, 12 and −4 MJ per part has 500×(40+12−4) = 24,000 MJ in the declared model. A negative term is a stipulated credit, not proof of actual recovery. Compare alternatives using consistent system boundaries and service life; a low production footprint can be offset by shorter life or greater use-phase demand.

## Evidence uncertainty and review gates

Every requirement should link to evidence: an approved requirements record, a validated analysis, a qualified test report, a supplier-lot certificate with traceable identity, or an explicitly unresolved item. Datasheet values describe particular conditions and populations. They do not guarantee minimum properties after forming, molding, additive consolidation, welding or adhesive joining. Evidence uncertainty includes property scatter, limited sample size, proxy tests, unknown processing history, model mismatch and conflicting records. Preserve these distinctions rather than collapsing them into one confidence percentage.

A useful selection record contains the function, loads, thermal and media exposure, wear mechanism, lifecycle assumptions, mandatory constraints, eligible candidates, calculations, sensitivity, evidence citations and open gates. Qualified engineering and safety reviewers must assess the actual application. Material and process qualification, inspection/MSA, lot traceability and nonconformance closure remain downstream evidence obligations. The review can conclude that a fictional comparison is internally complete while still stating that real fabrication readiness has not been established.

## Common mistakes

Do not begin with a material ranking and invent requirements afterward. Do not treat room-temperature static strength as evidence for cyclic, hot or chemically exposed performance. Do not confuse throughput with good throughput, fixed cost with total lifecycle cost, or an ordinal score with a measurement. Do not hide missing fatigue, wear, joining or inspection evidence behind a weighted total. Finally, do not turn a synthetic winner into supplier approval or production release.

## Scope and sources

The official [MIT 2.008 Design and Manufacturing II Spring 2025 calendar](https://ocw.mit.edu/courses/2-008-design-and-manufacturing-ii-spring-2025/pages/calendar/) provides a broader manufacturing, cost, quality and systems comparator. [MIT 3.032 Mechanical Behavior of Materials Fall 2007 syllabus](https://ocw.mit.edu/courses/3-032-mechanical-behavior-of-materials-fall-2007/pages/syllabus/) and the existing mechanics/materials records support mechanical-behavior prerequisites. The owner’s [open-construction-equipment](https://github.com/dylanstechmann/open-construction-equipment) repository is a personal hobby and learning project linked only for application context; no CAD, calculations, code or readiness claims are imported. All sources are link-only, and the package remains partial and unreviewed.
