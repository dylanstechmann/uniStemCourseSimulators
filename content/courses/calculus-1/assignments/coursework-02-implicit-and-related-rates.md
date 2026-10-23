# Assignment 2: implicit functions, inverse rates and changing geometry

Develop a locally saved mathematical report that connects derivatives, units, implicit constraints and inverse sensitivity. Use the [composite/implicit reading](../modules/08-composite-implicit-and-related-rates.md), [inverse-function reading](../modules/15-inverse-functions-exponentials-and-logarithms.md) and [local-approximation reading](../modules/12-local-approximations-newton-and-sensitivity.md). The browser checks selected numbers and interpretations; it does not evaluate your derivations, diagrams or error claims. Every curve and motion here is stipulated, with no real mechanical design claim.

## 1. A curve is not automatically a global function

Consider x²+xy+y²=7 near (x,y)=(1,2). Verify the point lies on the curve. Differentiate the relation treating y as a local function of x and derive a formula for y′. Identify the denominator that must remain nonzero for that formula to define a finite slope. Compute y′ at the supplied point. Derive y″ by differentiating the implicit relation again; retain all product-rule terms.

Solve the quadratic relation explicitly for the upper branch y(x) near x=1. State its radicand domain and verify that this branch returns y=2. Differentiate that explicit branch and compare its first and second derivatives at the point with your implicit results. Explain why a local branch can exist even though the whole closed curve fails the vertical-line test. At a point where the implicit y-slope denominator vanishes, decide whether the curve itself is absent or whether another coordinate description may be more appropriate.

## 2. Transform and invert the local branch

For z(x)=ln y(x), justify the logarithm's local domain before computing z′ and z″ at x=1. Distinguish the derivative of ln y from the logarithm of y′; the latter may not even be defined for the sign here. Derive the local inverse derivative dx/dy at y=2 and explain why it is the reciprocal of dy/dx only on an invertible local branch with a nonzero derivative.

Use the tangent line to predict y(1.05). Compare it with the exact upper-branch value. Report a signed error and distinguish a measured error at one step from a bound valid over a neighborhood. If you claim a Taylor error bound, supply a justified bound on |y″| over the entire stated interval rather than only its value at the starting point. Repeat with a negative perturbation and check whether the error changes sign as your curvature reasoning predicts. This task assesses transfer of a derivative calculation into a controlled approximation argument.

## 3. Differentiate a constraint before inserting time values

A fictional rigid segment of length 13 meters forms a right triangle with positive horizontal coordinate x(t) and vertical coordinate y(t). Thus x²+y²=169. At one instant x=5 meters, y=12 meters and dx/dt=0.6 meter per second. Draw the geometry and state which signs correspond to the horizontal endpoint moving outward and the vertical endpoint moving downward. Differentiate the constraint with respect to time, then calculate dy/dt.

Let theta be the angle between the segment and the positive horizontal direction, so cos(theta)=x/13 and sin(theta)=y/13. Derive dtheta/dt in radians per second and verify it independently using the other trigonometric relation. Then calculate the rate of change of the triangular area xy/2. Explain why substituting x=5 before differentiating would incorrectly erase one time-dependent factor. State how your formulas behave as y approaches zero and why that limiting sensitivity may conflict with a physical motion model.

## 4. Compare mathematical and model uncertainty

Give a first-order sensitivity estimate for the vertical rate if the supplied horizontal rate changes by 0.01 meter per second while the geometry is fixed at that instant. Then analyze a hypothetical geometry error separately. Explain why a derivative sensitivity is a local linear approximation, not a confidence interval or evidence that the rigid-segment assumptions hold. Identify one missing physical ingredient needed before treating the stipulated motion as an engineering prediction. No experiment or hardware operation is requested.

## Self-review after deriving the results

For the implicit curve, y′=−(2x+y)/(x+2y), giving −0.8 at (1,2). Differentiating once more yields y″=−[2+2y′+2(y′)²]/(x+2y), giving −0.336 there. The upper branch is y=[−x+sqrt(28−3x²)]/2 near x=1. The logarithmic derivatives are z′=−0.4 and z″=−0.328; the inverse slope is −1.25. The tangent prediction at x=1.05 is 1.96, but you must compute its actual error independently.

For the moving triangle, dy/dt=−x(dx/dt)/y=−0.25 meter per second. The angular rate is −(dx/dt)/y=−0.05 radian per second. The area rate is [x(dy/dt)+y(dx/dt)]/2=2.975 square meters per second, positive despite the decreasing height. All signs follow the declared coordinates and angle.

Retain the implicit and explicit derivative checks, domain analysis, local inverse argument, perturbation comparison and a labeled rate diagram. Include units and hypotheses for every conclusion. This original assignment was developed with substantial AI assistance; the [MIT OCW 18.01SC Fall 2010 differentiation applications](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-2-applications-of-differentiation/) are a link-only scope reference, with no imported problem or figure. Qualified mathematical review and measured workload remain open; the package is partial and unreviewed.
