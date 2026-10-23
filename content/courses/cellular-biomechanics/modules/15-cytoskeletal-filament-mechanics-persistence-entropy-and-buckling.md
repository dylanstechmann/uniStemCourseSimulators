# Cytoskeletal filament mechanics: persistence length, entropic elasticity and buckling

The [adhesion and cytoskeleton lesson](02-adhesion-cytoskeleton-and-force-transmission.md) described actin filaments, microtubules and intermediate filaments as the cell's load-bearing structures and traced force from the matrix to the nucleus. It treated the filaments qualitatively. This lesson gives them mechanical properties. A filament's **bending stiffness** sets how far thermal motion bends it, measured by its **persistence length**. A flexible chain resists stretching mainly by losing configurational entropy rather than by straining bonds, so it behaves as an **entropic spring**. A stiff filament pushed along its length can **buckle** at a force that depends steeply on its length. All filaments and parameter values here are synthetic, labelled actin-like or microtubule-like for orientation only, and thermal energy is stipulated as k_BT = 4.1 pN·nm.

The MIT OCW [20.310J Molecular, Cellular, and Tissue Biomechanics (Spring 2015) calendar](https://ocw.mit.edu/courses/20-310j-molecular-cellular-and-tissue-biomechanics-spring-2015/pages/calendar/) opens with single-molecule mechanics (session 2) and returns to microstructural models of the cytoskeleton (session 19). This lesson draws on that scope within the local cytoskeleton week. It uses 20.310J as a scope comparator only and reproduces no MIT material.

## Learning objectives

By the end of this lesson, you should be able to:

1. Relate bending stiffness to persistence length, calculate the decay of tangent correlations, and classify a filament as flexible, semiflexible or stiff by comparing its persistence and contour lengths.
2. Calculate the mean-square end-to-end distance of a worm-like chain, the small-extension entropic spring constant, and the force needed for a given fractional extension.
3. Calculate the Euler buckling force of a filament, the length at which it buckles under a given load, and how bundling changes it, and state the assumptions behind each estimate.

## Bending stiffness and persistence length

A thin elastic rod resists bending with stiffness κ = EI, the product of Young's modulus and the second moment of area. Bending a short segment of length s through a small angle θ stores energy κθ²/(2s). At temperature T, thermal kicks supply energy of order k_BT, so a filament wanders in direction over a length set by

**L_p = κ / (k_BT),**

the **persistence length**. Along a filament in three dimensions, the average cosine of the angle between tangents a distance s apart decays as

**⟨cos θ(s)⟩ = e^(−s/L_p).**

(For a filament confined to a surface, the exponent is −s/(2L_p).)

**Synthetic examples.** An actin-like filament with L_p = 10 μm has κ = 4.1 × 10⁻²¹ J × 10 × 10⁻⁶ m = **4.1 × 10⁻²⁶ N·m²**. Two points 2 μm apart keep a tangent correlation of e^(−0.2) = **0.82**: nearly straight over that span. A microtubule-like filament with L_p = 5 mm has κ = **2.05 × 10⁻²³ N·m²**, five hundred times stiffer, and is essentially straight on cellular scales.

**Classification.** Compare L_p with the contour length L. If L ≫ L_p the chain is **flexible** and coils randomly. If L ≈ L_p it is **semiflexible**, bending gently. If L ≪ L_p it is effectively **stiff**. Actin-like filaments a few micrometres long are semiflexible, which is why they form networks with unusual elasticity.

## The worm-like chain

The **worm-like chain** treats a filament as a continuous, inextensible rod with bending stiffness κ in a thermal bath. Its mean-square end-to-end distance is

**⟨R²⟩ = 2L_pL[1 − (L_p/L)(1 − e^(−L/L_p))].**

The formula covers both limits. For L ≪ L_p it approaches L², a straight rod. For L ≫ L_p it approaches 2L_pL, a random coil whose effective segment, the **Kuhn length**, is 2L_p. For a semiflexible filament with L = L_p, the root-mean-square end-to-end distance is **0.858 L**, already noticeably shorter than the contour.

## Entropic elasticity

Pulling the ends of a coiled chain apart reduces the number of shapes it can adopt. Its entropy falls, and the free energy rises even though no bond is stretched. For small extensions of a flexible chain, this gives a linear **entropic spring**:

**k_entropic ≈ 3k_BT / ⟨R²⟩.**

**Synthetic example.** A flexible polymer with L_p = 50 nm and L = 1.0 μm has ⟨R²⟩ = 9.5 × 10⁴ nm², so k ≈ 3 × 4.1/95 000 = **1.29 × 10⁻⁴ pN/nm**. The stiffness is proportional to temperature. Unlike a metal spring, an entropic spring gets stiffer when warmed, a signature that distinguishes entropic from energetic elasticity.

At larger extensions the response becomes strongly nonlinear. A widely used interpolation for the worm-like chain (Marko–Siggia) relates force F to fractional extension x/L:

**F L_p / (k_BT) = 1/[4(1 − x/L)²] − 1/4 + x/L.**

For the same chain with L_p = 50 nm, half extension needs only **0.10 pN**, while 90% extension needs **2.10 pN**, twenty times more. The force diverges as the chain approaches full extension, where bond stretching or unfolding eventually takes over. This is an interpolation rather than an exact force law;its approximation error is not quantified for these synthetic examples,and stretch/unfolding requires additional model information.

## Buckling of stiff filaments

A filament pushed along its axis stays straight until the compressive force reaches the Euler buckling load. For a rod pinned at both ends,

**F_c = π²κ / L².**

**Synthetic examples.** A microtubule-like filament 5 μm long buckles at F_c = π² × 2.05 × 10⁻²³/(5 × 10⁻⁶)² = **8.1 pN**. An actin-like filament only 1 μm long buckles at **0.40 pN**, less than the force of a single motor protein. Because F_c falls as 1/L², halving a filament's length quadruples the force it can bear.

These numbers explain several design patterns, stated here as model consequences rather than claims about any particular cell. Pushing structures such as protrusions use many short or bundled filaments. Crosslinking n filaments into a bundle raises the bending stiffness between about n times, if the filaments slide freely past one another, and n² times, if they are tightly coupled. Filaments embedded in a surrounding network are laterally supported and buckle at shorter wavelengths and higher forces than free filaments of the same length.

## Common mistakes

- Treating persistence length as a physical length of the filament; it is a ratio of stiffness to thermal energy.
- Using the three-dimensional correlation decay for a filament confined to a surface.
- Applying the flexible-chain result ⟨R²⟩ = 2L_pL to a semiflexible filament with L ≈ L_p.
- Expecting entropic springs to soften when heated.
- Using a linear spring constant at large fractional extensions.
- Forgetting that the buckling force scales as 1/L² and depends on end conditions.
- Mixing pN·nm with J or N·m; 4.1 pN·nm equals 4.1 × 10⁻²¹ J.

## Worked example

**Problem.** A synthetic microtubule-like filament has κ = 2.0 × 10⁻²³ N·m². Find its persistence length, the force at which a 10 μm segment buckles with pinned ends, the longest segment that can bear 5 pN, and the buckling force of a tightly coupled bundle of ten such 10 μm filaments.

**Step 1: persistence length.** L_p = κ/k_BT = 2.0 × 10⁻²³/4.1 × 10⁻²¹ = 4.9 × 10⁻³ m, about 4.9 mm. The filament is stiff on any cellular scale.

**Step 2: buckling at 10 μm.** F_c = π² × 2.0 × 10⁻²³/(1.0 × 10⁻⁵)² = 1.97 pN.

**Step 3: longest segment for 5 pN.** L = π√(κ/F) = π√(2.0 × 10⁻²³/5.0 × 10⁻¹²) = 6.28 μm.

**Step 4: bundle.** Tight coupling multiplies κ by about 10² = 100, so the bundle buckles near 197 pN. Free sliding would give only about 19.7 pN; real crosslinkers lie between these bounds.

## Limits of this lesson

All filaments and parameter values are synthetic; actin-like and microtubule-like labels are for orientation only. The models assume homogeneous, inextensible, isotropic rods in thermal equilibrium, small deflections for the Euler load and ideal end conditions. Filament polymerization dynamics, active motor forces, network rheology, crosslinker kinetics, prestress and intermediate-filament strain stiffening are not developed. Nothing here describes a measured property of a particular cell or an experimental protocol. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
