# Fatty-acid beta-oxidation: acetyl-CoA and reducing equivalents

Long-chain fatty acids can supply acetyl-CoA and reduced electron carriers to mitochondrial metabolism. Before estimating energy yield, keep three steps distinct: activation of the fatty acid, transport of long-chain acyl groups into the mitochondrial matrix, and the repeated beta-oxidation reactions. The resulting acetyl-CoA then enters the citric acid cycle, while NADH and FADH2 can donate electrons to oxidative phosphorylation. This lesson uses saturated, even-chain fatty acids for its main accounting model; unsaturated, odd-chain, and peroxisomal routes require additional steps.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate beta-oxidation cycle count, acetyl-CoA and reducing-equivalent outputs for an even-chain saturated fatty acyl-CoA, and account for activation cost when starting from a free fatty acid.
2. Integrate beta-oxidation with the citric acid cycle and electron transport using stated P/O assumptions, and explain carnitine transport and its regulation.

## Get the fatty acyl chain to the matrix

A free fatty acid is first converted to fatty acyl-CoA. The synthetase reaction uses ATP to AMP and pyrophosphate; because ATP is cleaved to AMP, activation costs **two ATP equivalents**. Long-chain acyl-CoA does not cross the inner mitochondrial membrane directly. The carnitine shuttle transfers its acyl group across: CPT1 forms acylcarnitine at the outer membrane, a translocase moves it across the inner membrane, and CPT2 regenerates acyl-CoA in the matrix. Carnitine returns to the cytosolic side. The shuttle transports the acyl group; it does not replace beta-oxidation or directly make ATP.

Malonyl-CoA, an intermediate associated with fatty-acid synthesis, inhibits CPT1 in the simplified fed-state control model. This reduces entry of long-chain acyl groups while synthesis is favored. When malonyl-CoA falls, transport into the matrix can increase if fatty-acid supply and other conditions support it. This is one regulatory gate, not a complete model of whole-body fuel choice.

## The beta-oxidation spiral shortens the chain by two carbons

For a saturated acyl-CoA in the matrix, each spiral turn has four reaction types: oxidation by an FAD-linked dehydrogenase, hydration, oxidation by an NAD+-linked dehydrogenase, and thiolysis. Thiolysis releases a two-carbon acetyl-CoA and leaves a fatty acyl-CoA shortened by two carbons, ready for another turn. In the usual bookkeeping, each turn yields one FADH2 and one NADH; the final cleavage of an even chain releases two acetyl-CoA units from the remaining four-carbon fragment.

For a saturated even-chain fatty acyl-CoA with **n** carbons, the number of turns is *n/2 − 1*, and the total acetyl-CoA is *n/2*. Palmitoyl-CoA (C16) therefore undergoes 7 turns and yields 8 acetyl-CoA, 7 NADH and 7 FADH2. Starting from free palmitate adds the 2 ATP-equivalent activation cost. The β-oxidation carriers and the acetyl-CoA products are separate ledgers; oxidation of the acetyl-CoA in the citric acid cycle makes additional carriers and GTP.

## Estimate ATP only after stating the convention

The carriers can feed the respiratory chain, but ATP yield depends on coupling, transport costs and the assumed P/O ratios. For one explicit estimate, assume P/O = 2.5 ATP per mitochondrial NADH and 1.5 ATP per FADH2; assume each acetyl-CoA yields 3 NADH, 1 FADH2 and 1 GTP in the citric acid cycle; count 1 GTP as 1 ATP equivalent; and subtract 2 ATP equivalents for activation from free palmitate. The complete theoretical ledger is then:

- NADH: 7 from beta-oxidation + 8 × 3 from the citric acid cycle = 31 mol.
- FADH2: 7 from beta-oxidation + 8 × 1 from the cycle = 15 mol.
- GTP: 8 mol from the cycle.
- ATP equivalents: (31 × 2.5) + (15 × 1.5) + 8 − 2 = **106 mol ATP equivalents per mol palmitate**.

This is an idealized accounting result under the stated convention, not a fixed biological yield. Different P/O estimates, proton leak, transport, incomplete oxidation and cellular demand change realized ATP capture.

## Worked example

**Problem.** How many beta-oxidation turns and acetyl-CoA molecules come from 3 mol palmitoyl-CoA?

**Step 1: count carbons per molecule.** C16 gives 16/2 − 1 = 7 turns and 16/2 = 8 acetyl-CoA.

**Step 2: scale by amount.** Three mol palmitoyl-CoA gives 21 mol turns and 24 mol acetyl-CoA. This starts from activated palmitoyl-CoA, so the 2 ATP-equivalent cost of activating free palmitate is outside this particular boundary.

## Common mistakes

- Counting one cycle per acetyl-CoA; an even-chain saturated fatty acid yields one more acetyl-CoA than the number of turns.
- Forgetting that activation of a free fatty acid to acyl-CoA costs two ATP equivalents, while the carnitine shuttle itself is a transport step.
- Counting the beta-oxidation NADH and FADH2 but omitting the additional carriers made when acetyl-CoA is oxidized in the citric acid cycle.
- Reporting an ATP yield without specifying P/O assumptions and activation boundary.
- Assuming every fatty acid follows the exact saturated even-chain calculation; unsaturation, odd-chain termination and peroxisomal oxidation change the bookkeeping.

## Practice and references

The accompanying questions are open formative checks with unlimited retries; responses are not collected or graded. See the link-only [KEGG fatty acid degradation map](https://www.kegg.jp/entry/map00071), [Reactome mitochondrial fatty-acid beta-oxidation pathway](https://reactome.org/content/detail/R-HSA-77289), and a [PubMed review of lipid metabolism](https://pubmed.ncbi.nlm.nih.gov/34470787/). No pathway diagram, source text or figure is reproduced here.
