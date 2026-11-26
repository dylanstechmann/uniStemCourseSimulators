# Datums, GD&T concepts, fits and tolerance-stack evidence

**Status:** Original reading in partial Materials Engineering for Fabrication 0.1.0; unreviewed and formative-only. All dimensions and assemblies are fictional and synthetic. This lesson introduces concepts without reproducing a standard, supplying a compliance checklist or declaring any real drawing conforming. Production release and standards review remain outside scope.

## Learning objectives

1. Explain datums, GD&T concepts and fits as functional geometric communication.
2. Calculate worst-case and independent RSS stacks separately with explicit assumptions.
3. Relate tolerances to assembly, inspection and measurement consequences.

## Datums connect function to measurement

A datum reference frame establishes an ordered geometric reference for relating features. It is not merely a convenient surface chosen after inspection. Functional assembly interfaces often guide datum selection because the same reference logic can then support design, process planning and measurement. Datum order matters: constraining degrees of freedom in a different sequence can change the measured relationship. Simulated datums in inspection also have physical imperfections and fixturing effects that require review.

Geometric dimensioning and tolerancing communicates constraints such as form, orientation, location, profile and runout through a defined language. This course does not teach standard-specific symbol compliance. Instead, it emphasizes that size alone does not control every geometric attribute. A hole can satisfy a diameter measurement while its axis is poorly located for assembly. A surface can meet a thickness requirement while excessive form variation prevents sealing. The drawing review must ask which functional variation each control addresses and whether the inspection method evaluates the same attribute.

## Fits and limiting dimensions

Clearance and interference are determined at limits, not only at nominal dimensions. If the smallest hole is 10.20 mm and the largest shaft is 10.10 mm, worst-case minimum clearance is 0.10 mm. If another fictional fit has largest shaft 10.16 mm and smallest hole 10.00 mm, maximum interference is 0.16 mm. The algebraic sign and terminology must be stated. Mixing maximum material and least material limits can produce an optimistic but meaningless result.

A fit calculation does not prove assembly. Form error, orientation, surface condition, thermal expansion, coatings, deformation and measurement uncertainty may matter. Nor does a nominal clearance guarantee every manufactured pair will assemble. Limit analysis should be connected to the actual drawing definition and inspection evidence rather than treated as an isolated arithmetic exercise.

## Worst-case stacks protect declared extremes

A worst-case tolerance stack sums absolute contributions in the unfavorable direction. If three independent-looking dimensions have bilateral tolerance magnitudes 0.02, 0.03 and 0.04 mm, the worst-case stack magnitude is 0.09 mm. This approach answers whether the declared extremes still satisfy the requirement, provided the stack directions and feature relationships are modeled correctly. It does not require statistical independence for its extreme-bound logic, but it does require a correct physical model and valid tolerances.

Worst-case analysis can be conservative for high-volume random assembly because simultaneous extremes may be rare. That observation is not permission to replace it with a statistical method without evidence. For safety- or function-critical interfaces, conservatism may be intentional. The review should record why a statistical model is acceptable and who authorized its use.

## RSS requires declared independence

Root-sum-square stacking models the standard uncertainty of a sum when contributions are independent and their values represent compatible standard-deviation-like terms. For 0.02, 0.03 and 0.04 mm, RSS = √(0.02²+0.03²+0.04²) = 0.05385165… mm. The difference between the worst-case 0.09 mm and this RSS value is 0.03614835… mm. These are different quantities, not competing versions of the same guaranteed limit.

Independence must be declared and justified. Dimensions produced by shared tooling, common thermal drift, sequential operations or correlated fixture error may not be independent. Repeated readings on one gauge are certainly not independent parts or independent geometric contributions. If covariance is known, the more general variance sum includes covariance terms; if it is unknown, do not silently set it to zero. RSS also needs distributional and tail interpretations before being used for yield claims. The arithmetic alone supplies no confidence level or acceptable defect rate.

## Assembly and inspection consequences

Tolerance decisions move through the entire evidence chain. A tight stack can require different datum choices, process routes, assembly sequencing or selective measurement, but this course does not prescribe those settings. Inspection must resolve the relevant characteristic with known bias and adequate measurement-system discrimination. A digital readout with many digits does not establish low uncertainty. Repeated inspection of the same part improves knowledge of that reading process only; it does not expand the lot sample.

A tolerance review should include the stack diagram in words or an original sketch, nominal direction, limits, independence statement, measurement method, uncertainty concerns and unresolved standards/engineering review. It should also identify who evaluates changes. Tightening one feature to improve a stack can shift cost, yield and measurement burden elsewhere. A passing synthetic stack is not drawing approval or production release.

## Common mistakes

Do not treat a datum as an arbitrary label, use nominal dimensions for a worst-case fit, confuse clearance with interference, or call RSS “statistical worst case.” Do not apply RSS when independence is undeclared, pool correlated features, or quote a yield probability from an unverified distribution. Never treat Cp/Cpk or a high-resolution display as proof that a geometric requirement is correctly defined.

## Scope and sources

[MIT 2.008 Spring 2025](https://ocw.mit.edu/courses/2-008-design-and-manufacturing-ii-spring-2025/pages/calendar/) links assembly/disassembly, design review, quality and measurement in a much broader manufacturing sequence. Existing statistics records support variance and independence concepts. The local treatment is original and selective; it imports no standard, drawing, symbol table, exercise or dataset. Formal GD&T standards training, qualified drawing review and actual metrology remain required outside this partial, unreviewed survey.
