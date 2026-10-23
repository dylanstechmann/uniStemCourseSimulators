# Assignment 3: state and observer evidence

This open report develops a full-state feedback and observer pair for a distinct two-state plant, then verifies the combined dynamics and their information limits. All matrices, signals and initial states are normalized teaching inputs. Retain derivations, code, plots and report locally; selected browser fields do not grade the complete state-space argument or establish a real estimator or controller.

## Part A: identify the model's input/output information

Use xdot=A x+B u, y=C x with A rows (0, 1), (-4, -4), B=(0, 1)' and C=(1, 0). There is no direct feedthrough. Derive G(s)=C(sI−A)^−1B and its zero-initial-state poles. Compute controllability and observability matrices and verify rank before assigning feedback or observer poles.

State the meaning of the chosen coordinates. A similarity transformation changes A, B, C and gain coordinates while preserving the represented dynamics. Using a gain vector from one state basis with measurements in another is a different controller, even if its numbers look familiar.

## Part B: feedback and reference gain

Apply u=−K x+N r. Target state-feedback poles are -3 and -7, giving characteristic s²+10s+21. Coefficient matching gives K=(17, 6) and reference multiplier N=21 for unit constant-reference gain.

Derive N from the equilibrium or full closed-loop transfer rather than assuming a stabilizing K automatically yields unit tracking. Verify the original state equations at the constant-reference equilibrium. The result assumes exact matrices, an attainable input and the declared feedback connection.

Compare open-loop and feedback modes and explain what their locations establish. Negative real parts imply asymptotic decay of homogeneous deviations for this finite linear model. They do not prove monotone coordinates, an acceptable input peak or satisfactory behavior under every perturbation.

## Part C: observer and combined dynamics

Use xhatdot=A xhat+B u+L(y−C xhat). Target observer-error poles are -6 and -9. The error characteristic is s²+(4+l1)s+(4l1+4+l2), so L=(11, 6)'. Verify the result by direct eigenvalue calculation.

With error e=x−xhat and control u=−K xhat+N r, construct the full four-state matrix in coordinates (x, e). Its diagonal blocks are A−B K and A−L C, with upper-right B K. The four poles are -3, -7, -6, -9, and the slowest is -3 under this exact linear model.

Show why the error equation is independent of reference when plant and observer receive the same known input and use the same model. If the observer uses requested input while the plant receives a different clipped value, the mismatch adds a forcing term. If both use the delivered input, the observer error and combined control still require the correct changed equations; do not claim one generic saturation conclusion without specifying the signal path.

## Part D: trajectory and hidden-mode checks

Choose explicit initial plant and estimate states, including a nonzero estimation error. Compare direct four-state integration with an independent matrix exponential or analytic modal reference. Refine the time step and separately report output tracking, estimation error and requested input.

Repeat the foundation's nonminimal stable-transfer/unstable-state example with a nonzero hidden-mode initial condition. Verify which rank property fails and why a zero-initial-state transfer calculation cannot establish internal decay. Keep that separate example distinct from the controllable and observable assignment plant.

Discuss measurement noise and model error as omitted assumptions. Faster observer poles do not automatically imply a more accurate physical state estimate:the correction gain also multiplies sensor errors. No noise distribution or optimization criterion has been supplied, so this is pole placement rather than a claimed optimal filter.

Compare a zero-initial-state input/output calculation with the response from the same bounded input and a nonzero autonomous-state initial value. Write both terms explicitly. A canceled transfer pole can leave the first term benign while the second grows; the comparison tests the scope of the transfer representation rather than a numerical solver defect.

Retain matrices, rank tests, characteristics, reference equilibrium, observer/combined equations and numerical comparisons. Plots require input/state definitions, scales and a plain-text description of tracking and estimation differences. A correct selected gain pair does not demonstrate the quality of the entire implementation.

Selected [MIT OCW 16.30 Fall 2010 lecture topics 5–16](https://ocw.mit.edu/courses/16-30-feedback-control-systems-fall-2010/pages/lecture-notes/) provide link-only state/feedback/observer scope. The local two-state treatment does not reproduce that course's full syllabus, software prerequisites or lab sequence. All examples and tasks are original and AI-assisted; no source matrix exercise, code, figure or data is imported. General state synthesis, robust/noisy estimation, physical implementation, measured workload and qualified review remain open; the package stays partial and unreviewed.
