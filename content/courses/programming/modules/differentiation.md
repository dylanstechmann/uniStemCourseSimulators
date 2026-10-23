# Numerical differentiation: truncation, noise and a defensible step size

**Status:** original instruction and open practice, developed with substantial AI assistance. Work with synthetic functions and tables; the browser does not run learner code. This reading belongs beside the quadrature lesson in week 7. Its goal is to choose and test a derivative approximation, rather than to equate a small step with accuracy.

## Derive the formulas before using them

Let f be a scalar function evaluated near x. The forward quotient is D_f(h) = [f(x+h)−f(x)]/h. Taylor expansion gives f(x+h) = f(x)+hf′(x)+h²f″(x)/2+O(h³), so D_f(h)=f′(x)+hf″(x)/2+O(h²). The leading truncation error is first order if the second derivative is finite and nonzero. This statement concerns exact evaluations of a smooth mathematical function.

Subtract the expansions at x+h and x−h instead. Even powers cancel, giving the central quotient D_c(h)=[f(x+h)−f(x−h)]/(2h)=f′(x)+h²f‴(x)/6+O(h⁴). It uses two symmetric evaluations and has second-order truncation error under stronger smoothness. This is not permission to sample outside a function's domain. At a boundary, use an appropriate one-sided formula or reformulate the problem.

The second derivative has a different stencil: [f(x+h)−2f(x)+f(x−h)]/h². Its dimensions are the units of f divided by squared units of x. Applying a first-derivative formula twice requires specifying the grids and boundary treatment; it is not the same operation as applying this three-point formula once to arbitrary observations.

## A calculation with a known truth

Use f(x)=x³, x=2 and h=0.1. Then f(2)=8, f(2.1)=9.261 and f(1.9)=6.859. The forward estimate is 12.61 and the central estimate is 12.01. The exact derivative is 12, so their signed errors are +0.61 and +0.01. For this cubic, forward error is 6h+h² and central error is h² exactly. Halving h to 0.05 gives forward estimate 12.3025 and central estimate 12.0025. The central error decreases by four, while the forward error decreases only approximately by two because it contains both first- and second-order terms.

The three-point second derivative is (9.261−16+6.859)/0.01=12. Its exactness for this cubic does not imply exactness for a quartic or noisy table. Polynomial test cases are useful because they isolate implementation mistakes, but testing only polynomials that a formula differentiates exactly cannot reveal its general truncation error.

## Roundoff and evaluation error reverse the refinement trend

Suppose each function evaluation carries an absolute error at most δ. The forward numerator can carry error up to 2δ, so its derivative error contribution can be as large as 2δ/|h|. For the central quotient, the analogous bound is δ/|h|. This bound treats errors adversarially; random measurement noise calls for a distributional model instead.

A useful central-difference error envelope is E(h)=A h²+B/h for h>0, with A and B expressed in compatible units. Differentiating gives E′(h)=2Ah−B/h². The stationary point is h*=(B/(2A))^(1/3), and the positive second derivative there makes it a minimum. If A=0.5 and B=10^−6 in a declared normalized problem, h*=0.01 and the bound is 0.00015. At h=0.001 the bound is approximately 0.0010005: tenfold refinement made the bound worse.

The familiar machine-precision scaling h≈epsilon^(1/3) for central differences is a scale estimate after nondimensionalizing the argument and function. It is not a universal literal step. Units, derivative magnitudes, discontinuities, function-evaluation error and noise all matter. Use a step expressed on a meaningful input scale and inspect a sweep of values.

## Noisy observations are a different input problem

Suppose observations y(x−h) and y(x+h) have independent zero-mean errors with standard deviation σ. Their difference has variance 2σ², hence the central derivative's standard deviation is σ/(sqrt(2) h). With σ=0.02 and h=0.1 in declared observation/argument units, it is approximately 0.141421 derivative units. Increasing the separation to h=0.2 reduces this standard deviation to approximately 0.070711, while increasing smooth-function truncation bias. A claimed derivative needs a bias/noise trade-off, not only a machine-epsilon argument.

If the two errors are correlated, their covariance belongs in the variance of the difference. Repeated readings at the same x do not create new independent specimens. For irregularly spaced data, fitting a local polynomial and differentiating it may be useful, but the fit order, neighborhood and uncertainty model become part of the method. Blindly applying a symmetric equal-step stencil to unequal spacing changes the quantity being approximated.

## Use Richardson extrapolation conditionally

If D_c(h)=d+C h²+O(h⁴), then [4D_c(h/2)−D_c(h)]/3 cancels the h² term. For the cubic example, [4×12.0025−12.01]/3=12. The estimated magnitude of the fine central estimate's leading error is |D_c(h/2)−D_c(h)|/3=0.0025.

This argument fails when refinement changes the problem or when evaluation noise dominates. An extrapolated answer with more printed digits is not automatically more accurate. Check at least three steps, compare successive differences and explain which error model is plausible. Near a kink, a derivative may not exist; a convergent one-sided quotient can describe only the corresponding one-sided derivative.

## Implement an explicit contract locally

```python
import math


def central_difference(function, x, step):
    if not math.isfinite(x) or not math.isfinite(step) or step <= 0:
        raise ValueError("finite x and a positive finite step are required")
    left, right = x - step, x + step
    if left == x or right == x:
        raise ValueError("the step is not resolved at this input scale")
    low, high = function(left), function(right)
    if not math.isfinite(low) or not math.isfinite(high):
        raise ValueError("function evaluations must be finite")
    return (high - low) / (2 * step)
```

This function deliberately does not infer units, choose a step, smooth observations or catch every possible domain exception. Its caller supplies a function defined at both endpoints and interprets the result. Tests should include constants, linear and cubic functions, a domain boundary, an unresolved step at large x, and nonfinite output. A test that only checks whether the function returns a number misses the method's purpose.

## Practice and report

For a separate rehearsal, use f(x)=x³ at x=1 with h=0.2 and h=0.1. Work the forward and central formulas, compute signed errors against f′(1)=3, and then extrapolate the two central estimates. In a second task, use E(h)=2h²+0.000032/h to choose the positive minimum; calculate both error contributions at the chosen step. Keep these synthetic error constants distinct from an empirically established uncertainty model.

Report the definition of the derivative, input/output units, stencil, domain, step sweep and known-answer tests. Show an error-versus-step table before drawing a conclusion from one estimate. Separate numerical error for the declared function from uncertainty in whether the function describes observations. Common failures are dropping the denominator's factor of two, losing units, treating exact-polynomial agreement as universal validation and continuing to shrink h after noise dominates.

## Scope and attribution

This lesson covers scalar finite differences and their assumptions. Higher-dimensional gradients, automatic differentiation, complex-step methods and rigorous statistical smoothing remain further topics. The scope comparator is [MIT OCW 2.086, Fall 2014 calendar](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-fall-2014/pages/calendar/), whose opening unit includes numerical differentiation. The [syllabus](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-fall-2014/pages/syllabus/) supplies the broader computational-methods boundary. No source exercise, code, text or dataset is reproduced. Original material is CC BY 4.0; qualified review and measured workload remain outstanding.
