# Growth kinetics and process mass balance

Cell growth is a rate, while viable cell concentration is a state. A reactor balance connects the state to growth, loss, and any material entering or leaving. Keeping those quantities distinct makes an exponential-growth estimate useful without treating one fitted rate as a permanent property of a cell line.

## Exponential growth over a valid interval

During an interval with approximately constant specific growth rate $\mu$ and negligible death, viable cell concentration $X_v$ follows

$$\frac{dX_v}{dt}=\mu X_v, \qquad X_v(t)=X_{v,0}e^{\mu t}.$$

The units of $\mu$ are inverse time. Taking logs gives $\mu=\ln(X_v(t)/X_{v,0})/t$ for two observations in that phase. A plot of $\ln X_v$ against time is approximately linear over the fitted interval, and its slope estimates $\mu$. With a doubling time $t_d$, $\mu=\ln 2/t_d$ and $t_d=\ln 2/\mu$.

**Worked example.** If viable concentration rises from 0.5 to 2.0 million cells/mL over 48 hours, the fold increase is four, so $\mu=\ln(4)/48=0.0289$ h$^{-1}$. The doubling time is $\ln(2)/\mu=24$ h. This estimate describes that measured interval and its culture conditions; it is not a universal rate for that cell line.

Real cultures move through lag, exponential, nutrient-limited, stationary, and decline phases. Nutrient depletion, oxygen limitation, waste accumulation, pH, density, passage history, and media exchange can change growth or viability. If death is material, observed viable-count change reflects both growth and loss; a single exponential growth model can then misattribute the net rate.

## Count, concentration, and volume

Let $X_v$ be viable cells per volume and $V$ the culture volume. The total viable cell number is $N_v=X_vV$. Concentration can remain unchanged while total count increases if volume grows, and a concentration measurement alone does not give total biomass or the total number of cells. Record volume and distinguish viable from total counts.

For a well-mixed vessel, a general cell balance is

$$\text{accumulation}=\text{inlet}-\text{outlet}+\text{growth}-\text{loss}.$$

In a batch with fixed volume and no inlet or outlet, a simple viable-cell model is $dN_v/dt=(\mu-k_d)N_v$, where $k_d$ is a first-order loss rate. If death is negligible, $k_d\approx0$ and the balance reduces to the exponential model. In a fed or perfused vessel, flows also change total cell number and concentration; those cases require the corresponding inlet, outlet, and volume terms rather than the batch equation.

**Synthetic balance example.** Suppose a fixed-volume batch contains $2.0\times10^9$ viable cells, with $\mu=0.030$ h$^{-1}$ and a stipulated loss rate $k_d=0.005$ h$^{-1}$. With no cell flow, the net accumulation rate is $(0.030-0.005)(2.0\times10^9)=5.0\times10^7$ viable cells/h. The inputs are illustrative and the calculation assumes both rates remain constant over the interval.

## Substrate and product balances

For a well-mixed culture with substrate concentration $S$, feed flow $F_{in}$, outlet flow $F_{out}$, feed concentration $S_{in}$, and specific uptake rate $q_S$, a simple balance is

$$\frac{d(SV)}{dt}=F_{in}S_{in}-F_{out}S-q_SX_vV.$$

The final term is substrate consumption by cells. A product with specific formation rate $q_P$ instead has a positive generation term $q_PX_vV$. Units provide a check: concentration times volume is amount, and each flow or reaction term is amount per time. For a batch with no flow, these balances reduce to cellular consumption or production. A full fed-batch or perfusion model must also account for changing volume and any cells or solutes in the streams.

## Estimate the rate from data

Choose observations from the interval where the exponential assumption is plausible, use the same viable-count method, and report the sampling times and culture conditions. With more than two points, fit $\ln X_v$ versus time over a stated interval and examine residuals; a changing slope signals that one constant-$\mu$ model may not describe the full run. Replicate counts and uncertainty help distinguish a real change from measurement noise.

Do not mix base-10 logarithms with the natural-log formula without converting: $\ln z=2.303\log_{10}z$. Keep time units consistent. If $\mu$ is in h$^{-1}$, $t$ must be in hours to make $\mu t$ dimensionless. Passage number, viable-cell definition, sampling losses, and volume changes belong in the process record when they affect interpretation.

## Common mistakes

- Calling a fitted $\mu$ a universal cell-line property instead of a condition- and interval-specific estimate.
- Fitting across lag, limitation, and decline phases with one exponential rate.
- Confusing total viable cells $X_vV$ with viable concentration $X_v$.
- Ignoring cell death when interpreting a viable-count slope.
- Omitting feed, bleed, or changing-volume terms from a non-batch balance.
- Using $μ=\ln2/t_d$ with inconsistent time units or a base-10 logarithm.

## Check your model

Identify whether the question asks for concentration, total cell number, a specific rate, or a material balance. State the interval and assumptions before fitting. The public items preserve $\mu=\ln2/30=0.0231$ h$^{-1}$ for a 30-hour doubling time and a doubling time of about 8.96 hours for the 6.4-fold count increase over 24 hours. These are formative calculations, not process recipes.
