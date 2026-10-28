# The closed-system first law: work, heat and ideal-gas processes

The [control-volume lesson](01-control-volumes-and-conservation.md) wrote the first law as a rate balance for a volume with flows crossing its boundary, and the [entropy lesson](14-entropy-balances-and-irreversibility.md) balanced entropy for a closed system. Between them sits the plainest energy statement: a fixed amount of matter, no flow, and energy exchanged only as heat and work. It rests on ideas the course had not yet defined: the internal energy of a gas, which quantities depend only on the state and which on the path, the molar heat capacities of a gas, and the ideal gas. This lesson supplies them, and it shows why the same change of state can cost different amounts of work along different paths. All gases, volumes and temperatures are synthetic.

The [MIT OCW 20.110J Thermodynamics of Biomolecular Systems (Fall 2005) calendar](https://ocw.mit.edu/courses/20-110j-thermodynamics-of-biomolecular-systems-fall-2005/pages/calendar/) opens with temperature, work and heat (lecture 1), state functions and the first law (lecture 2), heat capacity (lecture 3), and reversible and irreversible processes (lecture 4). [Open Yale Courses PHYS 200](https://oyc.yale.edu/physics/phys-200/lecture-21) covers temperature and specific heat in Lecture 21, [Lecture 22](https://oyc.yale.edu/physics/phys-200/lecture-22) has chapters on quasi-static processes and on internal energy and the first law, and [Lecture 23](https://oyc.yale.edu/physics/phys-200/lecture-23) has chapters on specific heats at constant pressure and volume and on adiabatic processes. Both are link-only scope comparators; no text, figure or problem is reproduced.

## Learning objectives

By the end of this lesson, you should be able to:

1. Apply ΔU = Q − W to a closed system with the course's sign convention, and distinguish state functions from path functions.
2. Compute the work, heat and temperature change of isothermal, isobaric, isochoric and reversible adiabatic processes of an ideal gas from C_v, C_p and γ.
3. Compare reversible and irreversible expansions between the same states, and connect the difference to entropy generation.

## State and path

Thermodynamic temperature is measured in kelvin, T = θ + 273.15 for a Celsius reading θ, and two bodies at the same temperature exchange no net heat. A **state function** depends only on the present state of the system and not on how it arrived. Pressure, volume, temperature, internal energy U and enthalpy H = U + PV are state functions, so their changes depend only on the initial and final states. **Heat** Q and **work** W are not: they describe energy crossing the boundary during a process, and different paths between the same two states can transfer different amounts.

The course's sign convention is the one of the control-volume lesson: heat added to the system is positive, and work done by the system is positive. For a closed system,

\[
\Delta U = Q - W .
\]

This is the control-volume balance with no flow, no kinetic or potential energy change, and storage equal to the change of internal energy.

For a gas that expands slowly enough to stay at a uniform pressure P, the work it does is

\[
W = \int_{V_1}^{V_2} P\,dV ,
\]

the area under the pressure–volume path, which depends on the path taken.

## The ideal gas and its heat capacities

An ideal gas obeys PV = nRT, with R = 8.314 J/(mol·K) and T in kelvin, and its internal energy depends only on its temperature. Heating at constant volume does no expansion work, so Q = ΔU = nC_vΔT, where C_v is the molar heat capacity at constant volume. Because U depends only on T, this expression gives ΔU for every process of the gas, not only constant-volume ones. Heating at constant pressure also does work, W = PΔV = nRΔT, so the heat needed is larger: Q = ΔH = nC_pΔT. The enthalpy H = U + PV = U + nRT also depends only on T, so ΔH = nC_pΔT holds for every process of the gas, as ΔU = nC_vΔT does. The two molar heat capacities and their ratio γ are related by

\[
C_p = C_v + R,\qquad \gamma = C_p/C_v .
\]

In the models used here a monatomic gas has C_v = (3/2)R = 12.47 J/(mol·K), C_p = (5/2)R = 20.79 J/(mol·K) and γ = 5/3, and a diatomic gas near room temperature has C_v = (5/2)R and C_p = (7/2)R, so γ = 7/5.

## Four processes of one gas

Take n = 0.0500 mol of a monatomic ideal gas at 300 K and V₁ = 1.0 L, so P₁ = nRT/V₁ = 124.7 kPa. Expand it reversibly to V₂ = 3.0 L in two ways.

**Isothermal.** Heat flows in to hold T = 300 K. Then ΔU = 0 and Q = W = ∫ nRT/V dV = nRT ln(V₂/V₁) = 0.0500·8.314·300·ln 3 = **137.0 J**. The final pressure is 41.57 kPa.

**Adiabatic.** No heat flows, so Q = 0 and W = −ΔU. For a reversible adiabatic ideal gas PV^γ and TV^(γ−1) stay constant, so T₂ = 300·(1/3)^(2/3) = 144.2 K and the gas does W = nC_v(T₁ − T₂) = 0.0500·12.47·155.8 = **97.1 J** at the cost of its own internal energy. Its final pressure is only 19.98 kPa.

Both start in the same state and reach the same volume, yet they do different work and end at different temperatures and pressures: heat and work are path functions. In the adiabatic case integrating P dV along PV^γ = constant reproduces the 97.1 J.

**Isobaric and isochoric.** Heating the same gas at constant pressure from 300 to 350 K takes Q = nC_pΔT = 0.0500·20.79·50 = 51.96 J. Of that, ΔU = nC_vΔT = 31.18 J raises the internal energy and W = nRΔT = 20.79 J is the expansion work, so Q = ΔU + W = 51.96 J, and Q equals ΔH. Heating at constant volume by the same 50 K takes only 31.18 J, all of it ΔU.

Intermediate values are rounded for display. Each result comes from unrounded values, so a hand calculation with the factors shown can differ in the last digit.

## Reversible and irreversible expansion

The same change of state, 300 K and 1.0 L to 300 K and 3.0 L, can be made irreversibly. Let the gas expand against a constant external pressure equal to its final pressure, P_ext = 41.57 kPa, with heat exchanged so that it ends at 300 K. The work is W = P_ext ΔV = 41.57·2.0 = **83.1 J**, only 61% of the reversible 137.0 J. A reversible isothermal path delivers the maximum work between these states.

Free expansion is the extreme: a gas released into an evacuated, insulated container does no work and receives no heat, so ΔU = 0 and an ideal gas ends at its original temperature.

The entropy lesson shows why the irreversible path is worse. Entropy is a state function, so the gas's entropy rises by ΔS = nR ln 3 = 0.4567 J/K on either path. On the reversible path the heat absorbed, 137.0 J at 300 K, transfers Q/T = 0.4567 J/K and no entropy is generated. On the irreversible path only 83.1 J enters, which transfers 0.2771 J/K, and the balance ΔS = Q/T_b + S_gen gives S_gen = 0.1796 J/K, positive as the second law requires. The work lost is the entropy generated times the boundary temperature: 0.1796 × 300 = 53.9 J, which equals 137.0 − 83.1.

## Common mistakes

- Treating heat or work as a state function, or assuming a process between two states has a unique work.
- Using Celsius temperatures in PV = nRT or in a ratio such as T₂/T₁.
- Using C_v for a constant-pressure heating, or forgetting that ΔU = nC_vΔT holds for any process of an ideal gas.
- Mixing sign conventions: here work done by the gas is positive, so compression gives a negative W.
- Applying PV^γ = constant to an irreversible or non-adiabatic process.
- Expecting an ideal gas's temperature to fall in a free expansion.

## Worked example

**Problem.** A synthetic sealed syringe holds 0.0200 mol of a diatomic ideal gas at 300 K and 100 kPa. It is compressed to half its volume, once adiabatically and reversibly and once isothermally and reversibly. Find the work done on the gas and the final temperature and pressure in each case.

**Step 1: initial volume.** V₁ = nRT/P = 0.0200·8.314·300/100,000 = 0.4988 L, so the final volume is 0.2494 L.

**Step 2: adiabatic.** With γ = 7/5, T₂ = 300·2^0.4 = 395.9 K and P₂ = P₁·2^1.4 = 263.9 kPa. The work done on the gas equals its gain in internal energy, nC_v(T₂ − T₁) = 0.0200·20.79·95.85 = 39.85 J, and Q = 0.

**Step 3: isothermal.** T stays 300 K, P₂ = 200 kPa, and the work done on the gas is nRT ln 2 = 34.58 J. Since ΔU = 0, 34.58 J of heat leaves the gas.

**Step 4: check.** Integrating P dV along the adiabat gives 39.85 J again. The adiabatic compression takes more work than the isothermal one, 39.85 against 34.58 J, because the gas heats and its pressure rises faster. A rapid compression is closer to the adiabatic case, which is why it warms the gas.

## Limits of this lesson

All gases, amounts and temperatures are synthetic models of ideal gases with temperature-independent heat capacities, processes are idealized as quasi-static unless marked irreversible, and no real-gas correction or phase change is included. Cycles and heat engines are not developed. Nothing here is the design of a device or a safety statement. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
