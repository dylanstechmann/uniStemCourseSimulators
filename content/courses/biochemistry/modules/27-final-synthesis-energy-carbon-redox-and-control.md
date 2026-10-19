# Final synthesis: ledgers for energy, carbon, redox and control (weeks 8–14)

The second half of the course followed metabolism as a set of linked accounts. An ATP ledger counted energy under stated conventions. A carbon ledger followed which atoms can become glucose, fat or carbon dioxide. A redox ledger tracked NADH, FADH₂ and NADPH, and a nitrogen ledger, begun in week 2, sent amino nitrogen to urea. Around these ledgers sat the questions of control: which signal changes which enzyme, how fast, and how a measured pool, label or rate can tell a flux change from a pool change. This reading puts the ledgers side by side and ends with one fasting-liver calculation that needs all of them. It prepares for the open final review practice, which is cumulative, ungraded and not a final exam. All cells, compounds and values are synthetic.

## Learning objectives

By the end of this reading, you should be able to:

1. Build ATP, carbon, redox and nitrogen ledgers with stated conventions, and keep each ledger's boundary explicit.
2. Separate pool sizes, labeled fractions and fluxes, and say what extra information a flux claim needs.
3. Predict the direction of hepatic metabolism from signals that act on different time scales.
4. Distinguish uncoupling, respiratory-chain inhibition and a primary glycolytic defect from oxygen, lactate and glucose data.

## The ATP ledger and its conventions

Every ATP total in this course depends on a convention, and a total without its convention cannot be compared with another.

| Quantity | Value used in this course | What the value assumes |
| --- | --- | --- |
| Mitochondrial NADH | 2.5 ATP | About 10 H⁺ pumped per NADH and about 4 H⁺ per ATP made and exported |
| FADH₂ (via ubiquinone) | 1.5 ATP | Electrons enter after complex I, so fewer protons are pumped |
| One acetyl-CoA through the citric acid cycle | 10 ATP equivalents | 3 NADH + 1 FADH₂ + 1 GTP, with GTP counted as ATP |
| Glucose, complete oxidation | 32 ATP | Cytosolic NADH enters by the malate–aspartate shuttle; the glycerol-phosphate shuttle gives 30 |
| Free fatty acid activation | 2 ATP equivalents | ATP → AMP + pyrophosphate, and the pyrophosphate is hydrolyzed |
| Proton leak | Removes oxidative ATP only | Substrate-level ATP is unaffected |

Under these values free palmitate yields 106 ATP equivalents per mole. Acetoacetate yields 19 and D-β-hydroxybutyrate 21.5 when extrahepatic mitochondria oxidize them; those two values already subtract the GTP-forming step that SCOT bypasses. Dividing by the oxygen each fuel consumes gives a yield per O₂: glucose gives 32/6 = 5.33. Fuels that send more electrons through FADH₂ give less per O₂ under this convention. That ranking is bookkeeping, not a measured cellular efficiency.

## The carbon ledger: what can become what

- **Glucose to fat is open.** Glycolysis gives two pyruvate per glucose; pyruvate dehydrogenase releases one CO₂ and makes acetyl-CoA, which leaves the mitochondrion as citrate for fatty-acid synthesis.
- **Even-chain fat to net glucose is closed in mammals.** Pyruvate dehydrogenase is effectively one-way, and each acetyl-CoA that enters the cycle brings two carbons in while two leave as CO₂, so no net oxaloacetate is made. Glycerol from triacylglycerol is a separate glucose precursor.
- **Amino-acid skeletons split.** Skeletons that give pyruvate or cycle intermediates can support net glucose; leucine and lysine give only acetyl-CoA or acetoacetate.
- **Label is not net conversion.** Label from a ketogenic carbon source can reach glucose by exchange through cycle intermediates without any net glucose being made from it.

## The redox and nitrogen ledgers

**NADH** carries electrons from catabolism to the respiratory chain. When the chain is blocked, lactate dehydrogenase becomes the outlet that regenerates NAD⁺ for glycolysis. If that enzyme is near equilibrium at constant pH, the lactate/pyruvate ratio tracks the cytosolic NADH/NAD⁺ ratio.

**NADPH** supplies reducing power for synthesis: 14 per palmitate, plus cholesterol synthesis and antioxidant systems. The oxidative pentose phosphate branch makes 2 NADPH and 1 CO₂ per glucose 6-phosphate, and malic enzyme is another source. When a cell needs more ribose than NADPH, the reversible nonoxidative reactions rearrange glycolytic intermediates into pentose phosphates. When it needs more NADPH than ribose, the same reactions return pentose carbon to glycolysis.

**Nitrogen** leaves as urea: two nitrogen atoms per urea, the second from aspartate, at 3 ATP molecules or 4 high-energy phosphate equivalents per urea. Making one glucose from two alanine therefore costs the gluconeogenic inputs from pyruvate (4 ATP, 2 GTP and 2 NADH) plus 4 phosphate equivalents to dispose of the two nitrogen atoms. A carbon ledger alone would miss that second cost.

## Pools, labels and fluxes

A **pool size** is an amount at one time. A **labeled fraction** is the share of a pool that carries an isotope at one time. A **flux** is a rate through a step. None of the three can stand in for another.

- A constant ATP pool can hide a large ATP turnover, because synthesis and use change together.
- A rising labeled fraction can reflect tracer spreading through pools; converting it to a flux needs precursor labeling over time, pool sizes and a fitted model.
- In a crossover plot, a step whose substrate ratio rises above 1 while its product ratio falls below 1 is a candidate control site. The pattern locates a change; it does not measure the new flux.
- A flux control coefficient states the share of control one enzyme holds under one condition. With C = 0.40, a 10% rise in that enzyme predicts about a 4% rise in flux. The coefficients sum to 1, and the linear estimate holds only for small changes.

## Signals and their time scales

| Layer | Example from the course | Typical time scale |
| --- | --- | --- |
| Substrate and product levels | Keeping a product low lets a step with positive ΔG°′ run forward | Immediate |
| Allosteric effectors | AMP and fructose 2,6-bisphosphate on phosphofructokinase-1; malonyl-CoA on CPT1 | Seconds |
| Covalent modification | Hormone-triggered phosphorylation of the PFK-2/FBPase-2 enzyme, glycogen phosphorylase and acetyl-CoA carboxylase | Seconds to minutes |
| Enzyme amount | SREBP2-driven LDL-receptor and HMG-CoA reductase expression; induced enzymes | Hours to days |

A change in enzyme amount approaches its new level with first-order turnover. An enzyme with a 10-hour half-life gets halfway in 10 hours and 87.5% of the way in 30 hours, however large the change.

In a simplified fasting liver, the layers act together. Glucagon signaling lowers fructose 2,6-bisphosphate, which relieves inhibition of fructose 1,6-bisphosphatase and favors gluconeogenesis. Phosphorylated acetyl-CoA carboxylase makes less malonyl-CoA, so CPT1 admits more long-chain acyl groups for beta-oxidation. Acetyl-CoA then accumulates while oxaloacetate is drawn into gluconeogenesis, so more acetyl-CoA is directed to ketone bodies, which the liver exports.

## Telling three energy failures apart

Low ATP can come from several causes. The perturbation lesson compared two of them; an uncoupler adds a third pattern.

| Measurement | Uncoupler | Respiratory-chain inhibitor | Primary glycolytic defect |
| --- | --- | --- | --- |
| Oxygen use | Rises, because the gradient no longer restrains electron flow | Falls sharply | Stays near normal or falls a little if other fuels supply the mitochondria |
| ATP made per O₂ | Falls | Little oxygen is used | About unchanged for the fuels still oxidized |
| Lactate | May rise as glycolysis compensates | Rises, as an outlet for NADH | Falls |
| Glucose uptake | May rise | Rises | Falls or is limited by the defect |

No single row is decisive in every case. Oxygen use separates the first two columns most directly, and lactate separates the last two. A second, independent measurement is still needed before naming a mechanism, because hypoxia, fuel switching and transport changes can mimic parts of each pattern.

## Worked integration: a fasting hepatocyte ledger

A synthetic fasting hepatocyte model takes up 1.0 μmol palmitate. It oxidizes all of it by beta-oxidation, converts 6 of the resulting acetyl-CoA to acetoacetate for export and oxidizes the other 2 in the citric acid cycle. Use the course convention.

1. **Beta-oxidation.** Palmitate gives 7 turns and 8 acetyl-CoA, with 7 NADH and 7 FADH₂: 7 × 2.5 + 7 × 1.5 = 28 ATP equivalents, minus 2 for activation, so 26.
2. **The citric acid cycle.** 2 acetyl-CoA × 10 = 20 ATP equivalents. The liver's total is 26 + 20 = 46 μmol ATP equivalents.
3. **Ketone export.** 6 acetyl-CoA form 3.0 μmol acetoacetate, which uses no ATP in this convention. Extrahepatic mitochondria can recover 3.0 × 19 = 57 ATP equivalents from it.
4. **Closing the ledger.** 46 + 57 = 103, three fewer than the 106 from complete oxidation in one place. The difference is the one GTP-forming step per acetoacetate that SCOT bypasses. The ledger closes only because the convention was stated.
5. **What the liver's ATP can buy.** Gluconeogenesis from lactate costs 6 ATP equivalents per glucose, and oxidizing the lactate supplies the NADH it needs. If all 46 ATP equivalents went to that pathway, they would cover at most 46/6 ≈ 7.7 μmol glucose. That is a ceiling, not a prediction, because the cell has other ATP demands.

The calculation links four lessons: fatty-acid oxidation, ketone bodies, gluconeogenesis and mitochondrial bioenergetics. It also shows why fat oxidation can pay for glucose synthesis even though fat carbon cannot become net glucose.

## A final-review scratch pad

1. State the ledger: ATP, carbon, redox or nitrogen, and the convention it uses.
2. Draw the boundary: one cell type, one compartment, one interval.
3. Say whether each number is a pool, a labeled fraction or a rate.
4. For a regulatory question, name the signal, the enzyme it acts on, the direction and the time scale.
5. For a perturbation, list two explanations and the measurement on which they differ.

## Using the final review practice

Open **Practice gradebook** and select **Week 14 cumulative final review practice (ungraded; not a final exam)**. It combines seven new cross-week items with earlier lesson items from both halves of the course, because the final candidate it rehearses is cumulative. Before starting, reread the midterm synthesis for weeks 1–7. The points are formative and do not form a grade. The answer specifications are public in this repository. A separate, inactive final review candidate has an unreviewed private key and is not served to learners.

## Limits of this reading

All cells, compounds and values are synthetic. ATP equivalents, P/O values and shuttle choices are conventions, and measured yields in cells differ and vary. The regulatory summary is simplified: it omits other hormones, other tissues and the many enzymes not taught here. Nothing here is dietary, medical or treatment advice, and this reading has not been reviewed by a qualified instructor.
