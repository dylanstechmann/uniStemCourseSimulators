# Measuring volume and checking pipettes

Every concentration in the laboratory depends on a volume. This lesson sorts volumetric devices by what they are designed to do, separates accuracy from precision, sets out micropipette technique and the errors each lapse causes, and shows how to check a pipette by weighing water.

## Learning objectives

By the end of this lesson, you should be able to:

1. Choose a volumetric device for a task, distinguishing devices calibrated to contain from those calibrated to deliver.
2. Distinguish systematic from random error and compute both, as percentages, from replicate measurements.
3. Explain how pre-wetting, immersion depth, angle, speed and touch-off affect the volume an air-displacement pipette delivers, and when reverse pipetting is preferable.
4. Convert gravimetric readings of water to volume with a temperature-dependent factor Z, and decide whether a pipette meets acceptance limits.

## Devices and what they are calibrated for

| Device | Calibrated | Typical use |
| --- | --- | --- |
| Volumetric flask | to contain (TC) one volume | making a solution up to an exact volume |
| Volumetric (transfer) pipette | to deliver (TD) one volume | transferring an exact volume of a standard |
| Burette | to deliver variable volumes | titration |
| Graduated cylinder | to contain, graduated | approximate volumes of reagents and media |
| Serological pipette | to deliver, graduated | millilitre transfers in culture work |
| Air-displacement micropipette | to deliver, adjustable | microlitre transfers of aqueous liquids |
| Positive-displacement pipette | to deliver, adjustable | viscous, volatile or dense liquids |

A flask marked TC holds the stated volume when filled to the mark; pouring it out delivers slightly less, because a film stays on the glass. A pipette marked TD delivers the stated volume when drained as specified, and the liquid that remains in the tip is accounted for in its calibration. Beakers and flask graduations are not measuring devices. Class A glassware is made and marked to tighter tolerances than Class B; use it, with its marked tolerance, when a volume enters a calculation.

## Accuracy and precision

Repeated deliveries scatter around a mean. **Systematic error** (inaccuracy) is how far the mean lies from the intended value; **random error** (imprecision) is the scatter around the mean. Both are commonly reported as percentages of the nominal volume V₀:

  systematic error = (V̄ − V₀)/V₀ × 100,  random error (CV) = s/V̄ × 100,

where V̄ is the mean delivered volume and s the sample standard deviation. A pipette can be precise and inaccurate (tightly grouped around the wrong value, often a calibration offset) or accurate on average and imprecise (often a worn seal or poor technique). Averaging more replicates shrinks the effect of random error on the mean; it does nothing to systematic error.

Relative error grows at the low end of a pipette's range. An absolute error of 1 µL is 1% of 100 µL but 10% of 10 µL, so choose the smallest pipette whose range includes the volume.

## Technique with an air-displacement pipette

An air-displacement pipette moves a piston that draws an air cushion, and the air cushion draws the liquid. Anything that changes the cushion or leaves liquid behind changes the volume.

- **Pre-wet the tip.** Fill and empty a new tip two or three times. The first fill of a dry tip and its air cushion takes up vapour and delivers low.
- **Immerse a few millimetres, vertically.** Too shallow draws air; too deep leaves a film on the outside of the tip that is then delivered. Tilting the pipette changes the hydrostatic pressure on the cushion.
- **Move the plunger smoothly and consistently.** Releasing it abruptly can splash liquid into the shaft and draws an inconsistent volume.
- **Dispense against the wall and touch off.** Press to the first stop, wait, press to the second stop to blow out, and draw the tip along the wall to collect the last drop.
- **Equilibrate.** Liquid, pipette and tips at room temperature give the volume the pipette was set for; a pipette warmed by the hand drifts.

**Reverse pipetting** draws to the second stop and dispenses only to the first, leaving the excess in the tip. It is preferable for viscous, foaming or volatile liquids and for very small volumes of protein solutions, where forward pipetting delivers inconsistently.

## Checking a pipette by weighing water

Water has a well-known density, so a balance can measure delivered volume. Deliver water into a tared vessel, record each mass m, and convert with

  V = m × Z,  Z = (1/(ρ_water − ρ_air)) × (1 − ρ_air/ρ_weights),

where ρ_water depends on temperature, ρ_air ≈ 0.0012 g/mL, and ρ_weights = 8.0 g/mL is the conventional density of the balance's reference weights. Z corrects both for water being slightly less dense than 1 g/mL and for air buoyancy. With masses in milligrams, Z is in µL/mg: 1.0029 at 20 °C, 1.0032 at 21.5 °C and 1.0040 at 25 °C. Water density in this course follows the formula of Tanaka and colleagues (2001), which gives 998.207 kg/m³ at 20 °C.

**Example.** Ten deliveries from a pipette set to 200 µL weigh, in mg: 198.6, 199.1, 198.9, 199.4, 198.7, 199.0, 198.8, 199.2, 198.5 and 199.0, at 21.5 °C. The mean mass is 198.92 mg, so V̄ = 198.92 × 1.0032 = 199.55 µL. The systematic error is (199.55 − 200)/200 × 100 = −0.224% and the random error is s/V̄ = 0.279/199.55 × 100 = 0.140%. Treating milligrams as microlitres would have reported −0.540%, more than double the real offset.

Whether the pipette passes depends on acceptance limits, which a laboratory takes from its SOP, the manufacturer or ISO 8655 for the pipette's size and volume. The [bench practice](#/bench/micropipette-gravimetric-verification) simulation uses practice limits of ±0.8% systematic and 0.3% random at 1000 µL. A pipette that fails either limit is taken out of use, then adjusted or serviced and checked again.

## Common mistakes

- Pouring a solution out of a TC flask and treating the poured volume as exact.
- Averaging more replicates to fix an inaccurate pipette.
- Working at the bottom of a pipette's range when a smaller pipette is available.
- Skipping pre-wetting, or immersing too deep, then blaming the pipette.
- Converting milligrams to microlitres without the factor Z.

## Worked example

**Problem.** A check of a 1000 µL pipette at 25 °C gives a mean mass of 992.8 mg and a sample standard deviation of 2.10 mg over ten readings. Practice limits are ±0.8% systematic and 0.3% random. Does it pass?

**Step 1: volume.** V̄ = 992.8 × 1.0040 = 996.8 µL, and s_V = 2.10 × 1.0040 = 2.11 µL.

**Step 2: systematic error.** (996.8 − 1000)/1000 × 100 = −0.32%, within ±0.8%.

**Step 3: random error.** 2.11/996.8 × 100 = 0.21%, within 0.3%.

**Step 4: verdict.** The pipette passes at this volume. A full check repeats the test at other volumes in its range.

## Limits of this lesson

Evaporation during weighing, balance drift, and the exact requirements of ISO 8655 (which was not read for this course) are not covered. Acceptance limits shown are practice values for this course's simulation, not limits for any specific instrument. Technique effects are described qualitatively; their size depends on the pipette, tip and liquid.
