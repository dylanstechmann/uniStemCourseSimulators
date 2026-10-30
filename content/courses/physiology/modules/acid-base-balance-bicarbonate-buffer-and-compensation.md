# Acid–base balance: the bicarbonate buffer, ventilation and the kidney

Metabolism produces acid and carbon dioxide continuously, yet the pH of arterial blood stays within a narrow band around 7.40. Two organs share the work. The lungs control how much CO₂ leaves, and the kidney controls how much bicarbonate is kept and how much new bicarbonate is made. This lesson turns that division of labour into one equation, the Henderson–Hasselbalch relation, and uses it to reason about disturbances, compensation and the slow ledger that the kidney must balance. It builds on the [alveolar ventilation relation](11-respiratory-mechanics-and-gas-exchange.md), the [loop-gain relation](08-homeostasis-balance-and-feedback-gain.md) and the [buffer chemistry](../../general-chemistry-2/modules/01-acid-base-equilibria-and-buffers.md) of General Chemistry II.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute pH from bicarbonate concentration and P_CO₂ with the Henderson–Hasselbalch relation, and predict the direction and size of a change from the logarithm of the ratio.
2. Classify a disturbance as respiratory or metabolic from the term that moved, and calculate the ventilation change, the compensated pH and the loop gain of a compensation.
3. Use a daily acid ledger and the filtered bicarbonate load to show how the slow renal term can drift when net acid excretion falls short.
4. Use electroneutrality (the anion gap) and the CO₂ Fick balance to read ion and gas data without over-interpreting them.

## One buffer, two controlled terms

Carbon dioxide dissolves in water and slowly hydrates to carbonic acid, which dissociates; the enzyme carbonic anhydrase brings the reaction to equilibrium quickly inside red cells and in the kidney:

**CO₂ + H₂O ⇌ H₂CO₃ ⇌ H⁺ + HCO₃⁻.**

Combining the equilibrium constants into one effective constant, and writing dissolved CO₂ as α × P_CO₂, gives

**pH = 6.1 + log₁₀( [HCO₃⁻] / (0.03 × P_CO₂) ),**

with [HCO₃⁻] in mmol/L, P_CO₂ in mmHg, and α = 0.03 mmol/L per mmHg at body temperature. These are standard textbook values used here as round teaching constants. For [HCO₃⁻] = 24 and P_CO₂ = 40, dissolved CO₂ is 0.03 × 40 = 1.2 mmol/L, the ratio is 24/1.2 = 20, and pH = 6.1 + log₁₀ 20 = 7.40, which is a hydrogen-ion concentration of about 39.7 nmol/L.

Two things make this system useful. The pK′ of 6.1 is far below 7.4, so by itself a closed bicarbonate solution would buffer only weakly at this pH. In the body, however, the system is **open**: ventilation holds P_CO₂ and the kidney holds [HCO₃⁻], so each term is regulated rather than allowed to drift. And because pH depends on the logarithm of a **ratio**, only the ratio matters. Doubling P_CO₂ at fixed bicarbonate halves the ratio and lowers pH by log₁₀ 2 = 0.30; doubling both terms together leaves pH unchanged.

## Four primary disturbances

A disturbance is named for the term that moves first.

| Primary change | Name | Typical cause in the model |
| --- | --- | --- |
| P_CO₂ rises | respiratory acidosis | alveolar ventilation too low for the CO₂ produced |
| P_CO₂ falls | respiratory alkalosis | alveolar ventilation too high |
| [HCO₃⁻] falls | metabolic acidosis | added acid consumes bicarbonate, or bicarbonate is lost |
| [HCO₃⁻] rises | metabolic alkalosis | acid is lost or base is added |

The respiratory cause follows from the [alveolar relation](11-respiratory-mechanics-and-gas-exchange.md): P_ACO₂ ≈ 0.863 × V̇_CO₂ / V̇_A. If alveolar ventilation falls to 60% of its value with CO₂ production unchanged, P_CO₂ rises from 40 to 40/0.6 = 66.7 mmHg. With bicarbonate still 24 mmol/L the ratio is 24/2.0 = 12 and pH = 6.1 + log₁₀ 12 = 7.18. That change takes minutes.

**The same pH can come from different disturbances.** [HCO₃⁻] = 24 with P_CO₂ = 80 gives a ratio of 24/2.4 = 10 and pH 7.10. [HCO₃⁻] = 12 with P_CO₂ = 40 gives 12/1.2 = 10 and the same pH 7.10. One is respiratory, the other metabolic, and pH alone cannot tell them apart: a second number is needed.

## Compensation moves the other term

A compensation does not fix the cause. It moves the *other* term in the same direction, so that the ratio returns toward 20. In the metabolic case above (bicarbonate 12 mmol/L), the lungs can respond by raising ventilation until P_CO₂ falls to, say, 28 mmHg. The ratio becomes 12/0.84 = 14.3 and pH = 6.1 + log₁₀ 14.3 = 7.255. By the same P_ACO₂ relation with V̇_CO₂ = 200 mL/min, the required alveolar ventilation rises from 0.863 × 200/40 = 4.32 to 0.863 × 200/28 = 6.16 L/min, an increase of 43%.

The result is better than 7.100 but not 7.401. This is the steady-state error of a proportional controller, and the [loop-gain relation](08-homeostasis-balance-and-feedback-gain.md) applies directly. The uncompensated deviation is d = 7.401 − 7.100 = 0.301; the compensated deviation is e = 7.401 − 7.255 = 0.146. Then G = d/e − 1 = 1.06, and the compensation removed 1 − e/d = 51% of the disturbance. A higher gain would leave less error; it cannot leave none.

The two organs also differ in speed. Ventilation changes P_CO₂ within minutes. The kidney changes bicarbonate over days. A chronic respiratory acidosis with P_CO₂ = 60 mmHg and renal retention that has raised bicarbonate to 30 mmol/L gives a ratio of 30/1.8 = 16.7 and pH = 7.32, much nearer 7.40 than the 6.1 + log₁₀(24/1.8) = 7.22 that the acute case would show.

## The kidney as a ledger

The renal term is a quantity of bicarbonate, so it is best handled as a ledger. Two parts matter.

**Reclaiming filtered bicarbonate.** With a glomerular filtration rate of 180 L/day and plasma bicarbonate of 24 mmol/L, the filtered load is 180 × 24 = 4320 mmol/day. Almost all of it must be reabsorbed. A reabsorption shortfall of only 1% loses 43.2 mmol/day, which is large next to the acid load below. This is the same arithmetic as [clearance and tubular handling](06-renal-clearance-and-tubular-handling.md): excretion equals filtered load minus reabsorption, and a small fractional error in a large flow is a large absolute error.

**Excreting the daily acid load.** In the model a person produces 70 mmol/day of non-volatile acid. To keep bicarbonate constant, net acid excretion (titratable acid plus ammonium, minus any bicarbonate excreted) must equal 70 mmol/day. Suppose it is only 60. The shortfall of 10 mmol/day is taken from a bicarbonate pool that, in this simplified model, is spread through 14 L of extracellular fluid, ignoring intracellular and bone buffers. Bicarbonate then falls by 10/14 = 0.71 mmol/L per day, to 24 − 5 = 19 mmol/L after seven days. At P_CO₂ = 40 the pH would be 6.1 + log₁₀(19/1.2) = 7.30. A modest, steady mismatch is invisible in a day and obvious in a week.

This is a reserve problem of the kind described in [compensation and reserve](14-compensation-and-reserve.md): a normal bicarbonate value says the ledger balances, not how much capacity was used to balance it. General textbook statements that kidney function declines on average with age belong in that discussion; no age-related figure is cited or used here.

## Reading ion data: the anion gap

Blood is electrically neutral, so measured cations plus unmeasured cations equal measured anions plus unmeasured anions. Rearranged, the **anion gap**

**AG = [Na⁺] − [Cl⁻] − [HCO₃⁻]**

equals unmeasured anions minus unmeasured cations. With Na⁺ = 140, Cl⁻ = 104 and HCO₃⁻ = 24 mmol/L, AG = 12 in this model. Two acidoses with bicarbonate at 12 look different on this ledger. If chloride stays 104, AG = 140 − 104 − 12 = 24: the lost bicarbonate was replaced by an unmeasured anion, as when an acid with its own anion is added. If chloride rises to 116, AG = 140 − 116 − 12 = 12: chloride replaced the bicarbonate and the gap is unchanged. The gap is bookkeeping, not a measurement of pH or of any one cause; it can be unchanged in a real disturbance and it says nothing about the respiratory term.

## Carrying CO₂ and the Fick balance for CO₂

Blood carries CO₂ mostly as bicarbonate, with smaller amounts dissolved and bound to proteins as carbamino compounds. Hemoglobin that has released oxygen binds more H⁺ and CO₂, which is why oxygen unloading in tissue helps CO₂ loading (the Haldane effect), and the lower pH and higher CO₂ shift oxygen binding the other way (the Bohr effect, named in one sentence in the [biochemistry lesson on binding](../../biochemistry/modules/07-binding-equilibria-and-cooperativity.md)). Both are the same coupling seen from two sides.

The Fick principle works for CO₂ as for O₂: V̇_CO₂ = Q̇ × (C_vCO₂ − C_aCO₂). With cardiac output 5 L/min and CO₂ production 200 mL/min the venous–arterial content difference is 200/5 = 40 mL/L. If production rises to 250 mL/min at the same output the difference is 50 mL/L.

## Common mistakes

- Treating the pK′ of 6.1 as evidence that the system buffers poorly at pH 7.4, instead of noting that it is open and that both terms are regulated.
- Reading a normal pH as a normal acid–base state, when two offsetting changes can hide in the ratio.
- Assuming the same pH implies the same disturbance.
- Calling a compensation a cure, or expecting it to restore pH exactly.
- Treating pH as a linear scale: a fall of 0.30 pH units is a doubling of [H⁺], not a 30% rise.
- Reading the anion gap as a measure of pH.

## Worked example

**Problem.** A synthetic person with [HCO₃⁻] = 24 mmol/L and P_CO₂ = 40 mmHg develops a metabolic acid load that lowers bicarbonate to 15 mmol/L, then hyperventilates until P_CO₂ = 30 mmHg. Find the uncompensated pH, the compensated pH and the loop gain.

**Step 1: uncompensated.** The ratio is 15/1.2 = 12.5, so pH = 6.1 + log₁₀ 12.5 = 7.197 and d = 7.401 − 7.197 = 0.204.

**Step 2: compensated.** Dissolved CO₂ falls to 0.03 × 30 = 0.90 mmol/L, the ratio is 15/0.90 = 16.7, and pH = 6.1 + 1.222 = 7.322, so e = 7.401 − 7.322 = 0.079.

**Step 3: gain.** G = d/e − 1 = 0.204/0.079 − 1 = 1.58, and the compensation removed 1 − 0.079/0.204 = 61% of the disturbance.

**Step 4: reading the result.** The remaining 0.079 pH units is the built-in steady-state error of proportional control, not a failure to respond; and the lung's term alone cannot restore bicarbonate.

## Limits of this lesson

All values are synthetic and round. The bicarbonate system is treated as a single plasma compartment; non-bicarbonate buffers (hemoglobin, proteins, phosphate, bone) and the changing CO₂ content of blood are not modelled. The ledger uses one extracellular volume and invented excretion rates, the loop gain is a single-number summary of a nonlinear control, and the anion-gap reference value is a round teaching figure. The lesson explains reasoning about acid–base data and gives no medical advice.
