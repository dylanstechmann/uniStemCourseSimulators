# Conceptual load paths, work breakdown and construction dependencies

**Status:** Original lesson in partial version 0.1.0; unreviewed and formative-only. All structures and schedules are synthetic teaching abstractions, not real construction instructions or engineering approvals.

## Learning objectives

1. Trace a conceptual load from demand through structural members and supports to a foundation boundary without sizing real components.
2. Build a work breakdown and finish-to-start dependency network, calculating earliest completion from parallel and serial activities.
3. Place qualified design review, permits, inspection and change-control gates where a paper plan cannot authorize physical work.

## Follow the load to the boundary

A load path is a causal-structural account of how demand is transferred through a system. Start with the imposed demand, identify the element receiving it, follow transfer through members and connections into supports, and finish at the foundation and ground boundary. At each step record the idealization: direction, sharing assumption, restraint, load combinations that are absent and evidence still needed.

A sketch does not demonstrate capacity. It can omit stability, connection behaviour, material variability, deterioration, construction tolerances, ground conditions and lateral demands. Those omissions must remain visible rather than being hidden by a clean diagram. Site-specific analysis and qualified engineering are required before any real structure is designed or changed.

**Synthetic equilibrium example.** A conceptual 12 kN vertical load is carried by two identical idealized supports that are explicitly assumed to share equally. Each vertical reaction is 12/2 = **6 kN**. This arithmetic follows from the assumption and equilibrium. It does not establish member strength, foundation capacity, stability or suitability for construction.

The agricultural context adds dependencies rather than a ready-made structure. Tanks, lighting, equipment access and plant zones may create different demands and maintenance routes. The lesson asks whether those demands have a traceable conceptual path and a review owner; it does not specify components or physical steps.

## Work breakdown before schedule arithmetic

A work breakdown structure (**WBS**) decomposes the intended deliverable into reviewable pieces. Each work item needs a unique identifier, a clear output and an owner. A WBS is not merely a list of disciplines: “electrical” is too vague, while “document the lighting-energy evidence package” has an inspectable result. Work items can cover design evidence, procurement records, review documents and commissioning evidence without becoming instructions to perform physical work.

Dependencies state what must be complete before another activity can begin. In a finish-to-start relation, the successor begins only after the predecessor finishes. Parallel activities can overlap when their inputs and resources allow it. A human review can be a predecessor: if approval is required, treating it as a comment at the end makes the schedule logically false.

**Synthetic schedule example A.** Activities A and B take 3 and 4 days and can run in parallel. Review C takes 2 days and requires both. Earliest completion is max(3, 4) + 2 = **6 days**, not 3 + 4 + 2 = 9 and not 3 + 2 = 5.

**Synthetic schedule example B.** One path has durations 2 + 5 + 3 = **10 days** and another has 2 + 4 + 3 = 9 days. The controlling longest path is **10 days**. This is a deterministic teaching network, not a probabilistic completion forecast. Resource conflicts, uncertainty and review revisions require separate treatment.

## Human gates and change control

Human gates belong in the work logic, not as decorative disclaimers. A gate names the decision, responsible person or body, evidence needed and consequence of remaining unresolved. Design review, local permissions, inspection and acceptance can all be gates. The course does not assign those roles to the learner or claim that a checklist discharges them.

Change control is equally important. If a support concept changes, its load path, work items, predecessors and required reviews may change. Record the revision and re-evaluate affected evidence. An earlier review cannot silently cover a different concept. Scheduling software can detect dates, but it cannot approve structural adequacy, safety or permission.

## Common mistakes

- Stopping a load-path sketch at a convenient member instead of the foundation boundary.
- Treating equal-sharing arithmetic as a capacity or construction design.
- Adding parallel durations, or letting a successor start before all required predecessors finish.
- Omitting reviews from the dependency network and then calling the resulting date achievable.
- Allowing software or an owner repository to substitute for qualified, site-specific decisions.

## Scope and sources

This lesson covers conceptual mechanics and project logic only. It excludes physical procedures, member sizing, detailed estimating, contracting, probabilistic scheduling and site validation. [MIT OCW 1.040 Project Management, Spring 2004](https://ocw.mit.edu/courses/1-040-project-management-spring-2004/pages/syllabus/) is a link-only comparator for organization, WBS, planning, monitoring, control and learning; its broader course is not reproduced. The existing [MIT OCW 8.01SC Classical Mechanics](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/) registry record identifies the recommended mechanics foundation. The owner's [open-construction-equipment](https://github.com/dylanstechmann/open-construction-equipment) repository is a personal hobby and learning project linked only for systems context; its code, models, drawings, parameters and validation claims are neither imported nor endorsed.
