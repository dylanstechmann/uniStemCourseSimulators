# Cell-assay signals, attachment and net growth

## A signal needs a measurement model

The existing biocompatibility reading identifies controls and experimental units. This companion develops the mechanism between a counted population and an assay signal, so a change in optical or metabolic readout cannot silently become a change in cell number. The examples concern fictional materials and normalized measurements. They provide no culture procedure, acceptance standard or claim about an actual implant.

Write a simple signal equation S(t)=B(t)+alpha(t)N(t), where B is material/background signal, N is the population being measured and alpha is average signal per counted cell under the stated assay. A single S value cannot identify all three quantities. Material adsorption of a reporter, scattering, chemical interference and altered cellular activity can change signal even if N is constant. Conversely, cell number can change while opposing signal-per-cell effects leave S nearly unchanged.

A material-only blank estimates one background component under matched conditions. A reporter-spike recovery comparison can test one interference pathway. A direct cell count supplies a different observable with its own segmentation, sampling and viability limitations. None is a universal correction for every assay. Choose controls that address the actual causal path between material, cells and measured signal rather than adding an unmotivated list.

## Separate delivery, attachment and later population change

Let N_seed be cells delivered to a construct and f the retained attached fraction at a specified initial counting time. Define N(0)=f N_seed. Later, a simple constant-rate model is dN/dt=(g−d)N, giving N(t)=f N_seed exp[(g−d)t]. Here g is a division contribution and d a loss contribution in a deliberately closed effective model. Net growth r=g−d can be estimated from two compatible counts; g and d cannot be separated from that count trajectory alone.

If cells immigrate, detach into an unmeasured compartment or change detectability, the equation must change. The initial attachment interval also has its own dynamics: the convenient f is an endpoint fraction, not proof that all losses during that interval share one mechanism. State whether a later fold change is relative to seeded cells, attached cells or an earlier viable count. Those denominators answer different questions.

## Separate worked example

Deliver 800 cells to a fictional coupon and count 400 attached at the declared time zero. Count 800 at two days. Initial attachment is 0.5, attached-population fold change is two and net rate is ln2/2 per day. If background-corrected signal also doubles, the two endpoints are consistent with unchanged average signal per cell. They do not prove that alpha stayed constant at every intermediate time or that no cells were lost.

A division model with g=0.5 per day and d=0.5−ln2/2 gives the same net trajectory as another pair with g=0.7 and d=0.7−ln2/2. Both have positive rates. A measurement that separately follows division and losses could distinguish them under suitable assumptions. More endpoints of the same ideal exponential count curve would improve an estimate of r but would not identify two rates that only appear through their difference.

## Rehearsal: compare counts with signal

Now deliver 1,000 cells and count 600 attached at time zero, then 1,200 at day two. Attachment fraction is 0.6 and net rate remains ln2/2 per day. At the same times, raw signals are 70 and 190, with matched material-only blank 10 at both. Corrected signals are 60 and 180: a threefold signal change accompanies only a twofold count change. Average signal per counted cell rises from 0.1 to 0.15, a ratio of 1.5. Calling the signal change a threefold proliferation result ignores the independent counts and the signal model.

If a separate assay spike has recovery 0.8 on the material and one in a reference vessel, an inverse-recovery correction multiplies the corresponding retained reporter signal by 1.25 under a linear equal-recovery assumption. That does not automatically correct cell number, background or altered metabolism. The spike is an artificial analytical input, not evidence that a cell-generated reporter follows exactly the same fate. Explain what matching evidence would support using that correction.

## Functional output and geometry

Report a tissue-specific output separately from cell count. If a construct's total output is F=N f_cell in a declared additive model, a larger N can raise F without improving per-cell function. A normalized output can also look favorable after losing poorly functioning cells. Preserve total output, denominator and population selection in the report. Do not turn one marker into proof of mature tissue function.

For an imaging assay, retain the physical area and accessible depth used to convert sampled counts to a construct estimate. Material swelling or opacity can change the observable compartment. Fiducials, depth-sensitive imaging or a recovery ledger may help test those mechanisms; a generic increase in image intensity does not identify them. Refer formal uncertainty and independent-unit analysis to Statistics while keeping these material-specific measurement mechanisms explicit.

## Evidence tasks and boundaries

Derive the rehearsal's attachment, net growth, corrected-signal and per-cell ledgers. Construct two distinct positive division/loss pairs giving the same r, then specify an independent observable that could distinguish them. Explain one failure of the linear signal correction and one sampling change caused by a material. Retain calculations and causal diagrams locally. Selected checkpoints do not evaluate the full report or experimental design. MIT OCW 3.051J Spring 2006 quantitative-cell-behavior lecture topics guide scope; no source assay, data, protocol or figure is imported. All examples are original AI-assisted constructions, and qualified review and real experimental evidence remain open.
