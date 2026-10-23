# Assignment 2: nonlinear transforms and coverage evidence

This open report compares a nonlinear one-to-one coordinate map with a polynomial map that covers its image three times. It requires bounds, inverse information and independent target-region integrals, not merely a determinant. All domains and densities are synthetic normalized mathematics. Retain diagrams, derivations, code and report locally; selected browser fields do not evaluate the full geometric argument.

## Part A: transform a wedge explicitly

Use x=u v, y=v on one<=u<=two, one<=v<=three. Compute the derivative matrix and determinant v. Because v is positive, the local orientation is preserved. The inverse is v=y, u=x/y on this domain, so the map is also globally one-to-one here.

Describe the physical region as one<=y<=three, y<=x<=two y. Calculate area by both coordinate systems. It is four. For density f=x/y, the total is six and the area-average density is 1.5. The average lies between its minimum one and maximum two, providing a separate weighting check.

At (u, v)=(1.5, 2), the determinant is two. That pointwise value does not replace the variable factor v in the full integral. Treating the entire domain as though its local Jacobian were constant would define a different measure and can accidentally produce a plausible average while changing both totals.

## Part B: a distinct cubic map

Use the real polynomial transformation x=u³−3uv², y=3u²v−v³ on the full annulus one<=sqrt(u²+v²)<=two. Derive its Jacobian directly from the two polynomials. In input polar coordinates it is 9r^four, positive on the annulus.

The image has physical radius R=r³ and angle phi=three theta. Thus one<=R<=eight, and a full input rotation covers each physical angle three times. The distinct physical area is 63pi, while the integral of the absolute Jacobian over the full input annulus is 189pi.

State why excluding the critical origin is insufficient to make this map one-to-one. Local invertibility and a positive determinant do not remove the three distinct preimages in the declared full-angle domain. A numerical scatter plot can illustrate overlap, but an explicit angle/preimage argument establishes its count.

For physical density rho=x²+y², the distinct total is 4095pi/two. Derive this in target polar coordinates, and compare it with the full pullback integral. The latter must count multiplicity unless the input domain is restricted or the interpretation explicitly accounts for repeated coverage.

As another check, derive the cubic annulus average density 32.5 and compare it with the physical density range one to sixty-four. Explain why this valid average does not detect a triple count when both total and area are multiplied by three. Global coverage needs its own evidence.

## Part C: construct a once-covering description

Choose an input angular interval of length two pi/three, with an appropriate boundary-cut convention. Verify that it covers the physical annulus once up to negligible boundary duplication. Recompute the area and density total on that restricted domain.

Derive the squared-map and cubic-map factors from a common angular/radial pattern if useful, but check the actual polynomial derivatives rather than assuming every nonlinear transformation has constant multiplicity. Critical sets, domain restrictions and overlapping images can change the conclusion in other examples.

Keep unsigned area separate from oriented flux. The determinant's sign carries local orientation, whereas its absolute value supplies unsigned area. Neither convention alone repairs a globally repeated coordinate description. A sign change and a coverage count are different issues and can occur independently.

## Part D: independent numerical evidence

Implement selected target-domain and pullback integrals with a documented numerical method. Refine both discretization and any boundary approximation. Compare a deliberately unrestricted full-angle pullback with the once-covering result, and explain why better quadrature cannot fix the former's different counting interpretation.

Retain transformed bounds, a textual region description, derivative matrices, inverse or preimage arguments, exact area/density totals and numerical residuals. For the wedge, compare direct horizontal or vertical slices. For the cubic annulus, compare physical polar integration with both input angular domains. Disclose any symbolic or numerical software used rather than treating its output as a proof of global injectivity.

[MIT OCW 18.02SC Fall 2010 Unit 3 Part A](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/3.-double-integrals-and-line-integrals-in-the-plane/part-a-double-integrals/) supplies link-only change-of-variable scope. These polynomial coverage problems are original bounded extensions, not a complex-analysis or general measure-theory curriculum. No source exercise, proof, figure, code or data is imported. Broader transformation theory, measured workload and qualified review remain open; the course stays partial and unreviewed with substantial AI-assisted authoring.
