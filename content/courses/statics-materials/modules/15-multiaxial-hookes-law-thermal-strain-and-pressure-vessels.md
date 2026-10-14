# Multiaxial Hooke's law, thermal strain and thin-walled pressure vessels

The [combined-stress lesson](10-principal-stresses-mohrs-circle-and-yield.md) transformed a known two-dimensional stress state into principal stresses and checked it against yield criteria. That lesson took the stresses as given. This one connects them to deformation. A stretched bar also gets thinner, a stress in one direction strains the others, and a temperature change strains a material even with no load. When something prevents those strains, stresses appear. The thin-walled pressure vessel is the standard application: internal pressure produces a biaxial stress state whose principal stresses can be written down from equilibrium alone, and Hooke's law then predicts how much the vessel swells. All materials, loads and geometries here are synthetic teaching values.

The undergraduate [MIT OCW 2.001 Mechanics & Materials I (Fall 2006) syllabus](https://ocw.mit.edu/courses/2-001-mechanics-materials-i-fall-2006/pages/syllabus/) schedules multiaxial stress and strain, multiaxial stress–strain relationships, and stress–strain–temperature relationships with thin-walled pressure vessels (Lectures 12–15) just before stress transformations and principal stress (Lectures 16–17). This lesson follows that grouping within the local combined-stress week. It uses 2.001 as a scope comparator only and reproduces no MIT material.

## Learning objectives

By the end of this lesson, you should be able to:

1. Use Poisson's ratio and the generalized Hooke's law to calculate normal strains from a multiaxial stress state, including lateral contraction and volume change.
2. Calculate thermal strain, the stress in a fully or partly constrained member, and the stress that a lateral constraint induces.
3. Derive and apply the hoop and axial stresses in thin-walled cylinders and spheres, calculate the resulting change in radius, and state when the thin-wall model applies.

## Poisson's ratio

Pull a bar along x with stress σ. It extends by ε_x = σ/E and contracts sideways by

**ε_y = ε_z = −ν ε_x,**

where ν is **Poisson's ratio**. For most isotropic solids ν lies between about 0.25 and 0.35, and it cannot exceed 0.5 for a stable isotropic material; 0.5 corresponds to no volume change.

**Synthetic example.** A rod of diameter 20 mm with E = 70 GPa and ν = 0.33 carries 80 MPa. The axial strain is 80/70 000 = 1.143 × 10⁻³, the lateral strain is −3.77 × 10⁻⁴, and the diameter shrinks by **7.5 μm**. The change is small but measurable with strain gauges, which is how ν is found.

## The generalized Hooke's law

For an isotropic, linear-elastic material, each normal stress strains its own direction by σ/E and the other two by −νσ/E. Adding these effects by superposition gives

**ε_x = [σ_x − ν(σ_y + σ_z)]/E,**

and the same pattern for y and z. Shear strains are γ = τ/G, with G = E/[2(1 + ν)], and in this isotropic model they do not couple to the normal strains.

**Synthetic example.** With E = 200 GPa and ν = 0.30, a plate carries σ_x = 100 MPa, σ_y = 50 MPa and σ_z = 0. Then

- ε_x = (100 − 0.3 × 50)/200 000 = **4.25 × 10⁻⁴**;
- ε_y = (50 − 0.3 × 100)/200 000 = 1.0 × 10⁻⁴;
- ε_z = −0.3 × 150/200 000 = −2.25 × 10⁻⁴.

The plate thins even though nothing pushes on its faces. The **volumetric strain** is the sum, 3.0 × 10⁻⁴, which equals (1 − 2ν)(σ_x + σ_y + σ_z)/E. At ν = 0.5 the factor vanishes, the incompressible limit.

**Constraint creates stress.** If the same plate is held so that it cannot strain in y while σ_x = 100 MPa is applied, then ε_y = 0 requires σ_y = νσ_x = **30 MPa**. The constraint pushes back, and the x-strain becomes (100 − 0.3 × 30)/200 000 = 4.55 × 10⁻⁴, smaller than the 5.0 × 10⁻⁴ of a free bar. A laterally constrained material is effectively stiffer.

## Thermal strain

A temperature rise ΔT expands an unconstrained isotropic material equally in every direction by

**ε_T = α ΔT,**

with α the coefficient of thermal expansion. Free expansion produces no stress. The total strain is the sum of the mechanical and thermal parts: ε_x = [σ_x − ν(σ_y + σ_z)]/E + αΔT.

**Fully constrained bar.** A bar held between rigid walls cannot change length, so the total axial strain is zero and σ = −EαΔT. With E = 200 GPa, α = 12 × 10⁻⁶ K⁻¹ and ΔT = 50 K, the free strain would be 6.0 × 10⁻⁴, and the constrained stress is **−120 MPa**, compressive. That stress does not depend on the bar's length or cross-section.

**Partly constrained bar.** If a 1.000 m bar starts with a 0.10 mm gap at one wall, it first expands freely across the gap. The free expansion would be 0.60 mm, so the remaining 0.50 mm is suppressed and σ = −200 000 × 0.50/1000 = **−100 MPa**. If the free expansion were smaller than the gap, the stress would stay zero.

These stresses can buckle a slender member, which links back to the [strut-buckling lesson](09-buckling-of-slender-struts.md), or crack a brittle one.

## Thin-walled pressure vessels

A closed cylinder of mean radius r and wall thickness t holds internal gauge pressure p. Cut it in half along its length. The pressure acting on the projected area 2rL must be balanced by the hoop stress σ_θ acting on the two wall cuts of area tL:

**σ_θ = pr/t.**

Cut it across instead. The pressure on the end, πr²p, is balanced by the axial stress on the ring of area 2πrt:

**σ_z = pr/(2t).**

A sphere has the same cut in every direction, so its membrane stress is pr/(2t) everywhere. The radial stress varies from −p on the inner surface to zero outside, small compared with pr/t when r/t is large. The usual guide is **r/t ≥ 10**; below that, thick-wall theory is needed.

**Synthetic example.** A cylinder with r = 0.50 m and t = 10 mm holds 2.0 MPa. The hoop stress is **100 MPa** and the axial stress **50 MPa**, the same biaxial state as the Hooke's-law example above. The hoop strain is therefore 4.25 × 10⁻⁴, and the radius grows by 0.50 m × 4.25 × 10⁻⁴ = **0.21 mm**. A sphere of the same radius and thickness would carry only 50 MPa.

Because the hoop stress is twice the axial stress, a cylinder that fails by rupture usually splits along its length. In Mohr's-circle terms, the in-plane maximum shear is (100 − 50)/2 = 25 MPa. Including the near-zero radial stress, the absolute maximum shear is 100/2 = 50 MPa, the value a Tresca check uses.

## Common mistakes

- Forgetting the Poisson terms and writing ε_x = σ_x/E in a biaxial state.
- Assuming a free temperature change produces stress; stress needs a constraint.
- Using the full free expansion when a gap absorbs part of it.
- Swapping the hoop and axial formulas; the hoop stress is the larger.
- Applying thin-wall formulas when r/t is small.
- Using the in-plane maximum shear in a Tresca check when the out-of-plane principal stress is zero.
- Mixing MPa with GPa, giving strains a thousand times too large or small.

## Worked example

**Problem.** A synthetic cylindrical tank of mean radius 0.30 m holds 1.5 MPa gauge pressure. Its material has E = 200 GPa, ν = 0.30, and an allowable hoop stress of 120 MPa. Choose the wall thickness, check the thin-wall assumption and the Tresca shear, and find the fractional change in enclosed volume.

**Step 1: thickness.** σ_θ = pr/t ≤ 120 MPa gives t ≥ 1.5 × 0.30/120 = 3.75 mm.

**Step 2: thin-wall check.** r/t = 0.30/0.00375 = 80, well above 10.

**Step 3: stresses.** σ_θ = 120 MPa, σ_z = 60 MPa and σ_r ≈ 0. The absolute maximum shear is 120/2 = 60 MPa, which must also be acceptable under the chosen shear criterion.

**Step 4: strains.** ε_θ = (120 − 0.3 × 60)/200 000 = 5.1 × 10⁻⁴ and ε_z = (60 − 0.3 × 120)/200 000 = 1.2 × 10⁻⁴.

**Step 5: volume change.** The enclosed volume πr²L changes by the fraction 2ε_θ + ε_z = 1.14 × 10⁻³. That is about 0.11%, small but enough to matter when pressure is inferred from the volume of an almost incompressible fluid.

## Limits of this lesson

All materials, loads and geometries are synthetic. The analysis assumes isotropic, linear-elastic, homogeneous materials, small strains, uniform temperature changes and thin walls well away from ends, joints and openings. Anisotropic or composite materials, temperature-dependent properties, thermal gradients, thick-walled vessels, end-cap and nozzle stress concentrations, plasticity, fatigue and fracture are not developed. Nothing here is a design basis, pressure rating, test protocol or safety assessment for any real vessel, component or implant. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
