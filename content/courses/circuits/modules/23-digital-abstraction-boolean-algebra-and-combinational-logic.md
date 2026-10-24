# Digital abstraction, Boolean algebra and combinational gate routes

An instrument front end eventually reduces its evidence to symbols: a converter code, a comparator decision, a threshold flag. This original reading adds the declared digital abstraction, Boolean algebra and two-level combinational routes to the existing sampling, sensor and amplifier material. All logic levels, gate delays and functions here are invented teaching parameters, not a component family, datasheet or hardware procedure.

## The abstraction is a declared map

The sampling lesson treats a converter code as one of 1024 declared bins. The digital abstraction makes a coarser claim: a node carries one of two declared symbols, 0 or 1. Stipulate a nominal 0–5 V interface partitioned as follows: a driver presenting 0 must hold its output at or below 1.0 V, a driver presenting 1 must hold at least 4.0 V, a receiver may classify anything at or below 2.0 V as 0, and a receiver may classify anything at or above 3.0 V as 1. The open bands between those obligations are deliberately unhonored gaps: a compliant receiver need not interpret a node resting there, and a compliant driver must not leave it there. The differences between the driver and receiver bounds are the noise margins of this stipulated interface — here 1.0 V on each side — and they are bookkeeping for this exercise, not a measured family's guaranteed margins. The symbol a node "is" exists only relative to this declared convention, which is a specification choice and not a physical fact about the wire.

## Boolean algebra over the declared symbols

With two symbols, the elementary gates are fully described by small tables: AND outputs 1 only when every input is 1, OR outputs 1 when any input is 1, and NOT complements its single input. The useful identities follow algebraically: commutativity and associativity of AND and OR, distributivity of AND over OR, double complementation, and the complements $A\cdot\overline{A}=0$ and $A+\overline{A}=1$. Two identities deserve separate statement because they convert between the two shapes:

$$\overline{A+B}=\overline{A}\cdot\overline{B},\qquad \overline{A\cdot B}=\overline{A}+\overline{B}.$$

These De Morgan identities say that complementing a sum yields a product of complements, and conversely. NAND (NOT-AND) and NOR (NOT-OR) are complete by themselves: $\overline{X}=\mathrm{NAND}(X,X)$, $\mathrm{AND}(X,Y)=\mathrm{NAND}(\mathrm{NAND}(X,Y),\mathrm{NAND}(X,Y))$, and $\mathrm{OR}(X,Y)=\mathrm{NAND}(\overline{X},\overline{Y})$ applies De Morgan to build a sum from NANDs alone. A two-level sum-of-products route is one OR of several AND terms, one term per activating input pattern.

## Worked truth table with declared indices

Audit $F(A,B,C)=A\cdot B+B\cdot\overline{C}$ under the declared row index $4A+2B+C$, with $A$ the most significant bit. Enumerating the eight rows: $F$ is 1 exactly at $(A,B,C)=(0,1,0)$, $(1,1,0)$ and $(1,1,1)$ — indices 2, 6 and 7. Three of the eight rows are active, and the active indices sum to $2+6+7=15$. At index 5, the row $(1,0,1)$, both products vanish, so $F=0$. The index list is a labeling choice: reordering the variables relabels identical rows, so any index quotation must carry its convention.

## Worked De Morgan route with NAND gates only

Route $G=\overline{A+B\cdot C}$ through two-input NAND gates only. First complement the inner sum: $G=\overline{A}\cdot(\overline{B}+\overline{C})$. Then observe that $\mathrm{NAND}(B,C)=\overline{B\cdot C}=\overline{B}+\overline{C}$, so $G=\overline{A}\cdot\mathrm{NAND}(B,C)$. Build the remaining AND from NANDs alone: $\overline{A}=\mathrm{NAND}(A,A)$, the intermediate $X=\mathrm{NAND}(\overline{A},\mathrm{NAND}(B,C))$, and the output $G=\mathrm{NAND}(X,X)$. The stated construction uses four two-input NAND gates. Check two rows against the original expression: at $(A,B,C)=(0,1,1)$ the inner sum is $0+1=1$, so $G=0$; at $(0,0,0)$ the inner sum is 0, so $G=1$. The route agrees on both rows. Four is the gate count of this stated construction, not a proven minimum over all possible NAND networks.

## A propagation-delay ledger

Stipulate single-gate delays: NOT 1 ns, two-input AND 2 ns, two-input OR 3 ns. For the route $S=A\cdot B+\overline{A}\cdot C$ the direct term costs $2+3=5$ ns, while the $C$ term passes NOT, then AND, then OR for $1+2+3=6$ ns along three gates. The route's critical path is therefore 6 ns. At a stipulated 10 ns clock period the slack is $10-6=4$ ns. Two cautions: unequal path lengths can produce transient output patterns that the final truth table hides, and these stipulated constants are teaching numbers, not a standard-cell library — real delays vary with load, process and temperature.

## Instrument connection and boundaries

Comparator and converter flags from the earlier lessons are exactly the stipulated digital inputs these routes combine. [MIT OCW 6.002 Circuits and Electronics, Spring 2007 calendar](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/calendar/) places the digital abstraction in lecture L4 with Boolean logic and combinational gates in recitations R4/R4a; it is a link-only scope comparator. All tables, routes and delays here are original and AI-assisted; no source table, figure, problem or dataset is imported. Gate-level CMOS construction, energy and power of logic, programmable implementation and laboratory validation remain outside this package, which stays partial, unreviewed and formative-only.

## Common mistakes

Do not read a logic level without its declared map, quote minterm indices without their bit order, or call a four-gate route minimal without a stated exhaustive search. Do not treat stipulated delays as component datasheets, or infer glitch-free behavior from a functional truth table.

## Limits of this lesson

Every level, function and delay is synthetic. The noise-margin bookkeeping is arithmetic on stipulated bounds, not a measured interface characterization, and no hazard analysis beyond the qualitative caution is performed.