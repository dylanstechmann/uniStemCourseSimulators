# Linear-system conditioning, residuals and solution error

Numerical software can return a vector that nearly satisfies a linear system while the underlying solution remains highly sensitive to small input changes. This lesson separates three ideas: the conditioning of the mathematical problem, the residual or backward error of a computed vector, and the stability of the algorithm that produced it. The worked system is deliberately small so every quantity can be checked by hand.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute a linear-system residual and compare a computed vector with a known reference solution.
2. Calculate an infinity-norm condition number for a small matrix and interpret its sensitivity implication.
3. Distinguish problem conditioning, backward error, and algorithm stability when assessing a numerical result.

## A nearly dependent two-equation system

Treat the displayed decimal coefficients as exact synthetic values:

**A = [[1, 1], [1, 1.0001]],  b = [2, 2.0001]ᵀ.**

The exact solution is **x = [1, 1]ᵀ**. The determinant is 0.0001, so the rows are nearly dependent. A small difference between the rows has to distinguish the two unknowns.

For the infinity norm, take the largest absolute row sum. Thus **‖A‖∞ = 2.0001**. The exact inverse is

**A⁻¹ = [[10001, −10000], [−10000, 10000]],**

so **‖A⁻¹‖∞ = 20001** and the condition number is **κ∞(A) = ‖A‖∞‖A⁻¹‖∞ = 40004.0001**. This large value signals that small relative perturbations to the input can produce much larger relative changes in the solution. A condition number is a sensitivity measure for the problem and the stated norm; it does not diagnose a particular solver implementation by itself.

## Residual versus forward error

Suppose a numerical routine returns **x̂ = [0.5, 1.5]ᵀ**. Its residual is **r = b − Ax̂ = [0, −0.00005]ᵀ**, with **‖r‖∞ = 0.00005**. The vector exactly solves the nearby system with right-hand side **b̃ = [2, 2.00015]ᵀ**. The relative change in the right-hand side is about **2.5 × 10⁻⁵**.

Yet the forward error relative to the known solution is **‖x̂ − x‖∞/‖x‖∞ = 0.5**. A small residual therefore does not guarantee a small solution error when the system is ill-conditioned. Here the computed vector changes by 50% in the infinity norm even though the right-hand side changes by only about 0.0025%.

A normwise relative backward-error measure for this vector is

**η∞ = ‖b − Ax̂‖∞ / (‖A‖∞‖x̂‖∞ + ‖b‖∞) ≈ 1.0 × 10⁻⁵.**

This summarizes how closely the computed vector solves a nearby problem under the selected norm. Backward error and forward error answer different questions.

## Compare with a well-conditioned system

If **A = I** and the same right-hand side perturbation **δb = [0, 0.00005]ᵀ** is applied, then **δx = δb**. The relative solution change is about **2.5 × 10⁻⁵**, close to the relative input change. The contrast comes from the different problem conditioning, not from changing the perturbation magnitude.

Conditioning describes how the mathematical problem responds to perturbed inputs. Stability describes how an algorithm's computed result relates to the exact solution of a nearby problem. A backward-stable method can have a small backward error and still produce a forward-inaccurate answer for an ill-conditioned problem. Both properties matter when interpreting solver output.

## Practical checks and limits

1. Form **r = b − Ax̂** and report its scale relative to the matrix, vector, and right-hand side rather than relying on an unlabeled residual alone.
2. When a reference solution or independently justified bound is available, inspect forward error separately.
3. Estimate conditioning with an appropriate numerical routine in realistic problems; explicitly forming an inverse is used here only because the 2 × 2 example is hand-solvable.
4. State the norm and variable scaling. A condition number depends on these choices, while physical interpretation also depends on units and model meaning.

This original synthetic example develops one linear-system sensitivity strand. It does not compare direct, iterative, sparse, or eigenvalue algorithms, establish a universal tolerance, or validate a scientific model. MIT OCW 2.086 Fall 2014 is a curriculum comparator for the broader numerical-methods course; this lesson is narrower than that course.
