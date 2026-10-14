# Failure criteria, fatigue, and design margins

“Failure” is not one physical event. A part can begin to deform permanently, fracture, crack after repeated loading, become too flexible, leak, or stop performing a required biological or mechanical function. A calculation is meaningful only after the criterion has been stated: what response is limited, under which load history and boundary conditions, and using what material property or allowable. This reading organizes those choices and practices one simple capacity-to-demand ratio. It does not select a criterion for a real component.

## Define the event before calculating a margin

For a ductile material under a single monotonic load, a yield criterion may limit the stress or equivalent stress at the onset of permanent deformation. Yield does not mean that the part has separated; it means the response is no longer wholly recoverable under the chosen material model. The reported yield strength depends on a specified test convention and material condition. A design that permits some permanent set may choose a different requirement, but it must say so.

Ultimate strength describes a different point in a tensile test: the maximum engineering stress reached on the recorded engineering stress–strain curve. A fracture criterion can instead be controlled by crack growth, flaw size, constraint, or a fracture-toughness description. For a brittle material, a small flaw can be important before any ductile yielding redistributes stress. The words “yield strength,” “ultimate strength,” and “fracture limit” therefore cannot be exchanged as if they were the same capacity. A stated load state and failure mechanism determine which one is relevant to a model.

Fatigue concerns damage during repeated or fluctuating loading. A component may accumulate cracks even when every cycle's peak nominal stress is below the monotonic yield strength. A fatigue assessment depends on cycle count, amplitude, mean stress, environment, surface condition, defects, and the test or life model used. The later fatigue lesson develops S–N relations and cumulative-damage estimates; neither a single static factor nor one nominal stress answers a fatigue-life question. Run-outs and scatter also matter: a specimen that survived a finite test has not demonstrated infinite life.

Functional failure is defined by a requirement on what the device must do. Excessive deflection can misalign a mechanism; loss of stiffness can change load sharing; a crack-free channel can still fail if it leaks or loses flow; a support can fail its intended role without material fracture. Biological or clinical performance is a separate evidence question. This mechanics package can name these outcomes, but it cannot establish that a real implant, scaffold, fixture, or tissue interface is acceptable.

## A capacity-to-demand factor

After defining the criterion, write the capacity and demand in matching terms. A simple factor is

**n = R_capacity/R_demand.**

The numerator and denominator must refer to the same quantity, units, location or system level, load case, and failure mode. If the criterion is stress, divide a stress capacity by the modeled stress demand; if it is a load limit, compare loads. A ratio greater than one means the stated capacity exceeds the stated demand in this simplified comparison. It does not identify which uncertainties were included, and a ratio below one indicates that this chosen criterion is exceeded under the stated model.

For example, if a part has a specified allowable stress of 120 MPa and a calculated maximum stress of 40 MPa under the matching criterion, the ratio is 120/40 = 3. Likewise, a member with a 250 MPa yield strength and a working stress of 100 MPa has a simple yield-strength-to-demand ratio of 250/100 = 2.5. These examples preserve the arithmetic used in the practice items. A third load example gives the same arithmetic: a stated capacity of 900 N divided by a modeled demand of 300 N is 3. Units cancel, but only because both quantities are loads in the same model.

Terminology must be explicit. Some engineering standards define an allowable stress after applying one or more design factors to a measured strength. If that pre-factored allowable is the numerator, dividing by the demand describes remaining ratio to that allowable; applying another factor without explaining the convention can double-count a margin. Conversely, a ratio of yield strength to working stress is a strength-to-demand factor only for the stated yield criterion. State whether the numerator is a measured strength, an allowable that already incorporates factors, or another capacity limit. The exercise's label “factor of safety” does not erase that distinction.

## What the ratio does not tell you

A factor of safety is not a probability of survival. A ratio of 3 does not mean a 1-in-3, 1-in-3,000, or any other probability of failure. A probability claim needs distributions for loads, strengths, defects, environments, and model error, plus assumptions about dependence and time. A deterministic ratio can still be useful for transparent screening, but it is not a substitute for reliability analysis or validation.

The ratio also inherits the limits of its capacity and demand estimates. Geometry may vary; material properties scatter; loads may be misestimated; surface damage, corrosion, sterilization, hydration, temperature, and interfaces may alter response; a stress concentration or local defect may not appear in a nominal beam or axial formula. For cyclic service, the count and sequence of loads matter. For buckling, the support conditions and slenderness matter. For combined stresses, a stated multiaxial failure criterion is needed. Later lessons address these cases with their own models; do not turn a static strength ratio into an answer to all of them.

## A disciplined sequence

1. State the function and the event that counts as failure: yield, ultimate strength, fracture, fatigue, instability, excessive deformation, or another explicit limit.
2. State the load history, boundary conditions, location, and model used to compute demand.
3. Identify the capacity source and whether it is a strength, a pre-factored allowable, or a functional threshold. Keep units and definitions aligned.
4. Calculate the ratio, show the units cancel where appropriate, and say what conclusion follows only under the chosen model.
5. List major omitted uncertainties and evidence needed before interpreting the result beyond a classroom calculation.

This sequence makes an assumption visible rather than hiding it behind a single number. All examples in this course are synthetic formative exercises. No value here is a design allowable or safety advice, and the package supplies no test protocol, certification basis, reliability estimate, or clinical evidence.

## Reference

MIT OpenCourseWare, **2.001 Mechanics & Materials I**, Fall 2006, lecture notes including “Failure of Materials and Examples.” The course lecture-notes page is a link-only technical reference; this reading does not copy or adapt its notes, wording, illustrations, exercises, or other assets.
