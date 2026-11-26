# Mechanical failure, environmental degradation and fracture links

**Status:** Original reading in partial Materials Science 0.1.0; unreviewed and formative-only. All components, curves, flaws, environments and values are synthetic fictional teaching models. They provide no life prediction, compatibility judgement or approval for real service.

## A vocabulary that separates properties and mechanisms

Failure analysis starts by distinguishing material response from component performance. Stiffness describes resistance to elastic deformation under a defined model; strength concerns an appropriate stress or load criterion; ductility concerns plastic deformation capacity; toughness concerns energy absorption or fracture resistance under a specified measure. Hardness is another measurement and cannot substitute for all four. Geometry and constraints link material properties to component behavior.

Full stress, strain, bending and structural failure derivations belong to Statics & Mechanics of Materials. This route links to that continuation rather than duplicating it. Here a simplified stress–strain area illustrates why strength alone is not toughness. Model a fictional curve as a triangle reaching 200 MPa at strain 0.010, followed by a rectangle at 200 MPa from strain 0.010 to 0.030. The triangle area is 0.5×200×0.010 = 1 MPa and the rectangle is 200×0.020 = 4 MPa. Because MPa times strain equals MJ/m³, total area is **5 MJ/m³**.

That area is only a stipulated toughness proxy. It does not establish impact toughness, fracture toughness or safe energy absorption in another geometry. A brittle high-strength fictional material can have small area despite high maximum stress, while a more ductile comparator can absorb more energy. The loading rate, temperature, notch condition and measurement definition must be stated.

## Creep: time-dependent response

Creep refers to time-dependent deformation under sustained conditions, especially when thermal activation enables mechanisms that are negligible in faster lower-temperature models. A conceptual creep record may show primary, secondary and tertiary regions, but those shapes are not universal. Stress, temperature, microstructure and environment influence rates and transitions.

A strain-rate estimate from two synthetic points is (strain₂ − strain₁)/(time₂ − time₁). Such a secant rate is not automatically a steady-state constitutive parameter. If the record is short, sparse or taken during primary creep, extrapolation can be misleading. Time-dependent strain also says little by itself about remaining rupture life. Evidence must include test conditions, interruptions, measurement uncertainty and microstructural stability.

Creep can interact with fatigue, oxidation and stress relaxation. Treating each as an isolated mechanism because a spreadsheet has separate columns would be an artificial boundary. Conversely, combined language should not hide which observations actually exist. If cycles were not applied, fatigue damage remains unmeasured; if only total strain was recorded, the partition among instantaneous, recoverable and creep strain may remain unknown.

## Fatigue and cyclic-damage models

Fatigue concerns damage evolution under repeated loading. Cracks can initiate and grow at stresses that would not cause immediate monotonic overload. Surface condition, mean stress, stress range, notches, environment and residual stress can matter. Cycle counting is therefore not a complete life model.

The Miner sum is a simple linear damage approximation: D = Σ(nᵢ/Nᵢ), where nᵢ is cycles applied at level i and Nᵢ is modeled cycles to failure at that level. For fictional n₁ = 20,000, N₁ = 100,000, n₂ = 300,000 and N₂ = 1,000,000, D = 0.20 + 0.30 = **0.50**. A conventional classroom interpretation compares the sum with a criterion, but this package does not convert it into a safe-life statement. Sequence effects and variable-amplitude mechanisms can violate simple linear accumulation.

A Miner value below one does not guarantee survival, and a value above one does not locate the physical crack. It is an idealized index derived from inputs whose uncertainty may dominate the answer. Fractography and nondestructive evidence address different questions from the scalar sum.

## Fracture and flaw-sensitive behavior

Linear-elastic fracture models relate stress intensity to applied stress, flaw size and geometry. One simplified form is K = Yσ√(πa), where Y is a geometry factor, σ is remote stress and a is a defined crack-length measure. With fictional Y = 1.12, σ = 150 MPa and a = 0.0020 m, K = 1.12×150×√(π×0.0020) = **13.317… MPa√m**.

This calculation does not prove fracture or safety. Comparison with a fracture-toughness value requires matching validity conditions, orientation, temperature, rate and constraint. Crack shape and location affect Y, and plasticity can invalidate the linear-elastic model. A missing crack measurement is unknown, not zero crack length.

Creep, fatigue and fracture can form a linked sequence: time- and cycle-driven damage can produce or grow a flaw, which then changes stress intensity. The links are hypotheses to test, not a universal timeline. Material microstructure and environment can influence every stage.

## Galvanic and localized corrosion

Corrosion depends on material, environment and geometry together. Galvanic coupling requires electronic contact and an ionic path, with relative areas and kinetics influencing attack. A noble-looking comparison label is not enough to predict a real couple’s behavior. Passive metals can exhibit low general dissolution in some environments because a protective film limits reaction, but passivity is conditional rather than immunity.

Pitting involves localized attack, often associated with film breakdown and local chemistry. Crevice corrosion can develop in shielded regions where solution composition evolves differently from the bulk. Deposits, joints and gaskets can create such geometry. A fictional passive surface attacked beneath a deposit therefore motivates a crevice-corrosion hypothesis, not an automatic diagnosis. Pits and crevices can also create stress concentrators that interact with fatigue or fracture.

A bounded corrosion record includes electrolyte and contact conditions, exposed and shielded geometry, relative areas, film evidence, local observations and time history. No universal “compatible” or “incompatible” label is assigned here. Real selection requires application-specific testing and qualified review.

The existing [MIT Classical Mechanics](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/) record is a prerequisite link only; it does not supply this failure content. The [MIT 3.091SC Fall 2010 syllabus](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/syllabus/) remains a broader link-only materials comparator. No third-party curves, problems or data are imported. Detailed fatigue-curve fitting, elastic–plastic fracture, electrochemical kinetics, corrosion testing procedures and component certification are deferred.
