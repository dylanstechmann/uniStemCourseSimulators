# Mixing, shear, and scale-up

When a stirred culture moves to a larger vessel, the volume, flow paths, and distance between the impeller and vessel wall all change. Geometric similarity keeps selected shape ratios fixed, but it does not keep fluid motion or the cell environment identical. Scale-up therefore begins by identifying the process outcome that must be protected, then choosing measurements and a comparison criterion that speak to it.

## One criterion cannot preserve every condition

Common quantities describe different parts of the problem:

- **Impeller tip speed**, $u_{tip}=\pi ND$, is the speed at the impeller edge, where $N$ is rotations per time and $D$ is impeller diameter. It can be relevant to local velocity and stress near the impeller, but says little by itself about how quickly the whole vessel mixes.
- **Power per volume**, $P/V$, is a bulk energy-input measure. It is often used to compare mixing intensity, but the same average input does not imply the same local dissipation, gas dispersion, or oxygen transfer.
- **Reynolds number**, $Re=\rho ND^2/\mu_f$, compares inertial and viscous effects for density $\rho$ and dynamic viscosity $\mu_f$. It helps identify a flow regime; equal Reynolds number alone does not imply equal gas transfer or cell exposure.
- **Mixing time** describes how long a tracer or concentration difference takes to fall within a stated tolerance. Its value depends on where the tracer is introduced and observed, the tolerance, and the measurement method.

For geometrically similar vessels with a fixed impeller-to-vessel ratio, volume scales with the cube of a characteristic length. If the volume grows by a factor of 100, the length and impeller diameter grow by $100^{1/3}\approx4.64$. Even with that simple geometry, choosing constant tip speed requires the larger vessel to turn more slowly than choosing constant power per volume. Under the idealized turbulent relation $P=N_p\rho N^3D^5$ with the same power number $N_p$, constant $P/V$ instead gives $N\propto D^{-2/3}$. The two criteria therefore lead to different rotational speeds and different values of the other transport quantities.

**Worked comparison.** Suppose a geometrically similar vessel is scaled from 2 L to 200 L, and fluid density and power number are treated as constant. The linear scale factor is $\lambda=100^{1/3}\approx4.64$. At constant tip speed, the rotational-speed ratio is $N_2/N_1=1/\lambda\approx0.215$. At constant $P/V$, the idealized ratio is $N_2/N_1=\lambda^{-2/3}\approx0.359$, so tip speed rises by $\lambda^{1/3}\approx1.67$. Neither comparison preserves all of tip speed, power per volume, Reynolds number, mixing time, gas transfer, and local stress. The assumptions are for comparing scaling rules, not selecting operating conditions.

## Connect vessel mixing to what cells experience

An average may hide a harmful local history. Cells and aggregates can pass repeatedly through regions with different dissolved oxygen, substrate, pH, or shear. A bulk dissolved-oxygen probe can show an acceptable average while a poorly mixed region experiences a different concentration. The cell response also has a time scale: a brief excursion may have a different effect from a prolonged one, so the frequency and duration of gradients can matter along with their size.

A useful scale-up argument links the chosen criterion to an observable outcome. If oxygen limitation is suspected, combine oxygen-transfer and uptake estimates with measurements that can reveal spatial or transient changes. If mixing gradients are suspected, state the tracer, sampling locations, and mixing-time definition. If cell damage is suspected, pair an appropriate viability or function outcome with the relevant local-flow hypothesis. These comparisons can narrow a mechanism; one matching metric cannot prove that physiology will remain equivalent.

## Scale-down as a focused test

A smaller model can reproduce selected features of a large-vessel environment, such as repeated periods of oxygen limitation separated by better-mixed zones. The model should identify which feature it represents and which it omits. Matching the exposure time to the cell-response time, or matching a distribution of oxygen histories, may be more informative than matching geometric ratios alone. The match must be demonstrated with measurements or a validated representation; a small vessel is not automatically a valid scale-down model.

Compare conditions using replicated, predefined outcomes and record the uncertainty and operating context. A difference between scales supports a scale-sensitive effect under those tested conditions, but does not on its own identify the mechanism or predict every production vessel. Cell line, medium, gas composition, vessel geometry, probe location, and measurement delay can all affect the comparison. Real scale decisions require qualified process engineering and empirical validation; this reading supplies no vessel-specific recommendation.

## Common mistakes

- Treating geometric similarity as proof of dynamic or biological similarity.
- Assuming constant tip speed also preserves power per volume, Reynolds number, mixing time, or oxygen transfer.
- Reporting a mixing time without defining the tracer, locations, and tolerance.
- Inferring local cell exposure from a single bulk measurement or inferring a mechanism from one scale comparison.
