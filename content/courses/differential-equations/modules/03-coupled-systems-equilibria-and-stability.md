# Coupled systems, equilibria, and stability

A coupled dynamical system tracks several changing states together. For a state vector $\mathbf{x}(t)$, write

$$\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x}).$$

An equilibrium $\mathbf{x}^*$ satisfies $\mathbf{f}(\mathbf{x}^*)=\mathbf{0}$, so every component has zero instantaneous rate there. An equilibrium is a state, not necessarily the only long-term outcome. To ask whether nearby states return or move away, study small perturbations around it.

## Linearize near an equilibrium

Let $\boldsymbol{\delta}=\mathbf{x}-\mathbf{x}^*$. For a differentiable model, a Taylor expansion gives

$$\dot{\boldsymbol{\delta}}=J\boldsymbol{\delta}+O(\lVert\boldsymbol{\delta}\rVert^2), \qquad J=\left.\frac{\partial\mathbf{f}}{\partial\mathbf{x}}\right|_{\mathbf{x}^*}.$$

The Jacobian $J$ records how each state rate changes when each state is perturbed. Close enough to the equilibrium, the linear system $\dot{\boldsymbol{\delta}}=J\boldsymbol{\delta}$ captures the leading behavior when its linear modes dominate the higher-order terms. Its solution is assembled from modes of the form $\mathbf{v}e^{\lambda t}$, where $\lambda$ and $\mathbf{v}$ are an eigenvalue and eigenvector of $J$.

The real part of an eigenvalue sets growth or decay of that mode. A negative real part makes the mode decay; a positive real part makes it grow. A nonzero imaginary part adds oscillation. Eigenvalues have inverse-time units, so their numerical values depend on the time unit used in the model.

## Classify the local modes

For a two-state system, a few common patterns are useful:

- If both eigenvalues are real and negative, nearby perturbations decay without a sustained oscillation (a stable node in the usual two-dimensional case).
- If the eigenvalues are complex conjugates with negative real part, the state spirals toward the equilibrium while oscillating. The real part sets the exponential envelope; the imaginary part sets the angular frequency.
- If eigenvalues have real parts of opposite sign, at least one mode grows and the equilibrium is a saddle, hence unstable.
- If any eigenvalue has positive real part, an arbitrarily small perturbation in its growing direction moves away locally. One positive mode is enough for instability.

When every eigenvalue has a strictly negative real part, the linearized modes decay and a smooth nonlinear system is locally asymptotically stable at that hyperbolic equilibrium. If at least one eigenvalue has positive real part and none is on the imaginary axis, the equilibrium is unstable. When an eigenvalue has zero real part—including a zero eigenvalue or a purely imaginary pair—the linearization alone is inconclusive: nonlinear terms may decide whether nearby states return, drift, or depart.

**Worked examples.** For $J=\begin{bmatrix}0&1\\-2&-3\end{bmatrix}$, the characteristic polynomial is $\lambda^2+3\lambda+2=(\lambda+1)(\lambda+2)$. Both modes decay, with time constants 1 and 0.5 time units. For $J=\begin{bmatrix}-1&-2\\2&-1\end{bmatrix}$, the eigenvalues are $-1\pm2i$: perturbations oscillate at angular frequency 2 while their amplitude decays as $e^{-t}$, so the linearized equilibrium is a stable spiral. If a different system has eigenvalues $-2$ and $+0.1$, the positive mode makes the equilibrium unstable; the negative mode cannot cancel it in every direction.

## Locate equilibria with nullclines

In a two-dimensional model $\dot{x}=f_1(x,y)$ and $\dot{y}=f_2(x,y)$, the nullcline for $x$ is where $f_1=0$ and the nullcline for $y$ is where $f_2=0$. Their intersections are equilibria because both state rates vanish there. Away from a nullcline, the sign of each component tells whether its state is increasing or decreasing, which helps sketch local direction fields and identify candidate basins or boundaries.

Nullclines locate candidates but do not by themselves classify the equilibrium. Compute the Jacobian at each intersection and examine its eigenvalues. A nonlinear system may have several equilibria with different local stability, and trajectories far from one equilibrium can approach another state, hit a physical boundary, or enter a nonlinear cycle. A local eigenvalue result does not establish global behavior.

## A two-state linear example

For $\dot{\mathbf{x}}=A\mathbf{x}$, the origin is an equilibrium. If $A$ has eigenvalues $-1\pm2i$ s$^{-1}$, the modal perturbation rotates with period $2\pi/2=\pi$ s while its amplitude shrinks with a 1 s time constant. If instead the eigenvalues are $-2$ and $+0.1$ s$^{-1}$, the origin is unstable because one mode grows. The sign pattern gives the local classification, but eigenvectors are needed to determine which combinations of the original states align with those modes.

## Check the assumptions

Linearization is a local approximation around a particular equilibrium and parameter set. It assumes the model is differentiable there and the state perturbation is small enough for higher-order terms to be secondary. Changing parameters can move equilibria and change the Jacobian; a local classification can then change. A zero or purely imaginary eigenvalue calls for additional analysis such as higher-order terms, a Lyapunov function, or direct study of nearby trajectories.

Keep the state definitions, equilibrium, time units, and parameter values attached to the Jacobian. For a nonlinear system, report that the conclusion is local and state whether the eigenvalues are hyperbolic (none has zero real part). Do not turn a local stability result into a claim about every initial condition.

## Common mistakes

- Calling a state an equilibrium when only one component of its rate is zero.
- Using the Jacobian at the wrong point or forgetting that its entries depend on the equilibrium and parameters.
- Calling a mixed-sign pair stable because one eigenvalue is negative.
- Reading an imaginary component as growth instead of oscillation frequency.
- Treating zero-real-part modes as stable or unstable from linearization alone.
- Inferring global behavior from a local eigenvalue calculation.
