# Assignment 4: control and model boundaries

This cumulative open report joins energy-derived dynamics, computed torque, actuator clipping and the separate contact/geometry checks. It asks which ideal cancellation survives an explicitly changed input. All values are synthetic teaching inputs. Retain code, equations, plots and report locally; selected browser responses do not grade implementation, controller design or physical validity.

## Part A: specify the plant and controller separately

Use the uniform-rod model from the new foundation, with two one-meter, one-kilogram rods and synthetic g=1 m/s². At the instant q=(0,pi/2),v=(1,2), the mass matrix has rows (5/3,1/3),(1/3,1/3), velocity terms h=(-4,0.5) and compensation G=(1.5,0), in the corresponding SI units.

Define error e=qd−q and rate error edot=vd−v. Desired acceleration is (0.2,0.3) rad/s², e=(0.01,-0.02) rad and edot=(0.1,-0.1) rad/s. Use computed-torque acceleration gains Kp=100 per second squared and Kd=20 per second, applied componentwise.

The virtual acceleration qdd_desired+Kd edot+Kp e is (3.2,-3.7) rad/s². With an exact plant model and no clipping, requested torque M times that vector plus h+G is (1.6,1/3) N m. Derive the signed terms rather than using the earlier point-mass matrix for a rod model.

## Part B: deliver a different torque

Now clip each requested torque independently to the interval [-0.5,+0.5] N m. Delivered torque becomes (0.5,1/3), so only the shoulder request changes. Solve the original plant equation M a=tau_delivered−h−G. The resulting acceleration is (19/8,-23/8), or (2.375,-2.875) rad/s².

The elbow acceleration changes even though its delivered torque was not clipped, because the mass matrix couples the joints. Comparing only the clipped component misses that coupling. Verify the result by substituting both acceleration components into both original dynamic rows.

Actual error acceleration is desired acceleration minus actual acceleration: (-2.175,3.175) rad/s². The ideal decoupled error equation would have given (-3,4). The difference follows from the inverse mass matrix acting on the torque residual, with the correct error sign. A clipped plant no longer obeys the exact ideal cancellation law.

## Part C: integrate the declared nonlinear system

Implement the nonlinear rod plant and an exact-model computed-torque controller for a documented smooth reference trajectory and consistent initial state. First compare unclipped error evolution with the ideal linear error equation. Then add the stated torque clipping at the plant input and compare the trajectories under time-step refinement.

For the exact unclipped gains, each ideal error component has the critically damped analytic form [e(0)+(edot(0)+10e(0))t]exp(−10t). Derive it from the repeated root rather than fitting an exponential to the plotted trajectory. Use consistent initial error and rate error to compare that reference with the nonlinear plant result. After clipping, retain the analytic curve only as a comparison; it is no longer the governing error solution.

Record desired, requested and delivered quantities separately. Keep controller evaluation, model coefficients, solver step, clipping rule and initial error explicit. Do not clip position or velocity states after integration and claim the original input-clipped differential equations were solved. If another constraint or state-reset policy is introduced, define it as a separate model.

Track total mechanical energy and integrated delivered torque power. Without friction or contact the difference should converge with numerical refinement. Using requested power after the actuator clips can create a false energy ledger even if the plotted position appears plausible.

## Part D: isolate model and task boundaries

Repeat one comparison with a deliberately wrong mass distribution or gravity model, changing only that assumption. Explain how model mismatch and torque clipping enter different places in the plant/controller equations. Neither a residual nor a tracking error alone identifies their cause uniquely without the supplied comparison.

Assess a separately declared contact state using the constrained equations and reaction sign, rather than adding a spring or wall force after computing an unconstrained acceleration. Assess a separately declared geometric path with whole-link clearance and continuous rate/error bounds. Dynamic tracking, contact admissibility and obstacle separation require different evidence; success in one calculation does not supply the missing others.

Retain the point calculation, original-equation residual, nonlinear simulation, error-equation comparison, requested/delivered power ledger and a clear account of model boundaries. [MIT OCW 2.12 Fall 2005 syllabus/calendar](https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/pages/syllabus/) lectures 17–19 supply link-only dynamics/computed-torque scope. All derivations and tasks are original and AI-assisted, with no imported source exercise, code or dataset. Actual hardware identification, protective-function validation, measured workload and qualified review remain open; this package stays partial and unreviewed.
