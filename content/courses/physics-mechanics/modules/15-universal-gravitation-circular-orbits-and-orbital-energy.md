# Universal gravitation, circular orbits and orbital energy

The [circular-motion lesson](06-centrifuge-rotation-and-balance.md) required a net inward force of mv²/r for uniform circular motion and supplied it with a centrifuge rotor. Gravity can supply the same inward force on a planetary scale, which makes it a natural next application. So far this course has treated gravity as a constant downward force mg near a surface. This lesson replaces that with Newton's universal law, shows how the surface value g follows from it, and uses it to find the speed, period and energy of circular orbits. It also explains why mgh fails over large height changes, and why most of the energy needed to put an object in orbit goes into its speed rather than its height. The planet, satellites and constants are synthetic teaching values.

The undergraduate [MIT OCW 8.01SC Classical Mechanics (Fall 2016)](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/) introduces the universal law of gravitation in Week 2 (Lesson 5) and returns to it with an orbital circular-motion worked example in Week 3, alongside uniform circular motion. Its energy weeks then develop gravitational potential energy. This lesson follows that pairing within the local circular-motion week. It uses 8.01SC as a scope comparator only and reproduces no MIT material.

## Learning objectives

By the end of this lesson, you should be able to:

1. Apply Newton's law of universal gravitation, including the shell result, to find the gravitational force and the field strength g at a distance from a spherical body.
2. Calculate the speed and period of a circular orbit from the gravitational force, apply Kepler's third law for circular orbits, and find the radius for a given period.
3. Use gravitational potential energy U = −GMm/r to calculate the energy of a circular orbit, the energy to reach it, and the escape speed, and explain when mgh is an adequate approximation.

## The universal law

Any two point masses m₁ and m₂ a distance r apart attract each other with a force of magnitude

**F = G m₁ m₂ / r²,**

directed along the line joining them. This course stipulates G = 6.67 × 10⁻¹¹ N·m²/kg². The force is tiny for everyday masses: two 100 kg spheres with centres 1.0 m apart attract with only 6.7 × 10⁻⁷ N. It matters when one mass is planetary.

**The shell result.** A spherically symmetric body attracts an outside mass as if all its mass were concentrated at its centre. This makes planets tractable: r is measured from the centre, not the surface.

**Surface gravity.** Take a synthetic planet of mass M = 6.0 × 10²⁴ kg and radius R = 6.4 × 10⁶ m, so GM = 4.0 × 10¹⁴ m³/s². A mass m at the surface feels mg = GMm/R², so

**g = GM/R² = 9.77 m/s².**

The familiar constant g is therefore a local value. At a height equal to one planetary radius, r = 2R, the field falls to a quarter, **2.44 m/s²**. Near the surface, a height change h changes g by a fraction of only about 2h/R, so mg is an excellent approximation for heights much smaller than R.

## Circular orbits

A satellite moving in a circle of radius r around the planet has only gravity acting on it. Newton's second law in the inward direction is

GMm/r² = mv²/r, so **v = √(GM/r).**

The satellite's mass cancels, so every object at that radius moves at the same speed. For r = 7.0 × 10⁶ m, about 600 km above the synthetic surface, v = **7.56 km/s**. The period is T = 2πr/v = **5817 s**, about 97 min.

Eliminating v gives **Kepler's third law** for circular orbits:

**T² = (4π²/GM) r³.**

A larger orbit is slower and takes longer, with the period growing as r^(3/2). For a period of one synthetic day, 86 400 s, the radius is r = (GM T²/4π²)^(1/3) = **4.23 × 10⁷ m**, about 6.6 planetary radii. Kepler stated the law for elliptical orbits using the semi-major axis; this lesson treats only the circular case.

A satellite in orbit is in free fall: gravity is the only force, and it bends the path into a circle. Astronauts feel weightless not because gravity is absent but because they and their spacecraft fall together. At 600 km the field is still about 84% of its surface value.

## Gravitational potential energy

Because gravity weakens with distance, the work it does is not mgh over large distances. The potential energy of m at distance r from M, taking zero at infinite separation, is

**U(r) = −GMm/r.**

It is negative because work must be done to separate the masses to infinity. The change between r₁ and r₂ is GMm(1/r₁ − 1/r₂), which reduces to mgh when h = r₂ − r₁ is small compared with r₁.

**Energy of a circular orbit.** The kinetic energy is ½mv² = GMm/(2r). Adding U gives

**E = −GMm/(2r),**

so the kinetic energy equals −E, and U = 2E. Moving to a higher circular orbit raises the total energy, even though the satellite moves more slowly.

**Synthetic example.** Put a 1000 kg satellite from rest on the surface into the 7.0 × 10⁶ m orbit, ignoring the planet's rotation and air. The required energy is GMm(1/R − 1/(2r)) = **3.39 × 10¹⁰ J**. Only 5.4 × 10⁹ J of that is the gain in potential energy, and the remaining 2.86 × 10¹⁰ J is orbital kinetic energy. Using mgh with the surface g would give 5.9 × 10⁹ J for the height alone, about 9% too large even for this modest altitude.

**Escape speed.** An object launched with total energy zero just reaches infinity with no speed left. Setting ½mv² − GMm/R = 0 gives **v_esc = √(2GM/R) = 11.2 km/s** from the synthetic surface. This is √2 times the speed of a circular orbit at the same radius, and it does not depend on launch direction, ignoring air and obstacles.

## Common mistakes

- Measuring r from the surface instead of from the planet's centre.
- Using mgh for height changes comparable with the planet's radius.
- Including the satellite's mass in the orbital speed; it cancels.
- Adding a separate centripetal force to the free-body diagram; gravity is the centripetal force.
- Treating negative potential energy as an error; it reflects the choice of zero at infinity.
- Thinking a higher orbit needs less energy because it is slower; the total energy is higher.
- Assuming astronauts in low orbit are beyond gravity's reach.

## Worked example

**Problem.** A 500 kg synthetic satellite orbits the same planet in a circle of radius 8.0 × 10⁶ m. Find its speed, period, total energy, the energy needed to place it there from rest on the surface, and the escape speed from that orbit.

**Step 1: speed.** v = √(4.0 × 10¹⁴/8.0 × 10⁶) = 7.07 km/s.

**Step 2: period.** T = 2πr/v = 7107 s, about 118 min. Check with Kepler: (8.0/7.0)^(3/2) × 5817 s gives the same value.

**Step 3: orbital energy.** E = −GMm/(2r) = −1.25 × 10¹⁰ J.

**Step 4: energy to reach it.** GMm(1/R − 1/(2r)) = 1.88 × 10¹⁰ J, ignoring rotation, air and the energy cost of the launch vehicle.

**Step 5: escape from orbit.** √(2GM/r) = 10.0 km/s, so the satellite needs a further 2.93 km/s if the boost is applied along its motion.

## Limits of this lesson

All masses, radii and constants are synthetic except the stipulated G. The analysis treats spherically symmetric bodies, a stationary non-rotating planet, circular orbits, no atmosphere and two bodies only. Elliptical orbits and Kepler's first and second laws in full, orbital transfers, tides, rotating frames, many-body effects and relativistic corrections are not developed. Nothing here is mission design, a launch requirement or a spacecraft specification. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
