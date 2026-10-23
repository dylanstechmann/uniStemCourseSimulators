# Nonlinear Jacobians and global coverage

A Jacobian determinant describes local measure change. It does not alone establish that a coordinate map covers the intended region once. This original foundation develops a nonlinear one-to-one map and a polynomial map with positive Jacobian but repeated global coverage. The examples extend the regular polar/elliptical calculations while keeping unsigned area distinct from orientation and flux. All coordinates and densities are synthetic normalized quantities.

## Derive a local area factor

For a differentiable planar map (u, v) to (x, y), the two derivative columns describe the images of coordinate directions. Their determinant is the signed parallelogram-area factor. Ordinary unsigned area uses its absolute value. A change-of-variables integral also needs the correct transformed region and a usable one-to-one description, apart from suitable boundary exceptions.

A negative determinant reverses local orientation without making area negative. A positive determinant preserves local orientation, but distant input points can still have the same image. No increase in quadrature precision can discover that the intended quantity was distinct physical area rather than a multiply counted sweep.

## Worked nonlinear shear

Use x=u, y=v+u² on 0<=u<=one, 0<=v<=two. Its determinant is one and its inverse is u=x, v=y−x², so it is one-to-one on the declared region. In physical coordinates the bounds are 0<=x<=one, x²<=y<=x²+two.

Area is two, and the integral of y over that region is eight/three. Derive it both from the curved physical slices and from integral (v+u²)du dv on the rectangle. The nonlinear map keeps area locally but changes the boundary shape; leaving old rectangular physical bounds would describe a different region.

## A distinct polynomial rehearsal

Now use x=u²−v², y=2uv on the annulus one<=sqrt(u²+v²)<=two. The real Jacobian determinant is four(u²+v²), positive everywhere on this domain. At (u, v)=(one, one), it is eight and the image point has radius two.

Write u=r cos theta, v=r sin theta. The image is x=r²cos(2theta), y=r²sin(2theta). Thus physical radius R=r² runs from one to four, and a full input angle range zero to 2pi traverses each physical angle twice. Points (u, v) and (-u, -v) have the same image. The origin, where the Jacobian vanishes, is already excluded; its exclusion does not remove this two-to-one property.

The distinct physical annulus has area fifteen pi. Integrating the absolute Jacobian over the full input annulus instead gives thirty pi. The latter calculation is mathematically a covered-area total, not the distinct area requested. Both positive local determinant and an apparently plausible numerical answer can coexist with the wrong global counting convention.

## Density totals make the same issue visible

For physical density rho=x²+y², integrate directly in physical polar coordinates:

$$\int_0^{2\pi}\int_1^4 R^3\, dR\, d\phi=255\pi/2.$$

The distinct area-average density is (255pi/two)/(15pi)=17/2, which lies between its minimum one and maximum sixteen. This range check is useful but does not by itself detect repeated coverage, which multiplies both total and area by the same factor.

Pulling the density back gives rho=r^four. Multiplying by the map determinant and the input polar measure gives four r^seven dr dtheta. Over the full input annulus the total is 255pi, twice the distinct amount. Forgetting either Jacobian or coverage creates a different error, and one can accidentally compensate for the other in a single test.

## Choose a once-covering domain

Restrict the input angle to an interval of length pi, for example zero<=theta<pi. It covers the physical annulus once except for the conventional boundary cut, which has zero area. Repeating the area and density integrals on that domain gives the distinct totals.

A full input rotation is appropriate only if the task explicitly requests the twice-covered quantity or multiplicity is accounted for. Do not divide arbitrary answers by two without deriving the actual map and domain. Other maps can have different or varying multiplicities, critical sets or no global inverse on the proposed region.

## Retain the geometric evidence

A report should show derivative matrix, determinant sign, transformed boundaries, inverse or preimage count, and at least one direct integral in the target region. Distinguish unsigned volume/area measure from an oriented surface-vector element used for flux. Sampling input points may illustrate folding, but a finite scatter plot is not a proof of global injectivity or coverage.

[MIT OCW 18.02SC Fall 2010 Unit 3 Part A](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/3.-double-integrals-and-line-integrals-in-the-plane/part-a-double-integrals/) sessions 49–55 supply link-only integration/change-of-variable scope. The polynomial coverage extension is original and does not claim a complex-analysis or general measure-theory course. No source problem, figure, proof or code is imported. Workload and qualified review remain open; the course stays partial and unreviewed with substantial AI-assisted authoring.
