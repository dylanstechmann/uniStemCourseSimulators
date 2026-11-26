# Separation concepts and recovery–purity–energy trade-offs

Separations distribute components among products by exploiting differences in phase behavior, partitioning, selective transport or uptake. They do not create component mass, and their reported performance depends on denominators. This route compares equilibrium-stage and rate-based ideas across distillation, absorption, extraction, membranes and adsorption. It then connects recovery and purity to energy and resource trade-offs. The coverage is intentionally introductory; full stage calculations, transport models and process design remain future work.

## Equilibrium-stage and rate-based viewpoints

An equilibrium-stage model assumes that streams leaving an idealized contact stage have a declared equilibrium relationship. A cascade of such stages can achieve a separation that one contact cannot. Stage efficiency may be introduced to represent departure from equilibrium, but it is an additional model concept rather than a universal constant. Material balances around each stage and the overall unit remain necessary.

A rate-based model instead represents finite transfer rates, area and driving forces between phases or across a selective barrier. Compositions can vary continuously, and equilibrium still supplies boundary or driving-force information where appropriate. Rate-based descriptions require coefficients and applicability checks. Neither viewpoint guarantees a product specification, and neither supplies an equipment rating in this survey.

## Five separation families

Distillation uses differences in volatility and vapor–liquid equilibrium to distribute components between vapor and liquid products. Ideal stages can be organized into a cascade with feeds and reflux-related internal flows, but detailed column methods are deferred. The earlier synthetic K-value flash illustrates only a single equilibrium split, not a complete distillation model.

Absorption transfers a component from one phase into a contacting phase, often described with solubility or phase-equilibrium relationships and interphase mass transfer. The generic component A can have different concentrations in the two phases without those concentrations being numerically equal. Overall and component balances determine how much transferred; rate expressions describe how quickly the idealized approach occurs.

Extraction uses distribution between two contacted phases. For a synthetic single-stage model, define K as the desired-component concentration ratio between phase 1 and phase 2, and R as the corresponding phase-flow ratio. Under a declared dilute ideal balance, the extracted fraction is KR/(1+KR). With K = 3 and R = 2, KR = 6, so 6/7 = 85.7142857% is extracted and 1/7 remains. This simple expression does not describe every multistage, concentrated or nonlinear extraction.

Membrane separation uses selective transport across a barrier. Driving forces can involve differences in chemical potential represented through concentration, pressure-related or other variables under a suitable model. Permeance, selectivity, area and transport resistance influence rate-based performance. High selectivity and high throughput need not coincide, and concentration polarization or other resistances may change the apparent behavior.

Adsorption uses selective uptake onto or within a material. Capacity and uptake rate are different concepts: an equilibrium isotherm does not supply the time needed to approach equilibrium. Cyclic operation introduces loading, regeneration and history questions that are deliberately not turned into an operating sequence here. All five families require conservation, phase or uptake evidence and an applicability audit.

## Recovery, purity and yield

Recovery of A to a desired product is A in that product divided by A in feed. If 100 kg/h A enters and 80 kg/h A reports to product, recovery is 80%. Product purity divides A in the product by total product flow. If the product also contains 15 kg/h B and 5 kg/h S, purity is 80/100 × 100 = 80%. Recovery and purity happen to have the same numerical value in this construction, but they answer different questions and need not coincide.

Overall yield can combine reaction and separation performance. B formed in a reactor is not necessarily B recovered in product. If 42 kg/h B forms and recovery fraction is 0.90, recovered B is 37.8 kg/h. Multiplying a reactor yield by a recovery fraction is valid only when the denominators and bases are compatible. Unknown recovery must remain unknown rather than inferred from a nearby scenario.

## Energy and resource trade-offs

A sharper product split can require additional stages, contact area, selective capacity or another resource, and those changes can alter energy demand. Increasing recovery by taking a broader product cut can reduce purity. Improving purity can reject more desired component to another stream. These are possible trade-offs, not universal monotonic laws; flowsheet structure and model parameters determine actual behavior.

An honest comparison declares the objective, constraints and system boundary for energy accounting. It distinguishes duty from total resource use and avoids treating an ordinal score as a physical measurement. Sensitivity analysis can vary a synthetic recovery or coefficient to see whether a ranking changes. Missing property, kinetic or transfer evidence remains a review gate. Arithmetic closure and attractive recovery percentages are not proof of feasible operation, low energy use, product quality or approval.


## Evidence and use boundary

This original reading is part of an explicitly partial university-level survey. It is unreviewed and formative-only. Every process, stream, property and observation is synthetic and fictional; generic labels A, B and S do not identify real chemicals. Worked precision supports reproducible arithmetic, not measurement accuracy. Arithmetic closure is not proof of safe or feasible operation. No real production recipe, hazardous condition, plant operating target, controller setting, line or pump sizing, equipment rating, relief sizing, or safety/release approval is supplied. Qualified scientific, engineering, safety and instructional review remains unresolved.
