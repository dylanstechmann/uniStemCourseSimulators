# Drawings, BOM revision, risk and release-evidence governance

**Status:** Original reading in partial Materials Engineering for Fabrication 0.1.0; unreviewed and formative-only. All dossiers, roles, suppliers and records are fictional and synthetic. Fabrication readiness is the review objective, never an achieved claim. This lesson supplies no standard-specific compliance checklist, supplier approval or production release.

## Learning objectives

1. Audit drawing/BOM revisions and the evidence chain from risk to first article and change control.
2. Distinguish evidence completeness from real production readiness and authorized human release.
3. Assign only synthetic_review_complete or evidence_gaps_remain dispositions, with missing evidence causing a hold.

## The definition must be controlled

A drawing package identifies geometry, material and requirement definitions; a bill of materials identifies the intended constituent items and revisions. They must agree. A drawing revision change without corresponding BOM, process-plan, inspection and risk review creates an evidence gap even if the affected geometry appears minor. Supplier and lot records must point to the same controlled definition. An old certificate cannot automatically support a revised material or process.

Revision control is not a filename convention alone. The review needs revision identifiers, change reason, affected requirements, impacted analyses and inspections, approvals required by the actual organization, and disposition of existing inventory or work in progress. This course does not define an organization’s release procedure. It teaches reviewers to detect missing links and avoid assuming that an unsigned electronic record is authorized.

## Risk analysis and control plans

Risk analysis connects hazards or failure modes to causes, effects and planned controls. Severity, occurrence and detection rankings in a synthetic ordinal matrix can support prioritization, but their product is not a probability. Public practice calculates 8×4×5 = 160 as an ordinal risk-priority product. It must not be interpreted as a 160% risk or compared universally across unrelated scoring systems. High severity can require attention regardless of the product, and detection scores are only as credible as the inspection evidence.

A control plan translates selected risks and requirements into characteristics, evidence methods, record ownership, reaction expectations and references to the controlled definition. It is not a machine setup sheet in this course. Inspection frequency or acceptance criteria for a real process require qualified review and applicable requirements. The control plan must align with the drawing/BOM and process route and must change when those inputs change.

## Supplier-lot and first-article evidence

Supplier-lot evidence establishes identity and relevant properties for a defined input lot. Review the certificate’s material identity, lot link, revision, property context and relationship to actual received material. A visually plausible document with no lot linkage is incomplete. Process qualification asks whether the actual route produces acceptable results under its qualified boundary; evidence from another material, geometry or route cannot simply be borrowed.

First-article evidence compares the produced item and its records with the controlled definition. Coverage matters: 18 verified characteristics among 24 gives 75% in a synthetic coverage calculation, but the six unverified characteristics remain open. An average or percentage cannot erase a missing critical characteristic. Calibration and measurement-system analysis must support the inspection results, and any nonconformance needs documented disposition and closure rather than deletion from the report.

## Nonconformance and change control

Nonconformance records identify the requirement, observed condition, affected items/lots, containment, evaluation and authorized disposition. Closure requires evidence that the required action was completed and verified. If 12 items were opened and six have verified closure, verified closure is 50%; items merely marked “closed” without verification do not belong in the numerator. Open items affecting the reviewed evidence require a hold.

Change control asks what changed, why, which requirements and evidence are affected, and whether prior qualification remains valid. A supplier substitution, revised adhesive, altered fiber orientation or new inspection method can invalidate earlier comparisons. Missing change review remains unknown, not “no change.” Traceability must connect old and new records without rewriting history.

## Authorized roles and bounded dispositions

Real fabrication readiness requires approved drawings/BOM, qualified engineering and safety review, material and process qualification, calibrated inspection/MSA, lot traceability, nonconformance closure and a named authorized human release role. A learner, automated checklist or AI agent cannot supply that authority. The course therefore uses only two dispositions. `synthetic_review_complete` means every declared fictional teaching gate has evidence and the arithmetic review is complete; it still grants no production approval. `evidence_gaps_remain` means at least one required item is missing, open, unstable or unauthorized and the synthetic review stays on hold.

The word “complete” is deliberately qualified by “synthetic” and “review.” It never means the component is complete, qualified or ready. When in doubt, choose `evidence_gaps_remain` and name the exact missing record and responsible real-world role. Do not invent a third status such as production_approved.

## Common mistakes

Do not treat a high first-article coverage percentage as full verification, accept an unlinked supplier certificate, close nonconformance by hiding a row, or multiply ordinal risk ranks into a probability. Do not let a process change bypass drawing/BOM and risk review. Most importantly, do not convert a complete synthetic checklist into supplier approval, fabrication readiness or production release.

## Scope and application links

MIT 2.008 and 2.830J provide broader design-review, manufacturing-system and process-control comparators; NIST/SEMATECH supplies monitoring methods links. The owner’s [open-construction-equipment](https://github.com/dylanstechmann/open-construction-equipment), [machine-cad-agent](https://github.com/dylanstechmann/machine-cad-agent) and [diaper-changing-machines](https://github.com/dylanstechmann/diaper-changing-machines) repositories are personal hobby and learning projects linked only for discussion of evidence gaps around digital concepts. No code, CAD, BOM, drawing, parameter or validation claim is imported. Owner review and fabrication readiness are not implied.
