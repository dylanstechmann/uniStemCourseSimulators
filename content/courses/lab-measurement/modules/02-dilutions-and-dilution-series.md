# Dilutions and dilution series

Diluting is the most frequent calculation at a bench: a 10× buffer to 1×, a stock drug to its working concentration, a culture to countable numbers of colonies, a protein standard into a series. The arithmetic is simple, but the conventions for naming dilutions are inconsistent, and errors compound along a series. This lesson fixes the conventions, sets out serial and parallel series, and shows how pipetting error accumulates.

## Learning objectives

By the end of this lesson, you should be able to:

1. Use C₁V₁ = C₂V₂ to plan a single dilution, and state the dilution factor unambiguously.
2. Design a serial dilution series to reach a target dilution, and compute the dilution of every tube.
3. Back-calculate a concentration in the original sample from a count or a reading in a diluted tube.
4. Compare serial and parallel dilution series, and estimate how pipetting errors propagate along a series.

## One dilution: C₁V₁ = C₂V₂

The amount of solute does not change when solvent is added, so the concentration times the volume is the same before and after: C₁V₁ = C₂V₂. To make 500 mL of 1× buffer from a 10× stock, V₁ = 1 × 500/10 = 50 mL of stock, made up to 500 mL, which means adding 450 mL of water.

A **dilution factor** is the ratio of the final volume to the volume of the sample: 50 mL made up to 500 mL is a tenfold dilution, written 1:10, 1/10 or 10⁻¹. Here 1:10 means one part in ten parts total. Some fields write "1:9" for one part sample plus nine parts diluent, which is the same tenfold dilution. Because the two readings differ, write the volumes in a protocol (for example "100 µL into 900 µL") rather than a ratio alone.

## Serial dilution series

In a serial dilution each tube is made from the previous one. With a constant step of factor f, after n steps the dilution is f⁻ⁿ. A tenfold series of 100 µL into 900 µL, or 10 mL into 90 mL as in the [plate-count protocol](#/bench/decimal-dilution-aerobic-plate-count), gives 10⁻¹, 10⁻², 10⁻³ and so on. A fivefold series of 200 µL into 800 µL reaches 5⁻⁴ = 1/625 after four steps.

Serial series are the only practical way to reach very large dilutions, which is why microbiology uses them to bring a sample containing millions of cells per millilitre down to tens or hundreds of colonies on a plate. The cost is that each tube inherits every earlier error.

**Back-calculation.** The concentration in the original sample is the measured quantity divided by the volume plated and by the dilution of the tube it came from. If 47 colonies grow from 0.1 mL of the 10⁻⁵ tube, the original concentration is 47/(0.1 mL × 10⁻⁵) = 4.7 × 10⁷ CFU/mL. The [plate-count protocol](#/bench/decimal-dilution-aerobic-plate-count) uses the same reasoning to combine plates from several dilutions, as FDA BAM Chapter 3 describes: total colonies on the countable plates divided by the total amount of sample they received.

## Parallel dilution series

In a parallel series every tube is made directly from the same stock. A protein standard curve from a 2.00 mg/mL stock might use 5, 10, 20 and 40 µL each made up to 200 µL, giving 0.0500, 0.100, 0.200 and 0.400 mg/mL. Errors do not accumulate, because no tube depends on another, but very large dilutions would need impractically small volumes of stock. Standard curves usually use parallel series or short serial series for this reason.

## How errors propagate

Suppose each transfer is accurate to within a relative error e, independent from step to step. After n serial steps:

- **Random errors** add in quadrature, so the relative error of the final tube is about e√n. With e = 1% and six steps, about 2.4%.
- **Systematic errors** multiply. A pipette that always delivers 1% too much makes each step slightly stronger than intended, and after six steps the final tube is 1.01⁶ − 1 = 6.2% too concentrated.

A transfer that loses liquid systematically is just as bad. Delivering 98 µL instead of 100 µL into 900 µL gives 98/998 = 0.0982 of the intended 0.1, about 2% low per step. A reused tip or pipet is worse in the other direction: liquid left in it from a stronger tube is carried into a weaker one. In the plate-count simulation a reused pipet carrying 0.1 mL back from a dilution ten times stronger makes each step about 10% too strong, which roughly doubles the count by the fifth dilution.

Three habits keep serial series honest: mix each tube thoroughly before taking from it, use a fresh tip for every transfer, and check pipettes regularly, as in the [gravimetric verification protocol](#/bench/micropipette-gravimetric-verification).

## Common mistakes

- Reading "1:10" as one part plus ten parts when the protocol meant one part in ten.
- Forgetting the dilution of the plated volume itself (0.1 mL plated is another factor of 10 relative to per-millilitre counts).
- Taking from a tube before mixing it, so the sample is not representative.
- Reusing a tip along a series, which carries stronger solution forward.
- Extrapolating a single high-dilution result back to the sample without checking the neighbouring dilutions.

## Worked example

**Problem.** A culture is thought to contain about 10⁸ CFU/mL. You want plates with 30–300 colonies from 0.1 mL spread plates. Which tubes of a tenfold series should you plate, and how do you back-calculate if 152 colonies grow from the 10⁻⁶ tube?

**Step 1: target concentration.** 30–300 colonies from 0.1 mL means 300–3000 CFU/mL in the plated tube.

**Step 2: dilution needed.** 10⁸/3000 to 10⁸/300 is about 10⁻⁴·⁵ to 10⁻⁵·⁵. Plate 10⁻⁵ and the neighbours 10⁻⁴ and 10⁻⁶, because the estimate of 10⁸ could be off by tenfold.

**Step 3: back-calculation.** 152/(0.1 mL × 10⁻⁶) = 1.52 × 10⁹ CFU/mL, so the culture was denser than thought, and the 10⁻⁶ tube was the right one to rely on.

## Limits of this lesson

Error estimates assume independent, normally distributed transfer errors and perfect mixing. Counting statistics (the Poisson spread of colony counts), the ranges and rounding rules of specific counting methods, and plate-to-plate variation are only touched on; the plate-count protocol follows FDA BAM Chapter 3 for those.
