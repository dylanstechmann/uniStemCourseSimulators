# Fed-batch culture: changing volume, dilution and feeding to hold a substrate

The batch culture in the [mass-balance lesson](06-cell-culture-mass-balance.md) runs out of glucose after about 71 h. A chemostat avoids exhaustion by removing culture as fast as it feeds, but cells and product leave with the outflow. **Fed-batch** operation sits between the two: concentrated feed is added and nothing is removed until harvest, so the volume rises, nutrients are replaced, and cells and product stay in the vessel. Fed-batch operation is widely used for animal-cell production, which is why it belongs in this course. This lesson writes fed-batch balances with a changing volume, designs a feed that holds a substrate at a set point, and states what such a model leaves out. All numbers are synthetic.

The undergraduate [MIT OCW 10.442 Biochemical Engineering (Spring 2005) calendar](https://ocw.mit.edu/courses/10-442-biochemical-engineering-spring-2005/pages/calendar/) gives three sessions to bioreactor design after continuous culture, without itemizing operating modes on the calendar page. This lesson fills the operating-mode gap between this course's batch and continuous lessons within its animal-cell focus. It uses 10.442 as a scope comparator only and reproduces no MIT material.

## Learning objectives

By the end of this lesson, you should be able to:

1. Write fed-batch balances with a changing volume and explain why a dilution term D = F/V appears in the concentration equations even though nothing leaves the vessel.
2. Calculate an exponential feed that holds a substrate at a set point, the cumulative feed volume, and the time at which the vessel reaches its working volume.
3. Compare batch, fed-batch and continuous operation for cell concentration, product titer and dilution, and state what a single-substrate feed model omits.

## Balances when the volume changes

Let feed enter at flow F(t) with substrate concentration S_F, and let no culture leave. The volume, total cell number N = XV, total substrate SV and total product PV obey

- **dV/dt = F**
- **d(XV)/dt = μXV** (the feed contains no cells, and none leave)
- **d(SV)/dt = F S_F − q_S X V**
- **d(PV)/dt = q_P X V**

These amount balances follow directly from "accumulation = in − out + generation − consumption". The trap appears when converting to concentrations. Expanding d(XV)/dt = V dX/dt + X dV/dt and dividing by V gives

**dX/dt = (μ − D) X, with D = F/V.**

No cells leave, yet the cell concentration grows more slowly than the cell number. The added feed spreads the same cells through more liquid. For the substrate,

**dS/dt = D (S_F − S) − q_S X.**

The first term is the feed's net effect on concentration. It looks like the chemostat term, but in fed-batch it comes from volume growth, not from an outflow. Work with total amounts when in doubt, and convert to concentrations at the end.

## Feeding to hold the substrate at a set point

Holding the substrate at a constant set point S means dS/dt = 0. In amount form, the feed must supply exactly what the cells consume plus what is needed to keep the added volume at concentration S:

**F (S_F − S) = q_S N.**

If the cells grow exponentially, N = N₀e^(μt), and the required feed is itself exponential:

**F(t) = q_S N₀ e^(μt) / (S_F − S).**

**Synthetic culture.** Use the cells of the mass-balance lesson: V₀ = 1.0 L at 5.0 × 10⁵ cells/mL, so N₀ = 5.0 × 10⁸ cells; μ = 0.03 h⁻¹; q_G = 2.0 × 10⁻¹⁰ mmol glucose per cell per hour. A concentrated feed has S_F = 500 mM, and the set point is S = 5 mM.

- Initial demand: q_G N₀ = 0.100 mmol/h, so **F(0) = 0.100/495 L/h = 0.202 mL/h**.
- At 72 h, N = 4.34 × 10⁹ cells and **F(72 h) = 1.75 mL/h**, larger by the factor e^(2.16) ≈ 8.67.
- Cumulative feed: integrating F gives **V_feed = q_S N₀ (e^(μt) − 1)/(μ(S_F − S)) = 51.7 mL** by 72 h, so the volume is 1.052 L.

The batch in the mass-balance lesson had run out of glucose by then. Here the glucose is still at 5 mM.

**Concentration versus number.** At 72 h the vessel holds 4.34 × 10⁹ cells in 1.052 L, a concentration of **4.12 × 10⁶ cells/mL**. A constant-volume culture with the same cell number would read 4.34 × 10⁶ cells/mL. The dilution rate at 72 h is D = 1.75 mL/h ÷ 1052 mL = **1.67 × 10⁻³ h⁻¹**, so the concentration grows at μ − D = 0.0283 h⁻¹, slightly slower than the cells divide.

**Product.** With a stipulated q_P = 1.0 × 10⁻¹² g per cell per hour, the product formed by 72 h is q_P times the integral of N, which is 1.0 × 10⁻¹² × 1.279 × 10¹¹ = 0.128 g. The **titer** is 0.128 g ÷ 1.052 L = **0.122 g/L**. Because nothing is removed, all of it is still in the vessel at harvest. A chemostat would have carried part of it out with the outflow.

## The working volume ends the run

A vessel can hold only so much. If the working volume is 1.5 L, the run must stop when the cumulative feed reaches 0.5 L. Solving 0.100(e^(μt) − 1)/(0.03 × 495) = 0.5 gives e^(μt) = 75.25 and **t = 144 h**. The model would then have 3.76 × 10¹⁰ cells, or 25 × 10⁶ cells/mL. Long before that, the oxygen-transfer capacity from weeks 5–8 and accumulating by-products would need checking. The volume limit is a ceiling, not a prediction that the culture reaches it.

A more concentrated feed (larger S_F) adds less volume per mmol supplied and postpones the volume limit. It also raises the local concentration where the feed enters, which the well-mixed model cannot see.

## Batch, fed-batch and continuous compared

| | Batch | Fed-batch | Continuous (chemostat) |
| --- | --- | --- | --- |
| Inflow / outflow | none / none | feed / none until harvest | feed / equal outflow |
| Volume | constant | rises | constant |
| Concentration equation | dX/dt = μX | dX/dt = (μ − D)X | dX/dt = (μ − D)X |
| What D represents | — | volume growth | removal by outflow |
| Product at harvest | in vessel | in vessel, diluted by feed | partly removed continuously |
| Ends when | a nutrient runs out | volume, oxygen or by-products limit | washout or a planned stop |

The fed-batch and chemostat rows share a concentration equation, but the physical meaning of D differs. Confusing them leads to errors such as expecting fed-batch "washout" when D exceeds μ. In fed-batch, cells are never removed, so the total cell number keeps rising even if the concentration falls.

## Common mistakes

- Writing dX/dt = μX for a fed-batch culture and forgetting the dilution term.
- Treating D = F/V in fed-batch as cell removal and predicting washout.
- Setting a constant feed equal to the initial demand. Exponential growth soon outstrips it, and the substrate falls.
- Reporting titer from the amount of product without dividing by the final volume.
- Ignoring the working-volume limit when extending an exponential feed.
- Assuming that holding one substrate constant keeps the culture balanced, while other nutrients, by-products and osmolality drift.

## Worked example

**Problem.** For the synthetic culture above, a constant feed of 0.202 mL/h is started instead of the exponential feed. Glucose is 5 mM at t = 0. Is the supply adequate after 24 h, and what does the exponential schedule require then?

**Step 1: demand at 24 h.** N = 5.0 × 10⁸ × e^(0.72) = 1.03 × 10⁹ cells, so uptake is q_G N = 0.205 mmol/h.

**Step 2: constant supply.** The feed supplies 0.202 mL/h × 0.500 mmol/mL = 0.101 mmol/h. The cells consume about twice what arrives, so glucose is being drawn down. Once the reservoir in the vessel is used, the culture becomes glucose-limited.

**Step 3: required feed.** The exponential schedule needs F(24 h) = 0.205/495 L/h = **0.415 mL/h**, about twice the constant rate. The gap doubles again every ln 2/μ = 23 h.

## Limits of this lesson

All values are synthetic, and the model is a teaching simplification. It assumes a well-mixed vessel, constant specific rates, exponential growth without death, a single limiting substrate and a feed free of cells. Real feeds supply many nutrients at once and may be added as boluses rather than continuously. By-products such as lactate and ammonium, rising osmolality, oxygen transfer and feed-point gradients can limit a run long before the volume does. Nothing here is a protocol, a feeding recipe or a statement about any real cell line or process.
