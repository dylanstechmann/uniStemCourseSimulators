# Robotics & Mechatronics

**Maturity: partial. Version: 0.4.8.** Personal hobby and learning project with substantial AI assistance; no university equivalence or institutional credit.

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

| Week | Reading | Items | Cards |
|---|---|---:|---:|
| 1 | Frames, rotations, and homogeneous transforms | 3 | 2 |
| 2 | Frames, calibration and position uncertainty | 9 | 4 |
| 3 | Forward and inverse kinematics | 2 | 2 |
| 4 | Positioning a lab robot arm: forward and inverse kinematics of a planar two-link arm and the cost of joint error | 6 | 4 |
| 5 | Jacobians, singularities and force mapping | 9 | 4 |
| 6 | Inverse branches, joint limits and clearance | 9 | 4 |
| 7 | Robot dynamics, actuators, and energy | 3 | 2 |
| 8 | Actuators, gearing and sensing for a lab robot joint: torque budgets, resolution and failure limits | 6 | 4 |
| 9 | Mass matrix, gravity and energy ledgers; Model-based joint control: gravity compensation and computed torque | 20 | 8 |
| 10 | Motor envelope, backlash and sampled feedback | 9 | 4 |
| 11 | Time scaling, clearance and stopping bounds | 9 | 4 |
| 12 | Planning, sensing, and closed-loop execution | 9 | 6 |
| 13 | Sensing residuals and stall-case evidence | 9 | 4 |
| 14 | Virtual lab 1: direction-dependent motion near extension | 8 | 4 |

## Assessment policy

There are 15 readings, 111 public practice items and 56 cards, plus the preserved case. Most newer lessons have six numeric and three conceptual choices; the computed-torque lesson has eight numeric and three conceptual choices. Week 12 adds three contact-model calculations and three conceptual checks; the lab includes eight grouped velocity summaries, inverse-rate and limiter calculations, structured choices and multiple-select interpretation. Eleven numeric items require units; significant figures, dimensions, planner/controller code, diagrams and written diagnoses are not automatically scored. Unlimited retries provide study feedback, not course grades. Outcome links remain provisional.

## Inactive integrative project draft

The [trajectory timing and actuator-margin portfolio](assessment-specs/trajectory-timing-actuator-margin-project-draft.md) compares fictional cubic time scalings against joint-speed, gravity/inertia torque and conditional stopping-clearance limits. It is a paper-only model, is not scheduled or assigned, and establishes no real robot performance or safety.

## Current limitations

No compact prototype readings remain. One data lab is not a laboratory sequence; graded homework and exams remain absent, and the new project draft is inactive and ungraded. Workload and qualified subject/accessibility review are outstanding. The lab uses frozen Jacobians, a common speed limiter and deterministic report variants, without a dynamic robot simulation. Inward and tangent are fixed base x/y direction labels, not exact radial/tangent directions at every bent pose. No physical operation, protective-function validation or standards compliance is established. The preserved case's torque wording requires a dynamic model: finite force mapping does not universally diverge. Its redundancy option requires usable extra degrees of freedom or task relaxation. The package stays partial, unreviewed and formative-only.

## Sources and licensing

MIT OCW [2.12 Introduction to Robotics, Fall 2005](https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/pages/syllabus/) is an undergraduate scope comparator; its calendar explicitly schedules hybrid position-force control (L12) and compliance/end-effector design (L13). The local contact primer adds synthetic spring arithmetic only and does not reproduce MIT course materials. Existing signals and numerical-methods links remain comparators. Five retrieved Modern Robotics supplements by Kevin M. Lynch and Frank C. Park at Northwestern University are link-only references for transforms, singularities, mass matrices, torque control and trajectories. Metadata and relevant description/transcript content were checked directly. No source prose, example, problem, figure or dataset was copied; no new DOI, PMID, NCT or paper link was introduced. Original readings, text map and synthetic CSV are CC BY 4.0 with substantial AI assistance. See source-map.json and content/SOURCES_AND_LICENSES.md for rights and the software/content boundary. Links establish no endorsement or review.
