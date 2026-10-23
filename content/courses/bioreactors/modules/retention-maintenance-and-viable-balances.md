# Retention, maintenance and viable-state balances

The continuous-culture reading derives a constant-yield chemostat without death or maintenance. Retaining cells changes the loss term, but does not abolish every possible loss of viable biomass. This original extension separates hydraulic dilution, leakage, bleed, death and non-growth-associated substrate demand. All rates and concentrations below are invented normalized quantities. They are not specifications for a cell line or culture operation.

## Declare each boundary before writing concentrations

Let a constant-volume, well-mixed vessel receive cell-free feed at hydraulic dilution rate $D$. A fraction $b$ of its total liquid outlet is a bleed carrying viable concentration $X$. The remaining fraction passes a separator whose outlet contains $\epsilon X$. Here $0\leq b,\epsilon\leq1$; the two outlet fractions sum to one. The effective viable-cell loss coefficient is

$$L=D[b+\epsilon(1-b)].$$

This definition counts the bleed within the total liquid flow. Adding a second full $DX$ removal term would count part of the outlet twice. Perfect retention with no bleed has $b=\epsilon=0$ and $L=0$; an ordinary unretained outlet has $b=1$ and $L=D$. Concentration and total amount agree up to fixed volume in this model, but that shortcut cannot be carried unchanged into the separate fed-batch reading with changing volume.

Use a gross viable-biomass production coefficient $\mu(S)=\mu_{\max}S/(K_S+S)$ and a viable-death coefficient $k_d$. Stipulate specific substrate consumption

$$q_S=\mu/Y_G+m,$$

where $Y_G$ is a growth-associated yield coefficient and $m$ is a non-growth-associated consumption coefficient. This is a phenomenological teaching law, not a calibrated or universal description of cell maintenance. All terms must use a consistent viable-biomass and substrate basis. The balances are

$$X'=(\mu-k_d-L)X,\qquad S'=D(S_{in}-S)-(\mu/Y_G+m)X.$$

Death removes viability; it does not make the material disappear. For an optional explicitly unretained dead-material state $Z$, with no lysis or recycling in the modeled window, add $Z'=k_dX-DZ$. This is a viable/dead inventory, not a complete elemental reaction network. Substrate material not assigned to viable growth is outside that simplified state ledger; do not claim a full atom balance without supplying the missing product and gas states.

## Derive a positive steady state

If $X_*>0$, then $\mu_*=k_d+L=g$. Inverting the stipulated Monod relation gives

$$S_* = \frac{K_Sg}{\mu_{\max}-g},\qquad X_* = \frac{D(S_{in}-S_*)}{g/Y_G+m}.$$

Require $g<\mu(S_{in})$, positive denominator and nonnegative states. A formal algebraic root with $S_*>S_{in}$ and negative $X_*$ is inadmissible. The washout state is $X=0,S=S_{in}$; its viable growth eigenvalue is $\mu(S_{in})-k_d-L$. Retention changes this comparison through $L$, while hydraulic replacement still appears separately in the substrate balance.

In the selected model, linearization at a positive steady state has matrix

$$J=\begin{pmatrix}0&\mu'X_*\\-q_{S*}&-D-\mu'X_*/Y_G\end{pmatrix}.$$

For positive $D,q_{S*},X_*,\mu'$ its trace is negative and determinant is positive, establishing local asymptotic stability for this two-state fixed-parameter system. It does not establish stability of a delayed controller, a changing retention device or an inhibited growth law.

## A model boundary is not a numerical tolerance

The constant maintenance term cannot be extended to arbitrary nutrient depletion. At S=0, the substrate derivative is D Sin−mX; sufficiently large X makes it negative even in the exact differential equation. For example, the rehearsal coefficients with X=20 give 0.25×2−0.05×20=−0.5. This is a model-domain failure, not an Euler artifact. Restrict the constant-maintenance law to its declared positive-substrate window, stop a study at its admissibility boundary, or supply and justify a substrate-limited replacement law. Clipping a negative state after every numerical step silently changes the balances. Local stability of the positive steady state does not prove global nonnegative invariance of this simplified law.

## Worked retained-state ledger

Choose $D=0.2,b=0.1,\epsilon=0.05,k_d=0.011,\mu_{\max}=0.2,K_S=1,S_{in}=5,Y_G=0.5,m=0.02$. The outlet fraction is $0.1+0.05(0.9)=0.145$, so $L=0.029$ and $g=0.04$. Then $S_*=0.25$, $q_{S*}=0.1$ and $X_*=9.5$.

Gross viable production is $0.04(9.5)=0.38$, split into viable outlet $0.029(9.5)=0.2755$ and death $0.011(9.5)=0.1045$. Substrate supply/use is $0.2(5-0.25)=0.95=0.1(9.5)$. If the optional dead state is included, $Z_*=0.1045/0.2=0.5225$. Every amount rate is on its declared basis; the numerical values have no direct human-cell interpretation.

## Distinct rehearsal and yield interpretation

Use $D=0.25,b=0.2,\epsilon=0.1,k_d=0.03,\mu_{\max}=0.5,K_S=0.4,S_{in}=2,Y_G=0.4,m=0.05$. Now the outlet fraction is 0.28, $L=0.07$, $g=0.1$, $S_*=0.1$, $q_{S*}=0.3$ and $X_*=19/12$. Gross production is $19/120$, viable outlet $133/1200$, death $19/400$, and substrate supply/use 0.475. The optional dead state is 0.19.

The ratio of viable exported biomass to consumed substrate is $L/q_{S*}=7/30$, different from both the gross-production ratio $g/q_{S*}=1/3$ and the stipulated growth-associated coefficient $Y_G=0.4$. Which yield is meant depends on the numerator and boundary. A steady viable concentration does not mean no growth, no death or no substrate consumption.

[MIT OCW 10.442 Spring 2005 calendar](https://ocw.mit.edu/courses/10-442-biochemical-engineering-spring-2005/pages/calendar/) supplies link-only scope for growth models, continuous culture and animal-cell culture. This narrower model does not reproduce the source's microbial/enzyme curriculum. All derivations, parameters and tasks are original and AI-assisted. Device dynamics, lysis/recycling, detailed metabolism and physiological validation remain deferred; the course remains partial and unreviewed.
