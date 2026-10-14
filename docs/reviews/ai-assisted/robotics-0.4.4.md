# Robotics & Mechatronics 0.4.4 — planning and closed-loop execution

Date: 2026-10-10. Codex expanded the original week-12 planning and feedback reading and added a numerical regression. The same AI assistant authored the reading and test, so these checks are not independent academic, engineering or human review. The course remains **partial, unreviewed and formative-only**.

## Scope

The lesson distinguishes a geometric path from its time scaling, discusses frame and sensing uncertainty, and works through a deliberately static biased-measurement feedback example. It qualifies the example against delay, noise, saturation and dynamics, and states that recovery limits depend on the mechanism and risk analysis. Existing practice questions, keys and objectives are unchanged. All scheduled lessons now have expanded or original instructional text; the synthetic lab, missing workload evidence and human review remain unresolved.

## Numerical checks

For the constructed model $y_k=u_k+0.1$, target $r=1$, initial command $u_0=0$ and gain $K=0.5$, successive residuals are 0.9, 0.45 and 0.225. The corresponding commands are 0, 0.45 and 0.675. The regression recomputes these values and checks the lesson's path/time-scaling and dynamic-limit language. This scalar arithmetic is not a controller stability or safety validation.
