# Comparative fabrication routes, joining and DFM/DFA process-plan logic

**Status:** Original reading in partial Materials Engineering for Fabrication 0.1.0; unreviewed and formative-only. Every route, part and quantity is fictional and synthetic. This is non-operational design-review instruction: no feeds/speeds, CNC toolpaths, weld parameters, cure schedules, mold settings or machine setups are included.

## Learning objectives

1. Compare fabrication and joining routes using shape, material, volume and evidence constraints.
2. Construct DFM/DFA process-plan logic with reproducible yield and cost arithmetic.
3. Identify inspection, distortion, accessibility and qualification evidence required by a route.

## Compare mechanisms before labels

Machining removes material and can provide accessible geometric control, but tool access, workholding, thin-feature stability, burrs and residual stress require review. Casting creates shape through solidification and can support complex forms, while shrinkage, porosity, draft and subsequent machining affect evidence needs. Forming redirects material through plastic deformation; springback, thinning, texture and residual stress can dominate tolerances. Molding shapes a polymer or composite system and introduces flow, shrinkage, weld-line, cure and fiber-orientation questions. These are comparative mechanisms, not universal rankings.

Additive fabrication builds geometry through localized addition or consolidation. It can consolidate parts and enable internal features, but anisotropy, surface condition, trapped material, support strategy, defect detection and qualification can control feasibility. Powder-sintering routes shape and consolidate powder; compaction, shrinkage, density gradients and porosity require evidence. A complex shape alone does not make additive the best route, just as a high quantity alone does not justify a mold.

Welding creates joints through localized thermal and metallurgical processes. Distortion, residual stress, heat-affected regions, access and inspection are central. Adhesive joining distributes load differently and can join dissimilar materials, but surface condition, bondline control, environmental aging, cure state and inspection create different evidence demands. Mechanical fastening and integral design may alter disassembly and stress concentration. Joining choice belongs in the initial architecture, not after all part geometry is fixed.

## DFM and DFA as connected questions

Design for manufacture asks whether the proposed geometry and material can be produced with controlled evidence at the required volume and lifecycle cost. Design for assembly asks whether parts can be oriented, joined, inspected, serviced and disassembled with acceptable risk. Reducing part count may simplify assembly while making a single geometry harder to fabricate or inspect. Conversely, splitting a part can improve access but add datums, fasteners, sealing surfaces and tolerance stacks.

Use a route matrix with rows for candidate routes and columns for material compatibility, geometric access, feature scale, volume, expected defects, secondary operations, joining, inspection and evidence maturity. Mark unknowns explicitly. Do not assign a total score before eliminating routes that fail mandatory requirements. A prototype route and a production route can differ, so transferring evidence between them requires justification rather than an assumption of equivalence.

## Process-plan logic without settings

A non-operational process plan is an ordered evidence and dependency graph: approved input definition, incoming material identity, shape-forming route, secondary geometry operations, joining, inspection, nonconformance handling and record retention. It names what each stage must accomplish and what evidence passes to the next. It does not prescribe machine parameters. Include reference frames and inspection access early; a late operation can destroy an earlier datum or make a critical surface inaccessible.

Yield multiplication illustrates why route stages interact. With fictional step yields 0.98, 0.95 and 0.90, overall expected yield is 0.8379, or 83.79%, if those probabilities apply to the same unit population under the declared model. Averaging the three percentages would not compute surviving fraction. Correlation and rework can invalidate this simple model. If a final powder-derived batch must contain 100 kg and the declared yield is 0.92, required input is 100/0.92 = 108.69565… kg; multiplying by yield would move in the wrong direction.

Cost crossover arithmetic compares fixed and variable terms, not equipment recommendations. Route A has 15,000 fixed and 5 per part; route B has 5,000 fixed and 8 per part. Equality occurs at (15,000−5,000)/(8−5) = 3,333.333… parts. Below this idealized crossover, B has lower model cost; above it, A does. Quality, delay, lifecycle and uncertainty may dominate the decision and are not captured by the crossover.

## Inspection and qualification implications

Every process family changes what can be measured and when. Internal additive features may be inaccessible to contact inspection; cast and sintered parts may need density or defect evidence; formed parts may need shape/residual-stress review; molded composites may need orientation and cure evidence; welded and adhesive joints need joint-specific inspection and qualification. A dimensional report alone cannot establish internal integrity or service durability.

The process plan should therefore name evidence dependencies alongside operations. It should preserve lot and route identity, define when nonconformance is recorded, and prevent later work from hiding an unresolved discrepancy. Real readiness requires qualified process review, approved drawings/BOM, calibrated inspection/MSA, traceability, closure and authorized release. A plausible route diagram supplies none of those approvals.

## Common mistakes

Do not select a route solely by minimum unit price, maximum nominal throughput or geometric novelty. Do not ignore secondary operations, joining distortion, inspection access or evidence transfer between prototype and production routes. Do not average stage yields, divide by cost when solving for material input, or interpret a cost crossover as a procurement instruction. No route in this survey receives fabrication approval.

## Scope and sources

The [MIT 2.008 Spring 2025 calendar](https://ocw.mit.edu/courses/2-008-design-and-manufacturing-ii-spring-2025/pages/calendar/) spans molding, machining, assembly/joining, forming, casting, additive processes, quality and manufacturing systems; this single reading is deliberately selective and omits its laboratory/CAD/CAM delivery. The owner’s [open-construction-equipment](https://github.com/dylanstechmann/open-construction-equipment) project is linked only as a personal hobby and learning application context. No repository design, parameter, code or validation claim is imported. The package remains partial, unreviewed and non-operational.
