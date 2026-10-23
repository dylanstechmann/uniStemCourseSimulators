# Parallel gas exchange: mix oxygen content before pressure

Ventilation supplies gas to exchange units; perfusion carries blood through them. Different units can return blood with different oxygen contents, and their flows determine the mixed output. This reading extends [respiratory mechanics](11-respiratory-mechanics-and-gas-exchange.md), [oxygen content/Fick balance](05-oxygen-delivery-and-the-fick-principle.md) and [pressure/flow](10-hemodynamics-pressure-flow-resistance-compliance.md). All curves, pressures and flows here are invented mathematical inputs, not measured blood values or health targets.

## The conserved quantity in blood mixing

For two streams with blood flows Q1,Q2 and oxygen contents C1,C2, oxygen amount per time entering a mixer is Q1C1+Q2C2. With no accumulation or loss, total flow is Q1+Q2 and mixed content is

$$C_a=\frac{Q_1C_1+Q_2C_2}{Q_1+Q_2}.$$

Use content in mL oxygen per liter blood and flow in liters per minute, with the same oxygen-volume reference conditions throughout. The numerator is then mL oxygen per minute. A flow-weighted average of partial pressures generally does not conserve oxygen when blood content is a nonlinear function of pressure. This concerns mixing binding blood streams, not a blanket rejection of ideal-gas mixture laws.

Ventilation/perfusion mismatch can produce heterogeneous exchange, but a measured mixed content alone cannot identify every unit's ventilation, perfusion and diffusion behavior. The general context is supported by link-only [OpenStax A&P 2e gas exchange](https://openstax.org/books/anatomy-and-physiology-2e/pages/22-4-gas-exchange). The nonlinear curve below is an original deliberately simplified teaching relation.

## A stipulated nonlinear content curve

Let C(P)=Cmax P²/(K²+P²), with positive P and K in the same pressure units. Cmax has content units. This toy relation omits dissolved oxygen and is not a fitted human hemoglobin curve. Assume every stream and the final equilibrated mixture share the same binding conditions. For 0<C<Cmax, solving the relation gives P=K sqrt[C/(Cmax−C)]. Invert the mixed content only after the amount balance; averaging the original pressures answers a different question.

If temperature, binding capacity, pH or other conditions differed, a single shared inverse curve would not automatically apply. At C approaching Cmax the inverse becomes very sensitive, and values above Cmax have no admissible finite pressure in this selected model. That failure would challenge the supplied observation/model combination, not justify taking a square root of a negative value.

## Worked parallel-unit balance

Use Cmax=200 mL/L and K=30 pressure units. Unit one returns at P1=90, giving C1=180 mL/L; unit two returns at P2=30, giving C2=100. With Q1=3 and Q2=2 L/min, mixed content is (540+200)/5=148 mL/L. The equivalent common-condition pressure is 30 sqrt(148/52), about 50.61164. Direct pressure averaging would give 66, which does not produce the same content under the supplied curve.

Oxygen delivery is Qtotal Ca=740 mL/min. If the common mixed-venous content is stipulated 60 mL/L and storage is steady, whole-body uptake is Qtotal(Ca−Cv)=440 mL/min. The same result follows by adding unit uptakes 3(180−60)+2(100−60). Delivery, uptake and extraction fraction are different quantities; a content alone supplies none of the flow information needed to determine them.

## Compare flow boundary conditions

Holding the output contents fixed while redistributing a fixed total five L/min to Q1=4,Q2=1 gives Ca=164 mL/L and delivery 820 mL/min. This is a controlled mixing comparison. In a real exchange model, changing flow can also change each unit's content through transit and ventilation/perfusion effects, so those fixed-output assumptions need evidence.

Alternatively, hold a common driving pressure difference fixed and let branch resistances determine flows. Increasing the resistance of one branch can reduce total flow, not merely redirect a fixed flow. Mixed content may then rise even while total oxygen delivery falls. The [parallel-flow assignment](../assignments/coursework-02-gas-flow-and-evidence.md) derives both cases and asks which boundary was held fixed before interpreting a change.

## An equivalent bypass parameter is not a unique mechanism

Suppose a different two-stream representation mixes content Ccap with unoxygenated-return content Cv in fractions 1−q and q. Algebra gives q=(Ccap−Ca)/(Ccap−Cv), when the denominator is nonzero. In the worked example, using Ccap=180 and Cv=60 gives q=4/15. That parameter can represent the same mixed-content deficit without showing that either original exchange unit was an anatomical bypass. Several heterogeneous exchange patterns can yield the same Ca.

Check 0≤q≤1 and whether Ca lies between the proposed endpoint contents. If both endpoints are equal, every q gives the same mixed content and the parameter is unidentifiable. A calculated fraction outside the interval rejects that particular mixture model/input combination. It does not identify a real disease or treatment response.

## Rehearsal and evidence

For rehearsal take Cmax=180, K=20, P1=60,P2=20, Q1=2,Q2=1 and common Cv=54. Derive both unit contents, mixed content, equivalent pressure, delivery, uptake and extraction. Compare the equivalent pressure with the weighted pressure. Keep full precision and label each ratio's numerator and denominator.

A usable interpretation should state the shared content curve, steady storage, flow boundaries and measured endpoints. Additional evidence is needed to distinguish ventilation, diffusion, perfusion and bypass explanations. [MIT OCW HST.542J Organ Transport Systems Spring 2004 calendar](https://ocw.mit.edu/courses/hst-542j-quantitative-physiology-organ-transport-systems-spring-2004/pages/calendar/) is a link-only respiratory/integration scope comparator. The explanation, curve, inputs and tasks are original and developed with substantial AI assistance; no source problem, figure or measured data was imported. Qualified review and measured workload remain open, and the course remains partial and unreviewed.
