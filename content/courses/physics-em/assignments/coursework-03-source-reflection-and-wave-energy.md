# Assignment 3: source, reflection and wave-energy evidence

This open report connects the existing Maxwell/plane-wave/interference readings with an explicit radiating boundary and a separate reflecting boundary. It asks for signed fields, normals, cycle averages and energy evidence. Both cases are ideal mathematical models. They do not prescribe an antenna, exposure condition or equipment operation. Retain the full calculations, plots and report locally; browser checkpoints assess selected outputs and interpretations only.

## Constants and cases

Use the foundation's consistent stipulated constants: $c=3.00\times10^8$ m/s, $\mu_0=4\pi\times10^{-7}$ H/m, $\epsilon_0=1/(\mu_0c^2)$ and $Z_0=120\pi$ ohms. Label the source-sheet and conducting-reflection calculations as separate cases with different boundary conditions. Combining their source assumptions without re-solving would define a third problem.

## Part A: distinct prescribed surface current

The first case is an infinite sheet at $z=0$ with $\mathbf K(t)=0.03\cos(\omega t)\hat{\mathbf x}$ A/m. Require outgoing waves in identical vacuum on both sides. Derive tangential electric continuity and the magnetic-field jump using the declared normal. Do not assume that the electric field points with the imposed current; solve the source-boundary sign.

The peak electric magnitude on either side is $Z_0K_0/2=1.8\pi\approx5.65487$ V/m. Each side's time-average outward intensity is $Z_0K_0^2/8=0.0135\pi\approx0.0424115$ W/m². Total outward flux per sheet area is twice that, $0.027\pi$ W/m². Retain the outward normals when combining the two sides: opposite coordinate Poynting vectors do not imply cancellation of the energy leaving the source region.

Evaluate $\mathbf E\cdot\mathbf K$ at the sheet and average it over a cycle. Show that electromagnetic energy supplied by the prescribed source matches both outgoing sides. Explain the difference between that field-source ledger and a detailed mechanical model that might also store carrier kinetic energy. Infinite-area sources have finite flux per area but no finite total antenna power in this calculation.

For an arbitrary positive frequency, write the retarded-time field at positive and negative observation positions. Compare two locations at the same observation time and state which earlier source times they sample. A snapshot of the source does not describe every remote field at that same coordinate time.

## Part B: distinct perfect-conductor reflection

The second case removes the prescribed source sheet. A sinusoidal plane wave with incident peak electric amplitude 4.5 V/m travels toward a perfect conductor at $z=0$ from vacuum $z<0$. Derive the reflected electric sign from the tangential wall condition, then derive its magnetic sign from its propagation direction. Add fields before computing energy or flux.

At the wall the total electric field vanishes while the peak magnetic field is $2E_0/c=30$ nT. Electric antinodes reach 9 V/m at the appropriate positions. The incident intensity is $0.084375/\pi$ W/m². The reflector pressure is $2I/c=0.5625/\pi$ nPa, and the average total standing-field energy density is $\epsilon_0E_0^2=0.5625/\pi$ nJ/m³.

Derive the zero time-average normal Poynting flux from the full standing fields and compare it with their nonzero electric and magnetic energies. Explain why the traveling-wave relation $E=cB$ cannot be used instantaneously for the combined standing pattern. Also explain why momentum transfer to the reflector does not require net time-average energy absorption by the ideal perfect conductor.

## Part C: independent numerical cycle checks

Implement the source, incident, reflected and total fields as separate functions. Use numerical cycle quadrature for intensity, source work, electric energy, magnetic energy and normal Poynting flux. Compare with the analytic averages and refine the time grid. Avoid evaluating a single phase point and treating it as an average.

Check at least two standing-wave positions, including a node and an antinode. Demonstrate that electric and magnetic maxima do not occur at the same position/time, while the average total energy density has the derived spatial behavior. Preserve the vector directions or signed components; magnitude-only computations cannot test the interface signs.

## Part D: scope and model comparison

Contrast source power generation, outward transport, standing energy storage and reflector momentum transfer. State which conclusion follows from each boundary model. A finite antenna's pattern, diffraction, losses and material dispersion require further assumptions; this report does not establish them from an infinite-sheet result or a perfect conductor.

The [MIT OCW 8.02 Spring 2007 class topics](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/class-topics/) and [Chapter 13 scope](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/resources/chapte13em_waves/) are link-only comparators for generation, standing waves and conducting reflection. All text, cases and numerical inputs are original with substantial AI assistance; no source assessment, diagram, animation or code is imported. Qualified physics review, measured workload and experimental competence remain open. The course remains partial and unreviewed.
