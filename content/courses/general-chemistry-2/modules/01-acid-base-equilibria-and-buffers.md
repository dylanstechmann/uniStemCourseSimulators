# Acid-base equilibria and buffers

A weak acid does not dissociate completely. Its equilibrium links the acid form HA, the conjugate-base form A⁻, and hydrogen ion. A buffer contains appreciable amounts of both HA and A⁻, so it can consume added strong base or strong acid while shifting their ratio. The ratio helps estimate pH; the total amount of buffer helps determine how much addition it can absorb.

## Relate Ka to acid dissociation

For

$$HA \rightleftharpoons H^+ + A^-,$$

the thermodynamic equilibrium constant is expressed with activities:

$$K_a=\frac{a_{H^+}a_{A^-}}{a_{HA}}, \qquad pK_a=-\log_{10}K_a.$$

Activities account for nonideal interactions. In a sufficiently dilute solution with modest activity effects, they can be approximated by concentrations relative to the standard concentration. In that approximation, $K_a\approx[H^+][A^-]/[HA]$. Smaller $pK_a$ means a larger $K_a$ and a stronger acid under the stated conditions.

For a solution made from a formal concentration $C$ of a weak monoprotic acid, neglect water autoionization and let $x$ dissociate. Then $[H^+]=[A^-]=x$ and $[HA]=C-x$, giving

$$K_a=\frac{x^2}{C-x}.$$

When dissociation is small relative to $C$, the approximation $C-x\approx C$ gives $x\approx\sqrt{K_aC}$. This estimate needs to be checked against the small-dissociation assumption; if $x$ is not small or if water contributes appreciably, solve the full mass and charge balances instead. The equilibrium model also assumes temperature and other conditions are specified, because $K_a$ depends on conditions.

## Derive the buffer pH relation

Starting from the concentration form of the equilibrium expression,

$$[H^+]\approx K_a\frac{[HA]}{[A^-]},$$

take negative base-10 logarithms to obtain

$$pH\approx pK_a+\log_{10}\left(\frac{[A^-]}{[HA]}\right).$$

This is the Henderson–Hasselbalch approximation. The ratio is dimensionless, so the logarithm is defined. A tenfold excess of A⁻ over HA puts the approximate pH one unit above $pK_a$; equal amounts give $pH\approx pK_a$. The equation is most useful when both forms are present in appreciable amounts, the ratio is not extreme (often roughly 0.1 to 10 for introductory estimates), water autoionization is small, and activity effects are modest. It is not an exact identity for arbitrary concentrations or conditions.

**Worked estimate.** If $pK_a=7.2$ and $[A^-]/[HA]=10$, then $pH\approx7.2+\log_{10}(10)=8.2$. For an acetate example with $pK_a=4.76$, $[A^-]=0.20$ M and $[HA]=0.10$ M, the ratio is 2 and $pH\approx4.76+\log_{10}(2)=5.06$. These are estimates under the stated concentration approximation, not a calibration or prediction for a real sample.

## Neutralize first, then re-equilibrate

When strong acid or base is added, first account for the fast stoichiometric reaction with the buffer forms. Added $H^+$ converts A⁻ to HA; added $OH^-$ converts HA to A⁻. Update the amounts, check that neither buffer form has been exhausted, and only then use the new ratio in the equilibrium approximation. Applying Henderson–Hasselbalch to the starting ratio after a substantial addition gives the wrong state.

**Synthetic addition.** Begin with 10 mmol A⁻ and 10 mmol HA, so the initial ratio is 1 and the approximate pH is $pK_a$. Adding 1 mmol of strong acid consumes about 1 mmol A⁻ and forms 1 mmol HA. Before the small re-equilibration adjustment, the amounts are 9 and 11 mmol, so the estimated shift is $\log_{10}(9/11)\approx-0.087$ pH units. The ratio changed even though the total buffer amount stayed 20 mmol. This mole-accounting example is idealized and gives no laboratory preparation or handling instructions.

For a strong-base addition, the same accounting runs in the opposite direction: consume HA and form A⁻. If the added amount exceeds the available component, the buffer model no longer applies in that form; determine the remaining strong acid/base and then solve the appropriate equilibrium. Near low concentrations or extreme pH, include water ionization and use charge balance as well as mass balance.

## Distinguish pH from buffer capacity

At fixed conditions, total buffer concentration $C_T=[HA]+[A^-]$ and the ratio play different roles. The ratio sets the approximate pH, while $C_T$ helps determine how much strong acid or base is needed to change that ratio. Diluting a buffer without changing the ratio leaves the Henderson–Hasselbalch pH estimate unchanged, but reduces the amount of added acid or base it can absorb.

For an ideal monoprotic buffer, neglecting water autoionization and activity corrections, buffer capacity per unit volume can be written

$$\beta=\frac{1}{V}\frac{dn_{\mathrm{base}}}{d(pH)}=2.303C_T\frac{K_a[H^+]}{(K_a+[H^+])^2}.$$

It is largest when $[H^+]=K_a$, equivalent to $pH=pK_a$, where $\beta\approx0.576C_T$ per pH unit. For a synthetic $C_T=0.10$ M buffer, the ideal maximum is about 0.0576 mol/(L·pH unit). This is a local slope near equilibrium, not an amount that can be added while keeping the pH exactly fixed; the buffer ratio and pH change as material is added.

## Common mistakes and model limits

- Using the initial buffer ratio after strong acid or base has reacted; update the mole balance first.
- Treating $pH=pK_a$ as a universal rule; it holds in the approximation when acid and conjugate base activities are equal.
- Inferring high buffer capacity from pH alone; total concentration matters as well as the ratio.
- Taking a logarithm of a dimensional quantity instead of a ratio.
- Using concentration ratios when activity effects, water autoionization, depletion, or extreme pH make those approximations inadequate.

The equations here are equilibrium and amount-accounting models for formative calculations. They do not specify any real buffer recipe, chemical handling procedure, biological compatibility, or pH-control protocol.
