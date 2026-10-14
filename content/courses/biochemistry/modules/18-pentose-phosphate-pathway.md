# The pentose phosphate pathway: NADPH, ribose and carbon exchange

Glucose 6-phosphate sits at a branch point. It can continue through glycolysis, enter glycogen storage, or pass through the pentose phosphate pathway (PPP). The PPP supplies cytosolic NADPH for reductive reactions and ribose 5-phosphate for nucleotide synthesis, while returning some carbon to glycolysis. It is not a direct ATP-producing pathway. Following both its redox and carbon ledgers helps explain how cells match pathway flux to biosynthetic and redox demand.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate oxidative-branch NADPH and carbon dioxide outputs from glucose 6-phosphate and distinguish NADPH production from ATP yield.
2. Explain how reversible nonoxidative reactions connect pentose needs to glycolytic carbon and how NADP availability relates to oxidative-branch flux.
3. Calculate a labeled-ribose fraction from a synthetic isotopomer distribution and explain why labeling alone does not quantify pathway flux.

## Oxidative branch: capture reducing power and release one carbon

In the oxidative branch, glucose 6-phosphate dehydrogenase (G6PD) oxidizes glucose 6-phosphate and reduces NADP+ to NADPH. A lactonase opens the product ring, then 6-phosphogluconate dehydrogenase performs a second oxidation and releases CO2, yielding ribulose 5-phosphate. The net bookkeeping per glucose 6-phosphate is **2 NADPH, 1 CO2 and 1 ribulose 5-phosphate**. The six-carbon sugar becomes a five-carbon sugar plus carbon dioxide.

NADPH is a reducing currency for biosynthesis and cellular redox maintenance; NADH commonly transfers electrons toward respiratory ATP synthesis. They are not interchangeable labels. The oxidative PPP itself does not directly make ATP. It diverts glucose 6-phosphate away from glycolysis to support NADPH and pentose needs, and its carbon may later return to glycolytic intermediates.

G6PD requires NADP+ as a substrate. When the NADPH/NADP+ balance indicates a high supply of reducing equivalents, product feedback and substrate availability tend to limit further oxidative flux. When NADPH is used and NADP+ becomes available, the oxidative branch can run faster if glucose 6-phosphate is available. This is a useful control model, not a complete predictor of flux: substrate supply, enzyme amount, other reactions and compartment also matter.

## Nonoxidative branch: rearrange sugars without changing total carbon

Ribulose 5-phosphate can be isomerized to ribose 5-phosphate for nucleotide synthesis or epimerized to xylulose 5-phosphate. Reversible transketolase reactions transfer two-carbon units, and transaldolase transfers a three-carbon unit. In the common net accounting, **3 pentose phosphates (15 carbons) can form 2 fructose 6-phosphate plus 1 glyceraldehyde 3-phosphate (also 15 carbons)**. These products can re-enter glycolysis or related pathways.

The two branches can meet different needs. If a cell needs ribose for nucleotides more than NADPH, glycolytic intermediates can be rearranged through the nonoxidative reactions toward ribose 5-phosphate without requiring the oxidative decarboxylation for every pentose. If NADPH demand is high relative to ribose demand, pentose carbons can be rearranged into glycolytic intermediates and, depending on the cell's network, recycled toward glucose 6-phosphate. That recycling can permit additional NADPH production, but the complete carbon and energy cost depends on the routes used to regenerate the starting hexose phosphate.

## Worked example

**Problem.** A synthetic preparation sends 6 mol of glucose 6-phosphate through one pass of the oxidative branch. What amounts of NADPH, CO2 and ribulose 5-phosphate are produced?

**Step 1: use the per-molecule outputs.** Each mol of glucose 6-phosphate gives 2 mol NADPH, 1 mol CO2 and 1 mol ribulose 5-phosphate.

**Step 2: scale each ledger by 6.** The preparation produces **12 mol NADPH, 6 mol CO2 and 6 mol ribulose 5-phosphate**. No ATP is included as a direct product. The NADPH count describes reducing equivalents; it does not by itself reveal how much glucose carbon will later re-enter glycolysis.

## Reading a carbon-tracer pattern

Stable-isotope tracing follows labeled atoms from a supplied nutrient into measured metabolites. In mass-isotopomer notation, M+0 contains no tracer-derived heavy-carbon increment, M+1 contains one 13C atom above the unlabeled mass, and M+2 contains two. These labels describe how many heavy carbons a molecule contains, not which positions carry them or how quickly the pool turns over.

**Synthetic example.** Cells receive a mixture containing [1,2-13C2]glucose. A teaching dataset reports ribose 5-phosphate as M+0 = 40%, M+1 = 45% and M+2 = 15%. The fraction with at least one labeled carbon is **45% + 15% = 60%**. This arithmetic describes the measured distribution in the example; it is not an observed biological result.

The label pattern can support the claim that carbon from the labeled glucose reached ribose 5-phosphate. It cannot, by itself, tell how much ribose came through each branch or give a PPP flux. The oxidative branch removes glucose carbon 1 as CO2, while nonoxidative transketolase and transaldolase reactions rearrange labeled carbon among sugar phosphates. The resulting isotopomers depend on atom positions, substrate enrichment, unlabeled inputs, pathway exchange and sampling conditions. A quantitative flux estimate requires a suitable atom-transition/network model fitted to multiple measurements and an uncertainty analysis.

Primary studies illustrate both the potential and the limits. Lee and colleagues used [1,2-13C2]glucose with ribose and lactate mass-isotopomer analysis to estimate pentose-cycle and relative transketolase/transaldolase activity in their modeled experimental system. Metallo and colleagues found that tracer choice changed the precision of mammalian-cell flux estimates, with [1,2-13C2]glucose performing well for their tumor-cell model and analysis. Neither result makes one isotopomer percentage a universal flux marker.

## Common mistakes

- Calling NADPH “NADH” or treating NADPH as ATP.
- Counting three carbons lost from each glucose 6-phosphate; only one CO2 leaves in the oxidative pass described here.
- Assuming every ribose 5-phosphate molecule must come through oxidative decarboxylation.
- Forgetting that transketolase and transaldolase rearrange carbon while preserving total carbon atoms.
- Inferring pathway flux from NADPH concentration alone without considering NADP+, substrate supply, demand and other reactions.
- Treating a possible carbon-recycling route as having no energetic or pathway cost.
- Reading M+1 or M+2 as a direct rate or a unique branch contribution without an atom-mapping model.

## Practice and references

The accompanying items are open formative checks with unlimited retries; responses are not collected or graded. See the link-only [KEGG pentose phosphate pathway map](https://www.kegg.jp/entry/map00030), [Reactome human pentose phosphate pathway](https://reactome.org/content/detail/R-HSA-71336), [Lee et al. (1998)](https://doi.org/10.1152/ajpendo.1998.274.5.E843) and [Metallo et al. (2009)](https://doi.org/10.1016/j.jbiotec.2009.07.010). No pathway diagram, source text, figure or study data are reproduced here.
