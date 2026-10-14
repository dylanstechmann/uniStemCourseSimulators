# LTI systems, convolution, and transfer functions

## Learning objectives

1. Interpret the pole and impulse-response description of a simple linear time-invariant system.
2. Derive a first-order zero-state transfer function from a differential equation and calculate its DC gain.

## A model maps an input to an output

A system model is a rule that relates a specified input signal to a specified output. For example, input **u(t)** might be a voltage command and output **y(t)** a measured sensor voltage. The symbols are labels, not a guarantee that the physical process is linear or that the sensor is instantaneous. Before using a model, say what is treated as the input, what is observed as the output, and what operating range the model is meant to describe.

A system is linear when it obeys superposition: scaling an input scales the output by the same factor, and adding inputs adds their corresponding outputs. If input **u₁** produces **y₁** and input **u₂** produces **y₂**, then the combined input **a u₁ + b u₂** produces **a y₁ + b y₂** for constants **a** and **b**. This statement assumes the same model and compatible initial conditions. Saturation, dead zones, thresholding, and many real sensor limits violate this rule outside a restricted operating range.

A system is time-invariant when shifting the input in time shifts the output by the same amount without otherwise changing its shape. A sensor whose response has the same lag today and tomorrow may be approximated as time-invariant; a process whose parameters change as a component heats up may not be. Linearity and time invariance are separate properties. Calling a model LTI asserts both, within a declared range and time interval.

## Impulse response summarizes an LTI model

The impulse response **h(t)** is the output produced by an ideal unit impulse under the model's zero-state condition. An impulse is a mathematical input concentrated at one instant with unit area; it is not a finite pulse with an arbitrary peak. Linearity and time invariance allow a sufficiently well-behaved continuous input to be represented as a weighted collection of shifted impulses. The output is then the corresponding weighted collection of shifted copies of **h**. The resulting convolution integral is developed in the next lesson; here the important point is that the impulse response is a compact description of the zero-state input–output behavior of an LTI system.

The [MIT OpenCourseWare lecture on convolution](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/resources/lecture-8-convolution/) develops this impulse-response connection. For a causal continuous-time system, the response cannot begin before an input is applied, so **h(t) = 0** for **t < 0**. If a causal system has an absolutely integrable impulse response, it is bounded-input/bounded-output stable: every bounded input produces a bounded output. A nondecaying impulse response can signal that this condition fails, but detailed stability tests belong to later lessons.

An impulse response and a transfer function describe related aspects of the same zero-state model. The transfer function **G(s)** is the Laplace transform of **h(t)** where the transform and its region of convergence apply. In input–output form, **Y(s) = G(s)U(s)** for zero initial conditions. The transform changes a differential equation into algebra, so it is useful for identifying modes and steady-state gain. It does not erase the assumptions: if initial stored energy is nonzero, that additional natural response must be included separately.

## Derive the transfer function from a first-order equation

Consider a model with input **u(t)** and output **y(t)**:

**dy/dt + 2y = 6u.**

Assume the coefficients stay fixed, the model is linear, and the initial output is zero for the transfer-function calculation. Taking the Laplace transform gives **sY(s) + 2Y(s) = 6U(s)**. Collecting the output terms and dividing by the input yields **G(s) = Y(s)/U(s) = 6/(s + 2)**. The factor of 6 is part of the input–output gain; dropping it would change the system being modeled.

The pole is the value of **s** that makes the denominator zero. Here the pole is **s = −2**. With time measured in seconds, its units are inverse seconds and its natural zero-input mode is proportional to **e^(−2t)**. That mode decays for positive time, consistent with a stable first-order response. The same algebra applied to **G(s) = 1/(s + 4)** places the pole at **s = −4**, which is the preserved pole-location question in this week's practice.

For a stable first-order model **τ dy/dt + y = K u**, where **τ > 0**, the zero-state transfer function is **G(s) = K/(τs + 1)**. Its pole is **−1/τ** and its DC gain is **G(0) = K**. The time constant **τ** has units of time; **s** has units of inverse time, so **τs** is dimensionless. A pole with a larger negative magnitude corresponds to a faster exponential mode when the same time units and first-order model apply. Do not compare pole numbers expressed under different time-unit conventions without converting them.

## DC gain is a steady-state ratio

The DC gain is the transfer function evaluated at **s = 0**, when a finite steady state exists under the stated input and the system is stable. Setting the derivative to zero in the first-order equation **dy/dt + 2y = 6u** gives **2y = 6u**, so **y/u = 3** for a constant input in steady state. Equivalently, **G(0) = 6/(0 + 2) = 3**. This is the preserved gain practice calculation. If the input and output use different physical units, the gain carries output-units per input-unit; a numerical value of 3 does not by itself mean a unitless gain.

This check is useful because it catches a common coefficient error. Writing **G(s) = 6/(s + 2)** and evaluating at zero gives 3; writing **1/(s + 2)** would give 0.5 and would not reproduce the original equation's steady-state balance. It also separates a pole question from a gain question: the denominator identifies natural modes, while numerator and denominator together determine the zero-frequency input–output ratio.

## Read the model within its limits

The transfer function **G(s) = Y(s)/U(s)** is a zero-state input–output description, not the full state of every physical system. A nonzero initial value contributes a zero-input response. A nonlinear sensor or a process whose parameters change with time may not have one fixed transfer function over the conditions of interest. The system boundary matters too: a transfer function for a sensor alone is not automatically the transfer function from the biological quantity of interest to a recorded voltage if the electrode, amplifier, and filter are omitted.

Pole locations help describe natural modes in a rational model, but a pole calculation is not a complete proof that a real apparatus is safe, correctly identified, or robust to delay and parameter variation. Numerator zeros can shape the response as well, and internal state behavior can require more information than an input–output ratio. Later units introduce final-value reasoning, frequency response, feedback stability, margins, sampling and controller implementation. Week 1 establishes the LTI and transfer-function language those analyses use; it does not tune a real controller or specify a sensor configuration.

When checking a calculation, start from the stated differential equation, keep its coefficients, state the zero-initial-condition assumption, and verify the DC result against the constant-input balance. Identify a pole by setting the denominator to zero, then interpret the sign only in the context of the continuous-time model and its time units. These steps connect the symbols to the model without mistaking a useful mathematical representation for a complete description of a changing physical process.
