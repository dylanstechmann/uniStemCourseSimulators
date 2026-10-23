# Chemical potential and reaction equilibrium

Entropy balances set the direction of spontaneous change for a complete system. Chemical potential makes that idea useful for mixtures: it measures how the Gibbs energy changes when the amount of one species changes at fixed temperature and pressure. In this lesson, an ideal dilute mixture and one reversible reaction connect chemical potential, reaction Gibbs energy and equilibrium composition.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate a reaction quotient and reaction Gibbs energy from stated activities.
2. Relate the standard reaction Gibbs energy to an equilibrium constant and solve a one-reaction equilibrium composition.
3. Distinguish equilibrium conditions from reaction rates and identify assumptions in the ideal-mixture calculation.

## Chemical potential is a thermodynamic driving force

For species \(i\), the chemical potential is the change in Gibbs energy when an infinitesimal amount of that species is added at fixed temperature, pressure and amounts of the other species:

\[
  \mu_i=\left(\frac{\partial G}{\partial n_i}\right)_{T,P,n_{j\ne i}}.
\]

In an ideal mixture, its dependence on composition is written

\[
  \mu_i=\mu_i^\circ+RT\ln a_i,
\]

where \(a_i\) is dimensionless activity, \(R\) is the gas constant, and \(T\) is absolute temperature. For an ideal dilute solute, \(a_i\approx c_i/c^\circ\), with the standard concentration \(c^\circ\) stated explicitly. Chemical potential differences drive redistribution: in the ideal dilute approximation, changing an activity by a factor \(r\) changes the corresponding composition term by \(RT\ln r\). Charged species also require electrical potential in their electrochemical potential; that extension is outside this example.

## Reaction Gibbs energy and equilibrium

For a reaction \(\sum_i\nu_i A_i=0\), with products assigned positive stoichiometric coefficients and reactants negative ones, the reaction Gibbs energy is

\[
  \Delta_rG=\sum_i\nu_i\mu_i=\Delta_rG^\circ+RT\ln Q,
  \qquad Q=\prod_i a_i^{\nu_i}.
\]

At fixed temperature and pressure, the forward reaction lowers Gibbs energy when \(\Delta_rG<0\), and the reverse direction lowers it when \(\Delta_rG>0\). At equilibrium, \(\Delta_rG=0\) and \(Q=K\), so

\[
  \Delta_rG^\circ=-RT\ln K.
\]

The equilibrium constant describes a composition ratio at equilibrium. It is not a rate constant and does not say how quickly equilibrium is approached.

## Worked example: \(A\rightleftharpoons B\)

At \(T=298\,\mathrm K\), suppose the ideal-mixture equilibrium constant is \(K=4.00\), using dimensionless activities referenced to \(c^\circ=1.00\,\mathrm{mM}\). With \(R=8.314\,\mathrm{J\,mol^{-1}\,K^{-1}}\),

\[
  \Delta_rG^\circ=-RT\ln4=-3.43\,\mathrm{kJ\,mol^{-1}}.
\]

For a current mixture with \([A]=1.00\,\mathrm{mM}\) and \([B]=0.20\,\mathrm{mM}\), the quotient is \(Q=a_B/a_A=0.20\). Thus

\[
  \Delta_rG=RT\ln(Q/K)=RT\ln(0.20/4.00)=-7.43\,\mathrm{kJ\,mol^{-1}}.
\]

The forward direction lowers Gibbs energy for this stipulated mixture. The value does not give a reaction rate.

If the closed batch contains only \(A\) and \(B\), their total concentration remains \(1.20\,\mathrm{mM}\). At equilibrium \([B]/[A]=K=4\); therefore \([A]=1.20/(1+4)=0.24\,\mathrm{mM}\) and \([B]=0.96\,\mathrm{mM}\). The ratio is dimensionless because both concentrations use the same stated standard.

## Assumptions and limits

- The example uses one reversible reaction, a fixed temperature, a closed batch and ideal dilute activities.
- It assumes no side reactions, binding, changing volume or species-specific activity corrections.
- A real bioengineering system can be open to matter flow, electrically coupled, nonideal or far from equilibrium. The one-reaction calculation does not replace a full balance or kinetic model.
- At equilibrium there is no net thermodynamic driving force for the reaction, though forward and reverse molecular events can continue.
- All values are synthetic teaching examples; they do not predict a real material, tissue, process or reaction rate.

MIT OCW 20.110J places equilibrium/free energy, chemical potential and chemical equilibrium in its undergraduate sequence. This local reading develops a single ideal \(A\rightleftharpoons B\) calculation; the later phase/activity and electrochemical-coupling readings extend the selected examples, while a general thermodynamic treatment remains beyond this combined course.
