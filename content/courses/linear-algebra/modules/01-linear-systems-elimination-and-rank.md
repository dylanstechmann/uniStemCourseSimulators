# Linear systems, elimination, and rank

A linear system asks for a vector of unknowns that satisfies several equations at once. In matrix form, write the coefficient matrix as (A), the unknown vector as (x), and the right-hand side as (b): (Ax=b). Elimination converts this system to a simpler one with the same solution set. The resulting pivot pattern tells us whether a solution exists, whether it is unique, or whether free variables remain.

## Learning objectives

By the end of this lesson, you should be able to:

1. Solve (Ax=b) with elimination.
2. Interpret pivots and rank as information about solutions.

## Row operations preserve the solutions

The augmented matrix ([A\mid b]) records the coefficients and the right-hand side together. Gaussian elimination uses three reversible row operations: interchange two rows, multiply a row by a nonzero constant, or add a multiple of one row to another. Each operation produces an equivalent system because it changes the equations without changing which (x) satisfy them. The right-hand side must undergo the same operations as the coefficient columns.

Elimination produces row-echelon form: each nonzero row begins at a pivot, pivots move right as you go down, and any zero rows are at the bottom. A pivot column identifies a variable that can be solved from the equations after any free variables have been assigned. Back-substitution then recovers the pivot variables. Reduced row-echelon form continues the process to make each pivot the only nonzero entry in its column, which can make the solution set easier to read.

## Worked example: solve a system with one solution

Consider

\[
x+y=3, \qquad x-y=1.
\]

Its augmented matrix is

\[
\begin{bmatrix}1&1&\mid&3\\1&-1&\mid&1\end{bmatrix}.
\]

Replace row 2 by row 2 minus row 1:

\[
\begin{bmatrix}1&1&\mid&3\\0&-2&\mid&-2\end{bmatrix}.
\]

The second row gives (y=1); substituting into the first gives (x=2). There is a pivot in both variable columns, so there are no free variables. The coefficient matrix has rank 2, equal to the number of unknowns, and this consistent system has one solution. Substitution into the original equations is a quick check: (2+1=3) and (2-1=1).

## Pivots, rank, and the solution set

The rank of (A), written \(\operatorname{rank}(A)\), is the number of pivots in its coefficient columns. It counts the independent rows and also the independent columns. A row that becomes all zeros contributes no new independent equation; a pivot contributes one independent constraint. Counting pivots is more informative than counting the original rows, since some equations may repeat or be combinations of others.

There are (n) variable columns when (x\in\mathbb{R}^n). Each pivot column corresponds to a pivot variable; every non-pivot column corresponds to a free variable. For a consistent system of rank (r), the number of free variables is (n-r). If (r=n), every variable is a pivot variable and the solution is unique. If (r<n), at least one free variable remains; when the system is consistent, different choices of that variable produce infinitely many solutions.

Consistency is checked in the augmented matrix. A row of the form

\[
[0\;0\;\cdots\;0\mid c], \qquad c\ne 0,
\]

would require (0=c), which is impossible. In that case, the system has no solution. Equivalently, (Ax=b) is consistent exactly when

\[
\operatorname{rank}(A)=\operatorname{rank}([A\mid b]).
\]

If the augmented column creates an additional pivot, the two ranks differ and the system is inconsistent. This is why rank alone does not tell us whether a particular right-hand side is reachable: we must inspect the augmented matrix too.

## Repeated equations and contradictory equations

The system (x+y=3,\;2x+2y=6) has one independent equation repeated at a different scale. Its augmented matrix reduces to

\[
\begin{bmatrix}1&1&\mid&3\\0&0&\mid&0\end{bmatrix}.
\]

The coefficient rank is 1 and there are 2 unknowns, so (y=t) is free and (x=3-t). Every real value of (t) gives a solution. By contrast, change the second equation to (2x+2y=7). Elimination then gives a row (0=1), so the augmented matrix has one more pivot than (A) and no solution exists. Both systems have a rank-deficient coefficient matrix; only the augmented system distinguishes the consistent case from the inconsistent one.

## Rank also describes the matrix map

Each column of (A) is the output produced by one coordinate direction of (x). The set of all possible outputs (Ax) is the column space of (A). Its dimension is the rank. A right-hand side (b) can be reached exactly when it lies in that column space, which is the geometric version of the consistency test. If columns are dependent, different input vectors may produce the same output; the difference between those inputs lies in the null space, the set of vectors (z) with (Az=0).

This connects the three solution cases. If (b) lies outside the column space, there is no solution. If (b) lies in the column space and the null space contains only zero, there is one solution. If (b) is reachable and the null space contains nonzero vectors, adding any null-space vector to one particular solution produces another solution. In a consistent system, the null-space dimension is (n-r), the same count as the free variables.

## Exact rank and numerical computation

For exact arithmetic, a pivot is either zero or nonzero. With measured or rounded data, small values can be affected by floating-point error, and a computed matrix may behave as though it were nearly rank-deficient even when its exact rank is full. Numerical algorithms use pivoting and tolerances to reduce avoidable error. Rescaling a row or a variable may improve the computation, but it does not create new information in the underlying measurements. The later lessons on conditioning and regularization examine how small perturbations can change an answer even when elimination returns a solution.

Do not confuse singularity with ill-conditioning. A singular square matrix has no inverse and has rank below its dimension. An ill-conditioned matrix may be invertible, but small changes in its entries or right-hand side can produce large changes in the computed solution. The first is an exact structural property; the second concerns sensitivity. In applications, report the model assumptions, units, scaling, and validation checks alongside fitted values.

## Common reasoning errors

- Counting original equations instead of independent pivots.
- Checking only (A) and ignoring the augmented column when testing consistency.
- Calling every rank-deficient system inconsistent, even though it may have infinitely many solutions.
- Calling a pivot in every row a unique solution when there are more variables than pivots.
- Treating a numerical tolerance as a mathematical definition of exact rank.
- Assuming a small residual or an algebraic solution validates the model that produced (A) and (b).

## Further study

MIT OpenCourseWare 18.06SC, *Linear Algebra*, Massachusetts Institute of Technology, offers independent study materials for [Elimination with Matrices](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/resources/elimination-with-matrices-1/) and [Solving \(Ax=0\): Pivot Variables, Special Solutions](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/ax-b-and-the-four-subspaces/solving-ax-0-pivot-variables-special-solutions/). These are linked for further study; no source text or problem has been reused in this reading.

## Limits of this lesson

The examples use exact arithmetic and constructed numbers. They teach how elimination and rank classify solution sets; they do not establish that a real model is well specified, identifiable from measurements, or numerically stable. Those questions require assumptions and validation beyond counting pivots.
