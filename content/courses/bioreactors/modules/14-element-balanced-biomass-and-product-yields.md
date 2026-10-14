# Element-balanced biomass and product yields

Monod kinetics tells how a modeled specific growth rate changes with a limiting-substrate concentration. It does not by itself say how substrate atoms are divided among new biomass, a product, carbon dioxide, and water. A stoichiometric equation supplies that accounting for a declared reaction model. This original exercise uses a synthetic biomass formula and synthetic product; it describes no real cell line or production pathway.

## Learning objectives

By the end of this lesson, you should be able to:

1. Solve unknown stoichiometric coefficients using separate carbon, hydrogen, oxygen, and nitrogen balances.
2. Calculate biomass and product yields from a balanced reaction and verify carbon recovery.
3. Explain how a stoichiometric yield model differs from Monod kinetics and what the stipulated equation cannot establish.

## Set up the declared reaction

Use one mole of glucose, **C₆H₁₂O₆**, as the basis. Let **X = CH₁.₈O₀.₅N₀.₂** be a stipulated empirical biomass unit containing one carbon-mole, and let **P = C₂H₆O** be a purely symbolic product. Suppose the synthetic model allocates two carbon-moles to biomass, one mole to product, and the remaining carbon to carbon dioxide:

**C₆H₁₂O₆ + a NH₃ + b O₂ → 2 X + 1 P + c CO₂ + d H₂O.**

Treat the displayed formulas and coefficients as exact for this bookkeeping exercise. Balance one element at a time; do not infer the coefficients from a growth-rate equation.

## Balance each element

**Carbon:** six carbon-moles enter with glucose. Two go to biomass and two to product, leaving **c = 2** for carbon dioxide: 6 = 2 + 2 + c.

**Nitrogen:** each X unit contains 0.2 N, and two units are produced. Ammonia is the only nitrogen source, so **a = 2 × 0.2 = 0.4 mol NH₃**.

**Hydrogen:** the inputs contain 12 + 3a = 13.2 mol H atoms. Biomass and product contain 2 × 1.8 + 6 = 9.6 mol H atoms. Water supplies the remaining 3.6 mol H atoms, so **d = 3.6/2 = 1.8 mol H₂O**.

**Oxygen:** glucose and oxygen gas supply 6 + 2b mol O atoms. The products contain 2 × 0.5 + 1 + 2c + d = 7.8 mol O atoms. Therefore 6 + 2b = 7.8 and **b = 0.9 mol O₂**.

The closed synthetic equation is

**C₆H₁₂O₆ + 0.4 NH₃ + 0.9 O₂ → 2 X + P + 2 CO₂ + 1.8 H₂O.**

Check all four totals: C = 6, H = 13.2, O = 7.8, and N = 0.4 mol of atoms on each side. Each balance closes independently.

## Convert coefficients to yields

For every mole of glucose consumed under this fixed equation, the modeled yields are **2 C-mol biomass/mol glucose**, **1 mol P/mol glucose**, and **0.9 mol O₂ consumed/mol glucose**. The carbon recovery is (2 C-mol in X + 2 C-mol in P + 2 mol C in CO₂)/6 C-mol in glucose = **1.00**, or 100%.

If the stipulated reaction extent were 10 mmol of glucose, linear scaling of this equation would give 20 C-mmol of X, 10 mmol of P, 20 mmol of CO₂, 9 mmol of O₂ consumed, 4 mmol of NH₃ consumed, and 18 mmol of water formed. This is a stoichiometric calculation under an unchanged equation, not a forecast of an operating culture.

## What this model does and does not say

Monod kinetics models a rate as a function of substrate concentration. The balanced reaction encodes a particular distribution of atoms and an implied yield. A complete process model would also need rates, maintenance, additional nutrients and products, gas transfer, accumulation, and condition-dependent physiology. A closed elemental balance is a necessary accounting check; it does not identify a biochemical pathway, prove that the product forms, or establish a real biomass composition or yield.

All formulas and values here are synthetic. The biomass formula is a stipulated surrogate, P is only a formula label, and no process, cell line, feed, or operating condition is recommended. MIT OCW 10.442 Spring 2005 is an undergraduate comparator whose calendar assigns sessions 11–12 to stoichiometry of growth and product formation. This single worked sequence addresses only a narrow part of that course.
