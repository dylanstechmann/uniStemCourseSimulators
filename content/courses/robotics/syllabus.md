# Robotics & Mechatronics

**Maturity: partial. Version: 0.6.0.** Personal hobby and learning project with substantial AI assistance; no university equivalence or institutional credit.

Original instruction develops labeled frames and calibration, Jacobian velocity and force mapping, constrained inverse branches, point-mass dynamics and energy, motor and feedback limits, trajectories and conditional stopping bounds, model-based sensing evidence, a quasistatic comparison of position tracking and force regulation in compliant contact, and model-based joint control with gravity compensation and computed torque. Preserved planar-arm and gearbox lessons remain. An original frame text map has a verbal description.

## Prerequisites

Linear Algebra and Differential Equations; Circuits recommended. Manifest relationships are provisional and establish no university prerequisite equivalency.

## Authored outcomes

- Transform coordinates between robot and task frames.
- Solve forward and inverse kinematics for a planar arm.
- Relate actuator torque, gearing, and load.
- Design a sensing and control loop with failure limits.

## Proposed 14-week schedule

This is planning scope, not measured workload or a reviewed semester. Weeks 1, 3, 7 and 12 now have expanded frame-transform, two-link kinematics, rotor/actuator energy, and planning/feedback primers; the other scheduled readings have original instructional text. Week 9 pairs the point-mass dynamic model with gravity compensation and computed-torque control. Week 14 is a synthetic direction-dependent near-extension lab, revisiting the preserved stall case. All activities are public formative practice.

| Week | Readings and activities | Practice items | Cards |
| --- | --- | ---: | ---: |
| 1 | [Frames, rotations, and homogeneous transforms](modules/01-frames-rotations-and-homogeneous-transforms.md) | 3 | 2 |
| 2 | [Frames, calibration and position uncertainty](modules/07-frames-calibration-and-position-uncertainty.md) | 9 | 4 |
| 3 | [Forward and inverse kinematics](modules/02-forward-and-inverse-kinematics.md) | 2 | 2 |
| 4 | [Positioning a lab robot arm: forward and inverse kinematics of a planar two-link arm and the cost of joint error](modules/05-planar-arm-kinematics-and-joint-error.md) | 6 | 4 |
| 5 | [Jacobians, singularities and force mapping](modules/08-jacobians-singularities-and-force-mapping.md) | 9 | 4 |
| 6 | [Inverse branches, joint limits and clearance](modules/09-inverse-branches-joint-limits-and-clearance.md) | 9 | 4 |
| 7 | [Robot dynamics, actuators, and energy](modules/03-robot-dynamics-actuators-and-energy.md); [Distributed links and energy-derived dynamics](modules/distributed-links-and-energy-derived-dynamics.md) | 7 | 6 |
| 8 | [Actuators, gearing and sensing for a lab robot joint: torque budgets, resolution and failure limits](modules/06-joint-torque-budget-and-sensing.md) | 6 | 4 |
| 9 | [Mass matrix, gravity and energy ledgers](modules/10-mass-matrix-gravity-and-energy-ledgers.md); [Model-based joint control: gravity compensation and computed torque](modules/14-gravity-compensation-and-computed-torque-control.md); [Assignment 1: dynamics and work ledgers](assignments/coursework-01-dynamics-and-work-ledgers.md) | 22 | 10 |
| 10 | [Motor envelope, backlash and sampled feedback](modules/11-motor-envelope-backlash-and-sampled-feedback.md); [Workless constraints and signed reactions](modules/workless-constraints-and-signed-reactions.md) | 13 | 8 |
| 11 | [Time scaling, clearance and stopping bounds](modules/12-time-scaling-clearance-and-stopping-bounds.md); [Whole-link clearance between samples](modules/whole-link-clearance-between-samples.md) | 13 | 8 |
| 12 | [Planning, sensing, and closed-loop execution](modules/04-planning-sensing-and-closed-loop-execution.md); [Assignment 2: constraint and release evidence](assignments/coursework-02-constraint-and-release-evidence.md) | 11 | 8 |
| 13 | [Sensing residuals and stall-case evidence](modules/13-sensing-residuals-and-stall-case-evidence.md); [Trajectory-margin portfolio project guide (optional, ungraded)](assignments/trajectory-margin-project-guide.md); [Assignment 3: trajectory clearance evidence](assignments/coursework-03-trajectory-clearance-evidence.md) | 16 | 11 |
| 14 | [Virtual lab 1: direction-dependent motion near extension](labs/01-direction-dependent-motion-near-extension.md); [Assignment 4: control and model boundaries](assignments/coursework-04-control-and-model-boundaries.md) | 10 | 6 |

## Assessment policy

Current practice inventory: 23 lesson/activity routes, 136 public practice items, 81 retrieval cards and 6 Case studio prompts, including five project milestones. Counts do not measure semester depth or independently reviewed quality.

Most newer lessons have six numeric and three conceptual choices; the computed-torque lesson has eight numeric and three conceptual choices. Week 12 adds three contact-model calculations and three conceptual checks; the lab includes eight grouped velocity summaries, inverse-rate and limiter calculations, structured choices and multiple-select interpretation. Eleven numeric items require units; new continuous checkpoints request three significant figures. Dimensions, planner/controller code, diagrams and written diagnoses are not automatically scored. Unlimited retries provide study feedback, not course grades. Outcome links remain provisional.

## Connected coursework (open, ungraded)

Three original foundations derive distributed-link Euler–Lagrange dynamics (week 7), workless constraints and unilateral release (week 10), and whole-link between-sample clearance bounds (week 11). Four reports require periodic dynamics/work evidence (week 9), active/released constraint and curved-boundary checks (week 12), geometry/error/rate certificates (week 13), and clipped computed-torque analysis (week 14). Twenty checkpoints/cards assess selected values and interpretations. Retain diagrams,proofs,code and full reports locally; they are not automatically evaluated. The existing near-extension lab and trajectory project remain available. Counts and proposed scheduling do not establish semester depth or measured workload.

## Optional trajectory-margin portfolio project (ungraded)

The [trajectory-margin portfolio project guide](assignments/trajectory-margin-project-guide.md) makes the planned project usable as open practice. Week 13 includes the guide, a separate worked example and five rehearsal items; Five Case studio milestones save private self-check responses without submission or grading. The inactive review draft below remains separate.

## Inactive integrative project draft

The [trajectory timing and actuator-margin portfolio](assessment-specs/trajectory-timing-actuator-margin-project-draft.md) compares fictional cubic time scalings against joint-speed, gravity/inertia torque and conditional stopping-clearance limits. It is a paper-only model, is not scheduled or assigned, and establishes no real robot performance or safety.

## Current limitations

The first three prototype readings remain concise primers with longer companions;the fourth already has a longer contact treatment. One data lab is not a laboratory sequence; graded homework and exams remain absent, and the new project draft is inactive and ungraded. Workload and qualified subject/accessibility review are outstanding. The lab uses frozen Jacobians, a common speed limiter and deterministic report variants, without a dynamic robot simulation. Inward and tangent are fixed base x/y direction labels, not exact radial/tangent directions at every bent pose. No physical operation, protective-function validation or standards compliance is established. The preserved case's torque wording requires a dynamic model: finite force mapping does not universally diverge. Its redundancy option requires usable extra degrees of freedom or task relaxation. The package stays partial, unreviewed and formative-only.

## Sources and licensing

MIT OCW [2.12 Introduction to Robotics, Fall 2005](https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/pages/syllabus/) is an undergraduate scope comparator; its calendar explicitly schedules hybrid position-force control (L12) and compliance/end-effector design (L13). The local contact primer adds synthetic spring arithmetic only and does not reproduce MIT course materials. Existing signals and numerical-methods links remain comparators. Five retrieved Modern Robotics supplements by Kevin M. Lynch and Frank C. Park at Northwestern University are link-only references for transforms, singularities, mass matrices, torque control and trajectories. Metadata and relevant description/transcript content were checked directly. No source prose, example, problem, figure or dataset was copied; no new DOI, PMID, NCT or paper link was introduced. Original readings, text map and synthetic CSV are CC BY 4.0 with substantial AI assistance. See source-map.json and content/SOURCES_AND_LICENSES.md for rights and the software/content boundary. Links establish no endorsement or review.

The 0.6.0 expansion compares actual point-mass dynamics,computed torque,quasistatic contact and sampled-clearance readings with [MIT OCW 2.12 Fall 2005 syllabus and embedded calendar](https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/pages/syllabus/): hybrid/compliance L12–13,dynamics L17–18,computed torque L19 and navigation L22–23. Existing point-mass/control/segment calculations were covered; distributed center/rotational inertia,acceleration/reaction compatibility and a whole-link continuous certificate were absent or shallow. Selected [Modern Robotics 8.7](https://modernrobotics.northwestern.edu/nu-gm-book-resource/8-7-constrained-dynamics/) and [10.2.1](https://modernrobotics.northwestern.edu/nu-gm-book-resource/10-2-c-space-obstacles/) descriptions/transcripts are link-only concept references. The local Linear Algebra/Differential Equations prerequisites differ from the source's required2.003/2.004 dynamics/control background. Four reports and a synthetic lab do not reproduce its eight problem sets,ten labs,two hardware projects or mid/end exams. Mobile/nonholonomic systems,vision,broad planning/contact algorithms and physical validation remain outside this narrower planar course. No source text,mechanism,figure,path,exercise,code or data is imported; measured workload and qualified review remain open.
