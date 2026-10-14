# Closed-loop poles as the gain changes: Routh–Hurwitz and the root locus

The feedback lesson showed that closing a loop replaces the plant's poles with the roots of 1 + G(s). With a proportional controller of gain K, the loop is K·G(s), so the closed-loop poles move as K changes. This lesson answers two questions about that motion without solving a polynomial for every gain. The **Routh–Hurwitz criterion** tells for which gains every closed-loop pole lies in the left half-plane. The **root locus** sketches where the poles travel as K goes from zero to large values. All plants and numbers are synthetic teaching models.

The undergraduate [MIT OCW 2.004 Dynamics and Control II (Spring 2008) calendar](https://www.ocw.mit.edu/courses/2-004-dynamics-and-control-ii-spring-2008/pages/calendar/) spends lectures 25–29 on Routh–Hurwitz stability and root-locus development, directly after closed-loop steady-state error and before Bode plots. This lesson follows that placement within the local feedback week and uses 2.004 as a scope comparator only. It reproduces no MIT material.

## Learning objectives

By the end of this lesson, you should be able to:

1. Build a Routh array for a closed-loop characteristic polynomial, find the range of proportional gain that keeps the loop stable, and count right-half-plane poles from sign changes.
2. Sketch a root locus from its construction rules (start and end points, real-axis segments, asymptotes and centroid, breakaway point, imaginary-axis crossing) and read gains from it.
3. Connect the stability limit to the gain margin, and state what these polynomial methods cannot handle, including time delay.

## The characteristic polynomial with a gain

Take the synthetic plant **G(s) = 1/((s + 1)(s + 2)(s + 3))**, which could stand for three first-order lags in series (a heater, a vessel wall and a sensor), under proportional control with gain K and negative unity feedback. The closed-loop poles are the roots of 1 + K G(s) = 0, which after clearing the denominator is

**s³ + 6s² + 11s + (6 + K) = 0.**

At K = 0 the poles are the open-loop poles −1, −2 and −3. As K grows, only the constant term changes, and the roots move.

A first check needs no array. For a polynomial with real coefficients, **every coefficient must have the same sign** for all roots to lie in the left half-plane. For K > −6 all four coefficients are positive, so the check passes. The condition is necessary but not sufficient beyond second order: a cubic with all-positive coefficients can still have two unstable roots.

## The Routh array

For a cubic a₃s³ + a₂s² + a₁s + a₀, write the coefficients in two rows and compute the rest:

| Row | First column | Second column |
| --- | --- | --- |
| s³ | a₃ = 1 | a₁ = 11 |
| s² | a₂ = 6 | a₀ = 6 + K |
| s¹ | (a₂a₁ − a₃a₀)/a₂ = (66 − 6 − K)/6 | 0 |
| s⁰ | a₀ = 6 + K | |

The **number of sign changes in the first column equals the number of right-half-plane roots**. All roots lie in the left half-plane exactly when every first-column entry is positive. Here that requires 60 − K > 0 and 6 + K > 0. For a positive gain, the loop is **stable for 0 < K < 60**.

- At **K = 10** the first column is 1, 6, 8.33, 16, so there are no sign changes and the loop is stable.
- At **K = 100** it is 1, 6, −6.67, 106, so there are two sign changes and **two right-half-plane poles**.
- At **K = 60** the s¹ entry is zero. The row above gives the **auxiliary polynomial** 6s² + 66 = 0, so s = ±j√11. The loop is marginally stable and would oscillate at **ω = √11 ≈ 3.32 rad/s**.

## Sketching the root locus

The root locus traces all closed-loop poles as K runs from 0 to ∞. A few rules give its shape without a computer:

1. **Start and end.** There is one branch per open-loop pole. Branches start at the open-loop poles (K = 0) and end at open-loop zeros or travel to infinity. This plant has three poles and no zeros, so all three branches go to infinity.
2. **Real-axis segments.** A real-axis point lies on the locus if an **odd** number of real open-loop poles and zeros lie to its right. That gives the segments between −1 and −2, and to the left of −3.
3. **Asymptotes.** Branches that go to infinity approach straight lines. Their number is n − m (poles minus zeros) = 3. They meet at the **centroid** σ = (Σpoles − Σzeros)/(n − m) = (−1 − 2 − 3)/3 = **−2**, at angles of ±60° and 180°.
4. **Breakaway point.** Two branches on the segment between −1 and −2 meet and leave the axis where K = −(s + 1)(s + 2)(s + 3) is largest along that segment. Setting dK/ds = 0 gives 3s² + 12s + 11 = 0, whose root in the segment is **s = −1.423**. There K = **0.385**: the two dominant poles are equal, which is the critically damped point.
5. **Imaginary-axis crossing.** The Routh calculation already found it, at ±j3.32 when K = 60.

Putting these together: as K rises from zero, the poles at −1 and −2 move toward each other, meet at −1.423, then split into a complex pair. The pair heads toward the ±60° asymptotes and crosses into the right half-plane at K = 60. The pole that starts at −3 moves left along the axis.

## Reading a design gain from the locus

The locus turns a design question into geometry. A damping ratio ζ corresponds to a ray from the origin at angle arccos ζ from the negative real axis. For **ζ = 0.5** that ray is at 60°. The complex branch meets it at **K ≈ 8.00**, where the dominant poles are −0.917 ± j1.588 and the third pole is at −4.17. The third pole is about 4.5 times farther left, so the pair's second-order behavior dominates the response, with roughly 16% overshoot from the second-order lesson. Check the arithmetic: the three poles sum to −6, the negative of the s² coefficient, as they must.

## Stability limit and gain margin

The gain margin from the margins lesson measures how much the loop gain can grow before the loop reaches the stability boundary. Routh gives the same number directly: at a nominal gain K₀, **GM = 60/K₀**. For K₀ = 10, GM = 6, or 20 log₁₀ 6 ≈ 15.6 dB. The frequency-response method agrees. The phase of G(jω) reaches −180° at ω = √11, where |G(j√11)| = 1/(√12·√15·√20) = 1/60, so the loop K·G has unit magnitude there exactly when K = 60.

## Common mistakes

- Treating all-positive coefficients as proof of stability for third- and higher-order polynomials.
- Counting negative entries rather than sign changes in the Routh first column.
- Placing real-axis locus segments to the left of an even number of poles and zeros.
- Computing the centroid from poles only when the loop has zeros.
- Reading the breakaway gain as a stability limit; it marks where poles become complex, not where they become unstable.
- Applying Routh directly to a loop with a pure time delay, whose characteristic equation is not a polynomial.

## Worked example

**Problem.** For the same plant with gain K₀ = 20, is the loop stable, what is its gain margin, and roughly where are its dominant poles relative to the ζ = 0.5 design?

**Step 1: Routh.** With K = 20 the first column is 1, 6, (66 − 26)/6 = 6.67 and 26. There are no sign changes, so the loop is stable.

**Step 2: margin.** GM = 60/20 = **3**, about 9.5 dB.

**Step 3: locus position.** K = 20 is above the ζ = 0.5 gain of 8.00, so the complex pair has moved farther along its branch toward the imaginary axis. Damping is lower, and the response will overshoot more than the ζ = 0.5 design. Raising K buys speed and steady-state accuracy at the cost of damping and margin.

## Limits of this lesson

All plants and numbers are synthetic, and the analysis assumes a linear, time-invariant, rational model with proportional control and no actuator saturation. A pure time delay e^(−sT) makes the characteristic equation transcendental. Routh cannot then be applied directly, and the delay-margin analysis of the margins lesson is needed (a Padé approximation would be only an approximation). Root-locus rules give a sketch, not exact pole positions; precise values here come from solving the polynomial. A model that is stable for a gain range says nothing about unmodeled dynamics, and nothing here is a controller setting or a statement about any real device.
