# Concentration and solution preparation

Almost every bench procedure begins with a solution someone had to make: a buffer, a medium supplement, a stain, a standard. A concentration error at this stage passes silently into every later result. This lesson covers the concentration units used at the bench, how to calculate what to weigh or measure, and how to make a solution so that it actually has the concentration on the label.

## Learning objectives

By the end of this lesson, you should be able to:

1. Convert between molar, mass, percentage and parts-per-million concentrations, and state which quantity each one fixes.
2. Calculate the mass of a solid to weigh for a target concentration and volume, correcting for water of hydration and reagent purity.
3. Calculate the molarity of a concentrated liquid reagent from its mass percentage and density.
4. Describe how to bring a solution to final volume, and decide when to make a concentrated stock instead of weighing the working amount directly.

## Units that look alike but fix different things

| Unit | Definition | Example |
| --- | --- | --- |
| Molarity, M | moles of solute per litre of final solution | 0.150 M NaCl |
| Mass concentration | mass of solute per volume of final solution | 9.0 g/L, or 1 mg/mL |
| % w/v | grams of solute per 100 mL of final solution | 2% w/v agarose = 2 g in 100 mL |
| % v/v | millilitres of solute per 100 mL of final solution | 70% v/v ethanol |
| % w/w | grams of solute per 100 g of solution | concentrated HCl, 37% w/w |
| ppm (dilute water) | milligrams per litre, approximately | 5 ppm ≈ 5 mg/L |

Every unit except % w/w is defined by the **final volume of solution**, not the volume of solvent added. That single fact explains most preparation errors. The prefixes follow the usual steps of a thousand: 1 M = 1000 mM = 10⁶ µM.

Converting needs the molar mass. Physiological saline, 0.9% w/v NaCl, holds 9 g per litre; with M(NaCl) = 58.44 g/mol that is 9/58.44 = 0.154 mol/L, or 154 mM.

## Weighing a solid: mass = C × V × M

To make a volume V of a solution of molarity C from a solid of molar mass M, weigh

  m = C × V × M.

For 500 mL of 0.150 M NaCl: m = 0.150 mol/L × 0.500 L × 58.44 g/mol = 4.38 g.

Two corrections are common.

- **Water of hydration.** The molar mass is that of the material in the bottle. Calcium chloride is often sold as the dihydrate, CaCl₂·2H₂O, with M = 147.01 g/mol; the anhydrous salt has M = 110.98 g/mol. For 250 mL of 0.100 M CaCl₂ from the dihydrate, weigh 0.100 × 0.250 × 147.01 = 3.68 g. Weighing the anhydrous figure, 2.77 g, of the dihydrate gives only 0.100 × 110.98/147.01 = 0.0755 M, a quarter low.
- **Purity.** If the label states an assay below 100%, divide by it. For 1.00 L of 0.200 M Tris (M = 121.14 g/mol) from material that is 98.0% pure, weigh 0.200 × 1.00 × 121.14/0.980 = 24.7 g.

## Concentrated liquid reagents

Concentrated acids and some solvents are labelled by % w/w and density. One litre of the reagent has a mass of 1000 mL × density, of which the stated fraction is solute. For concentrated hydrochloric acid at 37.0% w/w and 1.18 g/mL:

  C = 1000 × 1.18 × 0.370 / 36.46 = 12.0 mol/L.

To make 250 mL of 1.00 M HCl, measure 1.00 × 250/11.97 = 20.9 mL of the concentrated acid and add it to roughly 200 mL of water before making up to volume. Concentrated acid is added to water, never water to acid, because the heat released when a little water meets a lot of acid can boil and spatter it. This is chemical-hygiene practice; follow the safety data sheet and your laboratory's chemical hygiene plan for any real reagent.

## Making up to volume

Because concentration is defined by the final volume, the solid is dissolved in less solvent than the final volume, and only then is the solution brought to the mark:

1. Weigh the solid into a beaker and dissolve it in about 70–80% of the final volume.
2. Adjust pH now if the recipe calls for it, because acid or base adds volume.
3. Transfer quantitatively to a volumetric flask (rinsing the beaker into the flask), or into a graduated cylinder for less exacting work.
4. Add solvent to the mark, cap and invert to mix.

Adding 500 mL of water to 4.38 g of NaCl does not give 500 mL of 0.150 M solution: dissolved solute changes the volume, and for many solutes the volumes of solute and solvent are not additive. The error is small for dilute salts and large for concentrated sugars, glycerol or ethanol.

## When to make a stock instead

Small amounts are hard to weigh accurately. Ten millilitres of a 50 µM solution of a compound with M = 400 g/mol needs 50 × 10⁻⁶ × 0.010 × 400 = 2.0 × 10⁻⁴ g, which is 0.200 mg, below the minimum weight a typical analytical balance can deliver to 1% (the [weighing lesson](04-balances-and-weighing.md) explains minimum weight). Instead, make 1 mL of a 10 mM stock, which needs 4.00 mg, and dilute it 200-fold as the [dilution lesson](02-dilutions-and-dilution-series.md) describes. Concentrated stocks (10× buffers, 1000× antibiotics, 10 mM drug solutions) also save time and reduce the number of separate weighings that can go wrong.

## Common mistakes

- Using the molar mass of the anhydrous compound for a hydrate.
- Adding the full volume of solvent to the solute instead of making up to the final volume.
- Adjusting pH after bringing to volume, which dilutes the solution.
- Treating % w/w like % w/v when calculating from a concentrated reagent.
- Weighing a sub-milligram amount directly instead of making a stock.

## Worked example

**Problem.** You need 200 mL of 25.0 mM MgSO₄ and the bottle holds MgSO₄·7H₂O (M = 246.47 g/mol, assay 99.5%). How much do you weigh, and how do you make the solution?

**Step 1: moles needed.** 0.0250 mol/L × 0.200 L = 5.00 × 10⁻³ mol.

**Step 2: mass of the hydrate.** 5.00 × 10⁻³ × 246.47 = 1.232 g.

**Step 3: purity.** 1.232/0.995 = 1.24 g.

**Step 4: preparation.** Dissolve 1.24 g in about 150 mL of water, transfer to a 200 mL volumetric flask with rinses, make up to the mark and mix by inversion.

## Limits of this lesson

Molar masses are rounded to two decimals. Non-ideal volumes, temperature effects on volumetric glassware and the activity of ions are ignored. Reagent hazards are mentioned only where they change the procedure; the safety data sheet and your laboratory's chemical hygiene plan govern real handling.
