# Optimization and related rates

Optimization combines a function with a feasible domain. The derivative identifies interior candidates, but the model determines which candidates are allowed and a value comparison determines which one wins. A constraint often reduces a problem with several dimensions to a single decision variable. Before differentiating, name that variable, state its units, and write the domain implied by the geometry or design.

## A rectangle with fixed perimeter

Suppose a rectangular frame uses 20 cm of material around its boundary. Let one side be $x$ cm and the other be $y$ cm. The constraint is

$$
2x+2y=20,\qquad y=10-x.
$$

The area to maximize is therefore a function of one variable:

$$
A(x)=x(10-x)=10x-x^2.
$$

Positive side lengths require $0<x<10$. Its derivative is $A'(x)=10-2x$, so the only interior critical point is $x=5$ cm. Then $y=5$ cm and the area is 25 cm². Because $A$ is a downward-opening parabola, this point is a maximum. We can also compare values: as $x$ approaches either endpoint, the area approaches 0, while $A(5)=25$.

The distinction between an open and closed domain matters. With strictly positive sides the endpoints are not feasible, so there is no smallest attained area even though the infimum is 0. If a collapsed rectangle is allowed as a limiting design, the closed interval $[0,10]$ includes both zero-area endpoints; the extreme-value theorem then guarantees both an attained maximum and minimum for this continuous function. Either model gives the same maximum, but the claim about a minimum depends on the design rules.

## A reliable candidate check

For a continuous objective on a closed, bounded interval, list every interior point where the derivative is zero or undefined and both endpoints, then evaluate the original objective at every feasible candidate. Check units and constraints after solving. A derivative test can classify a local extremum, but it does not replace the global comparison. If the domain is open, unbounded, or has excluded points, separately check limiting behavior: a largest value may fail to be attained, and an unbounded objective has no finite maximum. A stationary point outside the feasible domain is not a candidate, even if the algebra is correct.

This workflow also catches common modeling errors. Do not optimize the area as though $x$ and $y$ could vary independently when the perimeter is fixed. Do not confuse a critical point with the requested quantity: after finding the side lengths, substitute them into the area function. Keep the physical constraints visible so that a mathematically convenient value is not mistaken for a feasible design.

## When dimensions change with time

Optimization compares possible designs at one instant; a related-rate calculation follows a changing design through time. For a rectangle with constant length $l=10$ cm and width $w(t)$, area is $A(t)=lw(t)$. Differentiating with respect to time gives

$$
\frac{dA}{dt}=l\frac{dw}{dt}+w\frac{dl}{dt}=10\frac{dw}{dt},
$$

because $dl/dt=0$. If the width is increasing at 0.2 cm/s, area grows at 2 cm²/s, regardless of the current width. The units follow from “cm times cm/s”. If both dimensions change, both product-rule terms must be retained. For more involved linked quantities, first write the constraint, then differentiate it with respect to time while keeping every changing variable's rate. The later related-rates lesson treats implicit constraints and cases in which slope or rate interpretation requires additional checks.

The synthetic geometric examples here are practice models, not engineering specifications. Optimization answers depend on the stated objective and feasible set; changing either can change the result.
