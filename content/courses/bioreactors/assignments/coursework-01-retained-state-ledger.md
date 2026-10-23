# Assignment 1: retained viable-state and substrate ledger

This open report connects the existing batch, fed-batch, elemental-yield and continuous-culture readings with the new retention/maintenance foundation. It asks for amount-rate ledgers and model-domain evidence, rather than a single steady concentration. All values are normalized synthetic inputs. They are not operating conditions for any culture, cell line or device. Keep calculations, code and report locally; browser checkpoints assess selected outputs only.

## Part A: reconstruct the process boundary

A constant-volume vessel has total hydraulic dilution rate $D=0.3$. A fraction $b=0.25$ of the total liquid outlet is a bleed carrying viable concentration $X$. The remaining outlet has viable concentration $\epsilon X$, with $\epsilon=0.2$. The feed contains substrate at $S_{in}=2$ and no viable biomass. Use gross production $\mu(S)=0.6S/(0.5+S)$, death coefficient $k_d=0.03$, growth-associated yield $Y_G=0.5$ and maintenance coefficient $m=0.1$.

Draw the outlet split and identify whether each quantity is a volume rate, concentration or amount rate. The bleed belongs within the total hydraulic outlet, so the effective viable loss is $L=D[b+\epsilon(1-b)]=0.12$. Do not remove both this effective loss and another full hydraulic $DX$ term. Explain which idealized limits recover complete retention and an unretained chemostat.

Write the original two differential equations before reducing them. At a positive steady state, gross production must replace death plus viable outlet, so $\mu_*=0.15$. Inverting the stipulated growth law gives $S_*=1/6$. Specific consumption is $q_{S*}=\mu_*/Y_G+m=0.4$, and substrate balance gives $X_*=11/8=1.375$. Verify that the positive branch is supported by the feed and lies inside the declared substrate domain.

## Part B: close separate ledgers

Construct a viable-biomass table with gross production, viable export, death and net accumulation. For the stated steady state, the rates are 0.20625, 0.165, 0.04125 and zero respectively. The first equals the sum of the next two. A stationary viable concentration is therefore compatible with ongoing production, loss and replacement.

Construct a separate substrate table. Net substrate supply is $D(S_{in}-S_*)=0.55$, equal to $q_{S*}X_*$. Split that consumption into growth-associated and maintenance contributions using the stipulated law. Identify the numerator and denominator of every yield ratio: viable export per consumed substrate is 0.3, while gross production per consumed substrate is 0.375, both different from $Y_G=0.5$.

If an optional unretained dead-material state has $Z'=k_dX-DZ$, its steady value is 0.1375. Explain why this simple viable/dead ledger does not establish a full elemental balance. Connect it to the earlier elemental-yield reading: a genuine C/H/O/N closure needs specified species and coefficients, including the products or gas streams missing from these phenomenological state equations. Do not combine a viable-count basis with a mass basis without an explicit conversion.

## Part C: test a model boundary

The constant maintenance law is valid only in its stipulated positive-substrate window. At $S=0$, gross Monod production is zero but the law still consumes $mX$. For a separate boundary check with $X=10$, the substrate derivative is $0.3(2)-0.1(10)=-0.4$. This negative derivative belongs to the exact model, not to an oversized numerical step. Identify the implication for nonnegative-state invariance.

Propose a clearly labeled response: stop the simulation at a declared admissibility event, or introduce and justify a substrate-limited replacement law and rederive its balances. Arbitrarily clipping a negative state to zero after each step changes the equation and destroys the original amount-rate interpretation. If you study the replacement, keep its results separate from the constant-maintenance model's checkpoints.

## Part D: transient and sensitivity evidence

Implement the two original equations near the positive steady state. Form its Jacobian, verify trace and determinant signs, and compare small perturbations with the local linearized solution under step refinement. A local stability result is narrower than global admissibility from all starts. Include one deliberately large starting biomass that approaches the substrate boundary and report the stopping condition.

Change one retention parameter while holding the remaining stated coefficients fixed, then recompute the positive steady state and every ledger. Explain why an actual retention device might also change viability, flow or other coefficients; the controlled mathematical comparison does not identify those real effects. Provide a sensitivity table and preserve the parameter definitions so a reviewer can reproduce it.

## Self-review and scope

The retained report should include the outlet diagram, original equations, admissible branch, two rate ledgers, yield definitions, optional dead-state boundary and numerical evidence. Browser checkpoints do not evaluate the derivation, code or proposed replacement model. The [MIT OCW 10.442 Spring 2005 calendar](https://ocw.mit.edu/courses/10-442-biochemical-engineering-spring-2005/pages/calendar/) growth-model/continuous/animal-cell strands are link-only comparators. Problems, parameters and explanations are original with substantial AI assistance. No source problem, data or process recipe was imported. Qualified review, validated physiological assumptions and measured workload remain open; the course stays partial and unreviewed.
