# Model-based joint control: gravity compensation and computed torque

The [mass-matrix lesson](10-mass-matrix-gravity-and-energy-ledgers.md) built the dynamic equation τ = M(q)q̈ + h(q, q̇) + G(q) for a two-link arm in a vertical plane, and the [motor-envelope lesson](11-motor-envelope-backlash-and-sampled-feedback.md) tuned PD feedback for a single joint with no gravity. This lesson joins the two. It asks what PD feedback alone does to a two-link arm under gravity, how a gravity model removes the resulting sag, and how the full dynamic model can make each joint's error follow the same linear equation in every posture. That last scheme is **computed-torque control**. Each step depends on a model, so the lesson also traces what a modeling error does. The arm, masses and gains are synthetic teaching values.

The undergraduate [MIT OCW 2.12 Introduction to Robotics (Fall 2005) syllabus](https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/pages/syllabus/) schedules computed-torque control (L19) directly after its two dynamics lectures (L17–L18). This lesson follows that placement within the local dynamics week. It uses 2.12 as a scope comparator only and reproduces no MIT material.

## Learning objectives

By the end of this lesson, you should be able to:

1. Predict the steady-state sag of a PD-controlled arm under gravity, and calculate the residual error left when the gravity model has the wrong mass.
2. Write the computed-torque law, explain why it makes each joint error obey a linear second-order equation independent of posture, choose its gains from a natural frequency and damping ratio, and calculate the feedforward torque at a trajectory point.
3. Trace how model error, torque limits and sampling break the ideal cancellation, and compare fixed-gain PD with computed torque.

## The model

Use the arm from the mass-matrix lesson: massless links L₁ = 0.30 m and L₂ = 0.20 m, a point mass m₁ = 1 kg at the elbow and m₂ = 0.5 kg at the tool, g = 9.81 m/s². The shoulder angle q₁ is measured from horizontal and the elbow angle q₂ relative to link one. At q = (0, 90°) the first link is horizontal and the second points straight up, so

- G = ((m₁ + m₂)gL₁cos q₁ + m₂gL₂cos(q₁ + q₂), m₂gL₂cos(q₁ + q₂)) = **(4.4145, 0) N·m**;
- M = [0.155, 0.020; 0.020, 0.020] kg·m².

Write the target as q_d and the error as e = q_d − q.

## PD alone sags under gravity

Apply τ = K_p e − K_d q̇ with diagonal gains K_p = diag(50, 20) N·m/rad and hold the target q_d = (0, 90°). At rest the derivative term is zero, so the proportional term alone must supply the holding torque. That requires a nonzero error: K_p e = G(q) at equilibrium.

A first estimate evaluates G at the target: e₁ ≈ 4.4145/50 = **0.0883 rad**, about 5.1°. Because the arm droops, G changes slightly. Solving K_p e = G(q_d − e) exactly gives e ≈ (0.0898, 0.0046) rad. The elbow now sags a little too, because the tool link is no longer vertical once the shoulder droops. Raising K_p shrinks the sag but never removes it, and higher gains demand more torque for the same disturbance. An integral term can remove the steady error, but it adds its own dynamics and needs a saturation policy, as the motor-envelope lesson noted.

## Gravity compensation

Add the modeled gravity torque:

**τ = K_p e − K_d q̇ + Ĝ(q).**

The hat marks a model value. If Ĝ = G, then at rest K_p e = 0, so the arm settles exactly on target. The feedback gains are then free to shape the transient rather than fight gravity.

**Wrong mass.** Suppose the tool actually weighs 0.6 kg while the model still assumes 0.5 kg. The uncompensated part is ΔG = 0.1 × 9.81 × (0.30 cos q₁ + 0.20 cos(q₁ + q₂)), which is 0.2943 N·m at the shoulder and zero at the elbow for this posture. The residual sag is about 0.2943/50 = **0.0059 rad**. That is fifteen times smaller than with no compensation, but not zero. Gravity compensation converts a large systematic error into one proportional to the modeling error.

## Fixed gains feel different in different postures

The shoulder's effective inertia is M₁₁(q₂) = m₁L₁² + m₂(L₁² + L₂² + 2L₁L₂cos q₂). It is 0.155 kg·m² at q₂ = 90° and 0.215 kg·m² with the arm straight (q₂ = 0). If the elbow is held and the shoulder gain is K_p = 15.5 N·m/rad, the shoulder's natural frequency √(K_p/M₁₁) is **10.0 rad/s** in the bent posture but **8.49 rad/s** when straight. The off-diagonal term M₁₂ also couples the joints, so accelerating the shoulder disturbs the elbow. A PD design tuned in one posture is therefore slower, less damped or more coupled in another.

## Computed torque

Computed torque uses the whole model to cancel the configuration-dependent dynamics:

**τ = M̂(q)[q̈_d + K_d ė + K_p e] + ĥ(q, q̇) + Ĝ(q).**

If the model is exact, substituting into τ = Mq̈ + h + G and cancelling gives

**ë + K_d ė + K_p e = 0**

for each joint separately. Here K_p and K_d are acceleration gains, in s⁻² and s⁻¹, not torque gains. Every joint, in every posture, now has the natural frequency √K_p and damping ratio K_d/(2√K_p). For ω_n = 10 rad/s and critical damping, choose K_p = 100 s⁻² and K_d = 20 s⁻¹. The inner model turns a coupled nonlinear system into decoupled linear ones; the outer gains then set the response.

**Feedforward at a trajectory point.** On a planned path at q = (0, 90°) with q̇ = (1, 2) rad/s and q̈_d = (1, 0) rad/s², and zero tracking error, the law reduces to τ = Mq̈_d + h + G. The velocity-product terms at q₂ = 90° are h₁ = −m₂L₁L₂(2q̇₁q̇₂ + q̇₂²) = −0.24 N·m and h₂ = m₂L₁L₂q̇₁² = 0.03 N·m. Adding Mq̈_d = (0.155, 0.020) and G = (4.4145, 0) gives

**τ = (4.3295, 0.050) N·m.**

Gravity dominates the shoulder, but the velocity term subtracts 0.24 N·m, more than the inertial term adds. Omitting h would make the shoulder push too hard by that amount.

## What breaks the cancellation

- **Model error.** With the 0.6 kg tool, the computed-torque arm at rest satisfies M̂K_p e = ΔG, so e = M̂⁻¹ΔG/K_p. With K_p = 100 s⁻², this is about **0.022 rad** at the shoulder and an error of similar size and opposite sign at the elbow. The elbow error appears even though ΔG₂ = 0, because M̂⁻¹ couples the joints. In computed torque, model errors act as disturbances that the linear loop must reject.
- **Torque limits.** The cancellation assumes the requested torque is delivered. If the command exceeds an actuator limit, the cancellation fails and the error equation is no longer linear. Large gains on a large initial error are the usual cause.
- **Sampling and delay.** The law uses measured q and q̇ at discrete instants. Velocity from differenced positions is noisy, and delay erodes damping, as the motor-envelope lesson showed for a single joint.
- **Unmodeled effects.** Friction, gear compliance, motor dynamics and payload changes are absent from M̂, ĥ and Ĝ unless they are added and identified.

## Common mistakes

- Expecting PD alone to reach the target under gravity; the proportional term needs an error to supply holding torque.
- Mixing torque gains (N·m/rad) with computed-torque acceleration gains (s⁻²).
- Dropping the velocity-product term h during fast motion.
- Treating gravity compensation as exact when the payload mass is uncertain.
- Assuming computed torque decouples the joints when the model is wrong or the torque saturates.
- Tuning PD gains in one posture and assuming the same response everywhere.

## Worked example

**Problem.** The arm holds q_d = (0, 90°) under PD control with K_p = diag(50, 20) N·m/rad and no gravity model. The designer considers adding gravity compensation, or switching to computed torque with ω_n = 10 rad/s and ζ = 1. The tool's true mass is 0.6 kg; the model assumes 0.5 kg. Compare the steady errors.

**Step 1: PD alone.** The true gravity torque at the shoulder is 1.6 × 9.81 × 0.30 = 4.709 N·m. The linear estimate of the sag is 4.709/50 = 0.094 rad.

**Step 2: with gravity compensation.** Only ΔG₁ = 0.2943 N·m is left, so the error is 0.2943/50 ≈ 0.0059 rad.

**Step 3: computed torque.** With K_p = 100 s⁻², e = M̂⁻¹ΔG/100. The inverse of M̂ = [0.155, 0.020; 0.020, 0.020] is (1/0.0027)[0.020, −0.020; −0.020, 0.155], so e ≈ (0.0218, −0.0218) rad at the target posture.

**Step 4: interpret.** Computed torque has the larger steady error here because its effective stiffness, M̂K_p, is about 15.5 N·m/rad at the shoulder, below the PD design's 50 N·m/rad. Its advantage is a posture-independent, decoupled transient, not automatic accuracy. Payload identification, a larger K_p within torque limits, or an outer integral term would address the residual.

## Limits of this lesson

All masses, lengths and gains are synthetic, and the arm is an idealized point-mass model with no friction, motor dynamics or flexibility. The analysis assumes continuous-time control, exact measurement and unsaturated actuators except where stated. Stability proofs for PD with gravity compensation, adaptive and robust computed torque, and task-space control are not developed. Nothing here is a controller setting or safety assessment for any real robot, and no human-interaction or safety-rated function is addressed. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
