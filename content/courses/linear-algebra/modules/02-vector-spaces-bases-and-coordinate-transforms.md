# Vector spaces, bases, and coordinate transforms

A vector is the object being described; a coordinate list is one way to represent it after choosing a basis. The same geometric vector can therefore have different coordinate values in different bases. This distinction is central in geometry, robotics, mechanics and data analysis: transformations may rotate a vector, change the coordinate frame, or do both, and the matrix multiplication depends on which operation is intended.

## Learning objectives

By the end of this lesson, you should be able to:

1. Test linear independence and span.
2. Distinguish a geometric vector from its coordinates in a basis.

## Span, independence, and basis

Given vectors (v_1,\ldots,v_k), their span is the set of all linear combinations

\[
c_1v_1+\cdots+c_kv_k.
\]

The vectors are linearly independent when the equation

\[
c_1v_1+\cdots+c_kv_k=0
\]

has only the solution in which all coefficients are zero. If some nonzero coefficient choice gives zero, at least one vector can be built from the others, so the set contains redundancy. A basis is a set that both spans the space and is linearly independent. It provides enough vectors to describe every element in the space without redundant coordinate choices.

In \(\mathbb{R}^n\), place candidate basis vectors as columns of a matrix (P). If (P) is square, its columns form a basis exactly when (P) is invertible, equivalently when its columns are independent and span \(\mathbb{R}^n\). Elimination reveals the pivot count. If a pivot is missing, the columns are dependent and do not span the full space. For a subspace of dimension (k<n), a basis has (k) independent vectors that span that subspace; it need not span all of \(\mathbb{R}^n\).

## Coordinates are coefficients in a chosen basis

Let (B=(b_1,\ldots,b_n)) be a basis. The coordinate vector \([v]_B\) stores the coefficients used to build (v) from those basis vectors. The matrix

\[
P_B=\begin{bmatrix}b_1&\cdots&b_n\end{bmatrix}
\]

maps the basis coordinates to standard coordinates:

\[
[v]_{\mathrm{standard}}=P_B[v]_B.
\]

If (P_B) is invertible, then \([v]_B=P_B^{-1}[v]_{\mathrm{standard}}\). The vector itself has not changed; only its numerical description has. The identity matrix is the basis matrix for the standard basis, so standard coordinates and the underlying vector are often written with the same numbers. That convenient shorthand can hide a basis change.

## Worked example: one vector, two coordinate lists

Choose (b_1=(1,0)) and (b_2=(1,1)). They are independent because the matrix with these columns,

\[
P_B=\begin{bmatrix}1&1\\0&1\end{bmatrix},
\]

has determinant 1. Suppose the coordinates of (v) in this basis are \([v]_B=(3,1)\). Then

\[
v=3b_1+1b_2=3(1,0)+(1,1)=(4,1).
\]

Thus \([v]_{\mathrm{standard}}=(4,1)\), even though \([v]_B=(3,1)\). To check the conversion in the other direction,

\[
P_B^{-1}=\begin{bmatrix}1&-1\\0&1\end{bmatrix}, \qquad
P_B^{-1}\begin{bmatrix}4\\1\end{bmatrix}=\begin{bmatrix}3\\1\end{bmatrix}.
\]

Multiplying the basis matrix by its coordinate vector reconstructs the same vector. If the basis were dependent, the representation could be non-unique; if it did not span the space, some vectors could not be represented at all.

## Change between two bases

Let (P_B) and (P_C) have the basis vectors for (B) and (C) as columns, both written in standard coordinates. For a vector described first in basis (B),

\[
[v]_C=P_C^{-1}P_B[v]_B.
\]

The rightmost matrix acts first: (P_B) reconstructs standard coordinates, then (P_C^{-1}) expresses that same vector in basis (C). The composite (P_C^{-1}P_B) is a coordinate conversion, not necessarily a physical movement. Writing a label such as (P_{C\leftarrow B}) can help: it sends coordinates “from (B) to (C).” Before multiplying, state what frame each vector is expressed in and what frame the result should use.

## Active rotations and passive frame changes

A two-dimensional counterclockwise rotation through angle \(\theta\) uses

\[
Q(\theta)=\begin{bmatrix}\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta\end{bmatrix}.
\]

For \(\theta=90^\circ\), (Q(3,0)^T=(0,3)^T\): this is an active rotation, in which the vector moves while the coordinate frame stays fixed. A passive frame change keeps the vector fixed and changes the coordinates used to describe it. If the new orthonormal frame is rotated counterclockwise by (Q) relative to the old frame, then the new coordinates are (Q^T[v]_{\mathrm{old}}). For the same vector \((3,0)\), that gives \((0,-3)\) in the rotated frame. The sign difference follows from changing the frame rather than rotating the vector.

For an orthonormal basis matrix (Q), (Q^TQ=I), so (Q^{-1}=Q^T) and lengths and angles are preserved. A proper rotation also has determinant (+1); a reflection is orthogonal but has determinant (-1\). General basis matrices need only be invertible: they may stretch, shear, or change orientation. They still convert coordinates, but they do not preserve lengths or angles unless they are orthogonal.

## Scaling and numerical care

An algebraically valid basis can still be inconvenient for computation. If one basis vector is thousands of times larger than another, or two vectors are nearly parallel, solving for coordinates can amplify roundoff and measurement error. This is a conditioning issue, not a failure of the basis definition: an exactly invertible matrix may be numerically sensitive. Orthonormal bases are often useful because their coordinates preserve lengths and the conversion matrix has a simple inverse. Scaling or orthogonalizing a basis can improve computation, but the coordinate conversion must be applied consistently.

## Common reasoning errors

- Treating a coordinate tuple as the vector itself without stating its basis.
- Multiplying by (P_B) when the task asks for basis coordinates; that direction requires (P_B^{-1}).
- Using (Q) for a passive frame change when the inverse (Q^T) is required.
- Assuming every basis change is a rotation or preserves lengths.
- Calling a set a basis after checking only independence or only span.
- Interpreting a badly scaled basis as mathematically invalid instead of numerically sensitive.

## Further study

MIT OpenCourseWare 18.06SC, *Linear Algebra*, Massachusetts Institute of Technology, offers independent study materials for [Independence, Basis and Dimension](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/ax-b-and-the-four-subspaces/independence-basis-and-dimension/). This is linked for further study; no source text or problem has been reused in this reading.

## Limits of this lesson

The calculations use exact two-dimensional examples. In larger systems, a computed coordinate conversion can be sensitive to roundoff and data error, especially for nearly dependent bases. This lesson defines the transformations; it does not guarantee that a chosen frame or model is appropriate for a physical application.
