# Synthetic-data habitat audit lab

**Status:** Original zero-point lab in partial version 0.1.0; unreviewed and formative-only. Every row in `habitat-audit.csv` is original synthetic data. No row is a physical measurement, independent experiment or life-support result.

## Learning objectives

1. Recompute every synthetic energy and water row and quantify any nonzero balance residual.
2. Identify missing sensors, timer conflicts and review-gate failures without converting absent data into zero values.
3. Report per-scenario findings without treating reused or correlated rows as independent replicates or as real habitat evidence.

## Evidence and data dictionary

Download [habitat-audit.csv](habitat-audit.csv). Work with a spreadsheet or a simple table reader; no executable project code is required. Preserve the original file and make a working copy for calculations. Every `data_status` field must remain `synthetic-original`.

| Fields | Meaning and audit use |
| --- | --- |
| `record_id`, `scenario`, `duration_h` | Descriptive scenario identity and interval; identities are not independent-study identifiers |
| `grid_kwh`, `backup_kwh` | Declared electrical supplies for the interval |
| `lighting_kwh`, `climate_kwh`, `pumps_controls_kwh` | Declared load allocations within the model boundary |
| `water_start_l`, `water_input_l`, `water_recovered_l`, `water_consumed_l`, `water_end_l` | Opening stock, two input routes, declared consumption and closing stock |
| `temperature_status`, `human_gate` | Measurement availability and review status, not a temperature value or approval certificate |

For each row compute:

> energy residual = grid + backup − lighting − climate − pumps/controls.

> water residual = start + new input + recovered − consumed − end.

Keep the sign. A positive energy residual means supply exceeds declared loads; a negative one means declared loads exceed supply. Either can reveal a boundary or measurement problem. Do not add an “other” category just to force zero.

## Audit sequence

**1. Check provenance and shape.** Confirm six unique record IDs, the expected columns and the synthetic label. Check that outage rows A02 and A05 use their own durations rather than inheriting 24 h. Note that A01 and A06 reuse the normal-template structure; their agreement is not independent replication.

**2. Recompute all balances.** Rows A01, A02, A04, A05 and A06 have zero residuals under the declared model. A03 is deliberately discrepant: 30 − 14.4 − 9.6 − 4.8 = **+1.2 kWh**, and 138 + 30 + 40 − 50 − 156 = **+2 L**. Report both instead of hiding them in an adjustment.

**3. Audit missing evidence.** A04 has `temperature_status = missing`. This is not a zero temperature, a favourable temperature or proof of an excursion. Do not borrow A01's status as a measurement. A03 and A04 have unresolved human gates, so the audit cannot label their concepts reviewed even where arithmetic happens to close.

**4. Describe outage evidence separately.** A02 and A05 record 3.6 kWh and 2.4 kWh backup supply. Their descriptive total is **6.0 kWh**. Report it alongside the row durations of 6 and 8 h and each scenario's loads. The sum is not a reliability distribution or proof of adequate reserve.

**5. Write a per-scenario handoff.** Use one row per scenario with energy residual, water residual, missing evidence, gate status and required next evidence. Add a short narrative identifying the synthetic and correlated-data limitations. Do not pool the rows into Wilson intervals, confidence intervals, failure rates or a claim about a real habitat.

## Expected self-check

A complete audit contains all six rows, both formulas, A03's two nonzero residuals, A04's missing-temperature flag, the two outage durations and a statement that reused templates do not create independent evidence. It also explains why zero balance residuals cannot establish water quality, structural safety, actuator response or life-support performance.

## Common mistakes

- Auditing only A03 and assuming every other row closes without recomputation.
- Dropping residual signs or replacing them with unexplained balancing categories.
- Treating `missing` as zero or as permission to impute silently.
- Counting reused synthetic templates as independent experiments.
- Turning descriptive outage totals into real-world reliability or habitability claims.

## Scope and sources

This is a data-integrity exercise, not a habitat operation or statistical validation. [NASA ECLSS](https://www.nasa.gov/reference/environmental-control-and-life-support-systems-eclss) remains a link-only reference for the breadth of real engineered life-support subsystems, none of which is validated here. The owner's [habitat-resource-sandbox](https://github.com/dylanstechmann/habitat-resource-sandbox) is a personal hobby and learning project linked only as a resource-simulation exploration; this CSV is newly authored and imports none of its code or data. [MIT OCW 1.040](https://ocw.mit.edu/courses/1-040-project-management-spring-2004/pages/syllabus/) is a link-only comparator for documenting review and control decisions.
