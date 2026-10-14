# Indeterminate limits and L’Hôpital’s rule

## Learning objectives

1. Identify when direct substitution produces the indeterminate quotient forms `0/0` or `∞/∞`.
2. Apply L’Hôpital’s rule only when its local hypotheses hold, and recheck the form after each use.
3. Select algebraic simplification, dominant terms, a transformed quotient or L’Hôpital’s rule for a limit.

## An indeterminate form is a question, not an answer

When substitution into a quotient gives `0/0`, the numerator and denominator both approach zero; that information alone determines no limit. For example, as `x→0`, `x/x→1`, `x²/x→0`, and `x/x²` has no finite two-sided limit. All three quotients have the same substitution form but different behavior. Likewise, `∞/∞` does not determine a quotient's limit. Compare leading growth, simplify, or use a theorem whose assumptions are satisfied.

L’Hôpital’s rule applies to a quotient `f(x)/g(x)` near a finite point `a` (or from one side) under a specific set of conditions: `f` and `g` are differentiable on a punctured neighborhood on the side being considered; `g(x)` and `g′(x)` are nonzero there; both functions tend to zero, or both grow without bound in magnitude; and `f′(x)/g′(x)` has a limit, possibly an infinite one. Then `f(x)/g(x)` has that same limit. A corresponding version holds as `x` tends to infinity when the conditions hold on a tail. For a two-sided limit, check the two sides or establish that they agree.

The rule does not say to differentiate a numerator and denominator whenever a quotient is inconvenient. It does not directly cover a nonzero-over-zero form, a product, a difference, or a power. The derivative quotient must itself have a limit. If one L’Hôpital step leaves `0/0` or `∞/∞`, verify the conditions again before applying the rule a second time.

## Verify the form, then differentiate

For `lim_(x→0) (e^(2x)−1)/sin(3x)`, substitution gives `0/0`. The derivatives are `2e^(2x)` and `3cos(3x)`, so their quotient tends to `2/3`. Therefore the original limit is `2/3`. The derivative acts on each function separately; this is not the quotient rule.

For `lim_(x→0) (x−sin x)/x³`, one step gives `(1−cos x)/(3x²)`, still `0/0`. A second justified step gives `sin x/(6x)`, still `0/0`; a third gives `cos x/6`, which tends to `1/6`. Stop once the quotient is no longer indeterminate and its limit is directly available. This result can also be checked from the Taylor expansion, but the two methods rely on different reasoning.

At infinity, `(5x²+2)/(2x²−1)` has the form `∞/∞`. L’Hôpital’s rule gives `10x/(4x)→5/2`. Dividing numerator and denominator by `x²` gives the same result more directly. The leading-term method works for this rational quotient because both polynomials have matching degrees; it is not a general replacement for limit analysis.

## Simplify before choosing the rule

For `lim_(x→0) (sqrt(1+x)−1)/x`, direct substitution gives `0/0`. Rationalizing the numerator gives `1/(sqrt(1+x)+1)`, so the limit is `1/2` without differentiating. Simplification can expose cancellation and reduce unnecessary derivative work.

Some other indeterminate forms can be transformed into quotients. For `x→0+`, the product `x ln x` has a zero factor and an unbounded factor. Rewrite it as `ln x/(1/x)`, an `−∞/∞` quotient. L’Hôpital’s rule gives `(1/x)/(-1/x²)=−x`, which tends to zero. The original product therefore tends to zero.

For a positive-base expression of the form `u(x)^{v(x)}→1^∞`, take a logarithm: `ln(u^v)=v ln u`. Evaluate the resulting limit only after identifying its form. For `(1+x)^(1/x)` as `x→0+`, `ln u^v=ln(1+x)/x` is `0/0`; L’Hôpital’s rule gives a limit of `1`. Exponentiating yields `e`. Positivity of the base is essential for using this real logarithm transformation. An `∞−∞` difference may sometimes be combined into one quotient or rationalized, but the transformation must preserve the original domain and limit.

## Why the hypotheses matter

The two-sided expression `(1+x)/x` near zero is not `0/0`; its numerator tends to `1`, and its left and right limits differ. Differentiating numerator and denominator would give `1`, an incorrect answer. The rule cannot be applied because its indeterminate-form condition fails.

Even a genuine `0/0` quotient may resist this rule. For `x→0`, `(x² sin(1/x))/x = x sin(1/x)→0` by the squeeze theorem. The derivative quotient is `2x sin(1/x)−cos(1/x)`, which has no limit, so L’Hôpital’s rule gives no conclusion. The original limit still exists. A failed attempt to meet the theorem's conditions is not evidence that the original limit fails to exist.

## A practical method choice

1. Substitute and classify the resulting form.
2. If the denominator tends to a nonzero value, use continuity and direct substitution.
3. For `0/0`, try factoring, conjugates, identities or a known local approximation when these make the structure clear.
4. For `0/0` or `∞/∞`, check the theorem's conditions and the derivative quotient; use the rule only if they hold.
5. Transform products, differences or powers only with an equivalent expression on the relevant domain, then classify the new form.
6. At infinity, inspect dominant terms when the expression permits it. After any calculation, check that the limit's sign, scale and one-sided behavior match the original expression.

## Limits of this lesson

The examples develop selected quotient forms and simple transformations. They do not prove the full theorem, cover every oscillatory or multivariable limit, or replace a course in real analysis. All expressions are mathematical examples, not empirical models. Practice feedback checks selected values and choices rather than proof quality. The instruction is original with substantial AI assistance; MIT materials are linked only as a scope comparator.
