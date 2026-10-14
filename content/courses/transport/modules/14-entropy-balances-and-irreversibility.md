# Entropy balances and irreversibility

## Learning objectives

1. Separate entropy carried by heat or mass from entropy generated within a system.
2. Write a closed-system or steady-flow entropy balance with consistent signs and absolute temperature.
3. Check a proposed process against the second law and distinguish entropy generation from energy accumulation.

## Energy is conserved; entropy can be generated

An energy balance accounts for energy stored, transferred as heat or work, and carried by flowing material. The second law adds a different accounting rule: entropy may cross the boundary or be generated inside, but entropy generation cannot be negative. In a reversible idealization, generation is zero. Friction, mixing and heat transfer across a finite temperature difference generate entropy even when the energy balance closes exactly.

Keep three quantities distinct. A system's entropy change is `ΔS`; entropy transfer with heat depends on the boundary temperature where that heat crosses; and entropy generation is `S_gen ≥ 0`. Moving material also carries entropy into or out of a control volume. Work transfers energy but does not carry entropy directly in this classical balance.

## Closed-system balance

For a closed system with no mass crossing its boundary,

`ΔS = Σ_j ∫(δQ_j/T_b,j) + S_gen`.

Heat `δQ` is positive into the system. `T_b` is the absolute temperature, in kelvin, at the boundary location where that heat is transferred. If the boundary temperature is constant during a heat transfer `Q`, its entropy transfer is `Q/T_b`. Heat leaving the system contributes a negative term. Use kelvin, not degrees Celsius, because entropy transfer depends on absolute thermodynamic temperature.

For a synthetic box receiving `600 J` at a uniform boundary temperature of `300 K`, the heat transfer brings in `2 J/K` of entropy. If internal friction generates another `0.2 J/K`, the balance gives `ΔS=2.2 J/K`. The system entropy change is greater than the transfer term because the process is irreversible. If the same closed system is adiabatic, `Q=0` and `ΔS=S_gen`; that equality does not apply to a system exchanging heat.

## Steady-flow control volume

For a control volume with steady storage, use specific entropy `s` for each stream and absolute boundary temperatures for heat transfer:

`0 = Σ_in ṁ s − Σ_out ṁ s + Σ_j(Q̇_j/T_b,j) + Ṡ_gen`.

Each stream term is mass rate times specific entropy. Heat into the volume is positive, and `Ṡ_gen ≥ 0`. At steady state the entropy stored in the control volume does not change, but entropy can still enter with streams, leave with streams, cross with heat, and be generated inside. The terms have units such as `W/K` or `kW/K`.

Consider an adiabatic, well-mixed ideal flow device with one inlet and one outlet, each at `0.10 kg/s`, and specific entropies `2.0` and `2.3 kJ/(kg·K)`. The stream contribution is `0.10(2.0−2.3)=−0.03 kW/K`, so steady balance requires `Ṡ_gen=0.03 kW/K`. The outlet stream carries away more entropy than entered; no heat transfer supplied it, so the difference was generated within the modeled volume. The values are stipulated for arithmetic practice and identify no real device.

If the same adiabatic calculation instead implied negative entropy generation, the stated process would violate the second law. Treat that as evidence that the assumed data or model is incomplete or inconsistent: check stream directions, signs, omitted heat and mass streams, and the steady-state assumption. Do not report negative entropy generation as a physical result.

## A finite-temperature heat transfer

Transfer `1200 J` of heat from a hot reservoir at `400 K` to a cold reservoir at `300 K`. For the two-reservoir universe, no heat crosses the outer boundary. The hot reservoir loses `1200/400=3 J/K`; the cold reservoir gains `1200/300=4 J/K`. Total entropy change and generation are therefore `1 J/K`, equivalently `Q(1/T_cold−1/T_hot)>0`. The energy lost by one reservoir exactly equals the energy gained by the other, yet the process generates entropy because heat passes across a finite temperature difference. Reversible heat transfer in the limiting case of no temperature difference generates none.

This calculation also shows why using Celsius would be wrong: reciprocals of Celsius readings are not thermodynamic entropy-transfer factors. Check signs by asking which body loses heat and which gains it before substituting values.

## A balance checklist

1. Draw the system or control-volume boundary and mark every heat and mass crossing.
2. Choose signs and units; label heat into the boundary as positive.
3. Use absolute temperature at each heat-transfer boundary and specific entropy for each material stream.
4. Set the accumulation term to zero only when the system is at steady state.
5. Solve for generation or change, then check that entropy generation is nonnegative.
6. Keep the energy balance separate; a correct energy balance does not by itself establish a second-law-consistent process.

## Limits of this lesson

The examples introduce classical entropy bookkeeping for selected closed and steady-flow systems. They do not develop chemical potential, phase equilibrium, exergy, statistical thermodynamics, reacting-mixture property tables or a full thermodynamics course. Stream properties and temperatures are stipulated; no empirical medium, cell culture, equipment specification or operating procedure is represented. Practice checks selected signs and calculations, not a written derivation or engineering design. The new instruction is original with substantial AI assistance; MIT materials are links used to compare scope, and no source asset is imported.
