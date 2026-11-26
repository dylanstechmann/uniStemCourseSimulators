# Integrated conceptual flowsheet and model-audit project guide

This optional **zero-point, self-assessed project** integrates the survey through a fictional process with generic A, B and S. It is not a capstone, detailed design or operating exercise. Use [flowsheet-audit-rehearsal.csv](flowsheet-audit-rehearsal.csv) for the quantitative rehearsal and the Case studio for five private milestone self-checks. No points, grade, professional competence or release decision is awarded.

## Project brief and conceptual flowsheet

Construct a BFD with fresh feed, optional recycle mixing, reaction, separation, desired-B product and an unrecovered stream. Then write a PFD narrative with stable stream IDs and explicit boundary crossings. You may include a bypass or purge only if you define its topology and explain its balance role. Do not add equipment details, line sizes, pump selections, controller settings or protective-system specifications.

Prepare a stream-table schema with total and A/B/S flows, units, measurement/specification/reconciliation status and blanks for unknown values. Define whether conversion refers to fresh feed or reactor inlet, and define selectivity, recovery, purity and overall yield before inserting numbers. State the steady, one-to-one synthetic reactor accounting and separator recovery assumptions. Your diagrams can be text-based; clarity and auditability matter more than graphical polish.

## Rehearsal data and conservation checks

The CSV contains four distinct synthetic scenarios, R01–R04. Derived columns within a scenario are correlated through the same constructed model; they are not repeated independent measurements. Distinct scenario IDs also do not represent physical replication. Use them for descriptive comparison and sensitivity, not pooled statistical inference.

For every scenario, recompute feed A = converted A + unreacted A and converted A = B formed + S formed. R01 has 100 = 60 + 40 and 60 = 42 + 18. R02 has 120 = 72 + 48 and 72 = 48 + 24. R03 has 90 = 45 + 45 and 45 = 30 + 15. R04 has 150 = 90 + 60 and 90 = 60 + 30. These checks are required for all rows, not only rows used by numeric practice.

Where recovery is declared, recovered B = B formed × B recovery fraction. R01 recovered B is 42 × 0.90 = 37.8 kg/h. R02 B selectivity is 48/(48+24) × 100 = 66.6666667%. R03 recovered-B overall yield on feed A is 24/90 × 100 = 26.6666667%. R04 recovery fraction, recovered B and separator purity are blank and remain unknown. Do not fill them with zero or borrow a mean from R01–R03.

## Five milestones

**Milestone 1 — boundaries and streams.** Submit the BFD/PFD narrative, stream-table schema, unit conventions and assumption register. Show fresh-feed, reactor and overall boundaries. List unknown phase, property, energy, transfer and dynamic evidence rather than treating it as absent.

**Milestone 2 — balances and reconciliation.** Close every lab and rehearsal relationship, report residuals with a declared sign and distinguish measured from reconciled values. Define conversion, selectivity, recovery, purity and yield denominators. Include the correlated-record disclosure and preserve all blanks.

**Milestone 3 — model domains.** Recompute the lesson energy and valid flash examples and show composition closure. Explain why both K values below one cannot be forced into an interior two-phase root. Audit the transfer model for geometry, regime, property and correlation range. Compare batch/CSTR/PFR equations, parallel-reaction selectivity, RTD evidence and nonisothermal omissions. Do not turn this into a detailed design.

**Milestone 4 — separations and trade-offs.** Compare equilibrium-stage and rate-based viewpoints across distillation, absorption, extraction, membranes and adsorption. Recompute R01–R03 performance, discuss recovery–purity–energy sensitivity and leave R04 unknown. State how a change in separator recovery could alter overall yield without claiming an optimal target.

**Milestone 5 — bounded handoff.** Assemble the four earlier milestones, an alternatives/sensitivity note, unknown register, source links and unresolved review gates. Cross-reference every important claim to a reading, public item or CSV row. Finish with the exact conceptual status: partial, unreviewed, formative-only, synthetic and non-operational.

## Model-audit and self-assessment checklist

Check units, independent balances, denominator definitions and every total/component closure. Test phase roots and fractions for valid domains. Identify where constant properties, steady state, ideal mixing, constant K values, stage equilibrium or rate coefficients are assumed. Distinguish missing evidence from negligible evidence and arithmetic consistency from physical validation. Evaluate whether a proposed alternative changes the conclusion and what new evidence would be required.

Use the six rubric criteria in the integrative Case studio and the three criteria in each milestone as prompts, not automated grades. Saving a checklist does not establish reviewer agreement. Qualified chemical-engineering, thermodynamic, transport, reaction, separation, statistics, accessibility and safety reviews remain open. The result is a reproducible learning dossier, not a process design package, safety case, operating instruction or release approval.


## Evidence and use boundary

This original reading is part of an explicitly partial university-level survey. It is unreviewed and formative-only. Every process, stream, property and observation is synthetic and fictional; generic labels A, B and S do not identify real chemicals. Worked precision supports reproducible arithmetic, not measurement accuracy. Arithmetic closure is not proof of safe or feasible operation. No real production recipe, hazardous condition, plant operating target, controller setting, line or pump sizing, equipment rating, relief sizing, or safety/release approval is supplied. Qualified scientific, engineering, safety and instructional review remains unresolved.
