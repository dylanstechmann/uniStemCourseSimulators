# Truss deformation and statically indeterminate trusses

**Status:** original ungraded instruction with substantial AI assistance. Trusses, loads, areas and moduli are synthetic. This reading joins the week-1 truss statics to the week-3 axial stress, strain and compatibility lesson. It is not a structural design, rating or serviceability instruction.

## Learning objectives

1. Calculate the length change of a truss member from its force, length, cross-sectional area and modulus.
2. Find a joint displacement of a determinate truss by geometric compatibility and by the unit-load method, and check one against the other.
3. Solve a truss that is statically indeterminate to one degree by adding a compatibility equation to equilibrium.
4. Explain how relative member stiffness redistributes force in an indeterminate truss, and state the assumptions that limit these results.

## From member force to member length change

In the week-3 axial lesson, a uniform bar of length L, cross-sectional area A and Young's modulus E carrying an axial force F changes length by

  δ = F L / (A E).

The product AE is the bar's **axial rigidity**, and AE/L is its **axial stiffness**, the force per unit stretch. In a truss, each member is a two-force member, so this relation applies to every bar once its force is known. With the tension-positive convention from the truss statics lesson, a positive δ is an elongation and a negative δ a shortening.

Units need care. With F in newtons, L in metres, A in square metres and E in pascals, δ comes out in metres. A 400 mm² bar is 4.00 × 10⁻⁴ m², and E = 200 GPa is 2.00 × 10¹¹ Pa, so AE = 8.00 × 10⁷ N. Convert before multiplying.

## Joint displacement by compatibility

A member's length change is the stretch of the line between its two end joints. For small displacements, if joint P moves by (u_P, v_P) and joint Q by (u_Q, v_Q), and the unit vector from P to Q is (c, s), then

  δ_PQ = (u_Q − u_P)c + (v_Q − v_P)s.

Only displacement along the member changes its length. Movement across the member to first order only rotates it. Writing this equation for enough members, together with the support conditions, gives the joint displacements.

**Worked example 1.** A synthetic triangular bracket has a pin at A (0, 0), a roller at B (8, 0) and an apex C (4, 3), with dimensions in metres. The legs AC and BC are 5 m long, and AB is 8 m. A downward load of 12 kN acts at C. Every member has AE = 8.00 × 10⁷ N.

*Forces.* The reactions are 6 kN upward at each support. At A, ΣFy gives 6 + (3/5)F_AC = 0, so F_AC = −10 kN (compression), and ΣFx gives F_AB + (4/5)F_AC = 0, so F_AB = +8 kN (tension). By symmetry F_BC = −10 kN.

*Length changes.*

- δ_AB = (8,000 N)(8 m)/(8.00 × 10⁷ N) = +0.800 mm.
- δ_AC = δ_BC = (−10,000)(5)/(8.00 × 10⁷) = −0.625 mm.

*Displacements.* A is pinned, so u_A = v_A = 0. The roller at B allows only horizontal motion, and AB lies along x, so u_B = δ_AB = 0.800 mm. By symmetry C moves horizontally half as far, u_C = 0.400 mm. For member AC, the unit vector from A to C is (4/5, 3/5):

  −0.625 = (0.400)(0.8) + v_C(0.6), so v_C = −1.575 mm.

The apex drops 1.575 mm. The geometry, not just the shortening of the legs, sets that number: the spreading of the base adds to the drop.

## Joint displacement by the unit-load method

Compatibility becomes tedious for large trusses. The **unit-load method**, a virtual-work result, finds one displacement component in one sum. Apply a unit force at the joint, in the direction of the displacement wanted, find the member forces f produced by that unit load alone, and combine them with the real forces F:

  Δ = Σ F f L / (A E).

For worked example 1, the real forces are proportional to the load, so the unit-load forces are f = F/(12 kN): f_AB = 2/3 and f_AC = f_BC = −5/6. Then

  Δ_C = [(8,000)(2/3)(8) + 2(−10,000)(−5/6)(5)] / (8.00 × 10⁷)
   = (42,667 + 83,333)/(8.00 × 10⁷) m = 1.575 mm, downward.

The two methods agree, which is the check to make every time. The unit-load method gives a displacement in the direction of the unit load; a positive result means the joint moves in that direction. It rests on the same assumptions as compatibility: linear elastic members, small displacements and equilibrium written on the undeformed geometry.

## Statically indeterminate trusses

When m + r > 2j, the joint equations cannot give every force. Each extra member or reaction needs one extra equation, and it comes from deformation: the members must still fit together after they stretch. The approach is the same one the week-3 lesson used for parallel bars and the week-6 lesson used for a propped beam:

1. **Equilibrium**, with one unknown more than the equations.
2. **Compatibility**: the joints are shared, so the member length changes are tied together by geometry.
3. **Force–deformation**: δ = FL/(AE) for each member.

**Worked example 2.** A load P = 30 kN hangs from joint D, which is held by three bars attached to a rigid ceiling. The centre bar is vertical and 4 m long. The two side bars run from ceiling points 3 m to either side and are 5 m long, so each makes an angle with the vertical whose cosine is 4/5. All three bars have AE = 8.00 × 10⁷ N.

*Count.* The truss has j = 4 joints (D and three ceiling pins), m = 3 bars and r = 6 reactions (two at each ceiling pin). Then m + r − 2j = 3 + 6 − 8 = 1: one degree indeterminate. Only joint D has unknown forces, and it gives two equations for three bar forces.

*Equilibrium at D.* By symmetry the side bars carry equal force F_s and D moves straight down. Vertically, F_c + 2(4/5)F_s = P.

*Compatibility.* If D moves down by v, the centre bar stretches by v. Each side bar stretches by the component of v along it, v(4/5).

*Force–deformation.* F_c = (AE/4)v and F_s = (AE/5)(4/5)v = 0.16AE·v.

Substituting into equilibrium: AE·v(0.25 + 2 × 0.16 × 0.8) = AE·v(0.506) = 30,000 N, so v = 0.741 mm. Then F_c = 14.8 kN and F_s = 9.49 kN. Check: 14.8 + 2(0.8)(9.49) = 30.0 kN.

The centre bar carries more than either side bar because it is shorter and aligned with the load, so it is stiffer in the direction D moves.

## Stiffness redistributes force

In a determinate truss, member forces depend only on geometry and loads. Make a member stiffer or softer and its force does not change; only the deflections do. In an indeterminate truss, the stiffer path attracts more of the load.

Double the centre bar's AE in worked example 2 and solve again: F_c rises to 19.8 kN and F_s falls to 6.35 kN, while v drops to 0.496 mm. The centre bar's force grew by about a third, not by a factor of two, because the side bars still share the same displacement. Redundancy can be useful, since a structure with an extra load path need not collapse when one member fails. It also means that a misfit, a support settlement or a temperature change puts force into members even with no applied load, which is not possible in a determinate truss.

## Limits of the model

These results assume pinned joints, loads only at joints, linear elastic members, small displacements and equilibrium written on the undeformed geometry. They fail when a compression member buckles (week 10), when a member yields (week 8 plastic redistribution), when joints slip or are rigid enough to bend members, or when displacements are large enough to change the geometry. A computed deflection is a model prediction for those conditions, not a measured or certified property of a real frame.

## Common mistakes

- Mixing units in FL/(AE), for example millimetres squared with gigapascals and newtons, and losing factors of a thousand.
- Taking a joint displacement equal to the length change of one member, and forgetting that other joints also move.
- Using the real member forces in place of the unit-load forces f, or applying the unit load in a different direction from the displacement wanted.
- Treating an indeterminate truss with equilibrium alone, or assuming the extra load shares equally between members of different stiffness.
- Applying these linear results after a compression member has buckled or a joint has slipped.

## Scope and sources

MIT OpenCourseWare 2.001 Mechanics & Materials I, Fall 2006, schedules "Trusses and Their Deformations" (lecture 9) and "Statically Determinate and Indeterminate Trusses" (lecture 10), and is used as a link-only scope comparator ([syllabus](https://ocw.mit.edu/courses/2-001-mechanics-materials-i-fall-2006/pages/syllabus/)). The 2.001 readings assign a commercial textbook that was not read. This reading, its examples and its derivations are original; no source text, problem, figure or data is imported. Matrix stiffness analysis and the formal virtual-work derivation of the unit-load method are not taught here. Original material is CC BY 4.0 with AI assistance; qualified review and measured workload remain open.
