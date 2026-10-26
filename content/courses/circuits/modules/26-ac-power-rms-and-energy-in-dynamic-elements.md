# AC power, RMS and energy in dynamic elements

An instrument is more than a signal path: it moves energy from a supply into resistive heat and into magnetic or electric storage, and its protective ratings are written in those terms. This original reading adds alternating-current power, root-mean-square bookkeeping and cycle-by-cycle energy accounting to the existing frequency-response, noise and acquisition material. Every voltage, current and component value here is an invented teaching parameter, not a mains recommendation, a safety rating or a measured instrument characterization.

## RMS is a mean-square budget

The RMS value of a periodic signal is defined by its mean square:

$$V_\mathrm{rms}=\sqrt{\frac{1}{T}\int_0^T v^2(t)\,dt}.$$

For the sinusoid $v(t)=V_p\sin\omega t$ the average of $\sin^2$ over a period is one half, so $V_\mathrm{rms}=V_p/\sqrt{2}$. Stipulate $V_p=5.00\sqrt{2}\approx 7.07$ V, so $V_\mathrm{rms}=5.00$ V, with crest factor $V_p/V_\mathrm{rms}=\sqrt{2}\approx 1.41$. Dissipation follows the mean square, so a resistor obeys $P=V_\mathrm{rms}^2/R$ in the same algebraic form as DC: the stipulated source across a $50.0\ \Omega$ resistor delivers $25.0/50.0=0.500$ W and draws $I=0.100$ A RMS. The peak current $0.141$ A matters to headroom, never to the heat: a fuse or winding carrying this current is sized by its RMS value, not its instantaneous peaks.

## Real power and the power factor

Drive instead a series load with $R=30.0\ \Omega$ and $L=40.0$ mH at $\omega=1000$ rad/s. The inductor presents $X_L=\omega L=40.0\ \Omega$, the impedance magnitude is $|Z|=\sqrt{30^2+40^2}=50.0\ \Omega$, and the current is $5.00/50.0=0.100$ A RMS, lagging the voltage by $\theta=\arctan(40.0/30.0)=53.1^\circ$. Only the in-phase component of the current carries energy on average:

$$P=V\,I\cos\theta=5.00\cdot0.100\cdot0.600=0.300\ \text{W},$$

and the resistor confirms it: $P=I^2R=0.0100\cdot30.0=0.300$ W. The quadrature component supports

$$Q=V\,I\sin\theta=5.00\cdot0.100\cdot0.800=0.400\ \text{var}$$

of reactive cycling, equal to $I^2X_L$. The factor $\cos\theta=0.600$ is the power factor of this stipulated load; it is a property of the load angle, not an efficiency.

## Energy cycles through the dynamic elements

The inductor stores $w_L=\tfrac12Li^2$, maximal at the current peak $I_p=\sqrt{2}\cdot0.100$ A:

$$W=\tfrac12\cdot0.0400\cdot(0.1414)^2=4.00\times10^{-4}\ \text{J}=0.400\ \text{mJ}.$$

The reactive power and this peak exchange are one bookkeeping: $Q=\omega W=1000\cdot4.00\times10^{-4}=0.400$ var. Over one period $T=2\pi/\omega=6.28$ ms the resistor dissipates $PT=0.300\cdot6.28=1.89$ mJ, about $4.71$ times the peak stored energy — the load burns several storage budgets per cycle. The capacitor behaves dually: its current leads, its reactive power is negative under the load sign convention, and $\omega CV^2$ replaces $\omega LI^2$.

An instrument measures this with the acquisition strand rather than trusting a label: sample $v$ and $i$ simultaneously and recover the load angle from their time offset, $\theta=\omega\,\Delta t$. A lag of $\Delta t=0.928$ ms at $1000$ rad/s is $53.1^\circ$, the same angle the algebra produced.

## Correcting the power factor

Place a capacitor in parallel with the RL load. It contributes $Q_C=\omega CV^2$ of leading reactive power at the same 5.00 V RMS. Cancelling the 0.400 var requires

$$C=\frac{0.400}{1000\cdot25.0}=1.60\times10^{-5}\ \text{F}=16.0\ \mu\text{F}.$$

The load still consumes exactly 0.300 W, but the source now supplies only real power: $I=P/V=0.300/5.00=0.0600$ A RMS instead of 0.100 A. Through a stipulated $5.00\ \Omega$ delivery resistance the line loss falls from $0.100^2\cdot5.00=50.0$ mW to $0.0600^2\cdot5.00=18.0$ mW. Nothing was gained inside the load; only the cycling current in the line shrank. The same bookkeeping, at enormously larger scale, is why grid and converter engineers track power factor; that is context for the arithmetic, not a claim about any real instrument here.

## Instrument connection and boundaries

Fuse ratings, supply budgets and amplifier thermal limits are RMS quantities, and crest factor separates the peak that clips from the heat that accumulates. The comparator for this unit is [MIT OCW 6.002 Circuits and Electronics, Spring 2007 calendar](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/calendar/) session L24 "Energy and power" with recitation R24, whose assigned readings are Agarwal and Lang, *Foundations of Analog and Digital Electronic Circuits* (Morgan Kaufmann, 2005) chapters 11.1–11.3 and 11.5, per the public [readings page](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/readings/); both are link-only scope comparators. The CMOS switching-power portion of R24 is deliberately not developed here and is recorded as an optional beyond-scope strand in the syllabus.

## Common mistakes

Do not size a fuse or thermal budget from a peak value, quote a power factor without its load angle, or call reactive power a loss: the 0.400 var cycles through the inductor and back. Do not treat a corrected power factor as a change inside the load; the load's 0.300 W is untouched, and only the line current improved.

## Limits of this lesson

All sources, loads and lines are stipulated synthetic parameters at a teaching frequency of 1000 rad/s, far from mains frequencies. No insulation, grounding, mains or safety guidance is provided or implied, and no real component, instrument or supply is characterized.