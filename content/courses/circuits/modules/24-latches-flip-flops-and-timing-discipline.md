# Memory elements and timing discipline

Combinational routes forget: outputs follow inputs with only gate delays in between. A measurement instrument cannot forget: a sample must persist until its successor is ready. This original reading adds one-bit storage elements, edge-triggered clocking and an explicit timing discipline to the combinational routes of the digital-abstraction lesson. All latches, registers, clocks and delays here are invented teaching parameters, not a component family, datasheet or hardware procedure.

## A NOR pair stores one bit

Cross-couple two NOR gates: each gate's output feeds the other's input. Name the outputs $Q$ and $\overline{Q}$, and drive the two remaining inputs with set $S$ and reset $R$. The state table follows from the gate definition alone. $S=1,R=0$ forces $Q=1$. $S=0,R=1$ forces $Q=0$. $S=R=0$ releases both gates to hold whatever the cross-coupling already established: this is the stored bit. The fourth combination, $S=R=1$, forces both outputs to 0, so the pair is not complementary and the stored bit is not defined; this combination is excluded — one of the four input pairs. The exclusion is a property of the declared element, not a defect to be repaired by better NOR gates.

## From a transparent latch to an edge-triggered flip-flop

A gated D latch adds an enable: while the enable is asserted the output follows D, and while the enable is released the output holds. Transparency is convenient but awkward for a route whose own output feeds back or feeds a neighbor, because during the asserted window changes race through. An edge-triggered D flip-flop closes that window: D is sampled only near the clock edge, and changes between edges wait for the next one. The register behind a clocked converter is exactly this pattern — the comparator flags and codes of the earlier lessons are latched once per acquisition cycle rather than streamed continuously.

## A declared timing discipline

Stipulate a single clock of period 20 ns, a source flip-flop with clock-to-Q delay 4 ns, a combinational route of delay 8 ns, and a destination flip-flop requiring setup 5 ns and hold 2 ns. Two inequalities decide whether the route is usable:

$$\text{setup: } T-t_{cq}-t_{pd}\ \ge\ t_{su},\qquad 20-4-8=8\ \ge\ 5\ \text{(slack 3 ns)},$$
$$\text{hold: } t_{cq}+t_{pd}\ \ge\ t_{h},\qquad 4+8=12\ \ge\ 2\ \text{(slack 10 ns)}.$$

The setup bound also answers a design question: at this period the route may grow until $20-4-5=11$ ns before setup fails. Both checks use stipulated constants, one clock domain and no clock skew; they are teaching arithmetic, not a sign-off analysis.

## A shift register moves a serial route

Take a four-bit register whose serial input enters at $Q_0$ and shifts toward $Q_3$ on each rising edge, older bits moving to more significant positions. Present the bits 1, 1, 0, 1 in that order. After the first edge the state $Q_3..Q_0$ is 0001 (decimal 1); after the second, 0011 (3); after the third, 0110 (6); after the fourth, 1101 (13). Four edges are needed to load four bits, and the final state reads the first-presented bit as the most significant. Serializing a trip vector onto a logging bus is the same pattern; the bit-order declaration is what makes any decimal reading meaningful.

## A ripple counter wraps and divides

Cascading three toggle stages, each clocked by the previous stage's falling output, counts input pulses modulo 8: eight distinct states. The last stage completes one full cycle per eight input pulses, so a 2 MHz input yields a last-stage frequency of $2000/8=250$ kHz, and thirteen pulses leave a count of $13\bmod 8=5$. The stages do not switch simultaneously — later stages wait on earlier ones — so intermediate readings can be transiently wrong; a synchronous counter avoids that, and this lesson only stipulates the wrap arithmetic, not a delay-accumulation analysis.

## Metastability is a boundary, not a solved problem

An asynchronous instrument signal sampled near the clock edge can violate the setup/hold window and resolve to an unpredictable level for an unbounded interval. A synchronizer chain of one or two flip-flops reduces the exposure but does not eliminate it, and no probability is claimed here. The honest policy is explicit: synchronize asynchronous inputs before combinational routes, and declare the residual risk rather than pretending the sampling discipline removed it.

## Common mistakes

Do not use the excluded latch input, confuse a transparent latch with an edge-triggered flip-flop, or check setup while forgetting hold. Do not treat ripple stages as simultaneous, read a shift register without its declared bit order, or call a synchronizer chain a metastability cure.

## Limits of this lesson

Every element, clock and delay is synthetic. Gate-level CMOS implementation, memory arrays, energy and power of logic, synthesis tool flows and laboratory validation remain outside this package. [MIT OCW 6.002 Circuits and Electronics, Spring 2007 calendar](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/calendar/) schedules digital memory and state in lecture L15 and digital memory arrays in recitation R15; it is a link-only scope comparator, and all tables, routes and timing arithmetic here are original and AI-assisted. The package remains partial, unreviewed and formative-only.