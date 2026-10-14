# Bioenergetics and central carbon metabolism

This reading is a map of carbon, reducing equivalents and ATP through central metabolism. It establishes what each ledger describes; the quantitative thermodynamics and mitochondrial ATP accounting are developed in the dedicated [free-energy and redox](06-free-energy-coupling-and-redox.md) and [mitochondrial bioenergetics](11-mitochondrial-bioenergetics-and-atp-yield.md) lessons. The [glycolysis](10-glycolysis-energy-charge-and-amp-signal.md) and [citric-acid-cycle](15-citric-acid-cycle-carbon-and-redox.md) lessons develop those pathways in detail.

## Follow carbon and direct ATP

In glycolysis, one six-carbon glucose becomes two three-carbon pyruvate molecules. The net yield is two ATP and two NADH per glucose, after subtracting the ATP invested. Five moles of glucose therefore yield ten moles of ATP directly from glycolysis; this count excludes later oxidation and oxidative phosphorylation.

Pyruvate can be oxidized to acetyl-CoA, releasing carbon dioxide and transferring electrons to NADH. The citric-acid cycle further oxidizes acetyl-derived carbon and generates reduced cofactors. Carbon atoms mix with pathway pools, so the carbon released as CO₂ in one turn need not be the carbon that entered in that turn. In oxygen-limited conditions, fermentation can regenerate NAD⁺ from NADH so glycolysis can continue; fermentation does not add the ATP made by oxidative phosphorylation.

## Keep the ledgers separate

An atom balance tracks where carbon goes. A redox balance tracks oxidation and the acceptors that receive electrons. NADH and FADH₂ carry reducing equivalents; they are not ATP. Their oxidation can support ATP synthesis when electron transfer is coupled to a proton gradient and ATP synthase. The [free-energy lesson](06-free-energy-coupling-and-redox.md) derives reaction direction, coupling and redox-energy changes; the [mitochondrial lesson](11-mitochondrial-bioenergetics-and-atp-yield.md) develops proton-motive force, leak and ATP-yield conventions. Oxygen use reports terminal electron transfer under the stated conditions, not ATP production by itself.

## ATP pool change is not turnover

A synthetic pool ledger compares rates of ATP appearance and use. If synthesis and utilization are each 120 µmol/min, the net ATP-pool change is zero even though both rates are nonzero. If synthesis is 146 µmol/min and utilization is 134 µmol/min, the net amount increases by 12 µmol/min. This is an amount-per-time calculation; without compartment volume it gives no concentration change and does not identify the pathway carrying ATP flux. A stable amount is compatible with substantial simultaneous synthesis and consumption.

## Check the model boundary

Label each quantity before calculating: carbon amount, electron carrier, ATP amount, oxygen use or pathway rate. Distinguish direct glycolytic ATP from ATP estimated from oxidative phosphorylation, and state the shuttle and coupling assumptions for a whole-pathway yield. With an uncoupler, proton return bypasses ATP synthase, so ATP produced per oxygen falls even if electron flow and oxygen use continue; the detailed prediction belongs to the [mitochondrial lesson](11-mitochondrial-bioenergetics-and-atp-yield.md). The public practice items preserve the direct net yield of 2 ATP per glucose, the qualitative uncoupling prediction, and the distinction between pool change and turnover. These are formative bookkeeping models, not measurements of a cell.

## Common mistakes

- Counting ATP consumed during glycolysis instead of reporting its net direct yield.
- Treating NADH as ATP rather than as an electron carrier.
- Assuming oxygen consumption is a direct ATP meter.
- Treating a stable ATP amount as zero ATP turnover, or inferring pathway flux from a pool-change rate.
