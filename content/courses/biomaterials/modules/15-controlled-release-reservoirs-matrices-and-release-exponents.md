# Controlled-release kinetics: reservoirs, matrices, burst and release exponents

The [degradation and release lesson](05-degradation-and-release-time-scales.md) estimated how long a solute takes to diffuse out of a hydrogel and compared that time with a repair timeline. This lesson turns the time scale into a release profile. A delivery device can hold a drug behind a rate-limiting membrane, disperse it through a matrix, or tie its release to degradation, and each design gives a characteristic shape of cumulative release against time. Recognizing those shapes, and the assumptions behind the equations that produce them, is the first step in reading release data. All devices, solutes and data here are synthetic teaching examples. Nothing here is a formulation or clinical recommendation.

The undergraduate [MIT OCW 3.051J Materials for Biomedical Applications (Spring 2006) syllabus](https://ocw.mit.edu/courses/3-051j-materials-for-biomedical-applications-spring-2006/pages/syllabus/) lists drug delivery among its applications, and this course's scope crosswalk recorded it as outside the selected local strand. This lesson adds a bounded kinetic treatment within the local release week. It uses 3.051J as a scope comparator only and reproduces no MIT material.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate the constant release rate from a membrane-controlled reservoir, and identify when zero-order release ends.
2. Apply the Higuchi square-root model for a drug dispersed above its solubility in a matrix, and the early-time Fickian solution for a slab, including estimating a diffusion coefficient from a release fraction.
3. Compare zero-order, square-root and first-order profiles, fit a release exponent from two time points, and explain burst release and the limits of exponent-based mechanism claims.

## Reservoirs: zero-order release

In a reservoir device, the drug sits in a core, often as excess solid that keeps the inner solution saturated at C_s, behind a polymer membrane of thickness h. If the outside is a **sink**, kept near zero concentration, Fick's first law through the membrane gives a constant flux:

**dM/dt = A D K C_s / h,**

where A is the membrane area, D the drug's diffusion coefficient in the membrane and K the partition coefficient between membrane and core solution. Constant rate means **zero-order release**: the cumulative amount rises linearly in time.

**Synthetic example.** With A = 2.0 cm², D = 1.0 × 10⁻⁷ cm²/s, K = 0.50, C_s = 10 mg/mL and h = 0.010 cm, the rate is 1.0 × 10⁻⁴ mg/s, or **0.36 mg/h**. A 50 mg load would sustain that rate for at most 50/0.36 = **139 h**, about 5.8 days. In practice the rate falls earlier, once the excess solid dissolves and the core concentration drops below C_s. Release then becomes first-order. A time lag also occurs at the start while the membrane fills, and a burst occurs if drug has already migrated into the membrane during storage.

## Matrices: square-root release

Disperse the drug through a non-degrading polymer matrix at a loading A_L, well above its solubility C_s in the matrix. Drug near the surface dissolves and diffuses out first, and a depletion front moves inward. Release slows because each new portion must travel farther. The Higuchi model gives the cumulative amount released per unit area as

**Q = √[D (2A_L − C_s) C_s t].**

**Synthetic example.** With A_L = 50 mg/cm³, C_s = 2.0 mg/cm³ and D = 1.0 × 10⁻⁶ cm²/s, Q is **4.12 mg/cm²** after one day and **8.23 mg/cm²** after four. Quadrupling the time only doubles the release. The model assumes A_L ≫ C_s, a planar geometry, perfect sink conditions, a constant D and a matrix that neither swells nor erodes. It stops applying as the front approaches the centre of the device.

**Dissolved drug in a slab.** If the drug is fully dissolved at a uniform initial concentration in a slab of thickness L that releases from both faces, the exact Fickian solution has a simple early-time form:

**M_t/M_∞ ≈ 4√[D t/(π L²)],** valid for M_t/M_∞ below about 0.6.

This again rises as √t. It can be inverted for D. If a synthetic 0.10 cm slab releases 20% of its drug in 1.0 h, then D = π L² (0.20/4)²/t = **2.2 × 10⁻⁸ cm²/s**.

## First-order release and degradation-linked release

When the driving concentration falls in proportion to the drug remaining, or when release follows a first-order degradation as in the earlier lesson, the cumulative fraction is

**M_t/M_∞ = 1 − e^(−kt).**

With k = 0.10 h⁻¹, 70% is released after 12 h and the half-time is 6.9 h. The rate is fastest at the start and decays exponentially.

## Recognizing the shape: release exponents

A common empirical summary fits the early data, up to about 60% released, to

**M_t/M_∞ = k t^n.**

On log–log axes this is a straight line with slope n. For a thin slab, n = 0.5 is consistent with Fickian diffusion, n = 1 with zero-order or swelling-controlled transport, and values between with mixed behaviour. (The diagnostic values differ for cylinders and spheres, about 0.45 and 0.43.)

**Synthetic example.** A slab releases 20% at 1 h and 40% at 4 h. Then n = log(0.40/0.20)/log 4 = **0.50**, consistent with Fickian diffusion.

An exponent is a description, not a proof of mechanism. Different mechanisms can give similar exponents, burst release distorts the early points, and fitting beyond 60% biases n downward.

## Burst release

Many matrices release a large fraction in the first hour or so. Drug deposited at or near the surface during fabrication dissolves immediately, and porous or cracked matrices expose more drug than the ideal geometry assumes. A burst can be intended, as a rapid initial release, or an unwanted spike. In data, it appears as a non-zero intercept or as an early slope steeper than the √t trend predicts. Reporting the burst separately, and fitting the rest of the curve after it, avoids attributing a surface effect to bulk diffusion.

## Common mistakes

- Calling any declining-rate curve first-order; √t and exponential profiles differ and need a log or √t plot to tell apart.
- Assuming a reservoir is zero-order to the end; it is constant only while the core stays saturated and the outside stays a sink.
- Applying the Higuchi model when the loading is near or below the solubility.
- Fitting a release exponent to data above about 60% released, or including a burst.
- Treating n = 0.5 as proof of diffusion control in every geometry.
- Mixing hours and seconds when D is in cm²/s.

## Worked example

**Problem.** A synthetic reservoir has A = 3.0 cm², D = 5.0 × 10⁻⁸ cm²/s, K = 0.40, C_s = 8.0 mg/mL and h = 0.020 cm, with a sink outside. Find the release rate per hour, and decide which profile a second, matrix device follows if it releases 30% at 1 h and 45% at 3 h.

**Step 1: reservoir rate.** dM/dt = 3.0 × 5.0 × 10⁻⁸ × 0.40 × 8.0/0.020 = 2.4 × 10⁻⁵ mg/s = 0.0864 mg/h.

**Step 2: duration check.** At this rate, each milligram of releasable drug in the saturated regime lasts about 11.6 h, so a reservoir sized for weeks needs a large excess of solid drug.

**Step 3: matrix exponent.** n = log(0.45/0.30)/log 3 = 0.37. That is below 0.5, which for a slab suggests either a burst inflating the 1 h point or a geometry or distribution effect, not a cleaner Fickian process.

**Step 4: what to check.** Plot cumulative release against √t. If the line has a positive intercept, report the burst and refit the later points before inferring any mechanism.

## Limits of this lesson

All devices, solutes and data are synthetic. The models assume perfect sink conditions, constant diffusion and partition coefficients, ideal planar geometry and non-interacting solutes. Swelling, polymer erosion coupled to diffusion, drug–polymer binding, osmotic pumping, stimulus-responsive release, in vivo clearance and pharmacokinetics are not developed. Nothing here is a formulation, dosing schedule, release specification or clinical recommendation for any real drug or device. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
