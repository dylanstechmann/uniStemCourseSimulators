# Torsion and bending

A slender member can carry an internal torque that twists its cross-section, a bending moment that curves its centerline, or both. These internal resultants arise at a cut through the member and keep each separated part in force and moment balance. The stresses they create depend on the section geometry as well as the applied load. This reading develops two ideal elastic relations: torsional shear stress in a circular shaft and normal stress in a beam under bending. Both are first models, not universal stress formulas for arbitrary shapes or materials.

## Circular shafts in torsion

Imagine a straight, circular shaft held at one end and twisted by a torque `T` at the other. The torque is carried across the cross-section by shear stress. For a prismatic circular shaft in elastic torsion, the shear stress at radial distance `r` from the center is

**τ(r) = Tr/J,**

where `J` is the polar second moment of area of that cross-section. For a solid circle of diameter `d`, **J = πd⁴/32**; for a hollow circle with outside diameter `dₒ` and inside diameter `dᵢ`, **J = π(dₒ⁴ − dᵢ⁴)/32**. The greatest magnitude occurs at the outer radius `c`, so **τ_max = Tc/J**. At the shaft axis, `r = 0`, the idealized shear stress is zero; it grows linearly with radius under this model.

For a solid shaft, substituting `c = d/2` gives **τ_max = 16T/(πd³)**. That cubic diameter dependence makes geometry consequential: at fixed torque, doubling a solid shaft's diameter reduces its ideal maximum shear stress to one-eighth. A larger outside radius does not help if material is removed in a way that also changes `J`; calculate the section property for the actual idealized geometry. `J` is a geometric quantity with units of length to the fourth power, not a material property.

As a units check, take a synthetic solid shaft with `d = 20 mm = 0.020 m` under `T = 12 N·m`. Its outer radius is `c = 0.010 m`, and `J = π(0.020 m)⁴/32 = 1.571 × 10⁻⁸ m⁴`. Thus `τ_max = (12 N·m)(0.010 m)/(1.571 × 10⁻⁸ m⁴) = 7.64 × 10⁶ N/m² = 7.64 MPa`. The dimensions reduce to force per area. If the radius is entered in millimeters while torque is in N·m, the mixed units must be converted before evaluating the expression.

The relation assumes a straight, uniform circular section, torque about the shaft axis, and a region away from grips, shoulders, keyways, abrupt changes, and load-introduction details. It also uses an elastic material response and the classical circular-shaft stress distribution. A noncircular shaft can warp and does not generally use the circular `J` formula or the same linear distribution. Local stress concentrations, plastic twist, anisotropy, and bonded or layered construction need additional models. Shear stress from torsion is distinct from the normal stress in axial loading and bending; if several load types act together, their stress components must be combined at the same point using an appropriate later analysis.

## Beams in bending

A beam's internal bending moment `M` creates tension on one side of a cross-section and compression on the other. In elementary elastic beam theory, the longitudinal normal stress varies with signed distance `y` from the neutral axis:

**σₓ(y) = −My/I.**

The sign depends on the moment and coordinate convention; the magnitude is **|σₓ| = |M y|/I**. Here `I` is the area second moment of the section about the neutral axis in the bending direction. At the neutral axis, `y = 0`, the ideal longitudinal bending stress is zero. At the farthest surface, `|y| = c`, its maximum magnitude is **σ_max = |M|c/I**. `I` also has units of length to the fourth power, but it is an area moment about a particular axis. It is not interchangeable with the polar quantity `J` used in shaft torsion.

For a rectangle of width `b` and depth `h`, bent about the centroidal axis parallel to its width, **I = bh³/12** and `c = h/2`. Consider the preserved practice example with `b = 0.050 m`, `h = 0.100 m`, and `M = 500 N·m`. Then `I = (0.050 m)(0.100 m)³/12 = 4.167 × 10⁻⁶ m⁴`, and `c = 0.050 m`. The extreme-fiber stress magnitude is `(500 N·m)(0.050 m)/(4.167 × 10⁻⁶ m⁴) = 6.00 × 10⁶ Pa = 6.00 MPa`. The unit check again gives force per area. Reversing the moment swaps which side is in tension and which is in compression, while keeping the magnitude the same in this symmetric idealization.

Because `h` is cubed in the rectangle's `I`, section depth strongly affects bending stress and stiffness. However, a stress estimate alone does not answer whether the beam deflects too much. Serviceability, stability, fatigue, and material failure are distinct questions. A member may remain elastic yet be too flexible for its intended function. The later beam-deflection reading addresses curvature and deflection; this one uses moment to estimate a nominal cross-section stress.

## What the formulas require

The elementary bending relation is a slender-beam approximation: the member is straight before loading, the section is prismatic over the region considered, deflections and rotations are small enough for the chosen geometry model, and the stress-strain relation is approximately linear and elastic. Its simplest form is most useful away from supports and concentrated load points, where a local three-dimensional stress field can differ from the beam estimate. Transverse shear stress, stress concentrations, shear deformation in short or deep beams, and large rotations are not represented by `My/I` alone.

For a homogeneous isotropic material the neutral axis passes through the centroid in the elementary case. In a composite or direction-dependent section, stiffness distribution and material axes affect the neutral axis and the relation between curvature and stress; inserting one average modulus or treating a porous structure as a uniform solid can be misleading. Likewise, hollow and noncircular sections need their actual area moments, and their local wall behavior may impose further limits. The equations support learning and transparent first calculations, but a real design needs validated geometry, boundary conditions, material data, load combinations, a stated failure or serviceability criterion, and an appropriate review process. This package provides none of those design approvals; the numbers here are synthetic teaching examples.

## A short calculation routine

First draw the member and mark the applied torque or bending moment, the axis, and the section where the internal resultant is being considered. Then identify the section geometry and compute `J` for a circular shaft or `I` about the correct bending axis. Convert all lengths consistently before taking fourth powers. Evaluate the stress at the radius or distance from the neutral axis that the question asks for, and keep the sign convention if tension versus compression matters. Finally, state which idealizations make the number a reasonable nominal estimate and what effects have been left out. This sequence keeps a correct arithmetic answer from being mistaken for a complete component analysis.

## Reference

MIT OpenCourseWare, **2.001 Mechanics & Materials I**, Fall 2006, lecture notes on pure bending and torsion and twisting. The course page is provided as a link-only technical reference; this reading does not copy or adapt its notes, diagrams, exercises, or other assets.
