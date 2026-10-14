# Determinants: volume scaling, row operations and invertibility

Earlier lessons used the determinant as a tool: as a check on a 2 × 2 eigenvalue calculation, as the denominator in Cramer's rule for a calibration line, and as the product of eigenvalues of a symmetric matrix. This lesson explains where the number comes from and what it does and does not tell you. The determinant of a square matrix measures how the map x ↦ Ax scales signed area or volume. Three row-operation rules then make it computable by elimination, and the same rules explain why det A = 0 exactly when A is singular. All matrices are synthetic teaching examples.

The undergraduate [MIT OCW 18.06SC Linear Algebra (Fall 2011) Unit II](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/least-squares-determinants-and-eigenvalues/) gives determinants three sessions: properties, formulas and cofactors, and Cramer's rule, inverses and volume. They sit between Gram–Schmidt and eigenvalues. This lesson follows that placement and uses the course as a scope comparator only. It reproduces no MIT text, figure or problem.

## Learning objectives

By the end of this lesson, you should be able to:

1. Interpret det A as the signed area or volume scale factor of x ↦ Ax, and use det A ≠ 0 as a test for invertibility linked to pivots, rank and the null space.
2. Compute a determinant by elimination (product of pivots, with a sign change for each row exchange) and by cofactor expansion, and apply the rules for row operations, products, transposes, inverses and scalar multiples.
3. Connect the determinant to eigenvalues through det(A − λI) = 0, and explain why a determinant's size does not measure how close a matrix is to singular.

## The determinant as a volume scale factor

Apply A = [[3, 1], [1, 2]] to the unit square. The square's edges e₁ and e₂ map to the columns (3, 1) and (1, 2), so the square becomes a parallelogram. Its area is 3 × 2 − 1 × 1 = **5**. For a 2 × 2 matrix [[a, b], [c, d]], the determinant ad − bc is exactly this area, with a sign attached. Any region, not just the square, has its area multiplied by |det A| under the map, because a region can be approximated by small squares and each one scales by the same factor.

The sign records **orientation**. Exchanging the two columns of A gives [[1, 3], [2, 1]], whose determinant is 1 − 6 = −5. The parallelogram is the same, but traversing e₁ then e₂ now turns clockwise instead of counterclockwise. In three dimensions, |det A| is the volume of the parallelepiped spanned by the columns, and the sign separates right-handed from left-handed frames. A rotation has determinant +1 and a reflection has −1, as the coordinate-transform lesson noted.

**Applied reading.** Suppose a synthetic image-registration map takes coordinates in one microscope frame to another by M = [[1.2, 0.1], [0, 0.9]]. Then det M = 1.08, so a cell outline of area 120 μm² in the first frame occupies 1.08 × 120 = 129.6 μm² in the second. A linear map changes every area by the same factor, wherever the region lies.

## Three rules make the determinant computable

The determinant is the unique function of the rows of a square matrix with three properties:

1. **det I = 1.** The unit cube has unit volume.
2. **Exchanging two rows flips the sign.** This is the orientation reversal seen above.
3. **The determinant is linear in each row separately.** Multiplying one row by c multiplies the determinant by c, and a row that is a sum splits the determinant into a sum.

Several working facts follow directly:

- **Two equal rows give det = 0.** Exchanging them leaves the matrix unchanged but must flip the sign, so det = −det.
- **Adding a multiple of one row to another leaves the determinant unchanged.** By linearity, the change is a multiple of a determinant with two equal rows, which is zero. This is the elimination step.
- **A row of zeros gives det = 0.**
- **A triangular matrix has det equal to the product of its diagonal entries.** Elimination clears the off-diagonal entries without changing the determinant, leaving a diagonal matrix, and linearity pulls out each diagonal entry.
- **det(cA) = cⁿ det A for an n × n matrix**, because each of the n rows is scaled by c. It is not c det A.

## Computing by elimination

Elimination reduces A to an upper-triangular U using only row additions and, if needed, row exchanges. The determinant is then the product of the pivots, times −1 for each exchange.

**Example without exchanges.** Take A = [[2, 1, 3], [4, 5, 7], [−2, 4, 1]].

- R₂ − 2R₁ gives (0, 3, 1). R₃ + R₁ gives (0, 5, 4).
- R₃ − (5/3)R₂ gives (0, 0, 4 − 5/3) = (0, 0, 7/3).

The pivots are 2, 3 and 7/3, so det A = 2 × 3 × 7/3 = **14**.

**Example with an exchange.** Take B = [[0, 2, 1], [1, 1, 0], [3, 1, 2]]. The first pivot position holds a zero, so exchange R₁ and R₂. Then R₃ − 3R₁ gives (0, −2, 2), and adding the new second row (0, 2, 1) gives (0, 0, 3). The pivots are 1, 2 and 3, with one exchange, so det B = −(1 × 2 × 3) = **−6**.

**A singular example.** Take S = [[1, 2, 3], [2, 4, 7], [3, 6, 10]]. Then R₂ − 2R₁ = (0, 0, 1) and R₃ − 3R₁ = (0, 0, 1). The second column has no pivot, and subtracting the two new rows leaves a zero row. So det S = **0**. The same elimination shows rank 2 and the null-space vector (−2, 1, 0): S(−2, 1, 0) = 0. The columns are dependent, so the image of the unit cube is flat and has zero volume.

## Invertibility, products and inverses

For a square matrix, the following statements are equivalent. Each is a different view of the same elimination:

- det A ≠ 0;
- elimination produces n nonzero pivots;
- rank A = n, and the null space contains only the zero vector;
- the columns (and the rows) are linearly independent;
- Ax = b has exactly one solution for every b.

Three further rules are used constantly:

- **det(AB) = det A · det B.** Volume scaling composes: apply B, then A. With the matrices above, det(AB) = 14 × (−6) = −84.
- **det(A⁻¹) = 1/det A**, because AA⁻¹ = I has determinant 1.
- **det Aᵀ = det A.** Every rule stated for rows therefore also holds for columns.

There is no comparable rule for sums: det(A + B) is generally not det A + det B.

## Cofactor expansion, Cramer's rule and their cost

The determinant can also be written as a sum over one row. For row 1 of a 3 × 3 matrix,

det A = a₁₁C₁₁ + a₁₂C₁₂ + a₁₃C₁₃, where the **cofactor** Cᵢⱼ = (−1)^(i+j) times the determinant of A with row i and column j removed.

For the first example, expanding along row 1 gives 2(5·1 − 7·4) − 1(4·1 − 7·(−2)) + 3(4·4 − 5·(−2)) = 2(−23) − 18 + 3(26) = **14**, matching the pivots. Expansion is convenient when a row or column has many zeros. Its cost, however, grows like n!: a 10 × 10 expansion carried all the way down contains 10! = 3,628,800 terms, while elimination needs on the order of n³/3 ≈ 333 multiply–subtract steps. Software computes determinants by elimination, not cofactors.

Cofactors also give closed formulas. The inverse is A⁻¹ = Cᵀ/det A. For 2 × 2 matrices this is the familiar [[a, b], [c, d]]⁻¹ = (1/(ad − bc))[[d, −b], [−c, a]]. **Cramer's rule** solves Ax = b as xᵢ = det(Bᵢ)/det A, where Bᵢ is A with column i replaced by b. The calibration-line lesson used this for a 2 × 2 normal-equation system. These formulas are useful for small systems and for reasoning about how a solution depends on the data. For computation beyond very small sizes, elimination is cheaper and better behaved.

## Determinants and eigenvalues

An eigenvalue λ makes A − λI singular, since (A − λI)x = 0 has a nonzero solution x. By the invertibility test, that happens exactly when **det(A − λI) = 0**, the characteristic equation used in the eigenvalue lessons. For A = [[3, 1], [1, 2]], det(A − λI) = (3 − λ)(2 − λ) − 1 = λ² − 5λ + 5. The roots are λ = (5 ± √5)/2, approximately 3.618 and 1.382. Their product is 5 = det A and their sum is 5 = trace A. In general, det A is the product of the eigenvalues, counted with multiplicity. A zero eigenvalue and a zero determinant are therefore the same statement.

## Size is not closeness to singularity

A determinant can be tiny for a perfectly well-behaved matrix. The 10 × 10 matrix 0.1I has determinant 0.1¹⁰ = 10⁻¹⁰, yet it shrinks every direction equally, its condition number is 1, and solving with it loses no accuracy. The size of det A also depends on units: rescaling a matrix by 10 multiplies an n × n determinant by 10ⁿ without changing its geometry.

The two-sensor matrix from the conditioning and case lessons shows the reverse problem. P = [[1, 0.99], [0.99, 1]] has det P = 1 − 0.9801 = 0.0199 and eigenvalues 1.99 and 0.01, so its condition number is 199. Multiplying P by 10 gives determinant 1.99, a hundred times larger, but the condition number is still 199 and the near-dependence of the columns is unchanged. To judge how close a matrix is to singular, compare its largest and smallest singular values, as the conditioning lesson does. Do not use the raw determinant.

## Common mistakes

- Writing det(cA) = c det A instead of cⁿ det A.
- Forgetting the sign change for each row exchange during elimination.
- Assuming det(A + B) = det A + det B.
- Treating a small determinant as evidence of near-singularity, or a large one as evidence of a well-conditioned matrix.
- Concluding that a matrix is invertible because all its entries are nonzero; S above has no zero entries and determinant 0.
- Using cofactor expansion for large matrices, where its cost explodes.
- Dropping the alternating signs (−1)^(i+j) in a cofactor expansion.

## Worked example

**Problem.** For C = [[1, 2, 0], [3, 4, 1], [0, 2, 5]], compute det C by elimination, confirm it by cofactor expansion, decide whether C is invertible, and find det(2C) and det(C⁻¹).

**Step 1: elimination.** R₂ − 3R₁ gives (0, −2, 1). Then R₃ + R₂ gives (0, 0, 6). The pivots are 1, −2 and 6, with no exchanges, so det C = **−12**.

**Step 2: cofactor check.** Along row 1: 1(4·5 − 1·2) − 2(3·5 − 1·0) + 0 = 18 − 30 = **−12**.

**Step 3: invertibility.** All three pivots are nonzero, so C is invertible, its columns are independent and Cx = b has a unique solution for every b. The negative sign means the map reverses orientation. It does not affect invertibility.

**Step 4: rules.** det(2C) = 2³ × (−12) = **−96**, and det(C⁻¹) = 1/(−12) ≈ **−0.0833**.

## Limits of this lesson

All matrices are small synthetic examples in exact arithmetic. The lesson develops determinants from the row-operation rules rather than from the full permutation formula, and it treats real square matrices only. Floating-point determinants of large matrices can underflow or overflow. Software therefore often reports log |det A|, and conditioning should be assessed with singular values.
