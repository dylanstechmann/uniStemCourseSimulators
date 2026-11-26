# Multistream and reactive balances, recycle and reconciliation

Reactive flowsheets require the same conservation discipline as simple mixers, but the boundaries and performance denominators multiply. A feed can be split between units, unreacted A can be recycled, a bypass can avoid a unit, and a purge can remove material from a loop. Each feature changes the equations. A strong solution keeps single-pass reactor behavior, overall process behavior and separator distribution separate instead of compressing them into one ambiguous efficiency.

## Reactive accounting and performance ratios

Consider a synthetic steady reactor fed with 80 kg/h A. If 20 kg/h A leaves unreacted, then 60 kg/h A reacted and conversion is (80−20)/80 × 100 = 75%. Conversion is bounded between zero and one, or zero and 100%, in this nonnegative single-reactant example. The unreacted fraction is 25%, not the conversion. For multiple feeds or recycle, the learner must state whether the denominator is fresh feed to the overall process or reactor inlet after mixing. Those denominators can produce different overall and single-pass conversions.

Suppose the declared one-to-one synthetic accounting converts the 60 kg/h A into 36 kg/h B and 24 kg/h S. Selectivity to B on reacted A is 36/60 × 100 = 60%. Yield of B on A fed is 36/80 × 100 = 45%. Selectivity therefore describes how reacted material is distributed, while yield combines how much reacted with how much became B. Different stoichiometries require explicit coefficients or a properly declared extent basis; the simple numerical equality here is a stipulated teaching model, not a universal mass-based formula.

A component balance can be written with extents for independent reactions. Independence matters: writing several reactions that are linear combinations of one another does not add degrees of freedom. Atom or element balances can provide a cross-check when real species are known, but this package deliberately remains with generic A, B and S and a declared conservation rule. No chemical identity, mechanism or production condition is inferred.

## Multistream, recycle, bypass and purge boundaries

In a multistream process, each inlet and outlet must cross the selected boundary exactly once in the accounting. Mixing fresh feed with recycle creates a reactor inlet whose flow and composition may differ from both streams. A reactor balance then determines effluent from its inlet and reaction extent. A separator divides that effluent according to declared recoveries. The recycle returns selected material to the mixer, while product and purge leave the overall system.

Overall fresh-feed balances can be simpler than internal loop balances because recycle cancels when it both enters and leaves the overall boundary. This cancellation does not mean recycle is irrelevant. Internal reactor inlet, separator load and single-pass conversion still depend on it. Solving coupled equations may require iteration, but the need for iteration does not change conservation.

A bypass sends part of a stream around a unit and recombines it elsewhere. Its fraction must be included in both the split and mixing balances. A purge removes part of a recycle or circulating stream. Conceptually, it can prevent indefinite accumulation of a species that is not removed elsewhere, but the amount and effect depend on the full steady balance. Neither purge nor bypass automatically increases purity, recovery or safety. No operating fraction is recommended here.

## Deterministic data reconciliation

Synthetic process records may contain measurements that do not close exactly. Reconciliation starts by separating three roles: measured values, declared specifications and reconciled values. A residual must have a defined sign, such as measured minus reconciled. If measured product flow is 102 kg/h and reconciled flow is 100 kg/h, the residual is +2 kg/h. Averaging those numbers would destroy the distinction and would not create a new measurement.

A deterministic reconciliation can enforce total and component balances under declared rules. It does not, by itself, identify which sensor or record caused a discrepancy. Several alternative adjustments can close the same equations. Uncertainty-weighted reconciliation would require a defensible measurement model, covariance information and independence assumptions that this survey does not supply. Outlier investigation likewise needs evidence beyond a convenient residual.

Rows from one scenario are correlated records because they share constructed stream constraints, feed values and reconciliation decisions. Three rows for feed 1, feed 2 and product are not three independent experimental replicates. Repeating the same scenario with a changed measured field also does not establish physical replication. Report scenario-level descriptive closure rather than pooled confidence intervals or claims of statistical significance.

## Audit routine and failure modes

A complete reactive-flowsheet audit writes fresh-feed and reactor-inlet balances separately, defines conversion and yield denominators, checks every component, and shows where bypass, purge and recycle cross boundaries. It tests whether product flows are nonnegative and whether fractions close. It then compares measured and reconciled values without overwriting either. Unknown measurements remain blank even when a reconciled estimate is available.

Common failure modes include using fresh feed in a single-pass conversion denominator, calling selectivity a yield, allowing recycle to appear twice in an overall balance, treating a purge as a bypass, and using total closure to hide a component residual. Another is assuming that a consistent table proves feasible operation. It proves only that the declared numbers satisfy the declared equations. Physical properties, phase behavior, dynamics, equipment limits, hazards and human review remain outside the arithmetic.


## Evidence and use boundary

This original reading is part of an explicitly partial university-level survey. It is unreviewed and formative-only. Every process, stream, property and observation is synthetic and fictional; generic labels A, B and S do not identify real chemicals. Worked precision supports reproducible arithmetic, not measurement accuracy. Arithmetic closure is not proof of safe or feasible operation. No real production recipe, hazardous condition, plant operating target, controller setting, line or pump sizing, equipment rating, relief sizing, or safety/release approval is supplied. Qualified scientific, engineering, safety and instructional review remains unresolved.
