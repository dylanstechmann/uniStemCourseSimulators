# Alternating access and coupled transport cycles

## A membrane protein changes a kinetic path

A concentration gradient is not a transport mechanism. The existing free-energy and mitochondrial readings provide the energetic tools; this companion connects them to channels, alternating-access carriers and energy-coupled pumps. A channel supplies a selective conductive path whose open probability and driving force affect current. An alternating-access carrier exposes binding sites to opposite sides at different stages rather than leaving a continuously open pore. A pump couples a transport cycle to an energy-releasing process. These descriptions distinguish mechanisms without implying that every real protein fits one two-state diagram.

Binding, accessibility and direction must all appear in a carrier model. A substrate can bind on one side, become occluded, and be released on the other after a conformational change. Return of the empty carrier completes a simple uniport cycle. A coupled transporter instead makes occupancy of another solute part of the permitted cycle. Preventing an uncoupled return step can enforce a stoichiometric relationship between transported species. A mutation that opens a leak pathway can break that relationship even if binding remains measurable.

## Reversible flux and saturation

Use the stipulated symmetric reversible-carrier law J=V(C_out−C_in)/(K+C_out+C_in), with compatible normalized concentrations and positive V,K. It captures a zero at equal concentrations, a sign reversal with the gradient, and finite turnover at large concentrations. It is a teaching law, not a complete derivation for every transporter or a model of ion electrical energy. Define outward-to-inward flux as positive.

For V=6, K=1, C_out=4 and C_in=1, J=3. Doubling both concentrations to 8 and 2 preserves their ratio but gives J=36/11, approximately 3.27273, rather than doubling the flux. Turnover and occupancy matter as well as the concentration ratio. Equal concentrations give zero net flux in this symmetric neutral-solute model even though molecules can still exchange in both directions. A measured zero net rate does not establish that the protein is absent or every microscopic movement stopped.

## Close a coupled free-energy cycle

For transfer from outside to inside, the dimensionless electrochemical free-energy change of an ion with charge z is DeltaG/RT=ln(C_in/C_out)+zF(psi_in−psi_out)/RT. The potential difference is explicitly inside minus outside; do not transfer the earlier mitochondrial positive-gradient-magnitude convention without translating signs. For a neutral solute, the electrical term is zero.

Stipulate a monovalent positive driving ion with outside/inside concentration ratio 10 and FDeltaPsi/RT=−ln10. Inward ion transfer then has DeltaG_ion/RT=−2ln10. Moving a neutral substrate inward with ratio R=S_in/S_out costs ln R. A tightly coupled cycle importing n ions per substrate has total DeltaG_cycle/RT=ln R−2n ln10. Its ideal reversible stall ratio is R=10^(2n). At stall the thermodynamic drive is zero; this upper ratio is not a prediction of a useful finite transport rate.

For two ions and substrate ratio 1,000, the cycle free energy is −ln10, so the specified inward cycle is energetically allowed. Its ideal stall ratio is 10,000. A one-ion cycle would stall at 100 and cannot drive that same 1,000-fold ratio under these gradients. An uncoupled neutral uniporter also cannot maintain uphill accumulation merely because its binding affinity is high.

## Pumps and dissipative paths

Now reverse the ion movement: exporting each ion under the same gradients costs +2ln10 RT. Suppose ATP hydrolysis supplies a stipulated −12RT per pump cycle. Exporting two ions costs 4ln10 RT, leaving total cycle free energy 4ln10−12<0. Exporting three would cost 6ln10>12 and is unfavorable under the same conditions. The maximum integer count with strictly negative cycle free energy is therefore two in this model. Actual pump stoichiometry is a structural/mechanistic property, not freely chosen after calculating an energy ratio.

A leak dissipates the gradient without performing the intended coupled work. If maintaining a gradient requires a separate pump, account for that pump's energy as well; secondary transport does not create free energy. Similarly, a concentration endpoint alone does not prove a particular coupling count. Measure flux relationships and perturbations that distinguish coupled cycles from independent pathways, while preserving membrane integrity and compatible concentration scales.

## Worked comparison and evidence tasks

For a separate one-ion example with the same driving-ion gradient and neutral ratio 10, total free energy is −ln10 RT. Compare it with the two-ion rehearsal at ratio 1,000: both have the same cycle free energy but different transported amounts and stall ratios. Equal energetic drive does not establish identical kinetics, protein abundance or mechanism.

Draw both alternating-access cycles, mark which return steps are permitted, and write signed energy terms beside each transported species. Recompute the carrier-law fluxes, ideal stall ratios and pump limits. Propose one observation that separates a changed carrier abundance from an added leak, and explain what a binding measurement alone cannot identify. Retain the full derivation and diagram locally. MIT OCW 7.05 Spring 2020 lecture 13 is a link-only scope comparator; all equations, parameters and examples are original AI-assisted constructions. Broader channel gating, detailed transporter structures and physiological regulation remain selective, and no real transport measurement or qualified review is implied.
