# A radiating sheet, reflection and standing-field energy

The plane-wave reading describes energy carried far from a source but does not supply a source boundary. The interference reading superposes fields but does not impose a conducting interface. Two separate ideal models now make those boundaries explicit: a prescribed current sheet emitting in both directions, and an incident wave reflected by a perfect conductor. These original mathematical cases are not an antenna design or an equipment procedure.

Use a consistent set of stipulated teaching constants: $\mu_0=4\pi\times10^{-7}$ H/m, $c=3.00\times10^8$ m/s, $\epsilon_0=1/(\mu_0c^2)$ and wave impedance $Z_0=\mu_0c=120\pi$ ohms. The supplied $c$ is rounded; the other derived relations are internally consistent within this model. Earlier exercises may stipulate their own rounded constants, so do not silently mix them in one numerical ledger.

## Prescribe a source and outgoing-wave condition

An infinite sheet at $z=0$ has surface current $\mathbf K(t)=K_0\cos(\omega t)\hat{\mathbf x}$, in A/m. Assume identical vacuum on both sides and waves propagating away from the sheet. Tangential electric field is continuous. The magnetic boundary condition is $\hat{\mathbf z}\times(\mathbf H_+-\mathbf H_-)=\mathbf K$.

For an outgoing wave on the positive side, $H_y=E_x/Z_0$; on the negative side, $H_y=-E_x/Z_0$. Substitution in the boundary condition gives $E_x(0,t)=-Z_0K(t)/2$. Therefore the electric field on either side is

$$E_x(z,t)=-\frac{Z_0K_0}{2}\cos\left[\omega(t-|z|/c)\right].$$

The sign and the two magnetic-field directions follow from the selected surface-current reference and outgoing propagation. At a remote point, the waveform depends on the earlier source time $t-|z|/c$, not on the sheet's current at the observation time. This is one elementary generation model consistent with the source-free traveling waves away from the sheet.

The sheet is infinite, so report power per area rather than an infinite total power or a finite antenna pattern. No assertion is made about how a real material could maintain this prescribed coherent current across an unbounded area.

## Close the source and outward-energy ledger

The peak electric magnitude is $Z_0K_0/2$. Each side carries time-average outward flux

$$I_{one}=\frac{E_0^2}{2Z_0}=\frac{Z_0K_0^2}{8}.$$

The two outward fluxes add to $Z_0K_0^2/4$. Their Poynting vectors point in opposite coordinate directions, but each has positive dot product with its outward normal. Adding vectors without the boundary normals would confuse net vector direction with total energy leaving a control region.

At the sheet, the field's work on its prescribed current is $\mathbf E\cdot\mathbf K=-Z_0K^2/2$. The negative sign means this source transfers energy into the electromagnetic field. Its average electromagnetic power supplied per area is $Z_0K_0^2/4$, matching both outgoing sides. A detailed mechanical source could also store carrier kinetic energy; that additional instantaneous ledger is not represented by a prescribed current alone.

For a worked source choose $K_0=0.02$ A/m. Peak field is $1.2\pi$ V/m, each side carries $0.006\pi$ W/m², and total outward flux is $0.012\pi$ W/m². The rehearsal changes to $K_0=0.01$ A/m: peak field $0.6\pi$ V/m, one-side flux $0.0015\pi$ W/m² and total $0.003\pi$ W/m². With $\omega=10^8$ rad/s, wavelength is $2\pi c/\omega=6\pi$ m and a point 30 m away has propagation delay 0.1 microseconds.

## A separate conducting-boundary problem

Now remove the prescribed sheet model. A wave approaches a perfect conductor at $z=0$ from vacuum $z<0$. Take incident $E_x=E_0\cos(kz-\omega t)$. The reflected electric field is $-E_0\cos(kz+\omega t)$, so tangential electric field vanishes at the conductor. The two magnetic fields add there. Their total fields are

$$E_x=2E_0\sin(kz)\sin(\omega t),\qquad B_y=\frac{2E_0}{c}\cos(kz)\cos(\omega t).$$

The wall is an electric node and a magnetic antinode. Electric and magnetic standing-field maxima occur at different positions and times. The traveling-wave instantaneous relation $E=cB$ therefore cannot be applied to these total fields point by point.

Their Poynting flux oscillates in sign and averages to zero. Yet the time-average total field energy density is $\epsilon_0E_0^2$, nonzero and independent of position for this ideal equal-amplitude standing pattern. Zero average transport is not zero field energy. Reflection also transfers momentum: pressure on the ideal reflector is $2I_{incident}/c$, with $I_{incident}=E_0^2/(2Z_0)$. Momentum transfer does not require net time-average energy absorption by the perfect conductor.

For the rehearsal incident amplitude $E_0=6$ V/m, the wall's peak magnetic field is 40 nT and an electric antinode has peak magnitude 12 V/m. Incident intensity is $0.15/\pi$ W/m², reflector pressure is $1/\pi$ nPa, and standing-field average energy density is $1/\pi$ nJ/m³. Pressure and energy density share dimensions; their numerical equality here follows from this specific reflection model.

## Independent checks and limits

Verify the sheet's boundary signs, evaluate both outward fluxes, and integrate source work and wave flux over a cycle. For reflection, check the wall condition, Maxwell relations in vacuum, local electric/magnetic energy and zero average Poynting flux. Use full fields rather than intensity-only addition. The [MIT OCW 8.02 Spring 2007 class topics](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/class-topics/) and [Chapter 13 scope](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/resources/chapte13em_waves/) include source generation, standing waves and conducting reflection. They are link-only references; no text, figure, problem or animation is imported. All cases are original and AI-assisted. Finite antenna patterns, diffraction, lossy interfaces and material response remain deferred; the course stays partial and unreviewed.
