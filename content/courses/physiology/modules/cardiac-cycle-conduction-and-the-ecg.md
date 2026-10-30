# The cardiac cycle and the ECG: valve logic, filling time, conduction and the cardiac dipole

The heart is both an electrical conductor and a pump, and the two are timed against each other. Valves open and close because of pressure differences, so the order of events follows from simple logic. How long the ventricle has to fill sets how much it can eject. An electrical wave crosses tissues with very different conduction speeds, and the delays it accumulates are what a surface recording measures. This lesson works these ideas through with synthetic numbers. It extends the [pressure–volume loop and pump work](10-hemodynamics-pressure-flow-resistance-compliance.md) of the hemodynamics lesson by adding time, and the [length-constant and conduction ideas](15-passive-membrane-and-cable-properties.md) of the cable lesson by applying them to a tissue with a built-in delay.

## Learning objectives

By the end of this lesson, you should be able to:

1. Assign the phase of the cardiac cycle from chamber and aortic pressures using valve logic, and compute stroke volume and ejection fraction from end-diastolic and end-systolic volumes.
2. Use a stipulated filling model to show how heart rate shortens diastole more than systole, why cardiac output can peak and then fall as rate rises, and how a stiffer ventricle changes the result.
3. Compute conduction delays from distance and velocity and a pacemaker rate from the slope of diastolic depolarization.
4. Project a cardiac vector onto the limb-lead axes, apply Einthoven's law, recover the vector's size and angle from two leads, and state what the dipole model leaves out.

## Valve logic and the four phases

Heart valves have no muscle of their own. A valve is open when the pressure upstream exceeds the pressure downstream and closed otherwise. For the left ventricle (LV), the mitral valve separates it from the left atrium (LA) and the aortic valve from the aorta (Ao). That gives four phases:

| Phase | Mitral valve | Aortic valve | LV volume |
| --- | --- | --- | --- |
| Filling | open (P_LA > P_LV) | closed | rises |
| Isovolumic contraction | closed | closed (P_Ao > P_LV) | constant |
| Ejection | closed | open (P_LV > P_Ao) | falls |
| Isovolumic relaxation | closed | closed | constant |

Take three synthetic instants with pressures in mmHg. At P_LV = 5, P_LA = 8, P_Ao = 80 the mitral valve is open and the aortic is closed, so the ventricle is filling. At P_LV = 60, P_LA = 8, P_Ao = 100 both valves are closed, so volume cannot change; because the ventricle has just ejected and pressure is falling, this is isovolumic relaxation. At P_LV = 118, P_Ao = 116 the aortic valve is open and the ventricle is ejecting. Pressure alone cannot separate isovolumic contraction from isovolumic relaxation, because both have both valves closed. The direction in which pressure is changing, or the point in the cycle, decides which.

The stroke volume is **SV = EDV − ESV** and the **ejection fraction** is EF = SV/EDV. For EDV = 120 mL and ESV = 50 mL, SV = 70 mL and EF = 70/120 = 0.583.

## How heart rate trades filling time

The cycle length is T = 60/HR seconds. As rate rises, T shrinks, but the contraction phase shortens by less than the whole cycle, so diastole takes most of the loss. As a stipulated teaching model, let systole last **t_sys = 0.15 + 0.2 T** seconds and diastole **t_dia = T − t_sys = 0.8 T − 0.15**. At 60 beats per minute, T = 1.00 s, t_sys = 0.35 s and t_dia = 0.65 s. At 120, T = 0.50 s, t_sys = 0.25 s and t_dia = 0.25 s. Doubling the rate cut systole by 29% and diastole by 62%.

Filling takes time. Model the ventricle as filling toward a ceiling volume V∞ = 130 mL with time constant τ = 0.25 s, starting from ESV = 50 mL, and assume that ejection always returns it to the same ESV:

**EDV = V∞ − (V∞ − ESV) e^(−t_dia/τ),  SV = EDV − ESV,  CO = HR × SV.**

| Heart rate | t_dia (s) | EDV (mL) | SV (mL) | CO (L/min) |
| --- | --- | --- | --- | --- |
| 60 | 0.650 | 124.1 | 74.1 | 4.44 |
| 75 | 0.490 | 118.7 | 68.7 | 5.15 |
| 120 | 0.250 | 100.6 | 50.6 | 6.07 |
| 150 | 0.170 | 89.5 | 39.5 | 5.92 |
| 180 | 0.117 | 79.8 | 29.8 | 5.37 |

Stroke volume falls steadily as rate rises, because less time is left to fill, but output rises at first because the rate rises faster than the stroke volume falls. In this model output peaks near 126 beats per minute at about 6.08 L/min and then declines. That peak, and every number around it, belongs to the invented parameters; it shows a mechanism, a finite filling time, not a measurement.

**A stiffer ventricle.** Suppose the ventricle fills more slowly, with τ = 0.40 s and all else unchanged. At 75 per minute, SV becomes 56.5 mL and CO 4.24 L/min, against 68.7 mL and 5.15. At 120 per minute, CO is 4.46 L/min against 6.07. Slower filling costs more at high rates, where diastole is short, so reserve is lost exactly where it would be used. This is the logic of [compensation and reserve](14-compensation-and-reserve.md): a resting value hides a lost capacity that only a stress would reveal. General textbook statements that ventricular filling slows on average with age belong to that discussion; no age-related figure is cited or used here.

## Pacemaker rate and conduction delays

Pacemaker cells have no stable resting potential. After each action potential they depolarize slowly (phase 4) until they reach threshold. If phase 4 begins at −60 mV, threshold is −40 mV and the slope is 25 mV/s, the interval is 20/25 = 0.80 s, or 75 beats per minute. Raising the slope to 30 mV/s shortens it to 0.667 s and raises the rate to 90; the slope needed for 100 per minute is 20/0.60 = 33.3 mV/s. A less negative threshold or a lower slope slows the rate. The model ignores the action potential's own duration, which is small beside phase 4.

Once the wave is launched, it crosses tissues at different speeds. The time to cross a segment of length d at conduction velocity v is **t = d / v**. In a stipulated example, the atria are crossed over 0.05 m at 1.0 m/s (0.050 s), the atrioventricular (AV) node over 0.005 m at 0.05 m/s (0.100 s) and the His–Purkinje system over 0.04 m at 3.0 m/s (0.013 s), for a total of 0.163 s. The node is the shortest segment and contributes most of the delay. That is its function: it lets atrial contraction finish filling the ventricle before the ventricle contracts. If the nodal velocity falls to 0.04 m/s, the node's delay becomes 0.125 s and the total rises to 0.188 s. Slow conduction in the node reflects small cells with weak electrical coupling, the cable idea of high axial resistance and low length constant.

## The ECG as a dipole projection

During depolarization the active tissue forms a moving boundary between depolarized and resting cells, and the net current is often summarized as a single vector **p**, the cardiac dipole (see the [dipole lesson](../../physics-em/modules/24-electric-dipoles-fields-torque-energy-and-force.md) in Physics II). A surface lead records the component of **p** along its axis, a projection as in the [orthogonality and projections lesson](../../linear-algebra/modules/08-orthogonality-projections-and-qr.md) of linear algebra.

The three standard limb leads are differences of potentials at the right arm, left arm and left leg: I = V_LA − V_RA, II = V_LL − V_RA and III = V_LL − V_LA. In the usual frontal-plane convention their axes point at 0°, +60° and +120°. For a vector of size p at angle θ,

**I = p cos θ,  II = p cos(θ − 60°),  III = p cos(θ − 120°).**

Because II = (V_LL − V_LA) + (V_LA − V_RA), **Einthoven's law** holds exactly: **II = I + III**.

*Example.* A vector of 1.2 mV at θ = 60° gives I = 0.6, II = 1.2 and III = 0.6 mV, and indeed 1.2 = 0.6 + 0.6. A vector at 90° is perpendicular to lead I, so lead I records zero while II and III record 0.866 p.

*Recovering the vector.* Two leads determine the vector. From p cos θ = I and p cos(θ − 60°) = II one finds p sin θ = (2 II − I)/√3. For I = 0.8 mV and II = 1.0 mV, p sin θ = 0.693 and p cos θ = 0.800, so θ = 40.9° and p = 1.06 mV, and lead III is II − I = 0.2 mV, which agrees with 1.06 cos(−79.1°) = 0.200.

The intervals on a recording are the timing of the previous sections made visible. The P wave is atrial depolarization, the PR interval includes the nodal delay, the QRS complex is ventricular depolarization and the T wave is ventricular repolarization. Heart rate is 60 divided by the R–R interval in seconds, so R–R = 0.75 s gives 80 per minute.

## Common mistakes

- Reading pressure alone as enough to separate isovolumic contraction from relaxation.
- Expecting cardiac output to rise without limit as heart rate rises.
- Forgetting that diastole, not systole, absorbs most of the shortening of the cycle.
- Attributing the AV delay to a long path, when it is a slow velocity over a short path.
- Treating the three limb leads as independent measurements, when II = I + III.
- Reading a lead's amplitude as the size of the vector, without its angle.

## Worked example

**Problem.** In the filling model (V∞ = 130 mL, ESV = 50 mL, τ = 0.25 s), what are the diastolic time, stroke volume and cardiac output at 90 beats per minute, and what would a stiffer ventricle (τ = 0.40 s) do to the output?

**Step 1: timing.** T = 60/90 = 0.667 s, t_sys = 0.15 + 0.2 × 0.667 = 0.283 s and t_dia = 0.383 s.

**Step 2: volume.** EDV = 130 − 80 e^(−0.383/0.25) = 130 − 80 × 0.216 = 112.7 mL, so SV = 62.7 mL.

**Step 3: output.** CO = 90 × 62.7 = 5.65 L/min.

**Step 4: stiffer ventricle.** With τ = 0.40 s, e^(−0.383/0.40) = 0.384, EDV = 130 − 80 × 0.384 = 99.3 mL, SV = 49.3 mL and CO = 4.44 L/min, a loss of about 21%. The same input gives less output because the filling time constant, not the rate, changed.

## Limits of this lesson

All values are synthetic and round. Valves are treated as ideal on-off switches without inertia, the filling model has one lumped time constant and ignores atrial contraction and the ventricle's pressure–volume relation, and systole is stipulated, not derived. The conduction speeds are invented round values of plausible order, not measurements. The dipole model replaces a three-dimensional, time-varying source in a conducting torso by one frontal-plane vector with equilateral lead axes, and it describes the geometry of a recording, not the interpretation of any recording from a person. The lesson gives no medical advice.
