# Decontamination, disinfection and sterilization

Everything that touches infectious material, from benchtops and pipettes to cultures and waste, has to be made safe before it leaves the laboratory or is reused. The words for doing this are often used loosely, but they mean different things and promise different results. This lesson follows Appendix B of BMBL, 6th edition (CDC and NIH, 2020), a US federal work adapted here with attribution. It covers the definitions, what makes disinfection succeed or fail, how to choose and dilute a chemical disinfectant, and how steam sterilization is verified.

## Learning objectives

By the end of this lesson, you should be able to:

1. Define cleaning, disinfection, sterilization and decontamination, and state what each does and does not guarantee.
2. Rank classes of microorganisms by their resistance to chemical disinfectants, and list the factors that determine whether disinfection works.
3. Choose a disinfectant by activity level and prepare a sodium hypochlorite solution of a target concentration from household bleach.
4. Use D-values to relate exposure time to log reduction and sterility assurance, and describe how autoclave cycles are monitored and validated.

## Four words, four promises

- **Cleaning** physically removes gross contamination (blood, tissue, medium) so that later processing can work. It may have no antimicrobial effect, but it is often a prerequisite: organic matter protects microorganisms and uses up disinfectant.
- **Disinfection** eliminates nearly all recognized pathogens, but not necessarily all microbial forms. It may leave bacterial spores, and it has no sterility margin.
- **Sterilization** makes an item free of all living microorganisms, including spores and viruses. Because a single survivor can never be ruled out, sterilization is defined operationally: a process after which the probability of any microorganism surviving on an item is less than one in a million, a **sterility assurance level (SAL)** of 10⁻⁶.
- **Decontamination** makes an item, area or material safe to handle, reasonably free of risk of disease transmission. In a laboratory, waste and used materials are often decontaminated by a sterilization process such as steam autoclaving.

## What makes disinfection work

BMBL lists five factors that determine the result:

1. the nature and number of contaminating organisms, especially bacterial spores;
2. the amount of organic matter (soil, blood, medium);
3. the type and condition of the surfaces or items;
4. temperature;
5. contact (exposure) time.

Organisms differ widely in resistance. BMBL ranks them, from most to least resistant to disinfectant chemicals:

1. prions;
2. bacterial spores;
3. mycobacteria;
4. non-enveloped or small viruses;
5. fungi;
6. vegetative bacteria;
7. enveloped or medium-size viruses, which include HBV, HCV and HIV.

There are exceptions. Bacteria in biofilms, for example, can approach the resistance of spores. A disinfectant that kills the agent you work with, at the concentration and contact time on its label, is the one to use. For routine work BMBL recommends a broad-spectrum product with a tuberculocidal (mycobactericidal) claim. In the United States, surface disinfectants are EPA-registered products and must be used according to their labels.

## Choosing a liquid disinfectant

BMBL tabulates the activity levels of generic chemical disinfectants, including:

| Chemical | Concentration | Activity level |
| --- | --- | --- |
| Hypochlorites (bleach) | 500–6000 mg/L free available chlorine | intermediate to high-level disinfection |
| Alcohols (ethyl, isopropyl) | 70% | intermediate-level disinfection |
| Hydrogen peroxide | 3–6% | intermediate to high-level disinfection |
| Phenolics | 0.5–3% | low to intermediate |
| Iodophors | 30–50 mg/L free iodine | low to intermediate |
| Quaternary ammonium compounds | variable | low-level disinfection |

Seventy percent ethanol evaporates quickly and does not reliably kill spores. It is useful for wiping cabinet surfaces and items entering a cabinet, but the surface has to stay wet for the contact time. Bleach is broad-spectrum, cheap and corrosive, so stainless steel needs a sterile-water wipe afterwards, as the [cabinet lesson](03-biological-safety-cabinets.md) notes.

**Diluting bleach.** For dilute aqueous solutions, a percentage of sodium hypochlorite converts to parts per million by multiplying by 10,000: household bleach labelled 6.0% holds about 60,000 ppm. Using C₁V₁ = C₂V₂ from the [laboratory-measurement package](../../lab-measurement/modules/02-dilutions-and-dilution-series.md), 1.00 L of 5,000 ppm needs 1.00 × 5,000/60,000 = 0.0833 L, or 83.3 mL of bleach made up to 1 L. A tenfold dilution of 6.0% bleach gives 6,000 ppm, the top of BMBL's range. Diluted bleach loses available chlorine over time, so laboratories set how often it must be remade.

## Steam sterilization and its verification

Moist heat under pressure is the workhorse for media, glassware and waste. BMBL gives an example: a steam cycle for **pre-cleaned** items can be 20 minutes at 121 °C. Waste with a high bioburden and no pre-cleaning needs longer cycles, verified and validated for the typical load, because organisms can be shielded from steam and the centre of a dense load heats slowly.

**D-values.** Heat kills microorganisms roughly exponentially. The D-value is the time at a stated temperature to reduce a population tenfold, so after time t,

  N = N₀ × 10^(−t/D).

Biological indicators (BIs) carry a known population of resistant spores, commonly *Geobacillus stearothermophilus* for steam. In a synthetic example with N₀ = 10⁶ spores and D₁₂₁ = 2.0 min, reducing the BI to one expected survivor takes 6 × 2.0 = 12 min. Reaching a SAL of 10⁻⁶, twelve log reductions in all, takes 24 min at temperature. That exposure begins only when the slowest-heating point of the load reaches 121 °C.

**Monitoring and validation.** BMBL describes two levels.

- **Routine verification.** Record each cycle's time, pressure and temperature, and place BIs within loads.
- **Validation.** For a typical waste load, use thermocouples and BIs placed throughout the load to show that steam penetrates and the required exposure is reached everywhere.

Chemical indicator tape shows that an item was exposed to heat, not that the load was sterilized.

Validating a waste cycle is practised in the [autoclave validation simulation](#/bench/autoclave-waste-load-validation), where the heating lag and the indicator lot change from run to run.

Practical points for waste in autoclave bags: close bags loosely so steam can enter, and carry them in a leak-proof tray or pan. Decide by testing whether water must be added. Never overload the chamber.

## Common mistakes

- Spraying 70% ethanol and wiping it off at once, before any contact time.
- Disinfecting a surface still covered in spilled medium, without first absorbing and cleaning it.
- Using an old bleach dilution, or diluting by eye.
- Assuming a cycle on the autoclave display sterilized the centre of a dense waste bag.
- Reading autoclave tape as proof of sterility.
- Using a low-level quaternary ammonium product against spores or non-enveloped viruses.

## Worked example

**Problem.** A laboratory decontaminates spills of a BSL-2 culture with 5,000 ppm hypochlorite and validates its waste cycle. (a) How do you make 500 mL of 5,000 ppm from bleach labelled 8.25%? (b) A thermocouple at the centre of a typical waste load reaches 121 °C 18 min after the chamber does. With BIs of 10⁶ spores and D₁₂₁ = 2.0 min, what minimum chamber time at 121 °C gives a SAL of 10⁻⁶ at the centre?

**Step (a).** 8.25% is about 82,500 ppm. V₁ = 500 × 5,000/82,500 = 30.3 mL of bleach, made up to 500 mL.

**Step (b).** The centre needs 12 × 2.0 = 24 min at temperature, and gets there 18 min after the chamber, so the chamber needs at least 18 + 24 = 42 min at 121 °C. The cycle is then confirmed with BIs placed at the centre of real loads.

## Limits of this lesson

The D-value, lag time and bleach concentrations in examples are synthetic or typical values for illustration. Real disinfectant choice follows the product label, the agent and your institution's SOPs. Space decontamination with formaldehyde, hydrogen peroxide vapour or chlorine dioxide, the inactivation of prions, and the validated inactivation procedures of BMBL Appendix K are only mentioned.
