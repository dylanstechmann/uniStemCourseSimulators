# Signals, Systems & Feedback Control

**Maturity: partial. Version: 0.4.9.**

Continuous and discrete signals, linear systems, frequency response, feedback, stability, and controller design for sensors, actuators, and biological regulation.

## Prerequisites

Differential Equations; Linear Algebra; Circuits recommended. Structured required, recommended, and concurrent relationships appear in the manifest and remain subject to author review. This package establishes no university prerequisite equivalency.

## Authored outcomes

- Model systems with transfer functions or state space.
- Interpret poles, zeros, and frequency response.
- Evaluate closed-loop stability and tracking.
- Tune feedback with attention to noise, saturation, and uncertainty.

## Proposed 14-week schedule

This is a proposed scope, not a measured or reviewed semester. Week 13 now links a first-order difference equation to its impulse response, Z-transform and discrete pole stability before the existing sampled-PI lesson. The four prototype readings in weeks 1, 4, 8 and 12 also have expanded instruction, and every lesson has public formative items and retrieval cards. See the [scope crosswalk](scope-crosswalk.md) for the boundary against MIT OCW 6.003 and 2.004.

| Week | Theme | Readings |
|---|---|---|
| 1 | LTI systems, convolution and transfer functions | LTI systems, convolution, and transfer functions |
| 2 | Convolution and impulse response: why a sensor blurs and delays what it measures | Convolution and impulse response: why a sensor blurs and delays what it measures |
| 3 | From a transfer function to a time response: poles, zeros and the final value | From a transfer function to a time response: Laplace transforms, poles, zeros and the final value |
| 4 | Frequency response and filtering | Frequency response and filtering |
| 5 | Second-order systems and impedance models | Second-order systems: damping, overshoot and ringing in a pressure transducer; From components to transfer functions: impedance models of electrical, mechanical and thermal plants |
| 6 | Reading Bode plots: decibels, phase and the cost of a delay | Reading Bode plots: gain in decibels, phase, corner frequencies and the cost of a delay |
| 7 | Proportional control of an incubator: steady-state error and saturation | Holding a culture at 37 °C: first-order plants, proportional control, steady-state error and saturation |
| 8 | Feedback, stability, Routh–Hurwitz and the root locus | Feedback, stability, and robustness; Closed-loop poles as the gain changes: Routh–Hurwitz and the root locus |
| 9 | Stability margins: gain, phase and delay margins | Stability margins: gain margin, phase margin and how much delay a loop can take |
| 10 | PI control, tuning and integrator windup | PI control, tuning and integrator windup: removing steady-state error without losing the margin |
| 11 | Virtual lab: identifying an incubator from step tests and checking a PI design | Virtual lab 1: identifying an incubator from step tests and checking a PI design |
| 12 | Controller design and sampled implementation | Controller design and sampled implementation |
| 13 | Discrete-time dynamics, Z-transform, and sampled PI control | Difference equations, the Z-transform, and discrete pole stability; sampling, aliasing, and a discrete-time PI controller |
| 14 | When a sensor filter makes a fast loop oscillate: phase lag, crossover and a safe retuning sequence | When a sensor filter makes a fast loop oscillate: phase lag, crossover and a safe retuning sequence |

## Assessment and study policy

Every lesson has public formative items (numeric, single-choice, multiple-select, data-interpretation, structured-response and CSV-upload) mapped to its objectives, plus retrieval cards for the review queue; each practice assessment also lists the course outcomes its items assess. Week 11 is a synthetic-data virtual lab and week 14 pairs a retuning lesson with the course case and its self-assessment checklist. These are practice activities with unlimited retries and no institutional grade, university credit or transferable credit. Workload has not been measured.

## Inactive integrative project draft

The [sampled-loop design portfolio](assessment-specs/sampled-loop-project-draft.md) combines aliasing, pre-sampling attenuation, hold phase cost, a sample-period bound, a saturated discrete PI update and the exact sampled plant. It is a calculation-only draft, distinct from the step-identification lab and week-14 filter-retuning lesson. It is not scheduled, submitted or graded and is not guidance for any real device.

## Current limitations

The schedule above is proposed, not measured, and has not been reviewed by a qualified instructor. There are no graded homework sets, midterm or final; the new project is inactive and ungraded. The discrete-time addition is a first-order foundation and does not cover the full Fourier, discrete-frequency-response or transform scope of MIT 6.003. The four original prototype readings now have expanded instruction, while the package remains incomplete and unreviewed. The package cites no new papers: the lessons teach standard methods with synthetic data, and the typical values they quote (tuning rules, margin targets, damping ratios, sampling rules of thumb) are textbook-level and vary between sources. All plants, signals, controllers and numbers are synthetic; no lesson gives controller settings, a safety procedure or a test protocol for any real device, and nothing here says anything about any real incubator, instrument or process. Qualified human review is required before this course could meet the complete-course standard.

The title reflects a selected combination of signals/systems and feedback-control topics; the course does not replace MIT OCW 6.003 or 2.004. Week 8 now adds Routh–Hurwitz gain limits and root-locus sketching for proportional control, following the 2.004 lecture order; compensator design on the locus is not developed. Week 5 now derives first- and second-order models from electrical, translational-mechanical and thermal impedances. Fourier analysis, rotational and two-port component modeling, operational amplifiers and hands-on lab implementation remain outside its developed sequence.

## Sources and licensing

Read source-map.json for module provenance and content/SOURCES_AND_LICENSES.md for the software/content license boundary. The discrete-time primer and course boundary were compared with MIT OCW 6.003 (Fall 2011) and 2.004 Dynamics and Control II (Spring 2008); no source asset was imported. Listed source courses are public curriculum comparators; no affiliation or equivalency is implied.
