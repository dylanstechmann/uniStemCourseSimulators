# Signals, Systems & Feedback Control

**Maturity: partial. Version: 0.6.0.**

Continuous and discrete signals, linear systems, frequency response, feedback, stability, and controller design for sensors, actuators, and biological regulation.

## Prerequisites

Differential Equations; Linear Algebra; Circuits recommended. Structured required, recommended, and concurrent relationships appear in the manifest and remain subject to author review. This package establishes no university prerequisite equivalency.

## Authored outcomes

- Model systems with transfer functions or state space.
- Interpret poles, zeros, and frequency response.
- Evaluate closed-loop stability and tracking.
- Tune feedback with attention to noise, saturation, and uncertainty.
- Compute selected continuous and discrete Fourier representations and verify convolution, phase and complete energy relationships.
- Assess controllability, observability and internal modes and construct selected state-feedback and observer models with explicit reference and implementation assumptions.

## Proposed 14-week schedule

This is a proposed scope, not a measured or reviewed semester. Week 13 now links a first-order difference equation to its impulse response, Z-transform and discrete pole stability before the existing sampled-PI lesson. The four prototype readings in weeks 1, 4, 8 and 12 also have expanded instruction, and every lesson has public formative items and retrieval cards. See the [scope crosswalk](scope-crosswalk.md) for the boundary against MIT OCW 6.003 and 2.004.

| Week | Readings and activities | Practice items | Cards |
| --- | --- | ---: | ---: |
| 1 | [LTI systems, convolution, and transfer functions](modules/01-lti-systems-convolution-and-transfer-functions.md) | 2 | 2 |
| 2 | [Convolution and impulse response: why a sensor blurs and delays what it measures](modules/06-convolution-and-sensor-impulse-response.md) | 6 | 4 |
| 3 | [From a transfer function to a time response: Laplace transforms, poles, zeros and the final value](modules/07-laplace-transforms-poles-zeros-and-the-final-value.md) | 8 | 4 |
| 4 | [Frequency response and filtering](modules/02-frequency-response-and-filtering.md); [Fourier representations and energy ledgers](modules/fourier-representations-and-energy-ledgers.md) | 6 | 6 |
| 5 | [Second-order systems: damping, overshoot and ringing in a pressure transducer](modules/08-second-order-systems-damping-and-overshoot.md); [From components to transfer functions: impedance models of electrical, mechanical and thermal plants](modules/16-impedance-models-of-electrical-mechanical-and-thermal-plants.md) | 21 | 8 |
| 6 | [Reading Bode plots: gain in decibels, phase, corner frequencies and the cost of a delay](modules/09-bode-plots-decibels-phase-and-delay.md); [Assignment 1: transform and energy evidence](assignments/coursework-01-transform-and-energy-evidence.md) | 11 | 6 |
| 7 | [Holding a culture at 37 °C: first-order plants, proportional control, steady-state error and saturation](modules/05-proportional-control-of-an-incubator.md); [State feedback, observation and hidden modes](modules/state-feedback-observation-and-hidden-modes.md) | 10 | 8 |
| 8 | [Feedback, stability, and robustness](modules/03-feedback-stability-and-robustness.md); [Closed-loop poles as the gain changes: Routh–Hurwitz and the root locus](modules/15-routh-hurwitz-and-the-root-locus.md); [Proper lead compensation and pole design](modules/proper-lead-compensation-and-pole-design.md) | 17 | 10 |
| 9 | [Stability margins: gain margin, phase margin and how much delay a loop can take](modules/10-stability-margins-gain-phase-and-delay.md) | 9 | 4 |
| 10 | [PI control, tuning and integrator windup: removing steady-state error without losing the margin](modules/11-pi-control-tuning-and-integrator-windup.md); [Assignment 2: compensation and model evidence](assignments/coursework-02-compensation-and-model-evidence.md) | 11 | 6 |
| 11 | [Virtual lab 1: identifying an incubator from step tests and checking a PI design](labs/01-identifying-an-incubator-from-step-tests.md) | 9 | 4 |
| 12 | [Controller design and sampled implementation](modules/04-controller-design-and-sampled-implementation.md); [Assignment 3: state and observer evidence](assignments/coursework-03-state-and-observer-evidence.md) | 4 | 4 |
| 13 | [Difference equations, the Z-transform, and discrete pole stability](modules/14-difference-equations-z-transform-and-pole-stability.md); [Sampling, aliasing and a discrete-time PI controller](modules/12-sampling-aliasing-and-discrete-pi-control.md); [Sampled-loop portfolio project guide (optional, ungraded)](assignments/sampled-loop-project-guide.md); [Exact sampled PI states and Schur stability](modules/exact-sampled-pi-states-and-schur-stability.md) | 26 | 17 |
| 14 | [When a sensor filter makes a fast loop oscillate: phase lag, crossover and a safe retuning sequence](modules/13-sensor-filter-phase-lag-and-safe-retuning.md); [Assignment 4: sampled stability and implementation](assignments/coursework-04-sampled-stability-and-implementation.md) | 11 | 6 |

## Assessment and study policy

Current practice inventory: 26 lesson/activity routes, 151 public practice items, 89 retrieval cards and 6 Case studio prompts, including five project milestones. Counts do not measure semester depth or independently reviewed quality.

Every lesson has public formative items (numeric, single-choice, multiple-select, data-interpretation, structured-response and CSV-upload) mapped to its objectives, plus retrieval cards for the review queue; each practice assessment also lists the course outcomes its items assess. Week 11 is a synthetic-data virtual lab and week 14 pairs a retuning lesson with the course case and its self-assessment checklist. These are practice activities with unlimited retries and no institutional grade, university credit or transferable credit. Workload has not been measured.

## Connected coursework (open, ungraded)

Four original foundations derive continuous/discrete Fourier and energy (week 4), two-state feedback/observation and hidden modes (week 7), proper lead polynomial design (week 8), and an exact specified sampled PI/Schur proof (week 13). Four reports require signed-pulse/discrete transform evidence (week 6), compensation/model comparison (week 10), state/observer evidence (week 12), and repeated-pole/update/stability implementation analysis (week 14). Twenty-four checkpoints/cards assess selected values and interpretations. Continuous fields request three significant figures in named normalized units; exact ranks have no precision penalty. Retain proofs, plots, code and full reports locally; they are not automatically evaluated. The step-identification lab and sampled-loop project remain available. Counts and proposed scheduling do not establish semester depth or measured workload.

## Optional sampled-loop portfolio project (ungraded)

The [sampled-loop portfolio project guide](assignments/sampled-loop-project-guide.md) makes the planned project usable as open practice. Week 13 includes the guide, a separate worked example and five rehearsal items; Five Case studio milestones save private self-check responses without submission or grading. The inactive review draft below remains separate.

## Inactive integrative project draft

The [sampled-loop design portfolio](assessment-specs/sampled-loop-project-draft.md) combines aliasing, pre-sampling attenuation, hold phase cost, a sample-period bound, a saturated discrete PI update and the exact sampled plant. It is a calculation-only draft, distinct from the step-identification lab and week-14 filter-retuning lesson. It is not scheduled, submitted or graded and is not guidance for any real device.

## Current limitations

The schedule above is proposed, not measured, and has not been reviewed by a qualified instructor. There are no graded homework sets, midterm or final; the new project is inactive and ungraded. The original discrete-time primer is first order; selected Fourier/discrete-frequency and exact two-state PI/Schur foundations now extend it, but general transform/modulation/quantization and digital synthesis remain incomplete. The four original prototype readings now have expanded instruction, while the package remains incomplete and unreviewed. The package cites no new papers: the lessons teach standard methods with synthetic data, and the typical values they quote (tuning rules, margin targets, damping ratios, sampling rules of thumb) are textbook-level and vary between sources. All plants, signals, controllers and numbers are synthetic; no lesson gives controller settings, a safety procedure or a test protocol for any real device, and nothing here says anything about any real incubator, instrument or process. Qualified human review is required before this course could meet the complete-course standard.

The title reflects a selected combination of signals/systems and feedback-control topics; the course does not replace MIT OCW 6.003 or 2.004. Week 8 now adds Routh–Hurwitz gain limits and root-locus sketching for proportional control, following the 2.004 lecture order; a proper lead coefficient-matching companion now develops one selected dynamic-compensation family. Week 5 now derives first- and second-order models from electrical, translational-mechanical and thermal impedances. Selected continuous/discrete Fourier and energy calculations and two-state feedback/observer design are now developed. General Fourier theory, rotational/two-port component modeling, operational amplifiers, broad robust/noisy synthesis and hands-on lab implementation remain outside this bounded sequence.

## Sources and licensing

Read source-map.json for module provenance and content/SOURCES_AND_LICENSES.md for the software/content license boundary. The discrete-time primer and course boundary were compared with MIT OCW 6.003 (Fall 2011) and 2.004 Dynamics and Control II (Spring 2008); no source asset was imported. Listed source courses are public curriculum comparators; no affiliation or equivalency is implied.

The 0.6.0 expansion compares actual convolution, Laplace, proportional root-locus and first-order sampled readings with [6.003 Fall 2011 calendar](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/pages/calendar/) Fourier/discrete/sampling lectures 14–22 and [2.004 Spring 2008 calendar](https://ocw.mit.edu/courses/2-004-dynamics-and-control-ii-spring-2008/pages/calendar/) root-locus/frequency lectures 25–34. Selected undergraduate [16.30 Fall 2010 lecture topics](https://ocw.mit.edu/courses/16-30-feedback-control-systems-fall-2010/pages/lecture-notes/) 2–4,5–16 and 20 support the bounded classical/state/digital companions. Existing models were covered; explicit Fourier-energy, proper compensator, state-information/observer and coupled sampled-stability derivations were absent or shallow. Local prerequisites differ from 6.003's 6.02,2.004's mechanics/E&M background and 16.30's classical-design/software expectations. Four reports and a synthetic lab do not reproduce their separate homework/exam/lab sequences or complete scope. No source prose, problem, code, figure or data is imported. The title remains a selected signals/control bridge, not three complete MIT courses; qualified review and measured workload remain open.
