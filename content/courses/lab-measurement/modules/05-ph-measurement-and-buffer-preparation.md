# pH measurement and buffer preparation

Cells, enzymes and many assays are sensitive to pH, so buffers are made and checked constantly. A pH meter is a voltmeter attached to an electrode whose response must be calibrated every day it is used. This lesson covers calibration and its acceptance checks, electrode care, and making a buffer that has the right pH at the temperature where it will be used.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calibrate a pH meter with two or three buffers, compute the electrode slope as a percentage of the theoretical value, and decide whether the calibration is acceptable.
2. Convert an electrode reading in millivolts to pH from a calibration.
3. Plan a buffer from the Henderson–Hasselbalch equation, then explain why the pH must still be measured and adjusted.
4. Account for temperature: the electrode's slope, automatic temperature compensation, and the temperature dependence of the buffer itself.

## How the electrode responds

A glass pH electrode develops a potential that changes linearly with pH. The theoretical change, the Nernst slope, is (RT ln 10)/F: 59.16 mV per pH unit at 25 °C, 58.17 at 20 °C and 61.54 at 37 °C. At pH 7 a typical combination electrode reads close to 0 mV, and the reading rises as pH falls. Real electrodes have a slope a little below theoretical and an offset from 0 mV, both of which drift as the electrode ages. Calibration measures them.

## Calibration

Calibrate with fresh standard buffers that bracket the expected sample pH, usually pH 7.00 first and then 4.01, 10.01 or both. Rinse the electrode with water between buffers and blot it dry; do not wipe the glass bulb, which can build up static and damage the hydrated layer.

**Example.** At 25 °C the pH 7.00 buffer reads +3.5 mV and the pH 4.01 buffer reads +172.0 mV. The slope is (172.0 − 3.5)/(7.00 − 4.01) = 56.35 mV per pH unit, which is 56.35/59.16 = 95.3% of theoretical. The offset at pH 7 is +3.5 mV. Laboratories commonly accept slopes of about 95–105% and offsets within about ±30 mV; your laboratory's SOP sets the actual limits. Here the slope is at the low edge: the calibration may be used, but the electrode should be cleaned or replaced soon.

A sample reading +60.0 mV then has pH = 7.00 − (60.0 − 3.5)/56.35 = 6.00. Readings outside the calibrated range are extrapolations; recalibrate with a bracketing buffer before trusting them.

## Electrode care

- Store the electrode in its storage solution (usually concentrated KCl), never dry and never in pure water, which leaches ions from the glass and the reference junction.
- Keep the fill hole open during measurements on refillable electrodes so the electrolyte flows through the junction.
- Stir samples and buffers the same way, and wait for a stable reading.
- Protein and Tris solutions can clog the reference junction; clean as the manufacturer directs if response becomes slow.

## Planning a buffer

The Henderson–Hasselbalch equation gives the ratio of base to acid forms needed for a target pH:

  pH = pKa + log₁₀([base]/[acid]).

**Example.** For 1.00 L of 0.100 M sodium phosphate at pH 7.40, using pKa₂ = 7.20: [base]/[acid] = 10^0.20 = 1.585, so the acid fraction is 1/2.585 = 0.387. That is 0.0387 mol of NaH₂PO₄ (5.34 g of the monohydrate, M = 137.99 g/mol) and 0.0613 mol of Na₂HPO₄ (8.70 g anhydrous, M = 141.96 g/mol).

The calculation gets you close; it does not finish the job. The tabulated pKa applies at a particular temperature and at low ionic strength, and a 0.1 M phosphate buffer is not dilute. So dissolve the components in about 80% of the final volume, measure the pH with a calibrated meter, adjust with small amounts of acid or base, and only then bring to volume, as the [solution-preparation lesson](01-concentration-and-solution-preparation.md) describes. Single-component buffers such as Tris are made the same way: dissolve Tris base and titrate down with HCl to the target pH.

## Temperature

Temperature enters in two separate ways, and they are easy to confuse.

- **The electrode.** The slope changes with temperature, following the Nernst equation. Automatic temperature compensation (ATC) corrects for this using a temperature probe. It does not change the sample's actual pH.
- **The buffer.** The pKa of the buffer itself changes with temperature. Tris is the classic example: its pKa falls by about 0.028 per °C. A Tris buffer adjusted to pH 8.00 at 25 °C and used at 4 °C is near pH 8.00 − 0.028 × (4 − 25) = 8.59. Phosphate changes much less.

So adjust a buffer's pH at the temperature where it will be used, or correct for the known shift, and record the temperature with the pH.

## Common mistakes

- Calibrating once a week, or with old or contaminated buffers.
- Measuring outside the range bracketed by the calibration buffers.
- Assuming ATC corrects the buffer's pH for temperature.
- Bringing the buffer to volume before adjusting its pH.
- Storing the electrode in pure water.

## Worked example

**Problem.** A meter is calibrated at 25 °C with pH 7.00 (−2.0 mV) and pH 10.01 (−170.6 mV) buffers. Is the calibration acceptable against a 95–105% slope limit, and what is the pH of a sample at −120.0 mV?

**Step 1: slope.** (−170.6 − (−2.0))/(10.01 − 7.00) = −168.6/3.01 = −56.01 mV per pH unit; the magnitude is 56.01/59.16 = 94.7% of theoretical.

**Step 2: verdict.** 94.7% is below 95%, so the calibration fails. Clean the electrode, use fresh buffers and recalibrate; replace the electrode if the slope stays low.

**Step 3: what the reading would have meant.** Using the failed calibration anyway, pH = 7.00 + (−120.0 − (−2.0))/(−56.01) = 9.11. The number can be computed, but it should not be reported.

## Limits of this lesson

Buffer pKa values and the Tris temperature coefficient are rounded literature-style values used for illustration; check the value for your buffer and conditions. Activity effects are described qualitatively. Acceptance limits for slope and offset are examples; your SOP sets the real ones. Reference electrodes, ion-selective electrodes and pH measurement in non-aqueous or very viscous samples are not covered.
