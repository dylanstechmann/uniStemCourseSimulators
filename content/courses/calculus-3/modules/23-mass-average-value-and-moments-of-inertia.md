# Applications of multiple integrals: mass, average value and moments of inertia

The [multiple-integrals lesson](10-multiple-integrals-and-jacobian-measures.md) set bounds from a region, changed coordinates with the Jacobian and used a density to total a quantity, as in the annulus whose average density was checked against its extremes. This lesson uses the same tools for three standard applications. The first is the total mass and center of mass of a plate or solid whose density varies. The second is the average value of a function over a region. The third is the **moment of inertia**, which measures how strongly a body resists being spun about an axis and which the [rotation lessons](../../physics-mechanics/modules/10-torque-angular-momentum-and-rolling.md) of the Mechanics course use without deriving. All densities, dimensions and masses here are synthetic.

[MIT OCW 18.02SC Multivariable Calculus (Fall 2010)](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/3.-double-integrals-and-line-integrals-in-the-plane/part-a-double-integrals/) gives Unit 3 Part A sessions to "Applications: Mass and Average Value" and "Applications: Moment of Inertia", and [Unit 4 Part A](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/4.-triple-integrals-and-surface-integrals-in-3-space/part-a-triple-integrals/) has "Applications and Examples" for triple integrals. The [Harvard Math 21a (Summer 2003) lecture plan](https://abel.math.harvard.edu/~knill/teaching/summer2003/syllabus.html) names double, triple and surface integrals but no applications by title. Both are link-only scope comparators; no text, figure or problem is reproduced.

## Learning objectives

By the end of this lesson, you should be able to:

1. Set up and evaluate integrals for the mass, the first moments and the center of mass of a plate or solid with variable density, and for the average value of a function over a region.
2. Set up the moment of inertia I = ∬ d²δ dA about a stated axis, evaluate it in rectangular and polar coordinates, and apply the parallel-axis theorem.
3. Use symmetry, weighting and bounds to predict and check where a center of mass lies and which of two bodies of equal mass has the larger moment of inertia.

## Mass and center of mass

A thin plate occupying a region D, with area density δ(x, y) in kg/m², has mass

\[
M = \iint_D \delta\,dA .
\]

The **first moments** weight position by mass: M_y = ∬ x δ dA about the y-axis and M_x = ∬ y δ dA about the x-axis. The **center of mass** is the density-weighted average position,

\[
\bar x = \frac{M_y}{M},\qquad \bar y = \frac{M_x}{M}.
\]

For a solid with volume density δ(x, y, z), replace dA by dV and include z̄ = (1/M)∭ z δ dV.

Take the plate 0 ≤ x ≤ 4, 0 ≤ y ≤ 2 (metres) with δ = 1 + x/2 kg/m², which is denser toward the right edge. The mass is M = ∫₀²∫₀⁴(1 + x/2) dx dy = 2·8 = 16 kg. The first moment about the y-axis is M_y = 2·∫₀⁴(x + x²/2) dx = 2·(8 + 32/3) = 112/3, so x̄ = (112/3)/16 = 7/3 = 2.33 m. That is to the right of the geometric center at x = 2, as expected for a density that grows with x. The density does not depend on y, so ȳ = 1.00 m, the middle of the plate's height.

Two checks apply to every center of mass. It must lie within the extreme coordinates of the body, here 0 ≤ x̄ ≤ 4, and it shifts toward the denser side. If both the region and the density are symmetric about a line, the center of mass lies on that line.

## Average value

The average value of a function f over a region D of area A is

\[
\bar f = \frac{1}{A}\iint_D f\,dA .
\]

For f = x² + y over the triangle 0 ≤ y ≤ x ≤ 2, the integral is ∫₀²∫₀ˣ(x² + y) dy dx = ∫₀²(x³ + x²/2) dx = 4 + 4/3 = 16/3. The triangle has area 2, so the average is 8/3 = 2.67. The check is that an average lies between the least and greatest values of f on the region: f ranges from 0 at the origin to 6 at (2, 2), and 2.67 lies between them. Total mass is an average density times area, M = δ̄A, so the first moments divided by M are averages of position weighted by density.

## Moment of inertia

A bit of mass dm at distance d from a chosen axis contributes d² dm to the **moment of inertia** about that axis:

\[
I = \iint_D d^2\,\delta\,dA .
\]

About the z-axis, perpendicular to a plate in the xy-plane, d² = x² + y². For the plate above,

I_z = ∬(x² + y²)(1 + x/2) dA = 2·∫₀⁴x²(1 + x/2) dx + ∫₀⁴(1 + x/2) dx·∫₀²y² dy = 2·(160/3) + 8·(8/3) = 128 kg·m².

In polar coordinates the factor r from the Jacobian multiplies the d² = r² already present. For a uniform disk of radius R and mass M = δπR²,

I = ∫₀^(2π)∫₀^R r²·δ·r dr dθ = δ·2π·R⁴/4 = ½ M R².

Now let the density grow outward, δ = kr, with k = 12 kg/m³ and R = 0.5 m. The mass is M = ∫₀^(2π)∫₀^R kr·r dr dθ = 2πkR³/3 = π = 3.14 kg, and the moment is I = ∫₀^(2π)∫₀^R r²·kr·r dr dθ = 2πkR⁵/5 = 0.15π = 0.471 kg·m². Then I/(MR²) = 0.6, compared with 0.5 for a uniform disk of the same mass and radius, because the weighted disk puts more of its mass farther from the axis. For any disk of mass M and radius R, 0 ≤ I/(MR²) ≤ 1, and the upper limit is reached by a thin ring with all its mass at the rim.

**The parallel-axis theorem.** If an axis passes through the center of mass, and a second axis parallel to it lies a distance d away, then

I = I_cm + M d².

For the rectangular plate, d² = x̄² + ȳ² = 49/9 + 1 = 58/9 measures how far the center of mass is from the z-axis through the origin. So I_cm = 128 − 16·(58/9) = 24.9 kg·m². The moment about the center of mass is much smaller, since that is the axis about which the mass is closest.

**A solid.** Take a solid cylinder of radius 0.1 m and height 0.4 m whose density grows with height, δ = 1000(1 + z/0.4) kg/m³. The mass is M = ∫₀^0.4 1000(1 + z/0.4)·π(0.1)² dz = 1000·π·0.01·0.6 = 18.85 kg. The center of mass height is z̄ = ∫z δ dz/∫δ dz = 5h/9 = 0.222 m, above the mid-height 0.2 m, because the top is denser. The moment about the cylinder's own axis is I = ∭ r²δ dV = ½ M R² = 0.0942 kg·m². The density's dependence on z does not matter for this axis: only the distance from the axis enters d², so the same formula as for a uniform cylinder holds.

## Common mistakes

- Integrating the area or volume when the mass is needed, by leaving out the density.
- Dividing a first moment by the area instead of by the mass.
- Using the distance d instead of d², or x instead of x² + y², in a moment of inertia.
- Omitting the Jacobian factor r in polar coordinates.
- Applying the parallel-axis theorem from an axis that does not pass through the center of mass.
- Averaging a function over a region larger than the one named, or forgetting to divide by its area.

## Worked example

**Problem.** A uniform semicircular plate of radius R = 0.6 m has mass 5.0 kg and lies in the half-plane y ≥ 0 with its straight edge on the x-axis, centered on the origin. Find ȳ, the moment of inertia about the z-axis through the origin, and the moment about the parallel axis through the center of mass.

**Step 1: density.** The area is πR²/2, so δ = 2M/(πR²) = 10/(π·0.36) = 8.84 kg/m².

**Step 2: center of mass.** By symmetry x̄ = 0. In polar coordinates, with 0 ≤ θ ≤ π and 0 ≤ r ≤ R, M_x = ∬ yδ dA = δ∫₀^π sin θ dθ·∫₀^R r²dr = δ·2·R³/3. Dividing by M = δπR²/2 gives ȳ = 4R/(3π) = 2.4/9.42 = 0.255 m.

**Step 3: moment about the origin.** I = δ∫₀^π∫₀^R r²·r dr dθ = δπR⁴/4 = ½ M R² = 0.90 kg·m². A half-disk has half the mass and, by symmetry, half the moment of the whole disk, so I/(MR²) is the same 1/2 as for a whole uniform disk.

**Step 4: parallel axis.** The center of mass is a distance ȳ from the origin axis, so I_cm = I − Mȳ² = 0.90 − 5.0·(0.2546)² = 0.90 − 0.324 = 0.576 kg·m².

**Step 5: check.** The center of mass lies on the symmetry axis and inside the plate. It is below the mid-height R/2 = 0.3 m, as it should be for uniform density: the half-disk is wider near its straight edge than near its top, so its average height is less than half its greatest height. And I_cm is smaller than I, as the parallel-axis theorem requires, since Mȳ² > 0.

## Limits of this lesson

All densities, plates, solids and masses are synthetic mathematical models. The treatment covers thin plates and solids with a stated density, and moments about axes whose distance formula is given. The full inertia tensor, products of inertia, principal axes and gravitational attraction between extended bodies are not developed. Nothing here is a design value for any real object. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
