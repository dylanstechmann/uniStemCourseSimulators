# Spectrophotometry and standard curves

Many bench measurements end with a number read from a spectrophotometer or plate reader: a protein assay, an enzyme rate, a cell-density reading, a colorimetric test. This lesson covers the Beer–Lambert law and its limits, blanks, the linear range, and how to build and use a standard curve without fooling yourself.

## Learning objectives

By the end of this lesson, you should be able to:

1. Relate absorbance, transmittance, path length and concentration through the Beer–Lambert law, and compute a concentration from an absorbance and an extinction coefficient.
2. Choose the right blank, and recognise readings outside the linear range of an assay or instrument.
3. Fit a straight-line standard curve by least squares, check its residuals, and interpolate an unknown.
4. Handle unknowns above the top standard by dilution rather than extrapolation, and back-calculate the original concentration.

## Absorbance and the Beer–Lambert law

A spectrophotometer measures the fraction of light transmitted through a sample, T = I/I₀. Absorbance is A = −log₁₀ T, so A = 1 means 10% of the light gets through and A = 2 means 1%. For a dilute solution of one absorbing species,

  A = ε l c,

where ε is the molar extinction coefficient at that wavelength, l the path length and c the concentration. NADH at 340 nm has ε = 6220 M⁻¹ cm⁻¹, so a reading of A₃₄₀ = 0.311 in a 1 cm cuvette means c = 0.311/(6220 × 1) = 5.00 × 10⁻⁵ M, or 50.0 µM. Plate readers have a path length set by the liquid depth, not 1 cm, so either correct for it or calibrate with standards in the same plate.

The law holds only over a limited range. At high absorbance so little light reaches the detector that stray light dominates, and many instruments become unreliable above an absorbance of roughly 1.5–2. At high concentration molecules interact and ε changes. Colorimetric assays such as protein dye-binding assays are often curved even at moderate absorbance. Treat the linear range as something to check, not assume.

## Blanks

The blank sets the instrument's zero and should contain everything the sample contains except the analyte: the same buffer, reagent and cuvette or plate type. A reagent blank in a protein assay is buffer plus dye, not water. For an assay with a standard curve, the zero standard serves as the blank, and blank-subtracted absorbances are used in the fit.

## Building a standard curve

Prepare standards spanning the range you expect, ideally by a [parallel dilution series](02-dilutions-and-dilution-series.md) from one stock, and treat them exactly like the samples.

**Example.** Blank-subtracted absorbances for protein standards are:

| Standard (mg/mL) | 0 | 0.125 | 0.250 | 0.500 | 1.000 |
| --- | --- | --- | --- | --- | --- |
| A₅₉₅ | 0.000 | 0.081 | 0.158 | 0.322 | 0.640 |

A least-squares straight line gives slope b = 0.6404 per (mg/mL) and intercept a = 0.00005, effectively zero. The residuals (observed minus fitted) are all within ±0.0022 and show no pattern, so a straight line describes these standards. A run of residuals that are positive in the middle and negative at the ends would signal curvature, and a non-linear fit or a narrower range would be needed.

An unknown reading A = 0.254 interpolates to c = (0.254 − a)/b = 0.397 mg/mL.

## Unknowns outside the range

An unknown reading 0.812 lies above the top standard (0.640). The fitted line would give 1.27 mg/mL, but that is an extrapolation: nothing shows the response is still linear there. Dilute the sample into the range and measure again. If a fourfold dilution (one part sample plus three parts buffer) reads 0.406, the diluted concentration is 0.634 mg/mL and the original is 4 × 0.634 = 2.54 mg/mL. That differs from the extrapolated value, as it often will for a curving assay. Dilute in the same buffer as the standards.

Below the lowest non-zero standard, results are also unreliable; report them as below the range of the curve rather than as a number.

## Replicates and records

Run standards and unknowns in replicate (duplicates at least, triplicates where the assay is noisy), and report the mean with the spread. Record the wavelength, path length or plate type, blank, standards with their source and preparation, the fitted equation and the range. Make a new curve for each run; standards and reagents age, and a curve from last week does not describe today's reagents.

## Common mistakes

- Blanking with water when the reagent itself absorbs.
- Extrapolating beyond the highest standard instead of diluting.
- Forgetting the dilution factor when back-calculating.
- Fitting a straight line to a curved assay because the correlation coefficient looks high; inspect the residuals.
- Reusing an old standard curve with new reagents.

## Worked example

**Problem.** Using the curve above, triplicate wells of a sample diluted 1:10 (one part in ten parts total) read 0.287, 0.291 and 0.283. What is the protein concentration of the undiluted sample?

**Step 1: mean absorbance.** (0.287 + 0.291 + 0.283)/3 = 0.287.

**Step 2: interpolate.** (0.287 − 0.00005)/0.6404 = 0.448 mg/mL, inside the range of the standards.

**Step 3: undo the dilution.** 10 × 0.448 = 4.48 mg/mL.

**Step 4: report.** 4.48 mg/mL from triplicate readings of a 1:10 dilution, interpolated within a 0–1.000 mg/mL standard curve.

## Limits of this lesson

Absorbance values are synthetic. The extinction coefficient of NADH is a standard value used for illustration. Weighted and non-linear fits, the uncertainty of an interpolated value, scattering samples such as cell suspensions, and fluorescence are not covered.
