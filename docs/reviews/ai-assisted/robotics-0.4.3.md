# Robotics & Mechatronics 0.4.3 — rotor energy and actuator power

Date: 2026-10-10. Codex expanded the original week-7 reading and added separate numerical checks. The same AI assistant authored the reading and tests, so these checks are not independent academic or human review. The course remains **partial, unreviewed and formative-only**.

## Scope

The reading distinguishes kinematics from dynamics, introduces the fixed-axis rotor model with its stated assumptions, relates torque, work, angular speed and power, and checks a gearbox's torque/speed tradeoff against efficiency. It explicitly limits the single-rotor example and points to the later multijoint model. Existing practice questions, keys and objectives are unchanged. The course advances from 0.4.2 to 0.4.3; one compact legacy reading remains.

## Numerical checks

For $I=0.02$ kg·m², $τ=0.10$ N·m, $ω_0=2$ rad/s and 0.40 s, angular acceleration is 5 rad/s², final speed is 4 rad/s, and displacement is 1.2 rad. Net work and kinetic-energy change both equal 0.12 J. A separate 20:1, 80%-efficient gearbox maps 0.10 N·m at 20 rad/s to 1.6 N·m at 1 rad/s, reducing mechanical power from 2.0 W to 1.6 W.

The regression checks the energy balance, gearbox power balance, version and formative/unreviewed status. These are equation checks on constructed values, not actuator-sizing or safety validation.
