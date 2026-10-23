# Indeterminate beams: compatibility, energy and support contact

**Status:** original ungraded instruction with substantial AI assistance. Beams, loads and stiffnesses are synthetic. This reading extends the existing elastic axial-compatibility and beam-deflection lessons to a redundant beam reaction. It is not a structural design, rating or operating instruction.

## Equilibrium is necessary but does not close every structure

A cantilever fixed at A and supported vertically at its far end B has a vertical reaction at A, a fixing couple at A and a vertical reaction at B. With only a vertical distributed load, force and moment equilibrium give two independent equations for those three quantities. Geometry and material response supply the missing relation: the end deflection must match the support displacement while contact is maintained.

Use an ideal straight beam of length L with constant flexural rigidity EI, small Euler–Bernoulli deflection and a uniform downward load w per length. Let R_B be positive upward. Define end deflection downward positive. The baseline structure removes the support at B, leaving a cantilever whose downward end deflection under w is δ_w=wL⁴/(8EI). An upward endpoint force R_B produces an opposing end deflection R_B L³/(3EI).

For an undeformed support level, compatibility is δ_w−R_B L³/(3EI)=0. Thus R_B=3wL/8. Force balance gives R_A=5wL/8. Equilibrium alone did not determine this sharing; it also used the selected stiffness model and displacement condition.

## Separate external reaction couple from internal bending sign

Take counterclockwise external moment positive. Whole-beam equilibrium about A gives M_A+R_B L−wL²/2=0, so the external fixing couple is +wL²/8. Under the common sagging-positive internal bending convention, the internal moment immediately to the right of A is −wL²/8. These have opposite signs because they describe different actions on different free bodies.

For a cut at x from A, the internal functions are

V(x)=5wL/8−wx,
M(x)=−wL²/8+(5wL/8)x−wx²/2.

Check dM/dx=V and dV/dx=−w. At x=L, M=0; the left-limit shear is −3wL/8 and the upward support reaction jumps it back to zero. The non-end zero of M occurs at x=L/4. Maximum positive bending occurs at V=0, x=5L/8, with M=9wL²/128. Its magnitude is smaller than the fixed-end hogging magnitude wL²/8.

A correct reaction calculation does not automatically yield a correct moment diagram. Verify endpoints, jumps, derivative relations and units before using M in a stress formula. A sign error in the external fixing couple can produce an apparently plausible diagram that fails the far-end moment condition.

## Recover compatibility through strain energy

The bending energy of a linear-elastic beam is U=integral M(x)²/(2EI) dx. For a hypothetical downward endpoint load P on the released cantilever, the generalized end displacement is ∂U/∂P under the appropriate linear-elastic assumptions. Equivalently, the unit-load expression uses the product of the actual moment and the moment from a unit generalized force.

For the downward uniform load on a cantilever, M_w(x)=−w(L−x)²/2 and the moment due to a unit downward endpoint load is m(x)=−(L−x). Then δ_w=integral M_w m/(EI) dx=wL⁴/(8EI). The endpoint flexibility is f_BB=integral m²/(EI) dx=L³/(3EI). Compatibility therefore gives R_B=δ_w/f_BB for the level prop.

This derivation can extend to a supplied varying EI(x) by retaining it inside both integrals. Substituting one average EI without justification may change reaction sharing. The method still assumes a valid beam kinematics/material model; it does not automatically include shear deformation, large rotation, plasticity or connection compliance.

## A worked synthetic beam

Use L=2 m, w=400 N/m and EI=20000 N m². The released end deflection is 400×2⁴/(8×20000)=0.040 m. Endpoint flexibility is 2³/(3×20000)=1/7500 m/N. The level-prop reaction is 300 N, with R_A=500 N and external fixing couple 200 N m. The fixed-end internal bending moment is −200 N m.

The positive moment maximum is 9×400×2²/128=112.5 N m at x=1.25 m, and the contraflexure point is x=0.5 m. These values close the force, moment and displacement ledgers under the stated ideal assumptions. They say nothing about the suitability of a real beam or support.

## Settlement requires a contact model

If support B settles downward by Δ while staying in contact, compatibility becomes δ_w−R_B f_BB=Δ. Thus R_B=3wL/8−3EIΔ/L³. For the worked beam at Δ=0.010 m, R_B=225 N. The other reactions must be recomputed from equilibrium; the original level-prop reactions no longer apply.

A simple prop can push upward but cannot pull the beam downward. If the contact formula predicts R_B<0 for a sufficiently large positive settlement, enforcing that negative force would introduce a tie-down absent from the model. Instead contact is lost: R_B=0 and the beam is the released cantilever, provided its deflection leaves a nonnegative gap to the settled support.

With downward displacement positive, define gap g=Δ−δ_B. The unilateral conditions are R_B≥0, g≥0 and R_B g=0. At contact g=0; at separation R_B=0. For Δ=0.050 m in the worked case, the free cantilever deflects 0.040 m, leaving a 0.010 m gap. The negative algebraic contact reaction is not a physically admissible prop force.

## Rehearsal and report

Use a separate beam L=1.5 m, w=600 N/m and EI=30000 N m². Derive its level reactions, external fixing couple, contraflexure point and positive-moment maximum. Compute released end deflection and then test settlements of 0.005 m and 0.020 m. Decide contact before reporting the final reactions.

Include labeled free bodies, both moment sign conventions, compatibility/energy derivation, unit checks, support assumptions and equilibrium substitutions. Distinguish a structural-model prediction from material or connection validation. An acceptable algebraic residual does not establish a missing contact constraint or a real component's capacity.

The [MIT OCW 2.001 Fall 2006 syllabus](https://ocw.mit.edu/courses/2-001-mechanics-materials-i-fall-2006/pages/syllabus/) and [readings](https://ocw.mit.edu/courses/2-001-mechanics-materials-i-fall-2006/pages/readings/) supply a link-only indeterminacy/deflection/energy-method scope comparator. This original selected example does not deliver the full truss/frame sequence. No source problem, diagram or data was imported. Original material is CC BY 4.0 with AI assistance; qualified review and measured workload remain open.
