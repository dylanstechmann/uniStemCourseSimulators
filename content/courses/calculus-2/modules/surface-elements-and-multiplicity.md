# Surface elements, rotation and multiplicity

The geometry reading develops disks, shells, parametric length and weighted radial amounts. Surface area needs a different small element: a slanted strip, not a disk or a vertical rectangle. This original extension derives a surface-of-revolution integral and checks what happens when its parameter map covers a surface more than once. Coordinates below are normalized to a common length scale; restore its square for area and cube for volume. No geometric example describes a real tissue or device.

## Derive the lateral element from a frustum

Approximate a smooth nonnegative graph $y=f(x)$ by a short line segment. Rotating that segment around the x-axis produces a conical frustum. Its lateral area is the average of the two end circumferences times the slant length: $\pi(r_1+r_2)\Delta s$. As the partition is refined, the radii approach the local value $y$ and the slant length approaches $ds=\sqrt{1+(y')^2}\,dx$. Therefore

$$S_{lateral}=2\pi\int_a^b y(x)\sqrt{1+(y'(x))^2}\,dx.$$

The radius contributes one length and the arc element another, so the result has area dimensions. A disk-volume integrand $\pi y^2dx$ has a different geometric role and dimensions. Replacing $ds$ by $dx$ would ignore the slope and generally underestimate the lateral area for a nonconstant graph.

For a smooth parametric generating curve, use

$$S_{lateral}=2\pi\int_{t_0}^{t_1}|y(t)|\sqrt{(x'(t))^2+(y'(t))^2}\,dt$$

when rotating about the x-axis. The absolute value is the nonnegative distance to the axis. Rotation about the y-axis instead uses $|x(t)|$. These formulas count the surface swept by the parameter map with its multiplicity. To obtain a geometric surface area, verify that the intended surface is covered once apart from negligible seams or endpoint degeneracy.

## Lateral area, end caps and volume

A worked straight segment is $y=1+x$, $0\leq x\leq1$. Its slant length is $\sqrt2$, and the frustum lateral area is $2\pi\sqrt2\int_0^1(1+x)dx=3\pi\sqrt2$. The same result follows from end radii one and two and slant length $\sqrt2$. This provides a geometric check independent of evaluating the integral.

If the intended object includes both circular end caps, add $\pi(1^2+2^2)=5\pi$. If the request is lateral area only, those caps do not belong in the answer. The enclosed volume is separately $\pi\int_0^1(1+x)^2dx=7\pi/3$. Three quantities describe the same outline but use different elements and boundaries.

The distinct rehearsal uses $y=2+x$, $0\leq x\leq2$. Slant length is $2\sqrt2$ and lateral area is $12\pi\sqrt2$. End radii two and four give cap sum $20\pi$, so the capped surface is $12\pi\sqrt2+20\pi$. Volume is $56\pi/3$. Sketch the boundaries and compare units before calculating decimals; a plausible-looking number can answer the wrong geometric question.

## A curve can be traced once while its rotated surface is covered twice

Take the unit circle $x=\cos t,y=\sin t$. Its parameter speed is one. The upper semicircle $0\leq t\leq\pi$, rotated around the x-axis, covers the unit sphere once. The formula gives $2\pi\int_0^\pi\sin t\,dt=4\pi$.

Using the full circle $0\leq t\leq2\pi$ and the nonnegative radius gives $2\pi\int_0^{2\pi}|\sin t|dt=8\pi$. The full planar circle is traversed once, but its upper and lower halves each generate the same sphere. The rotation map covers the sphere twice. The result is a multiplicity-weighted swept area, not twice as much distinct spherical surface.

Dropping the absolute value would instead produce zero from signed cancellation, which is also not the geometric area. The correct repair is to choose a generating interval covering the intended surface once, or otherwise account for the multiplicity explicitly. A sign correction alone cannot determine coverage.

## Numerical and limiting checks

Compare integral values for straight generators with the exact frustum formula. Refine a piecewise-linear approximation and distinguish its lateral area from endpoint caps. For a parametric curve, preserve both derivatives in the speed factor and inspect stationary points or repeated sections. A numerical integrator cannot infer the intended geometric multiplicity from an input interval.

For nonnegative radius and speed, the lateral integrand is nonnegative. If the generating curve lies between radii $r_{min}$ and $r_{max}$ and has length $L$, the bounds $2\pi r_{min}L\leq S\leq2\pi r_{max}L$ provide a scale check under the same coverage interpretation. The straight rehearsal satisfies these bounds. They do not certify the exact area or resolve a repeated parameter map.

## Connection and scope

The existing radial-density reading uses annular area to weight an amount; it should not be replaced by a surface-of-revolution element merely because both contain $2\pi r$. Identify whether the radius is multiplying a radial width, an arc length or an axial shell height. The next geometry report combines these distinctions without conflating their units.

[MIT OCW 18.01SC Fall 2010 Unit 4 Part B](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-4-techniques-of-integration/part-b-partial-fractions-integration-by-parts-arc-length-and-surface-area/) lists arc length and surface area after integration techniques. This is a link-only scope comparator. All examples and explanations here are original and AI-assisted; no source problem or figure is imported. General multivariable surface Jacobians belong to Calculus III. Qualified review, broader coursework and measured workload remain open; the paired Calculus I/II packages divide one comparator and do not establish two-course equivalence.
