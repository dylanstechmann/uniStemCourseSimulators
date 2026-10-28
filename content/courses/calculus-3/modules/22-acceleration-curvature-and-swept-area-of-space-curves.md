# Space curves: acceleration, curvature and swept area

The [spatial-curves lesson](07-vectors-planes-and-spatial-curves.md) parametrized a curve r(t), found its velocity r′(t) and unit tangent, and measured traced length with ∫|r′|dt. This lesson takes the next derivative. Acceleration says how velocity changes, and it has two independent parts: one that changes the speed and one that turns the direction. The turning part defines **curvature**, a measure of how sharply the path bends that does not depend on how fast the path is traversed. A final section uses the cross product to show when a position vector sweeps out equal areas in equal times. All curves, units and numbers here are synthetic.

[MIT OCW 18.02SC Multivariable Calculus (Fall 2010), Unit 1 Part C](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/1.-vectors-and-matrices/part-c-parametric-equations-for-curves/) has sessions on velocity and acceleration, velocity and arc length, and Kepler's second law. The [Harvard Math 21a (Summer 2003) lecture plan](https://abel.math.harvard.edu/~knill/teaching/summer2003/syllabus.html) gives consecutive lectures to "curves, velocity, acceleration" and "arclength, curvature". Both are link-only scope comparators; no text, figure or problem is reproduced.

## Learning objectives

By the end of this lesson, you should be able to:

1. Differentiate a parametrized space curve twice and split the acceleration into tangential and normal components, a_T = d|v|/dt and a_N = √(|a|² − a_T²).
2. Compute curvature from κ = |v × a|/|v|³ and from a_N/|v|², interpret its reciprocal as a radius of curvature, and evaluate arc length numerically when the speed has no antiderivative.
3. Show with r × v that a central acceleration sweeps equal areas in equal times, and state when the argument fails.

## Acceleration of a parametrized curve

Write v = r′ for velocity, a = r″ for acceleration, |v| for speed and T = v/|v| for the unit tangent wherever v ≠ 0. Take the synthetic curve r(t) = (2t, t², t³/3), with t in seconds and lengths in metres. Then v = (2, 2t, t²) and

|v|² = 4 + 4t² + t⁴ = (t² + 2)²,

so the speed is exactly t² + 2 m/s and no square root remains. The acceleration is a = (0, 2, 2t) m/s². The traced length over 0 ≤ t ≤ 3 is ∫₀³(t² + 2)dt = 9 + 6 = 15 m.

At t = 1 the velocity is (2, 2, 1) with speed 3 m/s, and the acceleration is (0, 2, 2) with magnitude 2√2 = 2.83 m/s². The acceleration is not parallel to the velocity, and the speed is changing: d|v|/dt = 2t = 2 m/s² there.

## Tangential and normal parts

Because v = |v|T, the product rule gives

\[
a = \frac{d|v|}{dt}\,T + |v|\,\frac{dT}{dt}.
\]

Since T·T = 1, differentiating shows T·T′ = 0, so T′ is perpendicular to T. Define the **curvature** κ as the rate at which the tangent turns per unit length travelled, κ = |T′|/|v|, using ds = |v|dt. If N is the unit vector along T′, which points toward the inside of the bend, then |v|T′ = κ|v|²N, and

\[
a = a_T\,T + a_N\,N,\qquad a_T = \frac{d|v|}{dt},\qquad a_N = \kappa\,|v|^2 \ge 0 .
\]

The tangential part changes the speed, and the normal part changes the direction. They are perpendicular, so |a|² = a_T² + a_N², which gives a_N without computing N, and a_T = a·v/|v| also follows from dotting a with T.

For the curve at t = 1, a_T = (0·2 + 2·2 + 2·1)/3 = 2 m/s², which matches d|v|/dt = 2t, and a_N = √(8 − 4) = 2 m/s².

A particle at constant speed has a_T = 0, so its acceleration is perpendicular to its velocity. For the helix r(t) = (3 cos t, 3 sin t, 4t) of the previous lesson, the speed is constantly 5 m/s and a = (−3 cos t, −3 sin t, 0) has magnitude 3 m/s², all of it normal. Then κ = a_N/|v|² = 3/25 = 0.12 m⁻¹. Constant speed does not mean zero acceleration, only zero tangential acceleration.

## Curvature two ways

The definition gives κ = a_N/|v|². The cross product gives a second route. Since v = |v|T and a = a_T T + a_N N,

v × a = |v| a_N (T × N),

and |T × N| = 1, so |v × a| = |v| a_N. Therefore

\[
\kappa = \frac{|v \times a|}{|v|^3}.
\]

At t = 1, v × a = (2, 2, 1) × (0, 2, 2) = (2, −4, 4), with length 6, so κ = 6/27 = 2/9 = 0.222 m⁻¹, the same as a_N/|v|² = 2/9. The reciprocal 1/κ = 4.5 m is the **radius of curvature**, the radius of the circle that best matches the path there.

Two properties follow. First, curvature belongs to the path. Traversing the same path twice as fast doubles v, quadruples a_N and leaves κ unchanged, because κ = |dT/ds| involves only the arc length s. Second, a circle of radius R has κ = 1/R, so a_N = v²/R, the centripetal acceleration of the [vector-kinematics lesson](../../physics-mechanics/modules/07-vector-kinematics-frames-and-constraints.md) in the Mechanics course. A synthetic ring-shaped channel of radius 0.5 m carrying fluid at 2 m/s has a_N = 4/0.5 = 8 m/s² directed toward its center. A straight line has κ = 0.

## When arc length has no closed form

The traced length s = ∫|v|dt exists for every smooth curve, but |v| often has no elementary antiderivative. For the ellipse r(t) = (4 cos t, 3 sin t, 0), the speed is √(16 sin²t + 9 cos²t), and the perimeter 4∫₀^(π/2) √(16 sin²t + 9 cos²t) dt is not an elementary function. Simpson's rule with 4000 panels gives **22.10 m**. Two independent checks are available. The perimeter must lie between those of the inscribed circle of radius 3, 2π·3 = 18.85, and the circumscribed circle of radius 4, 2π·4 = 25.13. And Ramanujan's approximation π[3(a + b) − √((3a + b)(a + 3b))] with a = 4 and b = 3 also gives 22.10.

The same ellipse has v = (−4 sin t, 3 cos t) and a = (−4 cos t, −3 sin t), so the third component of v × a is 12 sin²t + 12 cos²t = 12 at every t. Hence

κ = 12/(16 sin²t + 9 cos²t)^(3/2).

At the end of the long axis, (4, 0), κ = 12/27 = 4/9 = 0.444 m⁻¹ and the radius of curvature is 2.25 m. At the end of the short axis, (0, 3), κ = 12/64 = 3/16 = 0.1875 m⁻¹ and the radius is 5.33 m. The path bends most sharply at the ends of its long axis.

## Central acceleration and swept area

Differentiate the cross product of position and velocity:

d/dt (r × v) = v × v + r × a = r × a.

If the acceleration is **central**, meaning a is parallel to r so that r × a = 0, then r × v is constant. In a short time dt the position vector sweeps a thin triangle with sides r and v dt, of area ½|r × v|dt. So the **areal speed** ½|r × v| is constant: equal areas are swept in equal times, which is Kepler's second law.

Take r(t) = (4 cos 2t, 3 sin 2t, 0). Its acceleration is a = −4r, which is central. Then r × v = (0, 0, 24) at every t, and the areal speed is 12 m²/s. Check: the ellipse has area π·4·3 = 12π m² and is traversed in a period of π s, so the average rate is 12π/π = 12 m²/s.

The argument needs the acceleration to be central with respect to the point from which r is measured. It says nothing about the size of the acceleration, and if a had any component perpendicular to r about that point, r × a would not vanish and the areal speed would change.

## Common mistakes

- Treating constant speed as zero acceleration.
- Calling the whole of |a| the centripetal part, instead of splitting a into a_T and a_N first.
- Dividing |v × a| by |v| instead of |v|³, which leaves the wrong units for κ.
- Believing a faster traversal of the same path is more sharply curved.
- Using a_N = v²/R on a path whose radius of curvature is changing without evaluating R at that point.
- Applying the swept-area result about a point that is not the center of the acceleration.

## Worked example

**Problem.** A point on the rim of a synthetic wheel of radius R = 0.3 m, rolling without slipping at 1 rad/s, traces the cycloid r(t) = R(t − sin t, 1 − cos t, 0), with t in seconds. Find the length of one arch, then the speed, a_T, a_N, curvature and radius of curvature at t = π/2 and at the top of the arch, t = π.

**Step 1: speed.** v = R(1 − cos t, sin t, 0), so |v|² = R²(2 − 2 cos t) = 4R² sin²(t/2) and the speed is 2R sin(t/2) for 0 ≤ t ≤ 2π.

**Step 2: arch length.** ∫₀^(2π) 2R sin(t/2) dt = 8R = 2.4 m.

**Step 3: acceleration.** a = R(sin t, cos t, 0), so |a| = R = 0.3 m/s² at every instant.

**Step 4: t = π/2.** The speed is 2R sin(π/4) = 0.424 m/s. The tangential part is a_T = d|v|/dt = R cos(t/2) = 0.212 m/s², so a_N = √(R² − a_T²) = 0.212 m/s². Then κ = a_N/|v|² = 0.2121/0.18 = 1.18 m⁻¹ and the radius of curvature is 0.849 m.

**Step 5: top of the arch, t = π.** The speed is 2R = 0.6 m/s, twice the speed of the wheel's center. The speed is at its maximum, so a_T = 0 and a_N = |a| = 0.3 m/s². Then κ = 0.3/0.36 = 0.833 m⁻¹ and the radius of curvature is 4R = 1.2 m.

**Step 6: check.** In general the radius of curvature is |v|³/|v × a| = 4R sin(t/2), which gives 0.849 m and 1.2 m at the two instants. As t approaches 0 or 2π, where the rim point meets the ground, the speed and the radius both approach zero: the path has a cusp there, and T is not defined because v = 0.

## Limits of this lesson

All curves, wheels, channels and orbits are synthetic mathematical models. The results assume smooth regular curves with v ≠ 0, so curvature is not defined at a cusp. Torsion and the full moving frame of a space curve are not developed, and the swept-area result is a statement about r × a = 0, not about any particular force law, orbit or vehicle. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
