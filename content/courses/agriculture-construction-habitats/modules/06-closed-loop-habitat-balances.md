# Closed-loop habitat energy, water and outage balances

**Status:** Original lesson in partial version 0.1.0; unreviewed and formative-only. All habitat values are synthetic spreadsheet inputs. This is not a life-support design, human-rating exercise, habitability assessment or emergency guide.

## Learning objectives

1. Reconcile electrical supply and load energy over normal and backup intervals with explicit residual terms.
2. Reconcile stored water, new input, recovery and consumption without equating a recovery fraction with safety or autonomy.
3. Evaluate outage duration, critical-load assumptions and unmodelled hazards without making life-support or habitability claims.

## “Closed loop” is an accounting hypothesis

Calling a habitat closed-loop does not make matter or energy disappear. The boundary still receives energy, may receive new water and materials, and exports heat, products and waste. A loop describes one or more return flows within that boundary. The analyst must show what is recovered, what treatment and energy the return requires, and which losses remain.

For an interval, a useful electrical ledger is:

> grid energy + backup energy − lighting − climate − pumps/controls − other declared loads = residual.

A zero residual means the declared quantities reconcile. A nonzero residual is a finding: perhaps a load is missing, metering intervals disagree or arithmetic is wrong. Neither result demonstrates reliability. The model also needs time resolution, because a daily energy total can conceal intervals when demand exceeds available power.

Water has an analogous ledger:

> opening stock + new input + recovered water − consumption − other declared outputs − closing stock = residual.

Recovery volume is not quality evidence. Treatment performance, storage condition, suitability for a use and monitoring all require separate evidence. This lesson does not evaluate or specify them.

## Worked normal and recovery examples

**Synthetic electrical interval.** Grid supplies 28.8 kWh and backup supplies zero. Lighting uses 14.4 kWh, climate 9.6 kWh and pumps/controls 4.8 kWh. The residual is 28.8 − 14.4 − 9.6 − 4.8 = **0 kWh** for these categories. If pumps had been omitted, the same records would misleadingly suggest 4.8 kWh of spare energy.

**Synthetic recovery share.** An interval uses 36 L recovered water and 24 L new input. The recovered fraction of combined supply is 36/(36 + 24) × 100 = **60%**. This ratio says nothing about water safety, continuity of supply, treatment energy or whether people could depend on it.

**Synthetic stock during an outage.** A tank starts at 150 L, receives no new input, recovers 12 L and records 30 L consumed. Closing stock is 150 + 0 + 12 − 30 = **132 L**. The closing amount does not show that every demand was met throughout the interval; the time sequence still matters.

## Outage analysis begins with critical loads and time

An outage balance first names which loads are considered critical and why. Lighting, climate, pumps and controls should not silently inherit the normal-operation profile. Some may stop, others may have different demand, and some unmodelled hazards may dominate. The interval itself must be explicit.

**Synthetic outage energy.** A declared critical load is 0.35 kW for 8 h. Energy required is 0.35 × 8 = **2.8 kWh before reserves or conversion losses**. A device labelled 1 kW describes power, not stored energy. Actual deliverable energy depends on its state, operating limits, losses and load profile.

A robust report separates at least three questions: Does power suffice at each moment? Does energy suffice over the interval? Do temperature, water and other conditions remain within evidence-based limits? This course addresses only simplified versions of the first two and cannot answer the third for a real habitat.

## Common mistakes

- Equating a recovery percentage with quality, autonomy or life-support performance.
- Omitting support loads from the boundary and calling the residual spare capacity.
- Treating power rating as energy capacity or daily energy as proof of instantaneous adequacy.
- Assigning normal-operation loads to an outage without a stated rationale.
- Converting a balanced spreadsheet into a claim of safe occupancy or emergency readiness.

## Scope and sources

This lesson teaches conservation arithmetic and model boundaries only. It does not design air, water, waste, fire, medical, structural or emergency systems. [NASA's Environmental Control and Life Support Systems overview](https://www.nasa.gov/reference/environmental-control-and-life-support-systems-eclss) is a link-only reference showing that real ECLSS spans multiple engineered subsystems and verification contexts; it is not a template reproduced here. The owner's [habitat-resource-sandbox](https://github.com/dylanstechmann/habitat-resource-sandbox) repository is a personal hobby and learning project linked only as a resource-simulation exploration; no code, parameters or validation claims are imported. [MIT OCW 1.040](https://ocw.mit.edu/courses/1-040-project-management-spring-2004/pages/syllabus/) remains a link-only comparator for integrating risk and project review. No human-rating, operational or endorsement claim follows.
