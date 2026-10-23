# MOS operating regions and small-signal amplification

The op-amp abstraction hides internal device behavior. An elementary transistor stage makes operating-region checks visible and shows why a small-signal gain is a conclusion near a valid bias point. This original reading uses a prescribed ideal n-channel MOS model and a resistive drain load. It does not specify a real transistor, fabrication process or hardware build.

## Declare the stage and coefficient convention

Ground the source, prescribe gate voltage $V_G$, and connect drain resistance $R_D$ to a positive supply $V_{DD}$. The drain voltage is $V_D$ and current $I_D=(V_{DD}-V_D)/R_D$ flows from supply through the resistor and device. Gate current is zero in this ideal static model. Let $V_{ov}=V_G-V_{th}$ and choose a positive coefficient $\kappa$.

For positive overdrive, stipulate saturation current $I_D=\kappa V_{ov}^2/2$ only when $V_D\geq V_{ov}$. In the triode region, $0\leq V_D<V_{ov}$, stipulate $I_D=\kappa(V_{ov}V_D-V_D^2/2)$. For $V_G\leq V_{th}$ use the ideal off approximation $I_D=0$. The factor one half is part of this coefficient convention; another definition of a device parameter may absorb it.

These selected laws omit body effects, channel-length modulation, leakage, capacitance and many other properties. Saturation here names a transistor operating region, not a clipped op-amp output. Always combine the chosen device branch with the drain load line and check the inequalities after solving.

## Worked saturated bias and local gain

Use $V_{DD}=10$ V, $R_D=2$ kilo-ohms, $V_G=3$ V, $V_{th}=1$ V and $\kappa=1$ mA/V². Overdrive is two volts, so the saturation candidate has current 2 mA and drain voltage 6 V. Since six exceeds two, the candidate satisfies its region condition.

Within that branch, $g_m=\partial I_D/\partial V_G=\kappa V_{ov}=2$ mS. The small-signal drain gain is $dV_D/dV_G=-g_mR_D=-4$. This sign reflects inversion: increased gate voltage raises drain current and lowers drain voltage through the resistor. It is not a statement that every finite change follows the same linear rule.

For a mathematical gate increase of 0.1 V, the local prediction is drain 5.6 V; the full quadratic saturation law gives 5.59 V and still satisfies the region. Compare the discrepancy under smaller perturbations. The bias power ledger has supply 20 mW, resistor loss 8 mW and transistor power 12 mW, closing independently of the small-signal gain calculation.

## Distinct rehearsal

Take $V_{DD}=12$ V, $R_D=3$ kilo-ohms, $V_G=2.5$ V, $V_{th}=1$ V and the same stipulated coefficient 1 mA/V². Overdrive is 1.5 V. The saturation candidate is $I_D=1.125$ mA and $V_D=8.625$ V, comfortably above overdrive within this model. Transconductance is 1.5 mS and local gain is -4.5.

Retain units when multiplying kilo-ohms by millisiemens: their product is dimensionless. A drain-voltage ratio or the current divided by gate voltage is not automatically the derivative $g_m$. When the device law and supply/load boundary change, rederive the sensitivity rather than copying a familiar gain formula.

## Reject a branch that violates its own assumption

For a separate rehearsal perturbation set $V_G=4$ V while preserving the other rehearsal coefficients. Overdrive becomes three volts. The saturation formula would predict 4.5 mA and drain voltage -1.5 V, violating its region condition and the intended nonnegative drain domain.

Instead solve the triode law with the load line. The admissible root is

$$V_D=\frac{10-\sqrt{28}}3\approx1.56949913\ \mathrm V,$$

with current $(12-V_D)/3\approx3.47683362$ mA. Verify both the original current equation and $0\leq V_D<3$. The other algebraic quadratic root does not satisfy that branch's domain and must not be selected by a solver merely because it is real.

In the triode branch, implicit differentiation gives

$$\frac{dV_D}{dV_G}=-\frac{R_D\kappa V_D}{1+R_D\kappa(V_{ov}-V_D)}.$$

It differs from the saturation expression because current also responds to drain voltage. A correct local model must be linearized at the correct operating point and branch.

## A conditional input boundary

The rehearsal's saturation boundary occurs at $V_D=V_{ov}$. Combining that equality with the saturated current and load line gives $1.5V_{ov}^2+V_{ov}-12=0$. The admissible overdrive is $(-1+\sqrt{73})/3$, hence gate voltage about 3.51466792 V. This is a model branch boundary, not a real input-rating or guaranteed linear signal range.

The off and conducting states can illustrate a static inversion abstraction, but they do not establish logic thresholds, noise margins or complete CMOS/digital design. Those require additional definitions and evidence. The [MIT OCW 6.002 Spring 2007 calendar](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/calendar/) lectures 5 and 9–12 supply link-only MOS/large-signal/small-signal scope. All examples and text are original and AI-assisted; no manufacturer device data or source circuit is imported. Broader semiconductor/digital foundations, workload and qualified review remain open; the course stays partial and unreviewed.
