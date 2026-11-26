# Materials Science scope crosswalk

This crosswalk covers version 0.1.0, an explicitly partial foundational university survey with eight routes grouped into six modules. It was compiled with AI assistance on 2026-11-26 from the local original readings and the two official public comparator pages. It is an **agent-run comparison**, not scientific or engineering review. Topic alignment establishes no equivalence, credit, endorsement, physical validation or material approval.

## Comparator boundaries

[MIT OCW 3.091SC Introduction to Solid State Chemistry, Fall 2010 — syllabus](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/syllabus/) spans atomic/electronic structure, bonding, electronic materials, crystallography and XRD, defects, amorphous materials, reaction kinetics and diffusion, aqueous chemistry, polymers/biochemistry and phase diagrams. It is a chemistry-centered semester sequence. This package links its syllabus only and develops selected materials-science foundations; it neither imports nor reproduces its lectures, assessments, figures or data.

[MIT OCW 3.012 Fundamentals of Materials Science, Fall 2005 — calendar](https://ocw.mit.edu/courses/3-012-fundamentals-of-materials-science-fall-2005/pages/calendar/) combines structure/bonding with thermodynamics, including quantum models, lattices and XRD, free energy and solutions, phase diagrams, polymers and noncrystalline materials. The local survey uses the calendar only to identify breadth and remaining gaps. Advanced quantum and statistical thermodynamics remain deliberately deferred.

Existing `chemistry`, `mechanics` and `biomaterials-materials-3-051j` records provide prerequisite or application links. General Chemistry I supports bonding and composition; Classical Mechanics supports the failure vocabulary; MIT 3.051J supplies a broader material-application comparator. No old mapping is removed and no content is inherited from those records.

## Topic status

**Covered** means an original local reading develops the topic with examples and public practice. **Shallow** means selected foundations are present but substantial depth remains. **Absent/deferred** means deliberately not taught here.

| Topic | Local route and status | Comparator and remaining boundary |
| --- | --- | --- |
| Atomic/electronic models and quantum mechanics | Lesson 1 prerequisite link: **shallow prerequisite only** | MIT 3.091SC and 3.012 develop these extensively. Full atomic models, wave mechanics, band theory and semiconductor devices are **absent/deferred**. |
| Bonding, material classes and functional properties | [Lesson 1](modules/01-bonding-structure-material-classes.md): **covered at introductory level** | Ionic, covalent, metallic and secondary bonding are linked to classes and bounded thermal/electrical calculations. Molecular-orbital depth and broad reaction chemistry are deferred. |
| Crystallography and Miller indices | [Lesson 2](modules/02-crystallography-miller-bragg.md): **covered for notation and cubic geometry** | MIT comparators include broader lattices, symmetry and reciprocal-space ideas. Seven-system/Bravais enumeration, point groups, tensors and advanced structures are shallow or deferred. |
| Bragg XRD and structural inference | Lesson 2 and [lab](labs/materials-characterization-lab.md): **covered for supplied first-order synthetic records** | Learners compute d and cubic a. X-ray generation, Ewald construction, structure factors, refinement, texture and instrument methods are **absent/deferred**. |
| Defects, diffusion and slip | [Lesson 3](modules/03-defects-diffusion-slip-strengthening.md): **covered with idealized models** | Point/line/interface defects, Arrhenius D, steady flux and slip are included. Nonsteady diffusion, detailed dislocation mechanics and mechanism identification are deferred. |
| Strengthening and mechanical trade-offs | Lesson 3: **covered at model level** | Hall–Petch and mechanism comparisons are included. Full constitutive modeling, precipitation evolution and measured structure/property validation remain open. |
| Thermodynamics and binary phase diagrams | [Lesson 4](modules/04-phase-diagrams-transformations-heat-treatment.md): **shallow to covered at tie-line level** | MIT 3.012 includes free energy, solutions, spinodals/binodals and statistical mechanics; those are deferred. Local work covers phase fields and lever-rule mass balance. |
| Transformations and heat-treatment links | Lesson 4: **shallow, conceptual only** | A fictional transformed-fraction model and process–microstructure links are included. Detailed heat treatment and all recipes, cycles and fabrication settings are deliberately excluded. |
| Strength, toughness, creep, fatigue and fracture | [Lesson 5](modules/05-mechanical-environmental-failure.md): **covered at foundational model level** | Stress–strain area, Miner sum and K = Yσ√(πa) are synthetic. Full fatigue/fracture testing, life prediction and structural derivations remain in later/prerequisite mechanics work. |
| Galvanic and localized corrosion | Lesson 5: **covered conceptually** | Galvanic coupling, conditional passivation, pitting and crevice geometry are included. Electrochemical kinetics, testing procedures and real compatibility are deferred. |
| Polymer Mn/Mw/PDI, Tg/Tm and crystallinity | [Lesson 6](modules/06-polymers-ceramics-composites.md): **covered at introductory level** | Distribution calculations and transition distinctions are included. Polymer synthesis, Flory–Huggins theory, detailed crystallization and rheology are deferred. |
| Ceramics, composites and orientation bounds | Lesson 6: **covered at introductory level** | Microstructure/orientation evidence and Voigt–Reuss calculations are included. Ceramic processing, composite manufacturing and full anisotropic elasticity are excluded or deferred. |
| Multi-technique characterization | [Lab](labs/materials-characterization-lab.md): **covered for one synthetic CSV** | Structural, thermal, mass and mechanical channels are reconciled. No real acquisition, calibration experiment, instrument procedure or unique identification is supplied. |
| Constraints-based material selection | [Project](assignments/material-selection-project-guide.md): **covered as zero-point fictional rehearsal** | Hard constraints, specific stiffness, mass, energy and sensitivity are included. Standards, qualification, procurement, manufacturing and approval remain unresolved. |

## Link-only sources by module

| Module | Registered sources and exact use |
| --- | --- |
| 1 | MIT 3.091SC and 3.012 official comparators; existing `chemistry` prerequisite link. No source prose or exercises imported. |
| 2 | MIT 3.091SC syllabus and 3.012 calendar for crystallography/XRD breadth. Every crystal and peak value is newly invented. |
| 3 | Both MIT comparators for defects, kinetics and diffusion context. Fictional parameters are not empirical coefficients. |
| 4 | Both MIT comparators for phase and thermodynamic breadth. Local diagrams are prose-only and no heat-treatment procedure is given. |
| 5 | Existing `mechanics` prerequisite and MIT 3.091SC link. No structural derivation or source failure dataset imported. |
| 6 | Both MIT comparators plus existing `biomaterials-materials-3-051j` application link. Lab/project CSVs are original synthetic files. |

## Remaining gaps

- Quantum mechanics, electronic band theory, semiconductor devices and advanced solid-state chemistry.
- Free-energy and statistical-thermodynamic derivations, nonideal solutions and advanced phase-transform theory.
- Full diffraction physics, pattern refinement, microscopy/spectroscopy theory and validated multi-technique experiments.
- Advanced mechanical constitutive models, fatigue/fracture testing, electrochemical measurements and life prediction.
- Polymer synthesis/rheology, ceramic/composite fabrication and detailed anisotropic design.
- Instrument operation, heat-treatment recipes, fabrication settings, standard-specific compliance and material approval, deliberately excluded.
- Qualified scientific/engineering review, measured workload, independently collected physical data and graded assessment.
