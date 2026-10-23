# Initial-value problems, variable coefficients and solution intervals

An equation specifies a slope rule; an initial value selects a trajectory only when the rule supports existence and uniqueness. The existing relaxation reading states an integrating-factor recipe. This reading derives the initial-value form, uses a genuinely variable coefficient, and tests the assumptions that a numerical curve can conceal. All quantities below are normalized synthetic mathematical examples. No real organism or device is being fitted.

## Derive the integrating-factor solution

For $y'+p(t)y=q(t)$, suppose $p$ and $q$ are continuous on an interval containing $t_0$. Choose

$$M(t)=\exp\left(\int_{t_0}^t p(s)\,ds\right).$$

Then $M'=pM$ and the product rule gives $(My)'=Mq$. Since $M(t_0)=1$, integration yields

$$y(t)=M(t)^{-1}\left[y_0+\int_{t_0}^t M(s)q(s)\,ds\right].$$

This expression both constructs a solution and makes uniqueness transparent. The difference $z$ of two solutions with the same input satisfies $z'+pz=0$, hence $Mz$ is constant. Equal initial data make that constant zero. Nonzero initial-data differences propagate as $z(t)=z(t_0)/M(t)$; they need not decay when the coefficient has another sign.

A useful alternative is a two-time propagator

$$K(t,s)=\exp\left(-\int_s^t p(v)\,dv\right),\qquad y(t)=K(t,t_0)y_0+\int_{t_0}^t K(t,s)q(s)\,ds.$$

For variable $p$, this generally depends on both times separately. Replacing it by a convolution kernel depending only on $t-s$ would impose time invariance that the equation does not have. A constant-coefficient transfer function therefore cannot be used unchanged for every variable-coefficient equation.

## Worked variable-coefficient case

Take $y'+2t y=4t$, $y(0)=1$. Here $M=e^{t^2}$ and $Mq=4t e^{t^2}$, whose antiderivative is $2e^{t^2}$. Thus

$$y(t)=2-e^{-t^2}.$$

At $t=1$, $y=2-e^{-1}\approx1.63212$, and $y'=2t e^{-t^2}$ gives $y'(1)\approx0.735759$. Direct substitution returns $4t$ and the initial value is one. The difference from equilibrium decays like a Gaussian in $t$, not one exponential with a constant time constant. The coefficients are continuous for every finite real time, so this linear solution exists for all real $t$.

A distinct rehearsal uses $y'+t y=3t$, $y(0)=5$. Its factor is $e^{t^2/2}$ and solution is $3+2e^{-t^2/2}$. At $t=2$, the value is $3+2e^{-2}\approx3.27067$, with derivative $-4e^{-2}\approx-0.541341$. Verify both the residual and initial value before using those numbers. A zero residual evaluated at one time is weaker than an identity on the claimed interval.

## What local existence and uniqueness assert

For a nonlinear scalar IVP $y'=f(t,y)$, continuity near the initial point is a common sufficient condition for local existence. Continuity together with local Lipschitz dependence on $y$ is a sufficient condition for local uniqueness. A continuous partial derivative with respect to $y$ on a neighborhood is one convenient way to establish the latter condition. These are sufficient hypotheses, not necessary conditions for every unique solution.

Local means an interval around the initial time. It does not promise a solution for arbitrarily long times, a nonnegative state, bounded growth, or a physically meaningful model. State constraints need their own invariance argument. At a boundary $y=0$, for example, the vector field's direction matters; the existence theorem does not automatically keep every numerical update inside a chosen domain.

## A nonunique family that can be checked directly

For $y'=2\sqrt{|y|}$ and $y(0)=0$, the zero solution exists. For each $a\geq0$, another forward solution waits at zero until $t=a$ and then follows $(t-a)^2$. The value and first derivative match at the joining time. Before the join both sides are zero; afterward $y'=2(t-a)=2\sqrt{y}$. This explicit family establishes nonuniqueness. Merely observing that the derivative of $\sqrt{|y|}$ is unbounded at zero would show failure of one sufficient hypothesis, but would not by itself prove nonuniqueness.

A numerical solver that returns the zero branch has found one valid solution; a convergence plot cannot prove that no other branch exists. Likewise, dividing a separable equation by a state-dependent factor may remove equilibria. Always test the divided-out states in the original equation.

## Finite-time escape and maximal intervals

For $y'=y^2$, $y(0)=1$, separation gives $y=1/(1-t)$. The maximal interval containing zero is $(-\infty,1)$. The same algebraic expression is defined for $t>1$, but that disconnected branch is not a continuation through the singularity of this IVP. Local smoothness of $f=y^2$ does not prevent finite-time escape. The assignment changes the initial value so that the escape time must be rederived.

Retain an equation/initial-value/domain ledger, not just a closed expression. Differentiate the candidate, test the initial data, identify singular coefficient or state boundaries, and state which theorem hypotheses hold there. The next coursework uses these checks to compare exact and numerical solutions. The browser checks selected values and interpretations; it does not assess a proof, code or complete report.

## Scope and sources

The actual local first-order reading is expanded here beyond a stated recipe, using the analytic/geometric/numerical and integrating-factor strands of [MIT OCW 18.03SC Fall 2011 Unit I](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-i-first-order-differential-equations/) and the [syllabus](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/syllabus/syllabus/) as link-only scope comparators. All explanations and examples are original and developed with substantial AI assistance. General existence-theorem proofs, boundary-value problems and partial differential equations remain outside this selected treatment. The package remains partial and unreviewed.
