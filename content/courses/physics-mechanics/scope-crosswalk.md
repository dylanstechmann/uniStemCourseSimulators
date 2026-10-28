# Physics: Mechanics scope crosswalk

This crosswalk compares the local package, version 0.7.0, with two openly published undergraduate mechanics courses: MIT OpenCourseWare 8.01SC Classical Mechanics, Fall 2016 ([syllabus](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/syllabus/), Weeks 0–12), and Open Yale Courses PHYS 200 Fundamentals of Physics I, taught by Ramamurti Shankar ([course page](https://oyc.yale.edu/physics/phys-200)). It was compiled with AI assistance on 2026-10-28 from each comparator's public week, lesson and lecture titles, from the overviews and chapter titles of Yale lectures 8 and 10 and the sub-lesson titles of MIT's Week 5, and from the local readings and practice. It is an agent-run comparison, not a review by the owner or by a physics instructor. It does not compare lecture content, problem sets, exams or workload, and topic alignment establishes no equivalence, credit or endorsement.

Two scope notes apply. PHYS 200 also teaches special relativity, waves, fluids and thermodynamics, which a mechanics course for biomedical engineers does not require. Thermodynamics belongs to the Thermodynamics & Transport course, and relativity is outside this package's boundary. MIT's Fall 2016 version is a rewritten online course with week introductions, worked examples and deep dives. Status labels: **covered** means a local reading develops the topic with a worked example and practice; **absent** means no local instruction; **elsewhere** means another local course teaches it; **local extension** means the package teaches a topic neither comparator names in its titles. Local numbers are lesson IDs (physics-mechanics-N), and each links to its reading.

## Comparator map

| Topic | MIT 8.01SC | Yale PHYS 200 | Local lessons | Status |
| --- | --- | --- | --- | --- |
| Vectors and kinematics in one and two dimensions | Review Lesson 0; Week 1 Lessons 1–3 | Lectures 1–2 | [1](modules/01-kinematics-and-force-balance.md), [7](modules/07-vector-kinematics-frames-and-constraints.md) | Covered |
| Newton's laws, gravity, contact forces, tension, springs and friction | Week 2 Lessons 4–7 and friction deep dive | Lectures 3–4 | [1](modules/01-kinematics-and-force-balance.md), [8](modules/08-free-body-diagrams-contact-and-friction.md) | Covered |
| Circular motion | Week 3 Lessons 8–11 | — | [6](modules/06-centrifuge-rotation-and-balance.md) | Covered; named only by MIT |
| Pulleys, constraints and massive ropes | Week 4 Lessons 12–13 | — | [16](modules/massive-pulleys-and-coupled-constraints.md) | Covered; named only by MIT |
| Resistive (drag) forces | Week 4 Lesson 14 | — | — | Shallow: drag appears only as a neglected effect and as damping; named only by MIT |
| Momentum, impulse and conservation of momentum | Week 5 Lessons 15–16 | Lecture 8 | [3](modules/03-momentum-collisions-and-impulse.md), [5](modules/05-impact-forces-impulse-and-work-energy.md), [9](modules/09-work-momentum-and-system-boundaries.md) | Covered |
| Center of mass and its motion | Week 5 Lesson 17 ("Center of Mass and Motion of the Center of Mass") | Lecture 8 (chapter "The Center of Mass") | [22](modules/22-center-of-mass-parallel-axes-and-system-energy.md) | Covered in 0.7.0; previously absent |
| Relative velocity, recoil and continuous mass transfer | Week 6 Lessons 18–19 | Lecture 8 (chapter "The Rocket Equation") | [14](modules/14-variable-mass-momentum-and-mass-flow.md) | Covered |
| Work, kinetic energy, conservative forces, potential energy and energy conservation | Weeks 7–8 Lessons 20–25 | Lectures 5–6 | [2](modules/02-work-energy-and-power.md), [11](modules/11-oscillations-damping-and-energy-balance.md), [15](modules/15-universal-gravitation-circular-orbits-and-orbital-energy.md) | Covered |
| Collisions and the center-of-mass frame | Week 9 Lessons 26–27 and deep dive | Lecture 8 (chapter "Elastic and Inelastic Collisions") | [3](modules/03-momentum-collisions-and-impulse.md), [9](modules/09-work-momentum-and-system-boundaries.md), [22](modules/22-center-of-mass-parallel-axes-and-system-energy.md) | Covered; the center-of-mass frame was added in 0.7.0 |
| Rigid-body rotation, moment of inertia and torque | Week 10 Lessons 28–31 | Lectures 9–11 | [4](modules/04-rotation-torque-and-material-response.md), [6](modules/06-centrifuge-rotation-and-balance.md), [10](modules/10-torque-angular-momentum-and-rolling.md) | Covered |
| Parallel-axis theorem | Week 10 Lesson 29 (sub-lesson 29.6, derivation) | Lecture 10 (title and first chapter) | [22](modules/22-center-of-mass-parallel-axes-and-system-energy.md) | Covered in 0.7.0; previously absent |
| Angular momentum | Week 11 Lessons 32–34 | Lecture 10 | [10](modules/10-torque-angular-momentum-and-rolling.md) | Covered |
| Rolling kinematics, dynamics and energy | Week 12 Lessons 35–37 | Lecture 10 (chapters on kinetic energy of a system and no-skid rolling) | [10](modules/10-torque-angular-momentum-and-rolling.md), [17](modules/sliding-to-rolling-and-contact-power.md), [22](modules/22-center-of-mass-parallel-axes-and-system-energy.md) | Covered; the translation-plus-spin energy split was added in 0.7.0 |
| Gyroscopes | Week 12 deep dive | — | — | Absent; named only by MIT |
| Kepler's laws and gravitation | Lesson 5 (gravity) | Lecture 7 | [15](modules/15-universal-gravitation-circular-orbits-and-orbital-energy.md) | Covered |
| Simple harmonic motion | — | Lectures 17–18 | [11](modules/11-oscillations-damping-and-energy-balance.md) | Covered; named only by Yale |
| Waves | — | Lecture 18 (introduction) | — | Absent; named only by Yale |
| Fluid statics and Bernoulli's equation | — | Lecture 20 | — | Absent; named only by Yale |
| Thermodynamics | — | Lectures 21–24 | — | Elsewhere: the Thermodynamics & Transport course |
| Special relativity | — | Lectures 12–15 | — | Outside this package's boundary |
| Stress, strain, machine compliance and calibration | — | — | [12](modules/12-stress-strain-orientation-and-time-dependence.md), [13](modules/13-machine-compliance-calibration-and-model-inference.md), [lab](labs/01-machine-compliance-and-orientation.md) | Local extension |
| Exams | Three midterms and a final | A midterm and a final | — | Absent by policy: all practice is formative-only |

## What 0.7.0 changed

Two strands were named by both comparators and missing locally: the center of mass, taught in MIT Week 5 Lesson 17 and Yale Lecture 8, and the parallel-axis theorem, taught in MIT Week 10 Lesson 29 and Yale Lecture 10. A new week-8 reading follows the torque, angular-momentum and rolling lesson. It develops the center of mass for discrete and one-dimensional continuous systems, the motion of the center of mass under external force, the split of kinetic energy into center-of-mass and relative parts with its use in collisions, moments of inertia of rods and disks, a derivation of the parallel-axis theorem, and the translation-plus-spin energy of rolling and swinging bodies, with a pivoted-rod worked example. It adds three objectives, 13 practice items and four retrieval cards.

## Remaining gaps

- Resistive forces and gyroscopes, each named only by MIT 8.01SC.
- Waves and fluid statics with Bernoulli's equation, each named only by Yale PHYS 200.
- Graded homework and exams, measured workload, and review by a qualified person.
