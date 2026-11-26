# Optional constraints-based material-selection project guide

**Status:** Original optional project in partial Materials Science 0.1.0; unreviewed, ungraded, zero-point and formative-only. It produces a fictional evidence dossier, not a design release or material approval. All candidates, requirements, scores and numerical values are synthetic. No fabrication settings, heat-treatment recipe, standard-specific compliance or procurement instruction is included.

## Learning objectives

1. Translate fictional service needs into explicit hard constraints and measurable criteria before ranking candidates.
2. Recompute specific stiffness, mass and embodied-energy relationships for all synthetic rehearsal candidates.
3. Document trade-offs, sensitivity, unknown evidence and non-approval status in a five-milestone handoff.

## Project brief and rehearsal data

Prepare five linked records for a fictional component concept. Use the six thematic readings, the [characterization CSV](../labs/materials-characterization.csv) and the [rehearsal CSV](material-selection-rehearsal.csv). No physical experiment, material purchase, fabrication, standard certification or software execution is required.

Every rehearsal row is `synthetic-original`. The corrosion evidence score and cost index are invented ordinal teaching inputs, not measured corrosion rates, supplier quotes or compliance ratings. The fixed-volume comparison uses mass = ρV. Specific stiffness is E/ρ after converting GPa to Pa, and modeled embodied energy is mass multiplied by the stated fictional energy intensity.

For this rehearsal only, hard constraints are E ≥ 50 GPa, yield ≥ 150 MPa, maximum-temperature field ≥ 120 °C, corrosion evidence score ≥ 3 and cost index ≤ 8. These are arbitrary fictional criteria chosen for a reasoning exercise. They are not a service specification. Apply all constraints before discussing desirable trade-offs; a low cost or high modulus cannot erase a failed hard requirement.

| Candidate | Specific stiffness E/ρ (m²/s²) | Mass ρV (kg) | Energy (MJ) | Constraint outcome |
| --- | ---: | ---: | ---: | --- |
| R01 Asterion | 200×10⁹/7850 = 25,477,707.006… | 7850×0.0010 = 7.85 | 7.85×30 = 235.5 | Fails corrosion score |
| R02 Boralith | 120×10⁹/2700 = 44,444,444.444… | 2700×0.0020 = 5.4 | 5.4×18 = 97.2 | Eligible in model |
| R03 Caldrium | 190×10⁹/7800 = 24,358,974.359… | 7800×0.0015 = 11.7 | 11.7×35 = 409.5 | Fails cost index |
| R04 Densimere | 50×10⁹/1450 = 34,482,758.621… | 1450×0.0020 = 2.9 | 2.9×20 = 58 | Eligible in model |

R02 and R04 pass the fictional screen. R02 has higher specific stiffness; R04 has lower mass and modeled energy. There is no universal winner without a declared preference and sensitivity analysis. R01 and R03 remain ineligible under the declared constraints even though some of their individual values look attractive.

## Milestone 1: requirements and evidence gates

Define the fictional function, relevant loading and environment narratives, geometry convention and hard constraints. Separate mandatory requirements from optional criteria such as specific stiffness or inventory energy. List fatigue, joining, manufacturing, long-term stability, applicable standards and application-specific reviews as unknown unless supplied. No missing item may be treated as satisfied.

## Milestone 2: structure–property evidence note

Connect bonding and material class to candidate hypotheses. Use Miller indices and cubic spacing only for structural evidence, defects and phases for possible strengthening and transformation explanations, and polymer/ceramic/composite structure for class-specific limitations. Link Statics & Mechanics of Materials for full stress/strain and structural derivations instead of duplicating them. Explain process–microstructure–property links conditionally, without proposing a heat-treatment schedule or fabrication parameters.

## Milestone 3: multi-technique characterization audit

Recompute every lab-row d, cubic a and mass-loss percentage. Integrate structural, thermal and mechanical channels without treating them as interchangeable. Preserve C05’s unknown thermal event. Explain why one peak, a mass-loss percentage or a modulus value cannot identify composition, establish durability or approve a candidate. Include alternative explanations and the evidence needed to distinguish them, but no instrument operation or acquisition settings.

## Milestone 4: constraints and trade-off rehearsal

Recompute all four specific-stiffness, mass and energy values. Confirm R01 fails the corrosion constraint and R03 fails the cost constraint. Compare R02’s 44,444,444.444… m²/s² specific stiffness with R04’s 34,482,758.621… m²/s², then compare R04’s 2.9 kg and 58 MJ with R02’s 5.4 kg and 97.2 MJ. State how a change in preference could alter the choice while neither candidate becomes approved. R03 mass is 11.7 kg; do not discard it from the arithmetic audit merely because it fails screening.

A sensitivity note should identify which constraints or preferences change the eligible set or preferred trade-off. Do not silently loosen a constraint to rescue a favored candidate. Any revised criterion must be labelled as a new fictional scenario with its own assumptions.

## Milestone 5: bounded handoff

Assemble all five records with common identifiers and links to the reading, public practice, CSV rows and link-only source registry. Include hard constraints, all calculations, sensitivity, unknown fatigue and joining evidence, and unresolved scientific, engineering and application reviews. Finish by declaring the work optional, zero-point, formative, fictional and non-operational.

Use the six Case studio entries: one integrative case and five project milestones. Every rubric criterion carries zero points. These checklists do not grade prose, establish competence, verify standard compliance or confer material approval. A useful dossier lets another reader reproduce every value and see exactly where evidence ends.
