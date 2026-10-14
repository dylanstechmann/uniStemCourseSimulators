# Multiple integrals and coordinate transforms

A multiple integral accumulates a scalar density over a region. The region and its bounds are part of the model: sketch them first, identify the coordinate convention, then choose bounds that cover every point exactly once apart from boundaries of zero area. If a density varies over space, integrating it matters; multiplying one concentration by volume is valid only when that concentration is uniform.

## The Jacobian measures a transformed cell

Suppose coordinates $(u,v)$ map to physical coordinates $(x(u,v),y(u,v))$. A small rectangle in the $uv$ plane generally becomes a tilted parallelogram in the $xy$ plane. The determinant

$$
J=\det\begin{bmatrix}x_u&x_v\\y_u&y_v\end{bmatrix}
$$

gives its signed local area scale. For scalar area or mass accumulation, use the absolute value $|J|$ so the measure stays nonnegative; orientation is handled separately in oriented line and surface integrals. The change-of-variables rule is

$$
\iint_R f(x,y)\,dA=\iint_S f(x(u,v),y(u,v))\,|J|\,du\,dv.
$$

The transformation must be smooth and one-to-one over the chosen interior, or the region must be split to avoid counting points more than once. A zero determinant marks a locally collapsed coordinate direction, where this formula needs special treatment.

## Polar coordinates

With $x=r\cos\theta$ and $y=r\sin\theta$, the Jacobian determinant is $r$. Thus $dA=r\,dr\,d\theta$, with $r\ge0$. For a disk of radius $R$, use $0\le r\le R$ and one full angular turn, for example $0\le\theta\le2\pi$. Omitting the factor $r$ treats every radial strip as having the same area even though strips farther from the origin are wider.

For $R=3$, the disk area is

$$
\int_0^{2\pi}\int_0^3 r\,dr\,d\theta
=2\pi\left[\frac{r^2}{2}\right]_0^3=9\pi\approx28.274.
$$

The same result comes from the Cartesian bounds $-3\le x\le3$ and $-\sqrt{9-x^2}\le y\le\sqrt{9-x^2}$. Both setups describe the same disk, but polar bounds are simpler because the boundary is a constant radius.

As a variable-density example, let a constructed surface density be $c(r)=2+r$ mg/cm$^2$ on a disk of radius 2 cm. Its total amount is

$$
\int_0^{2\pi}\int_0^2(2+r)r\,dr\,d\theta
=2\pi\left[ r^2+\frac{r^3}{3}\right]_0^2
=\frac{40\pi}{3}\text{ mg}.
$$

The disk area is $4\pi$ cm$^2$, so the area-mean density is $10/3$ mg/cm$^2$. Multiplying the center value by the area would give $8\pi$ mg and undercount the total; a nonuniform field cannot be represented by one arbitrary point value.

## Other coordinates and checks

Cylindrical coordinates use volume element $r\,dr\,d\theta\,dz$. Spherical coordinates use $\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$ under the convention that $\phi$ is measured down from the positive $z$ axis. State angle ranges explicitly, since a different convention changes the bounds even when the Jacobian expression is adjusted consistently.

Before accepting an integral, check that the transformed bounds cover the intended region, the Jacobian is the absolute local scale for scalar accumulation, and the integrand retains its units after the measure is included. For an area density, concentration times area gives amount; for a volume density, concentration times volume does. Later lessons use Jacobian measures in more complex regions and connect accumulation to vector-field flux. These synthetic examples specify no biological concentration or tissue geometry.
