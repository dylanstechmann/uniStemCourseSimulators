# Continuous charge and a grounded cylindrical boundary

The earlier Gauss-law reading treats point-source superposition and a uniform insulating sphere. A continuous nonuniform distribution requires an actual charge integral before symmetry can simplify the field. This original cylindrical example also connects potential, conductor boundaries and two independent expressions for field energy. The geometry and charges are synthetic mathematical inputs, not tissue fields or an equipment specification.

## State the source and reference

An infinitely long insulating cylinder has radius $a$ and fixed volume density $\rho(r)=\rho_0(r/a)^2$ for $r<a$. A concentric conducting sleeve has inner radius $b>a$ and is grounded. Assume electrostatic equilibrium, cylindrical symmetry, no external sources and vacuum between the prescribed charge and sleeve. The insulator is not a conductor and is not generally an equipotential. Results are per unit length, so no infinite total energy is reported.

The potential reference is $V(b)=0$. A logarithmic potential for an unshielded infinite line cannot be assigned zero at infinity by copying a finite point-charge convention. The stated grounded sleeve and absence of external fields provide a finite field-energy boundary here. An isolated neutral sleeve would be a different problem with a different outer charge and field.

## Integrate enclosed charge before applying Gauss

A cylindrical shell of thickness $ds$ has cross-sectional area $2\pi s\,ds$. Thus the enclosed line charge for $r<a$ is

$$\lambda(r)=\int_0^r\rho_0(s/a)^2\,2\pi s\,ds=\frac{\pi\rho_0r^4}{2a^2}.$$

The total line charge is $\lambda=\pi\rho_0a^2/2$. A radius at half the source boundary encloses $1/16$ of the charge, not one quarter. The cross-sectional area fraction alone would apply to uniform density, which was not stipulated.

Define $K=\lambda/(2\pi\epsilon_0)$, measured in volts. Cylindrical symmetry makes the field radial and constant on the curved Gaussian surface, with no end-cap contribution. Gauss gives

$$E_r(r)=K\frac{r^3}{a^4}\quad(r<a),\qquad E_r(r)=\frac K r\quad(a<r<b).$$

The expressions agree at $a$, where no extra surface charge was specified. Inside the conducting material the electrostatic field is zero. The total induced inner-surface line charge is $-\lambda$, as a Gaussian surface inside the metal must enclose zero net charge. Its surface density is $\sigma_b=-\lambda/(2\pi b)$, or $\sigma_b/\epsilon_0=-K/b$. The sign follows from the conductor's inner boundary; dropping it would reverse the surface-charge conclusion.

## Recover potential by a reference integral

Use $V(r)-V(b)=\int_r^bE_r(s)\,ds$. In the annulus, $V(r)=K\ln(b/r)$. In the source region split the integral at $a$:

$$V(r)=K\ln(b/a)+\frac K4\left[1-(r/a)^4\right].$$

Both potential and radial field are continuous at the insulating boundary. At the axis the field is zero but the potential is $K[\ln(b/a)+1/4]$, generally nonzero. This reinforces the distinction between potential value and gradient. Differentiating the potential returns $E_r=-dV/dr$ in each smooth region.

For a worked case choose $K=12$ V, $a=0.02$ m and $b=0.06$ m. At $r=a/2$, the field is $K/(8a)=75$ V/m. The source-boundary potential is $12\ln3\approx13.1833$ V, and the axis potential is three volts higher. Just inside the grounded sleeve the radial field is 200 V/m and $\sigma_b/\epsilon_0=-200$ V/m.

A distinct rehearsal uses $K=10$ V, $a=0.04$ m and $b=0.08$ m. The half-radius field is 31.25 V/m, $V(a)=10\ln2$ V, and $V(0)=10\ln2+2.5$ V. At the sleeve the field is 125 V/m. Keep those parameters separate from the report's third case.

## Two energy calculations with different integrands

Integrating energy density over the cross section gives energy per length

$$U'=\int_0^b\frac{\epsilon_0 E_r^2}{2}\,2\pi r\,dr
=\pi\epsilon_0K^2\left[\ln(b/a)+\frac18\right].$$

The $1/8$ comes from integrating the interior $r^6$ field square with the extra radial area factor. The logarithm comes from the annular inverse-radius field. Both terms are nonnegative when $b>a$. For the rehearsal, the normalized energy $U'/(\pi\epsilon_0K^2)$ is $\ln2+1/8$.

Independently evaluate $\tfrac12\int_0^a\rho(r)V(r)\,2\pi r\,dr$. It gives the same result; the grounded conductor's surface term has zero potential. Replacing this integral with $\tfrac12\lambda V(0)$ or $\tfrac12\lambda V(a)$ would treat all fixed volume charge as if it occupied one potential and gives the wrong energy. A distributed insulator cannot automatically be substituted for one lumped equipotential capacitor terminal.

## Verification and scope

Compare symbolic integrals with numerical quadrature, differentiate the potential, and test charge fractions, boundary continuity and the induced surface sign. Near-axis and large-sleeve limits constrain the result. A cylindrical Gaussian surface alone does not justify this simplification for a nonsymmetric source. [MIT OCW 8.02 Spring 2007 class topics](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/class-topics/) supplies link-only scope for continuous charge, potential and Gauss law. All text and parameters are original and AI-assisted. Finite-end fields, general boundary solvers and material breakdown are outside this model; the course remains partial and unreviewed.
