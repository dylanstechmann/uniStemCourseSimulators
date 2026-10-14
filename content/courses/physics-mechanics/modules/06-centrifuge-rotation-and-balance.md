# Uniform circular motion and rigid-body rotation: an ideal centrifuge model

A centrifuge provides a concrete setting for circular-motion and rotational-dynamics calculations. This lesson uses only stipulated point-mass and rigid-body models with invented values. It predicts accelerations, energies, torques, and idealized support loads; it does not model a specimen or prescribe equipment operation.

## Learning objectives

By the end of this lesson, you should be able to:

1. Convert rotation rate to angular velocity, calculate inward radial acceleration and the conventional relative-centrifugal-force ratio, and compare two ideal circular paths.
2. Calculate a rigid body's moment of inertia, rotational kinetic energy, angular momentum, and ideal spin-up torque.
3. Estimate the rotating load associated with a point-mass imbalance and check calculations with units and limiting cases.

## Rotation rate and radial acceleration

A rotation rate in revolutions per minute converts to angular velocity by **ω = rpm × 2π/60** rad/s. A point moving at radius r in a circle has inward radial (centripetal) acceleration with magnitude **aᵣ = ω²r**. In an inertial frame, the net force on the point is directed inward; there is no additional outward force in this description.

The conventional quantity called **relative centrifugal force (RCF)** is the dimensionless acceleration ratio **aᵣ/g = ω²r/g**. Despite its name, this ratio is not a force.

**Synthetic calculation:** 3000 rpm gives ω ≈ 314.16 rad/s. At r = 0.10 m, aᵣ ≈ 9,870 m/s² and RCF ≈ 1,006. At that same radius, an acceleration ratio of 500 requires ω = √(500g/r), or about 2,115 rpm using g = 9.81 m/s². Halving ω quarters aᵣ; doubling r at fixed ω doubles it.

## The same motion described in the rotating frame

The inertial description above has only real forces, and their sum points inward. An observer riding on the rotor sees something different: a point fixed to the rotor is at rest, so its acceleration in that frame is zero. Newton's second law can be kept in this non-inertial frame only by adding a **pseudo-force** of magnitude mω²r directed outward, called the centrifugal term. It exactly balances the real inward force supplied by the wall or support. The name "relative centrifugal force" comes from this rotating-frame view.

Both descriptions predict the same measurable force on the support. A 1 g point at 0.10 m and 3000 rpm needs a real inward force of about 9.87 N, whichever frame is used to describe it. A point that moves relative to the rotor also acquires a Coriolis term, −2m ω × v, in the rotating frame. This lesson uses only points at rest on the rotor, so it never needs that term. Do not mix frames in one free-body diagram: either list real forces and an inward acceleration, or list real forces plus the pseudo-force and zero acceleration.

## The rotor as an ideal rotating body

Moment of inertia describes a body's resistance to angular acceleration: **I = Σmr²** for point masses, and **I = ½MR²** for a uniform solid disk. A synthetic 2 kg disk of radius 0.12 m has I = 0.0144 kg·m².

- **Rotational kinetic energy:** **K = ½Iω²**. At 3000 rpm, this disk has about 711 J of rotational kinetic energy.
- **Angular momentum:** **L = Iω**, or about 4.52 kg·m²/s at 3000 rpm. It is conserved when the net external torque is zero.
- **Ideal spin-up torque:** reaching ω in 20 s from rest at constant angular acceleration requires α = ω/20 ≈ 15.71 rad/s² and τ = Iα ≈ 0.226 N·m. This omits losses and any changing drive behavior. Doubling the target speed at the same spin-up time doubles this ideal torque and quadruples K.

## Point-mass imbalance model

If a point mass differs by Δm at radius r, its required inward net force has magnitude **Δmω²r**. The equal-and-opposite reaction contributes a rotating load on the support in this idealized model. An extra 1 g at 0.10 m and 3000 rpm corresponds to about 9.87 N. Two equal point masses at the same radius and opposite angles cancel their net rotating force in this model. Distributed rotor geometry, axial couples, supports, and vibration dynamics are omitted.

## Worked example: comparing two circular paths

**Problem.** A point follows a circle of radius 0.08 m at 4,000 rpm. What rotation rate gives the same inward acceleration on a circle of radius 0.10 m?

**Step 1.** Set the acceleration magnitudes equal: ω₁²r₁ = ω₂²r₂. Therefore ω₂ = ω₁√(r₁/r₂).

**Step 2.** The required rate is 4,000√(0.08/0.10) ≈ 3,578 rpm.

**Step 3.** Both ideal paths have aᵣ ≈ 14,024 m/s², about 1,429 times g. Keeping 4,000 rpm at 0.10 m instead gives about 17,552 m/s², 25% more acceleration. This comparison is only a kinematics calculation; it is not a device setting or a specimen prediction.

## Checks

- **Units:** ω²r has units s⁻²·m = m/s²; dividing by g gives a dimensionless ratio.
- **Limit:** as r approaches zero at fixed ω, aᵣ approaches zero.
- **Scaling:** at fixed r, doubling ω quadruples aᵣ and K; for a point-mass imbalance, the ideal load also scales with ω².
## Limits of this lesson

- **Sedimentation is outside this model.** The expression ω²r alone cannot predict a settling or pelleting time. Such a prediction needs a particle/fluid model and properties such as particle size, shape and density contrast, fluid viscosity, geometry, and flow conditions. Temperature can alter material properties, but this lesson provides no temperature comparison or operating recommendation.
- All numerical values are synthetic. No real rotor, specimen, safety limit, or operating protocol is represented.
