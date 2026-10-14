# Fluid mechanics and microvascular flow

Fluid mechanics connects pressure differences to motion and relates the importance of inertia to viscosity. In small channels, viscous effects often matter strongly, but a small dimension alone does not guarantee a particular flow regime. Begin with a defined geometry, fluid model, characteristic speed, and length. Then decide whether a dimensionless estimate and an ideal pressure-flow relation apply to the situation.

## Reynolds number compares inertial and viscous scales

The Reynolds number is

**Re = ρ U L / μ = U L / ν,**

where ρ is density, U a characteristic speed, L a characteristic length, μ dynamic viscosity, and `ν = μ/ρ` kinematic viscosity. With SI units, `kg/m³ × m/s × m ÷ (kg/(m·s))` is dimensionless. The length convention must be stated: for flow in a circular tube, the diameter is commonly used; in other geometries an appropriate hydraulic diameter or another specified scale may be used. Use the same convention when comparing results.

Re compares the scale of inertial effects with viscous effects. A small value indicates that viscosity is important at the stated scale; a large value indicates that inertia is more important relative to viscosity. The number alone is not a universal laminar-versus-turbulent switch. Transition depends on the geometry, disturbances, inlet development, surface conditions, and fluid behavior. A threshold often quoted for a long circular pipe cannot be transferred unchanged to a branching vessel, a short entrance region, or a non-Newtonian suspension. Low Re also does not mean that velocity gradients and wall stresses vanish; viscous stresses are central to the flow.

Use a representative speed that matches the question. In a pipe the cross-sectional mean speed is `U = Q/(πR²)` for volumetric flow rate Q and radius R; the centerline speed in ideal Poiseuille flow is twice that mean. Mixing these speeds changes Re. If a problem specifies a characteristic L, use that stated convention, convert it to meters, and make clear whether a biological structure or tube diameter is being treated as the scale.

## Pressure drives ideal laminar tube flow

For a steady, incompressible, Newtonian liquid in a straight, rigid, circular tube with no slip and fully developed laminar flow, the axial velocity profile is parabolic:

**u(r) = ΔP (R² − r²)/(4 μ ℓ),**

where R is tube radius, ℓ its length, ΔP the inlet-to-outlet pressure drop, and r the radial position. Integrating velocity over the cross-section gives the Hagen–Poiseuille relation:

**Q = πR⁴ ΔP/(8 μ ℓ).**

Equivalently, `ΔP = ℛ Q` with hydraulic resistance `ℛ = 8 μ ℓ/(πR⁴)`. Check dimensions: `Pa × m⁴ /(Pa·s × m)` gives `m³/s`. Pressure drop is a difference in pressure, not absolute pressure. A longer or more viscous tube has greater resistance; a larger radius lowers it sharply.

The fourth-power radius dependence is especially important. At the same pressure drop, halving R reduces Q by a factor of 16. At the same target flow, it instead takes 16 times the pressure difference in this ideal model. This sensitivity explains why a small geometric change can strongly affect a calculated pressure-flow relation. It is also why uncertainty in the effective radius can dominate a numerical estimate. Do not apply the circular-tube formula to a rectangular channel or an entire branching network without an appropriate model.

For multiple ideal tube segments in series, the same flow passes through each and pressure drops add, so the resistances add. For parallel branches with the same endpoints, pressure drop is shared while flows add; conductances `1/ℛ` add. Real networks may include changing radius, compliance, entrance losses, branching, and interacting flows, so this simple resistance bookkeeping is only an ideal starting point.

## Worked flow calculation

Take a rigid tube with `R = 0.50 mm = 5.0×10⁻⁴ m`, `ℓ = 0.10 m`, `μ = 1.0×10⁻³ Pa·s`, and `ΔP = 100 Pa`. Poiseuille's law gives `Q = π(5.0×10⁻⁴ m)⁴(100 Pa)/(8(1.0×10⁻³ Pa·s)(0.10 m)) = 2.45×10⁻⁸ m³/s`. The mean speed is `Q/(πR²) ≈ 0.0312 m/s`. These values solve the preserved numeric practice item under the specified ideal assumptions; they do not establish that a biological vessel behaves like this tube.

The Re example also needs unit conversion. With `ρ=1000 kg/m³`, `U=1 mm/s=0.001 m/s`, `L=100 μm=1×10⁻⁴ m`, and `μ=10⁻³ Pa·s`, `Re=ρUL/μ=0.1`. A low result says viscosity matters for this model and scale; it does not by itself validate the selected geometry, establish an exact transition threshold, or specify pressure drop.

## Limits for microvascular and cell-containing flows

The ideal equations assume a continuum fluid with constant properties, a rigid circular tube, a Newtonian constitutive relation, steady fully developed flow, and no-slip walls. In biological microflows, cells are finite objects rather than dissolved molecules, suspensions can show non-Newtonian behavior, vessel walls can deform, and branches or short segments can interrupt fully developed profiles. Effective viscosity may depend on diameter, cell fraction, flow rate, and the measurement scale. A single bulk viscosity and Poiseuille resistance may be useful as an approximation, but the assumptions and intended use must be stated.

Re, pressure drop, and flow rate answer related but different questions. Re is dimensionless and compares effects for a chosen scale; Poiseuille's law estimates Q from ΔP for a specific ideal geometry and fluid. A low Re does not give the pressure drop without a resistance model. Conversely, a computed flow rate does not prove that the assumptions hold. If dimensions are uncertain or the channel is compliant or branched, measured pressure-flow data or a more suitable model may be needed. These examples are synthetic teaching calculations, not predictions about a person, tissue, device, or process.

MIT OpenCourseWare lecture materials on fluid mechanics and microfluidic hydrodynamics are optional link-only technical references. No lecture text, figure, derivation, exercise, or dataset has been copied or adapted.

## Check whether the tube model has developed

“Fully developed” describes a velocity profile that no longer changes along the tube axis; pressure can still decrease continuously as viscous stresses dissipate mechanical energy. Near an inlet, the profile is developing, and a short segment may not contain a long region that meets the ideal assumption. Junctions, bends, contractions, and expansions also alter local velocity and pressure. A single pressure-drop calculation across such a network may need entrance or local-loss terms in addition to straight-tube resistance.

The pressure-flow formula also assumes the radius is known and constant. If a segment narrows or expands, treating the entire path as one uniform tube hides where most resistance occurs. For ideal segments in series, calculate each resistance with its own length and radius and then add pressure drops at a common flow. If the geometry is not circular, select a relation derived for that cross-section rather than substituting an equivalent radius without justification. These modeling checks help explain why a dimensionless Reynolds estimate and an ideal Poiseuille calculation are useful first screens but limited representations of vascular or engineered microflows.
