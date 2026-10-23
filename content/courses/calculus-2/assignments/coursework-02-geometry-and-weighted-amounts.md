# Assignment 2: geometry, coverage and weighted amounts

This open report combines the new surface-element derivation with the existing volume, parametric and radial-amount readings. It asks how a geometric element and its coverage determine the quantity computed. All coordinates and density profiles are normalized synthetic examples, not a measured distribution or device shape. Retain sketches, derivations, code and report locally; selected browser values are formative checkpoints rather than graded geometric proofs.

## Part A: a distinct straight generator

Rotate $y=1+2x$, $0\leq x\leq1$, about the x-axis. Identify the end radii, slope and slant length before selecting an integral. The slant length is $\sqrt5$, and the radii are one and three. The frustum lateral area is therefore $\pi(1+3)\sqrt5=4\pi\sqrt5$.

Derive the same result from $2\pi\int y\,ds$ and show why replacing $ds$ by $dx$ would miss the slope. The enclosed volume is separately $\pi\int_0^1(1+2x)^2dx=13\pi/3$. If both end disks belong to the requested boundary, the cap contribution is $10\pi$ and the total capped area is $4\pi\sqrt5+10\pi$.

Use one consistent coordinate length scale and restore the appropriate square or cube when interpreting dimensions. A request for lateral area, capped area or volume cannot be answered interchangeably by the same number. Label whether an axis segment contributes additional boundary area; the central axis itself has zero area, while the end disks do not.

## Part B: a different radial profile

On a disk of radius $R=3$, prescribe density $c(r)=10[1-(r/R)^4]$ in normalized amount per area. Write the annular element and integrate it explicitly. The total is $Q=60\pi$, while disk area is $9\pi$, so the area average is $20/3$.

Compare these with the center-density shortcut and with an unweighted radial average. State the different weighting and units of each expression. The same factor $2\pi r$ can appear in an annular area, a cylindrical shell or a surface of revolution; its partner differential determines which geometric object is actually represented.

Now find the radius containing one half of the total amount. Normalize $z=(r/R)^2$. The accumulated fraction is $F(z)=3z/2-z^3/2$. On $[0,1]$ it rises from zero to one; solving $F(z)=1/2$ gives the admissible root of $z^3-3z+1=0$. The radius fraction is approximately 0.58931855, not the radius obtained by simply halving R or the disk area.

Use a bracketed solve on the declared domain and verify the accumulated integral at the returned radius. The cubic has other algebraic roots, so an unconstrained root output needs an admissibility check. Distinguish a radius quantile of the weighted amount from the average density or the mean radius; those are different summaries.

## Part C: multiplicity is an independent boundary issue

Analyze the unit circle parameter map rotated about the x-axis. Compare the upper semicircle with the full circle. The upper semicircle generates the sphere once and gives area $4\pi$. The full circle is traversed once as a planar curve, but its upper and lower halves each generate that same sphere, making the swept-area integral $8\pi$.

Explain why using an absolute radius repairs negative area contributions but does not repair double coverage. Give a correct generating interval or describe an explicit multiplicity correction. Then compare the situation with the distinct frustum, whose generator covers the intended lateral surface once. A numerical integral cannot infer that geometric intention from the raw parameter limits.

## Part D: independent checks and numerical study

For the frustum, compare the exact geometric formula and direct quadrature. For the radial amount, change variables to z and compare with the original annular integral. For the half-amount radius, use bisection or another documented bracketed method and retain the endpoint residuals and stopping criterion.

Refine the quadrature grid and root tolerance independently. A tighter root solve does not correct a missing annular weight, and a finer integration grid does not correct a repeated surface map. Preserve at least one wrong-element or wrong-coverage calculation and the check that rejects it. State which conclusions follow from stipulated geometry and which would require a real measured density profile.

## Self-review and scope

The retained report should contain sketches, element/coverage definitions, exact lateral/volume/capped results, a weighted amount and average, an admissible quantile solve and refinement evidence. Browser checkpoints do not score those artifacts. [MIT OCW 18.01SC Fall 2010 Unit 3](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-3-the-definite-integral-and-its-applications/) and [Unit 4 Part B](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-4-techniques-of-integration/part-b-partial-fractions-integration-by-parts-arc-length-and-surface-area/) provide link-only area/volume/length/surface scope. All problems and explanations are original with substantial AI assistance. General multivariable surfaces belong to Calculus III; qualified review, broader coursework and measured workload remain open. No two-course MIT equivalence is claimed.
