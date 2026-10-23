# Assignment 2: coupled electrochemical and solvent balances

**Open, ungraded paper/simulation practice with substantial AI-assisted authoring.** Proposed placement: week 10. These are separate fictional transport models, not observations or operating instructions. The browser checks selected arithmetic and interpretation fields; code, derivations, plots and reports are not automatically evaluated.

## Part A: a direction-labeled ion transfer

At T=300 K, use R=8.314 J/(mol K), F=96485 C/mol and charge number z=+1. Positive transfer is A to B. The supplied activity ratio is a_B/a_A=3 and ψ_B−ψ_A=−0.010 V, with the same species standard state on both sides.

Calculate the chemical, electrical and total electrochemical changes per mole. Decide whether the declared transfer is uphill or downhill, and find the voltage difference that would make that ion's transfer thermodynamically neutral. Keep the voltage difference in volts in the energy equation; millivolts require an explicit conversion.

Reverse the transfer direction and independently change the charge number to −1 in two separate sensitivity calculations. Explain which terms change sign in each case. Do not infer a multi-ion membrane potential from this single-species equilibrium condition.

## Part B: a coupled energy budget

Suppose an auxiliary process has actual Gibbs-energy change −10000 J per mole of coupling events under the declared reservoir conditions. If each event drives an integer ν moles of the Part A ion transfer, compute ΔG_total=−10000+νΔμ_tilde. Find the largest positive integer ν with a strictly negative total and verify the next integer fails that criterion.

Distinguish this thermodynamic bound from a demonstrated molecular mechanism, rate or efficiency. Explain why a standard reaction Gibbs energy alone would be insufficient if actual activities differed. The supplied auxiliary energy is a fictional model input, not a universal biochemical constant.

## Part C: solvent flow between closed reservoirs

A separate ideal-dilute model has an impermeant neutral solute: n_A=0.004 mol and n_B=0.008 mol. Initial liquid volumes are V_A=V_B=0.002 m³. The solvent-permeable interface has area 0.001 m² and stipulated L_p=10^−12 m/(Pa s), reflection coefficient one and zero A-minus-B hydrostatic pressure difference. Temperature remains 300 K.

Write c_A=n_A/V_A and c_B=n_B/V_B. Define positive volume flow Q from A to B. With the stated linear constitutive law, Q=A_mem L_p RT(c_B−c_A), dV_A/dt=−Q and dV_B/dt=Q. Derive these signs from the osmotic-pressure difference rather than memorizing a formula. Check that total volume and each solute amount remain constant.

Compute initial concentrations, initial Q and its direction. Find the equilibrium volumes algebraically by setting c_A=c_B while preserving total volume and solute amounts. Do not freeze the initial concentration gradient while claiming to solve the closed-reservoir dynamics: solvent motion changes both concentrations.

## Part D: a reproducible numerical study

Integrate the volume equations locally, using a declared method and time scale. Select a time horizon relative to the model's rates rather than pretending the tiny coefficient gives a measured device timescale. Guard against nonpositive volumes, since concentration becomes undefined there. Compare numerical equilibrium with the independent algebraic result.

Report time-step/tolerance refinement, total-volume drift, nonpositive-state failures and whether the signed flow approaches zero. A projection that forces the volume total after every step can conceal an implementation defect; if used, explain its role and show an unprojected diagnostic too. Record code/software versions, parameters and units.

The near-linear law is a constitutive assumption. Its coefficients have not been measured and need not remain constant outside the declared regime. Neither an equilibrium solution nor a stable numerical trace establishes real membrane behavior.

## A separate worked solvent calculation

For ΔP=5000 Pa, ΔΠ=3000 Pa, σ=1 and L_p=2×10^−12 m/(Pa s), the positive A-to-B solvent flux is 4×10^−9 m/s under the A-minus-B difference convention. It follows directly from L_p(ΔP−ΔΠ). This fixed-gradient example illustrates the flux law; it does not replace the changing-volume reservoir balances above.

## Self-review and report

Initially the closed-reservoir concentrations are 2 and 4 mol/m³. The osmotic term drives solvent from A toward B, so A's volume decreases. Total volume is 0.004 m³; equilibrium gives V_A=0.004/3 and V_B=0.008/3 m³. The sum remains 0.004 m³ and both concentrations become 3 mol/m³. Check these equalities independently before interpreting a numerical solution.

A report must distinguish the ion energy ledger, the coupled reaction budget and the separate neutral-solute solvent model. Show units, signs, balances, parameter assumptions and model limitations. Give text descriptions of plots and disclose outside calculations and AI assistance. No real membrane, cell or clinical parameter is represented.

The original packet is CC BY 4.0. [MIT OCW 20.110J Fall 2005 calendar](https://ocw.mit.edu/courses/20-110j-thermodynamics-of-biomolecular-systems-fall-2005/pages/calendar/) and [20.330J Spring 2007 syllabus](https://ocw.mit.edu/courses/20-330j-fields-forces-and-flows-in-biological-systems-spring-2007/pages/syllabus/) are link-only scope comparators. No source assessment or code was imported; qualified review and measured workload remain open.
