# Nonlinear load lines and local circuit models

A linear port can be replaced by a Thevenin source over its stated operating domain. A nonlinear device needs a different first step: solve its operating point, then derive a local model if the perturbation is small enough. This original reading adds an ideal exponential junction to the existing nodal/port and amplifier material. All values are invented teaching parameters, not a measured device, component recommendation or hardware procedure.

## Stipulate a constitutive law and a network

Choose the ideal junction law $I=I_S[\exp(V_D/V_T)-1]$, with positive current flowing from the source through a series resistance and into the positive diode terminal. Here $I_S$ and $V_T$ are stipulated positive model coefficients; this exercise does not infer their values from a real temperature or junction. A source $V_S$ and resistance R impose $V_S=V_D+RI$.

The nonlinear operating point solves

$$F(V_D)=V_D+RI_S[\exp(V_D/V_T)-1]-V_S=0.$$

For a positive source, $F(0)<0$ and $F(V_S)>0$. Its derivative $F'=1+(RI_S/V_T)\exp(V_D/V_T)$ is positive, so a unique root lies between zero and $V_S$. A bracketed method preserves this admissible interval. Newton's method can be fast, but a small update or an optimizer success flag does not substitute for the original voltage and device residuals.

A piecewise constant-drop approximation is a different constitutive model, not the same equation with fewer displayed digits. Its usefulness depends on the intended accuracy and operating range. The stipulated exponential model also omits breakdown, capacitance, self-heating and other real effects. An algebraic solution outside a model's intended range is not validation of those omissions.

## Worked forward point

Use $V_S=2$ V, R=1000 ohms, $I_S=10^{-12}$ A and $V_T=0.025$ V. Solving the original scalar equation gives $V_D\approx0.52775142$ V and $I\approx1.47224858$ mA. Reconstruct $V_D+RI$ and compare it with the source. Verify the exponential device current independently rather than obtaining both currents by the same subtraction.

The static ratio $V_D/I$ is about 358 ohms, but it is not the incremental resistance. The local derivative is

$$r_d=\left(\frac{dI}{dV_D}\right)^{-1}=\frac{V_T}{I+I_S},$$

giving about 16.9808 ohms at this point. These quantities answer different questions: one is a ratio of the finite bias values and the other relates small changes near that bias. A nonlinear device cannot generally be replaced by one bias-independent resistor for every signal or source level.

## Derive a source-to-device sensitivity

Differentiate both the load line and device law at the operating point: $dV_S=dV_D+R\,dI$ and $dV_D=r_d\,dI$. Therefore

$$\frac{dV_D}{dV_S}=\frac{r_d}{R+r_d},\qquad\frac{dI}{dV_S}=\frac1{R+r_d}.$$

The source resistance participates in the incremental transfer; $r_d$ alone is not the complete circuit. This local result assumes the same constitutive law and topology, without an added dynamic state. Junction capacitance would require a frequency-dependent model with additional assumptions.

Compare a small mathematical source perturbation with a re-solved nonlinear point. Record the sign, absolute linearization error and error as the perturbation is halved. Do not infer a universal allowable signal amplitude from one successful perturbation; the model curvature and intended tolerance determine the comparison.

## Distinct rehearsal and power ledger

Choose a rehearsal bias current of 2 mA with R=500 ohms, $I_S=10^{-12}$ A and $V_T=0.025$ V. Its diode voltage is $0.025\ln(1+2\times10^9)\approx0.53541032$ V and the required source is about 1.53541032 V. These constructed values define a separate mathematical point, not another measurement of the worked device.

The exact incremental resistance retains $I+I_S$ in the denominator and is approximately 12.5 ohms. Source-to-diode incremental transfer is about 0.02439024. Keep unrounded values for subsequent checks. At this rehearsal point, diode power is approximately 1.07082065 mW and resistor power is 2 mW, totaling source power 3.07082065 mW.

The identity $V_SI=V_DI+RI^2$ follows from the original voltage equation. It is an independent ledger from the device's exponential residual: a wrong device law can still close a network power sum at a chosen voltage/current pair. Preserve both checks and the constitutive assumptions.

## Limits and connection to a circuits course

A local small-signal model does not provide a global Thevenin equivalent of the nonlinear junction. Reverse current in the stipulated law tends toward a small model value rather than describing real breakdown, and no transient is included. Keep voltage/current references and the valid neighborhood visible in any report.

[MIT OCW 6.002 Spring 2007 calendar](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/calendar/) places nonlinear resistors and small-signal analysis in lectures 6–7 before analog amplifiers. It is a link-only scope comparator. All explanations and cases here are original and AI-assisted; no source circuit drawing, problem or measured data is imported. Device physics, broad semiconductor behavior, actual specifications and qualified review remain outside this selected model. The course stays partial and unreviewed.
