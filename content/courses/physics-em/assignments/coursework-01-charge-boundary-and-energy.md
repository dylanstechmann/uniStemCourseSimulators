# Assignment 1: continuous charge, boundary and energy evidence

This open report connects superposition, Gauss law, potential gradients and field energy with the new nonuniform cylindrical source. It asks for a complete source/boundary ledger and two independent energy calculations. All geometries and charges are synthetic mathematical inputs. They are not a tissue-field model or electrical equipment specification. Retain derivations, code and report locally; browser checkpoints assess selected quantities only.

## Part A: a distinct prescribed source

Use an infinitely long insulating cylinder of radius $a=0.05$ m with fixed volume density proportional to $r^2$ inside it. A concentric sleeve has inner radius $b=0.15$ m and is grounded, with no external source fields. Define total line charge $\lambda$ and $K=\lambda/(2\pi\epsilon_0)=8$ V. The density is zero outside the insulating source; no surface charge is prescribed at $a$.

Write the volume density in terms of $\lambda$ and $a$, then integrate cylindrical shells to obtain enclosed line charge as a function of radius. Explain why a half-radius surface encloses one sixteenth of the total rather than the cross-sectional area fraction. Identify the distribution's symmetry before using a Gaussian surface; the cylinder's outline alone is not a symmetry argument.

Derive the radial field inside the source, in the annulus and inside the conductor. At $r=a/2$, $E_r=20$ V/m. At $a$ the field agrees across the insulating boundary because no added surface charge was stipulated. Sketch signed field and potential profiles and mark the regions where each formula applies. A plot with disconnected formulas is not a substitute for interface checks.

## Part B: potential and induced conductor charge

Use $V(b)=0$ and integrate the field from each observation point to that reference. The source-boundary potential is $V(a)=8\ln3\approx8.78890$ V. The axis potential is two volts higher, $V(0)=8\ln3+2$. Differentiate both interior and annular formulas and verify $E_r=-dV/dr$ where the expressions are smooth.

Find the induced line charge on the conductor's inner surface by using a Gaussian surface in the metal. It is $-\lambda$. At the inner radius, $\sigma_b/\epsilon_0=-K/b=-160/3$ V/m. Retain the sign and identify the direction of the radial field immediately before it falls to zero in the metal. State what would change if the sleeve were isolated and neutral rather than grounded.

The insulating charge distribution is not an equipotential terminal. In particular, $V(0)$ and $V(a)$ differ even though both lie within the source's geometric boundary. Explain why selecting one of them as “the” source voltage would omit the actual distribution when computing energy.

## Part C: two different energy integrals

Calculate energy per unit length from $\int\epsilon_0E^2/2\,dA$, splitting the integral at $a$. Independently calculate it from $\tfrac12\int\rho V\,dA$ over the insulating source. The grounded sleeve's surface contribution has zero potential. Show the equality of the two resulting expressions before evaluating any decimals.

The normalized value $U'/(\pi\epsilon_0K^2)$ is $\ln3+1/8$. Keep the interior and annular contributions separate so the radial integration factors remain visible. Compare the result with the incorrect shortcuts $\lambda V(0)/2$ and $\lambda V(a)/2$. Identify the physical assumption each shortcut would require and why that assumption fails for this prescribed volume charge.

Implement numerical quadrature for both integrals, compare convergence under refinement and report absolute or normalized discrepancies. A copied closed expression evaluated twice does not supply an independent numerical check. Near-axis behavior is finite; a numerical implementation should not evaluate the annular $K/r$ formula at zero.

## Part D: restrict the conclusion

Construct a nonsymmetric charge arrangement with zero net enclosed charge but a nonzero local electric field on part of a closed surface. Explain why zero total flux cannot identify every local field and why that counterexample does not contradict the correctly applied cylindrical result. Distinguish a local gradient, a boundary value and an integrated conservation statement.

Your retained report should include a source/boundary map, charge integral, field/potential profiles, induced-charge sign, energy identities and numerical evidence. State the ideal infinite-length and electrostatic assumptions. A finite cylinder with end fields, a changing dielectric or an external electrode would require a different boundary problem, not merely a different number in the same formula.

The [MIT OCW 8.02 Spring 2007 class topics](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/class-topics/) continuous-charge/potential/Gauss strands are link-only comparators. Problems and explanations here are original with substantial AI assistance; no university assessment, diagram or teaching text is imported. Numerical consistency does not establish qualified physics review or a measured semester workload. The course remains partial and unreviewed.
