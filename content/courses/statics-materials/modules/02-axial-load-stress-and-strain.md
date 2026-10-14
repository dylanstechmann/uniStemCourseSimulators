# Axial load, stress, and strain

An axial member is loaded along its length. A straight bar pulled at its ends is the simplest model: one end is restrained, the other carries a tensile force, and a cut through the bar reveals an internal force that balances the applied load. This lesson uses that idealized member to connect force, cross-section, deformation, and material stiffness. The equations are useful for first estimates and for checking units; their assumptions matter as much as their arithmetic.

## From force to average normal stress

At a section normal to the member's axis, the internal axial force is distributed across the cut. If the force is `F` and the area is `A`, the average normal stress is

**σ_avg = F/A.**

Take tension as positive and compression as negative when signs are useful. Many introductory calculations report only the magnitude and name the loading direction in words. Stress has units of force per area: pascals (Pa) in SI, where 1 Pa = 1 N/m². In a small engineering section, it is often convenient to use N/mm²; because 1 N/mm² = 1 MPa, a 500 N force on 50 mm² produces 10 N/mm², or 10 MPa. Writing the unit after each substitution prevents the common mistake of treating mm² as m² without a factor of one million.

The average is not a promise that stress is identical at every point. It is a useful one-dimensional description when the member is prismatic or changes gradually, the load is applied through the centroid, and the section is sufficiently far from supports, shoulders, holes, grips, and other load-introduction details. A sharp corner, defect, hole, interface, or eccentric force can produce a local field that is much larger or more complex. Those concentrations require a later local-stress model, measurement, or simulation. Here we stay with a straight, uniform member and an axial load whose line of action passes through its centroid.

## Strain describes deformation relative to length

Stress is a force intensity; strain describes relative change in length. If a reference length `L₀` changes by ΔL, the engineering axial strain is

**ε = ΔL/L₀.**

Strain is dimensionless because both lengths use the same unit. A 100 mm gauge length that extends by 0.1 mm has ε = 0.1/100 = 0.001. In tension, ΔL and strain are positive under the convention above; compression shortens the member and gives a negative strain. The small-strain approximation treats this change as small compared with the original length. At large deformation, the reference length, evolving geometry, and a finite-strain measure need more careful treatment.

The slope of a stress-versus-strain curve near the origin is the elastic modulus `E` when that portion of the response is linear. In uniaxial linear elasticity, **σ = Eε**, so **ε = σ/E**. Modulus has stress units. A larger `E` means a smaller strain at the same stress within the same linear model; it does not by itself state the strength or the stress at failure. The straight-line relation is an approximation over a bounded range, not a universal description of every material or loading history.

## Deriving the extension of a uniform bar

For a straight bar with constant area `A`, constant modulus `E`, and a constant axial force `F`, combine the stress and strain equations:

**ε = σ/E = F/(AE).**

Since ε = ΔL/L, rearranging gives **ΔL = FL/(AE)**. This result predicts the elastic change in the bar's length. It can also be written as a spring-like relation `F = kΔL`, where the axial stiffness is **k = AE/L**. Stiffness is a property of this member geometry plus its material model: increasing area or modulus increases stiffness, while increasing length decreases it. Do not confuse stiffness `k`, with force-per-length units, with material modulus `E`, which has force-per-area units.

For example, take an ideal 100 mm long bar with area 10 mm², modulus 2 GPa, and a tensile force of 20 N. Convert the modulus first: 2 GPa = 2,000 MPa = 2,000 N/mm². The nominal stress is 20/10 = 2 N/mm² = 2 MPa. Then ε = 2/2,000 = 0.001, and the predicted extension is 0.001 × 100 mm = 0.1 mm. A separate stiffness check gives k = (2,000 N/mm²)(10 mm²)/(100 mm) = 200 N/mm, so F/k = 20/200 = 0.1 mm. The agreement checks the algebra and units; it does not validate the material constants for any particular specimen.

When the axial force, area, or modulus varies along a member, the one-piece expression using a single `A` and `E` may not apply. A simple idealization divides the bar into segments and adds their elastic extensions, **ΔL_total = Σ(FᵢLᵢ/(AᵢEᵢ))**, when each segment's axial force and properties are known and compatibility at the joins is appropriate. More complicated load sharing, changing geometry, local features, or material transitions needs the relevant boundary conditions and a more complete model. The formula does not infer those conditions from a material label alone.

## A redundant axial assembly needs a compatibility equation

Equilibrium may leave forces unresolved when a structure has more unknown member forces than independent equilibrium equations. The missing relation comes from how connected parts must deform together. Consider two straight, uniform bars connected between the same pair of rigid end plates; one plate is fixed and the other carries an axial tensile load. The plate geometry requires the bars to undergo the same extension, **δ₁ = δ₂ = δ**. That is a compatibility condition. Each bar also follows its own linear-elastic force–deformation law, **δᵢ = FᵢLᵢ/(AᵢEᵢ)**, and force equilibrium requires **F₁ + F₂ = P**. The three relations together determine the two member forces and common displacement.

**Synthetic example.** Two bars each have length 400 mm and area 100 mm², with moduli 200 GPa and 100 GPa. A 30 kN load is applied to the moving end plate. Convert the moduli to 200,000 and 100,000 N/mm². Their axial stiffnesses are **k₁ = A E₁/L = 50 kN/mm** and **k₂ = A E₂/L = 25 kN/mm**. The common extension is **δ = P/(k₁ + k₂) = 30/75 = 0.4 mm**. The stiffer bar carries **F₁ = k₁δ = 20 kN** and the other carries **F₂ = 10 kN**; they sum to the applied load. The corresponding nominal stresses are 200 MPa and 100 MPa. The force split follows both the material stiffness and the shared-displacement constraint; it is not generally an equal split.

This model assumes the plates are rigid, the bars share the same end displacement, and each bar remains uniform, axially loaded, and linear-elastic. Different lengths or areas change the member stiffnesses; gaps, flexible joints, eccentric loading, temperature effects, yielding, or time-dependent behavior require additional relations. The example demonstrates the equilibrium–compatibility–constitutive sequence and is not a real component design or safety basis.

## Assumptions and model checks

Before using the equations, state the load path and boundary conditions: what is restrained, where the axial load enters, and whether the bar can expand or contract freely in the axial direction. The equations describe internal response between the end conditions; a fixed end supplies a reaction, but it does not alter force divided by area into a different stress definition. If temperature change is restrained, if the load is eccentric, or if the part carries bending or torsion as well as axial force, the simple one-dimensional result is incomplete. Weeks 4 and later treat torsion, bending, stress concentrations, and combinations explicitly.

Then check the material response. `E` is useful when the stress-strain response is approximately linear and recoverable over the strain range of interest. Once a metal yields, a polymer creeps, a soft tissue relaxes, a porous scaffold compacts, or a hydrated material changes with rate or orientation, one constant modulus may not describe the response. In anisotropic materials the modulus depends on direction; in viscoelastic materials it can depend on time and loading rate. A single number can be a teaching input without being a measured value for a real object. This package uses synthetic examples and supplies no design allowables.

A disciplined calculation therefore follows the sequence **load and boundary model → units → equilibrium → compatibility where needed → constitutive relation → stress and extension → assumption check**. If a result is implausibly large, check area units, convert GPa to MPa when using N/mm², and test whether the predicted strain remains within a credible linear-elastic range. A small computed extension is not proof of safety: failure criteria, defects, fatigue, instability, environmental effects, and appropriate uncertainty margins belong to other analyses. These introductory relations are for formative learning only, not a design basis or advice for an implant, fixture, scaffold, or other real component.

## Reference

MIT OpenCourseWare, **2.001 Mechanics & Materials I**, Fall 2006, is a link-only comparator. Lectures 7 and 14 introduce compatibility and force-deformation relations; the readings also schedule static indeterminacy and truss deformation. This reading selects a simpler synthetic parallel-bar example and does not copy or adapt MIT notes, figures, problems or other assets.
