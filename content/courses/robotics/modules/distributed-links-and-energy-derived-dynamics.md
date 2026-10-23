# Distributed links and energy-derived dynamics

The earlier dynamics reading uses massless links with point masses at the elbow and tool. That model is inspectable and useful, but a rod's center-of-mass motion and rotation contribute different inertia. This original foundation derives a separate distributed-link model from kinetic and potential energy. It does not silently replace the earlier point-mass parameters or claim either construction describes a physical robot.

## Define the bodies and coordinates

Use a vertical-plane two-link arm. Shoulder angle q1 is measured from horizontal; elbow angle q2 is relative to link one. Body one has length L1, mass m1, center distance r1 from its shoulder and center-of-mass rotational inertia I1. Body two has corresponding L2,m2,r2,I2. Its absolute angular rate is v1+v2, while body one's is v1.

The center positions are r1 e(q1) and L1 e(q1)+r2 e(q1+q2), where e(theta)=(cos theta,sin theta). Differentiate these positions to obtain center velocities. Total kinetic energy is the sum of one-half mass times center-speed squared and one-half center inertia times angular-rate squared for each body. Do not add a full pivot inertia on top of the center translation; that would count the parallel-axis contribution twice.

Collecting K=one-half v'Mv gives

$$M_{11}=m_1r_1^2+I_1+m_2(L_1^2+r_2^2+2L_1r_2\cos q_2)+I_2,$$
$$M_{12}=M_{21}=m_2(r_2^2+L_1r_2\cos q_2)+I_2,\qquad M_{22}=m_2r_2^2+I_2.$$

With downward gravity of magnitude g, potential energy is U=(m1 r1+m2 L1)g sin q1+m2 r2 g sin(q1+q2). Its gradient G is compensation torque, opposite the generalized gravitational force.

## A normalized physical-unit example

Choose two uniform rods, each one meter long and one kilogram, with centers at one half meter and center inertias 1/12 kg m². Stipulate g=1 m/s² as an invented teaching gravity, rather than Earth's gravity. The entries become M11=5/3+cos q2, M12=1/3+(cos q2)/2 and M22=1/3, in kg m². Potential is 1.5 sin q1+0.5 sin(q1+q2) joules.

Euler–Lagrange equations d/dt(partial K/partial vi)−partial K/partial qi+partial U/partial qi=taui yield M a+h+G=tau. For these rods,

$$h_1=-\tfrac12\sin q_2(2v_1v_2+v_2^2),\qquad h_2=\tfrac12\sin q_2v_1^2.$$

Derive these terms through the original energy derivatives. They differ from a point-mass construction even if the lengths and total masses happen to match. Nonzero velocities can make h important when acceleration is small.

## Worked nonzero-rate torque

At q=(0,pi/2), v=(1,2) rad/s and requested acceleration (1,0) rad/s², M has rows (5/3,1/3) and (1/3,1/3). Velocity terms are (-4,0.5) N m and G=(1.5,0) N m. Adding all signed contributions gives torque (-5/6,5/6) N m.

The negative shoulder torque is consistent with the supplied moving state; replacing every contribution with a positive magnitude would solve a different question. Kinetic energy is 13/6 J and potential is 0.5 J at this instant. A static holding calculation would omit both the inertial and velocity terms.

## Distinct rehearsal and a singular endpoint map

At q=(pi/2,0) and v=(1,-1), the matrix has entries 8/3,5/6,1/3. Its determinant is 7/36 and kinetic energy is 2/3 J. Potential is two joules. The endpoint Jacobian is singular at the straight posture, but the distributed bodies still have a positive-definite joint inertia. Endpoint position rank and joint kinetic energy describe different maps.

For a separate rehearsal point set q=(0,pi/2),v=(1,-1),a=(0,2). Here h=(0.5,0.5), G=(1.5,0), giving torque (8/3,7/6) N m. Keep these states distinct; carrying the preceding posture into this calculation changes the matrix and gravity.

For the uniform-rod model, direct expansion gives determinant 4/9−cos²(q2)/4. It is at least 7/36 because cos² never exceeds one, while M11 is at least two thirds. These inequalities establish positive definiteness at every posture of the ideal model, rather than only at the two displayed configurations. They also make a useful implementation check when evaluating a long trajectory. A computed negative determinant under these parameters indicates a formula, unit or numerical error. Real hardware could still require a different model; mathematical positivity does not identify its actual inertia.

## Close an energy ledger

Differentiating K gives v'Ma plus one-half v'Mdot v. The derived h satisfies v'h=one-half v'Mdot v, so actuator power tau'v equals d(K+U)/dt without friction or external forces. Verify the identity symbolically and with a numerical trajectory under refinement. Power can be positive or negative; signed net work differs from a sum of absolute torque magnitudes.

[MIT OCW 2.12 Fall 2005 syllabus/calendar](https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/pages/syllabus/) lectures 17–19 and the [Modern Robotics mass-matrix supplement](https://modernrobotics.northwestern.edu/nu-gm-book-resource/8-1-3-understanding-the-mass-matrix/) are link-only scope/concept references. All derivations and values are original and AI-assisted; no source example or diagram is imported. Friction, rotor/drivetrain coupling, flexible bodies and real identification remain omitted. The package stays partial and unreviewed.
