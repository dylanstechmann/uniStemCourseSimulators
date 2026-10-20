# Beam project guide: strength and stiffness of three synthetic sections (optional, ungraded)

**Status:** open, optional and ungraded. Five milestone self-checks in the Case studio save responses privately; nothing is submitted, collected or scored. The separate inactive project draft and its proposed review rubric remain unreviewed and are not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 3–5 hours across weeks 8 and 9.
**Prerequisite lessons:** [Free-body diagrams and equilibrium](../modules/01-free-body-diagrams-and-equilibrium.md), [Distributed loads, shear force, and bending moment](../modules/14-distributed-loads-shear-and-moment.md), [Torsion and bending](../modules/03-torsion-and-bending.md), [Beam deflection and stiffness](../modules/11-beam-deflection-and-flexural-modulus.md) and [Failure criteria, fatigue, and design margins](../modules/04-failure-criteria-fatigue-and-design-margins.md).
**Data:** the [project candidate table](../assessment-specs/beam-candidate-comparison.csv) and the [rehearsal candidate table](beam-rehearsal-candidates.csv).

## Purpose

The project carries one beam from equilibrium to a design-style comparison. Support reactions and the bending moment come from statics; stress and deflection come from the section properties; and two separate criteria, one for strength and one for stiffness, decide which synthetic candidate passes. The comparison shows that a beam can be strong enough and still too flexible, and the last step names what this idealized calculation cannot say about a real structure.

## The project

A simply supported beam spans L = 0.300 m with a centered point load F = 30 N. Each candidate is a rectangular section of width b = 0.020 m; the candidate table gives its depth h, elastic modulus E and yield strength S_y. Use

R_A = R_B = F/2, M_max = FL/4, I = bh³/12, σ_max = 6M_max/(bh²) and δ_max = FL³/(48EI).

Assume linear-elastic Euler–Bernoulli behaviour, and ignore shear deformation, stress concentrations, joints, fatigue, manufacturing variation and uncertainty. For this exercise, a candidate passes only if both σ_max ≤ S_y/2 and δ_max ≤ 0.600 mm.

1. Draw the free-body diagram and calculate the support reactions and the maximum bending moment.
2. Convert every candidate property to consistent SI units. Calculate I, the maximum bending stress and the maximum deflection for A, B and C.
3. Apply the two criteria separately. Explain why a candidate can pass the strength check and fail the stiffness check.
4. For each candidate, calculate the load at which the strength limit would be reached and the load at which the deflection limit would be reached. The smaller value controls under this simplified model.
5. Re-evaluate the only passing candidate at a 20% higher load, then identify the missing evidence that prevents this calculation from being a real design decision.

## Milestones

| Milestone | Suggested week | Task | Where to check yourself |
| --- | --- | --- | --- |
| Rehearsal | 8 | Work the rehearsal beams, then use the open rehearsal practice set | **Practice gradebook**: Beam project rehearsal |
| M1 | 8 | Free-body diagram, reactions and maximum moment (task 1) | Case studio: project milestone 1 |
| M2 | 8 | Units, I, stress and deflection for each candidate (task 2) | Case studio: project milestone 2 |
| M3 | 8 | The two criteria applied separately (task 3) | Case studio: project milestone 3 |
| M4 | 9 | Strength and deflection limit loads (task 4) | Case studio: project milestone 4 |
| M5 | 9 | The raised load and the missing evidence (task 5) | Case studio: project milestone 5 |

Each Case studio milestone lists self-review statements. Responses are saved privately in this application and are never scored. The rehearsal uses a different span, width, load, deflection limit and candidates, so its answers are not the project's answers.

## Worked example: one more beam

Take a separate synthetic beam X: span 0.200 m, a 10 N load at midspan, width 0.010 m, depth 0.010 m, E = 3.0 GPa and S_y = 30 MPa, with criteria σ_max ≤ S_y/2 = 15 MPa and δ_max ≤ 0.400 mm.

1. **Statics.** Each support carries 5 N, and M_max = 10 × 0.200/4 = 0.500 N·m.
2. **Section.** I = 0.010 × 0.010³/12 ≈ 0.8333 × 10⁻⁹ m⁴.
3. **Stress.** σ_max = 6 × 0.500/(0.010 × 0.010²) = 3.00 MPa, well below 15 MPa, so X passes the strength check.
4. **Deflection.** δ_max = 10 × 0.200³/(48 × 3.0 × 10⁹ × 0.8333 × 10⁻⁹) ≈ 0.667 mm, above 0.400 mm, so X fails the stiffness check.
5. **Limit loads.** Both quantities are proportional to the load: the strength limit is reached at 10 × 15/3.00 = 50 N and the deflection limit at 10 × 0.400/0.667 ≈ 6.0 N. Deflection controls.

Doubling the depth would multiply I by 8 and divide the deflection by 8, while the stress would fall by a factor of 4. That difference is why depth is the efficient way to stiffen a beam.

## Reporting conventions

- Convert millimetres, gigapascals and megapascals to SI before calculating, and give results in the units each criterion uses.
- Keep at least four significant figures in intermediate values and round only the reported results.
- Apply each criterion separately and say which one fails.
- Disclose any software, spreadsheets or AI assistance you used.

## Self-review rubric

The inactive project draft proposes five criteria for a future human reviewer and assigns them no points. For self-review, mark each criterion 0 (absent), 1 (partly correct) or 2 (complete and consistent with the stated model).

| Criterion | Evidence of a complete response |
| --- | --- |
| Equilibrium | Correct support reactions and maximum moment |
| Stress | Consistent section moment and unit conversion |
| Deflection | Correct second moment and span and depth scaling |
| Failure criteria | Applies the yield and deflection limits independently |
| Limits | Separates this idealized calculation from real structural safety or design |

These marks are a self-check. They are not calibrated, carry no grade and do not stand in for an instructor's judgment.

## Limitations and provenance

The beams, loads, properties and thresholds are synthetic teaching values. The model assumes linear-elastic Euler–Bernoulli beams with ideal supports and ignores shear deformation, stress concentrations, joints, fatigue, imperfections, material variability and load uncertainty. Nothing here is a design basis, a safety-factor recommendation or an analysis of any real structure, fixture, implant or device. Original guide and synthetic rehearsal data: CC BY 4.0.
