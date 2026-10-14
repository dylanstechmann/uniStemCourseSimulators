# Vectors, partial derivatives, and gradients

A scalar field assigns one number to each point, such as concentration over a surface. A vector field assigns a vector to each point, such as a local transport direction and magnitude. A point's coordinates need a declared frame and scale: changing from centimetres to millimetres changes derivative units, even when it describes the same physical field.

## Partial change and a local linear model

For a scalar field $f(x,y)$, the partial derivative $f_x$ changes $x$ while holding $y$ fixed; $f_y$ does the converse. These coordinate-wise rates form the gradient

$$
\nabla f=(f_x,f_y).
$$

For a small displacement $(\Delta x,\Delta y)$ near a differentiable point, the first-order change is

$$
\Delta f\approx f_x\Delta x+f_y\Delta y=\nabla f\cdot(\Delta x,\Delta y).
$$

This linearization is local. Its error depends on curvature and on the displacement size; it is not an exact finite-change rule. If coordinates carry length units and $f$ is concentration, each partial derivative has concentration-per-length units. Uncertainty in the coordinates can therefore create value uncertainty through the same first-order model, but a numerical uncertainty estimate also needs an uncertainty model.

## Directional change and level curves

If $\mathbf{v}$ is a unit direction, the directional derivative is $D_{\mathbf{v}}f=\nabla f\cdot\mathbf{v}$. A non-unit vector scales the rate by its length, so normalize a direction before interpreting it as change per unit distance. Where $\nabla f\ne 0$, the gradient points toward the steepest local increase; its negative points toward the steepest decrease. A tangent to a smooth level curve $f(x,y)=c$ is perpendicular to the gradient because moving along the curve produces no first-order change in $f$.

For a field measured in a rotated coordinate frame, both the components and direction must use a consistent frame. A frame error can change the reported directional derivative even when the underlying physical field is unchanged. At a critical point where the gradient is zero, the first-order directional change is zero in every direction; that fact alone does not classify the point as a maximum, minimum or saddle.

## Keep the gradient and direction in the same frame

Consider a point where the gradient is $(3,4)$ concentration units per centimetre, and a unit direction is $(3/5,4/5)$. Their dot product gives a directional derivative of $3(3/5)+4(4/5)=5$ concentration units per centimetre.

Now rotate the coordinate axes by 90° so the new positive axes point along the old directions $(0,1)$ and $(-1,0)$. The same gradient has new components $(4,-3)$, and the same physical direction has new components $(4/5,-3/5)$. The dot product is still $4(4/5)+(-3)(-3/5)=5$. Mixing the old gradient components with the new direction components instead gives zero, an answer produced by inconsistent coordinates rather than by the field. This invariance applies to an orthonormal rotation; changing coordinate scales also changes derivative units and requires the corresponding scale conversion.

## Worked directional derivative

Use dimensionless coordinates and the constructed field $f(x,y)=x^2y+\sin y$. Then $f_x=2xy$ and $f_y=x^2+\cos y$. At $(1,0)$,

$$
\nabla f(1,0)=(0,2).
$$

For the unit direction $\mathbf{v}=(3/5,4/5)$, the directional derivative is $0(3/5)+2(4/5)=8/5=1.6$. For a small displacement $(0.02,0.03)$, the linear model predicts $\Delta f\approx 0(0.02)+2(0.03)=0.06$. The exact change is about $0.06121$, close but not equal; the difference is a second-order effect. Reversing the displacement direction would reverse the first-order term.

These computations describe a smooth mathematical field with normalized coordinates. They do not identify what a biological sensor detects, establish a unique transport mechanism, or replace measurements in a specified frame. The following concentration-field lesson adds a synthetic spatial example and examines when a gradient can be resolved across a finite cell.
