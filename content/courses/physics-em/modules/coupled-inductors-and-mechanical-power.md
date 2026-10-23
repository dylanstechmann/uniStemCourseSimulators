# Coupled inductors and mechanical power

The existing induction reading establishes a single inductor's state and energy. Mutual coupling adds a second current, a reference-dependent cross term and a useful test of passive energy consistency. A separate moving-rod example then connects induced emf, drag and external work. All circuits, fields and motions below are prescribed ideal teaching models; they are not instructions for building electrical or mechanical equipment.

## References belong in the model

Choose both reference currents to enter dotted terminals and each coil's voltage positive where its current enters. For fixed linear geometry, write

$$\begin{pmatrix}v_1\\v_2\end{pmatrix}=L\begin{pmatrix}i_1'\\i_2'\end{pmatrix},\qquad
L=\begin{pmatrix}L_1&M\\M&L_2\end{pmatrix}.$$

The sign of $M$ follows the declared winding/reference orientation. Reversing one coil's terminal/current convention changes the signs of its mutual terms as well as the relevant state and voltage coordinates. A negative mutual coefficient is therefore not by itself evidence of an active device or negative total stored energy. Keep the source and observation references fixed when comparing two descriptions.

For constant symmetric $L$, stored magnetic energy is

$$U=\frac12L_1i_1^2+Mi_1i_2+\frac12L_2i_2^2=\frac12\mathbf i^TL\mathbf i.$$

Differentiating gives $U'=\mathbf i^TL\mathbf i'=i_1v_1+i_2v_2$. This is total coil port power under passive signs. Either port can return power, and the total can be negative while the stored energy decreases. Adding the absolute values of port powers would destroy the energy identity.

## Passive energy constrains the coefficients

Require $L_1,L_2>0$ and $M^2\leq L_1L_2$ so that $L$ is positive semidefinite. The coupling magnitude is $|M|/\sqrt{L_1L_2}\leq1$. When the inequality is strict, the energy is positive definite and the current derivative can be found by inverting $L$. At equality an ideal perfectly coupled model is singular and needs its constraint interpreted; an arbitrary inverse formula is not valid there.

If $|M|$ exceeds the bound, some current direction makes the quadratic energy negative. That is a failure of this assumed passive two-inductor model, not a new source of available energy. Real geometry, loss and nonlinear magnetization can require a different constitutive law, but cannot be silently imported into the selected linear equation to excuse an inconsistent coefficient table.

## Worked instantaneous ledger

Choose $L_1=0.04$ H, $L_2=0.09$ H and $M=0.03$ H. The coupling magnitude is one half. At currents $(2,-1)$ A, energy is $0.08-0.06+0.045=0.065$ J. At derivatives $(3,-2)$ A/s, the voltages are $(0.06,-0.09)$ V. Total port power is $2(0.06)+(-1)(-0.09)=0.21$ W, matching the direct derivative of the energy expression.

A distinct rehearsal uses $L_1=0.02$ H, $L_2=0.08$ H, $M=0.02$ H, currents $(1,-2)$ A and derivatives $(4,1)$ A/s. Coupling is again one half, but energy is 0.13 J. The voltages are 0.10 and 0.16 V and total port power is $0.10-0.32=-0.22$ W. The negative sign describes energy returning through the ports at that instant. The determinant is 0.0012 H², so this rehearsal remains nonsingular and passive.

## Add resistive loss without double counting

With series resistances collected in a positive diagonal matrix $R$ and external voltage vector $u$, the dynamics are $L\mathbf i'+R\mathbf i=\mathbf u$. Multiply by $\mathbf i^T$:

$$\mathbf u^T\mathbf i=U'+\mathbf i^TR\mathbf i.$$

The source input splits into stored-energy change and resistive dissipation. A source can receive energy during part of a transient even though resistive dissipation remains nonnegative. An energy report should retain signed source work, the storage difference and integrated loss as separate entries. Small equation residuals do not automatically verify the signs of all three.

## Motional induction and external work

For a separate conducting rod of length $\ell$ translating perpendicular to a uniform field $B$ and to its own length, the ideal motional emf magnitude is $B\ell u$. Assume a closed resistive path of total resistance $R$, negligible inductance and a prescribed constant speed. Then $I=B\ell u/R$, the magnetic drag magnitude is $IB\ell$, and the external agent maintaining the speed supplies

$$P_{ext}=F_{drag}u=I(B\ell u)=I^2R.$$

For a worked rod use $B=0.4$ T, $\ell=0.5$ m, $u=2$ m/s and $R=4$ ohms. The emf is 0.4 V, current 0.1 A, drag 0.02 N and supplied power 0.04 W. The rehearsal changes to $B=0.5$ T, $\ell=0.2$ m, $u=3$ m/s and $R=2$ ohms: emf 0.3 V, current 0.15 A, drag 0.015 N and power 0.045 W.

Lenz's law fixes drag opposite the prescribed motion. The microscopic magnetic force is perpendicular to an individual charge's total velocity; the macroscopic motional-emf and mechanical-reaction ledger includes the moving conductor and external constraint. Ignoring that mechanical boundary creates an apparent energy contradiction. If speed or inductive storage varies, include the missing state/energy terms rather than reusing the steady resistive identity unchanged.

## Verification and limits

Check the matrix quadratic form, passive determinant, voltage equation and signed energy derivative independently. Compare a numerical resistive transient with source/storage/loss quadrature. For the rod, retain orientation and external work as well as current. [MIT OCW 8.02 Spring 2007 class topics](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/class-topics/) sessions 20–23 supply link-only induction/mutual-energy scope. All explanations and cases are original and AI-assisted. Lossy cores, nonlinear saturation and equipment design remain deferred; the course remains partial and unreviewed.
