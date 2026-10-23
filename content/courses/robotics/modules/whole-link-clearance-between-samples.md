# Whole-link clearance between sampled poses

The inverse-branch reading checks link-to-obstacle distance, and the time-scaling reading warns that finite samples can miss a collision. This foundation derives a conditional continuous bound from a velocity limit that holds throughout each interval. It also constructs a path whose endpoints are clear while its middle overlaps an obstacle. The result is a mathematical statement about supplied geometry and bounds, not a validated protective function or permission to operate a machine.

## Bound every modeled link point

For a planar arm, link-one endpoint is L1 e(q1), and a point on link two is L1 e(q1)+s L2 e(q1+q2), with fixed material coordinate 0<=s<=1. If absolute joint rates are bounded globally by w1 and w2, differentiating this position and using the triangle inequality gives

$$V=L_1w_1+L_2(w_1+w_2)$$

as a speed bound for all centerline points on both links. The link-one bound L1 w1 is no larger. Fixed-radius capsule geometry can use the same centerline distance bound against fixed obstacles. A tool extending beyond the modeled second link needs its own enclosure or additional term.

The rate bounds must hold between samples. The largest measured sampled rate does not establish a global bound, and tool speed alone need not bound every elbow/link point. Joint limits and angle wrapping must respect the same physical coordinates used in the path.

## From motion to clearance

Distance from a point to a fixed closed obstacle is one-Lipschitz: moving the point by at most d changes its distance by at most d. Applying the same bound to matched points along a moving segment and then minimizing over the segment gives a V-Lipschitz centerline distance. Subtracting fixed obstacle and link radii preserves that bound for the signed separation expression used here.

Use a time grid including both endpoints, with largest gap Delta. Every time is within Delta/2 of at least one checked grid point. If minimum sampled clearance is cmin and delta bounds additional geometric/location error deterministically, then

$$c(t)\geq c_{min}-V\Delta/2-\delta.$$

A strictly positive right side establishes separation for the declared model under those bounds. A nonpositive lower bound is inconclusive; it does not establish that a collision occurred. Zero lower bound also fails to establish strict separation. One standard deviation is not automatically a deterministic delta.

## Worked certificate and distinct rehearsal

For a worked arm let L1=0.4 m,L2=0.3 m,w1=0.5 rad/s,w2=0.8 rad/s. The all-link speed bound is 0.59 m/s. With maximum gap 0.1 s, sampled clearance 0.06 m and deterministic error allowance 0.01 m, the lower bound is 0.0205 m. The maximum gap must be strictly less than 2(0.06−0.01)/0.59, about 0.16949153 s, to certify strictly positive separation with those other inputs.

For the distinct rehearsal use L1=0.3,L2=0.2,w1=0.4,w2=0.6 in the corresponding units. Then V=0.32 m/s. At gap 0.2 s the between-sample allowance is 0.032 m. With cmin=0.05 m and delta=0.005 m, the certified lower bound is 0.013 m, and the strict gap threshold is 0.28125 s.

## Clear endpoints can conceal overlap

Use a separate straight arm with both links 0.25 m and q2=0. Rotate q1 continuously from zero to pi/2. Place a disk obstacle at (0.25,0.25) m, radius 0.03 m, and use link radius 0.01 m. At each endpoint configuration the center-to-segment distance is 0.25 m, giving clearance 0.21 m.

At q1=pi/4 the obstacle center lies on the second-link segment. Signed clearance is -0.04 m. The tool's endpoints and the whole-link start/end checks therefore do not certify the swept path. Slowing that same geometric motion cannot remove the overlap, although a tighter sampling grid may reveal it.

## Convert a stated angular bound carefully

For deterministic joint-angle errors bounded by d1,d2 radians, the unit-vector inequality |e(theta+error)−e(theta)|<=|error| gives position bound (L1+L2)d1+L2 d2 for all modeled link points. This inequality does not require calling the angular errors normally distributed or treating a standard uncertainty as a hard maximum.

In the rehearsal, d1=0.01 and d2=0.02 give 0.009 m. If that replaces the earlier delta=0.005 allowance, the lower bound becomes 0.009 m. Do not add both allowances unless they represent separate justified error sources. Unbounded calibration uncertainty leaves a conditional numerical result rather than a deterministic physical claim.

## Retain the proof inputs

A report needs the full geometry, collision routine, continuous rate bound, largest time gap, every sampled clearance and the provenance of delta. Check zero-length segments and clamped projection parameters. [Modern Robotics 10.2.1 C-Space Obstacles](https://modernrobotics.northwestern.edu/nu-gm-book-resource/10-2-c-space-obstacles/) supplies link-only geometry/planning context; the bound and counterexample here are original and AI-assisted. No source shape, figure, path or code is imported. General planning, moving obstacles, deformation and physical safety validation remain open; the package stays partial and unreviewed.
