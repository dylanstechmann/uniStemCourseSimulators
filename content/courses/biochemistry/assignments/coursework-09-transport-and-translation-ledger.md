# Assignment 9: transport and translation ledger

## Couple a mechanism to an accounting boundary

This bridge report follows the course's eight existing homework packets and addresses the new transport and translation foundations. Use a fictional biochemical system with independently stipulated gradients and energy costs. The task is to connect a protein-mediated cycle to its chemical ledger, not to infer a real transporter, optimize a biological construct or duplicate the earlier enzyme-fitting assignment.

Prepare alternating-access and translation diagrams, signed energy equations, an integer feasibility proof and a conditional-selection table. Retain all work locally. Selected browser fields provide formative feedback; diagrams, code, full reports and biological interpretations are not automatically graded. Every value and probability is synthetic, and no experimental procedure or sequence design is requested.

## Part A: a distinct coupled transporter

For a positive monovalent driving ion, stipulate outside/inside concentration ratio four and F(psi_in−psi_out)/RT=−ln4. Inward ion transfer therefore releases 2ln4 RT. A tightly coupled transporter moves two such ions inward with each neutral substrate. Derive total cycle free energy DeltaG/RT=ln R−4ln4 for substrate accumulation ratio R=S_in/S_out.

At R=64 the cycle free energy is −ln4 RT, and the ideal reversible stall ratio is 256. Check both results directly from the separate chemical and electrical ion terms. Explain why stall is a zero-driving-force boundary rather than a prediction of useful finite flux. Compare with a neutral uniporter under the same substrate ratio and show why high binding affinity alone does not supply the missing uphill free energy.

For a separate pump that exports the same ion, stipulate ATP hydrolysis free energy −10RT per cycle. Find the largest integer export count that leaves a strictly negative total cycle free energy. Three ions cost 6ln4 RT, leaving 6ln4−10<0; four cost 8ln4>10. Therefore three is the mathematical maximum under this exercise boundary. A real pump's stoichiometry is a mechanistic property, not a knob chosen from an energy quotient.

## Part B: reversible kinetics is another constraint

Use the separate stipulated carrier law J=V(C_out−C_in)/(K+C_out+C_in), with V=8,K=2,C_out=6,C_in=2. Calculate J=3.2. Double both concentrations and calculate the new flux, preserving the same concentration ratio. Explain why the change is less than twofold and why this neutral symmetric law should not be silently substituted for the electrochemically coupled transporter above.

Propose an observation that distinguishes changed transporter abundance from a leak pathway, and name an assumption needed to interpret it. A concentration endpoint, binding curve and net transport rate measure different aspects of a cycle. More than one mechanism can match one of them.

## Part C: charge and translate a distinct product

For a fictional 60-residue product, stipulate one successful charging per residue, two elongation GTP for every addition after the first and six overhead GTP per complete product. Charging consumes 60 ATP-to-AMP events, equivalent to 120 high-energy transfers under the declared pyrophosphate-regeneration convention. Elongation costs 118 GTP, overhead adds six, and the total is 244 high-energy equivalents for 59 peptide bonds.

Report ATP molecules, GTP molecules, peptide bonds and phosphate equivalents as different columns. Explain why ATP is not directly hydrolyzed by the peptide-transfer step even though translation's full ledger requires ATP. Add a hypothetical discarded charged intermediate and state how it would alter the boundary, rather than assuming the no-retry arithmetic remains universal.

## Part D: conditional error selection

Use a distinct two-filter model: incoming incorrect fraction 0.02 and correct 0.98; first-filter survival is 0.1 for incorrect and 0.9 for correct; second conditional survival is 0.01 for incorrect and 0.95 for correct. Correct accepted output is 0.8379 per attempt and incorrect output is 0.00002. Calculate total acceptance 0.83792 and the incorrect fraction among accepted outputs, 1/41896. Contrast it with incorrect output divided by all attempts.

Explain why these conditional fractions cannot identify actual enzyme kinetic rates, and why a correct anticodon can still carry an incorrectly charged amino acid. A complete local report closes both the chemical cycle and the measurement denominator without merging their separate assumptions. Continuous checkpoints request three significant figures; integer counts are exact. MIT OCW 7.05 Spring 2020 transport/translation topics guide scope; all tasks are original and AI-assisted with no imported problems or data. Qualified review and measured workload remain open.

Include one explicit failed alternative: a pump cycle with an unfavorable signed energy sum, and a selection denominator that counts rejected attempts as accepted product.
