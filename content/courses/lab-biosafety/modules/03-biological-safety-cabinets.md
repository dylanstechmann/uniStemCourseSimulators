# Biological safety cabinets: classes, selection and certification

The biological safety cabinet (BSC) is the primary barrier for most work with infectious material, and also one of the most misunderstood pieces of laboratory equipment. A laminar-flow clean bench looks similar and protects only the product; a chemical fume hood protects the worker but not the culture. This lesson explains how each class of BSC moves air, which protections each gives, how to choose one, and what certification checks. It follows Appendix A of BMBL, 6th edition (CDC and NIH, 2020), a US federal work adapted here with attribution. How to work inside a cabinet is practised in the [biological safety cabinet simulation](#/bench/class-ii-bsc-session-with-spill).

## Learning objectives

By the end of this lesson, you should be able to:

1. Distinguish personnel, product and environmental protection, and state which ones Class I, Class II and Class III cabinets, clean benches and fume hoods provide.
2. Describe the airflow of Class II Types A1, A2, B1 and B2, including inflow velocity and the share of air recirculated or exhausted.
3. Calculate the inflow volume of a cabinet from its face velocity and opening, and select a cabinet type for biological work with or without volatile chemicals.
4. State when a cabinet must be certified, what UV lamps can and cannot do, and how cabinet placement and room activity affect containment.

## Three kinds of protection

- **Personnel protection**: room air is drawn in at the front opening, so aerosols made inside do not reach the worker.
- **Product protection**: HEPA-filtered air flows down over the work surface, so room contaminants do not reach the culture.
- **Environmental protection**: air leaving the cabinet passes through a HEPA filter.

A **horizontal laminar-flow clean bench** blows HEPA-filtered air across the work surface toward the worker. It is not a BSC and protects only the product. BMBL says clean benches should never be used for cell culture materials, drug formulations, potentially infectious materials or other hazardous materials, because the worker is exposed to whatever is on the bench. They suit dust-free assembly of sterile equipment. A **chemical fume hood** draws room air in and exhausts it unfiltered: it gives personnel protection from vapours but no product protection and no HEPA filtration.

## The classes

**Class I.** Unfiltered room air is drawn in through the front opening at a minimum of 75 linear feet per minute (lfm) and leaves through a HEPA filter. It gives personnel and environmental protection but no product protection, so it is used mostly for enclosing equipment such as centrifuges or for aerosol-generating procedures where sterility does not matter.

**Class II.** Room air enters the front grille, HEPA-filtered air flows down over the work surface, and the downflow splits about halfway between the front and rear grilles, two to six inches above the surface. Class II cabinets give all three protections. The types differ in how much air they recirculate:

| Type | Minimum inflow | Air handling | Volatile toxic chemicals |
| --- | --- | --- | --- |
| A1 | 75 lfm | about 70% recirculated through the supply HEPA filter, 30% exhausted through the exhaust HEPA filter | not suitable |
| A2 | 100 lfm | as A1, with every positive-pressure contaminated plenum surrounded by negative pressure | small quantities only if exhausted outside through a canopy connection with an alarm |
| B1 | 100 lfm | about 70% of the downflow exhausted through the rear grille to the building exhaust, 30% through the front grille | small quantities, worked toward the rear |
| B2 | 100 lfm | total exhaust; nothing recirculated (up to about 1,200 cubic feet per minute of room air) | small quantities |

Type A1 and A2 cabinets can be connected to the building exhaust only through a **canopy** with a small air gap, never hard-ducted, because fluctuations in the building exhaust would upset the cabinet's balance. Type B cabinets are hard-ducted and depend on the building exhaust. If that exhaust fails, a B2 cabinet becomes pressurized and blows air from the work area back into the room, so B cabinets need exhaust alarms and interlocks.

**Class III.** A gas-tight enclosure with a non-opening window and heavy rubber gloves sealed to ports. Materials pass in and out through a dunk tank or a double-door pass-through that can be decontaminated. Supply air is HEPA-filtered, exhaust air passes through two HEPA filters (or a HEPA filter and an incinerator) to a dedicated exhaust, and the cabinet is held at a negative pressure of at least 0.5 inches of water. It gives the highest protection and is used for the most hazardous agents.

## Choosing a cabinet

BMBL's selection table matches cabinets to Biosafety Levels: Class I for personnel and environmental protection at BSL-1 to BSL-3; Class II for all three protections at BSL-1 to BSL-3; Class III, or Class II in a suit laboratory, at BSL-4. Within Class II the choice usually turns on chemicals. For cell culture and microbiology with no volatile toxic chemicals, a Type A2 is the usual choice. Work with small amounts of volatile toxic chemicals or radionuclides needs a cabinet that exhausts outside: an A2 with a canopy connection and alarm, or a Type B. A B2 costs the most to run, so BMBL says its use should be justified by the risk assessment.

## Inflow volume

The inflow that protects the worker is a velocity through an opening, so the volume of air drawn in is

  Q = v × A,

with v the face velocity and A the area of the front opening. A cabinet with a 4.0 ft wide opening and an 8.0 in (0.667 ft) sash height has A = 2.67 ft². At the Type A2 minimum of 100 lfm, Q = 100 × 2.67 = 267 cubic feet per minute. Raising the sash to 10 in at the same fan setting spreads the same airflow over 3.33 ft², so the face velocity falls to 267/3.33 = 80 lfm, below the A2 minimum. That is why the sash must stay at its certified, marked height, and why a cabinet alarms when it is raised.

## Placement, room activity and certification

Containment depends on the air curtain at the front opening, which room activity can disrupt. BMBL warns about rapid arm movements, walking traffic, room fans and doors opening near the cabinet face. Cabinets need clearance around and above them for maintenance and exhaust-filter testing.

Every cabinet must be field-certified, to NSF/ANSI 49 Annex F, by experienced, qualified personnel, preferably accredited certifiers:

- when it is installed, before it is put into service;
- at least annually thereafter;
- whenever a HEPA or ULPA filter is replaced or internal parts are repaired;
- whenever the cabinet is moved, because relocation can break filter seals.

**UV lamps.** BMBL says UV lamps should not be used as the sole disinfection method in a BSC. If they are installed, they need regular cleaning and checking with a UV meter, and replacing when output falls below 40 µW/cm². Unshielded lamps must be off when the room is occupied, and the sash is closed while the lamp is on.

## Common mistakes

- Using a laminar-flow clean bench for infectious work because it "has a HEPA filter".
- Raising the sash for more room to work, which lowers the face velocity.
- Hard-ducting a Type A cabinet to the building exhaust.
- Using volatile solvents in a recirculating A1 or A2 cabinet.
- Trusting a UV lamp in place of wiping surfaces with disinfectant.
- Continuing to use a cabinet past its certification date, or after moving it, without recertification.

## Worked example

**Problem.** A stem-cell laboratory needs a cabinet for human iPSC culture at BSL-2. A collaborator also wants to fix cells with small volumes of paraformaldehyde and handle a volatile solvent in the same cabinet. The cabinet's opening is 5.0 ft wide with a 10.0 in sash. What inflow volume must it draw to meet the Type A2 minimum, and what type should the laboratory choose?

**Step 1: opening.** A = 5.0 ft × (10.0/12) ft = 4.17 ft².

**Step 2: inflow.** Q = 100 lfm × 4.17 ft² = 417 cubic feet per minute.

**Step 3: type.** Culture alone suits an A2 recirculating to the room. Volatile chemicals need exhaust to the outside: an A2 with a canopy connection and exhaust alarm (small quantities), or a Type B. Often the better answer is to move the solvent work to a chemical fume hood and keep the cabinet for culture.

**Step 4: before use.** Check the certification label, and recertify after installation.

## Limits of this lesson

Airflow descriptions are simplified from BMBL Appendix A, which in turn refers to NSF/ANSI 49-2018 (not read for this course). Real selection depends on the risk assessment, the manufacturer's specifications and your biosafety officer. Type C1 cabinets and the details of field-certification tests are not covered.
