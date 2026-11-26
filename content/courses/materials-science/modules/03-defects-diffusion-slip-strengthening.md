# Defects, diffusion, slip and strengthening

**Status:** Original reading in partial Materials Science 0.1.0; unreviewed and formative-only. All alloys, values and property outcomes are synthetic fictional models. They are not measured parameters, processing prescriptions or material approvals.

## Imperfections are part of material structure

An ideal infinite lattice is a starting model, not a complete description of a useful material. Point defects include vacancies, interstitials and substitutional atoms. Dislocations are line defects with characteristic geometry. Grain boundaries, phase boundaries and free surfaces are planar or interface defects. Voids and inclusions can require a three-dimensional description. These categories are simplified: real features interact and can evolve with temperature, composition and mechanical history.

Point defects can participate in diffusion because atomic rearrangement may occur through local jumps into available configurations. The details depend on the species and lattice, so observing net transport does not automatically identify a vacancy mechanism. Diffusion coefficients summarize mobility under particular conditions; they are not universal constants for a material name.

Dislocations provide a mechanism for slip in which localized motion accommodates permanent deformation without simultaneously displacing an entire atomic plane. A dislocation’s Burgers vector describes lattice displacement associated with its closure failure, while line direction and slip plane help define possible motion. Full vector derivations belong to more advanced treatments. Here the essential connection is that line defects can enable plasticity and that obstacles to their motion can strengthen a material.

Interfaces can both obstruct and assist processes. Grain boundaries can impede some dislocation motion, provide rapid diffusion pathways in some conditions, or act as sites for precipitation and corrosion. Therefore a statement such as “more boundaries are always beneficial” is unsupported. The property, loading state, environment and microstructure must be named.

## Arrhenius diffusion and steady flux

An idealized diffusion coefficient can follow D = D₀exp(−Q/RT), where D₀ is a prefactor, Q is an activation energy, R is the gas constant and T is absolute temperature. The exponent must be dimensionless and negative for this conventional form. The model captures strong temperature sensitivity but does not establish mechanism by itself.

For fictional inputs D₀ = 1.0×10⁻⁵ m²/s, Q = 80,000 J/mol, R = 8.314 J/(mol·K) and T = 1000 K, Q/(RT) = 9.622…, giving D = **6.62335…×10⁻¹⁰ m²/s**. This is a stipulated model output, not an experimental value for any real substance. Using Celsius directly or dropping the negative sign would invalidate the calculation.

For steady one-dimensional diffusion with constant D and linear concentration change, flux magnitude is J = DΔC/Δx. Fick’s signed form relates flux to the negative concentration gradient, so direction depends on the coordinate convention. With D = 1.0×10⁻¹⁰ m²/s, ΔC = 0.80 mol/m³ and Δx = 0.0020 m, the fictional flux magnitude is **4.0×10⁻⁸ mol/(m²·s)**. This calculation assumes steady state and does not describe transient buildup, moving boundaries or coupled reactions.

A computed flux does not reveal the diffusing species or prove a unique defect pathway. Those questions require compositional and mechanistic evidence. It also does not supply a heat-treatment duration or fabrication setting; this package deliberately provides neither.

## Slip and strengthening mechanisms

Plastic deformation requires both driving conditions and available mechanisms. Strengthening strategies generally increase resistance to dislocation motion or reduce the freedom of deformation, but they can affect other properties. Solid-solution strengthening introduces local lattice distortions and interactions. Work strengthening increases dislocation density and entanglement through prior plastic deformation. Grain-size strengthening uses boundary resistance in suitable regimes. Precipitation strengthening depends on particle size, spacing, coherency and stability, not merely the presence of a second phase.

A simplified Hall–Petch expression is σ = σ₀ + k/√d, where σ is a model yield strength and d is grain size with compatible units. For fictional σ₀ = 100 MPa, k = 0.50 MPa·m^1/2 and d = 4.0×10⁻⁶ m, √d = 0.002 m^1/2 and σ = **350 MPa**. This model is bounded: it does not apply indefinitely to every grain size, material or deformation mechanism, and it does not predict ductility or toughness.

Suppose a fictional refined alloy shows higher measured strength but lower ductility than a comparator. The defensible conclusion is a trade-off for that condition. Exclusive causation would require matched composition, processing and measurement evidence. Other strengthening routes can also trade ductility, corrosion behavior, thermal stability or toughness. Optimizing one measured number can damage system performance.

## Linking mechanisms without overclaiming

Diffusion and dislocation slip are distinct, but they can interact in time- and temperature-dependent deformation. Recovery, recrystallization, precipitate evolution and creep may alter the structure on which a simple strengthening estimate was based. A single room-temperature strength value cannot establish long-term stability.

An evidence table should separate observed structure, assumed mechanism, calculated model quantity and measured property. If grain size was not measured, it remains unknown; if only overall flux was observed, the defect species remains unresolved; if ductility was not tested, it cannot be inferred from strength alone. Independent comparisons must avoid treating multiple readings from one specimen as independent materials.

The official [MIT 3.091SC Fall 2010 syllabus](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/syllabus/) includes defects, kinetics and diffusion across a broader sequence, while the [MIT 3.012 Fall 2005 calendar](https://ocw.mit.edu/courses/3-012-fundamentals-of-materials-science-fall-2005/pages/calendar/) supplies link-only thermodynamic context. These sources inform scope only. The original exercises here use fictional parameters and do not reproduce source problems. Advanced rate equations, nonsteady diffusion solutions, dislocation-energy derivations and processing design remain outside this foundational route.
