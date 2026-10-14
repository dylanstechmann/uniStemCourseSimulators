# Controller design and sampled implementation

## Learning objectives

1. Compare proportional, integral and derivative action, including the conditions under which integral action can remove a steady-state offset.
2. Explain how actuator saturation, sensor noise and digital sampling constrain an ideal controller model.

## A controller turns error into an action

A feedback controller receives an error **e(t)** between a reference and a measured output, then calculates a command **u(t)** for an actuator. The signs, units and limits of those signals depend on the chosen system. A common continuous-time parallel PID form is

**u(t) = Kp e(t) + Ki ∫ e(τ) dτ + Kd de(t)/dt.**

The proportional, integral and derivative terms use different aspects of the error history. This formula is an ideal model: an actual actuator has finite range and rate, and software or electronics approximate the calculation. The [MIT OpenCourseWare feedback-control notes](https://ocw.mit.edu/courses/2-017j-design-of-electromechanical-robotic-systems-fall-2009/28a8095968b3e99189fe8c619640a2e1_MIT2_017JF09_feedback.pdf) are a link-only reference for PID action and integrator windup. A separate [MIT digital-control course](https://ocw.mit.edu/courses/2-171-analysis-and-design-of-digital-control-systems-fall-2006/) is a link-only reference for computation, sampling and implementation limits.

The units of each gain follow from the signals. If **e** is measured in degrees and **u** in volts, **Kp** has units V/degree, **Ki** has units V/(degree·time), and **Kd** has units V·time/degree. Different error and actuator units produce different gain units. Treating **Kp**, **Ki** and **Kd** as interchangeable dimensionless numbers hides their different roles and time scales.

## Compare the three actions

Proportional action responds to the error that exists now: **uP = Kp e**. A larger proportional gain commands a larger change for the same error and can speed correction. A proportional controller can still need a nonzero steady error to produce the sustained actuator command that balances a constant load. Raising the gain may reduce that offset, but it can also increase overshoot, amplify measurement noise and use more actuator range. The direction of a gain change is not, by itself, a guarantee of a stable or acceptable response.

Integral action responds to accumulated error: **uI = Ki ∫e dt**. If a constant error persists, the integral term continues to change the command. In many stable, unsaturated loops this can remove a constant steady-state offset. It also adds memory to the controller and can increase lag or overshoot. Integral action is not an instant correction: the integral must accumulate, and the rest of the loop must be able to respond.

Derivative action responds to the error's rate of change: **uD = Kd de/dt**. It can anticipate an approaching error change and add damping in some models. But differentiation emphasizes fast variations: a small high-frequency fluctuation in a measured signal can create a much larger derivative component. Practical derivative action therefore uses filtering and often operates on the measured output rather than the setpoint error, which can avoid a large derivative impulse when the reference jumps. Filtering the derivative also changes phase and response; it is not a free noise fix.

These terms are building blocks, not a list of settings. A proportional-only, PI, PD or PID controller can be appropriate for different models and goals. The later PI-tuning lesson calculates a specific controller law, crossover and tuning comparisons; this overview does not duplicate those derivations or recommend gains for a real process.

## Saturation can make the integral remember too much

An actuator cannot exceed its physical or configured limits. If a heater command is capped at its maximum while the measured output remains below its reference, the error may remain positive even though the controller cannot request more useful output. If the integral continues adding that error, its stored value can become large. After the error changes sign or the actuator leaves saturation, the integral term may continue commanding the old direction and cause a substantial overshoot. This is integrator windup.

The preserved practice scenario describes a PI controller whose actuator saturates during a large setpoint step and asks why the output later overshoots. The likely cause is that the integral kept accumulating while the actuator could not respond. This is a model-level explanation; saturation alone does not identify every cause of overshoot in an actual system, which could also involve delay, plant dynamics, a changed load or incorrect feedback polarity.

Anti-windup methods coordinate the stored integral with the actuator's achievable command. Conditional integration can pause accumulation when the actuator is saturated and the error would drive it farther into the limit. Back-calculation can feed the difference between the requested and applied command into the integral state. Both methods require deliberate design around the actuator and signal units; they are not equivalent to making the actuator limit disappear. A reset or clamp can also be appropriate in a specified controller, but its behavior must be considered at mode changes and startup.

## A digital controller acts at sample times

A digital controller reads a sensor at times **t = kTs**, calculates a command, and commonly holds that command until the next update. The sampling period **Ts** is the time between updates, and the sample frequency is **fs = 1/Ts**. This zero-order hold means the physical actuator does not receive a continuously changing command between samples. Sampling, computation time and communication can add phase lag or delay, especially when the loop responds on a time scale close to the update period.

If the sample period is too long for the dynamics that matter, a brief change may occur between readings and the controller may react late. A faster update is not automatically better: it raises computation and communication demands, can make quantization or high-frequency noise more visible, and cannot restore information that was already aliased. The previous frequency-response lesson explains why an analog anti-alias filter must precede conversion; the later sampling unit develops alias calculations, sample-period selection and discrete PI equations in more detail.

Finite ADC and DAC resolution quantize measurements and commands into available digital levels. Numerical rounding and bounded data types can also affect a software update. A controller implementation should therefore be understood as a timed sequence of measurements, calculations and actuator commands, not simply as its ideal continuous equation. The loop may miss a deadline, use a stale sensor sample or saturate even when the continuous transfer model predicts an acceptable result.

## Keep sensor noise and actuator limits in the same picture

Measurement noise enters the error calculation and can be converted into command variation. Derivative action is especially sensitive to rapid changes, while high proportional gain can also make a controller react more strongly to noise. Filtering may reduce some high-frequency variation but adds delay and phase lag. In a feedback loop, that extra lag can affect stability margin; the later case lesson studies the consequence of filtering a measurement in a fast loop.

Saturation, noise and sampling are connected. A noisy reading may trigger rapid command changes; a command may then reach its limit; accumulated integral action can persist while the actuator is capped; and delayed samples can make the controller respond to old information. No single P, I or D term explains every response without the plant, sensor, actuator, sample timing and controller implementation. The ideal equation is a starting model for analysis, not a complete device description.

For the preserved integral-action question, identify which term accumulates error and remember that offset removal assumes a stable loop with sufficient actuator authority. For the windup question, trace what the integral state does while the actuator is saturated. For a digital implementation, name the sample period and held output, then consider sensor noise, quantization and delays. These checks explain the controller mechanisms without supplying real-world settings, safety procedures or test protocols.
