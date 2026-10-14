# Kinetics and reaction mechanisms

## Learning objectives

After this reading, you should be able to:

1. Infer reaction order from controlled rate data and explain why a balanced overall equation usually does not determine the rate law.
2. Relate a rate constant to temperature with the Arrhenius model, using kelvin and consistent energy units.

## What a reaction rate measures

Chemical kinetics describes how quickly composition changes and how that change depends on conditions. For a dissolved reactant A, its concentration usually falls with time, so its disappearance rate is written with a minus sign: rate of disappearance = −Δ[A]/Δt. A product concentration usually rises, so its formation rate is +Δ[P]/Δt. These average rates use a finite time interval; the instantaneous rate is the limiting slope at one moment on a concentration-versus-time curve. Concentration rate commonly has units mol L⁻¹ s⁻¹, although the time unit can be minutes or another stated unit.

For the overall reaction aA + bB → cC, the stoichiometrically normalized reaction rate is −(1/a)Δ[A]/Δt = −(1/b)Δ[B]/Δt = (1/c)Δ[C]/Δt. The coefficients connect rates of change of different species. They do not, by themselves, provide the powers in the kinetic rate law. This distinction matters whenever a question gives the rate of one species but asks for the reaction rate or a different species' rate.

## The experimental rate law

At fixed temperature and other controlled conditions, many reactions can be described over a specified range by a rate law such as rate = k[A]ᵐ[B]ⁿ. The exponents m and n are reaction orders with respect to A and B; their sum is the overall order for this rate law. The constant k is the rate constant at the stated temperature and medium. The rate law is an empirical model: experiments determine whether it applies and what its exponents are. The equation is not a universal law for every concentration range or mechanism.

Initial-rate comparisons provide one way to infer orders while minimizing the complication that concentrations drift during a run. Suppose a synthetic data set gives these initial observations:

| Trial | [A] (M) | [B] (M) | Initial rate (M s⁻¹) |
|---|---:|---:|---:|
| 1 | 0.10 | 0.10 | 0.0020 |
| 2 | 0.20 | 0.10 | 0.0040 |
| 3 | 0.10 | 0.20 | 0.0080 |

Comparing trials 1 and 2 doubles [A] while holding [B] fixed and doubles the rate, so this data set is first order in A. Comparing trials 1 and 3 doubles [B] while holding [A] fixed and quadruples the rate, so it is second order in B. The resulting model is rate = k[A][B]², third order overall. Using trial 1, k = (0.0020 M s⁻¹)/((0.10 M)(0.10 M)²) = 2.0 M⁻² s⁻¹. Its units follow from the requirement that the rate law produce concentration per time. A first-order rate constant has units of inverse time, while a second-order rate constant commonly has units M⁻¹ time⁻¹.

When more than one concentration changes between two trials, a simple rate ratio does not isolate one exponent. Choose pairs that hold all but one reactant constant, or solve the simultaneous ratio equations explicitly. Repeat measurements and uncertainty matter: small noisy differences should not be treated as exact powers. A fitted order describes the observed behavior under tested conditions; it is not necessarily a molecular count or a whole-number exponent.

## Connecting rate and temperature

For many reactions over a limited temperature interval, the Arrhenius model relates the rate constant to absolute temperature: k = A exp(−Eₐ/RT). Here Eₐ is an activation energy, R is the gas constant, T is in kelvin, and A is a model parameter called the pre-exponential factor. The exponential term summarizes the strong effect of the energy barrier on the fraction of suitably energetic molecular encounters. This model is useful but approximate; its parameters or dominant pathway can change outside the studied range.

Comparing two temperatures cancels A when it is treated as constant:

ln(k₂/k₁) = (Eₐ/R)(1/T₁ − 1/T₂).

The temperatures must be kelvin, and Eₐ and R must use matching energy units. For a synthetic reaction with Eₐ = 50.0 kJ mol⁻¹, compare 298 K and 308 K. Convert Eₐ to 50,000 J mol⁻¹ to match R = 8.314 J mol⁻¹ K⁻¹. Then ln(k₃₀₈/k₂₉₈) = (50,000/8.314)(1/298 − 1/308) ≈ 0.655, so k₃₀₈/k₂₉₈ ≈ e⁰·⁶⁵⁵ ≈ 1.93. Under this model, the rate constant at 308 K is about 1.93 times the rate constant at 298 K. This is a ratio, not an absolute rate, and an actual measured rate also depends on reactant concentrations and the applicable rate law.

The formula also predicts a larger k at the higher temperature for a positive Eₐ. A ratio below one in this comparison usually signals swapped temperatures, an incorrect sign, or a kelvin/unit error. Celsius values cannot be substituted directly into the reciprocal-temperature expression.

## Mechanisms: possible steps behind an overall equation

A reaction mechanism is a proposed sequence of elementary steps whose sum gives the observed overall reaction. A species formed in one step and consumed in another is an intermediate; it cancels when the steps are added and should not remain in the net equation. The balanced overall equation records net stoichiometry, but usually does not say which collisions occur in each elementary step or in what order.

The distinction explains an important exception about rate-law powers. For a single elementary step, its molecular event gives a rate expression in terms of the reactants in that step. For example, if the elementary event A + B → products is the rate-controlling event, a rate proportional to [A][B] can be plausible for that step. But a multistep reaction’s experimentally observed rate law cannot in general be read from the coefficients of its overall equation. A slow step may be preceded by a rapid equilibrium, followed by another step, or involve an intermediate whose concentration must be related to measurable reactants. A proposed mechanism must be consistent with both the net stoichiometry and observed kinetic evidence; matching one rate law alone rarely proves a unique pathway.

The phrase rate-determining step is a useful introductory shorthand for a step that constrains the observed rate. It is not a license to ignore faster preceding equilibria or to assume every mechanism consists of one slow and several irrelevant fast steps. Mechanism analysis often requires combining stepwise kinetics with conservation, equilibrium relations, or experimental tests. The dedicated rate-law and mechanism lesson later in this course develops those derivations in more depth.

## Collision theory and catalysts

Collision theory gives a molecular picture for why a reaction has an activation barrier: reacting particles must encounter one another in a suitable arrangement and with sufficient energy to reach a reactive configuration. Raising temperature increases the fraction of encounters with enough energy for many activated processes, which helps explain the Arrhenius trend. Orientation, solvent, and other environmental details can also affect the measured rate, so collision theory is a model rather than a complete description of every solution reaction.

A catalyst provides a pathway with a lower activation barrier and can therefore increase rates in both directions of a reversible reaction. It is regenerated overall and does not change the net reaction or the equilibrium constant at a given temperature. Enzymes are catalysts: in a biochemical setting, binding and local molecular interactions help organize a reaction path, but a simple classroom rate model does not capture every feature of an enzyme. Catalysis affects how quickly a system approaches equilibrium, not which equilibrium composition is favored.

## A limited first-order half-life check

For a first-order disappearance process, the integrated relation is ln([A]ₜ/[A]₀) = −kt, and the half-life is t₁/₂ = ln 2/k. If k = 0.35 min⁻¹, then t₁/₂ = 0.693/(0.35 min⁻¹) = 1.98 min. The inverse-time units cancel to leave time. This relation applies when the process is first order under the stated conditions; it is not a general half-life formula for every reaction. Week 6 compares integrated forms and their concentration-time signatures in more detail.

## Common reasoning checks

- Determine orders from controlled experimental comparisons, not by copying coefficients from the net equation.
- State what is held constant when using initial-rate ratios; use units and confirm the inferred k reproduces a measured rate.
- Use kelvin in Arrhenius calculations, convert activation energy to match R, and check that a positive activation energy predicts a larger rate constant at higher temperature.
- Keep rate constant, rate, and reaction progress distinct. The rate constant has units and depends on temperature; the rate also depends on concentrations and the rate law.
- Treat a mechanism as a testable model. Balanced steps and agreement with a measured rate law are necessary checks, but neither alone guarantees a unique mechanism.

## Further study

These link-only textbook sections provide additional background: [Chemical Reaction Rates](https://openstax.org/books/chemistry-2e/pages/12-1-chemical-reaction-rates), [Rate Laws](https://openstax.org/books/chemistry-2e/pages/12-3-rate-laws), [Integrated Rate Laws](https://openstax.org/books/chemistry-2e/pages/12-4-integrated-rate-laws), [Collision Theory](https://openstax.org/books/chemistry-2e/pages/12-5-collision-theory), and [Reaction Mechanisms](https://openstax.org/books/chemistry-2e/pages/12-6-reaction-mechanisms). This lesson is original instruction; no source prose, figures, examples, problem wording, or datasets are reproduced.
