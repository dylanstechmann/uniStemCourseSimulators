# Assignment 1: distributed dynamics and work ledgers

This open report turns the uniform-rod foundation into an original trajectory analysis. It requires body kinematics, energy-derived dynamics and a signed work check rather than only a torque at one static pose. All dimensions, masses, motion and gravity are stipulated teaching inputs. Retain diagrams, calculations, code and report locally; selected browser fields do not evaluate the full derivation or implementation.

## Part A: derive the body model

Use the foundation's two uniform rods: each has length one meter, mass one kilogram, center distance one half meter and center inertia 1/12 kg m². Use synthetic gravity g=1 m/s². Shoulder angle is measured from horizontal and elbow angle is relative to link one. No friction, gearing, flexibility or external contact is included.

Write each center position and velocity, and each body's absolute angular rate. Build kinetic energy from center translation and center rotation, then derive M from its quadratic form. Obtain potential and compensation G from the same coordinates. Apply Euler–Lagrange equations to recover the velocity-product vector h.

Compare the resulting mass matrix with the earlier massless-link point-mass lesson. The models have different mass distributions and cannot share coefficients merely because their link lengths look similar. State which body information would have to be measured before either construction could represent actual hardware.

## Part B: evaluate a complete periodic trajectory

Prescribe q1(t)=0.2 sin t and q2(t)=0.4+0.1 cos(2t), for 0<=t<=2pi seconds. Angles are in radians. Differentiate analytically to obtain rates and accelerations. The original equations then determine required actuator torque along the path; the path has not been shown feasible for any real actuator.

At t=0 the configuration is (0,0.5), velocity (0.2,0) and acceleration (0,-0.4). The shoulder torque is 41/30+0.3 cos(0.5), about 1.6299414 N m. The elbow torque is -2/15+0.02 sin(0.5)+0.5 cos(0.5), about 0.31504646 N m.

Kinetic energy at that instant is 0.02[5/3+cos(0.5)], about 0.05088498 J, and potential is 0.5 sin(0.5), about 0.23971277 J. Obtain each quantity from the original body construction and compare it with your matrix implementation, preserving unrounded intermediate values.

At t=pi/2, q=(0.2,0.3), rates are zero and acceleration is (-0.2,0.4). Evaluate both torques and potential. This point has no velocity-product torque, but gravity and acceleration still contribute. Do not carry t=0's h or configuration into this second calculation.

## Part C: integrate signed power independently

Compute required torque dotted with the actual velocity and integrate it over the full interval. Compare signed work with E(2pi)−E(0), where E=K+U. The trajectory and its velocity return to their original values, so the net energy change is zero. This does not mean instantaneous power, each actuator's work or the integral of absolute power is zero.

Refine the integration grid and show convergence of the work residual. Derive the identity v'h=one-half v'Mdot v independently and use it to diagnose a deliberately omitted h term. Compare at multiple nonzero-rate configurations; a rest-state check cannot expose every velocity-product error.

Repeat the energy comparison after adding a constant reference offset to U. Its gradient and required torque must remain unchanged, while the offset cancels in the energy difference. This is a useful implementation invariant: a model that changes its trajectory merely because the potential zero moved has introduced a nonphysical term. Separately verify the gradient with a centered numerical difference at several nonhorizontal poses, keeping that derivative error distinct from trajectory-integration error.

## Part D: forward dynamics and numerical evidence

Use the prescribed torque as an input to a forward integration with consistent initial position and velocity. Compare the resulting motion with the analytic path under step refinement. Separate the quadrature error in the work ledger from the state-integration error. A solver that returns a smooth plot can still solve a sign-reversed or parameter-mismatched plant.

Repeat a selected check with the old point-mass matrix incorrectly substituted into the rod model. Explain which energy or trajectory residual reveals the mismatch. Do not interpret that deliberate comparison as an empirical identification experiment or a physical model-fit result.

Retain body diagrams with verbal descriptions, exact equations, point tables, trajectory/error plots, code and refinement evidence. [MIT OCW 2.12 Fall 2005 syllabus/calendar](https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/pages/syllabus/) lectures 17–19 are link-only dynamics/control scope. All material and values are original with substantial AI assistance; no source exercise, code or dataset is imported. General multibody identification, actual actuator feasibility, measured workload and qualified review remain open; the course remains partial and unreviewed.
