# Photons, matter waves and quantization in a box

The [photon-accounting lesson](07-atoms-amount-and-photon-accounting.md) used E = hν = hc/λ to turn a wavelength into the energy of one photon, and the [hydrogenic-orbital lesson](hydrogenic-orbitals-and-radial-probability.md) used energy levels and probability distributions without saying why an electron should have either. This lesson supplies that reason. It shows that light delivers energy in lumps, that matter has a wavelength, that confinement lets a wave take only certain shapes, and that those shapes carry the quantized energies. The model is one-dimensional, and every metal, box and light source is synthetic.

The undergraduate [MIT OCW 5.111SC Principles of Chemical Science (Fall 2014) Unit I](https://ocw.mit.edu/courses/5-111sc-principles-of-chemical-science-fall-2014/pages/unit-i-the-atom/) opens with the wave-particle duality of light ([Lecture 3](https://ocw.mit.edu/courses/5-111sc-principles-of-chemical-science-fall-2014/pages/unit-i-the-atom/lecture-3-wave-particle-duality-of-light/)) and of matter with the Schrödinger equation ([Lecture 4](https://ocw.mit.edu/courses/5-111sc-principles-of-chemical-science-fall-2014/pages/unit-i-the-atom/lecture-4-wave-particle-duality-of-matter-schrodinger-equation/)). The published topic index of [UC Irvine Chem 1A General Chemistry](https://ocw.uci.edu/courses/chem_1a_general_chemistry.html) lists the photoelectric effect in Lecture 3 and the de Broglie wavelength, the Heisenberg uncertainty principle and the particle in a box in Lecture 4. The repository's General Chemistry I/II scope crosswalk had recorded the wave and particle treatment as missing, and this lesson adds a bounded version of it. Both courses are link-only scope comparators; no text, figure or problem is reproduced.

## Learning objectives

By the end of this lesson, you should be able to:

1. Apply the photon picture to the photoelectric effect: find a threshold wavelength, a maximum kinetic energy and a stopping potential.
2. Use the de Broglie relation and the uncertainty relation to decide when the wave nature of a particle matters.
3. Derive the allowed wavelengths and energies of a particle in a one-dimensional box, and use them to predict an absorption wavelength and a probability.

## Light arrives in photons

When light shines on a clean metal, electrons can leave its surface. Three observations resist a picture in which light spreads its energy smoothly over a wavefront. Below a threshold frequency ν₀ no electrons leave, however intense the light. Above it, electrons leave with no measurable delay. And the maximum kinetic energy of the emitted electrons rises with the light's frequency but does not change with its intensity, which only changes how many electrons leave each second.

The photon picture explains all three. A photon of frequency ν carries energy hν, and one photon gives its energy to one electron. The electron must spend at least the metal's **work function** φ to escape, and whatever remains is kinetic energy:

\[
KE_{\max} = h\nu - \varphi = \frac{hc}{\lambda} - \varphi .
\]

Escape needs hν ≥ φ, so the threshold frequency is ν₀ = φ/h and the threshold wavelength is λ₀ = hc/φ. The **stopping potential** V_s is the retarding voltage that just halts the fastest electrons, so eV_s = KE_max. Work in electronvolts, with 1 eV = 1.602 176 634 × 10⁻¹⁹ J. Because h, c and e are exact, hc = 1239.84 eV·nm, and a wavelength in nanometres gives the photon energy in electronvolts directly as E = 1239.84/λ.

## Matter has a wavelength

A particle of momentum p has the de Broglie wavelength λ = h/p, which is h/(mv) at speeds far below the speed of light. The electron mass, 9.109 × 10⁻³¹ kg, is a measured value, not an exact constant. An electron moving at 1.00 × 10⁶ m/s has λ = 6.626 × 10⁻³⁴/(9.109 × 10⁻³¹ × 1.00 × 10⁶) = 7.27 × 10⁻¹⁰ m = 0.727 nm, a few times the spacing between atoms. A 0.145 kg ball at 40 m/s has λ = 1.14 × 10⁻³⁴ m, far below anything measurable, so its wave nature never shows.

An electron accelerated from rest through a potential difference V gains kinetic energy eV, so p = √(2meV) and λ = h/√(2meV). At 100 V this is 0.123 nm, comparable to the spacings between atoms in a crystal, which is why a beam of such electrons can diffract from one.

## Uncertainty

A wave-like particle cannot have both a sharp position and a sharp momentum. If Δx and Δp are the spreads of position and momentum in its state,

\[
\Delta x\,\Delta p \ge \frac{\hbar}{2}, \qquad \hbar = \frac{h}{2\pi} = 1.0546 \times 10^{-34}\ \text{J·s}.
\]

This is a property of the wave description, not a statement that instruments are clumsy. Confine an electron to Δx = 0.10 nm, about an atom's width. Then Δp ≥ ħ/(2Δx) = 5.27 × 10⁻²⁵ kg·m/s, so Δv ≥ 5.8 × 10⁵ m/s. That is comparable to the speeds of electrons in atoms, so a definite orbit has no meaning at this scale. A 1.0 µg dust grain located to within 1.0 µm has Δv ≥ 5.3 × 10⁻²⁰ m/s, which no experiment would notice.

## A standing wave in a box

Place an electron in a region 0 ≤ x ≤ L that it cannot leave. The wave must vanish at both walls, like a string fixed at both ends, so only standing waves with a whole number n of half-wavelengths fit: L = nλ/2, with n = 1, 2, 3, …. The de Broglie relation then gives p = h/λ = nh/(2L). Inside the box the potential energy is zero, so all the energy is kinetic:

\[
E_n = \frac{p^2}{2m} = \frac{n^2 h^2}{8 m L^2}.
\]

Four consequences follow. The energy is quantized because the walls allow only certain wave shapes. The lowest energy E₁ = h²/(8mL²) is not zero, because n = 0 would mean no wave at all; this agrees with the uncertainty relation, since confinement to a width near L forces a momentum spread near ħ/L. The levels spread apart, with E_{n+1} − E_n = (2n + 1)E₁. And E_n scales as 1/L², so shrinking the box raises every level and widens every gap, the idea behind the size-dependent colours of semiconductor quantum dots. Real dots need a more detailed model than a particle in a box.

For L = 1.00 nm, E₁ = 0.3760 eV, E₂ = 1.504 eV and E₃ = 3.384 eV. Promoting the electron from n = 1 to n = 2 takes ΔE = 3E₁ = 1.128 eV, which a photon of wavelength 1239.84/1.128 = 1099 nm supplies. Halving the box to 0.50 nm quadruples every energy, so ΔE = 4.513 eV and the wavelength falls to 274.8 nm.

The allowed waves are ψ_n(x) = √(2/L) sin(nπx/L), and |ψ_n|² is the probability density. Integrating from 0 to a gives the probability of finding the electron there:

\[
P_n(0 \to a) = \frac{a}{L} - \frac{\sin(2n\pi a/L)}{2n\pi}.
\]

For n = 1 and a = L/4, P = 1/4 − 1/(2π) = 0.0908, well below the uniform value 0.25 because the ground-state wave piles up probability near the middle. For n = 2 the wave has a node at L/2, and P(0 → L/3) = 1/3 − sin(4π/3)/(4π) = 0.4022.

**Where the Schrödinger equation enters.** The equation −(ħ²/2m) d²ψ/dx² = Eψ with ψ = 0 at both walls is solved by exactly these sine waves and exactly these energies. This lesson reached them from the standing-wave condition and the de Broglie relation and does not develop the equation further. A box and a hydrogen atom show how the shape of the potential sets the pattern of levels: a box gives E ∝ n², with levels that spread out, while the Coulomb attraction of the hydrogenic lesson gives E ∝ −1/n², with levels that crowd together toward ionization.

## Worked example

**Problem.** A synthetic metal film has a work function of 2.30 eV and is illuminated with 400 nm light. Find the photon energy, the maximum kinetic energy and stopping potential, the threshold wavelength, the speed and de Broglie wavelength of the fastest electron, and the effect of doubling the intensity.

**Step 1: photon energy.** E = 1239.84/400 = 3.100 eV.

**Step 2: kinetic energy and stopping potential.** KE_max = 3.100 − 2.30 = 0.800 eV, so V_s = 0.800 V.

**Step 3: threshold.** λ₀ = 1239.84/2.30 = 539 nm. The light's 400 nm is shorter, so its frequency is above threshold and emission occurs.

**Step 4: the fastest electron.** KE = 0.800 × 1.602 × 10⁻¹⁹ J = 1.28 × 10⁻¹⁹ J, so v = √(2KE/m) = 5.30 × 10⁵ m/s and λ = h/(mv) = 1.37 nm, several atomic spacings.

**Step 5: intensity.** Doubling the intensity doubles the number of photons per second, and therefore the number of electrons per second, but each photon still carries 3.100 eV, so KE_max and V_s do not change.

## Common mistakes and checks

- Substituting a wavelength in nanometres into hc/λ with SI constants, or mixing electronvolts with joules.
- Expecting a brighter beam below threshold to eject electrons, or expecting intensity to raise KE_max.
- Forgetting the work function and calling the whole photon energy the kinetic energy.
- Using the speed of light for the electron in λ = h/(mv).
- Treating the wavelength of a macroscopic object as something observable.
- Allowing n = 0 in a box, or using E_n ∝ n instead of n².
- Mixing nanometres and metres in L, where E ∝ 1/L² turns a factor of 10⁻⁹ into 10⁻¹⁸.
- Reading Δx Δp ≥ ħ/2 as a limit on instruments rather than on what a wave-like state can have.

A quick check for atomic-scale answers: an electron in a 1 nm box has a ground-state energy near 0.4 eV, and every energy scales as 1/L².

## Limits of this lesson

All metals, films, boxes and light sources are synthetic. The treatment is non-relativistic and one-dimensional, and the infinite box is an idealization of a binding potential: it has no walls that leak, no electron spin and no electron–electron repulsion. The Schrödinger equation is named and its box solutions are used, but it is not derived or solved in general, and many-electron atoms are not treated. Black-body radiation and the history of the Bohr model are not developed; the hydrogenic lesson covers hydrogen-like levels. Nothing here is a laboratory procedure or a device design. Original instruction has substantial AI assistance and uses link-only references without copied source text. The course remains partial, unreviewed and formative-only.
