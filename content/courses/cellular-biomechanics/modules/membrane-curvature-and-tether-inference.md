# Membrane curvature and tether inference

The aspiration lesson uses a liquid-drop cortical-tension model. A membrane sheet with bending energy answers a different mechanical question. This original foundation minimizes the effective energy of a long cylindrical tube under stipulated tension, then asks which parameters force and radius can identify. All values are invented teaching inputs; no measured membrane, cortex or cell type is represented.

## Specify the selected sheet model

Use bending density (kappa/2)(2H)² with positive bending rigidity kappa and zero spontaneous curvature. Add a positive tension term sigma per area for the declared reservoir condition. This selected model has no in-plane static shear term, explicit cortex, pressure work, viscosity or active stress. End caps and finite-reservoir effects are omitted.

For a long cylinder of radius r and length L, its principal curvatures are 1/r and zero, so 2H=1/r and lateral area is 2pi rL. Its effective energy per length is

$$\mathcal E(r)=E/L=\pi\kappa/r+2\pi\sigma r.$$

Take kappa in pN nm,sigma in pN/nm and r in nm. Both terms in E/L have force units pN. Bending rigidity is an energy, whereas tension is force per length. A cortical-tension estimate and a bulk modulus cannot be substituted for either without a model connecting them.

## Minimize at the stated reservoir condition

Differentiate with respect to radius: d(E/L)/dr=−pi kappa/r²+2pi sigma. At fixed positive kappa and sigma the stationary radius is

$$r_* =\sqrt{\kappa/(2\sigma)}.$$

The second derivative 2pi kappa/r³ is positive. The energy rises at both very small and very large radius under these assumptions, so this stationary point is the minimum of the stated positive-radius problem. If sigma tends to zero, the finite optimum disappears toward large radius; a finite area or volume constraint would need its own energy and admissibility conditions.

With radius at that minimum and coefficients fixed, the extension force is the derivative with respect to length:

$$F=\mathcal E(r_*)=2\pi\sqrt{2\kappa\sigma}=4\pi\sigma r_*.$$

The bending and tension contributions to E/L are equal at the optimum. This is an equilibrium derivative of the selected effective energy, not a prediction for transient pulling through a viscous cortex or a finite closed cell.

## Worked radius and force

Choose kappa=80 pN nm and sigma=0.01 pN/nm. The optimal radius is sqrt4000, about 63.245553 nm, and force is 2pi sqrt1.6, about 7.9476706 pN. Doubling a length under the same fixed-radius/reservoir model doubles its energy but leaves this force unchanged; a limited membrane reservoir could violate that premise.

For a distinct rehearsal choose kappa=72 and sigma=0.02 in the same units. Radius is sqrt1800, about 42.426407 nm, and force about 10.662919 pN. Keep sufficient precision in intermediate square roots before reporting the selected three-significant-figure responses.

## Joint observations identify more than one force

From force alone, F²/(8pi²)=kappa sigma identifies a product. Many positive parameter pairs give the same force while predicting different radii. If an independent radius is supplied and the model applies, the inverse relations are

$$\sigma=F/(4\pi r),\qquad\kappa=Fr/(2\pi).$$

For a separate synthetic observation F=12pi pN and r=30 nm, these give sigma=0.1 pN/nm and kappa=180 pN nm. If thermal energy is stipulated as four pN nm, kappa is 45 thermal-energy units. At this optimum both bending and tension energy-per-length terms equal 6pi pN, summing to the supplied force.

At fixed kappa, multiplying tension by four halves the radius and doubles the force. That scaling checks the formulas independently. It does not demonstrate that a real perturbation changes only tension; changes in bending rigidity, cortex coupling or reservoir access could alter the interpretation.

## Evidence and classical credit

Retain the selected energy, boundary/reservoir conditions, units, minimization, force derivative and inverse residuals. Compare inferred parameters by predicting both force and radius again. A precise force with an unmeasured radius cannot uniquely determine two parameters. A consistent inversion establishes conditional arithmetic rather than membrane identity or empirical model validity.

[MIT OCW 20.310J Spring 2015 calendar](https://ocw.mit.edu/courses/20-310j-molecular-cellular-and-tissue-biomechanics-spring-2015/pages/calendar/) lecture 20 supplies link-only membrane stretch/bending/tension scope. Classical bibliographic credit: W. Helfrich, *Elastic properties of lipid bilayers: theory and possible experiments* (1973), [PMID 4273690](https://pubmed.ncbi.nlm.nih.gov/4273690/), DOI 10.1515/znc-1973-11-1209. The bibliographic record was verified; full paper text was not examined. The selected energy and original calculations above are stated self-contained, with no imported source text, figure, problem or dataset. Full membrane/cortex theory, experimental validity, workload and qualified review remain open; the course stays partial and unreviewed.
