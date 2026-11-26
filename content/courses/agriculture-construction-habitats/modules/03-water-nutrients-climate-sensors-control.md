# Water and nutrient inventories, climate sensors and control

**Status:** Original lesson in partial version 0.1.0; unreviewed and formative-only. All ledgers and sensor records are synthetic. This lesson supplies no nutrient formulation, concentration target, dosing recipe or autonomous operating procedure.

## Learning objectives

1. Close synthetic water and material-inventory balances with explicit initial stock, inputs, outputs and final stock.
2. Distinguish sensor readings, calibration evidence, missing data and spatial variation when interpreting climate records.
3. Evaluate feedback-control logs, actuator evidence and human fallback gates without treating a setpoint as a biological prescription.

## Conservation before interpretation

A water ledger begins with a defined store and interval. New input, recovered water, consumption, discharge and unmeasured loss are distinct categories even when they share volume units. Recovery describes a route within the model, not potability or suitability for a particular use. Consumption is also an accounting category: it may combine biological use and other declared removals, and those components should not be invented if they were not measured.

**Synthetic water example.** A tank starts at 180 L. It receives 40 L new input and 30 L recovered water, while 70 L is recorded as consumed. Closing stock is 180 + 40 + 30 − 70 = **180 L**. The unchanged level does not show constant quality, zero risk or an ideally performing recovery system. It means only that the four displayed terms balance.

A material inventory can be audited with the same conservation logic without turning it into a prescription. Another synthetic ledger starts with 12 mmol of a declared material, transfers 3 mmol out and assigns 4 mmol to estimated uptake. The unallocated remainder is **5 mmol**. No volume, concentration or application instruction is inferred. In a real investigation, analytical measurements, uncertainty and the validity of the uptake estimate would need independent review.

## Sensor data are evidence with a history

A climate record is not a transparent view of the environment. It reflects sensor physics, placement, calibration, sampling, processing and storage. Temperature at one height may differ from temperature at another. A probe near an outlet may describe the outlet rather than the canopy. Before calculating a mean, check whether the observations share units, location, interval and measurement status.

Three synthetic co-located readings of 22 °C, 24 °C and 23 °C have mean **23 °C**. The mean does not remove calibration bias or establish spatial uniformity. If another record is missing, the correct entry is `missing`, not zero. A carried-forward value is an imputation and must be labelled as such, with its effect on any conclusion made explicit.

Calibration or comparison evidence should have a timestamp and a relevant range. A sensor can agree with a reference at one condition and drift at another. The audit should separate precision from accuracy: repeated values can be tightly clustered around a biased reading. Status flags, maintenance records and raw observations belong in the evidence package rather than being hidden behind a cleaned dashboard.

## Feedback requires observed response and a safe fallback

A control loop compares a measured quantity with a desired state and adjusts an actuator. A setpoint records intention; it is not proof of the measured condition. Likewise, a command issued to a pump or fan is not proof that the device responded. Useful logs include measurement, setpoint, command, actuator feedback, alarm, manual override and time synchronization.

Oscillation, long delays and repeated saturation are findings to investigate, not defects to edit away. If actuator status is unavailable or observations become implausible, the concept should enter its declared safe fallback and await responsible human review. This course does not define that fallback for a real facility. Real limits and emergency responses require local engineering, biological and operational review.

**Synthetic decision example.** A controller oscillates while its actuator-status channel is missing. Deleting the oscillating samples would destroy evidence; increasing the command would assume an unverified remedy. The defensible audit marks control performance unresolved, preserves the log and requests sensor, actuator and fallback review.

## Common mistakes

- Using unchanged storage to infer unchanged quality or reliability.
- Turning a material-inventory exercise into a nutrient recipe.
- Replacing missing observations with zero or silent repetition.
- Treating co-located precision as proof of spatial accuracy.
- Confusing commands, setpoints and dashboard values with actual actuator and environmental states.

## Scope and sources

The lesson introduces conservation accounting and control-evidence literacy, not irrigation design, plant nutrition, HVAC design or control certification. [MIT OCW 1.74, Fall 2020](https://ocw.mit.edu/courses/1-74-land-water-food-and-climate-fall-2020/pages/food-and-natural-resources/resources-for-food-production-water/) is a link-only comparator for water in agricultural context. [USDA NRCS Subpart T](https://directives.nrcs.usda.gov/sites/default/files2/1723052016/Subpart%20T%20-%20Urban%20Agriculture.pdf) supplies a link-only broader urban-agriculture reference. The owner's [rural-florida-agriculture](https://github.com/dylanstechmann/rural-florida-agriculture) and [iran-vertical-agriculture](https://github.com/dylanstechmann/iran-vertical-agriculture) repositories are personal hobby and learning projects linked only for contrasting system contexts. No operating parameters, datasets, code or instructions are imported, and no physical validation is implied.
