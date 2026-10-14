# Stress, strain, and constitutive behavior

Mechanical measurements begin with a load and a change in shape, but force and displacement alone do not describe a material response. Stress and strain normalize those observations by geometry. A constitutive law then relates stress to strain, and in a time-dependent material it relates stress to the history of deformation. The model is useful only for the direction, deformation range, time scale, and preparation conditions it represents.

## From force and displacement to stress and strain

For a simple tensile specimen with initial cross-sectional area $A_0$, initial length $L_0$, applied axial force $F$, and length change $\Delta L$, engineering stress (also called nominal stress) and engineering strain are

$$\sigma_{eng}=\frac{F}{A_0}, \qquad \epsilon_{eng}=\frac{\Delta L}{L_0}.$$

Stress has units of pressure, such as pascals (N/m²); strain is a ratio and has no units. Displacement is an absolute length, whereas strain describes the fractional change relative to a stated reference length. In a general three-dimensional loading state, stress and strain have directional components; these one-dimensional expressions describe only a simple axial test. Shear stress is force parallel to a surface divided by area, not the same component as axial normal stress.

**Worked example.** A synthetic specimen with $A_0=1000$ µm² and $L_0=20$ µm is loaded by $F=10$ µN and extends by $\Delta L=0.4$ µm. Since $1000$ µm² is $1.0\times10^{-9}$ m², the nominal stress is $10$ kPa. The engineering strain is $0.4/20=0.020$, or 2%. If the response is linear elastic in this range, the slope is an apparent Young's modulus $E=\sigma/\epsilon=0.50$ MPa. The axial stiffness of this specimen is instead $F/\Delta L=25$ N/m. Modulus normalizes a material response; stiffness also depends on specimen geometry.

For small uniaxial deformation in a specified direction, a linear elastic model uses $\sigma=E\epsilon$. Its slope is not automatically a universal material constant: a nonlinear tissue may have different slopes at different strain ranges, and an anisotropic sample may respond differently along different axes. At larger deformation, engineering strain and stress no longer track the current configuration. With stretch ratio $\lambda=L/L_0$, logarithmic strain is $\epsilon_{true}=\ln\lambda$; true stress uses the current cross-sectional area. The choice of measure and reference configuration should match the deformation and model assumptions.

## The loading protocol determines the observation

In a **stress-relaxation** test, the specimen is brought to a specified strain and that deformation is held while stress is recorded over time. In a **creep** test, a specified stress is held while strain is recorded. The held variable distinguishes the tests: a declining force during a fixed-deformation hold is relaxation, while growing deformation under fixed force is creep. A rate-dependent material can give different apparent values when tested at different loading rates even if the specimen is unchanged.

The ideal Maxwell model places a spring and dashpot in series. After an ideal step strain, its stress decays as $\sigma(t)=\sigma_0e^{-t/\tau}$ with relaxation time $\tau=\eta/E$, where $\eta$ is viscosity and $E$ is spring modulus. It eventually relaxes fully in this idealization. A standard linear solid adds an elastic path in parallel with a Maxwell element, so its stress after a step strain has an exponential transient plus a nonzero long-time contribution. It can therefore represent partial relaxation over a stated time range. These models are useful simplified descriptions, not complete representations of active cells or tissues.

**Model comparison.** For a synthetic Maxwell element with $E=1$ kPa and $\eta=2$ kPa·s, $\tau=2$ s. Five seconds after the step, the predicted stress is $e^{-5/2}\approx0.082$ of its initial value, approaching zero at long time. A standard linear solid can instead approach its equilibrium spring contribution while its transient term decays. The distinction matters when interpreting a long hold: a material that retains stress at long time needs a model with a nonzero equilibrium response over that observation window. A purely elastic model would predict constant stress at fixed strain and cannot describe the observed relaxation.

## Choose a model for the regime and the question

If the observation time is much shorter than a relaxation time, a viscoelastic material can appear nearly elastic during that short window. At comparable times, relaxation or creep becomes visible; at longer times, the equilibrium behavior matters. Model selection should therefore follow the loading protocol and observation window rather than the name of a material alone. A force relaxation after a fixed indentation, for example, requires time dependence during that hold; it does not by itself identify the microscopic mechanism.

Biological specimens add further qualifications. They can be anisotropic, nonlinear, hydrated, porous, preconditioned, and actively remodeled. Geometry and boundary conditions determine the calculated stress and strain, while temperature, hydration, loading direction, loading rate, and prior cycles can change the measured response. Indentation also creates a nonuniform stress field and needs an appropriate contact model; it cannot be treated as a uniform axial test merely by dividing force by an arbitrary area. Report the specimen geometry, loading mode, reference configuration, rate, hold duration, and preparation when comparing results.

## Common mistakes

- Calling displacement “strain” without dividing by a stated reference length.
- Treating force per specimen as stress without accounting for the loaded area and direction.
- Calling specimen stiffness and material modulus interchangeable; specimen stiffness changes with geometry.
- Confusing creep with stress relaxation by overlooking which variable is held fixed.
- Selecting an elastic or viscoelastic model without specifying the strain range and observation-time window.
