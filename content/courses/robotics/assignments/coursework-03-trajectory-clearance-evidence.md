# Assignment 3: trajectory clearance evidence

This open report compares sampled geometric checks with a continuous lower bound under explicit rate and error assumptions. It requires an original collision routine and counterexample analysis rather than only a margin calculation. Every dimension, rate and allowance is stipulated. The result concerns a mathematical model; it does not validate a physical robot, protective function or operating condition. Retain geometry, code, plots and report locally.

## Part A: form a whole-link bound

Use a planar arm with L1=0.5 m,L2=0.25 m and continuous absolute joint-rate bounds w1=0.6 rad/s,w2=0.4 rad/s. Derive the speed bound for any point on either link from its actual material-coordinate position. The all-link bound is V=0.55 m/s.

Suppose the supplied grid includes both trajectory endpoints, has maximum gap 0.1 s and minimum sampled clearance 0.05 m. An independently stipulated deterministic geometry-error allowance is 0.01 m. The nearest-sample motion allowance is V Delta/2=0.0275 m, leaving a lower bound 0.0125 m after the geometry allowance.

State each assumption needed for that lower bound: fixed obstacle geometry, a conservative enclosure of the modeled links, continuous rate bounds, coverage of the full time interval and a justified deterministic error bound. A positive arithmetic result without these assumptions does not certify even the intended mathematical trajectory.

## Part B: replace the error model explicitly

For a separate variant replace the earlier 0.01 m geometry allowance with a bound derived from absolute joint-angle errors d1=0.01 rad,d2=0.02 rad. Use the exact unit-vector difference inequality rather than a small-angle normality assumption.

The resulting whole-link position allowance is (L1+L2)d1+L2 d2=0.0125 m. It replaces the original allowance in this comparison; the lower bound becomes 0.01 m. With the same sampled clearance, strict positive separation requires maximum gap below 2(0.05−0.0125)/0.55, about 0.13636364 s.

At equality the lower bound is zero, which does not establish strict separation. A negative or zero bound is inconclusive rather than proof of collision. Explain why changing the supplied error bound and adding a separate new source of error would be different variants with different ledgers.

## Part C: implement the actual geometry

Represent each finite-radius link as a capsule around its centerline and obstacles as fixed disks in the plane. For each segment and obstacle, compute the clamped closest-point parameter and subtract both radii from the center-to-segment distance. Include a separate zero-length segment rule to avoid division by zero.

Test an interior projection, an endpoint projection and a degenerate segment. Compare selected outputs with direct hand geometry. Checking only the tool or only the elbow does not represent the full link enclosure. A collision routine with very precise coordinates can still omit an entire body.

Construct the foundation's start/end-clear, middle-overlap path with two equal links, then calculate its signed clearance over the path. Relate workspace overlap to the configurations that belong to the obstacle set. Do not confuse two discrete inverse branches with a continuous null direction that automatically avoids an obstacle.

## Part D: sampled evidence and a conditional proof

Evaluate a chosen smooth synthetic joint path on at least two grids. Report sampled minimum clearance, global rate bound, maximum time gap, geometry allowance and the resulting lower bound separately. Refining samples may tighten an inconclusive bound. It cannot remove an actual geometric collision from the same path.

Demonstrate why sampled maximum velocity alone is insufficient by constructing or identifying an intervening speed peak. If an analytic global bound is unavailable, report the remaining gap rather than treating a dense plot as a proof. A different conservative method could be used, but its assumptions and numerical guarantees must be documented.

Compare a slower timing of the same path with a changed path. Slowing changes time-dependent rate and sampling allowances; changing geometry can change collision status. Those are distinct interventions on the mathematical problem. No conclusion about physical stopping performance follows without a separate actuator, delay and environment model.

Retain the complete geometry, tests, path definition, grids, intermediate clearances, error-bound derivation and a text description for each plot. [Modern Robotics 10.2.1 C-Space Obstacles](https://modernrobotics.northwestern.edu/nu-gm-book-resource/10-2-c-space-obstacles/) is link-only scope context. All algorithms, examples and tasks here are original and AI-assisted; no source shape, path, exercise or code is imported. General planning, actual calibration, moving obstacles, measured workload and qualified review remain open; the course stays partial and unreviewed.
