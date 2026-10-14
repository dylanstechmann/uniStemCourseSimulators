# Wave superposition and two-source interference

An electromagnetic wave can be described by its electric and magnetic fields at each point. When two waves occupy the same region, the fields add. Whether their amplitudes reinforce or cancel depends on their phase difference at the observation point. This reading uses two coherent, same-frequency sources and a far-field double-slit geometry to connect path difference, phase, fringe position and intensity.

## From path difference to phase

Let two in-phase sources emit waves of wavelength \(\lambda\). At an observation point, let their path lengths be \(r_1\) and \(r_2\), and define the path difference \(\delta=r_2-r_1\). The phase difference is

**\(\displaystyle \phi=\frac{2\pi\delta}{\lambda}.\)**

Adding the two electric-field amplitudes gives constructive interference when \(\phi=2\pi m\), or \(\delta=m\lambda\), and destructive interference when \(\phi=(2m+1)\pi\), or \(\delta=(m+\tfrac12)\lambda\), for integer \(m\). These conditions assume the sources themselves start in phase. An initial source phase offset must be added to \(2\pi\delta/\lambda\).

For two coherent waves with intensities \(I_1\) and \(I_2\), the combined intensity is

**\(\displaystyle I=I_1+I_2+2\sqrt{I_1I_2}\cos\phi.\)**

The cross term carries the interference. If the sources have equal intensity \(I_0\), then \(I=4I_0\cos^2(\phi/2)\): the maximum is \(4I_0\), and a dark minimum reaches zero. Unequal amplitudes can still interfere, but their destructive minimum is not fully dark. If the relative phase fluctuates rapidly, the cross term averages away.

## Fringe positions in the far field

Place two narrow openings a distance \(d\) apart, with a screen a distance \(L\) away. At a screen coordinate \(y\) near the central axis, the paths are nearly parallel when \(L\gg d\) and \(|y|\ll L\). The path difference is then approximately

**\(\displaystyle \delta\approx d\sin\theta\approx\frac{dy}{L}.\)**

Bright fringes occur at \(y_m\approx m\lambda L/d\), and dark fringes at \(y_{m+1/2}\approx(m+\tfrac12)\lambda L/d\). The spacing between adjacent bright fringes is therefore \(\Delta y\approx\lambda L/d\). Increasing wavelength or screen distance spreads the pattern; increasing source separation narrows it.

For example, take \(\lambda=600\,\mathrm{nm}\), \(d=0.30\,\mathrm{mm}\), and \(L=2.0\,\mathrm m\). The adjacent-bright spacing is

**\(\displaystyle \Delta y=\frac{(600\times10^{-9}\,\mathrm m)(2.0\,\mathrm m)}{0.30\times10^{-3}\,\mathrm m}=4.0\,\mathrm{mm}.\)**

The third bright fringe from the center is at \(y_3=12\,\mathrm{mm}\); the first dark fringe is halfway between the central and first bright fringes, at \(2.0\,\mathrm{mm}\). The central maximum is \(m=0\). Do not count the center as the first nonzero-order fringe.

## A checkable workflow and limits

State the medium and wavelength, check whether the sources are coherent and whether their initial phase is specified, then compute path difference and phase before classifying a point as bright or dark. For screen locations, use the far-field small-angle approximation only when its geometry supports it. Check that \(\lambda L/d\) has units of length and that a larger slit separation gives closer fringes. Distinguish field-amplitude addition from intensity addition; intensities alone cannot be added when a stable relative phase produces a cross term.

This two-source model does not derive how an antenna generates radiation, calculate a single-slit diffraction envelope, or treat polarization, near fields, interfaces, dispersion or coherence loss in detail. It assumes monochromatic waves and an ideal far-field screen. All numerical values are synthetic.

## Reference

MIT OpenCourseWare, **8.02 Physics II: Electricity and Magnetism**, Spring 2007, [class topics](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/class-topics/) and [interference problem-solving note](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/resources/solving11/). The schedule places interference after the Maxwell/radiation unit; the problem-solving note identifies coherent double-slit constructive and destructive conditions and intensity. These are link-only scope references. This explanation and its problems are original and do not copy MIT material.
