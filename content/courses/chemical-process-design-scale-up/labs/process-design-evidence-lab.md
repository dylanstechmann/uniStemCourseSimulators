**Status:** Original, explicitly partial advanced university/industry survey material; unreviewed and formative-only. All species, equipment, records, values and organizations are synthetic and fictional. This is a paper data exercise, not an operating, fabrication, safety, validation or release instruction.

# Original synthetic process-design, safety and equipment evidence lab

## Learning objectives

- Recompute integration, NPV, autocorrelation and scale relationships from every public scenario row.
- Separate derived columns from evidence, reused scenario structure from independent replication, and unknowns from zero.
- Trace all-wetted, inspection, safety and acceptance evidence to the required synthetic HOLD or bounded review state.

## Purpose and dataset contract

This zero-point lab uses [process-design-evidence.csv](/api/v1/courses/chemical-process-design-scale-up/resources/labs/process-design-evidence.csv), an original synthetic CSV with eight fictional scenarios. It contains no real chemical identifier, process recipe, operating target, equipment duty, controller setting or acceptance threshold. Numeric fields are accounting or model inputs only. They are not measurements taken by the owner or any organization.

Each row is a scenario, not a new independent experiment. Scenario structure is reused across derived columns, and the four residual fields are repeated instrument records from that same scenario. All rows are therefore **correlated and descriptive, not independent replicates**. Do not pool them for a confidence interval, capability claim or sample-size inflation. The `record_relation` field carries this limitation beside every row.

Download the CSV before beginning. Keep a calculation table with scenario ID, formula, substitution, result and interpretation. A blank or `missing` evidence state is unresolved and can never be converted to zero or pass. The numeric model fields are populated so every row can be recomputed, but arithmetic closure is not proof of safe or feasible operation, compatibility, inspection quality, validation or readiness.

## Part 1: bounded heat recovery

For each row compute `recovered_heat_kw = min(hot_model_term, hot_availability_factor, cold_model_term × cold_demand_factor)` using the two explicit products shown below. The CSV supplies hot capacity 120 and availability 4 for L01, giving 480, and cold demand 90 with factor 5, giving 450; recovered heat is 450 kW. This is a bounded accounting term, not temperature-level feasibility or an exchanger rating.

Check every row rather than only L01. Identify scenarios limited by the hot side and cold side. If a value were absent, the correct response would be unknown, not zero recovery. Do not infer utility savings, emissions reduction or equipment selection from this number alone.

## Part 2: scenario NPV

For each row compute

NPV = −initial_investment + annual_net_cash × [1−(1+discount_rate)^(−years)]/discount_rate.

For L02, the declared values are 800, 250, 0.10 and 4, so NPV = −800+250[1−1.1^−4]/0.10 = −7.53363841 cost units. For L05, the alternate values are 900, 300, 0.08 and 4, giving approximately +93.6380520 cost units. These independent recomputations are deterministic scenario arithmetic, not investment recommendations. There is no tax, schedule, residual-value or correlated-uncertainty model.

Compare signs without ranking away evidence gaps. A positive NPV cannot offset missing seal compatibility or an open safety action. Record which assumptions would require sensitivity review and why one-at-a-time changes would not establish a probability distribution.

## Part 3: lag-one residual correlation

For each row calculate the four-residual mean, then

r₁ = Σ[(xᵢ−mean)(xᵢ₊₁−mean)] / Σ(xᵢ−mean)²,

with i=1..3 in the numerator and i=1..4 in the denominator. L04 residuals [1,1,−1,−1] have mean zero, numerator 1−1+1=1 and denominator 4, so r₁=0.25. L07 residuals [2,−2,2,−2] have mean zero and r₁=−0.75. These are descriptive lag-one summaries of repeated instrument records, not fitted time-series models or evidence of independent replication.

Check denominators and do not append fabricated residuals. Explain why autocorrelation changes the interpretation of naïve independent errors and why a zero value would not prove independence.

## Part 4: scale ratios

For each row compute the declared turbulent geometric-similarity power-per-volume ratio `(diameter_ratio)^2` and area/volume ratio `1/diameter_ratio`. L06 has ratio 2, so modeled P/V ratio is 4 and area/volume ratio is 0.5. L08 has ratio 1.5, giving 2.25 and 0.6666667 respectively. These dimensionless comparisons are not equipment duty ratings, blend-time predictions or heat-removal designs. Note which other similarity groups remain unmatched.

## Part 5: evidence-state audit

The CSV includes separate fields for all-wetted compatibility (including seals, gaskets and linings), traveler/joint traceability, inspection/NDE records, nonconformance, safety/MOC, measurement/control, acceptance evidence and responsible reviewers. Apply this deterministic learning rule:

- If any required field is `missing`, `open`, `unresolved`, `unauthorized` or `unnamed`, assign **HOLD** and `evidence_gaps_remain`.
- Only if every fictional field is `complete-synthetic`, `closed-verified-synthetic` or `named-synthetic-roles` may the row be `synthetic_review_complete`.
- Neither state means `production_approved`, code compliance, safe operation, process validation or commercial release.

L01 lacks seal/gasket evidence and remains HOLD despite straightforward arithmetic. L02 has an open safety/MOC action. L03 lacks inspection coverage. L04 has an unnamed responsible reviewer. L05 has unresolved nonconformance verification. L06 lacks measurement/control evidence. L07 has incomplete joint traceability. L08 has missing acceptance evidence. At least one row deliberately shows that good numeric results and unresolved evidence coexist.

## Deliverable and self-check

Prepare a concise design-review memo containing the four recomputed tables, scenario-by-scenario evidence states, named missing evidence and required qualified reviewer roles. Cite CSV row IDs and formulas. Do not write startup/shutdown, bypass/isolation, emergency, waste-transport, welding, NDE, relief-sizing, controller-download or pilot-run instructions.

The self-check is complete only when every numeric row has been independently reproduced, all repeated records remain descriptive, every gap stays unresolved, and no operational or release claim appears. The Case studio rubric is zero-point and does not assess competence. Real readiness requires named qualified process, mechanical/materials, safety, inspection, instrumentation, quality and regulatory reviewers using current authoritative standards.
