# Forward and inverse kinematics

Forward kinematics maps joint angles to the position of an arm's endpoint. Inverse kinematics asks which joint angles can place the endpoint at a requested target. A target can have no solution, one limiting solution, or multiple valid solutions; geometry and joint limits decide which case applies.

## Forward position of a two-link arm

For a planar arm with link lengths $L_1,L_2$ and angles $\theta_1,\theta_2$, both measured counterclockwise from the positive horizontal axis for their respective joints, the endpoint is

$$
x=L_1\cos\theta_1+L_2\cos(\theta_1+\theta_2),\qquad
y=L_1\sin\theta_1+L_2\sin(\theta_1+\theta_2).
$$

The second link's absolute orientation is $\theta_1+\theta_2$. When both angles are zero, the links lie along the positive x-axis and the reach is $L_1+L_2$. All lengths must use the same unit. If $L_1=L_2=0.5$ m and both joints are at zero, the endpoint is $(1,0)$ m.

## Check reachability before solving

Let $r=\sqrt{x^2+y^2}$ be the distance from the base to a target. Triangle geometry requires

$$
|L_1-L_2|\le r\le L_1+L_2.
$$

Thus the reachable positions form an annulus, including its boundary when fully extended or folded configurations are permitted. With $L_1=0.4$ m and $L_2=0.3$ m, the inner radius is 0.1 m and the outer radius is 0.7 m. A target at radius 0.5 m passes this geometric check; a target at the origin does not. Joint stops or obstacles can further reduce the usable set, so this radial check is necessary but not sufficient for an installed mechanism.

## Two inverse branches can share one endpoint

The law of cosines gives an elbow-angle candidate through

$$
\cos\theta_2=\frac{x^2+y^2-L_1^2-L_2^2}{2L_1L_2}.
$$

If the right side is outside $[-1,1]$, no real elbow angle reaches the target. If it lies strictly inside that interval, the signs of $\sin\theta_2$ usually give two elbow branches. For each candidate,

$$
\theta_1=\operatorname{atan2}(y,x)
-\operatorname{atan2}(L_2\sin\theta_2,L_1+L_2\cos\theta_2).
$$

For $L_1=0.4$ m, $L_2=0.3$ m and target $(x,y)=(0.4,0.3)$ m, the radius is 0.5 m and $\cos\theta_2=0$. One solution is $(\theta_1,\theta_2)=(0^\circ,90^\circ)$; another is approximately $(73.74^\circ,-90^\circ)$. Substituting either pair into the forward equations gives the same endpoint. These are different arm postures, not two different target points.

At $\theta_2=0$ the links are fully extended; at $\theta_2=\pi$ they are folded. These collinear configurations are boundary cases where the planar Jacobian loses rank, so some small endpoint motions cannot be produced by a finite first-order joint-rate solution. The later Jacobian lesson develops the velocity consequences. A branch can also be geometrically valid but violate a joint limit, so list the constraints before choosing one.

## Verify every candidate

For an inverse solution, check the arccosine argument, compute each distinct branch, enforce joint limits, and substitute the result back into forward kinematics. Use tolerances appropriate to the units rather than comparing rounded display values. The calculations here use constructed link lengths and coordinates; they establish no particular robot's accuracy, collision clearance, dynamics or safe operation.
