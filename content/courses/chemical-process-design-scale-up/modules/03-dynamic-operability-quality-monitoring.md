**Status:** Original, explicitly partial advanced university/industry survey material; unreviewed and formative-only. All species, equipment, records, values and organizations are synthetic and fictional. This is a paper design-review exercise, not an operating, fabrication, safety, validation or release instruction.

# Dynamic operability, control separation and operations quality

## Learning objectives

- Interpret sensor, actuator, transport and delay evidence through a bounded FOPDT model and saturated PID arithmetic.
- Distinguish ratio, feedforward and override concepts while separating basic control, alarms and independent protective functions.
- Evaluate SPC, autocorrelation, PAT and deviation/OOS/OOT/CAPA records without inventing independence or acceptance evidence.

## Dynamic operability is more than steady-state gain

A steady flowsheet can close while the process remains difficult to observe or control. Dynamic review asks what changes, how quickly it changes, what can be measured, what can be manipulated and which constraints interact. Sensors add calibration, range, response, location and maintenance questions. Actuators add capacity, resolution, stiction, saturation and failure-state questions. Transport and mixing introduce delay and attenuation. A single nominal model does not cover all operating regimes, so uncertainty and model invalidation criteria belong in the review.

The synthetic first-order-plus-dead-time (FOPDT) representation is Y′(s)/U(s)=K exp(−Ls)/(τs+1). K maps a sustained input change to an output change under local linear assumptions, τ summarizes the first-order response and L is an apparent delay. If output changes from 12 to 18 model units while input changes from 5 to 8 command units, K=(18−12)/(8−5)=2. That estimate depends on steady endpoints and a declared local model. It does not identify a universal process gain, validate a fit or supply tuning. Residual structure, changing operating point and unmeasured disturbances can make an attractive fit misleading.

## PID arithmetic, saturation and windup

PID concepts separate proportional response to present error, integral accumulation of past error and derivative response to a selected measurement or error trend. Real implementations also need filtering, sample timing, output limits, mode transitions and anti-windup logic. This course provides no tuning recipe, controller download or production setting. A small arithmetic example illustrates saturation only: a fictional requested command is 20+3(9−4)=35, inside declared model limits 0 to 40, so the applied command is 35. An alternate request above the upper limit would be clipped, and the integrated state must not continue accumulating as though the extra command had acted.

Saturation changes the information available for identification and can hide demand that the actuator cannot deliver. Ratio control coordinates two model variables but inherits scaling and measurement errors. Feedforward acts on a measured disturbance and requires a causal model; it does not remove the need for feedback or protect against an unmeasured disturbance. Override or selector logic mediates competing constraints, but its selection, tracking and transition behavior require dynamic review. None of these conceptual blocks establishes a safe automation design.

## Alarms, control and interlocks have distinct claims

Basic process control supports a declared operating objective. An alarm communicates a condition requiring awareness or response within a defined philosophy. An interlock or protective function makes a separate risk-reduction claim and needs independent hazard evidence, design authority, testing and management of change. A value displayed by the control system is not automatically an independent protection layer. Shared sensors, logic, power, communications or human response can create common-cause dependence.

This package supplies no bypass, isolation, startup, shutdown or emergency procedure. It asks reviewers to document claim ownership, evidence and dependencies instead. Alarm floods, inconsistent prioritization, unclear response ownership and suppressed indications are human-factors concerns. An override cannot be used as a quiet way around unresolved protective evidence.

## Process monitoring and SPC

Statistical process control distinguishes common-cause variation from signals that may justify investigation. Rational subgrouping determines what variation is being summarized. Control limits are not specification limits, and process stability does not imply product or process acceptability. Capability arithmetic is meaningless for an unstable or improperly pooled record. Time order must be preserved because trends, shifts and autocorrelation violate naïve independent-sample interpretations.

Repeated instrument records within a scenario are correlated and descriptive, not independent replicates. For residuals [1,−1,1,−1] with mean zero, lag-one autocorrelation is

r₁ = [(1)(−1)+(−1)(1)+(1)(−1)]/(1²+1²+1²+1²) = −3/4 = −0.75.

This descriptive statistic does not prove periodic behavior or establish a time-series model. Reused scenario rows must not be pooled into a larger nominal sample size. Missing residuals remain unknown; they are not zero-filled. NIST/SEMATECH provides link-only scope for control charts, capability and time-series models, not an acceptance-sampling plan for this package.

## PAT, deviation, OOS and OOT

Process analytical technology (PAT) is treated as a measurement and knowledge framework: what attribute is inferred, what the instrument measures directly, how the inference model was developed, and where it is valid. A spectra-like or sensor-derived surrogate is not the attribute itself. Calibration transfer, reference-method error, sampling representativeness and model maintenance remain evidence needs. No PAT instrument configuration or release test is supplied.

A deviation records departure from an approved expectation. Out-of-specification (OOS) concerns a declared specification result; out-of-trend (OOT) concerns a trend rule or historical expectation. These categories can overlap but are not interchangeable. Investigation preserves original records, assesses measurement and process causes, avoids testing into compliance and assigns qualified quality review. This course grants no regulated batch disposition.

Corrective and preventive action (CAPA) links root-cause evidence, action ownership, due dates, implementation and effectiveness verification. Closing a task is not proving effectiveness. Continued verification asks whether the process remains in a state of control as new evidence, changes and drift appear. If nine of twelve CAPA packages are verified effective, the 75% ratio is descriptive only; three unresolved packages cannot be treated as closed or zero risk.

## Measurement and application links

The owner’s open-perfusion-rig and perfusion-calibration-lab repositories are link-only examples of the distinction between modeled actuation, measured delivery, repeated readings and independent runs. They are personal hobby and learning projects. No firmware, calibration equation, dataset or validation claim is copied. Their application context does not establish this synthetic FOPDT or quality model.

## Common mistakes

- Estimating gain from unsteady or saturated data and treating FOPDT as universally valid.
- Calling a control-loop alarm an independent interlock or crediting shared components twice.
- Treating repeated readings as new process units, control limits as specifications or CAPA closure as effectiveness.
- Assigning OOS/OOT or batch disposition without the required quality evidence and authority.

## Scope and sources

Existing control and statistics records are reused as accurate prerequisite links. NIST/SEMATECH process monitoring/control is link-only. FDA’s January 2011 Process Validation: General Principles and Practices page is linked for lifecycle and continued-verification context; this course does not perform process validation or commercial release. All examples are synthetic and formative, with no controller, operating or acceptance settings.
