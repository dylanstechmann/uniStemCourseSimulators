# Agricultural systems, inventories and site boundaries

**Status:** Original lesson in partial version 0.1.0; unreviewed and formative-only. Every site, value and scenario below is synthetic and is not a development proposal.

## Learning objectives

1. Draw a system boundary that separates production zones, support flows, wastes and external dependencies.
2. Reconcile synthetic land, water and input inventories without mistaking accounting for impact proof.
3. Evaluate site evidence and identify permissions, safety and community questions reserved for local reviewers.

## A system is a boundary plus stocks and flows

An agricultural system is not just a crop bed or a building. It is a chosen accounting boundary placed around living organisms, structures, equipment, people, material stocks and flows. A useful first map names production zones, support zones, energy and water entering, products leaving, residues and waste leaving, and information used for control. The map should also name what is deliberately outside it. Omitting a pump or an external energy source can make a favourable balance an artefact of drawing the boundary too narrowly.

Boundaries can be nested without being interchangeable. A **site boundary** may include paths, tanks and a packing area; a **production boundary** may include only the growing zones; an **operational interval** may cover one day, an outage or a crop cycle. A result must state which of these it uses. A percentage based on daily recovered water cannot silently become a claim about annual site independence, just as production area cannot silently become total land area.

Stocks are quantities present at a stated time, such as stored water or unallocated material. Flows change those stocks over an interval. The elementary ledger is:

> closing stock = opening stock + inputs − outputs ± recorded adjustments.

An adjustment is not a convenient plug. It needs a reason, evidence and an auditable sign. If the ledger does not close, report the residual and investigate missing flows, inconsistent intervals, metering or arithmetic.

## Worked synthetic boundary and inventory

A fictional teaching site has two growing zones of 120 m² and 80 m². Its site also contains 30 m² of shared paths. The production boundary therefore contains 120 + 80 = 200 m² before exclusions, or **170 m²** after paths are excluded. The paths remain in the site boundary, so removing them from production does not remove their construction, drainage or maintenance implications.

A daily water table records 18 L rainfall capture, 32 L reclaimed input and 50 L municipal input. Combined input is 100 L and the reclaimed share is **32%**. A support reservoir separately starts at 240 L, receives 60 L and records 180 L used, leaving **120 L**. None of these results establishes water quality, annual availability, ecological effect or financial performance. They only reconcile the displayed synthetic quantities.

| Boundary question | Evidence to retain | A claim to avoid |
| --- | --- | --- |
| What counts as production? | Zone identifiers, areas and shared-use exclusions | Calling production area the whole site |
| Which inputs cross the boundary? | Source, quantity, interval and measurement status | Treating recycled and new input as interchangeable quality evidence |
| Which outputs cross it? | Product, consumption, losses and waste routes | Assuming an unmeasured output is zero |
| What remains uncertain? | Residuals, missing records and alternative explanations | Hiding imbalance with an unexplained adjustment |

## Site evidence is more than an attractive ledger

A location can have a closed spreadsheet balance and still be unsuitable. Access, drainage, contamination history, neighbours, waste handling, worker safety, land-use rules and environmental obligations can change the decision. Indoor and vertical systems also depend on equipment access, fire and electrical review, maintenance and reliable external services. Rural systems can have different water, transport and ecological constraints. One generic checklist cannot settle these issues across jurisdictions.

For that reason, a concept dossier should contain a **human-gate register**. Name the question, responsible reviewer or authority, evidence required and current status. Examples include local land-use permission, water-source acceptance, structural and electrical review, environmental obligations and community impacts. “Not yet reviewed” is an honest status; “balanced, therefore approved” is not.

## Common mistakes

- Drawing the boundary around the crop while excluding the energy and equipment that make production possible.
- Mixing daily and seasonal flows, or production area and total site area.
- Treating a nonzero residual as rounding without checking its size and cause.
- Inferring regulatory, ecological or community acceptability from resource arithmetic.
- Treating an owner repository as a validated site design rather than a linked learning reference.

## Scope and sources

This is a short systems-literacy lesson, not agronomy, site engineering or legal advice. [MIT OCW 1.74, Fall 2020](https://ocw.mit.edu/courses/1-74-land-water-food-and-climate-fall-2020/pages/syllabus) is a link-only comparator for land, water, nutrients, environmental effects, technology and agricultural context; its broader reading seminar is not reproduced. [USDA NRCS Subpart T, amended August 2024](https://directives.nrcs.usda.gov/sites/default/files2/1723052016/Subpart%20T%20-%20Urban%20Agriculture.pdf) is a link-only reference for the breadth of urban-agriculture planning. The owner's [rural-florida-agriculture](https://github.com/dylanstechmann/rural-florida-agriculture) and [iran-vertical-agriculture](https://github.com/dylanstechmann/iran-vertical-agriculture) repositories are personal hobby and learning projects linked only as contrasting local explorations. No wording, data, code or design is imported from any of them, and no site-specific validation or endorsement is implied.
