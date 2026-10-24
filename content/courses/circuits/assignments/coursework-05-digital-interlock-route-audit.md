# Assignment 5: digital interlock route audit

This open report connects the new digital-abstraction, Boolean and memory/timing instruction with the existing acquisition strand. It audits a stipulated bench interlock from its trip flags through a combinational realization to a latched timing check. All flags, delays and clocks are invented mathematical inputs, not measured instrument performance or a hardware authorization. Retain calculations, code and the report locally; checkpoints assess selected outputs, not the complete evidence argument.

## Part A: trip flags and a majority audit

An instrument bench exposes three stipulated trip flags: O (overtemperature), C (overcurrent) and D (door open). The declared interlock is the majority function $S=O\cdot C+C\cdot D+O\cdot D$: the bench shuts down when any two of the three flags are one. Enumerate the eight rows under the declared index $4O+2C+D$, with $O$ the most significant bit:

| Index | O | C | D | S |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 |
| 2 | 0 | 1 | 0 | 0 |
| 3 | 0 | 1 | 1 | 1 |
| 4 | 1 | 0 | 0 | 0 |
| 5 | 1 | 0 | 1 | 1 |
| 6 | 1 | 1 | 0 | 1 |
| 7 | 1 | 1 | 1 | 1 |

$S$ is one exactly at indices 3, 5, 6 and 7: four trips, whose indices sum to $3+5+6+7=21$. At index 1, the single-flag row $(0,0,1)$, the majority $S$ stays zero while the single-flag route would already trip. Compare with the single-flag route $O+C+D$, which trips on seven of the eight rows: one stuck sensor would stop the bench alone, while the majority route requires two simultaneous faults. A stuck-at-zero failure is the dual case: the single-flag route loses that trip entirely while the majority route keeps every pair that does not involve the dead flag. State that trade-off explicitly in the report; it is a design argument, not a measurement.

## Part B: a two-level realization

Realize $S$ with two-input gates only: the three AND terms $O\cdot C$, $C\cdot D$ and $O\cdot D$ joined by two ORs, five gates in all, with six literal appearances. If a three-input NAND is declared available, the same function follows from four NAND gates: $\mathrm{NAND}(O,C)$, $\mathrm{NAND}(C,D)$ and $\mathrm{NAND}(O,D)$ each produce a complemented product, and a final three-input NAND complements their product back, because $\overline{\overline{OC}\cdot\overline{CD}\cdot\overline{OD}}=OC+CD+OD$ by De Morgan. Both realizations agree with the truth table; neither is a claim about propagation delay or a real component count.

## Part C: latch the trip and re-check timing

The trip feeds a D flip-flop clocked at 25 MHz (period 40 ns), through a combinational route of stipulated delay 22 ns. The source flip-flop has clock-to-Q delay 4 ns; the destination requires setup 6 ns and hold 3 ns. The setup check: $40-4-22=14\ \ge\ 6$, slack $8$ ns. The hold check: $4+22=26\ \ge\ 3$, slack $23$ ns. Both slacks are nonnegative, so the latched route meets its stipulated timing checks; record 1 for "passes" and 0 otherwise, and never round a negative slack into a pass.

## Part D: reset discipline

An operator reset is asynchronous by nature, and the metastability boundary of the memory lesson applies: route the reset through a declared synchronizer before it gates any state, and keep the interlock's trip path combinational-to-latched without asynchronous shortcuts. Distinguish an asynchronous clear, which forces the latch output immediately, from a synchronous reset, which only takes effect at a clock edge and therefore participates in the same setup/hold arithmetic as the trip path. State the policy and its residual risk in the report; no numeric field is graded for this part.

## Self-review and scope

Retain the truth table, the two-level gate argument, the latched timing arithmetic and the reset policy. [MIT OCW 6.002 Circuits and Electronics, Spring 2007 calendar](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/calendar/) schedules the digital abstraction (L4), Boolean logic and combinational gates (R4/R4a) and digital memory/state (L15); they are link-only scope comparators, and every table, route and number here is original and AI-assisted. No source text, figure, problem or dataset is imported. The package remains partial, unreviewed and formative-only; measured workload, hardware validation and qualified review remain open.