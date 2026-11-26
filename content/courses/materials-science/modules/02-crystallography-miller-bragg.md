# Crystallography, Miller indices, cubic spacing and Bragg XRD

**Status:** Original reading in partial Materials Science 0.1.0; unreviewed and formative-only. Every crystal, peak and numerical value below is synthetic and fictional. The route analyzes supplied records and provides no instrument operating procedure or acquisition settings.

## Lattices, directions and planes

A crystal model repeats a motif according to translational symmetry. The lattice supplies the repeat geometry, while the basis describes what is placed at each lattice point. Unit cells are chosen geometric representations of that repeat. They need not contain the same number of atoms for different structures, and a cell’s volume alone does not reveal its motif.

Crystallographic directions use square brackets, planes use parentheses, and families use angle brackets or braces respectively. A direction is constructed from vector components and reduced to the smallest integers with the same ratio. A plane is indexed through intercepts expressed in lattice-parameter units: take reciprocals, clear fractions and reduce. An intercept at infinity gives zero. A negative intercept produces a negative index, conventionally written with a bar over that index.

Consider a plane intersecting x at +a, y at −a and z at infinity. Its reciprocal intercepts are 1, −1 and 0, so the plane is (1 −1 0), with the minus displayed as an overbar in conventional typesetting. It is not the direction [1 −1 0]. Curly braces would refer to a symmetry-related family rather than this one explicitly stated plane. Careful notation prevents a geometric statement from turning into an ambiguous label.

Parallel planes share Miller indices in this convention, and translating a plane without changing orientation does not change its indices. Indices do not by themselves provide an absolute spatial location. The convention also depends on the chosen crystal axes; noncubic systems require the appropriate metric rather than the cubic formula used below.

## Cubic interplanar spacing

For a cubic lattice with parameter a, spacing between adjacent parallel (hkl) planes is d(hkl) = a/√(h²+k²+l²). This expression follows from cubic geometry. It should not be transferred unchanged to tetragonal, hexagonal or lower-symmetry cells.

A fictional cubic crystal has a = 0.400 nm. For (100), the squared-index sum is 1 and d(100) = **0.400 nm**. For (210), the sum is 2² + 1² + 0² = 5, so d(210) = 0.400/√5 = **0.178885… nm**. For (111), a would be divided by √3 instead. The calculation is deterministic once a and the plane family are stipulated; it does not establish that a real specimen contains those planes or that a reflection will be observable.

Structure-factor and selection-rule considerations can affect which reflections have measurable intensity. Geometric permission for a plane family is not a promise of a peak. Missing intensity can arise from several causes, including scattering factors, texture, resolution, overlap or an unsuitable model. Consequently, “no peak observed” is not equivalent to “element absent,” and a calculated d value is not a chemical analysis.

## Bragg geometry and the 2θ convention

The first-order Bragg model is nλ = 2d sinθ with n = 1. It connects wavelength λ, plane spacing d and the Bragg angle θ for a simplified constructive-interference condition. Many powder-diffraction records display the detector scattering angle 2θ. Always state which angle is being used. The ratio λ/(2d) must be dimensionless and within the inverse-sine domain for a real solution in this first-order model.

Suppose a synthetic record supplies λ = 0.154 nm and d = 0.200 nm. Then sinθ = 0.154/(2 × 0.200) = 0.385. Compute θ = asin(0.385), and then double it to obtain **2θ = 45.28748…°**. Substituting 45.4° directly as θ would double the intended angle incorrectly. Using different length units for λ and d would also corrupt the ratio.

To analyze a supplied peak at 2θ, reverse the procedure: divide the displayed angle by two before evaluating the sine, then solve d = λ/[2sin(θ)]. Only after obtaining d should a cubic lattice parameter be calculated as a = d√(h²+k²+l²), and only if the cubic assignment is stipulated or independently supported. The multi-technique lab performs this two-step calculation for every row.

## From a peak to bounded interpretation

A peak position constrains spacing under an assumed order and wavelength. Intensity, width and shape can carry other information, but their interpretation needs appropriate models and calibration. One position cannot by itself establish phase purity, grain size, residual stress, texture or composition. Even agreement with a cubic geometric model does not exclude an alternative assignment with overlapping spacing.

A useful synthetic analysis table therefore separates supplied data from derived quantities and interpretation. Supplied: 2θ, wavelength and a proposed (hkl) assignment. Derived: θ, d and, under a cubic assumption, a. Interpretation: consistency with that assignment. Unknown: complete phase identity, defects, texture and chemistry. This separation prevents arithmetic precision from masquerading as experimental certainty.

No specimen preparation, alignment, voltage, current, scan rate or other acquisition procedure is included. Learners work only from existing fictional CSV values. If evidence is missing, it remains unknown rather than being replaced with a plausible value.

The official [MIT 3.091SC Fall 2010 syllabus](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/syllabus/) places crystallographic notation, X-rays and defects within a much broader solid-state chemistry sequence. The [MIT 3.012 Fall 2005 calendar](https://ocw.mit.edu/courses/3-012-fundamentals-of-materials-science-fall-2005/pages/calendar/) provides another link-only comparator for lattices, symmetry and diffraction. This original route develops only foundational notation, cubic geometry and first-order Bragg analysis. Tensor crystallography, reciprocal-space constructions, structure-factor derivation and full pattern refinement are deliberately deferred.
