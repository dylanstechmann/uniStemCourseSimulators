# Frames, rotations, and homogeneous transforms

Robotics uses coordinate frames to describe where points and tools are located. A point has the same physical location in every frame, but its coordinate numbers depend on the chosen origin and axes. Write the frame labels before multiplying matrices so that each transformation has a clear source and destination.

## Rotate a point in two dimensions

Using column vectors, a counterclockwise rotation by angle $\theta$ about the origin is

$$
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}.
$$

At $\theta=90^\circ$, this maps $(1,0)$ to $(0,1)$. A valid planar rotation preserves lengths and satisfies $R^TR=I$ and $\det R=1$. The determinant distinguishes a proper rotation from a reflection, which also preserves lengths but reverses orientation.

## Add an origin shift with homogeneous coordinates

Let frame $B$ have origin $t_{WB}=(2,1)$ m in world frame $W$, and let $B$ be rotated $90^\circ$ counterclockwise relative to $W$. The homogeneous transform $T_{WB}$ maps coordinates in $B$ into coordinates in $W$:

$$
p_W=T_{WB}p_B,\qquad
T_{WB}=
\begin{bmatrix}
0&-1&2\\
1&0&1\\
0&0&1
\end{bmatrix}.
$$

The final coordinate 1 lets a single matrix multiply represent both rotation and translation. For the point $p_B=(1,0)$ m,

$$
\begin{bmatrix}x_W\\y_W\\1\end{bmatrix}
=T_{WB}\begin{bmatrix}1\\0\\1\end{bmatrix}
=\begin{bmatrix}2\\2\\1\end{bmatrix}.
$$

Thus its world position is $(2,2)$ m. The last row of a planar homogeneous transform is $[0\ 0\ 1]$; in three dimensions the corresponding rigid transform is a $4\times4$ matrix with a $3\times3$ rotation block, a three-component translation and last row $[0\ 0\ 0\ 1]$.

## Composition order follows the frame labels

For the column-vector convention, $T_{AB}$ maps coordinates from frame $B$ into frame $A$. Therefore

$$
p_A=T_{AB}p_B,\qquad T_{AC}=T_{AB}T_{BC}.
$$

The adjacent frame labels cancel in the product, like units in a dimensional calculation. Matrix order is not interchangeable: the rightmost transform acts first. In the example, translate-then-rotate in a fixed world-origin interpretation would rotate the translated point to $(-1,3)$ m, while the stated pose rotates the point in frame $B$ and then expresses it at the translated world origin, giving $(2,2)$ m. These operations describe different geometric setups; frame labels prevent confusing them.

The inverse transform recovers the original coordinates. For $T_{WB}=[R\ t]$, its inverse is $T_{BW}=[R^T\ -R^Tt]$. Equivalently, subtract the world-frame origin $t$ from $p_W$ and apply $R^T$. This both reverses the translation and undoes the rotation; negating the translation alone is not sufficient when the frames are rotated.

## A practical consistency check

Before using a transform, state the coordinate convention, direction of each frame mapping, angle sign and length units. Check that the rotation block is orthogonal with determinant $+1$, that the homogeneous last row has the right form, and that composition labels connect. Apply the transform to a simple point, then apply its inverse and verify that the original point returns. A frame sketch with labeled axes often reveals a reversed transform before it reaches a calculation.

These planar coordinates and dimensions are constructed examples for teaching matrix conventions. They do not describe a particular robot, calibration procedure or safety-rated motion system.
