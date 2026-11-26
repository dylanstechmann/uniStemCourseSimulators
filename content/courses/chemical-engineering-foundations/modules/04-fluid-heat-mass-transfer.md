# Fluid, heat and mass transfer model concepts

Transport models connect flow, energy and composition to driving forces and resistance. They also illustrate why an equation must be read together with its geometry, regime and property assumptions. This route introduces continuity, mechanical-energy and friction terms, pump/system-curve concepts, series transfer resistance, LMTD, NTU and analogous mass-transfer reasoning. It is a map of ideas, not a substitute for the future distinct fluid-mechanics and heat/mass-transfer packages.

## Continuity and mechanical energy

For steady incompressible flow through a defined average area, volumetric flow Q = vA. A synthetic Q = 0.020 m³/s and A = 0.005 m² gives average speed 4 m/s. This is an area-averaged statement, not a claim that velocity is uniform at every point. Compressible flow, multiple phases, branching or strongly varying profiles require additional accounting. Continuity constrains flow; it does not determine pressure loss or equipment feasibility by itself.

A mechanical-energy balance can relate pressure, elevation, velocity, shaft work and losses between two locations under declared assumptions. A Darcy-friction term has the form h_f = f(L/D)v²/(2g). With synthetic f = 0.020, L/D = 100, v = 2 m/s and g = 10 m/s², h_f = 0.4 m. The factor of two and the chosen Darcy convention matter. Other friction-factor conventions are not interchangeable. The calculation is a stipulated model term, not a line calculation or pressure specification.

The friction factor itself depends on regime and a suitable correlation. Geometry, roughness representation, property values and transition behavior can limit applicability. Applying a convenient correlation outside its declared range is a model error even if the resulting number is positive. Entrance effects, fittings, nonsteady behavior and multiphase interactions may require terms absent from the reduced balance.

## Pump and system curves as concepts

A system curve expresses required head or pressure-related contribution as a function of flow for a stipulated system model, often combining static and flow-dependent terms. An idealized pump curve expresses the head contribution associated with a pump model over a flow range. Their intersection represents a predicted operating intersection for those two curves. Changing a curve changes the intersection.

This concept does not select a pump or size a line. It does not establish available margin, transient behavior, cavitation performance, material compatibility or protective response. Real curves require validated equipment and system information that is intentionally absent. The appropriate educational conclusion is conditional: if the two declared curves are accepted, their intersection is the model solution. No plant operating target follows.

## Series resistance and transfer driving forces

For one-dimensional steady conduction through layers, heat flow can be represented as a temperature difference divided by the sum of thermal resistances. A planar layer has R = L/(kA); a convective boundary has an idealized resistance related inversely to hA. Resistances in series add when the same heat-flow path and steady assumptions apply. Parallel paths require a different combination. Interface geometry, contact behavior and property variation may complicate the simple network.

Mass transfer has an analogous driving-force-and-resistance organization. A flux may be represented by a coefficient multiplied by a concentration-related difference, with phase-specific coefficients and equilibrium relationships needed to construct an overall driving force. Units and concentration bases must be compatible. Adding unlike resistances or mixing phase bases creates hidden errors. Reaction alongside transfer can also change the concentration profile and invalidate a simple resistance addition.

## LMTD and NTU

For an ideal exchanger with terminal temperature differences ΔT1 = 40 K and ΔT2 = 20 K, the logarithmic mean temperature difference is (ΔT1−ΔT2)/ln(ΔT1/ΔT2) = 20/ln2 = 28.8539008 K. It differs from the arithmetic mean of 30 K. When the two terminal differences are equal, the limiting LMTD equals their common value rather than an undefined division. Sign and flow-arrangement conventions must remain consistent.

An ideal Q = UA·LMTD relationship combines the duty, overall conductance and driving force. An energy balance is still required to determine Q and terminal states. The overall U may reflect several resistances referenced to a particular area; referencing the wrong area changes the result. Neither Q nor LMTD alone supplies an exchanger rating.

The effectiveness–NTU approach offers another organization. NTU = UA/C_min uses a declared minimum capacity rate, and effectiveness compares actual idealized duty with a defined maximum. The relation between effectiveness and NTU depends on flow arrangement and capacity-rate ratio. It is not one universal formula for every exchanger. LMTD and NTU can be consistent representations of the same idealized problem, but their assumptions must match.

## Applicability audit

A transfer-correlation checklist asks: What geometry and boundary conditions were used to develop it? Which flow regime and dimensionless range are declared? Are properties evaluated at a consistent basis? Are phases stable and is reaction absent or represented? Does the geometry match the resistance network? How sensitive is the result to uncertain coefficients?

These questions apply equally to heat and mass transfer. A calculated flux, duty or curve intersection is useful only as a conditional model output. Detailed dimensional analysis, boundary-layer theory, transient transport, multiphase flow, radiation, diffusion-reaction coupling, equipment methods and correlation validation remain beyond this bounded survey. Closure of a mechanical-energy or heat-duty equation is not evidence of feasible operation.


## Evidence and use boundary

This original reading is part of an explicitly partial university-level survey. It is unreviewed and formative-only. Every process, stream, property and observation is synthetic and fictional; generic labels A, B and S do not identify real chemicals. Worked precision supports reproducible arithmetic, not measurement accuracy. Arithmetic closure is not proof of safe or feasible operation. No real production recipe, hazardous condition, plant operating target, controller setting, line or pump sizing, equipment rating, relief sizing, or safety/release approval is supplied. Qualified scientific, engineering, safety and instructional review remains unresolved.
