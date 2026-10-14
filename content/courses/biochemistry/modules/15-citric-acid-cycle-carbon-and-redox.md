# The citric acid cycle: carbon, reducing equivalents and replenishment

The citric acid (tricarboxylic acid, or TCA) cycle oxidizes acetyl groups while regenerating the four-carbon acceptor oxaloacetate. It also supplies precursors for biosynthesis. Keeping a carbon ledger and an electron-carrier ledger separate makes the cycle easier to reason about: carbon dioxide reports carbon loss, while NADH and FADH₂ carry electrons toward respiratory oxidation. All numerical examples here are bookkeeping models, not measurements from cells.

## Learning objectives

By the end of this lesson, you should be able to:

1. Account for carbon and cofactor outputs from one acetyl-CoA turn of the citric acid cycle and distinguish those outputs from pyruvate oxidation and electron transport.
2. Explain how withdrawal and replenishment of cycle intermediates and changing redox or energy demand can affect pathway flux.

## One turn: follow two ledgers

Pyruvate dehydrogenase acts **before** the cycle: one three-carbon pyruvate becomes a two-carbon acetyl group on CoA, releasing one CO₂ and making one NADH. The cycle proper begins when acetyl-CoA condenses with four-carbon oxaloacetate to form six-carbon citrate. Citrate is rearranged to isocitrate, then undergoes two oxidative decarboxylations, passing through α-ketoglutarate and succinyl-CoA. The remaining four-carbon intermediates pass through succinate, fumarate and malate to regenerate oxaloacetate. The acceptor is regenerated rather than consumed in the cycle’s net bookkeeping.

| Per acetyl-CoA entering the cycle | Carbon or energy-carrier result |
|---|---|
| Acetyl group | 2 carbons enter; the four-carbon oxaloacetate acceptor is regenerated |
| Oxidative decarboxylation | 2 CO₂ are released per turn |
| NAD⁺ reduction | 3 NADH are produced per turn |
| FAD reduction | 1 FADH₂ is produced per turn |
| Substrate-level phosphorylation | 1 GTP is produced per turn; the high-energy phosphate can be transferred to ADP |

One of the FAD-linked reactions is catalyzed by succinate dehydrogenase, which is also respiratory-chain complex II. That connection does not make FADH₂ a direct source of ATP: its electrons enter the respiratory chain, and ATP synthesis depends on the resulting proton motive force and coupling. The GTP-forming step is substrate-level phosphorylation and does not require the membrane gradient.

The two CO₂ released in a turn do not have to be the two carbons that entered as the acetyl group in that same turn. At first, carbon atoms mix among cycle intermediates; label can remain in the pool and appear as CO₂ during later turns. A carbon count across a complete oxidation boundary is valid, but “new acetyl carbon immediately becomes CO₂” is not a safe single-turn interpretation.

## From glucose to two turns

One glucose makes two pyruvate molecules, so complete processing supplies two acetyl-CoA molecules and runs the cycle twice. The cycle therefore produces **4 CO₂, 6 NADH, 2 FADH₂ and 2 GTP per glucose** under this simplified accounting. Pyruvate dehydrogenase separately contributes 2 CO₂ and 2 NADH; glycolysis contributes 2 pyruvate and 2 cytosolic NADH, plus a net 2 ATP. Thus the familiar six-CO₂ carbon count includes both pyruvate oxidation and the two cycle turns. It is not a count of two CO₂ from one glucose during the cycle’s first turn.

Do not add a fixed ATP number to the cycle’s NADH and FADH₂ without stating a P/O convention and the cell’s shuttle and coupling assumptions. The mitochondrial-bioenergetics lesson treats those qualifications. Here, report the carrier molecules and the one GTP per turn directly.

## A metabolic hub, not a closed pipe

Cycle intermediates can leave for other pathways. Citrate can supply carbon for lipid synthesis; α-ketoglutarate and oxaloacetate connect to amino-acid metabolism; oxaloacetate can enter gluconeogenesis. If intermediates leave faster than they are replenished, the cycle pool can shrink and limit ongoing oxidation even when acetyl-CoA is available. Replenishing reactions are called **anaplerotic**. In many mammalian tissues, pyruvate carboxylase can use pyruvate, bicarbonate and ATP to form oxaloacetate; amino-acid carbon can also refill cycle intermediates. These routes restore pools but do not erase the need to track where each carbon entered or left.

Flux also responds to the state of the system. A high NADH/NAD⁺ ratio can signal that electron carriers are reduced and respiratory oxidation is constrained; high ATP and low ADP often indicate less immediate demand for oxidative phosphorylation. Some control points respond to ADP, calcium or substrate availability, and the size of those effects depends on tissue and conditions. No one metabolite is a universal “on/off switch.” A stable citrate or oxaloacetate concentration does not prove cycle flux stayed constant: production and consumption can change together. Isotope time courses, oxygen use, redox measurements and enzyme-state measurements answer different parts of that question.

## Worked example

**Problem.** A synthetic cell completely processes 3.0 mmol of glucose through pyruvate oxidation and two TCA turns per glucose. How much GTP is formed in the cycle, and how many NADH molecules are produced by pyruvate dehydrogenase plus the cycle? Exclude glycolytic NADH.

**Step 1: cycle turns.** Each glucose supplies two acetyl-CoA, so 3.0 mmol glucose gives 6.0 mmol cycle turns.

**Step 2: GTP.** Six turns × 1 mmol GTP per turn = **6.0 mmol GTP**.

**Step 3: NADH.** Pyruvate dehydrogenase makes 2 NADH per glucose and the cycle makes 6; together that is 8 per glucose. 3.0 × 8 = **24 mmol NADH**. Cytosolic glycolytic NADH is outside this requested boundary.

## Common mistakes

- Including pyruvate dehydrogenase inside the cycle’s per-turn output.
- Counting the four CO₂, six NADH or two FADH₂ from two turns as the products of one turn.
- Treating GTP as oxidative phosphorylation or treating NADH as ATP.
- Assuming the acetyl carbons must be the first carbons released as CO₂.
- Calling the cycle closed when biosynthetic withdrawal can require anaplerotic refill.
- Inferring flux from a single pool concentration or a single tracer fraction.

## Reading isotope labels without overclaiming flux

Stable-isotope tracers add a second carbon ledger. A mass isotopologue written **M+n** contains *n* heavy-isotope atoms (here, ¹³C) in the measured molecule; M+2 does not specify which two carbon positions are labeled. Position-specific isotopomers distinguish those arrangements, which can matter when a pathway rearranges or loses particular carbons.

For a simplified entry map, uniformly labeled [U-¹³C₆]glucose produces [U-¹³C₃]pyruvate in glycolysis. Pyruvate dehydrogenase removes one pyruvate carbon as CO₂ and transfers the remaining two labeled carbons to acetyl-CoA. If that acetyl-CoA condenses with mostly unlabeled oxaloacetate, newly made citrate can be M+2. Pyruvate carboxylase takes a different route: it adds bicarbonate to pyruvate to make oxaloacetate. If the bicarbonate is unlabeled, that oxaloacetate can be M+3; its condensation with unlabeled acetyl-CoA can therefore make M+3 citrate. These are conditional entry signatures, not unique fingerprints: the result changes with bicarbonate labeling, precursor enrichment, other carbon sources, exchange, and later cycle turns.

**Synthetic illustration.** Suppose a deliberately reduced teaching dataset reports only M+0, M+2 and M+3 citrate fractions after the same labeled-glucose pulse. Each row sums to 100%; the omitted isotopologue classes are assumed to be zero in this simplified example.

| Time after pulse | M+0 citrate | M+2 citrate | M+3 citrate | Fraction labeled (M+2 + M+3) |
|---|---:|---:|---:|---:|
| 2 min | 70% | 20% | 10% | 30% |
| 12 min | 40% | 45% | 15% | 60% |

The labeled fraction rises by **30 percentage points**, from 30% to 60%, and doubles over this interval. That establishes greater label incorporation in the measured citrate pool under the stated pulse. It does **not** show that cycle flux doubled: labeling can rise as the tracer reaches more of the pool even if the underlying steady flux is unchanged. A different precursor enrichment, pool size, unlabeled nutrient contribution, exchange rate or sampling time can also change the observed fractions.

To estimate flux, investigators need an explicit model connecting tracer delivery and precursor labeling to time-resolved product labeling, along with measurements or defensible constraints on relevant pools and competing entry, exchange and exit routes. Position-specific measurements can distinguish patterns that a total M+n count merges. Multiple time points help constrain rates, but do not rescue an incomplete network model or make every rate identifiable. A concentration is a pool measurement; an isotopologue fraction is a labeling measurement; a flux is an amount per time inferred from a defined model and data. Keep those quantities distinct.

Primary studies illustrate both the opportunity and the limits. In a cultured-cell study, Alves and colleagues combined positional labeling of citrate with precursor/product relationships and dynamic modeling to estimate several mitochondrial rates; their analysis also showed that fitting glutamate labeling alone could admit more than one flux solution under their model. In perfused rat hearts, Comte and colleagues found that the precision and estimate of pyruvate-carboxylation contribution depended on the supplied substrate mixture. These are system-specific examples, not universal flux fractions. See the link-only primary reports: [Alves et al. (2015), integrated step-wise mass-isotopomeric flux analysis](https://doi.org/10.1016/j.cmet.2015.08.021) and [Comte et al. (1997), ¹³C analysis of anaplerotic pyruvate carboxylation](https://doi.org/10.1074/jbc.272.42.26125). No paper text, figure, table or data is reproduced here.

## Practice and pathway references

The accompanying questions use public formative answers with unlimited retries; no work is collected or graded. For an optional pathway map and a human pathway reconstruction, see the link-only [KEGG citrate-cycle map](https://www.kegg.jp/entry/map00020) and [Reactome human citric-acid-cycle pathway](https://reactome.org/content/detail/R-HSA-71403). These sources support pathway identity and canonical reaction accounting; no pathway diagrams or source text are reproduced here.
