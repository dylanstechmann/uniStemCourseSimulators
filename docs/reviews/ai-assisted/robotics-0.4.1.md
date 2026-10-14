# Robotics & Mechatronics 0.4.1 — frame transforms and conventions

Date: 2026-10-10. Codex expanded the original week-1 reading and added independent matrix calculations to the regression suite. The same AI assistant authored the lesson and tests, so these checks are not independent academic or human review. The course remains **partial, unreviewed and formative-only**.

## Scope

The reading now defines a labeled planar transform with column vectors, demonstrates rotation plus translation, gives composition and inverse rules, and lists consistency checks. It distinguishes frame-coordinate conversion from applying active operations in the opposite order. Existing practice questions, keys and objectives are unchanged. The course advances from 0.4.0 to 0.4.1; three compact legacy readings remain.

## Numerical checks

For a 90° counterclockwise frame orientation and world origin (2,1) m, the point (1,0) m in frame B maps to (2,2) m in W. Subtracting the frame origin and applying the inverse rotation recovers (1,0). Applying translation then rotation about the fixed world origin instead yields (−1,3), confirming the operations differ. The rotation preserves the tested basis vectors and has determinant +1.

The focused test also checks the course version and partial/unreviewed/formative labels. These checks do not validate a particular robot, calibration, safety function, full course or workload.
