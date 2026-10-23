# Assignment 2: a constitutive history and residual-load report

**Open, ungraded paper/computation practice developed with substantial AI assistance.** Proposed placement: week 14 after material response, compatibility and failure concepts. All properties and geometries are synthetic. The platform checks selected arithmetic fields, not a material characterization, simulation implementation or written argument.

## Part A: a free bar under imposed strain

Use an elastic–perfectly plastic one-dimensional law with E=120 GPa, tensile yield stress 240 MPa, initial length L=0.15 m and area A=0.0001 m². Load monotonically to imposed maximum strain 0.006, then unload to zero force with elastic slope E and no reverse yield.

Derive yield strain, maximum model stress/force, elastic and plastic strain at maximum, and the final permanent extension. Sketch or describe the loading/unloading path and identify which quantities are controlled. A force plateau is not an authorization for arbitrary stable deformation; fracture and instability are simply absent from the chosen law.

Integrate the stress–strain path to compute work input per original volume, recoverable elastic energy and plastic work. Multiply by original volume to obtain energies in joules. Check the energy partition. Explain why plastic work is not automatically a measured heat rise without thermal information.

## Part B: two compatible bars during loading

A separate assembly has two equal-length bars L=0.20 m, each area A=0.0001 m², between rigid parallel end plates. Both start unstressed and can carry either axial tension or compression in this paper model. Bar 1 has E_1=100 GPa and yield magnitude 100 MPa; bar 2 has E_2=200 GPa and yield magnitude 300 MPa. Both obey the same ideal perfectly plastic rule with elastic unloading and symmetric reverse yield.

Impose common maximum strain 0.0013. Determine which bar has yielded, each stress/force and the total applied force. Compute each retained plastic strain at the maximum. Explain why force sharing cannot be found by splitting the external force equally when moduli and histories differ.

Compare the assembly tangent stiffness before first yield with that after bar 1 has yielded but before bar 2 yields. State the displacement-controlled regime in which this comparison is being made. Do not extend a piecewise tangent law past the next yield transition without updating it.

## Part C: unload the assembly to zero external force

Keep the end plates compatible and remove the external resultant. Under an assumed elastic unloading branch, express each stress in terms of the shared final strain and the retained plastic strains. Solve force equilibrium for the final strain. Calculate residual stresses and residual extension.

Verify that the residual forces cancel and that neither member crosses its reverse-yield condition. If the assumed unloading branch were invalid, explain what additional constitutive branch would be required. Distinguish this zero-force condition from returning the plates to zero displacement; the two experiments generally have different external forces and internal states.

State why the assumed ability to carry compression matters. A tie that goes slack or a member that buckles would require contact/stability constraints in addition to the present constitutive law. This assignment does not validate those effects away.

## Part D: limiting cases and evidence

Repeat only the conceptual loading/unloading classification for maximum common strain 0.0008, below either yield strain. Predict whether permanent strain or residual stress remains under the ideal law, and verify your prediction from the equations. Also consider two identical bars with identical plastic histories: explain why residual stress can vanish while permanent extension remains.

Propose what measured information would be needed to replace the toy law with a material-specific model: full loading/unloading curves, gauge/fixture displacement separation, rate/temperature conditions and relevant failure observations. A single yield number cannot identify all of them. Distinguish model verification from experimental characterization.

## Separate worked comparison and self-review

The reading's different single bar uses E=100 GPa, yield 200 MPa, maximum strain 0.004 and length 0.10 m. It has permanent strain 0.002, extension 0.2 mm and work densities 600000 J/m³ input, 200000 recoverable and 400000 plastic. Use that as a calculation test before applying the assignment inputs.

For Part A, yield strain is 0.002, retained plastic strain 0.004 and permanent extension 0.0006 m. Work densities are 1200000 J/m³ input, 240000 recoverable and 960000 plastic. For Part B, maximum stresses are 100 and 260 MPa, giving total force 36000 N. Zero-resultant unloading leaves common strain 0.0001, stresses −20 and +20 MPa and residual extension 0.00002 m. Verify all these results independently and check their constitutive regime.

Report sign conventions, units, controlled quantities, material history, equilibrium/compatibility checks, energy partitions and limitations. Describe diagrams in text and disclose calculations, software and AI assistance. The original packet is CC BY 4.0; [MIT OCW 2.001 Fall 2006 syllabus/readings](https://ocw.mit.edu/courses/2-001-mechanics-materials-i-fall-2006/pages/syllabus/) are link-only scope comparators. No external problem or data was imported. Qualified review and measured workload remain open.
