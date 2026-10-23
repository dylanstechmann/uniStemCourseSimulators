# Assignment 3: curved boundary and field evidence

This open report closes a curved volume's full boundary, checks flux in two independent ways, and then uses a separate vector field for Stokes circulation. All fields and regions are constructed mathematics. Retain parameterizations, derivations, code and report locally; selected browser responses do not grade the complete theorem argument. State the integral type, region and orientation before selecting a formula.

## Part A: describe the complete region

Let D lie above z=one and below z=two−x²−y² over the unit disk x²+y²<=one. Its upper surface is a downward paraboloid patch and its bottom is a flat disk. They meet at the unit circle in plane z=one. The full outward boundary includes both pieces.

Use cylindrical coordinates to compute volume pi/two. Write the radial, height and angle bounds explicitly. A two-dimensional projected disk is not the volume, and the upper surface alone is not its closed boundary. The seam has zero surface area but supplies the boundary curve used later.

## Part B: flux of the first field

Use F=(xz, yz, z²). On the upper graph, outward orientation is upward and the area-vector element is (two x, two y, one)dxdy. Substituting z=two−r² gives F dotted with that vector equal to four−r^four. Its disk integral is 11pi/three.

On the bottom z=one, the outward normal points downward. Its flux is -pi, so the complete outward flux is eight pi/three. A positive upper contribution does not justify dropping a negative bottom contribution. Preserve the signed sum rather than adding absolute values.

Independently calculate divergence F=4z and integrate it over the same volume. It gives eight pi/three. Show the original derivatives and bounds rather than using the surface answer as the input to the volume calculation. The field is smooth throughout a neighborhood of this bounded piecewise-smooth region, so the theorem hypotheses are satisfied in this mathematical construction.

Calculate the volume integral of z independently and divide by volume to obtain mean height four/three, within the region’s range one to two. Since divergence is four z, this moment supplies an additional check on the complete boundary flux. Retain its separate integral and bounds rather than recovering the mean only from the already-computed flux.

## Part C: a separate Stokes field

Now use G=(-yz, xz, zero), not the preceding field F. Its curl is (-x, -y, 2z). Take the upper surface with upward normal and its boundary counterclockwise when viewed from above. The boundary lies at r=one, z=one.

Direct circle parameterization gives circulation two pi. Curl flux through the upper graph has integrand four−four r² and gives the same result. A flat upward disk at z=one provides another spanning-surface check because G is smooth on the needed neighborhood. Reversing the normal must reverse the boundary direction and both signs.

Explain why the divergence theorem and Stokes theorem use different integrands and geometric objects here. One relates a closed boundary's transfer to a volume divergence. The other relates an oriented boundary curve's circulation to curl flux through a spanning surface. An open surface can be appropriate for the second without being the complete boundary for the first.

## Part D: scalar area is another quantity

Calculate the upper graph's scalar area using sqrt(1+4r²)dA. The result is pi(5sqrt5−one)/six. Compare it with the graph's projected area pi and the volume pi/two; their dimensions and meanings differ.

The vector (two x, two y, one)dA already carries both normal direction and graph measure for a flux calculation. Multiplying it again by sqrt(1+4r²)would double-count the surface measure. Alternatively, a unit normal must be paired with the scalar surface element. Demonstrate that the two consistent conventions give the same flux.

Retain all boundary pieces, parameterizations, orientations, field derivatives, three kinds of integral and independent checks. If using numerical quadrature, refine it and report residuals separately from the theorem conditions. An accurate integral of the wrong surface or wrong field does not become correct by agreement with a mislabeled plot.

[MIT OCW 18.02SC Fall 2010 Unit 4 Part B](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/4.-triple-integrals-and-surface-integrals-in-3-space/part-b-flux-and-the-divergence-theorem/) and [Part C](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/4.-triple-integrals-and-surface-integrals-in-3-space/part-c-line-integrals-and-stokes-theorem/) supply link-only scope. All fields, problems and explanations are original and AI-assisted; no source proof, figure, exercise, code or data is imported. Real physical source/transport interpretation, broader coursework, measured workload and qualified review remain open; the course stays partial and unreviewed.
