# Voltage-gated conductances and the action potential: the Hodgkin–Huxley model

The excitable-cells lesson treated each conductance as fixed and noted that voltage- and time-dependent gates make the conductances change during an action potential. This lesson makes that statement quantitative. It follows the model that [Hodgkin and Huxley (1952)](https://doi.org/10.1113/jphysiol.1952.sp004764) fitted to voltage-clamp recordings from the squid giant axon. It shows how a voltage clamp separates the currents, how gating variables describe the sodium and potassium conductances, and how the different speeds of those gates produce the upstroke, repolarization, undershoot, threshold and refractory period of a spike. The numbers use the classic squid-axon parameter set at 6.3 °C as it is usually written today, with a resting potential of −65 mV. Mammalian neurons and heart cells have other channels and other values, so the mechanism transfers but the numbers do not.

The undergraduate [MIT OCW 6.021J Quantitative Physiology: Cells and Tissues (Fall 2004) calendar](https://ocw.mit.edu/courses/6-021j-quantitative-physiology-cells-and-tissues-fall-2004/pages/calendar/) gives the Hodgkin–Huxley model six lectures (20–25: space clamp, voltage clamp, current clamp, a modelling project and threshold) and channel gating four more (32–35). This reading is a compact version placed with the local excitable-cells lesson. It uses 6.021J as a scope comparator only and reproduces no MIT material.

## Learning objectives

By the end of this lesson, you should be able to:

1. Write the membrane equation for a uniformly polarized patch of membrane, and explain how a voltage clamp separates and measures the ionic currents.
2. Compute a gating variable's steady state and time constant from its opening and closing rates, its relaxation after a voltage step, and the resulting conductance and current.
3. Explain the upstroke, repolarization, undershoot, threshold and refractory period of an action potential from the different speeds of the m, h and n gates.

## The membrane equation

Consider a patch of membrane at one uniform voltage V, as in an axon with a wire threaded along its core (a space clamp). Charge conservation gives

**C_m dV/dt = −(I_Na + I_K + I_L) + I_stim,**

where I_Na = g_Na (V − E_Na), I_K = g_K (V − E_K) and I_L = g_L (V − E_L), with outward current positive as in the excitable-cells lesson. Currents are per unit area, in μA/cm², and C_m ≈ 1 μF/cm². In the classic set, E_Na = +50 mV, E_K = −77 mV and the leak reversal potential E_L = −54.4 mV.

The equation says that net inward current depolarizes the membrane at a rate set by the capacitance. With C_m = 1 μF/cm², a net inward current of 100 μA/cm² raises V by 100 mV per millisecond, because 1 μA/μF = 1 V/s = 1 mV/ms.

## The voltage clamp separates the currents

A voltage clamp uses feedback to hold V at a chosen command value. After the brief capacitive surge at the step, dV/dt = 0, so the current the amplifier injects equals the ionic current at that voltage. A step from rest to a depolarized level gives an early inward current followed by a later, sustained outward current. Hodgkin and Huxley separated the two by replacing most of the external sodium; later experiments used blockers such as tetrodotoxin for sodium channels and tetraethylammonium for potassium channels. Dividing each current by its driving force gives a conductance at each clamped voltage. The sodium conductance rises within a fraction of a millisecond and then falls even though the voltage stays depolarized. The potassium conductance rises after a delay, more slowly, and stays up.

## Gating variables

The model writes each conductance as a maximum times the fraction of channels that are conducting:

**g_K = ḡ_K n⁴ and g_Na = ḡ_Na m³h,**

with ḡ_K = 36 mS/cm², ḡ_Na = 120 mS/cm² and a constant g_L = 0.3 mS/cm². The activation variables n and m rise with depolarization; the inactivation variable h falls with it. Each behaves like a gate that opens at rate α and closes at rate β, both functions of voltage:

**dx/dt = α_x(V)(1 − x) − β_x(V) x.**

At a fixed voltage, x relaxes exponentially toward

**x∞ = α_x/(α_x + β_x), with time constant τ_x = 1/(α_x + β_x),**

so after a voltage step x(t) = x∞ − (x∞ − x₀) e^(−t/τ_x).

At rest (−65 mV) the classic rates give α_n = 0.0582 ms⁻¹ and β_n = 0.125 ms⁻¹, so n∞ = 0.318, τ_n = 5.46 ms and g_K = 36 × 0.318⁴ ≈ 0.37 mS/cm². At a clamp of 0 mV the time constants are about 0.24 ms for m, 1.03 ms for h and 1.65 ms for n. The m gates are four to seven times faster than the others, and that difference in speed shapes every phase of the spike.

The fourth power explains the delay in the potassium conductance. In the worked example below, n rises from 0.318 to 0.587 within 1 ms of a step to 0 mV, less than doubling, while n⁴, and so g_K, rises about 11.6-fold. The gate and conductance remain continuous, but their right-hand derivatives change when the voltage step changes the rates. In particular, d(g_K)/dt = 4 gbar_K n0³ [alpha_new(1−n0)−beta_new n0]; at n0=0.318 with the worked rates this initial slope is about 1.66155 mS/cm² per ms, not zero. Zero initial slope requires n0=0 or a zero initial gate derivative. The fourth power produces a nonlinear rise, not a universal zero-slope start. The exponents were chosen to fit the measured delays; independent gates are an idealization of how real channel proteins move.

## The action potential, step by step

1. A depolarizing stimulus raises V. Because τ_m is short, m rises within a fraction of a millisecond, the sodium conductance grows, and inward sodium current depolarizes the membrane further. This positive feedback is the upstroke, which carries V toward E_Na.
2. Over the next millisecond, h falls as sodium channels inactivate and n rises as potassium channels open. Outward potassium current overtakes the shrinking sodium current, and V falls back.
3. With n still high and h still low, V undershoots toward E_K, then recovers as n closes and h reopens.

In the model, a 1-ms pulse of 10 μA/cm² gives a spike that peaks near +39 mV about 2.5 ms after the pulse begins, stays above 0 mV for about 1.1 ms and undershoots to about −76 mV, close to E_K. At the peak, m ≈ 0.90, while h has already fallen to about 0.33 and n has risen to about 0.51.

## Threshold is a balance, not a fixed voltage

A spike begins when the inward sodium current recruited by a depolarization outruns the outward potassium and leak currents. That is a race between gates, so threshold depends on how the membrane is depolarized. In the model, a 1-ms pulse needs about 6.9 μA/cm² to trigger a spike, while a 0.1-ms pulse needs about 65 μA/cm². The shorter pulse needs far more current but about the same charge, 6.5 rather than 6.9 nC/cm², because what matters is charging the membrane quickly enough for sodium activation to win before inactivation and potassium activation catch up.

## Refractoriness

Right after a spike, h is low and n is high: few sodium channels are available, and extra potassium conductance opposes any depolarization. During the **absolute refractory period** no stimulus can trigger a second spike; during the **relative refractory period** a stronger stimulus than usual can. In the model, a second 1-ms pulse of 10 μA/cm² succeeds only about 15 ms after the first, while a pulse four times stronger succeeds from about 9.5 ms. Refractoriness limits the firing rate and, in an axon, keeps a spike from turning back over the membrane it has just crossed.

## Common mistakes

- Treating threshold as a fixed voltage instead of a balance that depends on how quickly the membrane is depolarized.
- Forgetting the fourth power of n and the third power of m when computing a conductance from gating variables.
- Reading τ_x as the time to reach x∞; it is the time to cover about 63% of the remaining distance.
- Attributing repolarization to sodium channels closing alone; inactivation (h) and potassium activation (n) both contribute.
- Mixing sign conventions, for example reading an inward current as positive under the outward-positive convention.
- Carrying squid-axon numbers over to mammalian neurons or heart cells.

## Worked example

**Problem.** At a clamp of 0 mV, the classic rates are α_n = 0.552 ms⁻¹ and β_n = 0.0555 ms⁻¹. Starting from the resting value n = 0.318, find n∞ and τ_n, then n, g_K and the potassium current 1 ms after the step.

**Step 1.** n∞ = 0.552/(0.552 + 0.0555) = **0.909**, and τ_n = 1/0.6075 = **1.65 ms**.

**Step 2.** n(1 ms) = 0.909 − (0.909 − 0.318) e^(−1/1.65) = 0.909 − 0.591 × 0.545 = **0.587**.

**Step 3.** g_K = 36 × 0.587⁴ = 36 × 0.1187 ≈ **4.27 mS/cm²**, about 11.6 times the resting 0.37 mS/cm².

**Step 4.** I_K = g_K (V − E_K) = 4.27 × (0 − (−77)) ≈ **329 μA/cm²**, outward.

## Limits of this lesson

The model describes a uniformly polarized patch of squid axon at 6.3 °C with deterministic, independent gates. Real membranes have many channel types, channel noise, temperature-dependent rates and spatial structure, and propagation along an axon needs the cable properties of the passive-membrane lesson. The parameter values are the classic set as conventionally written with a −65 mV rest, not measurements made for this course, and the voltage dependence of the rates is used but not derived. The thresholds, spike shape and refractory intervals quoted are outputs of the model under the stated pulses, computed for this lesson; they are not experimental values for any human tissue, and nothing here describes stimulation of a person.
