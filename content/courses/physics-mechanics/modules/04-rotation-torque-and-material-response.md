# Rotation, torque, and material response

## Learning objectives

1. Calculate the magnitude and sign of torque about a stated axis using the force direction and perpendicular moment arm.
2. Calculate engineering stress, strain, and a declared small-strain elastic modulus, then check units and the model's limits.

## Start by naming the axis

A force can tend to turn an object, but the torque it produces is always defined about a selected point or axis. In a planar drawing, choose the hinge or origin first, state which direction counts as positive rotation, and measure the force's position from that origin. Changing the reference point can change the torque even when the force itself is unchanged. A force whose line of action passes through the chosen axis has zero moment arm and produces zero torque about that axis.

In vector form, torque is **τ = r × F**, where **r** points from the chosen origin to the force's point of application and **F** is the force vector. The magnitude is **|τ| = rF sin θ**, with θ the angle between those vectors. Equivalently, **|τ| = r⊥F**, where **r⊥ = r sin θ** is the shortest, perpendicular distance from the axis to the force's line of action. This perpendicular distance is the moment arm. The [OpenStax torque section](https://openstax.org/books/university-physics-volume-1/pages/10-6-torque) is a link-only reference for this relation and the right-hand-rule sign convention.

The angle and the moment arm matter. A 30 N force applied 0.20 m from a hinge at 90° has a 0.20 m moment arm, so its torque magnitude is **30 N × 0.20 m = 6 N·m**. If the same force is applied at the same point but points along the line from the hinge, θ is 0° and the moment arm is zero. If the force direction changes to 30° from that line, the moment arm is **0.20 sin 30° = 0.10 m**, and the magnitude is **3 N·m**. Multiplying force by the full distance in those cases would overstate the turning effect.

For a two-dimensional calculation with the origin at the reference axis, the out-of-plane component is **τz = rx Fy − ry Fx**. With counterclockwise positive, a force of 30 N downward at position (0.20 m, 0) has **τz = (0.20 m)(−30 N) = −6 N·m**: it tends to turn clockwise. The magnitude remains 6 N·m; the negative sign records direction under the chosen convention. Reversing the force would make the sign positive. In three dimensions, the cross product gives a torque vector perpendicular to the plane of **r** and **F**. For this week's scalar practice, keep the stated planar axis and sign convention explicit rather than trying to reconstruct an unspecified three-dimensional geometry.

## Combine moments about the same axis

When several forces act on the same rigid-body model, calculate each signed torque about the same origin and add the signed values: **τnet,z = Στi,z**. For example, a +6 N·m counterclockwise moment and a −2 N·m clockwise moment give a net torque of +4 N·m about the stated axis. Do not add magnitudes and then attach a direction afterward; opposite directions can partly cancel. A force balance and a torque balance answer different questions: zero net force means no translational acceleration in the chosen inertial model, while zero net torque means no angular acceleration in the corresponding rigid-body model. A body can satisfy one balance and fail the other.

Torque has SI units of newton-metres. Work also has units that can be written N·m, but torque is a moment while work is energy transferred through displacement. The shared unit expression does not make these quantities interchangeable. Check both the physical question and the calculation: lever arm times force has units **m·N**, and a zero moment arm must give zero torque. The 6 N·m hinge example is a magnitude; its signed value depends on the selected positive direction.

This lesson computes a moment about a known axis. It does not yet determine angular acceleration from a moment of inertia, calculate rotational kinetic energy or angular momentum, or impose rolling constraints. Those questions require additional rotational-state information and appear in the later rotation lesson. In particular, do not infer a spin-up rate from a torque alone: the distribution of mass and the net moments are also needed for the fixed-axis model **Στ = Iα**.

## Use force and extension to describe a specimen

For a uniform specimen under axial loading, engineering tensile stress divides the axial force by the initial cross-sectional area: **σ = F/A₀**. Engineering strain divides its change in gauge length by the initial gauge length: **ε = ΔL/L₀**. Both definitions require the measured force direction and the stated specimen geometry. Stress has pressure units, such as pascals; strain is a ratio of lengths and is dimensionless. A strain of 0.0025 is the same as 0.25%, not 0.0025%.

In a declared linear elastic, uniaxial, small-deformation interval, Young's modulus is the proportionality between stress and strain: **σ = Eε**, or **E = σ/ε** when ε is nonzero. The OpenStax [stress, strain, and elastic modulus section](https://openstax.org/books/university-physics-volume-1/pages/12-3-stress-strain-and-elastic-modulus) is a link-only reference for the conventional definitions. Because E is stress divided by dimensionless strain, its units are also pascals. Keep stress and modulus in compatible units before taking their ratio.

Consider a model rod with axial stress **σ = 5.0 × 10⁶ Pa** and a specified linear modulus **E = 2.0 × 10⁹ Pa**. Then **ε = σ/E = (5.0 × 10⁶ Pa)/(2.0 × 10⁹ Pa) = 2.5 × 10⁻³**, or 0.0025 as a dimensionless fraction. The units cancel. If the gauge length were 0.20 m and the model remained valid, the corresponding extension would be **ΔL = εL₀ = 0.00050 m**, or 0.50 mm. The strain question supplied in practice asks only for the dimensionless ratio; it does not provide geometry needed to calculate a specimen's actual extension.

An elastic modulus is a property of a defined material model and test interpretation, not simply the force required to stretch an object. If a uniform bar has stiffness **k = F/ΔL**, substitution of the definitions gives **E = kL₀/A₀** for the stated axial linear model. Thus two bars made from the same ideal material may have different force–extension stiffness because their lengths or areas differ. Dividing force directly by extension yields stiffness, not modulus; the geometry correction is essential.

## State what the scalar model leaves out

The ratio **E = σ/ε** is meaningful only for the specified stress and strain measures and the regime in which the linear relation is an acceptable description. A curved stress–strain response does not have one slope that describes every load. A secant ratio from a chosen origin and a tangent slope at a point are different quantities; neither should be called a universal constant without identifying the interval and method. Near damage, yielding, large deformation, or changing specimen geometry, this simple engineering ratio may cease to summarize the response well.

Biological tissues and engineered biomaterials can also depend on orientation, loading rate, hydration, history and specimen preparation. A scalar modulus from one direction and one test interval does not establish isotropy, predict creep, or identify a microscopic mechanism. Stress concentrations, nonuniform geometry, shear, bending and boundary compliance may also matter in a real measurement. Treat this lesson's numbers as model calculations, not measurements of tendon, bone or a manufactured device. The later materials and calibration lessons address orientation, time dependence, machine compliance and inference boundaries in more detail.

## A short model check

Before reporting a result, name the reference axis for torque or the initial geometry for stress and strain. Confirm the angle or signed component, keep units through substitution, and distinguish a magnitude from a signed moment. For a material calculation, verify that stress and modulus use the same pressure unit, that strain is dimensionless, and that the linear small-strain assumption was actually supplied. These checks connect the arithmetic to its physical meaning without turning a model prediction into evidence about a real specimen.
