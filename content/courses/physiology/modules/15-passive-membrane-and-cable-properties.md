# Passive membrane and cable properties: time constant, length constant and conduction

The membrane-potential lesson found steady voltages from concentrations and conductances. Real signals change in time and spread along cells. Two passive properties decide how fast a membrane responds to a current and how far a voltage change reaches before it fades: the **membrane time constant** and the **length constant**. They also explain why thicker axons and myelinated axons conduct faster. This lesson builds both from the membrane's resistance and capacitance and the resistance of the cell's interior. All cells and values are synthetic teaching models.

The undergraduate [MIT OCW 6.021J Quantitative Physiology: Cells and Tissues (Fall 2004) calendar](https://ocw.mit.edu/courses/6-021j-quantitative-physiology-cells-and-tissues-fall-2004/pages/calendar/) gives the core-conductor and cable models four lectures (18, 19, 26 and 27) and myelinated fibers and saltatory conduction two more (29 and 30). This lesson selects the passive foundation of that sequence. It uses 6.021J as a scope comparator only and reproduces no MIT material. Hodgkin–Huxley channel kinetics remain outside this course's developed sequence.

## Learning objectives

By the end of this lesson, you should be able to:

1. Treat a patch of membrane as a resistor and capacitor in parallel, calculate its time constant and a small cell's input resistance, and predict the voltage response to a current step.
2. Calculate the length constant of a cylindrical process from membrane and axial resistances and predict steady-state electrotonic decay with distance.
3. Explain how fiber radius and myelination change the length constant and conduction velocity, and distinguish passive spread from a regenerated action potential.

## The membrane as a resistor and capacitor

Ion channels let current leak through the membrane, which therefore acts as a resistance. The thin lipid bilayer separates charge, so it also acts as a capacitor. Both properties scale with membrane area, and they are reported per unit area. The **specific membrane resistance** R_m (Ω·cm²) gives a patch's resistance when divided by its area. The **specific membrane capacitance** C_m is close to 1 μF/cm² for many cell membranes, a textbook-level value used here.

A patch's resistance and capacitance sit in parallel, and their product is the **membrane time constant**

**τ_m = R_m C_m.**

Area cancels: a small cell and a large cell made of the same membrane share τ_m. **Synthetic membrane:** R_m = 20 kΩ·cm² and C_m = 1 μF/cm² give τ_m = 20 × 10³ × 1 × 10⁻⁶ s = **20 ms**.

For a current step into a small, compact cell, the voltage change approaches its final value exponentially:

**ΔV(t) = ΔV∞ (1 − e^(−t/τ_m)), with ΔV∞ = I R_in.**

After one time constant, 63% of the final change has occurred; after two, 86%. The **input resistance** R_in of a compact spherical cell is R_m divided by its surface area. A 20 μm diameter cell has area 4πr² = 1.26 × 10⁻⁵ cm², so R_in = 20 × 10³ / 1.26 × 10⁻⁵ = **1.59 GΩ**. A 10 pA step would therefore change the voltage by 15.9 mV at steady state, reaching about 10 mV after 20 ms. Smaller cells have higher input resistance and respond to smaller currents, but their time constant is unchanged.

## The core-conductor model and the length constant

In a long, thin process such as an axon or dendrite, current that enters at one point flows along the interior and leaks out through the membrane on the way. Describe a cylinder of radius a by two resistances per unit length:

- **membrane resistance times length**, r_m = R_m / (2πa), in Ω·cm. The membrane of a longer piece leaks more, so this falls as length grows.
- **axial resistance per length**, r_i = R_i / (πa²), in Ω/cm, where R_i is the cytoplasm's resistivity.

At steady state, a voltage held at one point of a long uniform cylinder decays with distance as

**V(x) = V₀ e^(−x/λ), with λ = √(r_m / r_i) = √(R_m a / (2 R_i)).**

The **length constant** λ is the distance over which a steady voltage falls to 37% of its value. **Synthetic axon:** R_m = 20 kΩ·cm², R_i = 100 Ω·cm and a = 1 μm (10⁻⁴ cm) give λ = √(20 × 10³ × 10⁻⁴ / 200) = √0.01 cm = **1.0 mm**. Two length constants away, at 2 mm, only e^(−2) = **13.5%** of the voltage remains.

The square root matters. Because λ ∝ √a, making the radius four times larger only doubles the length constant. Raising R_m (fewer open channels) lengthens λ; raising R_i (more resistive cytoplasm) shortens it.

## From spread to speed

An action potential travels because the depolarized region pushes current ahead of itself and charges the next stretch of membrane to threshold. Faster spread of that charging current means faster conduction. Two passive factors set the pace. A longer λ lets the current reach farther, and a smaller membrane capacitance per length means less charge is needed to depolarize each stretch.

- **Unmyelinated fibers.** A scaling argument from the cable equation gives a conduction velocity proportional to √a. If a synthetic fiber conducts at 1.0 m/s, a fiber with four times the radius conducts at about 2.0 m/s. Raising speed through diameter alone is costly in space.
- **Myelinated fibers.** Many wraps of membrane around the axon greatly increase the effective membrane resistance and lower its capacitance. Multiplying R_m by 100 multiplies λ by √100 = 10. Current then spreads quickly along the insulated internode, and the action potential is regenerated only at the gaps, the nodes. This is **saltatory conduction**. For myelinated fibers, conduction velocity is roughly proportional to diameter rather than to its square root, so doubling the diameter roughly doubles the speed.

## Passive spread is not an action potential

A passive voltage change decays with distance and time; it can be graded in size and summed. An action potential is regenerated by voltage-gated channels wherever the membrane reaches threshold, so it keeps its size as it travels. Passive cable properties decide whether a synaptic potential arriving at a dendrite still matters at the cell body, and how fast an action potential can recruit the next stretch of membrane. They do not by themselves produce an action potential.

## Common mistakes

- Expecting a larger cell to have a longer time constant; τ_m = R_m C_m does not depend on area.
- Confusing specific resistance (Ω·cm²) with resistance (Ω) or with resistance per length.
- Writing λ ∝ a instead of λ ∝ √a for a passive cylinder.
- Treating the length constant as the distance at which a signal disappears; it is the 37% distance.
- Assuming myelin speeds conduction by making the action potential itself faster rather than by insulating the internode.
- Applying passive decay to an action potential, which is regenerated and does not decay with distance.

## Worked example

**Problem.** A synthetic dendrite has radius 0.5 μm, R_m = 40 kΩ·cm² and R_i = 200 Ω·cm. A steady 10 mV depolarization is held at a synapse 0.5 mm from the cell body. What is the length constant, how much of the depolarization reaches the cell body, and what is the membrane time constant?

**Step 1: length constant.** λ = √(40 × 10³ × 0.5 × 10⁻⁴ / (2 × 200)) = √0.005 cm = 0.0707 cm = **0.707 mm**.

**Step 2: decay.** V = 10 mV × e^(−0.5/0.707) = 10 × 0.493 = **4.93 mV** at the cell body, under the infinite-cylinder steady-state model.

**Step 3: time constant.** τ_m = 40 × 10³ × 1 × 10⁻⁶ s = **40 ms**. A brief synaptic current will be filtered more strongly than this steady calculation suggests, because the membrane does not have time to charge fully.

## Limits of this lesson

All values are synthetic, and C_m ≈ 1 μF/cm² is an approximate textbook-level value. The cable results assume a uniform, infinitely long, passive cylinder at steady state with a linear membrane. Real processes taper, branch, end and contain voltage-gated channels, and time-varying signals decay more than the steady-state length constant predicts. The conduction-velocity scalings are proportionalities, not predictions for any particular fiber. Hodgkin–Huxley kinetics, threshold and refractoriness are not developed here. Nothing here describes any person, diagnosis or treatment.
