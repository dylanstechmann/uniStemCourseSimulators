# Fictional rotor trade-off portfolio (inactive draft)

**Status: authoring draft only.** This fictional, ungraded paper exercise is not an assessment used by the course platform. Every geometry, mass, imbalance and target is invented. This comparison is not an operating specification, safety test, or recommendation about real equipment.

## Purpose

Integrate relative centrifugal force, angular speed, idealized moment of inertia, rotational energy and imbalance force in one model comparison. This paper-only draft is distinct from the machine-compliance/orientation lab and the tendon self-assessment case.

## Synthetic design set

Treat each candidate as a uniform solid disk with the listed rotor mass and radius. The sample sits at the listed radius. Compare all three at a hypothetical common target of 600 × g, using g = 9.81 m/s². Treat the imbalance mass as a point mass at the sample radius. The model omits supports, flex, bearing loss, containment, manufacturing tolerances and all real-device constraints.

| Candidate | Disk mass (kg) | Radius (m) | Imbalance mass (kg) |
|---|---:|---:|---:|
| A | 1.0 | 0.080 | 0.0005 |
| B | 1.2 | 0.120 | 0.0005 |
| C | 0.6 | 0.100 | 0.0010 |

## Learner task

1. For each candidate, calculate angular speed in rad/s and rpm required for the same hypothetical 600 × g at its sample radius.
2. Calculate the stipulated disk moment of inertia and rotational kinetic energy at that speed.
3. Estimate the rotating force due to the stipulated point-mass imbalance.
4. Compare the candidates: identify which one has the largest modelled rotational energy, which has the largest imbalance force, and explain why one cannot label a candidate “safest” from these calculations.
5. Check dimensions and one limiting relation (for example, how required speed changes as sample radius changes at fixed RCF).
6. Add a scope note that prevents these invented values from being used as a speed setting or equipment recommendation.

## Author reference calculations

At each sample radius r, the target gives ω = √(600g/r) and rpm = 60ω/(2π). For the stipulated disk, I = ½MR² and KE = ½Iω². The point-imbalance estimate is F = m_imbalanceω²r.

| Candidate | ω (rad/s) | Approx. speed (rpm) | I (kg·m²) | KE (J) | Imbalance force (N) |
|---|---:|---:|---:|---:|---:|
| A | 271.25 | 2,590 | 0.00320 | 117.7 | 2.943 |
| B | 221.47 | 2,115 | 0.00864 | 211.9 | 2.943 |
| C | 242.61 | 2,317 | 0.00300 | 88.3 | 5.886 |

Equal RCF does not imply equal rpm, stored rotational energy or imbalance force when radii, masses and imbalance assumptions differ. The force estimate reduces to m_imbalance × 600g in this particular comparison, so C's doubled imbalance mass doubles the estimate. None of these ideal calculations supplies material strength, speed rating, containment or a validated safety margin.

## Inactive-draft boundary

This paper-only proposal has no score, rubric, gradebook mapping, platform activation, required status or effect on course completion. A qualified instructor should review the mechanics, dimensions, framing, accessibility and workload before any future adoption. Course maturity remains partial.
