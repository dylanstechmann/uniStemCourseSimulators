# Water-balance feedback: lags, control effort and reserve

A regulated output can remain near its reference while the controller works harder, and a stable final state can be approached with overshoot. To reason about those possibilities, separate the state balance from the sensor/effector response. This reading extends [homeostasis and feedback gain](08-homeostasis-balance-and-feedback-gain.md), [renal/endocrine regulation](04-renal-endocrine-and-integrated-regulation.md) and [compensation/reserve](14-compensation-and-reserve.md) with an original two-state model. Every parameter is normalized and invented; none is a hormone concentration, fluid-intake target or physiological time constant measured in a person.

## Define deviations and signs

Let w=(W−Wref)/Wscale be a scaled water-pool deviation, with a declared positive scale, and h a normalized water-retaining control-signal deviation. A positive h reduces loss and tends to increase w. At fixed solute amount, a lower water pool raises concentration, so a simple local negative-feedback sensor makes low w increase h. Actual regulation combines osmotic, circulatory, neural and hormonal signals; this model isolates one signed pathway.

Let u be a scaled excess-input disturbance, with the chosen input normalization absorbed into the coefficients, tauW and tauH positive response times, and g and k positive dimensionless gains. The stipulated equations are

$$\tau_W\dot w=u-w+gh,\qquad \tau_H\dot h=-h-kw.$$

The term −w describes a restoring output dependence, while gh is the effector contribution. The controller relaxes toward −kw instead of changing instantaneously. h is a deviation around a positive reference signal; a negative h means below-reference activity, not a negative absolute hormone amount. A real application would need baseline, bounds, measured transfer functions and additional balances before those variables could be interpreted physiologically.

## Solve steady balance before studying the transient

For a constant disturbance, set both derivatives to zero. Then hstar=−k wstar and wstar=u/(1+gk). The product gk is the loop gain in this selected linear model. With the controller removed, k=0, the final w is u. Feedback reduces the remaining deviation but does not force it to zero for every finite gain. Integral control or another mechanism would be a different model, not a consequence of these equations.

For a worked case take tauW=4, tauH=1 in arbitrary time units, g=1, k=3 and a step u=0.2 from w=h=0. The new steady state is wstar=0.05 and hstar=−0.15. Initially wdot=0.2/4=0.05 per time unit and hdot=0. The output moves before the lagged controller fully responds. Reporting the final deviation alone would hide the control effort and the initial excursion.

## Derive the modes and their limits

Subtract the steady state and seek deviations proportional to exp(lambda t). Eliminating either variable gives the characteristic equation

$$\tau_W\tau_H\lambda^2+(\tau_W+\tau_H)\lambda+(1+gk)=0.$$

For positive parameters, its coefficients are positive and both roots have negative real part in this two-state model. When the discriminant is negative, modes are damped oscillations. In the worked case the roots are −5/8 plus or minus i sqrt(39)/8. Oscillatory modes and a stable final state are compatible. The actual trajectory also depends on initial conditions and how the disturbance enters; do not call the modal frequency a universal biological rhythm.

Adding an explicit delay, a different sign, additional pathways or nonlinear saturation can change stability. The positive-parameter result is attached to these two equations. “Negative feedback always stabilizes every system” is a stronger and false general claim. Conversely, an oscillation in one measured signal does not uniquely identify a particular hormone loop or prove instability.

## Bound the controller and test reserve

Suppose the target −kw is clipped to a finite interval before the controller relaxes toward it. If the unclipped equilibrium requires a signal outside that interval, the earlier steady-state formula is no longer admissible. Solve the active bounded branch and check that its clipping condition holds. This resembles a contact-state check in mechanics: an algebraic result can satisfy one equation while violating an allowed-action constraint.

For the [feedback assignment](../assignments/coursework-04-feedback-and-reserve.md), tauW=2, tauH=1, g=1, k=2 and u=0.3. Unbounded equilibrium is w=0.1, h=−0.2. If the minimum allowed signal deviation is −0.1, that state is unavailable. The lower-saturated branch instead has h=−0.1 and w=0.2; its requested target −kw=−0.4 lies below the bound, so the branch is consistent. A controlled value can depart further when reserve is exhausted, even though the same nominal gains are present.

## Bias changes what is sensed

If the sensor reads w+b, the unbounded controller target becomes −k(w+b). Steady balance gives wstar=(u−gkb)/(1+gk). A changed observed signal could therefore reflect disturbance, gain, sensor bias or effector limit. One concentration or output value does not identify all these possibilities. A study should compare controlled perturbations and several endpoints rather than infer a mechanism from one apparently regulated value.

For rehearsal use tauW=3, tauH=1, g=2, k=1 and u=0.3. Derive steady state, initial derivatives and the two modal roots. Compare the unbounded and clipped versions using a local simulation. Retain state-equation residuals, the clipping condition and a refinement study; a smooth plotted curve is not verification of the biological interpretation.

## Sources and scope

[MIT OCW HST.542J Organ Transport Systems Spring 2004 calendar](https://ocw.mit.edu/courses/hst-542j-quantitative-physiology-organ-transport-systems-spring-2004/pages/calendar/) supplies link-only control/integration scope, and [OpenStax A&P 2e endocrine kidney regulation](https://openstax.org/books/anatomy-and-physiology-2e/pages/25-8-endocrine-regulation-of-kidney-function) supports the general water-retention context. The equations, parameter sets and interpretation tasks are original and developed with substantial AI assistance; no source problem, data or physiological response curve was imported. This is a local normalized model, not a complete endocrine system or a health assessment. Qualified review and measured workload remain open; the package is partial and unreviewed.
