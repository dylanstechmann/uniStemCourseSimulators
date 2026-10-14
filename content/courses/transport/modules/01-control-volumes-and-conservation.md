# Control volumes and conservation

Transport analysis begins by choosing what to count and where to draw the boundary. A control volume is a region in space through which mass and energy may flow. It can surround a tank, a section of tubing, a chamber, a tissue region, or a connected collection of components. The boundary is an accounting choice: draw it so that the important inputs, outputs, storage, and transformations are visible. Then write a balance before simplifying it.

## Accumulation is a rate of storage change

For any conserved quantity, the rate of accumulation inside a control volume equals the rate that enters minus the rate that leaves, plus any generation inside, minus any consumption inside. For a chemical species A, using mass-flow rates,

**accumulation of A = A in − A out + generation of A − consumption of A.**

The terms must use the same units, such as grams per minute. A rate balance is not a list of concentrations: multiply a concentration by a volumetric flow rate to obtain a species mass-flow rate. If several streams enter or leave, sum each stream's contribution. A reaction can consume one species and generate another while total mass remains conserved across the reacting mixture; species balances include reaction terms even when the total-mass balance does not.

For a well-mixed liquid volume V with constant volume, volumetric inlet flows Qᵢ and outlet flows Qₒ, and concentration C, a simple species balance is

**V dC/dt = Σ(Qᵢ Cᵢ) − Σ(Qₒ C) + R V,**

where R is the net production rate per unit volume (positive for generation, negative for consumption). The well-mixed assumption makes the exiting concentration equal to the tank concentration. If the tank is not well mixed, an outlet concentration may differ from the volume average and a spatial model may be required. Check units: `L × (g L⁻¹ min⁻¹)` and `L min⁻¹ × g L⁻¹` both reduce to `g min⁻¹`.

## Steady does not mean motionless

Steady state means that the stored quantity does not change with time, so its accumulation term is zero. It does not require zero flow, zero diffusion, zero reaction, or zero heat transfer. At steady state, inflow and outflow can be large and equal, and a reaction can be balanced by continuing supply. A system is transient when one or more stored quantities change with time. A tank can have constant total volume while its species concentration is still changing, so state the balance being called steady: total mass, a particular species, energy, or all of them.

For a constant-volume vessel with one inlet, one equal-flow outlet, no reaction, and a uniform concentration, the balance reduces to

**V dC/dt = Q(Cᵢₙ − C).**

The time scale `V/Q` has units of time. When the inlet concentration is switched to a fixed value, the concentration difference from its final value shrinks exponentially with this time scale: `C(t) = Cᵢₙ + [C(0) − Cᵢₙ]e^(−Qt/V)`. A larger volume takes longer to wash in or wash out at the same flow; a larger flow shortens the ideal well-mixed time scale. This relation assumes constant volume and flow, perfect mixing, and no generation, consumption, or bypassing. Real systems may violate any of these assumptions.

With first-order consumption at rate `kC`, the equation becomes `V dC/dt = Q(Cᵢₙ − C) − kVC`. At steady state, set the derivative to zero and solve: `C = Q Cᵢₙ/(Q + kV)`. Here `kV` has units of volume per time, so it can be compared with Q. If reaction is omitted from the boundary accounting, the predicted steady concentration is wrong even though total liquid mass may balance.

## Choose a boundary that exposes the physics

Draw every stream crossing the boundary and label its flow and relevant properties. Decide whether the boundary encloses only fluid, a membrane and both fluid compartments, a reacting region, or an entire apparatus. If a membrane lies inside the boundary, its diffusive transfer is internal; if it lies across the boundary, include that transfer as an input or output. The same physical process can appear as a boundary flux or as an internal generation term depending on the chosen region, but it must be counted once, not omitted or counted twice.

For a moving or expanding liquid volume, the storage term may involve both concentration and volume: `d(VC)/dt`. It is not generally equal to `V dC/dt` if V changes. If liquid is incompressible and the vessel is rigid, constant volume may be a good approximation; otherwise the total-volume balance must support it. Also distinguish mass flow (mass per time) from volumetric flow (volume per time). They are related by density, `ṁ = ρQ`, when density is appropriately defined and known.

## Energy balance and sign convention

For a fixed control volume, one useful rate form of the first law is

**dEcv/dt = Q̇ − Ẇ + Σṁᵢ(hᵢ + vᵢ²/2 + gzᵢ) − Σṁₒ(hₒ + vₒ²/2 + gzₒ).**

Here heat transfer into the volume is positive, work done by the volume is positive, and the stream terms carry enthalpy, kinetic energy, and gravitational potential energy. Each term is energy per time (watts, or kilowatts). At steady state the energy-storage term is zero. Depending on the device and requested accuracy, kinetic, potential, shaft-work, or chemical-energy terms may be negligible, but justify that from the situation rather than dropping them by habit. For reactions, energy released or absorbed by chemical change must be represented consistently, often through enthalpy terms.

As a synthetic calculation, let a steady device have one inlet and one outlet, each at `1 kg/s`. Suppose the inlet specific enthalpy is `100 kJ/kg`, the outlet is `110 kJ/kg`, and shaft work, kinetic-energy change, and potential-energy change are negligible. With heat into the control volume positive, the energy balance gives `Q̇ = 1(110 − 100) = 10 kJ/s = 10 kW`. The positive sign means heat must enter to support the higher outlet enthalpy under these stated assumptions. If the outlet enthalpy were lower, the result would be negative and indicate net heat leaving.

## Worked species-balance example

Consider a well-mixed, rigid `100 L` tank with inlet and outlet flows both `2 L/min`, inlet concentration `5 g/L`, and first-order species consumption with `k = 0.02 min⁻¹`. Its species balance is `V dC/dt = Q(Cᵢₙ − C) − kVC`. At steady state, `C = Q Cᵢₙ/(Q + kV) = (2×5)/(2 + 0.02×100) = 2.5 g/L`. The liquid volume is steady, but the concentration would be transient while approaching that value from a different initial condition.

## A short balance checklist

1. Name the quantity being conserved and draw the control volume.
2. Mark each inlet, outlet, transfer across the boundary, and internal source or sink.
3. Write accumulation = in − out + generation − consumption with consistent signs and units.
4. State whether the balance is transient or steady; set accumulation to zero only for the latter.
5. Simplify only after stating assumptions about mixing, volume, flow, reaction, and energy terms.

All values here are synthetic teaching examples. The equations are balance frameworks, not a protocol or an equipment design method. MIT OpenCourseWare is an optional link-only technical reference; no lecture note, figure, example, or dataset has been copied or adapted.
