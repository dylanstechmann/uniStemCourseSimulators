# Assignment 3: a conservative transport verification study

**Open, ungraded derivation and local computation with substantial AI-assisted authoring.** Proposed placement: week 14 after the existing transport sequence. All coefficients and fields are synthetic. The browser checkpoints test selected calculations; they do not grade your derivation, implementation, plots or report.

## Part A: assemble a steady model from faces

A one-dimensional domain has length L=0.004 m and constant area A. Divide it into four equal cells with unknown cell-average concentrations. Diffusivity is D=2×10^−9 m²/s. Boundary face concentrations are c_L=2 and c_R=0 mol/m³. There is initially no reaction or advection.

Draw or describe the cell centers, boundary faces and distances used for every flux. Derive the half-cell boundary formulas and the internal-face formula. Assemble the steady linear equations from inflow minus outflow equals zero. Explain why a boundary-face concentration is not the first unknown cell-center value.

Solve the equations and compare them with the exact continuum linear profile c(x)=2(1−x/L). Since this reference is linear, cell averages equal center values. Report all four concentrations and every face flux. A check of one central cell alone can miss an incorrect boundary resistance.

## Part B: a transient no-flux experiment

Change the problem explicitly: use four no-flux cells, no reaction and normalized initial concentrations [0,1,0,0]. Select r=DΔt/Δx²=0.2 and derive the explicit Euler update using only the old vector. Perform the first step by hand and then integrate locally.

Verify nonnegativity and conservation of AΔx sum c_i. The long-time uniform concentration is one quarter of the initial sum because the cell volumes are equal. Test a step beyond the sufficient positivity limit and preserve the resulting failure in the report. Do not silently clip a negative concentration and continue claiming the original update was used.

Compare explicit and backward Euler on a common output grid. Check time-step refinement separately from spatial refinement. A stable implicit trace may be too smooth, and a preserved total may coexist with inaccurate timing. Record which reference or refinement comparison supports each numerical claim.

## Part C: add a first-order sink and close the global ledger

Return to the fixed-concentration boundary problem and add sink s=−k c with k=0.002 s^−1. Derive the modified steady matrix. The discrete global balance should satisfy j_left−j_right=kΔx sum c_i after dividing out constant area. Check that identity directly from the computed face fluxes and cell values.

The continuum reference solves D c″−k c=0 with the same face values. Derive c(x)=2 sinh[λ(L−x)]/sinh(λL), where λ=sqrt(k/D). Compare cell-average values, obtained by integrating this profile over each cell, with the finite-volume unknowns. Comparing a nonlinear profile's point value with a cell average introduces a separate approximation, so label it if you use it as an approximation.

Refine from four to eight and sixteen cells and report spatial errors and global balance errors separately. The reaction-diffusion length sqrt(D/k)=0.001 m is comparable to the original cell width, motivating a mesh study. A tiny matrix residual verifies your discrete equations, not a sufficiently resolved continuum solution.

## Part D: connect transport mechanisms and thermodynamics

Using the existing Péclet-number lesson, compare a characteristic advective velocity with D/L and state when neglecting advection is justified for the declared scale. If adding advection numerically, specify the boundary and face scheme rather than inserting a velocity into only the final flux report.

Explain why the chemical/electrochemical driving-force lessons concern which forces can drive transport, while the present diffusivity and face laws set a model rate. A favorable Gibbs-energy change is not a diffusivity. Conversely, a flux model with a sign error can violate its intended thermodynamic direction even if its matrix equations are solved accurately.

## A separate worked face check

For a three-cell domain of length 0.003 m, D=10^−9 m²/s and boundary values 1 and 0, the exact steady centers are [5/6,1/2,1/6]. All face fluxes are 3.3333333×10^−7 mol/(m² s). The half-cell boundary distance is 0.0005 m, while internal center distances are 0.001 m. Use this separate case to test geometry before running the four-cell assignment.

## Self-review and report

For Part A the four centers are [1.75,1.25,0.75,0.25] mol/m³ and the constant flux is 10^−6 mol/(m² s). For Part B the first update is [0.2,0.6,0.2,0], preserving the sum one. These references check selected steps, not your entire implementation or sink/refinement study.

Include derivations, cell/face definitions, units, code/software versions, solver settings, independent reference calculations, refinement tables and at least one diagnosed failure. Explain every plot in text and disclose tools and AI assistance. Distinguish discrete conservation, continuum accuracy and model validity.

This original packet is CC BY 4.0. [MIT OCW 20.330J Spring 2007 syllabus/calendar](https://ocw.mit.edu/courses/20-330j-fields-forces-and-flows-in-biological-systems-spring-2007/pages/syllabus/) is a link-only conservation/diffusion scope comparator; no external assessment or implementation was copied. Scientific/code/accessibility review and measured workload remain open.
