# Multivariable optimization and constraints

Optimization starts by stating the objective, the variables and the feasible set. A critical point can solve the derivative equations while still being a saddle, a boundary point, or infeasible for the intended problem. The type of conclusion depends on the curvature and on whether the feasible set is open, closed, bounded or otherwise constrained.

## Unconstrained critical points

For a differentiable function $f(x,y)$, an interior local maximum or minimum must satisfy $\nabla f=0$. The Hessian

$$
H_f=\begin{bmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy}\end{bmatrix}
$$

describes local curvature when the second derivatives are continuous. A positive-definite Hessian gives a strict local minimum; a negative-definite Hessian gives a strict local maximum; an indefinite Hessian gives a saddle. In two variables, $\det H_f>0$ together with $f_{xx}>0$ or $f_{xx}<0$ distinguishes the positive- or negative-definite cases. If the determinant is negative, the curvatures have opposite signs. A zero determinant makes this second-derivative test inconclusive, so higher-order terms or another argument are needed.

For example, let $F(x,y)=4-(x-1)^2-2(y+2)^2$. Its gradient vanishes at $(1,-2)$ and its Hessian is $\operatorname{diag}(-2,-4)$, which is negative definite. Because both squared terms are nonnegative, $F\le4$ everywhere, so this point is also the global maximum. The Hessian gives local classification; the global inequality supplies the stronger global claim.

## A smooth equality constraint

To optimize $f$ subject to $g(x,y)=c$, an interior constrained extremum with a regular constraint often satisfies

$$
\nabla f=\lambda\nabla g.
$$

The gradients are parallel because the objective has no first-order change in any feasible tangent direction. This condition assumes $\nabla g\ne0$ at the candidate. It is necessary under that regularity condition, but it does not classify the candidate or guarantee a global optimum. Check feasible boundaries and compare objective values whenever the domain permits them.

For $f(x,y)=xy$ subject to $x+y=10$, the gradients are $(y,x)$ and $(1,1)$. The multiplier equation gives $x=y$, so the constraint yields $(5,5)$ and $f=25$. To establish the global maximum on the entire feasible line, substitute $y=10-x$:

$$
f(x,10-x)=x(10-x)=25-(x-5)^2\le25.
$$

Thus the stationary candidate is a global maximum even though the feasible line is unbounded. If the model also imposed a restricted interval, each allowed endpoint would need checking. Additional inequality constraints can introduce active boundaries and corner candidates that the equality multiplier equation alone misses.

## Interpret the model before its answer

An objective represents what is being optimized; each constraint encodes a separate feasibility statement. A numerically optimal point outside a stated manufacturing or biological range is not an acceptable design. With several variables or constraints, units, coordinate scales and the meaning of each multiplier also matter. A multiplier can describe a local rate of change in the optimal value as a constraint changes, under regularity and a stable optimum; it is not automatically a causal effect.

The examples are mathematical constructions. Later lessons examine Hessians, degenerate critical points, active boundaries and constrained regions in more detail; the conditions stated there still govern whether a candidate is local, global or inconclusive.
