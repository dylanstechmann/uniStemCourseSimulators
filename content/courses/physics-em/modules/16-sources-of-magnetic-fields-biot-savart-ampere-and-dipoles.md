# Sources of magnetic fields: Biot–Savart, Ampère's law and magnetic dipoles

The [magnetic-vectors lesson](11-magnetic-vectors-fields-and-force-work.md) used two field models, μ₀I/(2πr) for a long straight wire and μ₀nI inside a long solenoid, as stipulated formulas. This lesson shows where such formulas come from and when they apply. The **Biot–Savart law** builds the field of any current path by adding the contributions of short segments. **Ampère's law** gives the same answers much faster when the current distribution is symmetric enough. A small current loop then turns out to act as a **magnetic dipole**, which feels a torque in a uniform field and produces a characteristic field far away. All currents, geometries and fields here are synthetic teaching values, and μ₀ = 4π × 10⁻⁷ T·m/A is stipulated.

The undergraduate [MIT OCW 8.02 Physics II: Electricity and Magnetism (Spring 2007) class topics](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/class-topics/) place creating magnetic fields with Biot–Savart and Ampère's law (sessions 14–16) before forces and torques on dipoles and current loops (sessions 17–19), and both before Faraday's law. This lesson follows that order within the local magnetic-fields week. It uses 8.02 as a scope comparator only and reproduces no MIT material.

## Learning objectives

By the end of this lesson, you should be able to:

1. Use the Biot–Savart law to find the field of a circular loop on its axis and of a finite straight segment, and compare the results with idealized infinite models.
2. Apply Ampère's law to symmetric current distributions, including inside a thick wire and in a toroid, and calculate the force per length between parallel wires.
3. Calculate the magnetic dipole moment of a current loop, the torque and potential energy in a uniform field, and the far-field approximation, and state when each model fails.

## The Biot–Savart law

A short segment dl carrying current I contributes a field

**dB = (μ₀/4π) I dl × r̂ / r²,**

where r is the distance from the segment to the field point and r̂ the unit vector toward the point. The cross product makes each contribution perpendicular to both the current and the line to the point. The total field is the vector sum, an integral along the whole path. Like Coulomb's law for charge elements, the contribution falls as 1/r², but its direction comes from a cross product rather than lying along r̂.

**Circular loop on its axis.** For a loop of radius R carrying current I, every segment is the same distance √(R² + z²) from a point on the axis at height z. By symmetry, the components perpendicular to the axis cancel in opposite pairs and only the axial parts add:

**B_axis = μ₀IR² / [2(R² + z²)^(3/2)].**

At the centre, z = 0 and B = μ₀I/(2R). For I = 0.5 A and R = 0.020 m, that is **15.7 μT**. At z = R the field falls by a factor 2^(−3/2) to **5.55 μT**. The direction follows the right-hand rule: curl the fingers with the current, and the thumb points along the axial field.

**Finite straight segment.** For a straight segment at perpendicular distance d, the integral gives B = (μ₀I/4πd)(sin θ₂ − sin θ₁), where the angles are measured from the perpendicular to each end. For a segment of half-length a centred opposite the point, this is (μ₀I/4πd) × 2a/√(a² + d²). With I = 2 A, d = 0.010 m and a = 0.010 m, B = **28.3 μT**. The infinite-wire formula would give 40.0 μT, so a segment as long as twice the distance supplies only about 71% of the idealized field. As a grows much larger than d, the formula approaches μ₀I/(2πd).

Four such segments form a square loop. For a square of side 0.040 m carrying 0.5 A, the centre field is 2√2 μ₀I/(πL) = **14.1 μT**, slightly below the 15.7 μT of a circle with radius equal to half the side.

## Ampère's law

For any closed loop, called an **Amperian loop**,

**∮ B · dl = μ₀ I_enclosed,**

where I_enclosed is the net current crossing any surface bounded by the loop. The law is always true for steady currents, but it gives B only when symmetry makes B constant in magnitude and tangent to a chosen loop, or zero on parts of it. Otherwise the line integral cannot be untangled to find B.

**Long straight wire.** A circle of radius r around the wire gives B × 2πr = μ₀I, so B = μ₀I/(2πr), the formula used earlier.

**Inside a thick wire.** If current I is spread uniformly over a wire of radius a, a circle of radius r < a encloses I r²/a². Then B = μ₀I r/(2πa²), which grows linearly from zero at the centre. For I = 10 A and a = 2.0 mm, B is **500 μT** at r = 1.0 mm and 1000 μT at the surface. Outside, it falls as 1/r and returns to 500 μT at r = 4.0 mm.

**Toroid.** A ring-shaped coil with N turns carrying current I has field lines that circle inside the ring. A circle of radius r inside the windings encloses N I, so B = μ₀NI/(2πr). For N = 200 and I = 1.0 A, B is **1.00 mT** at r = 0.040 m and 0.667 mT at r = 0.060 m, so it is not uniform across a thick toroid. Outside the windings the enclosed current is zero, and the ideal field vanishes. The long-solenoid result μ₀nI follows the same way from a rectangular loop.

**Parallel wires.** One wire's field at the other is μ₀I₁/(2πd), and the force on length L of the second wire is I₂LB. So **F/L = μ₀I₁I₂/(2πd)**, attractive for currents in the same direction. For 2 A and 3 A at 5.0 mm apart, this is **240 μN/m**.

## Magnetic dipoles

A planar loop of area A carrying current I, with N turns, has magnetic dipole moment

**μ = N I A,**

directed along the loop's normal by the right-hand rule. In a uniform field the forces on opposite sides cancel, so the net force is zero, but they produce a torque

**τ = μ × B, with magnitude μB sin θ,**

which turns μ toward B. The potential energy is U = −μ·B = −μB cos θ, lowest when aligned. A 50-turn coil of radius 1.0 cm carrying 0.10 A has μ = 50 × 0.10 × π(0.010)² = **1.57 × 10⁻³ A·m²**. In a 0.20 T field at 30°, the torque is **1.57 × 10⁻⁴ N·m**. Turning it from aligned to anti-aligned takes 2μB = 6.28 × 10⁻⁴ J of work. This torque is the operating principle of a moving-coil meter and of a simple motor.

Far from a small loop, its field takes a dipole form. On the axis, B ≈ μ₀μ/(2πz³) for z ≫ R, which follows from the exact loop formula when z dominates R. For the single 0.5 A, 0.020 m loop at z = 0.20 m, the dipole estimate exceeds the exact value by about 1.5%. The field falls as 1/z³, much faster than a wire's 1/r. In a non-uniform field, a dipole also feels a net force toward stronger field when aligned, which is the basis of magnetic levitation demonstrations.

## Common mistakes

- Treating dB as pointing along r̂; the cross product makes it perpendicular to both dl and r̂.
- Using μ₀I/(2πd) for a short segment; it assumes an infinitely long straight wire.
- Applying Ampère's law where B is not symmetric on the loop, and dividing by the loop length anyway.
- Counting all of a thick wire's current as enclosed for a loop inside the wire.
- Expecting a net force on a current loop in a uniform field; the forces cancel, and only the torque remains.
- Forgetting the number of turns in μ = NIA, or using diameter instead of radius in the area.

## Worked example

**Problem.** A synthetic coil has 100 turns, a square cross-section of side 2.0 cm and current 0.05 A. It sits in a uniform 0.10 T field with its normal perpendicular to the field. Find the torque, the work needed to turn it from aligned to anti-aligned, and the field at the centre of one turn from Biot–Savart.

**Step 1: dipole moment.** A = (0.020)² = 4.0 × 10⁻⁴ m², so μ = 100 × 0.05 × 4.0 × 10⁻⁴ = 2.0 × 10⁻³ A·m².

**Step 2: torque.** At θ = 90°, τ = μB = 2.0 × 10⁻⁴ N·m, the maximum.

**Step 3: work.** 2μB = 4.0 × 10⁻⁴ J.

**Step 4: centre field of one turn.** Each side is a segment with half-length 0.010 m at distance 0.010 m. Four sides give 2√2 μ₀I/(πL) = 2√2 × 4π × 10⁻⁷ × 0.05/(π × 0.020) = 2.83 μT. All 100 turns together give about 283 μT, if the turns are close together.

**Step 5: check.** The coil's own centre field is about 0.3% of the 0.10 T external field, so treating the external field as unchanged by the coil is reasonable.

## Limits of this lesson

All currents, geometries and fields are synthetic. The analysis assumes steady currents, thin wires except where a uniform current density is stated, vacuum permeability and ideal geometries such as infinite wires, ideal toroids and uniform external fields. Magnetic materials, magnetization, time-varying fields and relativistic effects are not developed, and the far-field dipole form is stated only on the axis. Nothing here is an exposure limit, a device design or a safety assessment. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
