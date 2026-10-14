# Displacement current and electromagnetic-wave energy

In a charging capacitor, current flows through the connecting wires, but charge does not cross the gap between the plates in the ideal model. The electric field in that gap changes as charge accumulates. Maxwell's correction to Ampère's law accounts for that changing field and makes the magnetic-field calculation consistent whichever surface spans the same loop. A source-free electromagnetic wave then shows how changing electric and magnetic fields carry energy through space.

## A changing electric flux closes the current balance

For a closed curve (C), the Ampère–Maxwell law is

**\(\displaystyle \oint_C \mathbf B\cdot d\boldsymbol\ell
=\mu_0 I_{\mathrm{cond}}+\mu_0\epsilon_0\frac{d\Phi_E}{dt}\).**

The second term is often described using the displacement current

**\(\displaystyle I_D=\epsilon_0\frac{d\Phi_E}{dt}\),**

where \(\Phi_E=\int \mathbf E\cdot d\mathbf A\) is electric flux through a surface bounded by \(C\). It is a changing-field term in the field equation, not a claim that charge carriers pass through the capacitor gap. The conduction current \(I_{\mathrm{cond}}\) and the flux-change term can contribute differently on different surfaces; their sum gives the same circulation for the chosen boundary curve.

Consider a parallel-plate capacitor of plate area \(A\), with edge fringing neglected. If charge \(Q(t)\) is on one plate, the ideal gap field is \(E=Q/(\epsilon_0 A)\). The flux between the full plates is therefore \(\Phi_E=EA=Q/\epsilon_0\), so

**\(\displaystyle I_D=\epsilon_0\frac{d}{dt}\left(\frac{Q}{\epsilon_0}\right)
=\frac{dQ}{dt}=I.\)**

The displacement-current magnitude matches the wire current in this ideal charging model. If a loop around the lead is spanned by a surface cutting through the wire, that surface counts the conduction current. A surface bowed through the capacitor gap counts no conduction charge crossing the dielectric, but it captures the changing electric flux. Ampère's uncorrected law would assign incompatible magnetic circulations to those two surfaces; the added term closes the balance.

## Magnetic field between circular plates

Suppose circular plates of radius \(R\) charge at a steady current \(I\), with current density uniform over the circular area. For an Amperian circle of radius \(r<R\) centered on the axis, the enclosed fraction of displacement current is

**\(\displaystyle I_{D,\,\mathrm{enc}}=I\frac{\pi r^2}{\pi R^2}
=I\frac{r^2}{R^2}.\)**

Rotational symmetry makes the tangential magnetic field constant around that circle. Ampère–Maxwell then gives

**\(\displaystyle B(2\pi r)=\mu_0 I\frac{r^2}{R^2},\qquad
B(r)=\frac{\mu_0 I r}{2\pi R^2}\quad (r<R).\)**

Outside the plate radius, \(r\ge R\), the circle encloses the full displacement current and \(B=\mu_0 I/(2\pi r)\). For a synthetic example with \(I=0.50\,\mathrm{mA}\), \(R=40\,\mathrm{mm}\), and \(r=20\,\mathrm{mm}\), one quarter of the total current is enclosed: \(I_{D,\,\mathrm{enc}}=0.125\,\mathrm{mA}\). Thus \(B=\mu_0(0.125\,\mathrm{mA})/[2\pi(20\,\mathrm{mm})]=1.25\,\mathrm{nT}\). At \(r=50\,\mathrm{mm}>R\), the whole \(0.50\,\mathrm{mA}\) is enclosed and \(B=2.00\,\mathrm{nT}\). The interior result grows linearly from zero; outside, the ideal field falls as \(1/r\).

This calculation assumes circular plates, uniform charging current density, axial symmetry, a small enough plate gap for the stated field model, and negligible fringing. It estimates a magnetic field from a prescribed current; it is not a capacitor or instrument design rule.

## Energy flow in a plane wave

In a sinusoidal plane wave traveling through vacuum far from its sources, the electric field \(\mathbf E\), magnetic field \(\mathbf B\), and propagation direction are mutually perpendicular. Their amplitudes obey \(E_0=cB_0\), where \(c=1/\sqrt{\mu_0\epsilon_0}\). The energy-flux vector is the Poynting vector

**\(\displaystyle \mathbf S=\frac{1}{\mu_0}\mathbf E\times\mathbf B.\)**

Its direction is \(\mathbf E\times\mathbf B\), the direction in which the wave transports energy. For fields with peak electric amplitude \(E_0\), the peak flux magnitude is \(E_0B_0/\mu_0\). Since sinusoidal electric and magnetic fields are in phase, averaging over one cycle gives

**\(\displaystyle \langle S\rangle=\frac{E_0B_0}{2\mu_0}
=\frac{1}{2}c\epsilon_0 E_0^2.\)**

For example, if \(E_0=120\,\mathrm{V/m}\), then \(B_0=E_0/c=4.00\times10^{-7}\,\mathrm T=0.400\,\mu\mathrm T\). The peak flux is \(38.2\,\mathrm{W/m^2}\), and the time-average flux is half as large, \(19.1\,\mathrm{W/m^2}\). The factor of one-half comes from averaging the sinusoidal product over a full cycle; it is not an additional material loss.

The equal electric and magnetic energy densities provide a cross-check. At an instant, \(u_E=\epsilon_0 E^2/2\) and \(u_B=B^2/(2\mu_0)\). With \(E=cB\), these are equal, so the total wave energy density is \(u_E+u_B=\epsilon_0 E^2\), and the instantaneous plane-wave flux magnitude is \(cu\). The units of \(S\) are power per area. Do not confuse this energy flux with charge current in a wire or with the field-energy stored in a lumped capacitor.

## A checkable workflow and limits

For a charging-capacitor field calculation, first identify the loop and the surface used to span it. Separate conduction current from the electric-flux term, use the geometry to find enclosed flux, and then apply the symmetry of the field. For a wave, state whether the provided electric amplitude is peak or RMS; convert with \(E_0=\sqrt2 E_{\mathrm{rms}}\) when needed; find \(B_0\); and only then calculate peak or average energy flux. Check vector direction, SI units and the expected factor of one-half.

These wave relations assume a source-free plane wave in vacuum, sinusoidal steady fields, and no reflecting interface, dispersion or absorption. Dielectrics, conductive media, standing waves, interfaces and radiation from a particular antenna require additional boundary conditions and models. This lesson does not calculate an antenna's radiation pattern or prescribe electrical equipment. All numerical values are synthetic.

## Reference

MIT OpenCourseWare, **8.02 Physics II: Electricity and Magnetism**, Spring 2007, [class topics](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/class-topics/). Its week 12 topics include Maxwell's equations, electromagnetic radiation and energy flow after the circuit units. This is a scope comparator only; the present explanation and problems are original and do not copy MIT notes, activities or problem sets.
