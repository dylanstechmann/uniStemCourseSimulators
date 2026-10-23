# Trajectory-margin portfolio project guide (optional, ungraded)

**Status:** open, optional practice. You can save milestone responses privately in the Case studio; this route is ungraded.
**Introduced in:** course package 0.5.0.
**Suggested time (unvalidated author estimate):** 2–4 hours across weeks 13–14.

## Start here

A timing choice changes velocity, acceleration and the actuator budget together. This project asks for one internally consistent candidate table instead of separate calculations that accidentally use different moves. The scalar stopping screen is deliberately conditional, and the ideal energy ledger answers a different endpoint question. Commands and measured execution remain separate evidence throughout.

Work through the supplied project after the related course readings. First close the model or evidence ledger on paper, then use the separate rehearsal to test your method. The worked example uses different inputs and is a demonstration of the reasoning, not a response to the project. Keep definitions, units, denominators, signs and assumptions visible in your own response. If a check fails, return to the model rather than adjusting a number to match an option.

## Project brief and supplied information

Use q(t) = Δq(3s²−2s³), s = t/T, for a fictional direct-drive joint from q = 0 to q = 1 rad. The [candidate durations](trajectory-timing-candidates.csv) are 0.8, 1.0 and 1.5 s. With Δq = 1 rad, inertia I = 0.20 kg m², point mass m = 2.00 kg, radius r = 0.250 m and g = 9.81 m/s², the stipulated torque is tau = I q_ddot + mgr cos(q). Angle is measured from horizontal and positive motion raises the load. Ignore friction. Limits are 1.00 rad/s speed and 5.50 N m **positive** output torque; no complete motor envelope is supplied.

At a designated checkpoint, assume scalar angular clearance 0.400 rad in the travel direction. The paper stopping screen stipulates latency 0.050 s, guaranteed constant braking magnitude 4.00 rad/s² after latency and separate deterministic position allowance 0.020 rad. Use d_stop = v×latency + v²/(2a) + allowance with the trajectory peak speed. These are invented model inputs, not measured braking or protective-function specifications. Check each candidate and separately solve continuous bounds, then close the ideal energy ledger and describe what a monitoring record would still need.

## Milestones and self-review

### Milestone 1: Differentiate the time scaling

Differentiate the project’s cubic move through Δq = 1 rad and derive bounds as functions of T before substituting the candidate durations. Identify the normalized times where speed and absolute acceleration reach their maxima.

- Differentiates with the t-to-s chain factor at each order.
- Finds the interior speed maximum and endpoint acceleration extrema.
- Keeps zero velocity distinct from zero acceleration at a join.

### Milestone 2: Gravity and actuator torque

For each project duration, evaluate tau = I q_ddot + mgr cos(q) using I = 0.20 kg m², m = 2.00 kg and r = 0.250 m. Explain the positive torque maximum over 0≤q≤1 rad and screen the stated 5.50 N m positive limit.

- Uses the horizontal angle reference and raising-positive sign.
- Includes inertia and gravity with compatible torque units.
- Checks the actual stated positive limit without inventing a missing actuator envelope.

### Milestone 3: Conditional stopping screen

For each project peak speed, compute d_stop = v×0.050 + v²/(2×4.00) + 0.020 rad and the reserve against 0.400 rad. Separate latency travel, braking travel and position allowance, then list the assumptions needed by this scalar screen.

- Reports all three allowance terms on the same angular basis.
- Checks clearance with a sign convention for reserve.
- Does not convert a conditional paper margin into a validated protective function.

### Milestone 4: Choose timing under all constraints

Screen the project candidates 0.8, 1.0 and 1.5 s against speed, positive torque and scalar stopping limits. Separately solve the continuous lower bound from each constraint and identify which one controls, without assuming the shortest candidate is feasible.

- Displays separate speed, torque and stopping results for each candidate.
- Solves continuous bounds independently of the listed candidate grid.
- Names the binding constraint and distinguishes equality from positive reserve.

### Milestone 5: Energy and a bounded monitoring record

For the project’s one-radian raise, close the ideal kinetic/potential work ledger. Propose a paper-only record keeping commands distinct from measured states, delivered-current information and time. State the cubic endpoint-acceleration issue and the limits of every performance or protective-function claim.

- Accounts for zero net endpoint kinetic-energy change and the potential rise.
- Separates duration-independent work from duration-dependent torque and stopping constraints.
- Keeps command, observation and unvalidated hardware assumptions distinct.

## Worked example: a separate case

Take a different move through 0.4 rad, with I = 0.08 kg m², m = 0.8 kg, r = 0.18 m and g = 9.81 m/s². The gravity coefficient is 1.41264 N m. Compare T = 0.8 and 1.0 s, using speed limit 0.8 rad/s and positive torque limit 1.8 N m. Differentiating the cubic gives peak speed 1.5×0.4/T and peak absolute acceleration 6×0.4/T².

At 0.8 s, speed is 0.75 rad/s and acceleration magnitude is 3.75 rad/s². Start torque is 1.41264 + 0.08×3.75 = 1.71264 N m, so these two screens pass. Now stipulate latency 0.030 s, braking magnitude 2 rad/s², position allowance 0.005 rad and scalar clearance 0.160 rad. The stopping allowance is 0.75×0.030 + 0.75²/(2×2) + 0.005 = 0.168125 rad. It exceeds the clearance by 0.008125 rad. Passing speed and torque did not imply passing the separate stopping model.

At 1.0 s, speed is 0.6 rad/s and acceleration magnitude 2.4 rad/s². Positive torque is 1.60464 N m and stopping allowance is 0.018+0.090+0.005 = 0.113 rad, leaving 0.047 rad under the stipulated screen. This comparison demonstrates why every constraint belongs in the same candidate table rather than being checked against different durations.

With both endpoint speeds zero and no losses, ideal work is 1.41264 sin(0.4) ≈ 0.5501 J for either duration. A second check can integrate tau×q_dot over time: the inertial contribution integrates to the zero endpoint kinetic-energy change and the gravity contribution integrates to the potential rise. The peak rates, however, differ with T. Neither calculation supplies real actuator efficiency, braking validation, backlash, obstacle geometry or an execution measurement. The cubic also reaches its stationary joins with nonzero acceleration, which must not be hidden by its zero endpoint speed.

## Rehearsal: practice before the project

The [rehearsal parameter table](trajectory-margin-rehearsal.csv) defines a different 0.6-rad move: I = 0.12 kg m², m = 1.5 kg, r = 0.20 m and g = 9.81 m/s². Compare durations 0.6, 1.0 and 1.4 s. The declared speed and positive torque limits are 1 rad/s and 3.5 N m. Scalar clearance is 0.25 rad, latency 0.04 s, braking magnitude 3 rad/s² and deterministic position allowance 0.01 rad. Most numeric rehearsal fields ask for the 1.00 s candidate; the timing fields separately ask for the continuous bound and shortest listed feasible duration.

Open **Practice gradebook** and choose **Trajectory-margin portfolio rehearsal**. Each numeric field names its reporting unit. Enter continuous quantities as bare numbers to three significant figures, using scientific notation when trailing zeros would otherwise hide the intended precision; enter exact counts as whole numbers. Keep extra digits in intermediate calculations. Interpretation choices test the declared model and evidence limits; a correct choice does not demonstrate a complete written argument. The public feedback explains each field and permits unlimited retries.

## Finish and check your report

Include the supplied inputs, your equations or evidence map, intermediate quantities with units, a final table with clearly labelled rows and a short interpretation. For every numerical result, include a second check: substitute into the original relation, verify a conservation balance, compare a limiting case or independently recompute it. For evidence interpretations, name the comparison, design, endpoint, uncertainty and the conclusion that remains unsupported. A diagram or plot needs a plain-text description that preserves its scientific meaning; colour alone must not carry a distinction.

Use the Case studio checklist only after finding the corresponding evidence in your response. Marking a box records your own review; it does not score prose, certify mastery or establish an institutional grade. Disclose spreadsheets, code, references and AI assistance so another reader can distinguish your reasoning from external calculations. Keep a copy of your report and review any discrepancy between your calculation and the public rehearsal feedback before moving on.

| Stage | Focus | Where to work |
| --- | --- | --- |
| Rehearsal | Separate synthetic inputs and public feedback | Practice gradebook: Trajectory-margin portfolio rehearsal |
| M1 | Differentiate the time scaling | Case studio: project milestone 1 |
| M2 | Gravity and actuator torque | Case studio: project milestone 2 |
| M3 | Conditional stopping screen | Case studio: project milestone 3 |
| M4 | Choose timing under all constraints | Case studio: project milestone 4 |
| M5 | Energy and a bounded monitoring record | Case studio: project milestone 5 |

## Scope and provenance

Scope comparator: MIT OCW 2.12 Introduction to Robotics, Fall 2005 syllabus and lecture notes, https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/pages/syllabus/ and https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/pages/lecture-notes/. The local actuator, dynamics and time-scaling readings support this single-joint synthesis. Full robot dynamics, configuration-dependent geometry, force/compliance control and physical project/laboratory depth remain beyond the exercise; no hardware performance or protective function is validated.

The original authoring draft remains a separate proposal for future qualified review; this guide supplies an open practice route without activating that draft as a graded assessment. Workload, scientific quality, assessment design and accessibility have not received independent approval. Original guide, synthetic inputs and rehearsal problems: CC BY 4.0, developed with substantial AI assistance as part of this personal hobby and learning project. No third-party prose, exercise, figure or dataset is reproduced.
