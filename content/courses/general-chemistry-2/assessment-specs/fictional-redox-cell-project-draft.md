# Fictional redox cell and charge accounting: inactive project draft

**Status:** authoring draft only. It is not scheduled, assigned, submitted, collected or graded. The symbols `A` and `B` denote fictional bookkeeping tokens, not elements or chemical species. The half-cell potentials and activities are synthetic teaching values, not a cell specification or laboratory procedure.

## Stipulated half-reactions and inputs

Use these formal standard reduction reactions:

\[
A^{2+}+2e^-\rightleftharpoons A(s),\quad E_A^\circ=-0.200\;V,
\]

\[
B^{3+}+3e^-\rightleftharpoons B(s),\quad E_B^\circ=+0.400\;V.
\]

At `T=298.15 K`, take `R=8.314 J/(mol·K)` and `F=96,485 C/mol e⁻`. For a separate nonstandard-state calculation, use dimensionless activities `a(A²⁺)=0.100` and `a(B³⁺)=0.0100`; pure-solid activities are one. For the charge-accounting part only, stipulate `I=0.200 A` for `30.0 min` with 100% Faradaic efficiency.

## Work sequence

1. Select the cathode, reverse and scale the anode half-reaction, and write the balanced net reaction. Check both electron count and net charge.
2. Calculate `E°cell`, `ΔG°=−nFE°cell`, and `ln K=nFE°cell/(RT)`. State why a large `K` is consistent with the sign of `ΔG°`.
3. Form the reaction quotient omitting pure solids. Use the Nernst equation to calculate the cell potential for the supplied activities and compare its sign with the standard-state value.
4. Convert the specified current and time to total charge, moles of electrons and reaction extent. Use stoichiometry to find the corresponding amount of A consumed and B³⁺ reduced.
5. State which assumptions—especially standard-state conventions, activity modeling, temperature and Faradaic efficiency—would need evidence in a real electrochemical system. Do not infer a real material or experimental procedure.

## Author calculation key

The B couple is the cathode reduction; oxidation of A is `A(s)→A²⁺+2e⁻`. After multiplying by three and two respectively, the net reaction is

\[
3A(s)+2B^{3+}\rightarrow3A^{2+}+2B(s),\qquad n=6.
\]

Both sides carry charge `+6` and the same A/B token counts. The standard cell potential is `0.400−(−0.200)=0.600 V`; `ΔG°=−6(96,485)(0.600)=−347,346 J/mol reaction`. Thus `ln K≈140.126` and `log₁₀K≈60.856`. For the nonstandard example, `Q=a(A²⁺)^3/a(B³⁺)^2=10`; the Nernst equation gives `E≈0.590141 V`, still positive for these stipulated activities.

The charge passed is `It=360 C`, or `360/96,485=0.00373115 mol e⁻`. Dividing by six gives extent `ξ=0.000621858 mol reaction`, corresponding to `3ξ=0.00186557 mol A consumed` and `2ξ=0.00124372 mol B³⁺ reduced`. These are arithmetic consequences of the fictional half-reactions, not measured yields.

## Proposed unweighted review rubric

| Criterion | Evidence for future human review |
|---|---|
| Redox balance | Chooses the correct cathode/anode directions and balances electrons and charge |
| Thermodynamics | Computes the cell potential and Gibbs-energy sign consistently |
| Equilibrium | Forms `Q` with the correct powers and applies the Nernst sign |
| Charge accounting | Converts current-time to charge, electron moles and reaction extent |
| Scope | Keeps fictional symbols separate from real chemical and laboratory claims |

The rubric has no point weights or automatic prose grader. Workload, accessibility, chemical accuracy and instructional design need qualified review. Do not activate this draft or describe it as a course assessment until those reviews and the course's missing homework, exams and laboratory sequence are addressed.

## Provenance

Original authoring and fictional numerical inputs, CC BY 4.0, developed with substantial AI assistance. No third-party dataset or real-world procedure is included.
