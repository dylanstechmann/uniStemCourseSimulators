# Electrical Circuits & Instrumentation

**Maturity: partial. Version: 0.4.8.** Personal hobby and learning project with substantial AI assistance; no university equivalence or institutional credit.

Original instruction develops nodal/port balances, finite feedback, differential/common-mode errors, filter loading/recovery, noise and uncertainty, acquisition and calibration domains, second-order RLC transients and frequency response, and op-amp summing, integrating, differentiating and active filtering. An original text feedback map includes a verbal description. Preserved sensor-loading/ADC and first-order frequency-response lessons remain.

## Prerequisites

Physics: Electricity & Magnetism; Calculus I recommended. Manifest relationships remain provisional and establish no university prerequisite equivalency.

## Authored outcomes

- Solve DC networks with Kirchhoff and Thevenin methods.
- Analyze first- and second-order transient and sinusoidal frequency response.
- Select an amplifier topology for a sensor signal.
- Quantify noise, loading, and calibration limits.

## Proposed 14-week schedule

This is planning scope, not measured workload or a reviewed semester. Weeks 1, 4, 7 and 12 now have expanded DC-network/Thevenin, amplifier/front-end, filter/sampling and sensor/calibration primers. Week 5 pairs finite feedback with op-amp summing, integrator, differentiator and active-filter stages, and week 8 pairs the preserved first-order RC filter with a second-order RLC unit, keeping the proposed 14-week sequence. Week 14 is a synthetic gain/clipping/common-mode/baseline lab and revisits the preserved movement-clipping/rest-drift case. All activities are public formative practice.

| Week | Reading | Items | Cards |
|---|---|---:|---:|
| 1 | DC network analysis and equivalent circuits | 3 | 2 |
| 2 | Nodal networks, port tests and power | 9 | 4 |
| 3 | Reading a sensor without fooling yourself: voltage dividers, loading error and ADC resolution | 6 | 4 |
| 4 | Operational amplifiers and analog front ends | 2 | 2 |
| 5 | Feedback, finite gain, bias and output range; Op-amp signal operations: summing, integrating, differentiating and active filtering | 22 | 8 |
| 6 | Differential signals, common mode and interface imbalance | 9 | 4 |
| 7 | Filters, sampling, and anti-aliasing | 3 | 2 |
| 8 | First-order RC response; Second-order RLC transients, damping, resonance and impedance | 15 | 8 |
| 9 | Filter loading, baseline and recovery | 9 | 4 |
| 10 | Noise bandwidth, covariance and uncertainty | 9 | 4 |
| 11 | Sampling, quantization and acquisition settling | 9 | 4 |
| 12 | Sensors, calibration, and uncertainty | 2 | 2 |
| 13 | Calibration, clipping, residuals and case evidence | 9 | 4 |
| 14 | Virtual lab 1: gain, clipping, common mode and baseline recovery | 8 | 4 |

## Assessment policy

There are 16 readings, 115 public practice items and 56 retrieval cards, plus the preserved case. Most newer lessons have six numeric and three conceptual choices; the op-amp operations lesson has ten numeric and three conceptual choices. The lab includes CSV summaries, gain/rejection/decay calculations, structured choices and multiple-select interpretation. Twenty numeric items require units; the RLC and op-amp operations calculations state the requested units, while other numeric items use their established answer formats. Significant figures, dimensions, diagrams, written diagnosis and uncertainty arguments are not automatically scored. Unlimited retries provide study feedback, not course grades. Outcome links still need qualified review.

## Inactive design project

An [integrative sensor-channel project draft](assessment-specs/integrative-sensor-channel-project-draft.md) combines loading, gain/headroom, CMRR, RC response, sampling and quantization using stated ideal assumptions. It is not scheduled, submitted or graded, and does not authorize a hardware build. Its synthetic design values and unweighted rubric are for future review only.

## Current limitations

No compact prototype readings remain. One data lab is not a laboratory sequence; graded homework, exams and a cumulative graded project remain absent. Workload, accessibility and circuit quality await review. The lab's known references, hard clamp, valid input range and separately stipulated drift are synthetic assumptions. They establish conditional electrical explanations without unique real interface identification. The preserved Nyquist key is a nominal two-times threshold, not a guarantee of arbitrary-phase recovery at the exact boundary or practical acquisition/filter performance. The package remains partial, unreviewed and formative-only.

## Sources and licensing

MIT OCW [6.002 Circuits and Electronics, Spring 2007 calendar](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/calendar/) is the direct undergraduate comparator for the week-8 addition; it schedules second-order transients (L16), damping (L17), sinusoidal frequency response (L18), impedance (L19), filters and Q (L20), and energy and power (L24). The local RLC unit is original and limited to one ideal series model. Existing MIT signals links remain scope comparators. Retrieved OpenStax Kirchhoff guidance, Texas Instruments op-amp specification guidance, NIST combined-standard-uncertainty guidance and an Analog Devices ADC teaching chapter are link-only references. No teaching prose, problem, figure or dataset was copied. No new DOI, PMID or NCT was introduced; document metadata was checked directly against the retrieved primary sources. Original readings, feedback map and synthetic CSV are CC BY 4.0 with substantial AI assistance. See source-map.json and content/SOURCES_AND_LICENSES.md for rights and the software/content boundary. Links establish no endorsement or review.
