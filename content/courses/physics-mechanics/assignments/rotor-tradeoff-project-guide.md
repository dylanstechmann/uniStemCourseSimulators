# Rotor trade-off project guide: speed, rotational energy and imbalance at a shared target (optional, ungraded)

**Status:** open, optional and ungraded. Five milestone self-checks in the Case studio save responses privately; nothing is submitted, collected or scored. The separate inactive project draft remains unreviewed and is not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 3–5 hours across weeks 11 and 12.
**Prerequisite lessons:** [Work, energy, and power](../modules/02-work-energy-and-power.md), [Torque, angular momentum and rolling](../modules/10-torque-angular-momentum-and-rolling.md) and [Uniform circular motion and rigid-body rotation: an ideal centrifuge model](../modules/06-centrifuge-rotation-and-balance.md).
**Data:** the [project candidate table](../assessment-specs/fictional-rotor-candidates.csv) and the [rehearsal candidate table](rotor-rehearsal-candidates.csv).

## Purpose

The project compares three invented rotors that must all reach the same hypothetical acceleration ratio at their sample radius. Speed, stored rotational energy and imbalance force each follow from one ideal model, and the comparison shows that a shared target does not make rotors alike. The last steps check dimensions and limiting behaviour and state why none of these numbers can serve as a speed setting, a safety judgment or an equipment recommendation.

## The project

Treat each candidate as a uniform solid disk with the listed rotor mass and radius; the sample sits at that radius. All three must reach a hypothetical common target of 600 × g at the sample radius, with g = 9.81 m/s². Treat the imbalance mass as a point mass at the sample radius. The model omits supports, flex, bearing loss, containment, manufacturing tolerances and every real-device constraint.

| Candidate | Disk mass (kg) | Radius (m) | Imbalance mass (kg) |
| --- | ---: | ---: | ---: |
| A | 1.0 | 0.080 | 0.0005 |
| B | 1.2 | 0.120 | 0.0005 |
| C | 0.6 | 0.100 | 0.0010 |

1. For each candidate, calculate the angular speed in rad/s and in rpm required for the same hypothetical 600 × g at its sample radius.
2. Calculate the stipulated disk moment of inertia and the rotational kinetic energy at that speed.
3. Estimate the rotating force due to the stipulated point-mass imbalance.
4. Compare the candidates: identify which has the largest modelled rotational energy and which has the largest imbalance force, and explain why none can be labelled "safest" from these calculations.
5. Check dimensions and one limiting relation, for example how the required speed changes with sample radius at a fixed target.
6. Add a scope note that prevents these invented values from being used as a speed setting or an equipment recommendation.

## Milestones

| Milestone | Suggested week | Task | Where to check yourself |
| --- | --- | --- | --- |
| Rehearsal | 11 | Work the rehearsal candidates, then use the open rehearsal practice set | **Practice gradebook**: Rotor project rehearsal |
| M1 | 11 | Angular speed and rpm for each candidate (task 1) | Case studio: project milestone 1 |
| M2 | 11 | Moment of inertia and rotational energy (task 2) | Case studio: project milestone 2 |
| M3 | 11 | Imbalance force (task 3) | Case studio: project milestone 3 |
| M4 | 12 | The comparison and why none is "safest" (task 4) | Case studio: project milestone 4 |
| M5 | 12 | Dimensions, a limiting relation and the scope note (tasks 5–6) | Case studio: project milestone 5 |

Each Case studio milestone lists self-review statements. Responses are saved privately in this application and are never scored. The rehearsal uses two different candidates at a different target, so its answers are not the project's answers.

## Worked example: one invented rotor

Take a separate invented candidate X: a 2.0 kg uniform disk of radius 0.050 m with a 0.0002 kg imbalance, at a target of 1,000 × g.

1. **Speed.** The target fixes ω²r = 1,000 × 9.81 = 9,810 m/s², so ω² = 9,810/0.050 = 196,200 rad²/s² and ω ≈ 442.9 rad/s, about 4,230 rpm by rpm = 60ω/(2π).
2. **Inertia and energy.** I = ½MR² = ½ × 2.0 × 0.050² = 0.0025 kg·m², and K = ½Iω² = ½ × 0.0025 × 196,200 = 245.25 J.
3. **Imbalance force.** F = mω²r = 0.0002 × 196,200 × 0.050 ≈ 1.962 N.
4. **A limiting check.** For this fixed rotor and radius, doubling the target doubles ω², so it doubles both K and F; the angular speed itself does not double.
5. **Units.** kg × (rad/s)² × m reduces to kg·m/s², a newton, because radians are dimensionless, and kg·m² × (rad/s)² reduces to joules.

None of these numbers says anything about strength, containment or a safe operating speed.

## Reporting conventions

- Keep units on every quantity: rad/s, rpm, kg·m², joules and newtons.
- Keep at least four significant figures in intermediate values and round only the reported results.
- Separate calculated model values from comparisons and from the scope note.
- Disclose any software, spreadsheets or AI assistance you used.

## Self-review rubric

The inactive project draft proposes no rubric. For self-review, mark each criterion 0 (absent), 1 (partly correct) or 2 (complete and consistent with the stated model).

| Criterion | Evidence of a complete response |
| --- | --- |
| Speeds | Correct ω and rpm for each candidate from its own sample radius |
| Energy | Correct disk inertia and rotational energy, with units |
| Imbalance | Correct point-mass force at the sample radius, with units |
| Comparison | Identifies the largest energy and force and explains why equal targets do not make rotors alike |
| Checks and scope | Checks dimensions and a limiting relation and rules out any use as a setting or recommendation |

These marks are a self-check. They are not calibrated, carry no grade and do not stand in for an instructor's judgment.

## Limitations and provenance

Every geometry, mass, imbalance and target is invented. The uniform-disk and point-imbalance models omit supports, flex, bearing loss, containment, manufacturing tolerances and material strength, and the acceleration ratio describes acceleration only. This comparison is not an operating specification, a safety test or a recommendation about real equipment. Original guide and synthetic rehearsal data: CC BY 4.0.
