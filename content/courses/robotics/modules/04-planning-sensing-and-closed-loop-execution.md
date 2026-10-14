# Planning, sensing, and closed-loop execution

Planning and feedback solve different parts of a motion task. A path describes a geometric route through a modeled workspace. A trajectory assigns time to that route, giving desired position, velocity and acceleration over time. A controller compares the desired motion with sensor estimates and adjusts actuator commands when the observed system differs from the plan.

## From a geometric path to timed motion

For a joint-space path $q(s)$, the path parameter $s$ moves from its start to its end. A time-scaling function $s(t)$ turns that path into a trajectory $q(s(t))$. The geometry can be unchanged while a slower time scale reduces desired speed and acceleration. But the chosen timing still has to respect actuator limits, obstacle clearance and the assumptions used to model the mechanism. A collision-free path alone is not evidence that a physical robot can execute it as planned.

The plan also depends on coordinate frames and estimated obstacle positions. If a plate or tool frame is offset, accurately measured joint angles can still correspond to the wrong task-space location. A fiducial or another external reference can help estimate that frame offset. A sensor reading is evidence with uncertainty; comparing it with an expected value creates a residual, but the residual alone does not identify whether the cause is calibration, a disturbance, a model error or a sensor fault.

## Feedback corrects measured deviations

Consider a deliberately simple static measurement model $y_k=u_k+b$, where $u_k$ is the commanded position, $b$ is a fixed sensor or frame bias, and the target is $r=1$. With $b=0.1$ and initial command $u_0=0$, the first reading is $y_0=0.1$ and error $e_0=r-y_0=0.9$. Use the update

$$
u_{k+1}=u_k+K e_k,\qquad K=0.5.
$$

Then $u_1=0.45$, $y_1=0.55$ and $e_1=0.45$. The next update gives $u_2=0.675$, $y_2=0.775$ and $e_2=0.225$. In this simplified model the error halves each step and approaches zero despite the fixed bias. This arithmetic illustrates why feedback can correct an imperfect estimate or disturbance when new measurements are available.

It is not a stability proof for a real mechanism. Delay, noise, saturation, backlash and dynamic coupling change the closed-loop response. A gain that works for a static equation may oscillate or diverge on a dynamic plant. The later motor-feedback and sensing lessons examine measured limits, residual evidence and model assumptions in more detail.

## Contact: position tracking, force regulation, and compliance

In free motion, a position command can describe the tool path. After contact, the same position command also compresses the environment, so its force depends on how stiff that environment is. For a deliberately simple one-dimensional spring model,

$$
F=k\delta,
$$

where $k$ is contact stiffness in N/m and $\delta$ is indentation in m. Suppose the commanded indentation is 2.0 mm. If the surface stiffness is 400 N/m, the modeled force is $400(0.002)=0.80$ N; at 600 N/m it is $600(0.002)=1.20$ N. A position controller that tracks the same 2.0 mm therefore does not hold force constant as stiffness changes. If the task's stated force limit is 1.0 N, the second modeled condition exceeds it. This is a model-based comparison, not a protective limit for hardware.

Force control instead uses a measured contact force and adjusts the normal position to reduce $e_F=F_d-F_{measured}$. For example, with $k=400$ N/m and $F_d=1.0$ N, the static model predicts $\delta=F_d/k=2.5$ mm. If the current indentation is 2.0 mm, then $F=0.80$ N and $e_F=0.20$ N, so the controller should increase indentation under this sign convention. A force sensor, a controller, and a model of the contact dynamics are needed; a commanded target by itself does not establish that the target will be reached or remain bounded.

Hybrid position-force control assigns different task directions to different objectives. In a contact frame, a surface-following task may regulate force along the constrained normal while tracking position along a tangent. The frame must be aligned well enough that those axes represent the intended contact directions. A compliant tool or surface deforms under load and can soften abrupt interaction, but compliance alone does not ensure a bounded force or a stable feedback loop.

These calculations use a quasistatic, frictionless, linear spring. They omit inertia, impact and contact transients, friction, sensor noise and latency, actuator saturation, changing contact geometry, and force-loop stability. They cannot establish safe operation, hardware performance, or a validated force limit. MIT OCW 2.12's undergraduate calendar explicitly includes hybrid position-force control and compliance in lectures 12–13; this short synthetic treatment is a local comparator-informed primer, not a reconstruction of that course.

## Monitor limits and define recovery

Execution should compare observations with declared operating bounds and define what happens when sensing is lost, a command saturates or the observed state leaves its permitted region. A controlled stop, hold or other safe response depends on the mechanism and risk analysis; this course's synthetic examples do not validate a protective function or safety-rated system. For laboratory automation, repeatability, contamination boundaries and recovery after an interrupted protocol also need explicit treatment rather than an assumption that retrying is always harmless.

Before interpreting a run, record the planned path, timing, frame assumptions, sensor source, uncertainty and actuator limits. Compare the measured trajectory with the planned one, report residuals with units, and separate observed deviation from a possible cause. These practices improve a model-based diagnosis but do not establish that a real robot is calibrated, collision-free or safe to operate.

The scalar update and examples are constructed for instruction. They specify no hardware, biological interaction, operating envelope or validated recovery procedure.
