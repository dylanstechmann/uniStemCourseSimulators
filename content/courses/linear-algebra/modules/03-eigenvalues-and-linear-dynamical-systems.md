# Eigenvalues and linear dynamical systems

An eigenvector is a direction that a matrix sends to a scalar multiple of itself: (Av=\lambda v), where (v\ne0). The eigenvalue \(\lambda\) tells how that direction is scaled in one matrix application. This simple relation becomes useful in a dynamical system because repeated updates or continuous evolution apply the same linear map again and again. When the state can be decomposed into eigenvector directions, each component evolves according to its own eigenvalue.

The eigenvalues themselves are the roots of the characteristic equation det(A − λI) = 0; the [determinants lesson](14-determinants-volume-row-operations-and-invertibility.md) explains why that test detects exactly the values of λ that make A − λI singular.

## Learning objectives

By the end of this lesson, you should be able to:

1. Interpret eigenvalues in discrete- and continuous-time linear dynamics.
2. Connect diagonalization to mode-by-mode behavior.

## Decompose the state into modes

Suppose (A) has (n) linearly independent eigenvectors. Put them into the columns of (V), and put their eigenvalues on the diagonal of \(\Lambda\). Then

\[
A=V\Lambda V^{-1}.
\]

Writing the initial state as (x_0=Vc) expresses it as a combination of eigenvector modes. In discrete time, for

\[
x_{k+1}=Ax_k,
\]

the state after (k) updates is

\[
x_k=A^kx_0=V\Lambda^k c.
\]

The component along eigenvector (v_i) is multiplied by \(\lambda_i^k\). If \(|\lambda_i|<1\), that mode decays; if \(|\lambda_i|>1\), its magnitude grows; if \(\lambda_i<0\), its sign alternates as it is scaled. A complex eigenvalue pair produces rotating or oscillating components, with magnitude controlled by \(|\lambda_i|^k\).

The vector (c=V^{-1}x_0) matters. A fast-growing eigenmode has no effect on a particular trajectory if that trajectory has zero component in its direction, though perturbations can introduce one. Eigenvalues characterize the system map; the initial condition determines which modes are present in a trajectory.

## Worked example: discrete modes

Take

\[
A=\begin{bmatrix}0.8&0\\0&-0.5\end{bmatrix}, \qquad
x_0=\begin{bmatrix}1\\2\end{bmatrix}.
\]

The coordinate axes are eigenvectors. After three steps,

\[
x_3=\begin{bmatrix}0.8^3&0\\0&(-0.5)^3\end{bmatrix}
\begin{bmatrix}1\\2\end{bmatrix}
=\begin{bmatrix}0.512\\-0.25\end{bmatrix}.
\]

The first component decays without changing sign. The second decays while alternating sign. In general, if all eigenvalues of a finite-dimensional discrete-time linear system have magnitude below 1, every mode tends to zero. An eigenvalue on the unit circle does not decay, and a Jordan block can add polynomial growth; therefore “magnitude at most 1” alone is not enough to conclude asymptotic decay.

## Continuous-time modes

For

\[
\dot{x}=Ax,
\]

the solution is (x(t)=e^{At}x(0)). Along an eigenvector (v_i) with eigenvalue \(\lambda_i\),

\[
e^{At}v_i=e^{\lambda_i t}v_i.
\]

Thus the real part of \(\lambda_i\) controls the exponential envelope. A negative real part means decay; a positive real part means growth. If \(\lambda=\alpha+i\beta\), the associated real motion oscillates with an envelope proportional to \(e^{\alpha t}\); \(\beta\) sets the angular frequency in the chosen time unit. For the scalar equation \(\dot{x}=-2x\), (x(t)=x(0)e^{-2t}\). Its e-folding time is (1/2) time unit because the amplitude is multiplied by \(e^{-1}\) after that interval.

For a finite-dimensional continuous-time linear system, the origin is asymptotically stable when every eigenvalue has strictly negative real part. An eigenvalue with positive real part creates a growing direction. Eigenvalues on the imaginary axis require more care: a simple oscillatory mode may remain bounded without decaying, while a defective eigenvalue can produce polynomial growth. A stability conclusion should state the time model and check all eigenvalues, not just the trace or a few matrix entries.

## Markov and transition matrices

A transition matrix updates a state from one step to the next. In a Markov model, a stationary distribution is unchanged by the update and corresponds to an eigenvalue of 1, with row- or column-vector conventions determining which side the matrix acts on. Other eigenvalues describe how deviations from that stationary mode evolve. Under suitable transition conditions, modes with magnitude below 1 decay and the distribution approaches stationarity; a mode near magnitude 1 decays slowly. Periodicity, multiple stationary classes, and the direction of the update can change the conclusion, so a transition matrix is not automatically a convergence guarantee.

## When diagonalization does not apply directly

Not every matrix has a complete set of independent real eigenvectors. A real matrix can have complex eigenvalues, and a repeated eigenvalue may have too few independent eigenvectors. In that case, the matrix cannot be written as (V\Lambda V^{-1}) over the real numbers in the proposed form. Generalized eigenvectors and Jordan form describe the missing directions; their solutions include polynomial factors such as (t e^{\lambda t}) or (k\lambda^k). The exponential or power still governs long-term behavior when its magnitude is strictly below or above the stability boundary, but short-term trajectories can look different from a pure exponential mode.

Even when a matrix is diagonalizable, eigenvectors need not be orthogonal. If they are nearly parallel, small changes in the initial state or matrix can strongly alter the modal coefficients. A system with decaying eigenvalues can also show temporary amplification before it decays, especially when eigenvectors are non-orthogonal. Eigenvalues summarize modal rates; they do not by themselves report every transient or sensitivity effect.

## Linearization is local

For a nonlinear model near an equilibrium, a matrix (A) may describe the first-order linearization. Its eigenvalues characterize nearby behavior under the linear approximation. The conclusion is local: far from the equilibrium, nonlinear terms can dominate, change which states are reachable, or create other equilibria and cycles. State where the model was linearized, the units and time scale, and the range over which the approximation is expected to be useful.

## Common reasoning errors

- Using the continuous-time real-part rule for a discrete-time update, where eigenvalue magnitude is the key quantity.
- Assuming that one eigenvalue below 1 makes every discrete mode decay.
- Inferring stability from the trace, determinant, or signs of entries without examining the spectrum.
- Assuming a matrix is diagonalizable merely because it has eigenvalues.
- Treating a stable eigenvalue spectrum as proof that no transient growth occurs.
- Extending a local linearization result to all states of a nonlinear system.

## Further study

MIT OpenCourseWare 18.06SC, *Linear Algebra*, Massachusetts Institute of Technology, offers independent study materials for [Diagonalization and Powers of A](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/least-squares-determinants-and-eigenvalues/diagonalization-and-powers-of-a/) and [Differential Equations and \(e^{At}\)](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/least-squares-determinants-and-eigenvalues/differential-equations-and-exp-at/). These links are for further study; no source text or problem has been reused in this reading.

## Limits of this lesson

The calculations illustrate linear models with known matrices. In applications, the matrix is estimated, the system may be noisy or time-varying, and a local linear approximation may not hold outside a neighborhood. Eigenvalues organize the behavior of the stated model; they do not validate that model or its assumptions.
