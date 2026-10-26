# Assignment 6: cumulative final channel audit

This open report connects the whole fourteen-week sequence into one audit: a stipulated sensor channel is followed from its Thévenin source through loading, gain, anti-alias filtering, quantization and sampling into a latched interlock route and a supply-power budget. All flags, gains, delays and clocks are invented mathematical inputs, not measured instrument performance or a hardware authorization. Retain calculations, code and the report locally; checkpoints assess selected outputs, not the complete evidence argument.

## Part A: loading and gain

A stipulated pressure sensor presents an open-circuit 10.0 mV DC signal with source resistance $R_s=1.00$ kΩ. The amplifier input resistance is $R_{in}=4.00$ kΩ, so the divider delivers $R_{in}/(R_s+R_{in})=4/5$ of open circuit: the loaded channel sees $8.00$ mV, a loading error of $20.0\%$. The gain stage is a non-inverting amplifier with $R_2/R_1=99$, gain $100.0$, so the channel output is $0.800$ V into the converter's stipulated $10.0$ V span — ample headroom. Re-derive both numbers in the report and state which error dominates the channel: the analog loading error, not the conversion. Also state the repair the audit implies: raising $R_{in}$ toward $99$ kΩ would push the divider to $99/100$ and shrink the loading error to $1.0\%$, a cheaper fix than any converter change, because the sensor and its source resistance are stipulated fixed.

## Part B: settling and sampling

The anti-alias stage is a first-order RC with $R=1.00$ kΩ and $C=1.00$ µF, so $\tau=RC=1.00$ ms. Reaching within a half-LSB of 8 bits requires settling through $8\ln 2$ time constants: $5.55$ ms. The signal band is stipulated at $40.0$ Hz, so the Nyquist rate is $80.0$ Hz; sampling at $200$ Hz carries a $2.50\times$ margin. Recompute all three from their stated assumptions rather than quoting them.

## Part C: quantization and noise

The 8-bit converter spans $10.0$ V in $256$ steps, so one LSB is $10.0/256=39.1$ mV and the half-LSB uncertainty is $0.195\%$ of span. Channel noise referred to the converter input is stipulated at $12.0$ mV RMS, that is $12.0/39.1=0.307$ LSB. Compare with Part A: a $20.0\%$ loading error dwarfs a $0.2\%$ conversion uncertainty, so extra converter bits would not repair this channel; state that budget conclusion explicitly. Tie the bookkeeping back to the RMS discipline of week 8: the same mean-square convention that sizes a fuse converts a random channel voltage into one heating-equivalent number, and the report must say which quantity each figure represents before any comparison is meaningful.

## Part D: the interlock route

The trip condition is the stipulated route $T=A\cdot(B+C)$. Enumerate the eight rows under the declared index $4A+2B+C$ with $A$ the most significant bit: $T$ is one exactly at $(1,0,1)$, $(1,1,0)$ and $(1,1,1)$ — indices 5, 6 and 7, three active rows whose indices sum to $18$. The route needs two two-input gates, one OR and one AND. The trip feeds a flip-flop clocked at a $40$ ns period through a $15$ ns route, with clock-to-Q $4$ ns, setup $6$ ns and hold $3$ ns: the setup slack is $40-4-15-6=15$ ns and the hold slack is $4+15-3=16$ ns; both are nonnegative, so record the route as passing, and never round a negative slack into a pass.

## Part E: supply power

The channel runs from a stipulated $12.0$ V supply drawing $25.0$ mA: $P=12.0\cdot0.0250=0.300$ W. Fuse and thermal ratings follow the same RMS discipline as the AC-power unit: the heating value is the steady draw, not a startup or reactive peak. If the supply's input stage presents a lagging power factor, only the real $0.300$ W heats the channel while the reactive part cycles; connect that distinction in the report.

## Part F: the audit table

Assemble one table with columns stage, quantity, value and source lesson: loading error $20.0\%$, gain $100.0$, channel output $0.800$ V, settling $5.55$ ms, Nyquist rate $80.0$ Hz, sampling margin $2.50\times$, noise $0.307$ LSB, latched slacks $15$ and $16$ ns, supply power $0.300$ W. Every row must cite the lesson that derives it; a number without provenance is not an audit result.

## Self-review and scope

Retain the derivations, the audit table and the dominance argument. The comparator set is [MIT OCW 6.002 Circuits and Electronics, Spring 2007 calendar](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/calendar/) and [syllabus](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/syllabus/), with textbook chapter mapping from the public [readings page](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/readings/); all are link-only scope comparators, and every number here is original, synthetic and AI-assisted. No source text, figure, problem or dataset is imported. The package remains partial, unreviewed and formative-only; measured workload, hardware validation and qualified review remain open.