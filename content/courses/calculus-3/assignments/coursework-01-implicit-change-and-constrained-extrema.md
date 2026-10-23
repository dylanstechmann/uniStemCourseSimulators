# Assignment 1: implicit change and constrained extrema

This open report connects a local graph, finite change, an error bound and a separate global constrained optimization. All equations and coordinates are invented mathematical inputs. Retain derivations, plots, code and report locally; selected browser responses do not grade the full proof or implementation. State branch and domain conditions before differentiating rather than using an algebraic derivative as a global existence claim.

## Part A: a distinct upper graph

Use F(x, y, z)=z²+xy−four=zero with positive branch z=sqrt(4−xy). At the base point (2, 1, sqrt2), Fz=2sqrt2 is nonzero. Calculate zx=-one/(two sqrt2)and zy=-one/sqrt2 through the original implicit identity, and verify them by differentiating the explicit square root.

Consider the finite displacement dx=0.1, dy=-0.05. The two linear contributions cancel, so the tangent prediction remains sqrt2. The exact new point has xy=1.995 and z=sqrt2.005, about 1.4159802. Its difference from the tangent prediction is about 0.00176666. A zero first-order change does not prove that the function is constant along the finite displacement.

Substitute both the base and new coordinates into the original relation. Compare the selected upper branch with the negative square-root branch and state why the given base point identifies which local graph is intended. Both branches can satisfy the same polynomial equation without belonging to the same selected neighborhood.

## Part B: certify a bounded remainder

Use the box 1.9<=x<=2.1, 0.9<=y<=1.1. Throughout it, z is at least 1.3 on the upper branch. Derive the second derivatives and bound their magnitudes using that lower denominator and the largest coordinate products in the box.

One componentwise bound is |zxx|<=1.21/(four times 1.3³), |zyy|<=4.41/(four times 1.3³), and |zxy|<=one/(two times 1.3)+2.31/(four times 1.3³). Use their Frobenius norm to justify the simpler operator-norm bound M=two. The line segment for the supplied displacement stays in the box.

The first-order Taylor remainder is therefore bounded by M times(dx²+dy²)/two=0.0125. Compare that conservative guarantee with the smaller actual error. A Hessian evaluated only at the base point would not establish the same uniform bound. Numerical agreement at a few samples is also distinct from bounding every denominator and numerator over the box.

For an independent numerical check, rationalize the small root difference as 0.005 divided by [sqrt2.005+sqrt2]. This avoids subtracting two nearly equal numbers while preserving the same exact value. Compare both evaluations at the working precision, and keep display rounding separate from the mathematical Taylor bound. A small original-constraint residual and a small approximation error are different checks and should be labeled separately.

## Part C: a separate global constraint

Now restrict x, y>=zero and x+y=three, still using the same upper relation. This is a different comparison from the preceding local displacement. Parameterize by y=three−x with x in[0, 3], then analyze z=sqrt[4−x(three−x)].

The maximum is two at the two endpoints (0, 3)and(3, 0). The minimum is sqrt7/two at x=y=1.5. Derive the interior stationary point and compare it with both endpoints. A multiplier calculation that returns only the interior candidate would miss the global maximum.

Verify that the selected branch remains positive and regular on this whole segment. Local regularity supports the derivative, but compactness and the boundary comparison support the global extrema. These are different logical steps. Count the two maximizing points explicitly rather than treating the maximum value as the number of solutions.

## Part D: verification and interpretation

Plot or describe the upper branch along the constrained segment and the local displacement path separately. Label normalized coordinates and distinguish tangent approximation, actual change and certified bound. Refine any numerical calculation independently of the analytic domain argument.

Compare with the foundation's fold curve, where a convenient graph coordinate fails while the curve remains regular. Explain why Fz=zero alone is not a universal proof of absent differentiability, and why a nonzero Fz supplies only local rather than global uniqueness. Retain one explicit counterexample or coordinate change supporting each distinction.

Your report should contain original constraint residuals, branch selection, implicit and explicit derivatives, regional Hessian bounds, global candidate list and independent checks. [MIT OCW 18.02SC Fall 2010 Unit 2](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/2.-partial-derivatives/) is link-only constrained-differential/optimization scope. All explanations and problems are original and AI-assisted; no source proof, exercise, figure, code or data is imported. General global implicit theory, measured workload and qualified review remain open; the course stays partial and unreviewed.
