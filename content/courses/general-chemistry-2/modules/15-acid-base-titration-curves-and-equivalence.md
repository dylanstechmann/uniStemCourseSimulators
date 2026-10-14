# Acid–base titration curves: equivalence, buffer regions and indicators

The buffer lessons predicted pH for a chosen mixture of a weak acid and its conjugate base, and the [charge-balance lesson](09-coupled-acid-speciation-and-charge-balance.md) solved pH from analytical totals. A **titration** sweeps through every such mixture. Base is added in measured portions to an acid, or the reverse, and the pH is recorded against the added volume. The resulting curve finds an unknown concentration from the equivalence volume, reads a pKa from the half-equivalence point, and shows why some indicators work and others mislead. This lesson computes the four regions of a titration curve, compares strong and weak acids, and checks the shortcuts against an exact charge-balance solution. All solutions are synthetic teaching systems at 25 °C.

The undergraduate [MIT OCW 5.111SC Principles of Chemical Science (Fall 2014) Unit III](https://ocw.mit.edu/courses/5-111sc-principles-of-chemical-science-fall-2014/pages/unit-iii-thermodynamics-chemical-equilibrium/) closes its equilibrium sequence with salt solutions and buffers (Lecture 22) followed by two lectures on acid–base titrations (Lectures 23–24). This lesson follows that placement within the local acid–base block. It uses 5.111SC as a scope comparator only and reproduces no MIT material.

## Learning objectives

By the end of this lesson, you should be able to:

1. Use the equivalence volume to find an unknown concentration, and identify the stoichiometric regions of a titration curve.
2. Calculate pH at the start, in the buffer region, at equivalence and beyond equivalence for strong-acid and weak-acid titrations with a strong base, and check the shortcuts against an exact charge balance.
3. Explain why the equivalence pH of a weak-acid titration lies above 7, read pKa from the half-equivalence point, choose an indicator whose transition brackets the equivalence pH, and locate the equivalence points of a diprotic acid.

## Conventions

Concentrations are in mol/L and volumes in mL; millimoles are mL × mol/L. As in the speciation lesson, K_a is a concentration-form teaching parameter under an ideal-solution convention, and K_w = 1.0 × 10⁻¹⁴ at 25 °C. The strong base is fully dissociated NaOH, and Na⁺ is a spectator ion. Volumes are taken as additive.

## Equivalence and stoichiometry

The **equivalence point** is reached when the added base exactly matches the acid in stoichiometric amount: n_base = n_acid for a monoprotic acid. This is a stoichiometric statement, independent of the pH there. If 20.00 mL of an unknown monoprotic acid requires 16.40 mL of 0.1000 M NaOH, the acid amount is 1.640 mmol and its concentration is 1.640/20.00 = **0.0820 M**. The acid's strength changes the shape of the curve, not the equivalence volume.

The **endpoint** is what an experiment observes, such as an indicator colour change or the steepest point of a measured curve. A good method makes the endpoint fall close to the equivalence point.

## A weak acid titrated with a strong base

Take 25.00 mL of 0.100 M weak acid HA with pK_a = 4.76 (K_a = 1.74 × 10⁻⁵), titrated with 0.100 M NaOH. The equivalence volume is 25.00 mL. Neutralize first, then re-equilibrate, as in the first buffer lesson:

- **Start (0 mL).** Only the weak acid is present. Solving K_a = x²/(C − x) gives [H⁺] = 1.31 × 10⁻³ M and **pH 2.88**.
- **Buffer region (0 to 25 mL).** Each mmol of OH⁻ converts one mmol of HA to A⁻. At 20.00 mL, 2.00 mmol of A⁻ and 0.50 mmol of HA remain, and Henderson–Hasselbalch gives pH = 4.76 + log(2.00/0.50) = **5.36**. The total volume cancels in the ratio.
- **Half-equivalence (12.50 mL).** Half the acid is converted, so [A⁻] = [HA] and **pH = pK_a = 4.76**. This is how a titration curve measures pK_a.
- **Equivalence (25.00 mL).** All of the acid is now A⁻: 2.50 mmol in 50.00 mL, or 0.0500 M. A⁻ is a weak base with K_b = K_w/K_a = 5.75 × 10⁻¹⁰. Then [OH⁻] = √(K_b × 0.0500) = 5.36 × 10⁻⁶ M, pOH 5.27 and **pH 8.73**. The solution is basic because the conjugate base takes protons from water.
- **Beyond equivalence (26.00 mL).** The excess 0.10 mmol OH⁻ in 51.00 mL gives [OH⁻] = 1.96 × 10⁻³ M and **pH 11.29**. Excess strong base dominates; the weak base A⁻ adds negligibly.

## A strong acid titrated with a strong base

Repeat with 25.00 mL of 0.100 M HCl. Before equivalence, the excess H⁺ sets the pH directly: at 24.00 mL, 0.10 mmol H⁺ remains in 49.00 mL, so **pH 2.69**. At equivalence, only Na⁺, Cl⁻ and water remain, so **pH 7.00**. Beyond it, the curve matches the weak-acid curve: **pH 11.29** at 26.00 mL.

The two curves differ most before equivalence. The strong acid starts lower, has no buffer plateau and rises more steeply at equivalence. The weak acid starts higher, rises gently through its buffer region and has a shorter, higher jump centred near pH 8.7. Weaker or more dilute acids give still smaller jumps, which makes the endpoint harder to locate.

## Checking against an exact charge balance

The shortcuts treat each region separately. The exact curve comes from a single equation. With C_A the total acid and C_Na the sodium, both diluted to the current volume,

**C_Na + [H⁺] = C_A K_a/(K_a + [H⁺]) + K_w/[H⁺].**

This is the electroneutrality relation from the speciation lesson with one acid–base pair. Solving it for [H⁺] at each volume gives pH 2.883, 4.761, 5.362, 8.730 and 11.292 at 0, 12.50, 20.00, 25.00 and 26.00 mL. Every shortcut above agrees to within 0.001 pH. The exact half-equivalence pH differs slightly from pK_a because a little extra HA has dissociated. The shortcuts fail mainly for very dilute or very weak acids, or within a few drops of equivalence, where several terms are comparable.

## Indicators

An indicator is itself a weak acid whose two forms have different colours. Its colour changes over roughly pK_In ± 1, and the transition range should bracket the equivalence pH. For the weak-acid titration above (equivalence pH 8.73), an indicator changing over about 8.2–10.0 is suitable. One changing over about 3.8–5.4 would change colour in the buffer region, long before equivalence. For the strong-acid titration, the jump is steep enough that indicators changing anywhere from about pH 4 to 10 give nearly the same endpoint volume. These ranges are illustrative teaching values, not specifications for any particular dye.

## Diprotic acids

A diprotic acid H₂A has two equivalence points, at one and two moles of base per mole of acid. For 20.00 mL of 0.0500 M H₂A titrated with 0.100 M NaOH, they fall at **10.00 mL** and **20.00 mL**. When the two pK_a values are well separated, the curve shows two buffer regions. Their midpoints, at 5.00 mL and 15.00 mL, have pH ≈ pK_a1 and pH ≈ pK_a2. At the first equivalence point the solution is mostly HA⁻, the species the speciation lesson found prevailing between the two pK_a values. When the pK_a values are close, the first jump blurs.

## Common mistakes

- Assuming the equivalence point is always at pH 7; that holds only for a strong acid with a strong base.
- Using Henderson–Hasselbalch at the very start or at equivalence, where one partner is absent.
- Forgetting the dilution from added titrant when computing concentrations at equivalence or beyond.
- Treating the endpoint as identical to the equivalence point.
- Choosing an indicator by its colour rather than by its transition range relative to the equivalence pH.
- Expecting a stronger acid to need more base; at the same concentration and volume, both need the same equivalence volume.

## Worked example

**Problem.** 20.00 mL of 0.0800 M weak acid (pK_a 4.20) is titrated with 0.100 M NaOH. Find the equivalence volume, the pH at equivalence, and the pH after 8.00 mL of base, and choose a suitable indicator range.

**Step 1: equivalence volume.** The acid amount is 1.600 mmol, so V_eq = 1.600/0.100 = 16.00 mL.

**Step 2: equivalence pH.** 1.600 mmol of A⁻ in 36.00 mL is 0.0444 M. K_b = 10⁻¹⁴/10⁻⁴·²⁰ = 1.58 × 10⁻¹⁰, so [OH⁻] = √(1.58 × 10⁻¹⁰ × 0.0444) = 2.65 × 10⁻⁶ M and pH = **8.42**.

**Step 3: halfway.** 8.00 mL is half of V_eq, so pH ≈ pK_a = **4.20**.

**Step 4: indicator.** The transition should bracket pH 8.4, so a range near 8–10 fits. A range near 4–5 would change colour at the half-equivalence point and report about half the true acid amount.

## Limits of this lesson

All solutions, constants and indicator ranges are synthetic or illustrative. The analysis uses concentration-form equilibrium constants under an ideal-solution convention, additive volumes, 25 °C and fully dissociated titrant. Activity corrections, carbon dioxide absorption, temperature effects, electrode calibration and indicator error are not modelled. Polyprotic titrations are treated qualitatively beyond their equivalence volumes. Nothing here is a laboratory procedure or handling instruction. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
