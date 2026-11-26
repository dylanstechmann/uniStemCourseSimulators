# Process variables, flowsheets, units and material balances

A chemical engineering model begins by deciding what is being represented and what evidence would change the representation. A stream is not merely a number beside an arrow. It has an identifier, a boundary crossing, a flow basis, component conventions and units. Temperature, pressure, composition, extensive flow and intensive state descriptions answer different questions. This survey uses synthetic steady processes with generic species A, B and S so that the bookkeeping remains visible. Nothing in a computed stream table demonstrates that a physical process exists or could operate.

## BFD and PFD communication

A block flow diagram, or BFD, groups a process into major functions. A possible fictional BFD is feed preparation → reaction → separation → recycle. Its purpose is to make the process logic discussable before details are known. A process flow diagram, or PFD, adds defined unit relationships and stream connections: two feeds enter a mixer, the mixed stream enters a reactor, and a separator divides reactor effluent into product and a stream that may be recycled. A PFD can support material and energy accounting, but it is not a fabrication drawing. It does not by itself specify mechanical construction, detailed connections, ratings, protective systems or operating instructions.

The same distinction prevents two common errors. First, adding more arrows does not necessarily add information: an arrow without an identifier or boundary can make the model less auditable. Second, a clean diagram does not validate the underlying assumptions. A reader should be able to trace every table row to a stream and every stream to a boundary crossing. Recycle must be shown explicitly rather than hidden in an overall conversion claim. Bypass routes material around a function, whereas purge removes a fraction from a declared loop; they are not interchangeable labels.

## Stream tables and units

A useful stream table has stable stream IDs and columns for total flow and component flows or fractions. If composition is given as a fraction, the table must declare mass or mole basis and whether the value is measured, specified or calculated. This package uses simple mass-flow examples and the generic components A, B and S. Fractions describing one stream must share a basis and sum to one within declared rounding. Component flows should sum to total flow on that same basis. Blank evidence remains unknown; it is never silently entered as zero.

Dimensional consistency is a reasoning check, not a formatting afterthought. A flow of 2.5 kg/s is 9000 kg/h because one hour contains 3600 seconds. Multiplying a mass flow by a heat capacity and a temperature difference requires compatible energy and time units. Mixing kilograms with another mass unit, or seconds with hours, can produce an apparently precise but meaningless result. Significant figures also require judgement: a calculator can emit many digits from coarse synthetic inputs, but those digits do not create experimental accuracy.

## Degrees of freedom before algebra

Before solving, list the unknowns and independent equations for one boundary. Three unknown stream variables with two independent material balances leave one degree of freedom. One additional independent specification is required. Repeating the total balance in different units does not add an independent equation. Likewise, a component equation that is algebraically formed from the other component equations and the total equation may not increase the independent count.

Degrees-of-freedom accounting is local to the declared model. Adding a reactor introduces reaction extents or kinetic relationships; adding recycle couples previously separate boundaries. A zero count does not prove that the specifications are physically reasonable. A negative count can indicate conflicting equations, redundant information suitable for reconciliation, or an incorrectly constructed model. The learner should explain which situation applies rather than automatically deleting an equation.

## Total and component balances

For a steady nonreactive mixer, total inflow equals total outflow. With feeds of 40 and 60 kg/h, the product is 100 kg/h. If the two feeds contain 20 and 18 kg/h A, product A is 38 kg/h. The B and S balances must also be checked independently. Total closure with an A residual is not complete closure. Conversely, component values chosen to close while ignoring the total can still be inconsistent.

The general steady statement is input + generation − output − consumption = 0 for the declared component and boundary. For total mass, chemical generation and consumption cancel over all species in the idealized accounting. For an individual species in a reactor, those terms matter. A batch or accumulating continuous system requires an accumulation term and cannot be forced into the steady formula. Different boundaries can provide different equations: a reactor balance describes conversion, while a separator balance describes distribution. An overall boundary can simplify recycle unknowns, but internal balances are still needed to recover internal streams.

A disciplined solution therefore follows a repeatable sequence: sketch the boundary, label streams and components, convert units, list unknowns, count independent equations, solve, and recompute every total and component closure. Finally, inspect negative flows, fractions outside zero to one, unexplained residuals and assumptions that the algebra cannot test. The arithmetic result is only a conditional statement about the model.


## Evidence and use boundary

This original reading is part of an explicitly partial university-level survey. It is unreviewed and formative-only. Every process, stream, property and observation is synthetic and fictional; generic labels A, B and S do not identify real chemicals. Worked precision supports reproducible arithmetic, not measurement accuracy. Arithmetic closure is not proof of safe or feasible operation. No real production recipe, hazardous condition, plant operating target, controller setting, line or pump sizing, equipment rating, relief sizing, or safety/release approval is supplied. Qualified scientific, engineering, safety and instructional review remains unresolved.
