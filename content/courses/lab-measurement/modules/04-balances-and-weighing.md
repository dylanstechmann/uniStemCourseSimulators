# Balances and weighing

A balance display shows more digits than it can be trusted to. This lesson explains readability, repeatability and minimum weight, the routine checks that tell you a balance is working, the habits that keep a weighing honest, and why air buoyancy matters at the level of precision analytical work needs.

## Learning objectives

By the end of this lesson, you should be able to:

1. Distinguish readability from repeatability, and compute a minimum weight from a balance's repeatability and a required tolerance.
2. Describe the set-up and routine checks of an analytical balance, and judge a check-weight reading against an acceptance limit.
3. Weigh by difference, and explain when it is better than taring a weighing boat.
4. Identify the effects of temperature, draughts, static and air buoyancy on a weighing, and correct a mass for buoyancy.

## Readability, repeatability and minimum weight

**Readability** (d) is the smallest step the display shows: 0.1 mg on a typical analytical balance, 0.01 g on a top-loading balance. **Repeatability** (s) is the standard deviation of repeated weighings of the same object, measured on that balance where it stands. It is usually larger than the readability and depends on the room as much as the instrument.

The relative uncertainty of a weighing falls as the mass rises, because s stays roughly constant. The **minimum weight** is the smallest mass for which that uncertainty meets the required tolerance. Using a coverage factor of 2:

  m_min = 2s / tolerance.

With s = 0.08 mg and a required tolerance of 0.10%, m_min = 2 × 0.08/0.0010 = 160 mg. For a looser tolerance of 1%, m_min = 16 mg. Weighing 0.2 mg on that balance, as the [solution-preparation lesson](01-concentration-and-solution-preparation.md) warns against, would carry a relative uncertainty of about 2 × 0.08/0.2 = 80%. Below the minimum weight, make a more concentrated stock or use a more sensitive balance.

## Setting up and checking a balance

- **Level.** Centre the bubble with the adjustable feet. An unlevel balance reads differently depending on where the load sits.
- **Warm up.** Leave the balance powered; electronic balances drift for some time after being switched on.
- **Close the draught shield** and keep the balance away from doors, vents and foot traffic.
- **Adjust or calibrate** with the internal or an external reference weight as the laboratory's procedure requires.
- **Check with a check weight** before use. A laboratory sets the acceptance limit. If a 100 g check weight must read within ±0.5 mg and reads 100.0003 g, the deviation of 0.3 mg is acceptable; a reading of 99.9992 g (−0.8 mg) is not, and the balance needs adjustment before use.
- **Record** the check in the balance log, with the weight's identity and its calibration status.

## Weighing habits

- **Tare** the empty container, add the sample, and read once the stability indicator settles.
- **Weigh by difference** for hygroscopic, volatile or static-prone solids, or whenever material may stick to a boat. Weigh the capped vial with the solid, transfer some solid to the receiving vessel, and weigh the vial again: 12.3456 g − 12.1123 g = 0.2333 g transferred. The mass is what left the vial, so anything left in a boat does not matter.
- **Equilibrate temperature.** A warm object sets up a convection current that pushes up on the pan, so it reads light; a cold one reads heavy and gathers condensation. Let objects from an oven or refrigerator come to room temperature in a desiccator or closed container.
- **Control static.** Dry plastic and powders can carry charge that pulls on the pan, giving drifting readings. Antistatic devices, metal or glass containers and grounding help.
- **Handle with care.** Use tongs or gloves for check weights and small vessels, since fingerprints add mass, and clean spills at once.

## Air buoyancy

A balance compares the downward force of the sample with that of its reference weights, both reduced by the buoyancy of the air they displace. If the sample is much less dense than the reference weights (8.0 g/cm³), it displaces more air and reads slightly light. The true mass is

  m_true ≈ m_reading × (1 − ρ_air/ρ_weights)/(1 − ρ_air/ρ_sample),

with ρ_air ≈ 0.0012 g/cm³. For water (ρ ≈ 1.00 g/cm³) the correction is about +0.105%: a reading of 1.0000 g corresponds to a true mass of about 1.0011 g. The correction is negligible for most solution preparation but not for calibrating volumes, which is why the factor Z in the [pipette lesson](03-measuring-volume-and-checking-pipettes.md) includes it.

## Common mistakes

- Treating the readability as the uncertainty.
- Weighing below the minimum weight and trusting the display.
- Weighing a warm beaker straight from the oven.
- Skipping the daily check because the balance "looked fine yesterday".
- Weighing a hygroscopic solid slowly on an open boat, so it gains water while you watch.

## Worked example

**Problem.** A balance's repeatability, measured with ten weighings, is s = 0.12 mg. You must weigh about 25 mg of a reference standard with a tolerance of 0.5%. Is the balance suitable, and what would you do if not?

**Step 1: minimum weight.** m_min = 2 × 0.12/0.005 = 48 mg.

**Step 2: compare.** 25 mg is below 48 mg, so the uncertainty of a single weighing would be about 2 × 0.12/25 = 0.96%, nearly twice the tolerance.

**Step 3: options.** Weigh at least 48 mg (for example 50 mg) and dissolve it in twice the volume, so the concentration is unchanged, or use a balance with better repeatability.

## Limits of this lesson

The minimum-weight formula is a simplified form of the approach used in pharmaceutical and metrology practice, with a coverage factor of 2 and repeatability as the only uncertainty; formal standards also consider other contributions. Acceptance limits here are examples, not requirements for any balance. Balance calibration by an accredited provider and the traceability of reference weights are described, not taught.
