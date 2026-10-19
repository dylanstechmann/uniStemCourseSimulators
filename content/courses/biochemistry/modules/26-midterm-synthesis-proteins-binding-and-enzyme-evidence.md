# Midterm synthesis: one enzyme preparation from charge to rate (weeks 1–7)

The first seven weeks looked at a protein from several directions: which of its groups carry charge at a given pH, whether it is folded, what it binds and how much, how pure a preparation of it is, and how fast it catalyzes a reaction and how an inhibitor changes that rate. Week 2 also followed amino-acid nitrogen into urea and amino-acid carbon into central metabolism. Each lesson had its own calculation. This reading connects them into one chain of reasoning about a single enzyme preparation, so that the output of one calculation becomes the input of the next, and it prepares for the open midterm review practice. That practice is ungraded and is not a midterm exam. All proteins, compounds and values here are synthetic.

## Learning objectives

By the end of this reading, you should be able to:

1. Carry a folded-protein or active-enzyme amount from a stability or purification calculation into a binding or rate calculation.
2. Recognize when a bound amount is no longer small compared with a total, and switch to the exact mass-balance solution.
3. Match an alternative explanation for a kinetic result to the control measurement that would test it.
4. Classify a statement as a direct observation, an inference under a stated model, or a claim beyond the data.

## The chain the first half built

| Weeks | Question about the protein | Quantity | Relation used in the course | A trap to avoid |
| --- | --- | --- | --- | --- |
| 1–2 | Which groups carry charge at this pH? | Net charge | Acid: −n/(1 + 10^(pKa − pH)); base: +n/(1 + 10^(pH − pKa)) | Reading the sign of the charge as a statement about stability or affinity |
| 2 | Where do amino-acid nitrogen and carbon go? | Urea, phosphate equivalents, carbon skeleton | Two nitrogen atoms per urea; 3 ATP molecules = 4 high-energy phosphate equivalents per urea | Merging the nitrogen ledger with the carbon ledger |
| 3 | What fraction is folded? | f_folded | K_u = exp(−ΔG_unfold/RT); f_folded = 1/(1 + K_u); ΔG_unfold = ΔG_H₂O − m[D] | Treating "more than 99% folded" as "no difference between variants" |
| 4 | How much ligand is bound? | θ or [RL] | θ = [L]/(K_d + [L]) with free ligand; the quadratic when depletion matters | Using total ligand as free ligand when the bound amount is not small |
| 4 | How pure is the preparation? | Specific activity, recovery, fold enrichment | Specific activity = units/mg; fold = final/crude specific activity | Equating enrichment with homogeneity |
| 5–7 | How fast, and how does an inhibitor act? | v₀, Vmax, Km, kcat, K_I | v₀ = Vmax[S]/(Km + [S]); Vmax = kcat[E_active]; α = 1 + [I]/K_I | Fitting reciprocal plots without asking how they weight the noise |

Read down the last column before the review. Most errors in the first half come from one of these six substitutions, not from arithmetic.

## Three habits that recur

### 1. Every fraction comes from one equilibrium ratio

Ionization, folding and binding each reduce to a fraction of the form 1/(1 + ratio). A basic group is protonated with fraction 1/(1 + 10^(pH − pKa)); a two-state protein is folded with fraction 1/(1 + K_u); a site is occupied with fraction [L]/(K_d + [L]) = 1/(1 + K_d/[L]). Writing them in one form makes limits easy to check. When the ratio is 1 the fraction is one half: pH equals pKa, ΔG_unfold is zero at the denaturation midpoint, or free ligand equals K_d. The ratio changes tenfold for one pH unit, for a tenfold change in free ligand, or for 5.71 kJ/mol of unfolding free energy at 25 °C (RT ln 10 = 2.479 × 2.303).

### 2. Totals are not free concentrations when binding is tight

The hyperbola uses free ligand. When the receptor or enzyme concentration is comparable to K_d or larger, binding removes a meaningful share of the ligand and the exact solution is needed:

[RL] = {(R_T + L_T + K_d) − √[(R_T + L_T + K_d)² − 4R_TL_T]}/2.

**Example.** With R_T = L_T = 30 nM and K_d = 3 nM, the sum is 63 nM and the square root is √(3969 − 3600) = 19.21, so [RL] = (63 − 19.21)/2 = 21.9 nM. Free ligand is 30 − 21.9 = 8.1 nM, and the check (30 − 21.9) × 8.1/21.9 ≈ 3.0 nM recovers K_d. The shortcut that treats 30 nM as free predicts θ = 30/33 = 0.909, or 27.3 nM complex, an overestimate of about 25%. The same algebra applies to a tight-binding inhibitor: the familiar α = 1 + [I]/K_I assumes that free inhibitor is close to total inhibitor. A useful check: the bound share of the ligand is about R_T/(K_d + [L]), so depletion is small when the receptor total is well below K_d or well below the ligand total.

### 3. Only the active amount does the work

Vmax = kcat × [active enzyme], not kcat × total protein. Unfolded or inactivated molecules and contaminating proteins add milligrams but no rate. The idea appears in three weeks. Folding gives the active total R_F = f_folded × R_T. Purification compares a pool's specific activity with the value pure active enzyme would show. Kinetics turns a fitted Vmax into kcat only after the active-site concentration is known.

**Example.** A fictional enzyme with kcat = 50 s⁻¹ and 40 kDa per active site: 1 mg is 1 × 10⁻³ g ÷ 40,000 g/mol = 25 nmol of sites, which turn over 25 nmol × 50 s⁻¹ × 60 s/min = 75 μmol/min. Pure active enzyme would therefore show 75 U/mg. A pool at 45 U/mg is at most 60% active enzyme by mass, if no contaminant contributes activity and the assay matches. Conversely, dividing a measured Vmax by total rather than active enzyme underestimates kcat by the inactive fraction.

## Matching alternatives to controls

One observation can have several explanations, and each explanation predicts a different result in a specific control. Suppose a compound lowers apparent Vmax while Km stays within error.

| Explanation | What it predicts | A control that separates it |
| --- | --- | --- |
| Reversible binding that lowers catalytic turnover | Activity returns after the compound is removed | Dilution or dialysis, then a repeat rate |
| Partial unfolding of the enzyme | Fewer folded or active molecules with the compound present | Folded-fraction or active-site measurement with and without the compound |
| Irreversible inactivation | No recovery after removal; loss grows with preincubation time | Removal test plus a preincubation time course |
| Interference with the product signal | The signal changes even without enzyme | A product standard with and without the compound, in a no-enzyme reaction |

The same habit applies to purification. A rising specific activity is evidence of enrichment for the measured activity. It does not show homogeneity, because a contaminant could co-purify or the assay could change. An orthogonal separation, one that uses a property the earlier steps did not use, and a composition check such as a gel, add evidence of a different kind.

Statements about any of these results fall into three levels. Take a purification in which specific activity rises from 3 to 150 U/mg across three steps. "Specific activity rose 50-fold" restates the data, so it is a **direct observation**. "The target was enriched about 50-fold" is an **inference under a model**: it assumes the assay measures only the target and that no activator or inhibitor was removed. "The preparation is pure" or "the enzyme behaves the same way in cells" is a **claim beyond the data**, because nothing measured addresses it.

## Worked integration: from a stability value to an inhibition constant

A fictional enzyme E is assayed at 25 °C in a buffer that contains 1.5 M urea. It has ΔG_H₂O = 20 kJ/mol, m = 10 kJ/mol per M, kcat = 30 s⁻¹ and Km = 6.0 μM. The total enzyme concentration is 20 nM, and only folded enzyme is active.

1. **Folding.** ΔG_unfold = 20 − 10 × 1.5 = 5.0 kJ/mol. K_u = exp(−5.0/2.479) = 0.133, so f_folded = 1/1.133 = 0.883 and the active enzyme is 0.883 × 20 = 17.7 nM.
2. **Vmax.** 30 s⁻¹ × 17.65 nM = 530 nM/s = 31.8 μM/min. Using total enzyme would predict 36.0 μM/min. Read in the other direction, dividing a measured 31.8 μM/min by 20 nM gives an apparent kcat of 26.5 s⁻¹, about 12% low.
3. **Inhibition.** At 4.0 μM, a competitive inhibitor raises the apparent Km from 6.0 to 14.0 μM. Then α = 14.0/6.0 = 2.33 and K_I = 4.0/(2.33 − 1) = 3.0 μM. The simple α expression is safe here because 20 nM enzyme cannot deplete 4.0 μM inhibitor.
4. **A rate.** At 6.0 μM substrate, v₀ = 31.8 × 6.0/(6.0 + 6.0) = 15.9 μM/min without inhibitor, and 31.8 × 6.0/(14.0 + 6.0) = 9.54 μM/min with it.
5. **What this does not show.** The calculation assumes two-state folding, an inactive unfolded state, a competitive mechanism and initial-rate conditions. It says nothing about where the inhibitor binds in the structure, or what it would do in a cell.

Each step uses one lesson's relation, but each also needs the previous step's output. The urea in the buffer changes the Vmax that the kinetics lesson would fit.

## A midterm-review scratch pad

Before answering any cumulative item, write five short lines:

1. The quantity asked for and its units.
2. Whether each concentration is free or total, and whether each enzyme amount is active or total.
3. The relation that applies and the assumption it needs: two-state folding, a single 1:1 site, initial rates, or a stated inhibition mode.
4. A quick check: a half-point, a limit or an order of magnitude.
5. The level of the conclusion: observation, inference under a model, or beyond the data.

## Using the midterm review practice

Open **Practice gradebook** and select **Week 7 midterm review practice (ungraded; not a midterm exam)**. It combines eight new cross-week items with ten items reused from the weekly lessons, so that every week from 1 to 7 appears at least once. The points are formative and do not form a grade. The answer specifications are public in this repository. A separate, inactive midterm review candidate has an unreviewed private key and is not served to learners.

## Limits of this reading

All proteins, compounds and numbers are synthetic. The relations assume two-state folding, independent ionizable groups with fixed pKa values, single 1:1 binding sites and initial-rate kinetics; real proteins can violate any of these. The ATP and phosphate conventions are bookkeeping choices stated in the earlier lessons. This reading gives no laboratory protocol, and it has not been reviewed by a qualified instructor.
