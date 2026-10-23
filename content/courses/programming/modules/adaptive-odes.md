# ODE computation: local error control, stiffness and independent checks

**Status:** original ungraded instruction with substantial AI assistance. Differential equations, states and tolerances are synthetic teaching inputs. This week-9 reading extends the explicit-Euler stability example into solver choice and verification; it does not execute learner code or validate a real system.

## Begin with a well-defined initial-value problem

An initial-value problem consists of y′=f(t,y), initial state y(t_0)=y_0, a time interval and any parameter values or events. Units of f must be state units per time. State constraints such as nonnegativity and conserved totals come from the model; they are not automatically enforced by every ODE method.

Keep mathematical, numerical and observational questions distinct. Existence and uniqueness concern the equations under stated regularity conditions. Solver accuracy concerns approximation of their solution. Agreement with observations concerns the model and measurement process. A small estimated integration error only addresses one of these questions.

## A two-stage method exposes the error calculation

For a trial step h from (t_n,y_n), explicit Euler predicts y_E=y_n+h f(t_n,y_n). Heun's method evaluates a second slope at that predicted endpoint and forms y_H=y_n+(h/2)[f(t_n,y_n)+f(t_n+h,y_E)]. For smooth problems, Heun has second-order global accuracy with fixed step, while Euler has first-order global accuracy.

Use y′=−y, y(0)=1 and h=0.2. Euler predicts 0.8. The second slope is −0.8, so Heun returns 1+0.1(−1−0.8)=0.82. The exact endpoint is exp(−0.2)≈0.81873075. Actual endpoint errors are approximately −0.01873075 and +0.00126925. The pair difference 0.02 estimates the leading local error of the lower-order prediction; it is not the exact error of the higher-order result.

Local error means the error introduced in one step starting from an exact input state. Global error includes accumulated and propagated errors over many steps. A per-step tolerance is not a direct promise that final global error is below that same number.

## Scale errors before deciding whether to accept

A common component scale is s_i=atol_i+rtol×max(|y_old,i|,|y_new,i|), with positive absolute tolerances and nonnegative relative tolerance. One can compare a norm of the normalized local-error estimate to one. Some libraries use a root-mean-square norm and other details; reproduce the actual method before comparing exact step sequences.

In the Heun/Euler example, take atol=0.001 and rtol=0.01. The scale is 0.011 and the normalized pair difference is 0.02/0.011≈1.81818. Under this declared rule the trial is rejected, even though the higher-order result's actual error happens to be much smaller. A controller follows its estimator, not unavailable knowledge of the exact solution.

If an estimator scales like h^q, a tentative next step is h_new=h×safety×err^(−1/q). For the displayed Euler/Heun difference, q=2 in the smooth small-step regime. With safety 0.9, the proposal is about 0.133492. A practical driver also limits growth/shrinkage, handles a zero estimate, checks minimum step and retries rejected trials without advancing time. This is an illustrative controller, not a description of every library implementation.

## Step doubling provides another check

For a method of global order p applied to a fixed endpoint from the same starting state, compare one step of length h with two steps of h/2. Under the leading local-error model, the fine result's error magnitude is approximately |y_fine−y_coarse|/(2^p−1). The estimate refers to that local comparison, with smoothness and small-step assumptions.

For Euler on y′=−y from one with h=0.2, the coarse result is 0.8 and two half steps give 0.9²=0.81. Their difference is 0.01. The fine result's actual error at t=0.2 is approximately −0.00873075. The estimate is plausible but not exact at this step. Halving a method's step without changing the equation helps diagnose discretization; changing the parameters at the same time destroys the comparison.

## Stiffness can make an accurate-looking slow trajectory expensive

Consider the independent modes y_1′=−y_1 and y_2′=−1000y_2. The physical time constants are 1 and 0.001 in the declared time unit. Explicit Euler's fast-mode amplification is 1−1000h. Absolute stability requires |1−1000h|<1, hence 0<h<0.002. A step h=0.01 may seem small for the slow mode but gives fast multiplier −9 and catastrophic numerical growth.

Backward Euler solves y_(n+1)=y_n+h f(t_(n+1),y_(n+1)). For y′=−λy this gives y_(n+1)=y_n/(1+λh), stable for all positive h when λ>0. At λ=40 and h=0.1 its multiplier is 0.2, while the exact multiplier is exp(−4)≈0.0183156. Stability is not accuracy. The implicit method damps the mode but can badly misrepresent a transient when its step is too large.

An implicit method replaces a stability restriction with an algebraic solve and an accuracy requirement; it does not eliminate work. For nonlinear f, each step can require Newton iterations, a Jacobian and a convergence decision. The inner-solver error should be controlled relative to the outer integration tolerance. Returning a step from a failed nonlinear solve makes the ODE error estimate unreliable.

## Events and invariants need their own evidence

An event such as y reaching a threshold can occur between saved output times. Finding it may use interpolation and a root solve. A coarse output table does not locate the crossing exactly. Specify event direction and whether the event terminates integration. Multiple crossings inside one large step can be missed by simple sign-change logic.

For a transfer system a′=−ka and b′=ka, the exact total a+b is constant. Check that total as a diagnostic, but note that a method can preserve a linear total while predicting a poor time course. Conservation, positivity, residual checks and refinement address different failure modes. A projection that forces a total after each step can hide a sign or indexing error unless its purpose is stated.

## Build a local verification study

Use y′=−3y, y(0)=2 and final time one as a separate rehearsal. Compare Euler, Heun and backward Euler on several fixed grids against 2exp(−3). For each method, show the maximum grid error, endpoint error, evaluation count and whether states remain nonnegative. An error table should retain the same final time and initial condition across refinements.

Then use the two-mode stiff system with both initial states one. Compare a step that is adequate for the slow mode with the fast-mode stability limit. Explain why a solver can take many tiny explicit steps after the fast state appears small: stability is a property of perturbation amplification, not only the displayed state magnitude. A production adaptive solver's performance depends on tolerances, formulation and implementation, so do not infer a universal speed ranking from one tiny test.

## Reporting and limits

Record solver/method, software version, tolerances, time span, initial values, output grid, events, rejected steps if available and termination status. Report model units and parameters. Verify with a closed-form solution, an independent method or a justified refinement study. Reusing the same implementation with different plotting settings is not an independent numerical check.

The [MIT OCW 2.086 Fall 2014 calendar](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-fall-2014/pages/calendar/) includes numerical ODEs and stiff/nonstiff software choices. This original reading develops scalar/two-mode examples, not a full adaptive-library implementation or a general stability proof. All prose, calculations and tasks are original CC BY 4.0 material with AI assistance. No MIT assessment or software was imported; qualified review and measured workload remain open.
