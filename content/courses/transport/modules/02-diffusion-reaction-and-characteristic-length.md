# Diffusion, reaction, and characteristic length

Diffusion moves a species in response to spatial differences in concentration. Reaction may create or consume that species while it moves. When both processes matter, a useful first question is not only “how fast?” but “over what distance can the species travel before reaction substantially changes it?” A characteristic length connects diffusivity, reaction rate, geometry, and boundary conditions to the size of concentration gradients.

## Flux follows the concentration gradient

For a dilute species in a stationary medium with constant diffusivity D, Fick's first law is

**J = −D∇C.**

The flux J is amount crossing unit area per unit time; if C is in mol/m³ and D in m²/s, J has units mol/(m²·s). The minus sign makes flux point down the concentration gradient. In one dimension, if concentration falls as x increases, `dC/dx < 0` and `Jx = −D dC/dx > 0`: material diffuses in the positive x direction. A flux is not itself a total rate. Across a uniform area A, the amount rate is `J A`.

Fick's first law relates flux to a local gradient. It does not specify a whole concentration profile until paired with conservation, geometry, and boundary conditions. A fixed surface concentration, an impermeable boundary with zero flux, and a specified incoming flux describe different physical situations. A membrane or interface can also impose an additional resistance. State what is held at each boundary before solving for the interior.

## Diffusion time is a scale estimate

Diffusion over a distance L takes a characteristic time on the order of

**tD ≈ L²/D.**

The expression has units of seconds because `m²/(m²/s) = s`. It is a scaling estimate, not an exact arrival time or a universal solution. Geometry and the chosen definition of “equilibrated” introduce numerical factors; for a simple one-dimensional slab, separation-of-variables solutions often include factors such as `1/π²` in the slowest mode. Doubling L increases the estimate fourfold, while doubling D halves it. Converting micrometers to meters before squaring is essential: `100 μm = 1×10⁻⁴ m`, so with `D=1×10⁻⁹ m²/s`, `L²/D=10 s`.

When no reaction or bulk flow acts and D is constant, the concentration evolution follows Fick's second law, `∂C/∂t = D∇²C`. This equation is a conservation statement combined with Fick's flux law. If there is a reaction source term R, write `∂C/∂t = D∇²C + R(C)`; for first-order consumption of a reactant, `R(C) = −kC`. If bulk fluid moves, an advection term is also needed; diffusion alone may not describe transport through a perfused channel or moving fluid.

## Compare diffusion and reaction clocks

For first-order consumption, the characteristic reaction time is

**tR ≈ 1/k,**

where k has units s⁻¹. The ratio of the diffusion time to the reaction time is a Damköhler-type number,

**Da = tD/tR ≈ kL²/D.**

Da is dimensionless. If `Da ≪ 1`, diffusion redistributes the species across L faster than first-order reaction consumes it; concentration may be relatively uniform on that scale. If `Da ≫ 1`, reaction is rapid compared with delivery across L, and a substantial gradient or depleted interior may develop. When Da is around one, neither process can be dismissed using this comparison alone. These categories guide model selection; they do not replace a solution with the relevant boundary conditions.

The associated reaction-diffusion length is

**λ = √(D/k),**

which has units of length. It is the distance over which diffusion and first-order consumption are comparable in the simple model. Since `Da = (L/λ)²`, comparing the object's dimension with λ gives the same first check. A larger object or larger k increases Da; a larger D decreases it. Geometry matters: a slab's half-thickness, a sphere's radius, or a cylinder's radius may be the relevant L, depending on the boundary and symmetry. Do not use a whole diameter when the longest path is only a radius, or a radius when the relevant supply path is longer.

For zero-order consumption, a simple reaction time instead depends on the concentration available: `tR ≈ C₀/r₀` for a starting concentration C₀ and a constant volumetric consumption rate r₀. Its units are time when r₀ is concentration per time. Saturable kinetics, multiple reactions, variable diffusivity, and spatially varying cell density change the comparison. The estimate should match the kinetic regime over the concentrations actually considered.

## A synthetic length-scale calculation

Let `D = 2×10⁻⁹ m²/s`, `L = 200 μm = 2×10⁻⁴ m`, and first-order `k = 0.05 s⁻¹`. Then `tD ≈ L²/D = 20 s`, while `tR ≈ 1/k = 20 s`; thus `Da ≈ 1`. The reaction-diffusion length is `λ = √(D/k) = 200 μm`, matching L. Diffusion and reaction act on comparable scales, so the full profile may matter. If L doubled with D and k unchanged, tD and Da would each increase fourfold; the reaction clock would stay at 20 seconds.

This calculation is consistent with the existing time-scale practice: for `D=1×10⁻⁹ m²/s` and `L=100 μm`, `tD ≈ 10 s`. That answer alone does not say whether reaction is limiting; a reaction rate or time is also needed. It only estimates the diffusion clock. Units provide a quick audit: squaring `100 μm` without first converting it to meters gives a wildly incorrect answer.

## What the estimate leaves out

Boundary concentrations, external film resistance, membrane permeability, geometry, binding, advection, and nonlinear or saturated kinetics can all change the internal field. In a cell-laden construct, a sufficient surface concentration does not guarantee that every interior location has the same concentration; a reaction-diffusion model may predict a lower interior value. That prediction depends on the assumed diffusivity, consumption law, shape, and boundary condition. Synthetic examples are useful for exploring those assumptions, but their numbers are not measurements of a real tissue or device.

Use the scale comparison to decide what to solve next: check flux direction and units, estimate `L²/D`, estimate the reaction time from the applicable kinetic law, compare the clocks, then select a geometry and boundary-value model if gradients matter. MIT OpenCourseWare's reaction-diffusion lecture is an optional link-only technical reference. No lecture note, equation derivation, figure, exercise, or dataset has been copied or adapted.
