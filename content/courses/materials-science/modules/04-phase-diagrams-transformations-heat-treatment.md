# Binary phases, transformations and process–microstructure links

**Status:** Original reading in partial Materials Science 0.1.0; unreviewed and formative-only. All compositions, phases, transformation histories and numerical examples are synthetic fictional constructions. No heat-treatment recipe, thermal cycle or fabrication setting is provided.

## Composition, phases and fields

A binary phase diagram organizes stable phase fields for two components under stated pressure and composition conventions. The horizontal coordinate may use weight percent, atomic percent or another declared measure. These conventions are not interchangeable without conversion. Temperature is commonly shown on the vertical coordinate, but this reading does not supply any processing schedule; the coordinate is used only to locate equilibrium states in fictional diagrams.

A phase is a region with a characteristic structure and composition description, not simply a region with a different color in a sketch. A single-phase field identifies one stable phase under the model. A two-phase field identifies two coexisting phases connected by a tie line at the chosen state. Boundary lines such as liquidus and solidus delimit particular fields in simple diagrams, while eutectic or peritectic features involve invariant reactions with their own compositions and geometry.

The overall composition C₀ is the bulk composition of the hypothetical system. Cα and CL are the α and liquid compositions at the ends of a tie line. These need not equal C₀. In a two-phase field, different overall compositions at the same temperature can have the same end-phase compositions but different relative phase amounts. That distinction is central to reading a diagram correctly.

Equilibrium diagrams do not show time. A field can identify stable phases without saying how quickly they form, what morphology they adopt or whether equilibrium is reached. A microstructure obtained along a real path may be metastable or incomplete. Kinetic and thermal-history evidence must therefore be kept separate from equilibrium phase reading.

## Lever rule and conservation

Within a two-phase field, the lever rule gives relative phase amounts from mass or mole balance appropriate to the composition convention. For overall C₀ between Cα and CL, the liquid fraction is (C₀ − Cα)/(CL − Cα), and the α fraction is (CL − C₀)/(CL − Cα). Each fraction uses the tie-line arm opposite the phase being calculated. Their sum is one.

For fictional C₀ = 40, Cα = 20 and CL = 60 in consistent units, the liquid fraction is (40 − 20)/(60 − 20) = 0.50, or **50% liquid**. The α fraction is also 50%. If instead C₀ = 30 with the same end compositions, the α fraction is (60 − 30)/(60 − 20) = 0.75, or **75% α**, leaving 25% liquid. A quick mass-balance check is C₀ = fαCα + fLCL: 0.75×20 + 0.25×60 = 30.

Using the nearer arm rather than the opposite arm is a common error. Another is mixing atomic percentages for one composition with weight percentages for another. Values outside the two-phase interval cannot produce physical fractions between zero and one; such a result indicates that the chosen field or compositions are inconsistent.

The lever rule calculates phase amounts, not automatically the area fraction of a microconstituent in an image. A lamellar colony can contain two phases, and its total colony fraction is a different descriptor from either phase fraction. Likewise, proeutectic and eutectic microconstituents require path and reaction analysis, not merely one arbitrary tie-line calculation.

## Transformations and microconstituents

A microconstituent is an organized microstructural region with a recognizable formation history or morphology. It may contain multiple phases. Alternating regions in a fictional eutectic-like colony illustrate this distinction: the colony is a microconstituent, while its constituent lamellae can be separate phases. Contrast in an image alone cannot identify either.

Transformations can change phase fractions, composition partitioning, morphology, defect density and residual stress. Solidification, precipitation, recrystallization and solid-state reactions involve different mechanisms. Even when two fictional specimens have the same nominal composition and similar equilibrium end phases, their transformation histories can produce different microconstituent scales and properties.

A compact fictional kinetic model can illustrate transformed fraction without pretending to capture those mechanisms. Let X = 1 − exp(−ktⁿ), with k = 0.020, t = 10 and n = 2 in consistent synthetic units. Then ktⁿ = 2 and X = 1 − e⁻² = **86.4665…% transformed**. The remaining 13.5335…% is untransformed in this model. Neither number determines morphology, grain size or property, and the stipulated k, t and n are not a recipe for a real material.

Avrami-type models require assumptions about nucleation and growth. A fitted exponent does not uniquely identify a mechanism, and extrapolation beyond the observed range is unsafe. Equilibrium lever-rule fractions and kinetic transformed fractions answer different questions and should never be substituted for one another.

## Process–microstructure–property links, without recipes

Heat treatment is a broad term for controlled thermal histories used to alter structure. At a conceptual level, heating and cooling paths can influence which transformations occur, how far they proceed and what microstructure remains. Quenching, aging, annealing and normalizing are labels associated with different history classes, but this package does not teach how to execute them or specify temperatures, durations, cooling media or equipment.

A process–microstructure–property memo should therefore use conditional language. For example: “In the fictional model, the history increases transformed fraction; if that transformation produces the assumed obstacle distribution, strength may change; direct microstructure and property evidence remain required.” This chain exposes assumptions instead of converting a phase diagram into an operational prescription.

Properties cannot be read uniquely from transformed fraction. A highly transformed fictional specimen might differ in strength, ductility, toughness or stability depending on precipitate size, grain structure and defects. Missing evidence stays unknown. Any actual thermal process requires qualified personnel, suitable facilities, material-specific evidence and independent safety and engineering review.

The official [MIT 3.091SC Fall 2010 syllabus](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/syllabus/) includes unary and binary phase stability in a broader chemistry context. The [MIT 3.012 Fall 2005 calendar](https://ocw.mit.edu/courses/3-012-fundamentals-of-materials-science-fall-2005/pages/calendar/) links phase diagrams with free energy, solutions and statistical-thermodynamic ideas. Both are link-only comparators; no diagram, prose, lecture or problem is imported. This route deliberately omits free-energy-curve construction, spinodal/binodal derivation, detailed steel heat treatment and all operational processing instructions.
