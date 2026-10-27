# Physics II: Electricity & Magnetism scope crosswalk

This crosswalk compares the local package, version 0.7.0, with two openly published undergraduate courses: MIT OpenCourseWare 8.02 Physics II: Electricity and Magnetism, Spring 2007 ([class topics](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/class-topics/)), and Open Yale Courses PHYS 201 Fundamentals of Physics II, taught by Ramamurti Shankar ([course page](https://oyc.yale.edu/physics/phys-201)). It was compiled with AI assistance on 2026-10-26 from each comparator's public session titles, lecture overviews and chapter titles, and from the local readings and practice. It is an agent-run comparison, not a review by the owner or by a physics instructor. It does not compare lecture content, problem sets, exams or workload, and topic alignment establishes no equivalence, credit or endorsement.

PHYS 201 also teaches geometric optics and quantum mechanics, so only its electromagnetism lectures and its wave-optics lecture bear on this package. Status labels: **covered** means a local reading develops the topic with a worked example and practice; **shallow** means the topic appears only in an optional activity or a brief mention; **absent** means no local instruction; **deferred** means deliberately outside the declared boundary for now. Local numbers are lesson IDs (physics-em-N), and each links to its reading.

## Comparator map

| Topic | MIT 8.02 sessions | Yale PHYS 201 lectures | Local lessons | Status |
| --- | --- | --- | --- | --- |
| Charge, Coulomb's law and electric fields | 1–2 | 1–2 | [1](modules/01-electric-fields-potential-and-capacitance.md), [7](modules/07-superposition-potential-and-gauss-boundaries.md) | Covered |
| Electric dipoles | 2 | 2 (chapter "Electric Dipoles") | [24](modules/24-electric-dipoles-fields-torque-energy-and-force.md) | Covered in 0.7.0; previously absent |
| Continuous charge distributions | 2, 6 | — | [7](modules/07-superposition-potential-and-gauss-boundaries.md), [17](modules/continuous-charge-and-grounded-boundaries.md) | Covered |
| Gradients, line and surface integrals | 3 | — | [7](modules/07-superposition-potential-and-gauss-boundaries.md) | Covered as needed; the general toolkit belongs to Calculus III |
| Potential, equipotentials and E from V | 4–5 | 5 | [1](modules/01-electric-fields-potential-and-capacitance.md), [7](modules/07-superposition-potential-and-gauss-boundaries.md) | Covered |
| Gauss's law and conductors | 7–9 | 3–4 | [7](modules/07-superposition-potential-and-gauss-boundaries.md), [17](modules/continuous-charge-and-grounded-boundaries.md) | Covered |
| Capacitors, dielectrics and stored energy | 9–11 | 6 | [1](modules/01-electric-fields-potential-and-capacitance.md), [5](modules/05-the-membrane-as-a-capacitor.md), [8](modules/08-capacitance-dielectrics-and-energy-boundaries.md) | Covered |
| Current, resistance and DC circuits | 12 | 7–8 | [2](modules/02-current-resistance-and-rc-transients.md), [9](modules/09-kirchhoff-thevenin-and-source-loading.md) | Covered |
| Biot–Savart and Ampère's law | 14–16 | 10 | [16](modules/16-sources-of-magnetic-fields-biot-savart-ampere-and-dipoles.md) | Covered |
| Magnetic forces on charges, currents and dipoles | 17–19 | 8 | [3](modules/03-magnetic-forces-and-induction.md), [11](modules/11-magnetic-vectors-fields-and-force-work.md), [16](modules/16-sources-of-magnetic-fields-biot-savart-ampere-and-dipoles.md) | Covered; magnetic levitation only qualitatively |
| Faraday's law, Lenz's law and motional emf | 20–21 | 11 | [3](modules/03-magnetic-forces-and-induction.md), [6](modules/06-induction-flow-meters-and-current-limits.md), [12](modules/12-induction-lenz-and-inductor-energy.md) | Covered |
| Mutual inductance, inductors and magnetic energy | 22–23 | 12 (chapter "Review of Inductors") | [12](modules/12-induction-lenz-and-inductor-energy.md), [18](modules/coupled-inductors-and-mechanical-power.md) | Covered |
| RC and RL transients | 23, 25–26 | 12 (chapter "Inductive Circuits") | [2](modules/02-current-resistance-and-rc-transients.md), [10](modules/10-rc-switching-initial-conditions-and-energy.md), [12](modules/12-induction-lenz-and-inductor-energy.md) | Covered |
| LC oscillation and undriven LRC circuits | 27 | 12 ("LCR Circuits — DC Voltage") | [25](modules/25-lc-oscillation-and-the-undriven-series-rlc-circuit.md) | Covered in 0.7.0; previously absent |
| Driven LRC circuits, impedance and resonance | 28–29 | 13 (impedance, resonance) | [13](modules/13-phasors-loading-and-measurement-inference.md), optional [project guide](assignments/series-resonance-project-guide.md) | Shallow: lesson 13 teaches phasors, but the driven resonance curve, bandwidth and Q appear only in the optional, ungraded project guide |
| Displacement current and Maxwell's equations | 30 | 13 (chapter "Displacement Current"), 14–15 | [14](modules/14-displacement-current-maxwell-and-wave-energy.md) | Covered |
| Electromagnetic waves, energy flow and momentum | 30–32 | 14–15 | [14](modules/14-displacement-current-maxwell-and-wave-energy.md), [19](modules/radiating-sheet-reflection-and-standing-energy.md) | Covered for ideal plane waves and an infinite current sheet |
| Generating radiation | 33 | — | [19](modules/radiating-sheet-reflection-and-standing-energy.md) | Deferred: finite antennas and radiation patterns are outside the package |
| Interference | 35 | 18 | [15](modules/15-wave-superposition-and-interference.md) | Covered for two coherent sources |
| Diffraction and gratings | — | 18 (chapter "Interference and Diffraction of Light") | — | Deferred |
| Magnetic materials | — | — | — | Deferred; stated in lesson 16's limits |
| Geometric optics | — | 16–17 | — | Outside this package's boundary |
| Quantum mechanics | — | 19–25 | — | Outside this package's boundary |
| Laboratory work | TEAL experiments and group work | — | [Virtual lab 1](labs/01-calibration-loading-and-time-constants.md) | Shallow: one synthetic-data lab |
| Homework and exams | Three exams and a final (sessions 13, 24, 34 and 36) | Weekly homework, a midterm and a final | — | Absent by policy: all practice is formative-only |

## What 0.7.0 changed

The two topics that both comparators teach and the package lacked now have original readings. The electric-dipole lesson, grouped in week 1 after superposition, builds the dipole field and potential from two point charges, compares exact and far-field values, and treats torque, orientation energy and the force in a nonuniform field with a Newton's-third-law check. The LC and undriven RLC lesson, grouped in week 9 after inductor energy and coupled coils, derives the oscillation from the loop rule, follows the energy between the two fields, and classifies the damped responses with their decay rates, quality factor and energy per period. Together they add six objectives, 21 practice items and eight retrieval cards. Their worked values are recomputed independently in the repository's tests.

## Remaining gaps

- A core reading on the driven series RLC response, so that resonance, bandwidth and Q do not depend on the optional project guide.
- Diffraction and gratings, if the boundary is extended toward the wave-optics lecture that PHYS 201 includes.
- Finite antennas, magnetic materials, graded homework and exams, a fuller laboratory sequence, measured workload, and review by a qualified person.
