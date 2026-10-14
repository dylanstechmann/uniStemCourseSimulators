# Cardiovascular and respiratory transport

This lesson connects three transport steps: bulk flow moves blood or air through a network, diffusion moves a dissolved gas across an exchange surface, and regional matching determines whether fresh air and blood reach the same parts of that surface. Keep the driving gradients and the assumptions of each model visible; a useful analogy does not make the systems identical.

## Pressure, flow, and resistance

For a steady flow through a segment, define the pressure drop in the direction of flow as $\Delta P=P_{upstream}-P_{downstream}$. Hydraulic resistance is $R=\Delta P/Q$, so $Q=\Delta P/R$. A larger pressure drop raises flow when resistance is fixed; a larger resistance lowers it when the pressure drop is fixed. Pressure is a driving difference, flow is a rate, and resistance describes how much pressure difference is needed per unit flow. The electrical analogy is voltage difference, current, and resistance, respectively.

For a straight, rigid, cylindrical tube carrying a steady laminar Newtonian fluid, Poiseuille's relation gives

$$R=\frac{8\mu L}{\pi r^4}, \qquad Q=\frac{\Delta P\,\pi r^4}{8\mu L}$$

Here $\mu$ is dynamic viscosity, $L$ is tube length, and $r$ is radius. Doubling length or viscosity doubles ideal resistance; doubling radius divides it by $2^4=16$. At fixed pressure drop, flow therefore rises sixteenfold. This strong fourth-power dependence is a model result, not a direct prediction for a living vessel: vessels branch, deform, pulse, change tone, and may not satisfy the tube assumptions. In a real network, pressure and resistance can change together.

**Worked example.** Suppose an idealized tube carries 0.50 mL/s at a fixed pressure drop. If its radius doubles while length, viscosity, and the pressure drop stay fixed, its resistance becomes $1/16$ as large and its modeled flow becomes $16(0.50)=8.0$ mL/s. The arithmetic tests the model's scaling; it does not claim that a biological vessel can undergo this isolated change.

## Combining pathways

Resistances in series share the same flow and add: $R_{eq}=R_1+R_2$. Their pressure drops add to the total. Parallel branches share the same pressure drop while their flows add, so $1/R_{eq}=1/R_1+1/R_2+\cdots$. Two equal branches each with resistance 8 flow-units-per-pressure-unit have an equivalent resistance of 4. At a shared pressure drop of 12 units, each branch carries 1.5 flow units and the combined flow is 3. Opening or closing a branch redistributes flow even if the total driving pressure is unchanged.

Compliance describes storage rather than steady flow: $C=\Delta V/\Delta P$. A compliant chamber changes volume substantially for a given pressure change. Resistance and compliance together can shape how quickly a system responds, but the simple definitions alone do not specify a full pulsatile or branching model.

## Diffusion across an exchange surface

Bulk flow delivers gas near an exchange surface; diffusion carries molecules across it down a partial-pressure gradient. A compact form of Fick's diffusion relation is

$$\dot n \propto \frac{D A}{T}\,\Delta P$$

where $\dot n$ is transfer rate, $D$ summarizes diffusivity, $A$ is exchange area, $T$ is barrier thickness, and $\Delta P$ is the partial-pressure difference across the barrier. Under otherwise fixed conditions, doubling area doubles modeled transfer, while doubling thickness halves it. Solubility and molecular properties contribute to $D$. This relation describes diffusion across the barrier; it does not replace the flow of air into the lung or blood through capillaries.

**Synthetic calculation.** Let $D=0.4$ in an arbitrary consistent unit system, $A=50$, $T=20$, and $\Delta P=4$. The proportional transfer index is $0.4\times50\times4/20=4$. If area doubles with the other quantities fixed, the index is 8; if thickness doubles instead, it is 2. These invented values illustrate proportional reasoning and are not measurements or physiological reference values.

## Ventilation, perfusion, and matching

Ventilation ($\dot V$) is air delivered per time; perfusion ($\dot Q$) is blood delivered per time. Their ratio $\dot V/\dot Q$ summarizes regional matching, but the ratio must be interpreted for a region and with consistent flow units. For a synthetic region receiving 0.8 L/min of ventilation and 1.0 L/min of perfusion, the ratio is 0.8. Whole-organ totals do not reveal how air and blood are distributed among regions, so adequate total ventilation and perfusion can coexist with poor matching.

A region with ventilation but little or no perfusion has high $\dot V/\dot Q$ and behaves like wasted ventilation (dead-space-like). A region with perfusion but little or no ventilation has low $\dot V/\dot Q$ and behaves like shunt-like flow. These are limiting descriptions; real regions can fall between the extremes. Changing either side of the ratio can alter the mix of blood leaving the lung, even when the other total is unchanged.

## What limits gas uptake?

Follow partial pressure along the capillary as blood moves past an exchange surface. If capillary partial pressure approaches alveolar partial pressure early in transit, diffusion across the barrier has largely equilibrated that blood. Additional uptake then depends mainly on bringing more unsaturated blood to the surface, so transfer is perfusion-limited in that setting. If the two partial pressures have not approached equilibrium by the end of transit, diffusion across the barrier or the available gradient remains limiting. The classification is about equilibration over the available transit time, not simply about naming a gas.

Ventilation limitation is a third possibility: fresh gas delivery to the exchange region is inadequate. A low regional ventilation-to-perfusion ratio can reduce the gas available to blood even if the barrier itself is intact. Thus, distinguish (1) airflow delivery, (2) diffusion across the barrier, and (3) blood-flow delivery. Oxygen partial pressure also does not equal total oxygen content when binding is present; content and delivery are developed separately in the Fick-principle lesson.

## Common mistakes

- Treating $Q=\Delta P/R$ as a claim that flow always rises when pressure rises, without checking whether resistance also changed.
- Applying the fourth-power radius result to a living network without stating the rigid-tube assumptions.
- Adding parallel resistances directly instead of adding their reciprocals.
- Calling every gas-transfer limit “diffusion,” even when ventilation or perfusion is the bottleneck.
- Inferring regional ventilation-perfusion matching from whole-lung totals alone.
- Equating gas partial pressure with total gas content.

## Check your model

Before calculating, identify the pathway or region, the driving gradient, the quantity held fixed, and whether the question concerns flow, diffusion, or matching. Then check units and boundary assumptions. In the ideal tube question, doubling radius at fixed pressure drop multiplies flow by 16. In the capillary-equilibration question, early equilibration means more perfusion can carry more gas; failure to equilibrate points toward a diffusion or gradient limitation. These are formative model checks, not clinical rules.
