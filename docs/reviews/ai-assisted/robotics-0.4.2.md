# Robotics & Mechatronics 0.4.2 — two-link kinematics and reachability

Date: 2026-10-10. Codex expanded the original week-3 reading and added independent inverse/forward calculations to the regression suite. The same AI assistant authored the lesson and tests, so these checks are not independent academic or human review. The course remains **partial, unreviewed and formative-only**.

## Scope

The reading derives the planar two-link forward equations, checks the reachable annulus before solving, computes both elbow branches for one target, and qualifies the result with joint limits and singular boundary cases. It explains that both branches can reach the same endpoint and asks learners to substitute every inverse candidate back into the forward model. Existing practice questions, keys and objectives are unchanged. The course advances from 0.4.1 to 0.4.2; two compact legacy readings remain.

## Numerical checks

For constructed links $L_1=0.4$ m and $L_2=0.3$ m, target $(0.4,0.3)$ m has radius 0.5 m within the reachable interval $[0.1,0.7]$ m and gives $\cos\theta_2=0$. The branches $(0^\circ,90^\circ)$ and $(73.74^\circ,-90^\circ)$ each reproduce the target. The fully extended and folded boundary angles make the planar determinant zero.

The regression checks both branch positions, geometric bounds, course version and schedule/status labels. It does not validate installed hardware, collisions, calibration, dynamics or safety.
