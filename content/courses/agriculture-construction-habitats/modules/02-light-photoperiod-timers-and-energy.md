# PPFD, DLI, photoperiod, timers and lighting energy

**Status:** Original lesson in partial version 0.1.0; unreviewed and formative-only. All measurements, fixtures and schedules are synthetic engineering examples, not crop-specific recommendations.

## Learning objectives

1. Convert between photosynthetic photon flux density and daily light integral with explicit time and unit conventions.
2. Compute lighting energy from fixture power and operating time, including independent checks of timer behaviour.
3. Interpret photoperiod, spatial light variation and energy records without inferring crop response from engineering quantities alone.

## Photon rate and daily photon total

Photosynthetic photon flux density (**PPFD**) describes the rate at which photons in the photosynthetically active radiation range arrive at a surface. In this lesson its units are µmol m⁻² s⁻¹. Daily light integral (**DLI**) accumulates photon delivery over a day and has units mol m⁻² d⁻¹. For a constant PPFD over a stated interval:

> DLI = PPFD × hours × 3600 / 1,000,000.

The factor 3600 converts hours to seconds, and one million converts micromoles to moles. If PPFD changes during the interval, integrate or sum the time-resolved measurements instead of assuming one value. A uniform value inferred from DLI is only an average; it does not prove that intensity was constant or that every canopy location received the same light.

**Synthetic example A.** A measurement of 200 µmol m⁻² s⁻¹ persists for 14 h. DLI = 200 × 14 × 3600/10⁶ = **10.08 mol m⁻² d⁻¹**. Conversely, DLI 12 distributed uniformly over 16 h corresponds to mean PPFD = 12 × 10⁶/(16 × 3600) = **208.333333… µmol m⁻² s⁻¹**.

PPFD is local. Height, fixture spacing, obstruction, canopy development and sensor orientation can produce gradients. A credible record identifies sensor location, height, time, instrument status and whether the value is measured or inferred. One central reading should not be presented as a canopy-wide map.

## Photoperiod is elapsed state, not summed timer labels

Photoperiod concerns the daily light and dark intervals experienced by the organism. Timer programming is evidence of intended control, not automatically evidence of delivered light. Power loss, relay faults, manual overrides, overlapping channels and sensor errors can separate command from outcome.

Suppose one synthetic channel commands a fixture from 08:00 to 20:00 and another commands the same fixture from 18:00 to 22:00. If both channels work, the on-state is the **union** of those intervals: 08:00 to 22:00, or **14 h**. Adding 12 h and 4 h to claim 18 h counts the two-hour overlap twice and can also exceed the elapsed window. An audit should combine command logs with an independent on/off or power record and document any gaps.

Photoperiod response is biological and species-, cultivar- and context-dependent. DLI and photoperiod can be equal between two schedules while intensity, darkness distribution and spectral conditions differ. This lesson therefore makes no universal scheduling or yield claim.

## Lighting energy and its system boundary

Electrical energy is power integrated over time. For constant fixture power:

> energy (kWh) = number of fixtures × power per fixture (kW) × operating time (h).

**Synthetic example B.** Four fixtures each draw 0.12 kW for 14 h. Their energy is 4 × 0.12 × 14 = **6.72 kWh**. This is fixture input energy, not photon output and not the energy of the whole growing system. Drivers, climate equipment, pumps, controls and conversion losses require separate entries if they belong to the declared boundary.

Nameplate power can be a useful estimate but is not a daily energy measurement. Dimming, degradation and actual switching can change power draw. A stronger energy audit uses measured power over verified intervals and reconciles it with the timer union. It also reports whether the interval is one day, a production cycle or an outage.

## Common mistakes

- Forgetting either the seconds-per-hour or micromoles-per-mole conversion.
- Dividing DLI by photoperiod without restoring SI time and amount units.
- Adding overlapping schedules instead of taking their union.
- Treating a setpoint, nominal wattage or timer command as measured delivery.
- Assuming equal DLI proves equal growth, nutrition, quality or resource efficiency.

## Scope and sources

This lesson covers definitions, arithmetic and audit evidence only. It does not provide crop-specific light recipes, spectral design, electrical installation instructions or a validated production model. [USDA NRCS Urban Agriculture Subpart T](https://directives.nrcs.usda.gov/sites/default/files2/1723052016/Subpart%20T%20-%20Urban%20Agriculture.pdf) is a link-only reference for the wider controlled-environment context. The owner's [iran-vertical-agriculture](https://github.com/dylanstechmann/iran-vertical-agriculture) repository is a personal hobby and learning project, linked only as an exploration of vertical-system questions. No source table, operating value, prose, code or design has been copied, and no biological performance or engineering review is claimed.
