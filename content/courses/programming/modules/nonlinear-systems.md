# Nonlinear systems: linearize, solve, check and globalize

**Status:** original ungraded instruction with substantial AI assistance. All equations are synthetic. This reading joins the scalar root lesson in week 8 and requires the linear-solver foundations. It explains what a nonlinear solver does and what its stopping message can establish.

## A vector root is not several unrelated scalar roots

For F:R^n→R^n, the target is a vector x satisfying every component of F(x)=0 simultaneously. If equations share unknowns, solving one and then freezing its answer while solving another usually changes the problem. State the unknown vector, domain, equations and units before selecting an algorithm.

Consider F_1(x,y)=x²+y²−5 and F_2(x,y)=x−y−1. The first describes a circle and the second a line. Substituting x=y+1 into the first gives 2y²+2y−4=0, so the two roots are (2,1) and (−1,−2). This exact geometric reduction provides a reference for testing an iterative method; the method's output alone should not be used as its own reference truth.

The equations are dimensionless teaching expressions. In a physical system, equations can have different units, and an unscaled sum of squared residuals can add incompatible quantities. Choose declared characteristic scales before using a norm to compare residual components.

## Derive Newton's correction

Taylor linearization gives F(x+Δ)≈F(x)+J(x)Δ, where J_ij=∂F_i/∂x_j. Setting that approximation to zero gives J(x)Δ=−F(x). Newton's method solves this linear system and updates x_new=x+Δ. The Jacobian is not an inverse, and elementwise division by its entries is not a linear solve.

For the circle/line system, J=[[2x,2y],[1,−1]]. At (2,0), F=[−1,1] and J=[[4,0],[1,−1]]. The correction equations are 4Δx=1 and Δx−Δy=−1, yielding Δ=[0.25,1.25]. The full step reaches (2.25,1.25), where F=[1.625,0]. Although the line residual is eliminated, the maximum absolute residual grew from 1 to 1.625. A correct Newton step need not decrease a residual norm far from a root.

At half that correction, (2.125,0.625), F=[−0.09375,0.5] and the infinity norm is 0.5. This smaller step improves the chosen norm. A damping or line-search rule can compare trial steps, but it needs a declared merit function, acceptance rule and failure status. Calling every reduced step “Newton convergence” hides these choices.

## Local speed requires hypotheses

Near a sufficiently regular simple root, with a nonsingular Jacobian and an adequate initial guess, Newton can converge quadratically: the next error can scale with the square of the current error. This is a local statement. Singular derivatives, poor initial guesses, constraints, discontinuities or inaccurate inner solves can prevent the expected behavior.

For this example, det J=−2(x+y). At (0.5,−0.5), the Jacobian is singular. The point still lies on the line x−y=1, but linearization loses the ability to distinguish the relevant circle direction there. A solver should report a failed or singular correction rather than silently returning that point as a solution.

A local solver can return either root depending on the initial guess. Its success does not prove uniqueness or locate every root. The exact line/circle analysis above establishes multiplicity for this particular problem; general systems need additional reasoning or a deliberately broader search.

## Check a Jacobian independently

Analytic derivatives can contain indexing and sign errors. Compare each Jacobian column with a central finite-difference approximation [F(x+h e_j)−F(x−h e_j)]/(2h), using a step sweep and the differentiation lesson's error trade-off. For x²+y² the central first derivative is exact in real arithmetic, making it a useful initial test but an incomplete general accuracy study.

A directional test compares Jv with [F(x+hv)−F(x−hv)]/(2h). At (2,1) and v=[1,−2], Jv=[0,3]. The direction is tangent to the circle to first order, so its first component is zero, while the line component changes by three. This test checks both cross-coupling and signs without constructing an inverse.

Finite differences evaluate the function at perturbed points. A domain-restricted model may be undefined there. Complex-step or automatic differentiation have their own applicability assumptions; they do not remove the need to test that the residual function matches the model.

## Scaling changes the numerical decision

Let residual scales s_i be positive quantities in the units of F_i, and define a dimensionless residual vector r_i=F_i/s_i. A tolerance on ||r||∞ then has a coherent meaning. Variable scales can similarly turn a step into a dimensionless quantity. Record both choices so another implementation can reproduce stopping decisions.

Multiplying an equation by a constant does not change its exact roots, but it changes an unscaled norm and can change the path or termination of a practical algorithm. If two implementations disagree after one equation is written in millimeters rather than meters, inspect scaling before declaring a scientific contradiction.

For a proposed result, report both the original residual values with units and the scaled norm. Do not use solver success as a synonym for acceptable residuals. Conversely, a solver might flag stagnation after reaching a residual acceptable for a particular application; the interpretation needs the stated contract rather than blind trust in a flag.

## Three separate termination questions

First, is the residual acceptably small on its declared scale? Second, is the update small relative to variable scales? Third, was the computation stopped by an iteration/evaluation limit, invalid domain, singular Jacobian or line-search failure? A small step alone can result from a nearly singular system or roundoff stagnation while residuals remain large.

Retain iteration count, function-evaluation count, final residual, scaled step and termination reason. Check feasibility and conservation constraints independently. A root outside a physically admissible domain is still unacceptable for that model even when its algebraic residual is tiny.

A constrained minimizer of ||F||² need not be a root: it may stop where the residual cannot be reduced further locally. Likewise, a least-squares fitting problem intentionally has residuals when observations are inconsistent. Distinguish equation solving from fitting before interpreting solver output.

## Rehearsal and implementation task

For a separate rehearsal, use G_1=x²+y²−10 and G_2=x−y−2, starting at (3,0). Derive the Jacobian, solve the first correction and compute the new residual. Find all exact roots by substitution and compare them with the iterative result. At (3,1), test the Jacobian in direction [1,−1] by both multiplication and symmetric differences.

Implement a local driver that accepts a residual function and a correction solver. Keep the merit function and damping rule explicit. Write tests for a known root, the first hand-calculated step, a singular Jacobian, an out-of-domain trial and iteration-limit reporting. A trace showing a decreasing residual is evidence about the selected numerical run, not proof that all initial guesses converge.

## Scope and provenance

The [MIT OCW 2.086 Fall 2014 calendar](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-fall-2014/pages/calendar/) includes nonlinear systems in its final unit. This original lesson develops Newton linearization, damping, scaling and validation on a two-equation system. Trust-region algorithms, continuation, general constrained optimization and exhaustive root finding remain further topics. No MIT code, exercise or prose was copied. Original instruction is CC BY 4.0 with disclosed AI assistance; qualified review and measured workload remain open.
