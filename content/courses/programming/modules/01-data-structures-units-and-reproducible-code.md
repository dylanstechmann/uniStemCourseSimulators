# Data structures, units, and reproducible code

Scientific code is easier to trust when its inputs, assumptions and outputs are explicit. A data structure should preserve how a measurement was obtained, not just its numeric value. A vector can store repeated measurements, while a record or dictionary can keep each value beside its sample, treatment, donor, batch and unit. If those fields are separated or their order is unclear, a correct formula can still produce a mislabeled result.

## Put units and validity in the data contract

A data contract states what inputs a function accepts and what its result means. It should specify units, allowed ranges, shape, missing-value rules and transformations. Missing is not zero: replacing an absent measurement with zero changes the dataset and its meaning. Likewise, silently accepting a negative mass, zero volume or unknown unit can turn a pipeline error into a plausible-looking number.

For example, suppose a sample contains 1.5 mg of material in 500 µL. Convert volume before dividing: $500\,\mu\text{L}=0.5\,\text{mL}$, so concentration is $1.5\,\text{mg}/0.5\,\text{mL}=3\,\text{mg/mL}$. Dividing by the raw number 500 would produce a value on the wrong scale. Keeping the input unit beside each measurement makes that conversion visible and reviewable.

## Prefer small pure functions

A pure function has explicit inputs and returns an output without changing its arguments, reading hidden global state or printing in place of returning a result. Identical inputs then produce identical outputs, so a test can compare a hand-calculated case with the returned value. Parsing, validation, unit conversion and calculation can be separate steps, each with a narrow purpose and clear failure behavior.

For the example above, a concentration function could accept `mass_mg` and `volume_uL`, reject non-finite or out-of-range values, convert microlitres to millilitres, and return `mass_mg / volume_mL`. A hand-checkable test should confirm that 1.5 mg and 500 µL return 3 mg/mL. Separate tests should exercise zero volume, negative mass and missing input. The function should not modify the raw record or silently substitute a default.

## Preserve provenance

Keep raw input files unchanged and write cleaned or summarized data as a derived artifact. Record the input identity, code version, parameters, unit conversions and relevant software environment so another analyst can reproduce the path from observations to result. If a procedure uses randomness, record the seed and generator as part of that record; a seed helps reproduce a run but does not make an unsuitable method valid.

Use array or table axes deliberately. State whether rows are samples and columns are features, and preserve identifiers when filtering or sorting. Shape checks can catch an accidental transpose, but they do not prove that sample labels align. Before reporting a summary, check row counts, rejected-record reasons, units and a few values against independent calculations.

These practices make a result auditable, not automatically correct. The example is a constructed unit conversion; it supplies no real assay data, validated protocol or evidence about biological samples. Later lessons develop explicit input contracts, parsing and testing in more detail.
