# Process–structure–property relationships, defects and property scatter

**Status:** Original reading in partial Materials Engineering for Fabrication 0.1.0; unreviewed and formative-only. All materials and values are fictional and synthetic. Heat treatment and cure are discussed conceptually, without recipes or schedules. No fabrication setting, material qualification or production approval is supplied.

## Learning objectives

1. Connect processing history to structure, defects and conditional property hypotheses.
2. Recompute property-change, residual-stress and idealized porosity examples with explicit assumptions.
3. Explain property scatter and sampling consequences without treating nominal values as qualified lot distributions.

## Processing leaves a structural record

Fabrication changes more than external shape. Thermal and mechanical histories alter phase fractions, grain size, texture, dislocation density, residual stress, interfaces and defect populations. In polymers, molecular mobility, crystallinity and network development depend on processing history. In fiber composites, fiber orientation and interface quality create direction-dependent response. A drawing that specifies only geometry and a generic material label may therefore leave important performance variables uncontrolled.

This relationship is conditional rather than a slogan that predicts exact properties. Heat treatment can change transformation products and precipitation states, but an equilibrium diagram does not specify a usable thermal cycle. Forming can induce texture and work hardening while also producing local thinning or damage. Residual stress arises when incompatible elastic strain remains after processing or assembly; its sign and spatial distribution matter. Porosity reduces effective load-bearing area and can concentrate stress, but size, shape and location prevent one universal strength correction. Cure describes network evolution rather than a single universal material state. These are review hypotheses requiring structure and property evidence.

## Defects are populations, not decorative labels

A defect review should identify type, scale, location, orientation, detection method and consequence. A pore near a highly stressed surface is not interchangeable with a small isolated internal pore. Lack-of-fusion in an additive or welded region differs from a spherical gas pore. Fiber waviness can redirect load, and an incompletely developed polymer network can change stiffness, damping and environmental response. Inspection resolution and probability of detection limit what “no defect observed” means.

Synthetic practice uses a deliberately simple square-law porosity model: strength = nominal strength × (1−p)². For nominal 250 MPa and p = 0.04, the result is 230.4 MPa. The equation is a teaching model, not a materials law or acceptance criterion. It cannot replace fractography, defect statistics, mechanics review or qualification. A different defect morphology would require a different model. Always name the model before quoting the number.

## Residual stress and signed superposition

For a bounded uniaxial illustration, applied stress and residual stress can be added algebraically when the same location, direction and sign convention are stipulated. Applied 120 MPa plus residual −45 MPa gives 75 MPa. Subtracting 45 again would confuse a compressive residual contribution with its magnitude. Real components contain spatial gradients and multiaxial states, and processing or service can relax the residual field. The synthetic sum does not predict yielding, fatigue life or fitness for service.

Property-change percentages require a baseline. A fictional mean increasing from 200 to 230 arbitrary strength units changes by (230−200)/200×100 = 15%. Saying the new mean is 115% of the old mean is also true but answers a different question. Keep mean shift separate from variance, skew, tails and batch-to-batch structure. An increased mean can coexist with an unacceptable lower tail.

## Scatter, lots and evidence design

Nominal properties are not distributions. A defensible review asks which specimens were independent, which lots and process conditions they represent, how orientation and location were sampled, and whether measurement uncertainty is small enough for the decision. Repeated readings on one specimen estimate aspects of measurement repeatability; they do not create independent parts or reveal part-to-part scatter. Parts sharing a lot, setup or thermal history may be correlated and should not automatically be pooled as independent evidence.

Scatter also changes interpretation of capability and margin. A mean well inside a specification can conceal a lower tail outside it. Conversely, comparing only extremes without a sampling model can overstate what is known. Record sample size, lot identity, orientation, missing data and censoring. Missing evidence remains unknown. Do not replace it with the mean of another lot.

## Process-plan consequences

Structure–property reasoning should feed the fabrication plan as evidence requirements, not operating instructions. If residual stress is a concern, the plan may require a qualified stress assessment and dimensional evidence at defined stages. If porosity matters, define the inspection question and detection limits. If fiber orientation matters, link drawing orientation references to material and inspection records. If cure state matters, require evidence tied to the actual material system and qualified process rather than inventing a schedule. Each requirement needs review by people authorized for the real application.

## Common mistakes

Avoid attributing every property change to grain size, assuming all porosity has equal severity, or treating compressive residual stress as automatically beneficial in every location. Do not infer cure completion from a calendar label, use one property average as a guaranteed minimum, or count repeated gauge readings as new parts. Never convert a conceptual process–structure relationship into a heat-treatment recipe, weld parameter, cure schedule or machine setup.

## Scope and sources

[MIT 3.032 Fall 2007](https://ocw.mit.edu/courses/3-032-mechanical-behavior-of-materials-fall-2007/pages/syllabus/) is a link-only comparator for elastic/plastic deformation, creep, fracture and processing across material classes; its integrated physical laboratories are not reproduced. Existing MIT 3.091SC, 3.012 and mechanics mappings provide foundational materials and mechanics links. [MIT 2.830J Spring 2008](https://ocw.mit.edu/courses/2-830j-control-of-manufacturing-processes-sma-6303-spring-2008/pages/calendar/) supplies a broader variation/modeling comparator. No source text, experiment, dataset or operational instruction is imported, and the local package remains partial and unreviewed.
