# Assignment 4: process evidence and factorial interpretation

This open capstone joins the existing factorial/scale-down readings with the new balance, observation and local-exposure work. It asks what an endpoint table can show and which mechanistic claims require other evidence. The table is constructed synthetic arithmetic, not observed culture data. All factor levels are abstract coded conditions; no process recipe or real intervention is specified. Keep your analysis, code and report locally. Browser checkpoints assess selected arithmetic only.

## Table and experimental-unit ledger

The [synthetic factorial run CSV](../assignments/process-evidence-factorial.csv) contains eight distinct fictional vessel-run identifiers, two factor codes $A,B\in\{-1,+1\}$ and one normalized endpoint per run. There are two constructed rows per factor combination. A denotes an abstract exchange-condition contrast and B an abstract retention-condition contrast. Their codes do not prescribe an exchange rate, separator, cell line or other real setting.

Read the table and verify its schema, unique identifiers, complete combinations and numeric values. The constructed cell means are 12 for $(A,B)=(-1,-1)$, 10 for $(+1,-1)$, 4 for $(-1,+1)$ and 14 for $(+1,+1)$. Each pair of responses differs from its mean by plus or minus 0.5. These deterministic offsets provide residual arithmetic; they are not a measured estimate of biological or instrument variation.

State the analysis unit and explain why repeated measurements of one vessel would not create additional independently assigned vessel runs. If you propose randomization or blocking, label it as a future hypothetical design rather than reporting that those actions occurred. The table by itself supplies no actual assignment log or provenance for a physical experiment.

## Part A: derive effects and coefficients

Fit the full two-factor model $y=\beta_0+\beta_A A+\beta_B B+\beta_{AB}AB+e$ with the stated ±1 coding. Derive the design matrix and solve its normal equations or use an orthogonal contrast. The grand mean is 10, with coefficients $\beta_A=2,\beta_B=-1,\beta_{AB}=3$.

Under the course's high-minus-low effect convention, the effects are twice those coefficients: A is four, B is minus two and AB is six. Show the group means or signed contrast used for each value. Changing the coding convention can change coefficient interpretations, so retain the definitions rather than comparing coefficients across incompatible encodings.

Compute the simple A effect separately at each B level. At B=-1 it is $10-12=-2$; at B=+1 it is $14-4=10$. Thus the averaged A effect of four does not describe either simple comparison. The difference of simple effects is twelve, twice the AB effect under this convention. Explain why an interaction cannot be summarized as one factor always improving the endpoint.

## Part B: residual arithmetic and its limits

The eight squared residuals sum to two. Four fitted coefficients leave residual degrees of freedom $8-4=4$, giving mean squared error 0.5. Verify these results from the raw rows, not only from the listed cell means. Reconstruct fitted values and residuals and check orthogonality to each design column.

If an independent equal-variance error model were justified, an effect's standard-error formula would give $\sqrt{4\,MSE/8}=0.5$ here. That is conditional arithmetic, not evidence that the deterministic table has random Gaussian biological errors. Do not attach real-process confidence or significance claims to constructed offsets. A separate simulation with an explicitly declared random-error distribution would answer a different methodological question.

## Part C: distinguish endpoint patterns from mechanisms

Use the preceding reports to construct at least two plausible explanations for a changed endpoint that the factorial table alone cannot separate. Possibilities include a real local-state change, altered observation dynamics, changed viable loss or a combination of parameters. State the equations behind each hypothetical explanation; factor names alone do not establish their physical effects.

Propose one additional synthetic observation or controlled comparison to distinguish them. A probe-only transient can leave rate labels ambiguous, a bulk concentration can conceal a low local zone, and a steady viable concentration can coexist with large death/export fluxes. Identify the quantity you would need and which confounding terms must be controlled or measured. Do not claim that a proposed investigation was carried out.

## Part D: integrated acceptance report

Prepare an evidence table separating parameter definitions, conservation residuals, admissible model domains, observation mapping, numerical convergence and endpoint inference. Include the positive steady-state ledger from Assignment 1, the swapped-rate comparison from Assignment 2 and the local/total exposure comparison from Assignment 3. Explain which conclusion each check supports and which it leaves unresolved.

Your retained report should distinguish an arithmetic fit, a structural model comparison, a proposed design and actual empirical validation. Selected browser checkpoints do not score this reasoning or approve a process. The [MIT OCW 10.442 Spring 2005 calendar](https://ocw.mit.edu/courses/10-442-biochemical-engineering-spring-2005/pages/calendar/) design/scale-down/animal-cell strands and the existing local statistics/factorial readings provide scope links. All table values, explanations and tasks are original and AI-assisted; no source data or university assessment was imported. Broader bioprocess evidence, measured workload and qualified review remain open; the course is partial and unreviewed.
