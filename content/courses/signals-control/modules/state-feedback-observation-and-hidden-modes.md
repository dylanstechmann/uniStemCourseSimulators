# State feedback, observation and hidden modes

A transfer function describes zero-initial-state input/output behavior. A state realization also describes internal motion and nonzero initial conditions. This original foundation checks controllability and observability before designing a selected feedback/observer pair, then gives a stable transfer function with an unstable internal mode. All matrices and signals are normalized synthetic models.

## Write the realization and its information tests

Use xdot=A x+B u, y=C x with no direct term. For two states, controllability matrix is [B, A B] and observability matrix has rows C, C A. Rank two means the corresponding full-state property holds in these two-dimensional examples. A rank test concerns the supplied model and chosen input/output; it does not prove sensors or actuators provide that information physically.

For a worked canonical plant A has rows (0, 1), (-2, -3), B=(0, 1)' and C=(1, 0). Its transfer function is 1/(s²+3s+2), and both rank tests give two. Feedback u=−K x+N r with K=(14, 5), N=16 places the poles at the repeated value -4 and gives unit constant-reference steady gain. An observer with L=(8, 4)' has error poles -5 and -6.

These gains follow coefficient matching for this model. They are not a general optimal design, noise filter or a real-device prescription. A repeated negative pole can produce a polynomial times exponential, so transient shape needs more than an unordered pole list.

## A distinct fully specified rehearsal

Use A with rows (0, 1), (-6, -5), the same B and C. The controllability matrix has rows (0, 1), (1, -5), and observability is the identity. Both have rank two. The open-loop zero-initial-state DC transfer gain is one sixth.

For K=(k1, k2), A−B K has characteristic s²+(5+k2)s+(6+k1). Target poles -5 and -6 give polynomial s²+11s+30, so K=(24, 6). Reference multiplier N=30 gives unit constant-reference gain for this exact plant. Derive it from the equilibrium or transfer equation; a stabilizing feedback alone does not set a unit reference gain.

State feedback requires the state or an estimate of it. Measuring only y=x1 does not directly provide both state components. That is why observability and an observer model matter here.

## Derive an observer rather than asserting a hidden measurement

Let the estimate obey xhatdot=A xhat+B u+L(y−C xhat). With common known input u and exact matrices, error e=x−xhat obeys edot=(A−L C)e. For L=(l1, l2)', the rehearsal error characteristic is s²+(5+l1)s+(5l1+6+l2).

Target observer poles -8 and -9 give s²+17s+72. Thus L=(12, 6)' and the slow observer pole is -8. These error modes describe the stipulated noise-free exact-model estimator; they do not guarantee accurate inference with unknown disturbances or arbitrary measurement noise.

With u=−K xhat+N r, write the combined system in coordinates (x, e). Its matrix is block upper triangular, with diagonal blocks A−B K and A−L C and upper-right block B K. The four poles are the union of the two designed pairs. This separation follows from the exact linear equations; saturation or model/input mismatches need a new analysis. Stable modes also do not imply a monotone state norm at every instant.

## Stable transfer behavior can hide internal growth

For a separate realization choose A=diag(-1, 2), B=(1, 0)' and C=(1, 1). The zero-initial-state transfer function reduces to 1/(s+1). Its convolution map is stable, but the second state follows x2(t)=x2(0)exp(2t) independently of the input. A nonzero second initial state therefore grows and appears in the output.

Controllability rank is one and observability rank is two. The unstable mode is observable but cannot be actuated through the chosen input. Setting its initial value to zero suppresses it for that ideal experiment; it does not stabilize the realization or make the mode disappear from its physics.

Changing instead to B=(1, 1)' and C=(1, 0) gives an unobservable unstable second state with the same transfer function. These examples show why canceled input/output poles do not establish internal stability. For a minimal realization, transfer poles represent all its modes; nonminimal models need the explicit state test.

Choosing faster observer poles is not automatically a better estimate. The correction multiplies measurement error by L, so an omitted noise model can make a fast design look more informative than it is. Pole placement supplies modal locations under the supplied equations; it does not optimize noise, range or uncertain-model performance.

## Verification and boundary

Retain A, B, C, rank calculations, characteristics, equilibrium reference gain, observer error and combined matrix. Compare analytic modes with direct integration for both zero and nonzero initial states. [MIT OCW 16.30 Fall 2010 lecture topics](https://ocw.mit.edu/courses/16-30-feedback-control-systems-fall-2010/pages/lecture-notes/) 5–16 provide link-only selected state/feedback/observer scope. This bounded two-state extension does not deliver that entire course or its classical-design/software prerequisites. All examples and derivations are original and AI-assisted; no source exercise, code, figure or data is imported. General state-space synthesis, robust/noisy estimation, physical implementation and qualified review remain open; the package stays partial and unreviewed.
