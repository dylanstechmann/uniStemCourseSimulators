# Translation, charging, proofreading and energy

## Separate the information and chemical tasks

The existing protein and enzyme readings develop molecular recognition and catalysis. Translation combines those principles with a directional template and activated chemical substrates. The ribosome reads an mRNA in the 5-prime to 3-prime direction and extends a polypeptide from its amino terminus toward its carboxyl terminus. Codon recognition, attachment of an amino acid to its tRNA and peptide-bond formation are different operations. An appropriate anticodon can deliver an incorrectly charged amino acid; correct codon pairing alone cannot prove correct side-chain assignment.

An aminoacyl-tRNA synthetase selects substrates and couples amino-acid activation to ATP cleavage. In a simplified chemical ledger, amino acid plus ATP forms an enzyme-associated aminoacyl-AMP intermediate and pyrophosphate; transfer to tRNA releases AMP. Subsequent pyrophosphate hydrolysis makes the overall process strongly directed under suitable cellular conditions. ATP-to-AMP charging is conventionally counted as two high-energy phosphate equivalents when regeneration through that hydrolysis ledger is included. It consumes one ATP molecule per charging event, not two ATP molecules.

## The ribosome uses an activated ester

The aminoacyl-tRNA ester carries chemical activation into translation. During elongation, the amino group on the incoming aminoacyl-tRNA attacks the ester-linked peptidyl chain, transferring the chain to the incoming tRNA. Ribosomal RNA contributes to the catalytic center. ATP is not directly cleaved at that peptide-transfer step; charging supplied the activation earlier. GTP-dependent delivery/selection and translocation provide additional kinetic and directional control.

A minimal bookkeeping convention assigns two GTP hydrolyses per elongation addition after the first residue: one for delivery/selection and one for translocation. Initiation, termination, recycling, scanning and quality-control costs depend on the biological system and chosen boundary. We therefore state any overhead separately rather than presenting one universal translation price. A peptide with N residues has N−1 peptide bonds, while N charging events are needed if each residue begins on a separately charged tRNA. A stop codon signals release rather than adding a stop amino acid.

## Derive a complete stipulated cost

For a fictional 40-residue product, assume one successful charging per residue, no rejected substrates or retries, two elongation GTP per addition after the first, and a separately stipulated overhead of four GTP per completed product. Charging consumes 40 ATP molecules converted to AMP, equivalent to 80 high-energy phosphate transfers under the declared regeneration convention. Elongation consumes 78 GTP and overhead adds four, giving 82 GTP molecules. Total high-energy equivalents are 80+78+4=162, for 39 peptide bonds.

A molecule count of 40 ATP plus 82 GTP is not the same number as 162 phosphate equivalents. Report both with their definitions. A different overhead, failed initiation, stalled chains or proofreading cycle would change the cost. The model does not include amino-acid biosynthesis or all nucleotide-regeneration and maintenance pathways, so it is not a whole-cell energy budget.

## Recognition and editing as conditional filters

Some synthetases use editing to reject substrates that are difficult to distinguish at activation alone. Think of a first selection followed by an editing step as two conditional filters. The resulting error fraction depends on the survival of correct and incorrect inputs, not simply the product of two percentages labelled “accuracy.” This mathematical illustration does not assert independence of real molecular events or universal rate constants.

Stipulate input fractions 0.9 correct and 0.1 incorrect. At a first filter, correct inputs survive with probability 0.8 and incorrect with 0.01. At a second conditional filter, correct survivors survive with 0.9 and incorrect survivors with 0.1. Correct output is 0.9×0.8×0.9=0.648 per input, incorrect output is 0.1×0.01×0.1=0.0001, and total accepted output is 0.6481. The incorrect fraction among accepted outputs is 1/6481, approximately 0.00015430. Dividing the incorrect output by all original attempts would answer a different question.

Without the second filter, the incorrect fraction among accepted outputs is 0.001/(0.720+0.001)=1/721. The improvement is close to, but not exactly, a factor of ten because the correct-survivor denominator also changes. Editing can consume substrates and energy, and a failed event may be retried. More selective output is not automatically free or faster output. Directly transferring these toy probabilities to an enzyme requires additional kinetic evidence.

## Evidence and transfer tasks

For a separate 10-residue worked comparison with the same four-GTP overhead, charging contributes 20 equivalents, elongation 18 and overhead four, totaling 42. It has nine peptide bonds. Derive the general N expression and explain the overhead's effect on short versus long products. Then reproduce the 40-residue rehearsal and conditional-filter fractions without rounding intermediate outputs.

Draw a causal diagram with possible errors at charging, codon recognition, translocation and release. Explain which measurements would distinguish an incorrect amino acid on the correct anticodon from a codon-mispairing event, and why total protein accumulation also depends on degradation. Link back to Cell Biology for gene-expression and turnover evidence rather than silently duplicating its full sequence. Retain diagrams, calculations and a limitations ledger locally. MIT OCW 7.05 Spring 2020 lectures 17–18 guide the link-only scope comparison. Every exercise is original and AI-assisted; no source sequence, figure, problem or experiment is imported. Detailed initiation systems, ribosome structures and real error-rate measurements remain selective or deferred.
