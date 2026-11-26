# State properties, energy balances and binary phase equilibrium

Thermodynamic reasoning begins with a system boundary and a state description. A state property depends on the equilibrium state, not the route used to reach it. Internal energy is a state property; heat and work are energy transfers associated with a process path. Pressure, temperature, specific volume and composition can define aspects of state under an appropriate model. A stream table may list these variables, but listing them does not supply an equation of state or a property method.

## First- and second-law accounting

The first law is conservation of energy. For a closed system, a change in stored energy is balanced by heat and work interactions with stated sign conventions. For an open steady control volume, entering and leaving stream energy, heat transfer and work must be included with flow-work treatment represented by enthalpy where appropriate. Accumulation disappears only under a declared steady assumption. Kinetic and potential energy terms may be negligible in one model and important in another.

A reduced sensible-energy example uses ṁcp(Tout−Tin). With synthetic mass flow 5 kg/s, constant cp = 2 kJ/(kg·K), and a rise from 8 to 20 on the declared Celsius scale, the term is 120 kW. The temperature difference has the same size in kelvin. This result assumes constant cp, one phase, no reaction-energy contribution and no omitted heat, shaft-work or accumulation terms. A phase change cannot be represented by simply extending the same sensible term through the transition. Strong property variation or reaction requires a more complete property and energy model.

The second law adds entropy accounting and constraints on process direction. Energy conservation alone does not establish spontaneity or reversibility. An ideal reversible comparison can bound performance, but a real process includes entropy generation. The second law does not replace the first law, and neither law supplies equipment dimensions or an operating target. Exergy, detailed cycles, statistical thermodynamics, fugacity methods and broad property prediction are deliberately deferred to deeper distinct packages.

## Model-domain checks

Before applying an energy equation, identify phases, reaction terms, work modes, time dependence and the property basis. Check whether heat-capacity values are constant over the stated interval and whether reference states cancel. When enthalpy differences come from a table or correlation, their units, reference and domain must match. Do not mix absolute and relative temperature scales in expressions that require an absolute temperature. Do not assign zero to an unreported heat effect.

Invalid models can still yield tidy arithmetic. A positive calculated duty may be numerically correct for a reduced equation while the equation omits the dominant physical contribution. A second-law audit asks whether the proposed path and heat-transfer direction are plausible, not merely whether inputs and outputs sum. A model audit should state which terms were neglected and what observation would make that neglect unacceptable.

## Phase equilibrium and synthetic K values

At vapor–liquid equilibrium, component chemical potentials or fugacities are related across phases under a suitable thermodynamic formulation. This survey replaces that complexity with declared synthetic K values, y_i = K_i x_i. K_A = 2.5 and K_B = 0.4 are teaching constants for generic A and B, not measurements, identifiers or predictions for a real binary mixture. Constant K values cannot reproduce general composition, temperature or pressure dependence.

For feed mole fractions z_A = 0.6 and z_B = 0.4, let V be vapor moles per mole of feed and L = 1−V. Component and total balances give z_i = (1−V)x_i + Vy_i. Substitution of y_i = K_ix_i gives x_i = z_i/[1+V(K_i−1)] and y_i = K_ix_i. The Rachford–Rice form used in practice is Σ z_i(K_i−1)/[1+V(K_i−1)] = 0.

For the declared values, the equation is 0.9/(1+1.5V) − 0.24/(1−0.6V) = 0. Cross-multiplication gives 0.9−0.54V = 0.24+0.36V, so V = 0.66/0.90 = 11/15 = 0.7333333. Then x_A = 2/7, y_A = 5/7 = 0.7142857, x_B = 5/7 and y_B = 2/7. Liquid and vapor mole fractions each sum to one, and a feed-component balance closes.

## Valid and invalid flash branches

A numerical root is admissible for the two-phase model only when 0<V<1, denominators remain nonzero and all compositions are physically meaningful. Roots at the boundaries require careful interpretation as single-phase limits rather than automatic acceptance as two-phase solutions. If both declared K values are below one, the stipulated binary system does not supply an interior two-phase root; the correct action is to reject that branch, not force V = 0.5. If both exceed one, the same caution applies from the other direction.

Even an admissible algebraic result remains conditional on the synthetic K model. A real flash calculation would need a validated property method, consistent phase stability analysis and appropriate data. This reading does not provide those tools or an operating condition. It provides a small, reproducible example of how material balances and declared equilibrium relations combine, and how domain checks prevent meaningless roots from being reported as separations.


## Evidence and use boundary

This original reading is part of an explicitly partial university-level survey. It is unreviewed and formative-only. Every process, stream, property and observation is synthetic and fictional; generic labels A, B and S do not identify real chemicals. Worked precision supports reproducible arithmetic, not measurement accuracy. Arithmetic closure is not proof of safe or feasible operation. No real production recipe, hazardous condition, plant operating target, controller setting, line or pump sizing, equipment rating, relief sizing, or safety/release approval is supplied. Qualified scientific, engineering, safety and instructional review remains unresolved.
