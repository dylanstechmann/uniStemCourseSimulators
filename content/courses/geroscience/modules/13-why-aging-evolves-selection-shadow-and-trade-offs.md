# Why aging evolves: the selection shadow, antagonistic pleiotropy and trade-offs

The [systems lesson](01-aging-as-a-systems-process.md) described aging as a gradual loss of resilience across interacting processes. That raises an earlier question. If natural selection favours traits that help organisms survive and reproduce, why has it not removed the decline? The classical evolutionary answer is not that aging is selected for its own sake. Instead, selection becomes **weaker with age**, so harmful late-acting effects are poorly opposed, and some can even be favoured when they come packaged with early benefits. This lesson builds that argument from survival and reproduction numbers, uses toy calculations to show how the environment changes the balance, and states what the theory does and does not explain. All populations and parameters are synthetic teaching values.

## Learning objectives

By the end of this lesson, you should be able to:

1. Explain why the force of natural selection declines with age, and calculate survival and relative selection strength under a constant extrinsic hazard.
2. Distinguish mutation accumulation, antagonistic pleiotropy and the disposable-soma idea, and use a mutation–selection balance to compare early- and late-acting alleles.
3. Calculate lifetime reproduction for a toy pleiotropic allele in high- and low-mortality environments, and state what evolutionary theory does not establish about mechanisms or interventions.

## Survival without aging

Imagine a population that does not age at all: its risk of death per year stays constant, set entirely by **extrinsic** causes such as predators, accidents, starvation and disease. With a constant hazard μ per year, the fraction surviving to age a is

**l(a) = e^(−μa).**

With μ = 0.3 per year, l(5) = e^(−1.5) = **0.223** and l(10) = e^(−3) = **0.050**. The mean lifespan is 1/μ ≈ 3.3 years, even though nobody's body declines. In such a population, very few individuals are ever old, and they are rare because of the environment, not because of senescence.

This is the starting point of the argument associated with Medawar and later formalized by Hamilton (1966) in *The moulding of senescence by natural selection*. A gene variant whose effect appears only at age 10 is expressed in about 5% of this cohort, and only after most of their reproduction has happened. Selection on it is weak.

## The force of selection falls with age

Suppose individuals mature at age α and then reproduce at a constant rate. In a stationary population, the strength of selection against a small increase in mortality at age a is proportional to the reproduction still expected after age a. Under a constant hazard μ, that remaining reproduction falls as e^(−μa). Relative to its value at maturity,

**S(a) = e^(−μ(a − α)) for a ≥ α.**

With μ = 0.3 per year and α = 1 year, S(6) = e^(−1.5) = **0.22**. A mutation that adds mortality at age 6 is opposed about one-fifth as strongly as one acting at maturity. Before maturity the curve is flat at its maximum, because everything an individual will ever contribute still lies ahead. Late in life it approaches zero. The region where it is small is often called the **selection shadow**.

Real populations grow or shrink, and their reproduction varies with age, which changes the exact shape. The qualitative result survives: selection on effects confined to late life is weaker than selection on effects early in life.

## Three classical explanations

**Mutation accumulation.** New harmful mutations arise at a low rate u per generation and are removed by selection of strength s. At equilibrium, the frequency of a harmful allele in a simple haploid model is roughly **q ≈ u/s**. With u = 10⁻⁵ and s = 0.01, an early-acting allele settles near q = 0.001. If the same allele acts only at an age where S = 0.05, the effective selection is 0.01 × 0.05 = 0.0005 and q ≈ 0.02, twenty times more common. Many such late-acting alleles, each poorly removed, can together produce decline in late life.

**Antagonistic pleiotropy.** Williams (1957), in *Pleiotropy, natural selection, and the evolution of senescence*, proposed that some alleles have more than one effect: a benefit early and a cost late. Because early effects are weighted more heavily, selection can spread such an allele even though it shortens life. In this view, aging partly results from traits that were favoured for what they do in youth.

**The disposable soma.** Kirkwood (1977), in *Evolution of ageing*, framed the same logic as an allocation problem. Resources spent on maintaining and repairing the body are unavailable for growth and reproduction. When extrinsic mortality is high, investing heavily in long-term maintenance pays off poorly, because most individuals die of external causes first. The predicted optimum maintains the body well enough for its expected lifespan in the wild, not indefinitely. This can be read as a physiological version of antagonistic pleiotropy.

These explanations are not mutually exclusive, and each predicts that lower extrinsic mortality should, over many generations, favour slower aging.

## A toy pleiotropic allele

Use a discrete model. Each year an individual survives with probability p, and from age 1 onward it produces one offspring per year that it is alive. The expected lifetime reproduction is the sum p + p² + p³ + … = **p/(1 − p)**. The fraction of that total produced after age k is p^k.

Now consider an allele that raises reproduction by 20% at ages 1 and 2 but causes death at the end of age 8.

- **High extrinsic mortality, p = 0.7.** The baseline is 0.7/0.3 = 2.333. Only 0.7⁸ = 5.8% of it comes after age 8. The allele gains 0.2 × (0.7 + 0.49) = 0.238 early and loses 0.135 late, for a total of **2.437**, about 4% more than the baseline. Selection favours it.
- **Low extrinsic mortality, p = 0.95.** The baseline is about 19.0, and 0.95⁸ = 66% of it comes after age 8. The same allele yields only **6.77**, about a third of the baseline. Selection strongly opposes it.

The break-even early boost is 11% when p = 0.7 but about 680% when p = 0.95. The same allele is favoured in one environment and removed in another. This is the quantitative core of the prediction that species, or populations, that are safer from external death should evolve slower aging.

## What the theory predicts and what it does not

Comparative studies broadly report that animals with lower extrinsic mortality for their size, such as many birds, bats and other protected or flying species, tend to live longer than similar-sized animals at higher risk. Laboratory evolution experiments in short-lived organisms have also tested whether selecting on late reproduction changes lifespan. These are tests of the theory's direction, not proofs of a single mechanism, and the patterns have exceptions and confounders, including body size, metabolism and phylogeny.

Evolutionary theory explains why the decline is poorly opposed by selection. It does not by itself say which molecular processes fail, how fast, or in what order; that is the role of the mechanistic lessons in this course. It does not imply that aging is a programme with a purpose, and it does not show that any intervention will slow aging in people. Some species show very slow or negligible demographic aging, which the theory must accommodate rather than ignore. Single-gene changes that extend lifespan in laboratory animals are compatible with the theory, because protected laboratory conditions remove the extrinsic mortality that shaped the wild trade-off.

## Common mistakes

- Saying aging evolved "for the good of the species" or to make room for the young; the classical theories need no such group benefit.
- Treating the absence of old individuals in the wild as evidence that aging kills them; extrinsic mortality alone produces it.
- Assuming selection is equally strong at every age.
- Treating mutation accumulation, antagonistic pleiotropy and the disposable soma as competing theories that must have one winner.
- Reading an evolutionary trade-off as a recommendation to reduce reproduction or change diet in people.
- Forgetting that the same allele can be favoured or removed depending on extrinsic mortality.

## Worked example

**Problem.** A synthetic population has annual survival p = 0.8 and reproduces once a year from age 1. An allele raises reproduction by 20% at ages 1 and 2 and causes death at the end of age 8. Is it favoured, and how large an early boost would make it neutral?

**Step 1: baseline.** p/(1 − p) = 0.8/0.2 = 4.0 expected offspring.

**Step 2: what is lost.** The share after age 8 is 0.8⁸ = 0.168, so the allele forfeits 4.0 × 0.168 = 0.671.

**Step 3: what is gained.** 0.2 × (0.8 + 0.64) = 0.288.

**Step 4: compare.** 4.0 − 0.671 + 0.288 = 3.617 < 4.0, so the allele is disfavoured.

**Step 5: break-even.** Neutrality needs b × 1.44 = 0.671, so b = 0.466, a 47% early boost. At p = 0.7 the break-even is only 11%, so the same allele's fate depends on the environment's extrinsic mortality.

## Limits of this lesson

All populations, rates and alleles are synthetic. The models assume a constant extrinsic hazard, stationary populations, haploid or additive effects and age-independent reproduction, and they ignore density dependence, kin effects, sex differences and changing environments. Named papers are cited as link-only references for their historical arguments; no text, figure or data is reproduced, and the comparative patterns are summarized qualitatively. Nothing here identifies a mechanism of human aging, recommends any intervention, or is medical advice. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
