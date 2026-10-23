# Implicit branches and local surface charts

Differentiating a constraint supplies a candidate derivative, but it also requires a branch and a usable coordinate chart. The earlier held-variable reading tracks differential constraints. This original foundation makes local graph assumptions explicit, derives second derivatives and distinguishes a failed chart from a singular geometric object. All fields and paths are synthetic mathematics, not measured surfaces.

## When an equation defines a local graph

Suppose a continuously differentiable F(x, y, z) vanishes at a point and Fz is nonzero there. The implicit-function theorem supplies a locally unique differentiable graph z=g(x, y) through that point. Differentiating F(x, y, g(x, y))=zero gives gx=−Fx/Fz and gy=−Fy/Fz, evaluated on the graph.

The result is local: it does not select a unique branch across an entire domain or prove every input has a solution. A zero Fz means this sufficient theorem condition fails; it does not by itself prove that no differentiable graph exists under every possible equation. Examine the actual relation and other coordinates before drawing a stronger conclusion.

If a smooth surface has nonzero full gradient but Fz=zero, another coordinate may provide a chart. For the unit sphere at its equator, the upper-z graph becomes problematic while the sphere itself remains smooth. Chart failure and geometric singularity are different statements.

## Worked upper-sphere chart

Use F=x²+y²+z²−one and positive branch z=sqrt(1−x²−y²). At (0.6, 0, 0.8), its slopes are gx=-0.75 and gy=zero. A graph parameterization (x, y, g) has area-vector element (-gx, -gy, one)dxdy, so its scalar area factor is sqrt(1+gx²+gy²)=1.25.

This factor is not another coordinate-area Jacobian for a flat region. It converts projected planar area to graph surface area. Flux can instead use the oriented area vector directly; multiplying that vector by the same scalar factor again would double-count the geometric measure.

## Distinct rehearsal and second derivatives

For the rehearsal use sphere point (one third, two thirds, two thirds). The first slopes are -one half and -one, and the scalar graph factor is three halves. Differentiate the original identity again rather than treating a denominator as constant.

For the upper sphere,

$$g_{xx}=-1/z-x^2/z^3, \qquad g_{xy}=-xy/z^3, \qquad g_{yy}=-1/z-y^2/z^3.$$

At the rehearsal point these are -15/8, -3/4 and -three. Directly differentiating the explicit square root gives an independent check on the implicit calculation. A derivative evaluated at one point does not establish a bound over an entire neighborhood; a Taylor remainder guarantee still needs a valid regional bound.

For a path through this point with xdot=0.1 and ydot=0.05, the graph derivative is zdot=gx xdot+gy ydot=-0.1. The three-dimensional speed is 0.15. Its velocity is perpendicular to the sphere's normal at this instant, as differentiating F=zero requires. This tangency condition concerns the constraint, not a claim that the curve has zero spatial motion.

## A fold exposes local and global distinctions

Use a separate curve F(x, y)=y³−3y+x=zero. At (0, 0), Fy=-three, so the selected local branch has yprime=one third. At the same x=zero, there are three real solutions y=zero and plus/minus sqrt3. Local uniqueness near one selected point does not erase the other distant branches.

At (2, 1), Fy=zero while Fx=one. Solving in the other direction gives x=3y−y³, which has a local maximum two at y=one. The explicit fold has two nearby y values on one side and none on the other; it cannot define one differentiable y(x) graph over a full neighborhood of x=two. The curve is nevertheless regular because the full gradient is nonzero.

Here the algebraic fold supports the stronger graph-failure conclusion. The vanished partial alone would not: a different relation such as (y−x)³=zero has the graph y=x despite a singular defining gradient. Distinguish a geometric object, its defining equation and the hypotheses of a particular theorem.

## Verification and scope

Retain the point, branch, held variables, nonvanishing condition, derivatives and independent substitution. Compare explicit and implicit differentiation where both are available, and verify a path derivative against the original constraint. Coordinate charts can support surface integrals and constrained optimization, but they do not supply global extrema or all boundary comparisons automatically.

[MIT OCW 18.02SC Fall 2010 Unit 2](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/2.-partial-derivatives/) and its constrained-differential scope are link-only comparators. This selected local-branch/fold extension clarifies those operations without claiming general manifold theory. All explanations, points and problems are original and AI-assisted; no source proof, problem, figure or data is imported. Broader analysis, measured workload and qualified review remain open; the course stays partial and unreviewed.
