# Assignment 3: coupled systems, forcing and conservation

A coupled-system solution should explain which states exchange amounts, how forcing enters, and why the proposed trajectory satisfies every component. This open report uses two distinct normalized systems. The first has a repeated eigenvalue and a sustained input; the second conserves a total and has a nonzero equilibrium family. These mathematical examples are not fitted transport or cellular models. Keep the derivations, code and comparisons locally; browser checkpoints assess only selected results.

## Part A: repeated eigenvalue with sustained forcing

Take

$$\mathbf x'=A\mathbf x+\mathbf b,\qquad A=\begin{pmatrix}-1&2\\0&-1\end{pmatrix},\quad\mathbf b=\begin{pmatrix}0\\1\end{pmatrix},\qquad\mathbf x(0)=\mathbf0.$$

Write $A=-I+N$ and verify $N^2=0$. The fundamental matrix is

$$\Phi(t)=e^{-t}(I+tN)=e^{-t}\begin{pmatrix}1&2t\\0&1\end{pmatrix}.$$

Differentiate this matrix and verify both $\Phi'=A\Phi$ and $\Phi(0)=I$. There is only one eigenvector direction even though there are two state dimensions; two identical exponentials without the $t e^{-t}$ term cannot supply the general homogeneous solution. The polynomial factor does not prevent asymptotic decay here.

Derive the forced solution using $\mathbf x(t)=\Phi(t)\mathbf x(0)+\int_0^t\Phi(t-s)\mathbf b\,ds$. Integrating the components gives

$$x_2=1-e^{-t},\qquad x_1=2[1-(1+t)e^{-t}].$$

At $t=1$, the values are $x_2=1-e^{-1}\approx0.632121$ and $x_1=2-4/e\approx0.528482$. The equilibrium is $(2,1)$, not zero. Compute the initial derivatives directly from the original equation and verify that $x_1'(0)=0$ while $x_2'(0)=1$. The first state starts changing only after the driven second state departs from zero.

Repeat the derivation by solving the lower equation first and using an integrating factor for the upper equation. Agreement between this triangular route and the matrix convolution gives a useful independent check. Solving $A\mathbf x_*=0$ would ignore the sustained input; identify that wrong step explicitly in your report.

## Part B: a closed conserved transfer system

Use the separate state $\mathbf z$ with

$$\mathbf z'=\begin{pmatrix}-3&1\\3&-1\end{pmatrix}\mathbf z,\qquad\mathbf z(0)=\begin{pmatrix}4\\0\end{pmatrix}.$$

Add the two component equations before doing any eigenvalue calculation. Their sum is zero, so $z_1+z_2=4$ is invariant. Substituting $z_2=4-z_1$ gives $z_1'=4-4z_1$. Therefore

$$z_1=1+3e^{-4t},\qquad z_2=3-3e^{-4t}.$$

At $t=(\ln2)/4$, the state is $(2.5,1.5)$. The matrix eigenvalues are zero and minus four. The zero mode represents a family of possible totals and equilibria; it does not make the selected initial-total trajectory drift without bound. With total four the equilibrium is $(1,3)$. Changing the total selects another equilibrium in the family.

Check nonnegative-state invariance from the vector field on each coordinate axis. At $z_1=0$ the first derivative is $z_2\geq0$; at $z_2=0$ the second derivative is $3z_1\geq0$. For this linear transfer system the continuous solution preserves the nonnegative quadrant. This is a separate claim from numerical stability or conservation by a discretization.

## Part C: compare numerical properties separately

Implement forward Euler and one implicit method for both systems. In the closed system, forward Euler updates with matrix $I+hA$. Its columns sum to one for every step, so the total is conserved algebraically, but nonnegative entries require $0\leq h\leq1/3$. Its decaying scalar mode has amplification $1-4h$, whose magnitude is at most one for $0\leq h\leq1/2$. Thus a step can be stable in that eigenmode while violating nonnegativity for some admissible initial states. At $h=0.4$, starting from $(4,0)$ gives $(-0.8,4.8)$ and still sums to four.

Use these concrete distinctions in the report: conserved total, stable amplification, positive states and accurate trajectory are four different properties. Verify the exact amplification threshold and a manufactured trajectory error under refinement. For an implicit update, solve the linear system rather than writing an explicit-looking formula without checking its matrix inverse or component signs.

For this closed matrix, backward Euler has inverse update $(I-hA)^{-1}=\frac{1}{1+4h}\begin{pmatrix}1+h&h\\3h&1+3h\end{pmatrix}$. Its entries are nonnegative and its columns sum to one for every nonnegative step. Verify those properties directly and compare the decaying-mode factor $1/(1+4h)$ with the exact factor $e^{-4h}$. Unconditional positivity and stability still do not make a large step accurate.

## Self-review and scope

Retain fundamental-matrix and convolution identities, equilibrium/initial-derivative checks, the conserved-total reduction, nonnegative-boundary arguments and the numerical-property counterexample. Explain which conclusions apply to all nonnegative starts and which use the particular initial data. A visually smooth curve and a tiny total residual do not establish every claim.

The [MIT OCW 18.03SC Fall 2011 Unit IV](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iv-first-order-systems/) is a link-only comparator for matrix solution, fundamental matrices and coupled-system interpretation. Original examples and explanations were developed with substantial AI assistance; no source code, problem or measured data was imported. Time-dependent matrix theory, general nonlinear conservation laws and qualified mathematical review remain outside this report. The package remains partial and unreviewed, and the retained report is not automatically graded.
