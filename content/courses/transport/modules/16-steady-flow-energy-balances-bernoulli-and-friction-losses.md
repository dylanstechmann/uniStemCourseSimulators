# Energy balances on flowing systems: the steady-flow first law, Bernoulli and friction losses

The [perfusion-tubing lesson](06-perfusion-tubing-balances-and-pressure-drop.md) used mass balances and the Poiseuille relation to find flow rates and pressure drops. This lesson adds energy. The [control-volume lesson](01-control-volumes-and-conservation.md) wrote conservation laws for an open system, and the first law for such a system decides how much heat a warmer must supply or how much work a pump must do. For a liquid flowing without heat transfer, a simpler mechanical energy balance applies. It reduces to **Bernoulli's equation** when friction is negligible, and adds a friction-loss term when it is not. The aim is to know which terms matter in a given flow and which can be dropped. All circuits, fluids and parameter values are synthetic teaching examples, and the liquid is treated as incompressible with constant properties.

The MIT OCW [20.330J Fields, Forces and Flows in Biological Systems (Spring 2007) syllabus](https://ocw.mit.edu/courses/20-330j-fields-forces-and-flows-in-biological-systems-spring-2007/pages/syllabus/) treats pressure-driven internal flow (L7) and then Bernoulli's equation (L8) in its fluid-mechanics sequence. The open-system first law follows the control-volume source already linked from the course's first lesson. This lesson combines them within the local perfusion week. It uses those sources as scope comparators only and reproduces no MIT material.

## Learning objectives

By the end of this lesson, you should be able to:

1. Write the steady-flow first law for a control volume, simplify it for a liquid, and calculate the heating power needed to warm a flowing stream.
2. Apply Bernoulli's equation along a streamline to relate pressure, velocity and height, including hydrostatic feed pressure, efflux speed and a constriction.
3. Use the mechanical energy balance with a Poiseuille friction loss to calculate pump work and power, and judge which terms are negligible.

## The steady-flow first law

For a control volume with one inlet and one outlet at steady state, the energy entering with the flow plus the heat added equals the energy leaving plus the shaft work done by the fluid:

**Q̇ − Ẇ_s = ṁ [Δh + Δ(v²/2) + g Δz].**

Here ṁ is the mass flow rate, h the specific enthalpy, v the mean velocity and z the height. Δ means outlet minus inlet, and Ẇ_s is the work done by the fluid, so a pump's work on the fluid enters as a negative Ẇ_s. For an incompressible liquid with constant specific heat c_p, Δh ≈ c_p ΔT + ΔP/ρ.

**Warming a stream.** A synthetic medium flows at 10 mL/min (ṁ = 1.67 × 10⁻⁴ kg/s) and is warmed from 22 °C to 37 °C. With c_p = 4180 J/(kg·K), the thermal term ṁ c_p ΔT is **10.5 W**. The pressure, kinetic and height terms for a few kilopascals, centimetres per second and centimetres of rise are smaller by factors of thousands, so the heater requirement is set by the temperature change alone. Heat lost through the walls of the tubing would add to the requirement.

## Bernoulli's equation

For steady, incompressible flow along a streamline with no friction, no heat transfer and no shaft work, the mechanical energy per unit volume is constant:

**P + ½ρv² + ρgz = constant.**

**Hydrostatic feed.** In a reservoir at rest, v ≈ 0, so the pressure rises with depth as ρgh. A medium reservoir raised 0.50 m above an outlet supplies 1000 × 9.81 × 0.50 = **4.9 kPa**, about **36.8 mmHg**, of driving pressure before any flow losses.

**Efflux speed.** For a large open tank draining through a small hole a depth h below the surface, both the surface and the jet are at atmospheric pressure, and the surface velocity is negligible. Then v = √(2gh), which is **3.13 m/s** for h = 0.50 m. This frictionless result is an upper bound; real orifices deliver less because of friction and jet contraction.

**Constriction.** Where a tube narrows, continuity forces the velocity up and Bernoulli forces the pressure down. At 5.0 mL/s, flow from a 4.0 mm to a 2.0 mm bore raises the mean velocity from 0.40 to 1.59 m/s and lowers the pressure by ½ρ(v₂² − v₁²) = **1.19 kPa**. Using mean velocities treats the flow as if it were uniform across the tube, which is an approximation for laminar profiles.

## Adding friction: the mechanical energy balance

Real flows dissipate mechanical energy as heat through viscosity. For a liquid with no heat-transfer interest, the first law can be rearranged into a mechanical energy balance per unit mass:

**ΔP/ρ + Δ(v²/2) + g Δz + h_f = w_pump,**

where h_f is the friction loss and w_pump the work per unit mass supplied by a pump. For fully developed laminar flow in a tube of diameter D and length L, the Poiseuille relation gives the frictional pressure loss ρh_f = 128μLQ/(πD⁴).

**Synthetic tubing circuit.** Medium with μ = 0.80 mPa·s flows at 10 mL/min through 2.0 m of 1.6 mm bore tubing. The mean velocity is 0.083 m/s and the Reynolds number is about 170, so the flow is laminar. The friction loss is **1.66 kPa**. The kinetic-energy term ½ρv² is only 3.4 Pa, so it is negligible here. Lifting the medium 0.30 m adds ρgΔz = 2.94 kPa. The pump must supply about 4.6 kPa at 1.67 × 10⁻⁷ m³/s, a hydraulic power of **0.77 mW**. At a synthetic 20% efficiency, that is 3.8 mW of input power.

**Where the lost energy goes.** The friction loss heats the fluid by ΔT = ΔP_f/(ρc_p), about 0.0004 K here. The mechanical energy is destroyed as far as pumping is concerned, which is an entropy-generating process in the language of the [entropy lesson](14-entropy-balances-and-irreversibility.md), but the temperature effect is negligible.

## Choosing the terms

- For heating and cooling a liquid stream, the thermal term ṁc_pΔT usually dominates the first law.
- For pumping in small tubing, friction and height dominate, and the kinetic-energy term is often negligible.
- Bernoulli alone applies only where friction is negligible, such as over short distances, at sudden contractions or in large reservoirs. It fails along long narrow tubes.
- Check the Reynolds number before using the laminar friction formula.

## Common mistakes

- Using Bernoulli across a long tube and ignoring a friction loss larger than every other term.
- Sign errors in shaft work: work done on the fluid by a pump is negative Ẇ_s in the first law above.
- Using volumetric flow where mass flow is required, or millilitres per minute without converting to cubic metres per second.
- Forgetting that hydrostatic pressure depends on height difference, not on tube length.
- Treating the efflux speed √(2gh) as achievable rather than as a frictionless upper bound.
- Applying the Poiseuille loss to turbulent or developing flow.

## Worked example

**Problem.** A synthetic perfusion circuit carries medium (ρ = 1000 kg/m³, c_p = 4180 J/(kg·K), μ = 1.0 mPa·s) at 20 mL/min through 1.5 m of 2.0 mm bore tubing, lifting it 0.50 m. Find the heating power to warm it from 20 °C to 37 °C, the friction loss, and the pump input power at 25% efficiency.

**Step 1: heating.** ṁ = 3.33 × 10⁻⁴ kg/s, so ṁc_pΔT = 3.33 × 10⁻⁴ × 4180 × 17 = 23.7 W.

**Step 2: flow regime.** v = 0.106 m/s and Re ≈ 212, so the flow is laminar.

**Step 3: friction loss.** 128 × 1.0 × 10⁻³ × 1.5 × 3.33 × 10⁻⁷/(π × (2.0 × 10⁻³)⁴) = 1.27 kPa.

**Step 4: pump.** Adding the lift of 4.91 kPa gives 6.18 kPa, and the hydraulic power is 6.18 × 10³ × 3.33 × 10⁻⁷ = 2.06 mW. At 25% efficiency, the input is 8.24 mW.

**Step 5: compare.** The heater needs about three thousand times more power than the pump. Thermal and mechanical energy demands in such circuits differ by orders of magnitude, which is why they are designed separately.

## Limits of this lesson

All circuits, fluids and parameter values are synthetic. The analysis assumes steady, incompressible, single-phase flow with constant properties, mean velocities, fully developed laminar friction where stated and no minor losses at fittings or valves. Turbulent friction factors, entrance-length effects, compressible gases, pulsatile flow, non-Newtonian media and heat-exchanger design are not developed. Nothing here is an equipment specification or operating procedure for any real perfusion system. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
