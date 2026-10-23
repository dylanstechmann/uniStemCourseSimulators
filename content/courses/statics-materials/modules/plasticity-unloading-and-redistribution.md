# Material response beyond an elastic limit: unloading and load redistribution

**Status:** original ungraded instruction developed with substantial AI assistance. Every material law, geometry and load is an invented teaching model. This reading extends the course's yield/failure distinctions into a specific elastic–perfectly plastic constitutive calculation. It is not a characterization, design criterion or prediction for a real material.

## A yield number does not define the whole stress–strain curve

An elastic model gives σ=Eε and returns to zero strain after unloading. A stated yield strength marks a convention or model transition; it does not specify subsequent hardening, fracture strain, cyclic response or unloading without more information. Choose the material law before calculating permanent set.

For a one-dimensional elastic–perfectly plastic tension model, stress is Eε up to ε_y=σ_y/E, then remains σ_y during continued monotonic tensile straining. Unloading is elastic with slope E until another yield condition is reached. Decompose strain as ε=ε_e+ε_p, where ε_e=σ/E and ε_p is the retained plastic part in the stated loading history.

This is a deliberately simple constitutive model. Real materials can harden, soften, depend on rate/temperature, develop damage or exhibit different reverse-yield behavior. A perfectly plastic plateau does not mean unlimited deformation is admissible; the exercise simply omits fracture and instability rather than validating them away.

## A single-bar energy and residual-strain ledger

Take E=100 GPa, σ_y=200 MPa, initial length L=0.10 m and area A=0.0001 m². Under imposed maximum strain ε_max=0.004, yield occurs at ε_y=0.002. The maximum model stress is 200 MPa and force is 20000 N. Plastic strain at that point is 0.004−0.002=0.002.

If the bar is then freely unloaded to zero force without reverse yielding, the elastic strain 0.002 is recovered and the remaining extension is Lε_p=0.0002 m, or 0.2 mm. A calculation that uses σ_max/E as the total maximum strain would miss the permanent part.

The monotonic work input per original volume is the stress–strain area: σ_y²/(2E)+σ_y(ε_max−ε_y)=600000 J/m³. The recoverable elastic energy at the maximum is σ_y²/(2E)=200000 J/m³. The remaining 400000 J/m³ is plastic work under this ideal law. It should not be relabeled as fully recoverable strain energy. For the original volume AL=10^−5 m³, these energies are 6 J input, 2 J recoverable and 4 J plastic work.

Do not equate plastic work with a measured temperature rise without specifying heat conversion, heat capacity and exchange conditions. A mechanical energy partition is not a calorimetry experiment.

## Two parallel bars add compatibility to constitutive behavior

Now use two bars of equal length and equal area A=0.0001 m² between rigid parallel end plates. They share axial strain; assume both can carry tension or compression without buckling in this model. Bar 1 has E_1=100 GPa and σ_y1=100 MPa. Bar 2 has E_2=200 GPa and σ_y2=300 MPa. Both begin unstressed with zero plastic strain.

During common imposed tensile strain, bar 1 yields first at 0.001; bar 2 would yield at 0.0015. At ε_max=0.0012, bar 1 is plastic at 100 MPa, while bar 2 remains elastic at 240 MPa. Their forces are 10000 and 24000 N, so total applied force is 34000 N.

Equilibrium alone cannot divide this total force. Compatibility and the two different material laws determine the sharing. After bar 1 yields, an incremental imposed extension increases its plastic strain while the incremental elastic load is carried by bar 2 under the perfect-plasticity assumption. The tangent stiffness of the assembly changes from A(E_1+E_2)/L to AE_2/L over that regime.

## Remove the external force and solve for the residual state

At the maximum, bar 1 has plastic strain ε_p1=0.0012−100 MPa/(100 GPa)=0.0002; bar 2 has none. During elastic unloading, their stresses are σ_1=E_1(ε−ε_p1) and σ_2=E_2ε. When external force becomes zero, force equilibrium for equal areas requires σ_1+σ_2=0.

Thus the common residual strain is ε_f=E_1ε_p1/(E_1+E_2)=0.00006667. The residual stresses are about −13.333333 MPa in bar 1 and +13.333333 MPa in bar 2. They cancel externally while remaining internally self-equilibrated. At L=0.10 m, residual extension is approximately 6.6666667 μm.

Check the assumed unloading regime: the compressive stress magnitude in bar 1 is below its stipulated reverse-yield magnitude 100 MPa, and bar 2 remains below 300 MPa. If an assumed elastic-unloading solution crossed a yield boundary, the material history would need another branch. Do not accept a convenient elastic formula outside its own constitutive regime.

The assembly's final strain differs from either a freely unloaded isolated plastic bar or an assembly forced back to zero displacement. “Unloaded” must specify whether external force or end displacement is prescribed. Residual stress is compatible with zero external resultant, and residual strain depends on the compatibility constraints.

## Verification and limits

For an all-elastic loading path below the first yield strain, unloading should return both stresses and common strain to zero. Use that limiting case as a test. For identical bars with identical plastic histories, residual stress vanishes at zero external force, although permanent extension can remain. These checks isolate constitutive, equilibrium and compatibility errors.

An actual parallel tie system may not sustain compression; contact/slack or buckling would change the residual problem. The bars here are explicitly bilateral axial members. Similarly, a test-machine crosshead displacement can include fixture compliance; it need not equal specimen strain times gauge length. Those are additional models, not corrections supplied by the toy law.

## Rehearsal and reporting

For a separate free bar, use E=80 GPa, σ_y=160 MPa, ε_max=0.005 and L=0.20 m. Calculate yield strain, permanent strain/extension and input/recoverable/plastic-work densities. Then compare a loading path that reaches only ε=0.001: explain why it leaves no permanent set under the declared law.

For the parallel bars above, recompute stresses and total force at ε_max=0.0011, followed by zero external force. Track plastic strain in each member, solve the common residual strain and verify force cancellation and absence of reverse yield. Show the loading/unloading paths with a text description of the same quantities.

The [MIT OCW 2.001 Fall 2006 syllabus/readings](https://ocw.mit.edu/courses/2-001-mechanics-materials-i-fall-2006/pages/syllabus/) frame force–deformation, compatibility and material/failure behavior. The local perfect-plasticity example is a selected extension, not a claim of full plasticity-course depth. No source exercise, text, figure or dataset was copied. Original material is CC BY 4.0 with disclosed AI assistance; qualified review and measured workload remain open.
