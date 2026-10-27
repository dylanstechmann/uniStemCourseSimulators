# Electric dipoles: field, torque, energy and force

The [superposition lesson](07-superposition-potential-and-gauss-boundaries.md) added the fields and potentials of separate point charges. The most important arrangement built that way is the **electric dipole**: two equal and opposite charges held a small distance apart. A dipole is neutral overall, yet it produces a field, turns in a uniform field and is pulled by a nonuniform one. The same three behaviours reappear for the magnetic dipole of a current loop in the [field-sources lesson](16-sources-of-magnetic-fields-biot-savart-ampere-and-dipoles.md), and many small aligned dipoles are the microscopic picture behind the [dielectrics lesson](08-capacitance-dielectrics-and-energy-boundaries.md). All charges, distances and fields here are synthetic teaching values, and the rounded Coulomb constant k = 9.00 × 10⁹ N·m²/C² is stipulated, as in the superposition lesson.

Both comparators treat dipoles early. The [MIT OCW 8.02 Physics II: Electricity and Magnetism (Spring 2007) class topics](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/class-topics/) name dipoles in session 2, beside electric fields and continuous charge distributions, and [Open Yale Courses PHYS 201, Lecture 2: Electric Fields](https://oyc.yale.edu/physics/phys-201/lecture-2) has a chapter on electric dipoles. Both are used here only as link-only scope comparators; no text, figure or problem is reproduced.

## Learning objectives

By the end of this lesson, you should be able to:

1. Build the field and potential of a two-charge dipole by superposition, and use the far-field forms on its axis and on its perpendicular bisector.
2. Calculate the torque, potential energy and rotation work for a dipole in a uniform field, and identify its stable and unstable orientations.
3. Find the net force on a dipole in a nonuniform field, check it against the force on the source charge, and judge when the point-dipole approximation is adequate.

## Two charges, one moment

Place +q and −q a distance d apart. The **dipole moment** is the vector

\[
\vec p = q\,\vec d,
\]

with magnitude qd, in C·m, pointing **from the negative charge to the positive charge**. Field lines run the other way, from + to −, which is a frequent source of sign errors. For q = 2.0 nC and d = 4.0 mm, p = 8.0 × 10⁻¹² C·m. Only the product qd matters far away: doubling the charge and halving the separation gives the same distant field.

## The far field falls as 1/r³

On the axis, at distance z from the centre on the positive side, the two contributions point in opposite directions, and superposition gives

\[
E_\text{axis} = kq\left[\frac{1}{(z - d/2)^2} - \frac{1}{(z + d/2)^2}\right] = \frac{2kqzd}{(z^2 - d^2/4)^2} \approx \frac{2kp}{z^3}\quad (z \gg d).
\]

The field points along p on both sides of the dipole. At z = 4.0 cm, ten times the separation, the exact value for the example dipole is 2261 N/C and the far-field estimate 2kp/z³ gives 2250 N/C, about 0.5% low.

On the perpendicular bisector, at distance y from the centre, the components along the bisector cancel and the components parallel to the axis add:

\[
E_\text{bisector} = \frac{kp}{(y^2 + d^2/4)^{3/2}} \approx \frac{kp}{y^3},
\]

directed **opposite** to p. At y = 4.0 cm this is 1121 N/C exactly and 1125 N/C from the far-field form. At the same large distance, the axial field is twice the bisector field.

Why 1/r³ rather than 1/r²? The two charges' fields nearly cancel, and what survives is their small difference, which falls one power of distance faster than either field alone. A net charge always dominates at large distance; a neutral pair has only this weaker residue.

The potential (zero at infinity) shows the same structure. Far away, V ≈ kp cos θ/r², where θ is measured from p. On the axis at z = 4.0 cm the exact value kqd/(z² − d²/4) is 45.1 V, against 45.0 V from the approximation. On the bisector every point is equidistant from +q and −q, so **V = 0 exactly**, even though the field there is not zero. A zero of potential says nothing about the local field, which depends on how V changes nearby.

## Torque and energy in a uniform field

In a uniform field E, the forces qE and −qE are equal and opposite, so the **net force is zero**. They act at different points, however, and form a couple with torque

\[
\vec\tau = \vec p \times \vec E,\qquad |\vec\tau| = pE\sin\theta,
\]

which turns p toward E. The corresponding potential energy, taking zero when p is perpendicular to E, is

\[
U = -\vec p\cdot\vec E = -pE\cos\theta .
\]

It is lowest when p and E are aligned, a **stable** equilibrium, and highest when they are anti-aligned, an **unstable** one: a small tilt from 180° grows. Turning the dipole slowly from θ₁ to θ₂ takes external work U(θ₂) − U(θ₁) = pE(cos θ₁ − cos θ₂).

For the example dipole in a uniform 5.0 × 10⁴ N/C field, the largest torque, at 90°, is pE = 4.0 × 10⁻⁷ N·m, and at 30° it is half that. Turning the dipole from aligned to anti-aligned takes 2pE = 8.0 × 10⁻⁷ J. These are the same forms as τ = μ × B and U = −μ·B for a current loop.

## A net force needs a nonuniform field

If the field differs at the two charges, the forces no longer cancel. For a dipole aligned with a field that changes along the dipole's direction, the net force is approximately p times the rate of change of the field along that direction, and it pulls an aligned dipole **toward the stronger field**. An anti-aligned dipole is pushed toward weaker field, but that orientation is unstable.

Near a fixed point charge Q, the field kQ/r² falls with distance, and an aligned dipole on the radial line feels

\[
F \approx p\left|\frac{dE}{dr}\right| = \frac{2kQp}{r^3},
\]

directed toward Q. For the example dipole 10 cm from a +5.0 nC charge, F ≈ 7.2 × 10⁻⁷ N; summing the two point-charge forces exactly gives 7.21 × 10⁻⁷ N. Newton's third law provides an independent check. The dipole's own axial field at Q is 2kp/r³ = 144 N/C, so the force on Q is 5.0 nC × 144 N/C = 7.2 × 10⁻⁷ N, equal in size and opposite in direction. Interactions between a charge and a neutral object, such as a charged rod attracting small neutral scraps, rest on this mechanism once the field has induced or aligned dipoles in the object.

## When is a point dipole good enough?

The approximations replace the exact two-charge sums by their leading terms, so their accuracy depends on d/r. On the axis, the exact field divided by 2kp/z³ is (1 − d²/4z²)⁻²: about 1.005 at z = 10d, 1.020 at z = 5d and 1.138 at z = 2d. Close to the charges, use superposition of the two point charges directly. A dielectric's polarization is a further step: it treats very many molecular dipoles as a smooth average, which the dielectrics lesson uses through a permittivity rather than by adding individual dipole fields.

## Common mistakes

- Pointing p from + to −; the moment points from the negative charge to the positive one.
- Using a 1/r² law for a dipole's far field; the leading field falls as 1/r³.
- Concluding that the field vanishes on the bisector because the potential does.
- Forgetting the factor of 2 on the axis, or the reversed direction on the bisector.
- Expecting a net force on a dipole in a uniform field; only a torque acts.
- Treating U = −pE cos θ as an absolute energy; only differences between orientations matter.
- Applying far-field formulas within a few separations of the charges.

## Worked example

**Problem.** A synthetic dipole has charges ±3.0 nC separated by 2.0 mm. Find its field on the axis 3.0 cm from the centre, the torque on it at 60° in a uniform 2.0 × 10⁴ N/C field, the work to turn it there from alignment, and the net force when it is aligned on the radial line 5.0 cm from a +4.0 nC point charge.

**Step 1: moment.** p = qd = 3.0 × 10⁻⁹ × 2.0 × 10⁻³ = 6.0 × 10⁻¹² C·m.

**Step 2: axial field.** z = 15d, so the far-field form should do well: 2kp/z³ = 2 × 9.00 × 10⁹ × 6.0 × 10⁻¹²/(0.030)³ = 4000 N/C. The exact two-charge sum gives 4009 N/C, about 0.2% higher.

**Step 3: torque.** pE sin 60° = 6.0 × 10⁻¹² × 2.0 × 10⁴ × 0.866 = 1.04 × 10⁻⁷ N·m, turning p toward E.

**Step 4: work.** pE(cos 0° − cos 60°) = 1.2 × 10⁻⁷ × 0.5 = 6.0 × 10⁻⁸ J.

**Step 5: force near the charge.** 2kQp/r³ = 2 × 9.00 × 10⁹ × 4.0 × 10⁻⁹ × 6.0 × 10⁻¹²/(0.050)³ = 3.46 × 10⁻⁶ N, toward the charge.

**Step 6: check.** The dipole's axial field at the point charge is 2kp/r³ = 864 N/C, so the force on the charge is 4.0 × 10⁻⁹ × 864 = 3.46 × 10⁻⁶ N, equal and opposite, as Newton's third law requires.

## Limits of this lesson

All charges, separations and fields are synthetic. The analysis uses point charges in vacuum, rigid dipoles and fields that are either uniform or produced by a single fixed point charge. The general off-axis field of a dipole is stated only through the potential, and quadrupole and higher multipole terms, molecular polarizability and the microscopic theory of dielectrics are not developed. Nothing here describes a real molecule, device or material. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
