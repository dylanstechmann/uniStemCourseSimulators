# Ideal reactors, selectivity, RTD and model boundaries

Reaction engineering combines stoichiometry, rate laws, material balances and energy balances. The ideal batch, continuous stirred-tank and plug-flow reactor models differ primarily in their mixing and concentration-history assumptions. A learner should derive or identify the balance before using a conversion formula. Reactor labels alone do not guarantee performance, and a computed conversion is not an equipment design.

## Rate laws and constant-parameter models

A rate law specifies how a reaction rate depends on concentration and other variables under a declared model. For a synthetic first-order consumption of A, r_A = kC_A. The parameter k has units consistent with the rate and concentration definitions. An elementary reaction mechanism should not be inferred merely because a simple empirical rate law fits a teaching example. Multiple reactions require rates for each pathway and a clear distinction between species production and consumption.

The following calculations assume isothermal operation, constant k, constant volume or a corresponding steady volumetric-flow definition, and no transport limitation. Those assumptions make the algebra transparent but narrow. Temperature-dependent kinetics, reversible reactions, catalysis, biological rates, diffusion within structured media and parameter estimation remain deeper topics.

## Batch, CSTR and PFR conversion

For an isothermal constant-volume batch reactor with first-order consumption, the material balance leads to C_A = C_A0exp(−kt). Conversion X = 1−C_A/C_A0 is therefore 1−exp(−kt). With synthetic k = 0.2 min⁻¹ and t = 10 min, X = 1−exp(−2) = 0.8646647. The remaining A fraction is exp(−2), not the conversion.

For a steady ideal CSTR, the contents are assumed perfectly mixed, so outlet concentration equals the uniform reactor concentration. A first-order steady balance gives X = kτ/(1+kτ), where τ is the declared space time. With k = 0.2 min⁻¹ and τ = 5 min, kτ = 1 and X = 0.5. Perfect mixing is a strong assumption; it is not interchangeable with the batch concentration history.

For an ideal PFR, fluid elements progress without axial mixing in the idealization, and concentration changes along the reactor. The first-order integrated result is X = 1−exp(−kτ). At the same k and τ = 5 min, X = 1−exp(−1) = 0.6321206. Comparing this with the CSTR value is valid only for the shared assumptions and definitions. It does not establish a universal ranking for other kinetics, densities, recycle policies or thermal conditions.

## Multiple reactions and selectivity

Consider parallel synthetic reactions A→B and A→S with r_B = k_BC_A and r_S = k_SC_A². The local ratio is r_B/r_S = k_B/(k_SC_A). Concentration therefore affects which pathway dominates. At high concentration in this example, the second-order undesired pathway becomes relatively more important. Other order combinations can reverse the trend.

Selectivity depends on rate ratios integrated over the concentration history, while conversion describes total A consumption. High conversion can accompany poor desired-product selectivity. Reactor choice, feeding strategy and concentration trajectory may matter, but no universal recommendation follows without parameters and objectives. Yield combines conversion and selectivity and must use a declared feed denominator. Separation and recycle can change overall performance even when single-pass kinetics are unchanged.

## Residence-time distributions

Ideal reactor models assume particular flow behavior. A residence-time distribution, or RTD, describes the distribution of times fluid elements spend in a vessel. Its shape can reveal bypassing, stagnant regions or mixing patterns that depart from ideal assumptions. A tracer-response interpretation requires an appropriate experimental or simulation model; this package uses the concept only and supplies no physical procedure.

RTD evidence does not replace kinetics or an energy balance. Two systems can share a mean residence time and have different distributions and conversion. Models such as tanks in series or combinations of ideal regions can organize nonideal behavior, but their parameters and assumptions must be justified. A distribution alone does not uniquely identify every internal flow pattern.

## Nonisothermal and coupled boundaries

When temperature changes, material and energy balances become coupled. Rate and equilibrium parameters vary with temperature, heat exchange affects the energy balance, and conversion in turn affects reaction-energy terms. Adiabatic and nonadiabatic models require different declared boundary conditions. Multiple steady states and stability questions may arise even in relatively simple nonlinear systems.

Transport resistances can also alter observed rates. A bulk concentration need not equal the concentration where reaction occurs. Coupled diffusion and reaction, catalyst effectiveness and multiphase transfer therefore cannot be added as an afterthought without checking the model. Likewise, using an isothermal formula with an average temperature is not generally equivalent to integrating a temperature-dependent rate.

A defensible reactor audit identifies the mixing model, rate law, parameter units, space-time definition, energy assumptions and evidence for neglecting transport. It recomputes conversion and selectivity with their own denominators, examines RTD evidence separately, and marks nonisothermal or coupled behavior as outside a reduced model when necessary. The numerical result remains conditional and non-operational.


## Evidence and use boundary

This original reading is part of an explicitly partial university-level survey. It is unreviewed and formative-only. Every process, stream, property and observation is synthetic and fictional; generic labels A, B and S do not identify real chemicals. Worked precision supports reproducible arithmetic, not measurement accuracy. Arithmetic closure is not proof of safe or feasible operation. No real production recipe, hazardous condition, plant operating target, controller setting, line or pump sizing, equipment rating, relief sizing, or safety/release approval is supplied. Qualified scientific, engineering, safety and instructional review remains unresolved.
