# Assignment 2: device bias and amplifier-region evidence

This open report connects an ideal transistor constitutive law with a drain load line, local gain and finite perturbations. It asks for an admissible operating region before a small-signal conclusion. All supplies, coefficients and states are invented mathematical inputs, not recommended components or a build procedure. Retain diagrams, calculations, code and report locally; selected browser responses do not grade the complete analysis.

## Part A: a distinct saturated bias

Ground an ideal n-channel MOS source, prescribe its gate and connect the drain to $V_{DD}=9$ V through $R_D=2$ kilo-ohms. Use $V_{th}=1$ V and coefficient $\kappa=0.5$ mA/V² in the foundation's convention $I_D=\kappa V_{ov}^2/2$ for saturation. At the first gate level $V_G=3$ V, overdrive is two volts.

The saturation candidate is 1 mA and drain voltage 7 V. Verify that seven is at least the overdrive. The local transconductance is 1 mS and the saturated small-signal drain gain is -2. Derive each quantity from the declared equations, preserving milli/kilo unit factors and the inversion sign.

Draw the load line and the relevant piece of the device relation, mark the operating point and list the inequalities that admit it. A real quadratic root or a familiar gain formula is insufficient without this region check. Compare the derivative with a numerical small gate perturbation and retain the original nonlinear calculation as the reference.

## Part B: reject a saturated candidate at a different gate

For a separate point keep all coefficients fixed and set $V_G=5$ V. Overdrive is four volts. The saturated current candidate would be 4 mA and the drain voltage one volt, which violates the assumed $V_D\geq V_{ov}$ condition. Do not keep that candidate and merely call the device “clipped.” It belongs to the wrong constitutive branch.

Use the triode law $I_D=\kappa(V_{ov}V_D-V_D^2/2)$ with the same load line. The admissible solution is $V_D=5-\sqrt7\approx2.35424869$ V and current $(9-V_D)/2\approx3.32287566$ mA. Check both original equations and $0\leq V_D<4$. Explain why the other root does not supply another admissible operating point for this branch.

Derive the implicit small-signal gain for the triode branch and compare it with the saturated expression. The drain dependence of current adds a denominator term. Changing branch without changing the local model can therefore give the wrong gain even if one voltage happens to look plausible.

## Part C: power and finite perturbation evidence

At each admitted point, calculate supply input, resistor loss and transistor power using compatible voltage/current references. Verify their sum independently of the region inequality. A network power balance can close for a candidate pair that does not satisfy the chosen device branch, so it does not replace the constitutive check.

Implement the piecewise ideal model with documented region selection. Sweep a normalized gate interval crossing the selected branch boundary, and retain the off, saturated and triode conditions used at each point. This is a mathematical model sweep rather than a real gate-rating or reliability study. Missing capacitance, body effects and heating remain omitted assumptions.

Choose small gate perturbations within one branch and compare local predictions with re-solved values. Then choose a perturbation crossing a branch boundary and explain why the original single-branch derivative need not describe the full change. Refine both numerical root tolerance and perturbation size separately; a precise solve of the wrong branch is still the wrong model.

## Part D: abstraction and evidence

Describe how the ideal off/conducting behavior could support a qualitative inversion abstraction, then identify what is absent for a real digital-gate claim: prescribed input/output logic levels, noise margins, loading, timing and device evidence. The report does not develop a complete Boolean/CMOS course from one transistor stage.

Compare the transistor analysis with the existing op-amp abstraction. Both require operating-domain checks, but their constitutive equations and internal information differ. The transistor's saturation region is not synonymous with an op-amp output rail. Keep those terms attached to their actual models.

Retain one intentionally invalid branch selection and show the inequality/residual that rejects it. Your analysis should distinguish algebraic existence, model admissibility, local gain, finite signal response and physical device validity. A browser-correct numeric response establishes only one selected calculation.

## Self-review and scope

The retained report should include reference and load-line diagrams, both operating points, rejected candidates, branch-specific sensitivities, power ledgers and perturbation evidence. [MIT OCW 6.002 Spring 2007 calendar](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/calendar/) lectures 9–12 provide link-only MOS amplifier/large-signal/small-signal scope. All explanations and problems are original and AI-assisted; no source device table, circuit or assessment is imported. Broader semiconductor/digital theory, experimental competence, measured workload and qualified review remain open; the course stays partial and unreviewed.
