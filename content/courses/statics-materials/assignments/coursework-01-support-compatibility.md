# Assignment 1: a redundant support and its admissible contact state

**Open, ungraded derivation/computation practice with substantial AI-assisted authoring.** Proposed placement: week 9 after beam deflection and the new compatibility reading. All geometry, loads, stiffness and settlement values are synthetic. This is a model-verification task, not a structural design or assessment of a real component. Save your free bodies, calculations and report locally or in notes; the browser checks selected fields only.

## Part A: identify what equilibrium leaves unknown

Use a beam fixed at A, length L=1.20 m, constant EI=18000 N m² and uniform downward load w=500 N/m. Its endpoint B rests on a vertical prop at the original level. Define upward reactions positive, counterclockwise external couples positive and downward beam displacement positive.

Draw or describe the whole-beam free body and count unknown reactions. Write independent equilibrium equations. Explain why the endpoint reaction cannot be determined from them alone. Release the prop and derive the end deflection from the load and endpoint flexibility using either integration or the unit-load energy expression.

Apply compatibility for a level support and calculate R_A, R_B and the external fixing couple. Then derive the internal shear and bending functions using a cut-section free body. Keep external reaction-couple signs separate from sagging-positive internal bending. Verify the derivative relations, endpoint moment and shear jump.

## Part B: a settled support still in contact

Move the support downward by Δ=0.002 m. Recompute the redundant reaction from the displacement condition, then use equilibrium to update the other reactions. Check the beam endpoint displacement against Δ using the independently derived flexibility relation.

Derive the revised internal moment function. Find the internal contraflexure point and the location/value of the positive bending maximum. Compare fixed-end moment magnitude with the level-support case. A support settlement can reduce the prop reaction while increasing fixed-end hogging demand; a single reaction trend does not describe every response quantity.

## Part C: test whether contact is admissible

Now prescribe Δ=0.010 m. First calculate the algebraic contact reaction, then test the fact that a prop can push but cannot pull. If contact would require a negative upward reaction, solve the no-contact state instead. Compute the gap between the settled support and the released cantilever endpoint.

State the complementarity conditions R_B≥0, g≥0 and R_B g=0 with your sign convention. Test both candidate states, not only whichever gives an attractive force value. Distinguish a simple prop from a bilateral tie-down, which would be a different structural model and could carry a downward reaction.

## Part D: independent verification

Implement a small local calculation or use exact symbolic/rational work to check the derivation. One independent route is the polynomial displacement field satisfying constant-load beam equations, fixed displacement/slope at A, zero end moment at B and the contact displacement at B. Another is virtual-work flexibility with original moment fields. State which equations and sign conventions each route uses.

For a varying supplied EI(x), outline how the two unit-load integrals would change. Explain why substituting a nominal average stiffness can change an indeterminate reaction even though a determinate structure's equilibrium reactions do not use E. No varying-stiffness numerical data are required here; the aim is to identify the additional model information.

## A separate worked reference

The reading uses L=2 m, w=400 N/m and EI=20000 N m². Its released deflection is 0.040 m and level reactions are 300 N at B and 500 N at A, with external fixing couple 200 N m. A 0.010 m settlement leaves 225 N at B; a 0.050 m settlement separates the prop. Those values test the method on a different input set, not the assignment's beam.

## Self-review after attempting the assignment

For the level assignment prop, R_B=225 N, R_A=375 N and the external fixing couple is +90 N m. At Δ=0.002 m, R_B=162.5 N, R_A=437.5 N and the external fixing couple is +165 N m. The released end deflection is 0.0072 m, so the Δ=0.010 m support lies below the released endpoint and leaves a 0.0028 m gap; the admissible prop reaction is zero there.

These values close the stipulated equilibrium/compatibility/contact problem. They do not check material yield, shear deformation, connection behavior, instability, fatigue or any real structure's safety. Include free bodies, units, moment/shear checks, energy or displacement verification, contact-state logic, a text description of diagrams and disclosure of tools/AI assistance.

The [MIT OCW 2.001 Fall 2006 syllabus](https://ocw.mit.edu/courses/2-001-mechanics-materials-i-fall-2006/pages/syllabus/) is a link-only indeterminacy/deflection/energy-method comparator. This original packet is CC BY 4.0; no source exercise, diagram or data was imported. Qualified mechanics review and measured workload remain open.
