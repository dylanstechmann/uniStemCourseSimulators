# Prokaryotic regulatory circuits: negative and positive control

An operon links regulatory DNA and coding regions so that a cell can coordinate expression with its environment. The lac system illustrates two distinct inputs to transcription: a repressor provides negative control, while CAP–cAMP provides positive activation. Reading the system as a small circuit lets us predict expression for a set of conditions and then design a comparison that distinguishes an operator mutation from a change in a diffusible regulator. The examples are synthetic and conceptual, not laboratory instructions.

## The lac operon integrates two signals

When lactose is absent, the LacI repressor can bind the lac operator and reduce transcription from the lac promoter. When lactose is available, its derivative allolactose binds LacI and reduces operator binding. This is **negative inducible control**: an inhibitor of transcription is relieved by the inducer. Repression is often strong rather than perfectly absolute, so predictions should distinguish basal from high expression.

Glucose provides another input. Low glucose increases cAMP, which allows CAP to bind near the promoter and stimulate transcription. High glucose lowers cAMP and reduces this positive activation. Thus lactose removes the repressor, but low glucose is also needed for high output. For wild-type regulatory DNA, a simplified prediction table is:

| Lactose | Glucose | LacI at operator | CAP activation | Expected lac expression |
|---|---|---|---|---|
| absent | high | bound | low | very low |
| absent | low | bound | high | very low |
| present | high | mostly unbound | low | basal to moderate |
| present | low | mostly unbound | high | high |

The two-control model explains why adding lactose does not necessarily produce maximal expression. The repressor and activator act at different regulatory sites, and one input cannot substitute for the other.

## Regulatory mutations act in distinct ways

A loss-of-function mutation in `lacI` removes or weakens the repressor. It makes expression inducible by lactose no longer necessary, but it does not supply CAP activation. With high glucose, a `lacI−` cell can therefore remain below the high-expression state. By contrast, a constitutive operator allele (`lacOᶜ`) alters a DNA site and affects transcription of the linked operon in **cis**. Providing a wild-type `lacI` gene on a separate plasmid does not repair that operator site. A superrepressor allele that cannot respond to allolactose has the opposite logic: it keeps the operator repressed even when lactose is present. These predictions assume the promoter and structural genes are functional.

Not all prokaryotic control is inducible. In the trp operon, tryptophan acts as a corepressor: when tryptophan is abundant, it helps the Trp repressor bind its operator and reduce biosynthetic gene expression. This is **negative repressible control**. The contrast is useful: lactose relieves a repressor when a substrate is available; tryptophan promotes repression when the end product is abundant. Additional mechanisms such as attenuation add layers to some operons, but are outside this short unit.

## Turn the circuit into a controlled test

To ask whether a mutation changes lactose response, compare matched wild-type and candidate-mutant regulatory genotypes under a two-by-two design: lactose absent or present, crossed with high or low glucose. Use the same promoter-linked reporter and cell background for each condition. A reporter with no functional promoter can reveal background signal; a constitutive reporter or a justified cell-density measure can identify broad differences in growth or measurement scale. A known responsive construct provides a positive check that the reporter system can respond. The genotype and operator sequence should be verified, because a reporter change alone does not reveal which regulatory element changed.

The predictions separate hypotheses. A `lacI−` mutant should lose lactose dependence but retain sensitivity to glucose through CAP. A `lacOᶜ` reporter should lose LacI dependence only on the DNA molecule carrying the operator change; adding functional LacI in trans should not restore repression. If every reporter changes similarly across conditions, altered cell growth or global expression may explain the result. Even a clean reporter response establishes regulation of that construct in the tested context, not the entire native chromosome or a phenotype in every environment.

## Worked example

For wild-type cells with lactose present and low glucose, allolactose reduces LacI binding while high cAMP allows CAP activation, so lac expression is high. With lactose present but high glucose, LacI is still mostly released, yet CAP activation is weak, so expression is lower. A `lacI−` mutant under high glucose is not expected to reach the high-output state merely because repression is absent. A two-by-two lactose/glucose comparison with an operator-mutant construct and matched promoter control can test those predictions without conflating the two signals.

## Common reasoning errors

- Saying lactose activates lac transcription by itself, without accounting for glucose and CAP.
- Calling the lac repressor a positive regulator because its binding state changes after lactose is added.
- Expecting a trans-acting repressor on a plasmid to repair a mutated operator in cis.
- Treating a constitutive `lacI` mutant as insensitive to every environmental control.
- Inferring native chromosome behavior from one reporter construct without checking copy number, context and normalization.

## Limits of this lesson

The circuit is a simplified teaching model with synthetic examples. It does not develop transcriptional attenuation, sigma-factor networks, phage switch circuits, or genome-wide bacterial regulation. The course is partial, unreviewed and formative-only; no prediction here is evidence about a real organism.
