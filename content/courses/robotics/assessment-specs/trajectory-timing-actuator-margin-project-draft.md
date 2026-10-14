# Trajectory timing and actuator margins: inactive project draft

**Status:** authoring draft only. It is not scheduled, assigned, submitted, collected or graded. The single-joint model, limits and clearances are fictional teaching inputs. This calculation establishes no real robot performance, protective function or safety.

## Stipulated move and limits

A direct-drive fictional joint moves from `q=0` to `q=1 rad` under constant gravity load from a point mass. Use the cubic time scaling `q(t)=q_0+Delta_q(3s^2-2s^3)`, with `s=t/T` and candidate durations `T` from the [candidate table](trajectory-timing-candidates.csv).

Use `Delta_q=1 rad`, `I=0.20 kg m²`, `m=2.00 kg`, `r=0.250 m`, and `g=9.81 m/s²`. The angle is measured from horizontal, positive motion raises the load, and the declared actuator torque is `tau=I q_ddot + m g r cos(q)`. Ignore friction and assume the motor limit is already stated at the joint output. Its stipulated speed limit is `1.00 rad/s`, and its positive torque limit is `5.50 N m`.

At a designated checkpoint near the peak-speed portion of the move, assume the one-dimensional model grants `0.400 rad` of clearance in the direction of travel. For this paper screen only, use latency `ell=0.050 s`, guaranteed constant braking magnitude `a=4.00 rad/s²` after latency, and a separate deterministic position allowance `delta=0.020 rad`. Calculate the conditional stopping allowance as `d_stop=v ell+v²/(2a)+delta`, using the trajectory's peak speed. All limits and margins are synthetic.

## Work sequence

1. Derive the peak speed and peak absolute acceleration for the cubic scaling as functions of `T`. Evaluate them for each candidate.
2. Evaluate the torque at the start and explain why it is the maximum over this stipulated move. Check each duration against both output-speed and output-torque limits.
3. Calculate the stopping allowance and remaining clearance for each duration. Identify the time, braking and geometry assumptions that make this only a conditional model check.
4. Determine the shortest candidate duration satisfying all three constraints. Also calculate the continuous lower bound on `T` from the speed, torque and stopping constraints and identify which bound controls.
5. Close an ideal mechanical-energy ledger. With zero endpoint speeds and no losses, compute the work needed to raise the load through one radian, and explain why this ideal work is independent of duration even while torque, speed and stopping margins depend on timing.
6. Propose a paper-only monitoring record that would keep commanded position distinct from measured position, speed, delivered-current information and timestamps. State what the model would flag if any limit is exceeded; do not describe this as a real controller or protective function.
7. Note the cubic's nonzero endpoint acceleration and state one consequence if it is joined directly to a stationary segment.

## Author calculation key

For `Delta_q=1`, `v_max=1.5/T` and `|q_ddot|_max=6/T²`. The gravity torque is largest at the start, where `q=0` and `q_ddot=6/T²`, so `tau_max=4.905+1.2/T²` N m. The commanded torque decreases over the interval under the given positive angle and acceleration profile.

| `T` (s) | `v_max` (rad/s) | `|q_ddot|_max` (rad/s²) | `tau_max` (N m) | `d_stop` (rad) | clearance reserve (rad) | Result |
|---:|---:|---:|---:|---:|---:|---|
| 0.8 | 1.875 | 9.375 | 6.780 | 0.553203 | -0.153203 | Fails all three limits |
| 1.0 | 1.500 | 6.000 | 6.105 | 0.376250 | 0.023750 | Fails speed and torque; passes the stipulated stop screen |
| 1.5 | 1.000 | 2.667 | 5.438 | 0.195000 | 0.205000 | Passes all three stipulated limits |

The speed constraint requires `T>=1.500 s`. The torque constraint requires `T>=sqrt(1.2/(5.50-4.905))≈1.420 s`. Solving `v(0.050)+v²/(8)+0.020<=0.400` for peak speed gives about `1.555 rad/s`, or `T>=0.965 s`; the speed limit controls, so the shortest feasible continuous duration is `1.500 s` under these scalar assumptions.

The ideal work is the potential-energy rise `m g r sin(1)=4.905 sin(1)≈4.12742 J`; the initial and final kinetic energies are both zero. The cubic has nonzero endpoint acceleration, so joining it to a stationary interval creates an acceleration discontinuity. These answers are arithmetic consequences of the supplied model and are not a hardware recommendation.

## Proposed unweighted review rubric

| Criterion | Evidence for future human review |
|---|---|
| Time scaling | Derives velocity and acceleration bounds from the declared path |
| Actuator budget | Computes gravity/inertia torque with consistent signs and units |
| Stopping screen | Applies latency, braking and deterministic clearance assumptions explicitly |
| Energy ledger | Separates duration-independent ideal work from rate-dependent limits |
| Scope and evidence | Separates commands from measurements and rejects claims of hardware safety |

The rubric has no point weights or automatic prose grader. Mathematical accuracy, instructional design, accessibility and workload need qualified review. Do not activate this draft or describe it as a course assessment until those reviews and the course's missing homework, exams and laboratory sequence are addressed.

## Provenance

Original authoring and synthetic inputs, CC BY 4.0, developed with substantial AI assistance. No real robot data, executable controller or operation procedure is included.
