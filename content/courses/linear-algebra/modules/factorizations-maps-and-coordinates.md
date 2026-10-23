# Factorizations, linear maps and coordinate geometry

Elimination, a change of basis and a quadratic-form substitution can all involve multiplying matrices, but they preserve different objects. A row operation changes a system of equations without changing its solution set. Similarity changes coordinates for a linear map. Congruence changes the matrix representing a quadratic form. This reading connects [elimination](01-linear-systems-elimination-and-rank.md), [basis coordinates](02-vector-spaces-bases-and-coordinate-transforms.md) and [symmetric forms](09-symmetric-matrices-spectral-theorem-and-quadratic-forms.md), using original exact matrices. Algorithm implementation and performance belong to Programming; the emphasis here is algebraic structure and proof.

## Factor a sequence of row operations

Let A have rows (0,2,1), (2,1,1) and (4,3,3). Its first diagonal entry is zero, so a naive first-pivot division fails even though the matrix is invertible. Interchange the first two rows with permutation P. The reordered matrix has rows (2,1,1), (0,2,1) and (4,3,3). Eliminate the first entry of row three using multiplier two, leaving (0,1,1). Eliminate its second entry with multiplier one half, leaving (0,0,1/2).

The resulting upper-triangular U has rows (2,1,1), (0,2,1), (0,0,1/2). The corresponding lower-triangular L has unit diagonal, L31=2 and L32=1/2, with other strict-lower entries zero. Direct multiplication verifies PA=LU. The equality is an identity between matrices, not just agreement for one chosen right-hand side. To solve Ax=b, solve Ly=Pb and then Ux=y. The permutation must also act on b. Forgetting it can produce an exact solution of the wrong equations.

Here det(U)=2 and det(L)=1, while det(P)=−1, so det(A)=−2. A zero original diagonal entry did not imply zero determinant. In larger pivoted factorizations, row swaps occurring after elimination has started also require consistent treatment of previously stored multipliers. The small example isolates the algebra; it is not a complete numerical pivoting implementation or an argument that every matrix admits an unpermuted LU factorization.

For rehearsal, take A with rows (0,1,2), (1,1,0), (2,3,1). Again swap the first two rows. Multipliers two and one lead to U with rows (1,1,0), (0,1,2), (0,0,−1). Check PA=LU entry by entry and infer det(A)=1. Treat a matrix factorization as a claim that can be verified independently by multiplication.

## Similarity represents the same map

Let S have columns (1,0) and (1,1), and write a physical vector as x=Sz. Then x=(z1+z2,z2), so z=S inverse x. If a standard-coordinate map is A=diag(2,3), its z-coordinate matrix is B=S inverse A S, with rows (2,−1) and (0,3). Derive this by applying the map to x=Sz and then converting the output back to z coordinates. Do not memorize a multiplication order without identifying input and output coordinates.

B has the same eigenvalues two and three as A. Indeed, if Ax=lambda x, then B(S inverse x)=lambda(S inverse x); similarity carries eigenvectors between representations. More generally det(B−lambda I)=det[S inverse(A−lambda I)S]=det(A−lambda I), which proves characteristic-polynomial invariance. The names of vector components change, while the underlying linear map does not.

## A nonorthogonal basis changes the coordinate metric

For z=(1,2), the physical vector is x=(3,2). Its Euclidean norm squared is thirteen, although z transpose z equals five. In the new basis the same physical norm is z transpose G z, where G=S transpose S has rows (1,1), (1,2). The basis is invertible but not orthonormal. Treating coordinate entries as orthonormal physical components would change lengths and projection geometry.

This explains how B can look nonsymmetric even though the original A is symmetric. Its correct self-adjoint relation in these coordinates is B transpose G=GB, which you can check directly. Symmetry of a numerical array depends on the coordinate metric; orthonormal coordinates make that metric the identity. This bounded example does not introduce a general tensor calculus, but it prevents an incorrect conclusion that changing to any invertible basis preserves ordinary transpose symmetry.

## Congruence represents the same scalar form

For the physical quadratic form x transpose A x, substitute x=Sz. The new coefficient matrix is C=S transpose A S, with rows (2,2), (2,5). This is congruence, not similarity. Its eigenvalues in the ordinary z-coordinate Euclidean metric are six and one, unlike the map eigenvalues two and three. The scalar form remains identical after the coordinate substitution; its matrix eigenvalues need not remain identical.

Positive definiteness is preserved by invertible congruence: nonzero z gives nonzero Sz, so z transpose C z=(Sz) transpose A(Sz)>0 when A is positive definite. That argument proves the property without assuming the eigenvalues were preserved. State what invariant you are claiming before choosing a matrix transformation.

## Linear functionals transform differently from vectors

A scalar functional d transpose x with standard coefficients d=(1,2) becomes d transpose Sz. Its coefficient column in z coordinates is S transpose d=(1,3), not S inverse d. For z=(1,2), both representations give seven. A physical vector's coordinates and a linear functional's coefficients therefore follow different rules. In orthonormal coordinates, identifying vectors and functionals through the Euclidean inner product can conceal that distinction; the Gram matrix makes it explicit here.

The [subspace/map assignment](../assignments/coursework-01-subspaces-and-maps.md) asks for proofs and consistency checks using distinct rectangular data. Keep systems, maps, metric forms and functionals separate in every ledger. MIT OCW [18.06 Linear Algebra Spring 2010 syllabus](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/) and [calendar](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/calendar/) are link-only scope comparators. All explanations, proofs, matrices and problems here are original and developed with substantial AI assistance; no source exercise or figure was imported. General numerical factorization, abstract dual-space theory and qualified proof/workload review remain outside this selected treatment. The course is partial and unreviewed.
