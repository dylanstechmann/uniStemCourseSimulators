# Feedback, stability, and robustness

## Learning objectives

1. Derive the closed-loop transfer function for a single-input, single-output negative unity-feedback model.
2. Explain nominal stability, gain margin, and robustness to model uncertainty without treating them as interchangeable guarantees.

## Close the loop by comparing output with reference

An open-loop model describes a forward path from a command to an output. Feedback adds a measurement of the output and compares it with a desired reference. For negative unity feedback, the measured output is subtracted from the reference, giving the error **e = r − y**. A forward transfer function **G(s)** maps this error to output, so **y = G e**. These equations establish both the sign convention and the chosen system boundary before any algebra begins.

Substitute the error equation into the plant relation:

**y = G(r − y) = Gr − Gy.**

Collecting the terms in **y** gives **(1 + G)y = Gr**, so the closed-loop transfer function from reference to output is **T(s) = y/r = G/(1 + G)**. The plus sign in the denominator follows from negative feedback: the error subtracts the measured output. For positive feedback, the corresponding ideal expression would be **G/(1 − G)**, so confusing the summing-junction sign changes the characteristic equation and can change stability. The preserved unity-feedback question asks for the negative-feedback expression.

The [MIT OpenCourseWare analysis-of-feedback lecture](https://ocw.mit.edu/courses/2-004-systems-modeling-and-control-ii-fall-2007/resources/lecture12/) is a link-only reference for loop modeling. Unity feedback means the measurement path is one, not that the forward plant has unit gain. If the sensor has transfer function **H(s)**, the measured signal is **Hy**, the error is **r − Hy**, and the reference-to-output transfer becomes **G/(1 + GH)**. That different block diagram should not be silently replaced by the unity-feedback formula.

## Follow reference tracking and disturbances separately

The denominator **1 + G(s)** is called the closed-loop characteristic factor in this unity-feedback model. Its roots determine the modeled closed-loop natural modes when the transfer functions are proper and the internal realization is represented correctly. A stable open-loop plant does not guarantee a stable closed loop: closing the loop introduces the factor **1 + G**, whose roots can lie in an unstable region. Conversely, a stable closed-loop response is only a property of the stated model and assumptions.

For unity feedback, define the sensitivity function **S = 1/(1 + G)** and the complementary sensitivity **T = G/(1 + G)**. These satisfy **S + T = 1**. The reference reaches the output through **T**; the reference-to-error ratio is **S**. Where the loop gain **|G|** is large and the phase relation is favorable, **|S|** can be small, so some low-frequency tracking errors or disturbances are reduced. Where the loop gain is small, the output generally follows the plant's open-loop response more closely. This is a frequency-dependent trade-off, not a statement that feedback removes every disturbance.

Disturbance and noise enter at different points in a block diagram and therefore have different transfer paths. A load disturbance added at a plant input is shaped by the plant and controller and then by the feedback denominator. Measurement noise is injected in the sensor path and can be followed by the controller as if it were a real error. Raising loop gain may improve tracking in one band while increasing control effort or noise response elsewhere. This course uses “negative feedback” to specify the intended subtraction; real sensor polarity and wiring still have to agree with that model.

## Stability and performance answer different questions

For a continuous-time linear model, asymptotic stability means its natural modes decay with time after an initial disturbance. For a rational single-input, single-output transfer model, this is commonly assessed from closed-loop poles, subject to assumptions about cancellations and the internal state realization. A response can be stable yet too slow, too noisy, or inaccurate for a specified task. Stability alone does not establish acceptable tracking or uncertainty tolerance.

A nominal model uses one fixed set of parameters and dynamics. A physical system can differ because a gain is uncertain, a time constant drifts, a sensor adds delay, or a neglected mode becomes important. Robustness asks whether stability or performance persists across a stated range of such model changes. A conclusion is only as broad as the uncertainty set examined: testing a few parameter values does not prove behavior under every possible change.

## Read the gain-margin item in its limited setting

Gain margin compares a nominal loop with the additional scalar loop gain that would bring the loop magnitude to one at a frequency where its phase reaches the critical −180° condition. If the magnitude there is **|L| = 0.4**, the simple linear gain-margin factor is **GM = 1/0.4 = 2.5**. The preserved practice item asks for this factor. It is not 2.5 dB; converting to decibels would require **20 log₁₀(2.5)**. The later stability-margin lesson develops crossover frequencies, phase margin, delay margin, and cases with more complicated crossings.

This calculation is conditional on a nominal open-loop frequency response and the stated crossover. It does not independently prove that the full closed-loop realization is stable, that all relevant crossings were found, or that a real process can safely tolerate a 2.5-fold gain increase. Unmodeled dynamics, delays, actuator saturation and changed operating conditions can invalidate the simple prediction. The [MIT OpenCourseWare gain- and phase-margin notes](https://ocw.mit.edu/courses/2-004-systems-modeling-and-control-ii-fall-2007/resources/lecture30/) are a link-only technical reference; detailed margin analysis is reserved for the following stability-margin unit.

## Treat feedback as a model, not a device instruction

An algebraic loop diagram is useful only if the reference, measured output, feedback sign, controller, plant, disturbance locations and noise path are labeled. Moving a sensor or adding a filter changes the model. The later PI and sampled-control lessons examine integral action, actuator saturation, implementation delay and measurement filtering in more detail. This lesson does not prescribe a controller gain or test procedure for an incubator, medical sensor or other physical device; its systems and parameters are teaching models.

When checking the loop equation, write the signed error first and substitute it into the forward relation. For negative unity feedback, **y = G(r − y)** must yield **G/(1 + G)**. Then distinguish the reference path from the error and disturbance paths. Interpret the roots and gain margin only for the model and frequency conditions provided, and state separately what remains uncertain about the physical system.
