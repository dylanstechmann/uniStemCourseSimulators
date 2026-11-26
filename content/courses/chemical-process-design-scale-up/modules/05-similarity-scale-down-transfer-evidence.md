**Status:** Original, explicitly partial advanced university/industry survey material; unreviewed and formative-only. All species, equipment, records, values and organizations are synthetic and fictional. This is a paper design-review exercise, not an operating, fabrication, safety, validation or release instruction.

# Similarity, scale effects and technology-transfer evidence

## Learning objectives

- Use dimensionless similarity to state which mixing, pumping, heat-removal and reaction/transport regimes a scale comparison actually preserves.
- Analyze selectivity, separation and fouling scale effects and construct a scale-down hypothesis without asserting equivalence.
- Plan DOE, measurement uncertainty, pilot evidence and transfer records with independent experimental units and explicit unresolved gaps.

## Similarity is selective, not universal

Scale-up begins by identifying the phenomena that control the question. Geometric similarity preserves shape ratios, not every physical regime. Dynamic similarity requires relevant dimensionless groups; kinematic and boundary-condition similarity add further demands. Reynolds, Froude, power, Nusselt, Sherwood, Damköhler and other groups encode different balances. It is often impossible to preserve all of them across scales with the same fluid model and constraints. The design review must therefore say which groups are matched, which are allowed to move and why the resulting bias is acceptable for a specific hypothesis.

A dimensionless group is not a certificate. Its correlation range, geometry, property basis and transient history matter. Generic species and equipment prevent inference of real properties, so this lesson uses algebraic ratios only. Unknown property or regime evidence remains unresolved rather than being assigned a convenient typical value.

## Mixing, pumping and heat removal

For geometrically similar stirred models under a declared fully turbulent constant-speed power-per-volume approximation, P/V scales with diameter squared when other stipulated factors are fixed. Tripling the diameter ratio therefore gives (D₂/D₁)²=3²=9 for the modeled P/V ratio. This is not an agitator duty or motor rating. Blend time, micromixing, solids suspension, gas dispersion and local shear need not share that scaling.

Pumping discussions distinguish delivered flow, suction conditions, system resistance and measurement evidence. Scale changes can move cavitation, solids behavior and control authority even when nominal throughput scales cleanly. No pump curve, equipment rating or startup instruction is supplied.

Surface-area-to-volume effects make heat removal a central scale question. Under geometric similarity, area/volume scales as 1/L. A fourfold length increase gives a relative area/volume ratio of 1/4=0.25 if heat generation per volume were held constant. This ratio is not a heat-transfer coefficient or an exchanger design. Jacket limitations, internal surfaces, fouling, viscosity and mixing can change together. Scale-up claims must compare local thermal histories, not only bulk averages.

## Reaction, transport and selectivity

A Damköhler-type ratio compares characteristic reaction and transport or residence times. In the synthetic relation Da=kτ, k=0.3 per time unit and τ=8 time units gives Da=2.4. It does not identify a real kinetic constant or predict conversion without a reactor and rate model. At larger scale, mixing and heat/mass transfer can alter local concentration and temperature histories, changing the apparent selectivity between desired B and undesired S even when intrinsic kinetics are unchanged.

Fast reactions are especially sensitive to micromixing and feed-distribution history. Slow reactions may be more sensitive to residence-time distribution or thermal drift. A scale comparison should retain time-resolved evidence and avoid treating final bulk composition as proof of the same pathway. Measurement uncertainty and sample handling can also create apparent selectivity shifts.

## Separation and fouling scale effects

Separations couple equilibrium, rate, hydrodynamics and equipment geometry. Increasing throughput can change residence time, wetting, maldistribution, entrainment or pressure drop; none is captured by a single capacity multiplier. Membrane or adsorption concepts add accessibility and competitive transport questions. These are mechanism prompts, not equipment-selection rules.

Fouling changes effective area, resistance, flow distribution and cleanability over time. A short early record cannot establish long-run performance. Scale comparisons need matched foulant definitions, cleaning history, surface condition and time basis. If deposits alter both heat transfer and hydrodynamics, a heat-duty trend alone cannot diagnose the mechanism. No cleaning recipe, waste instruction or operational cycle is supplied.

## Scale-down models and DOE

A scale-down model is a deliberately biased experimental system used to reproduce selected large-scale mechanisms. The hypothesis might be “this model reproduces the proposed mixing-limitation regime,” not “this small unit is the plant.” Evidence compares dimensionless groups and local responses, identifies deliberately unmatched features and states the decisions for which the model is informative. Negative or divergent results revise the hypothesis rather than being hidden.

Design of experiments begins with the experimental unit, factors, responses, randomization, blocking and analysis model. Repeated probes or instrument records within one run improve description of that run but do not create independent runs. Reused scenarios and repeated instrument records are correlated and descriptive, not independent replication. Factor ranges must come from evidence and safety review, not arbitrary extremes. Interactions and curvature should be considered before declaring linear sensitivity. Missing runs and failed measurement checks remain unresolved.

## Measurement uncertainty and pilot campaigns

Uncertainty budgets distinguish bias, repeatability, reproducibility, calibration, sampling and model-inference contributions. Covariance matters when measurements share calibration or sampling history. A precise composite estimate cannot repair an unrepresentative sample. Pilot readiness therefore includes measurement-system evidence, model version, data provenance, independent run definitions and criteria for stopping interpretation when validity fails. This package provides no pilot run sheet or production setpoint.

A pilot campaign is an evidence program, not a ceremonial scale step. It should prioritize unresolved mechanisms, define comparison baselines and preserve raw time-linked records. Campaign scenarios can be counted descriptively, but reused conditions are not independent replicates. Technology transfer sends and receives evidence: design basis, model/version history, equipment and compatibility records, measurement methods, deviations, open risks and continued-verification responsibilities. Receiving-site differences can invalidate the sending-site model.

## Application links and common mistakes

The owner’s open-perfusion-rig and perfusion-calibration-lab repositories are link-only references for modeled displacement versus measured delivery and independent-run uncertainty. No code, data or calibration claims are imported. Habitat-resource-sandbox is link-only for resource-ledger boundaries, not process validation.

Common mistakes include preserving one dimensionless group while claiming full similarity, treating P/V or area/volume arithmetic as equipment design, pooling repeated readings into an artificial sample size, and calling a successful pilot demonstration technology transfer or process validation. Arithmetic similarity is not physical equivalence, and all missing scale or measurement evidence leaves the relevant gate on HOLD.

## Scope and sources

MIT 10.490 Fall 2006 and 10.491 Spring 2006 are link-only comparators for model-based design and team evidence. Existing transport and statistics records support prerequisite scope. FDA 2011 is link-only for lifecycle evidence context, not validation authority. The readings, ratios and synthetic campaign examples are original and unreviewed; real scale-up requires qualified process, reaction, transport, equipment, measurement, safety and quality reviewers with current data and standards.
