# Center of mass, parallel axes and the energy of a system

The [momentum and collision lesson](03-momentum-collisions-and-impulse.md) and the [system-boundaries lesson](09-work-momentum-and-system-boundaries.md) treated a group of bodies through its total momentum, and the [rotation lesson](10-torque-angular-momentum-and-rolling.md) used moments of inertia for standard shapes. Two pieces were missing. One is the single point that represents a system's translation, the **center of mass**. The other is the rule for moving a moment of inertia to a different axis, the **parallel-axis theorem**. Together they split a body's kinetic energy into a part carried by the center of mass and a part due to spin, which is what rolling and swinging bodies use. All masses, lengths and speeds here are synthetic, and g = 9.81 m/s² is stipulated.

[MIT OCW 8.01SC Classical Mechanics (Fall 2016)](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/week-5-momentum-and-impulse/) has a Week 5 lesson on the "Center of Mass and Motion of the Center of Mass", and its [Week 10 lesson on the moment of inertia](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/week-10-rotational-motion/) includes a derivation of the parallel-axis theorem. [Open Yale Courses PHYS 200, Lecture 8](https://oyc.yale.edu/physics/phys-200/lecture-8) has a chapter on the center of mass, and [Lecture 10](https://oyc.yale.edu/physics/phys-200/lecture-10) is titled for the parallel-axis theorem. Both are link-only scope comparators; no text, figure or problem is reproduced.

## Learning objectives

By the end of this lesson, you should be able to:

1. Locate the center of mass of discrete and continuous one-dimensional systems, and use M a_cm = F_ext and P = M v_cm.
2. Separate a system's kinetic energy into a center-of-mass part and a relative part, and use the split to find the energy lost in a perfectly inelastic collision.
3. Compute the moments of inertia of rods and disks, derive and apply the parallel-axis theorem, and split a rolling or swinging body's energy into translation and spin.

## The center of mass

For particles of mass mᵢ at positions rᵢ, the center of mass is the mass-weighted average position,

\[
\vec R_\text{cm} = \frac{\sum m_i \vec r_i}{M},\qquad M = \sum m_i .
\]

A synthetic three-segment limb has masses 2.0, 1.2 and 0.4 kg at 0.15, 0.40 and 0.60 m along its length. Then x_cm = (2.0·0.15 + 1.2·0.40 + 0.4·0.60)/3.6 = 1.02/3.6 = 0.283 m. It lies between the extreme positions and nearer the heavy segment.

For a continuous body the sum becomes an integral, and the center of mass is the weighted average of position that the [Calculus II averages lesson](../../calculus-2/modules/22-averages-weighted-averages-and-probability-densities.md) defines,

\[
x_\text{cm} = \frac{\int x\,\lambda(x)\,dx}{\int \lambda(x)\,dx},
\]

with linear density λ. A uniform rod has x_cm = L/2. A rod on 0 ≤ x ≤ 1.0 m with λ = 1.5 + 2x kg/m has M = 1.5 + 1.0 = 2.5 kg, and x_cm = (0.75 + 0.667)/2.5 = 0.567 m, beyond its midpoint because it is denser toward x = 1. The [multivariable lesson](../../calculus-3/modules/23-mass-average-value-and-moments-of-inertia.md) extends the integrals to plates and solids. The center of mass need not lie inside a body: a ring's lies at its empty center.

## Motion of the center of mass

Add Newton's second law over all the particles of a system. The internal forces occur in equal and opposite pairs by the third law, so they cancel in the sum, leaving

\[
M\,\vec a_\text{cm} = \vec F_\text{ext},\qquad \vec P = \sum m_i \vec v_i = M\,\vec v_\text{cm}.
\]

A system's center of mass accelerates as if all the mass sat there and only the external forces acted. Two blocks of 2.0 and 6.0 kg joined by a spring on a frictionless table, with a 16 N external force along the spring on the heavier block, have a_cm = 16/8.0 = 2.0 m/s² however the spring stretches and oscillates.

With no external force, v_cm is constant. Two skaters of 60 and 40 kg stand at rest on frictionless ice at x = 0 and x = 1.0 m, so x_cm = 40/100 = 0.40 m. They push apart. Since the total momentum stays zero, if the 60 kg skater moves at −2.0 m/s the other moves at +3.0 m/s. After 1.0 s their positions are −2.0 m and 4.0 m, and x_cm = (60·(−2.0) + 40·4.0)/100 = 0.40 m, unchanged. However hard they push, internal forces cannot move the center of mass.

## The center-of-mass frame and collisions

In a frame that moves with the center of mass, the total momentum is zero. The kinetic energy of any system then splits as

\[
K = \tfrac12 M v_\text{cm}^2 + K_\text{rel},
\]

and for two bodies K_rel = ½μ v_rel², with the reduced mass μ = m₁m₂/(m₁ + m₂) and v_rel the relative speed. The first term cannot be changed by internal forces or collisions.

A 2.0 kg body at 3.0 m/s strikes a 1.0 kg body at rest. The center of mass moves at v_cm = 6.0/3.0 = 2.0 m/s. The total kinetic energy is ½·2.0·3.0² = 9.0 J, of which ½·3.0·2.0² = 6.0 J belongs to the center-of-mass motion. The rest is K_rel = ½(2/3)(3.0²) = 3.0 J. A perfectly inelastic collision, in which the bodies move together at v_cm, loses exactly K_rel, leaving 6.0 J. A perfectly elastic collision reverses each velocity in the center-of-mass frame, so v₁′ = 2v_cm − v₁ = 1.0 m/s and v₂′ = 2v_cm − 0 = 4.0 m/s, which keeps the momentum 6.0 kg·m/s and the energy 9.0 J.

## Moments of inertia and the parallel-axis theorem

About a stated axis, I = Σ mᵢrᵢ², where rᵢ is the perpendicular distance to the axis. Two standard results, which integrals give, are I = ML²/12 for a uniform rod about its center and perpendicular to it, and I = ½MR² for a uniform disk or cylinder about its axis.

Suppose a second axis lies a distance d from a parallel axis through the center of mass. Write each particle's position relative to the center of mass as r′ᵢ, so its squared distance from the second axis is |d + r′ᵢ|² in the plane of rotation. Summing with weights,

\[
I = \sum m_i\,|\vec d + \vec r_i'|^2 = M d^2 + 2\,\vec d\cdot\sum m_i \vec r_i' + I_\text{cm} = I_\text{cm} + M d^2 ,
\]

because Σ mᵢr′ᵢ = 0 by the definition of the center of mass. This is the **parallel-axis theorem**. Since M d² ≥ 0, the axis through the center of mass has the smallest moment of inertia of all parallel axes.

For a uniform rod about one end, d = L/2, so I = ML²/12 + M(L/2)² = ML²/3, which is four times the center value. For a uniform disk about a point on its rim, I = ½MR² + MR² = (3/2)MR². For a 0.80 kg rod of length 0.50 m, I_cm = 0.01667 kg·m² and I_end = 0.06667 kg·m², and summing 4000 thin slices numerically gives the same two values. The theorem applies only from an axis through the center of mass: to move between two other axes, go through the center of mass.

## The energy of a body: translation plus spin

The same split holds for a rigid body that moves and spins, with the spin measured about the center of mass:

\[
K = \tfrac12 M v_\text{cm}^2 + \tfrac12 I_\text{cm}\,\omega^2 .
\]

A solid disk of mass 2.0 kg and radius 0.10 m rolls without slipping at v_cm = 1.5 m/s, so ω = v_cm/R = 15 rad/s. Its translational energy is ½·2.0·1.5² = 2.25 J, and its spin energy is ½(½MR²)ω² = ½(0.0100)(225) = 1.125 J, so K = 3.375 J = ¾Mv_cm². One third of the energy is rotational. As a check, take the rotation about the contact point, which is momentarily at rest: I_contact = ½MR² + MR² = (3/2)MR², and K = ½(3/2)MR²ω² = ¾Mv_cm², the same value. The parallel-axis theorem and the energy split agree.

## Common mistakes

- Using the geometric midpoint instead of the mass-weighted position.
- Letting internal forces enter M a_cm = F_ext; they cancel in pairs.
- Expecting the center of mass to lie inside the body.
- Applying I = I_cm + Md² between two axes that do not pass through the center of mass.
- Measuring d to the center of mass from a point instead of taking the perpendicular distance between parallel axes.
- Dropping ½Mv_cm² for a rolling or swinging body.
- Treating all of the initial kinetic energy as lost in a perfectly inelastic collision; the center-of-mass part survives.

## Worked example

**Problem.** A uniform rod of mass 0.80 kg and length 0.50 m is pivoted at one end and released from rest in a horizontal position. Find its moment of inertia about the pivot, its angular speed when it first hangs vertically, and the speeds of its center and tip, then check the energy split.

**Step 1: moment of inertia.** I_cm = ML²/12 = 0.01667 kg·m², and by the parallel-axis theorem I_pivot = 0.01667 + 0.80·(0.25)² = 0.06667 kg·m².

**Step 2: angular speed.** The center of mass falls L/2 = 0.25 m, releasing Mg(L/2) = 0.80·9.81·0.25 = 1.962 J, which becomes ½I_pivotω². So ω = √(2·1.962/0.06667) = 7.672 rad/s.

**Step 3: speeds.** The center of mass moves at v_cm = ωL/2 = 1.918 m/s, and the tip at ωL = 3.836 m/s.

**Step 4: check.** ½Mv_cm² = ½·0.80·1.918² = 1.4715 J and ½I_cmω² = ½·0.01667·7.672² = 0.4905 J, which sum to 1.962 J, the energy released. A numerical integration of the torque equation for the swing gives the same angular speed at the vertical.

## Limits of this lesson

All bodies are synthetic, rigid and treated as point-mass sums or one-dimensional integrals for rods; plates and solids are developed in the multivariable lesson. The lesson covers rotation about fixed or center-of-mass axes in a plane. The full inertia tensor, precession and gyroscopes are not developed, and the limb segments carry no anatomical measurements. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
