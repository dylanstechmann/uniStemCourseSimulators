# Homework 2 review candidate — protein stability, binding and purification

**State: inactive answer-free review candidate.** This seven-case, 70-point draft covers proposed weeks 3–4. It is not scheduled, assigned, submitted, graded, or listed in the course assessment policy. An unreviewed private key/grader draft is held outside the public package; tolerances, deadlines, attempt rules and workload have not been reviewed or approved. The point allocation is a blueprint proposal, not a course grade.

## Preparation and purpose

**Numeric response convention:** report three significant figures. Use the unit shown on each response field; enter a bare number for dimensionless results. These drafts have no assigned workload or approved grade policy.

Use the lessons on two-state folding, denaturant dependence, ligand binding, cooperativity and quantitative protein purification. The CSV is a fictional, internally stipulated dataset created for practice. Its folding parameters are independent inputs and must not be inferred from net charge. For two-state folding use the relation supplied in the course reading; use the listed temperature and gas constant. The binding case distinguishes free ligand from total ligand and asks when depletion matters. The purification table reports amounts and assay activities for fictional fractions; activity recovery and specific-activity enrichment do not by themselves prove homogeneity.

## Data dictionary

| Column | Meaning |
|---|---|
| `case_id` | Candidate case that uses the row |
| `variable` | Name of a stipulated model input or fraction measurement |
| `value` | Synthetic numeric or categorical value |
| `unit` | Stated scale; `none` means dimensionless |
| `notes` | Context and limits supplied for the exercise |

Use the listed pH, denaturant concentration and temperature only for the stated two-state model. The free-ligand binding case gives a free ligand concentration; the depletion case gives total receptor and ligand concentrations and a dissociation constant. For purification, calculate total activity and total protein from the fraction volumes and concentrations before comparing fractions. State the denominator used for recovery and the basis used for fold enrichment. Method choice should use the supplied property (charge, size, or selective binding) and should name a limitation rather than claiming a single step proves purity.

## Candidate cases

1. Convert a supplied unfolding free energy into an equilibrium constant and folded fraction under the stipulated two-state model.
2. Use the linear denaturant relation to compare stability at the listed concentration and find the model's denaturation midpoint.
3. Compare two fictional constructs under a stated perturbation and explain why marginal stability can affect proteostasis without assigning a real biological effect.
4. Calculate occupancy from a dissociation constant and free ligand, then compare with a total-concentration case using the exact ligand-depletion model.
5. Interpret the supplied Hill parameters and compare predicted unloading over the stated ligand range without equating a Hill coefficient with a binding-site count.
6. Use the fraction data to compute total protein, total activity, recovery and specific-activity enrichment with denominators stated.
7. Select a separation step with an orthogonal property after the supplied first step and state what enrichment evidence cannot establish.

## Limits and review needed

This is an assessment blueprint, not a validated graded assignment. Independent recalculation, scientific and assessment review, accessibility/fairness review, workload measurement, protected key/grader authoring and mutation tests, candidate-specific protected-delivery verification, and an operator release/retake decision remain required. Keep the candidate inactive and outside the course manifest until those gates are resolved.

## Provenance

Original answer-free authoring with synthetic model inputs. CC BY 4.0. No real protein, assay, clinical measurement, or third-party assessment is represented; no independent or qualified review is claimed.
