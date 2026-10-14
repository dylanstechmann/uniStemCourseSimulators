# Line integrals, flux, and integral theorems

Vector fields can be accumulated along a path or measured across a boundary. The geometry and orientation determine the integral. Parameterize the curve, keep its direction explicit, and check that the chosen theorem applies to the region and field.

## Work along an oriented curve

For a smooth path $\mathbf r(t)$ from $t=a$ to $t=b$ and a vector field $\mathbf F$, the work integral is

$$
\int_C\mathbf F\cdot d\mathbf r
=\int_a^b\mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt.
$$

The tangent vector $\mathbf r'(t)$ carries both direction and the change in path length. Reversing the path reverses this integral. A scalar line integral $\int_C f\,ds$ instead uses $ds=|\mathbf r'(t)|dt$ and does not change sign when the path direction is reversed.

For the counterclockwise unit circle $\mathbf r(t)=(\cos t,\sin t)$, $0\le t\le2\pi$, take $\mathbf F=(-y,x)$. Then $\mathbf F(\mathbf r(t))=(-\sin t,\cos t)=\mathbf r'(t)$, so the circulation is

$$
\int_0^{2\pi}\mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt
=\int_0^{2\pi}1\,dt=2\pi.
$$

Clockwise traversal gives $-2\pi$. This signed result distinguishes circulation from path length.

## Green's theorem as a check

If $C$ is a positively oriented, simple, closed planar boundary of a region $D$, and the field components have continuous first partial derivatives on a suitable neighborhood of $D$, Green's circulation form states

$$
\oint_C P\,dx+Q\,dy
=\iint_D(Q_x-P_y)\,dA.
$$

For $\mathbf F=(-y,x)$, $P=-y$ and $Q=x$, so $Q_x-P_y=1-(-1)=2$. Over the unit disk, the area integral is $2\pi$, matching the parameterized line integral. The match is a useful check on signs and orientation; reversing the boundary would reverse the circulation.

Green's flux form is

$$
\oint_C P\,dy-Q\,dx
=\iint_D(P_x+Q_y)\,dA.
$$

It converts outward planar flux to the double integral of divergence. For $\mathbf F=(x,y)$ on the unit circle, the divergence is 2, giving flux $2\pi$. Circulation uses the scalar curl $Q_x-P_y$; outward flux uses divergence $P_x+Q_y$. The integrands and geometric meanings differ.

## Choose the theorem by its boundary

Stokes' theorem relates circulation around an oriented boundary curve to the surface integral of curl over a surface spanning that curve. The boundary orientation must agree with the chosen surface normal by the right-hand rule. The divergence theorem instead relates outward flux through an entire closed surface to the volume integral of divergence inside it; it requires a suitable closed boundary and a field with the needed regularity throughout the enclosed region. Green's theorem is the planar special setting for a region and its boundary. None of the theorems removes the need to check holes, singularities or smoothness assumptions.

As a three-dimensional check, for $\mathbf F=(x,y,z)$, $\nabla\cdot\mathbf F=3$. The outward flux through the unit sphere is therefore $3$ times the unit-ball volume, $3(4\pi/3)=4\pi$. A direct surface calculation should agree when the normal points outward.

The examples use smooth constructed fields and idealized regions. Measurements on a sampled boundary do not by themselves establish the field between samples, and a numerical balance does not identify a unique physical source or mechanism.
