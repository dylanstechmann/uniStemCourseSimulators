# Second-order RLC transients, damping, resonance and impedance

A resistor, inductor and capacitor can store and dissipate energy while producing a response that changes over time. This lesson uses one constructed series RLC circuit to connect its step response with its sinusoidal steady state. The values are ideal teaching parameters, not a design specification.

## Natural frequency and damping

For a series RLC with constant components, the unforced charge equation is

$$
L\frac{d^2q}{dt^2}+R\frac{dq}{dt}+\frac{q}{C}=0.
$$

The undamped natural angular frequency and damping coefficient are

$$
\omega_0=\frac{1}{\sqrt{LC}},\qquad \alpha=\frac{R}{2L}.
$$

The damping ratio is $\zeta=\alpha/\omega_0=(R/2)\sqrt{C/L}$. If $\zeta<1$, the natural response oscillates with an exponentially shrinking envelope; if $\zeta=1$, it is critically damped; if $\zeta>1$, it is overdamped. For the underdamped case, $\omega_d=\sqrt{\omega_0^2-\alpha^2}$ is the damped angular frequency. These classifications follow from the linear model's characteristic roots.

Use the constructed values $R=20\,\Omega$, $L=10\,\mathrm{mH}=0.010\,\mathrm{H}$ and $C=10\,\mathrm{\mu F}=10\times10^{-6}\,\mathrm{F}$. Then $\omega_0=3162.3\,\mathrm{rad/s}$, $f_0=\omega_0/(2\pi)=503.3\,\mathrm{Hz}$, $\alpha=1000\,\mathrm{s^{-1}}$, and $\zeta=0.3162$. The circuit is underdamped and $\omega_d=3000\,\mathrm{rad/s}$.

## A step transient and the long-time limit

For a positive voltage step $V_s$ applied at $t=0$, with zero initial current and an initially uncharged capacitor, the ideal series current is

$$
i(t)=\frac{V_s}{L\omega_d}e^{-\alpha t}\sin(\omega_d t),\quad t\geq0.
$$

Take positive current from the source through $R$, $L$ and $C$. At $t=0$, current is zero, while its initial slope is $di/dt=V_s/L$: a positive step gives a positive initial rise. With a 1.0 V step and the values above, at $t=0.50\,\mathrm{ms}$,

$$
i=\frac{1.0}{(0.010)(3000)}e^{-0.5}\sin(1.5)\approx0.02017\,\mathrm{A}.
$$

The exponential envelope represents energy lost through the resistor in the unforced response. After a DC step has settled, the ideal capacitor is charged to the source voltage, the inductor has zero voltage, and the series current is zero. This steady-state check is a useful guard against treating an initial oscillation as a permanent DC current.

The capacitor and inductor store energy as $E_C=\tfrac12Cv_C^2$ and $E_L=\tfrac12Li^2$. For example, a 1.0 V capacitor state stores $0.5(10\,\mathrm{\mu F})(1.0\,\mathrm{V})^2=5.0\,\mathrm{\mu J}$. In an ideal unforced LC exchange, energy moves between the electric and magnetic fields; with $R>0$, the resistor dissipates energy and the natural response decays.

## Sinusoidal steady state, impedance and phase

For a sinusoidal source at angular frequency $\omega$, the series impedance is

$$
Z(\omega)=R+j\left(\omega L-\frac{1}{\omega C}\right),\qquad |Z|=\sqrt{R^2+\left(\omega L-\frac{1}{\omega C}\right)^2}.
$$

The sign of the net reactance $X_L-X_C$ matters. Below $f_0$, $X_L-X_C<0$, so impedance is net capacitive: its phase is negative and current leads the source. Above $f_0$, the net reactance is positive and current lags. At $f_0$, $X_L=X_C$; impedance is the real resistance $R$, and the source current is in phase with the voltage. For a fixed sinusoidal source amplitude, the ideal series-circuit current magnitude is largest at this resonance, but remains finite when $R>0$.

For the same constructed circuit at 250 Hz, $X_L=15.71\,\Omega$, $X_C=63.66\,\Omega$, and $X_L-X_C=-47.95\,\Omega$. Thus $|Z|\approx51.96\,\Omega$ and the impedance phase is about $-67.4^\circ$; a 1.0 V RMS source gives about 19.2 mA RMS, with current leading the source by about $67.4^\circ$. A series quality factor at resonance is $Q=\omega_0L/R=1/(2\zeta)\approx1.58$. Larger $Q$ means a narrower, less damped resonance in this idealized model; it is not a general guarantee about a component's measured behavior.

## Limits and relation to a circuits course

The calculations assume a lumped, linear series circuit with constant ideal components and an ideal source. They omit source resistance, inductor winding resistance, capacitor equivalent series resistance, parasitics, component tolerances, nonlinear devices, wiring and measurement loading. Tolerances can shift both the resonant frequency and damping; a real network may not have the predicted response. Do not use these examples as a hardware design or safety limit.

MIT OCW 6.002, *Circuits and Electronics* (Spring 2007), is an undergraduate comparator. Its calendar proceeds from second-order transients (L16), through damping (L17), sinusoidal frequency response (L18), impedance methods (L19), and filters and Q (L20), then returns to energy and power (L24). This short original lesson is one local topic unit; it is not a reconstruction of the course's digital, transistor, amplifier, lab or assessment sequence.
