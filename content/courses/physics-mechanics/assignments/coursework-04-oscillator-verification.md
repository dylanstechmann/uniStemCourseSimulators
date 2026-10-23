# Assignment 4: oscillator simulation and model verification

Develop a reproducible simulation study that distinguishes a mechanical energy law from the behavior of a numerical integrator. Use the [oscillation/damping reading](../modules/11-oscillations-damping-and-energy-balance.md), [calibration reading](../modules/13-machine-compliance-calibration-and-model-inference.md) and the numerical-method foundations in the separate Programming course if needed. Save source, tests, results and your report locally. Browser checkpoints assess selected calculations, not implementations, plots, reports or real material behavior.

## Exact unforced reference

Take a stipulated point mass m=1 kg, spring constant k=4 N/m, no damping and no forcing. Initial displacement is x0=0.1 m and initial velocity is zero. Derive the exact displacement and velocity, angular frequency, period and conserved mechanical energy. Verify both initial conditions and the differential equation. Treat x as measured from the supplied equilibrium; adding an extra static gravitational term would change the coordinate model.

Apply one forward-Euler step with h=0.1 s, updating both coordinates from the old state: xnext=x+h v, vnext=v−h(k/m)x. Calculate the state and its mechanical energy. Derive the energy change for an arbitrary current state of this unforced oscillator. Show that the energy is multiplied by 1+omega0²h² per step for this method. A positive numerical energy change in this exact conservative model is a discretization artifact, not evidence of an active spring.

Now use the velocity-first symplectic Euler variant: vnext=v−h(k/m)x, then xnext=x+h vnext. Calculate its first state and energy. The physical energy need not be exactly preserved on each step. Investigate its bounded oscillation at a sufficiently small step and contrast it with forward Euler's secular growth. Derive or numerically verify the linear-update stability boundary, state its restrictions and test a step beyond it. A method name alone does not guarantee stability for every step size.

## Refinement and error evidence

Integrate both methods to t=2 s with at least three steps that divide the final time exactly. Report errors in displacement, velocity and energy relative to the analytic reference. Explain whether phase and energy errors tell the same story. Compare at matched final times, not at whichever grid point lies closest. Define the error norm and retain enough intermediate precision to distinguish rounding from integration error.

Add a midpoint or trapezoidal method if you want a higher-order comparison, but verify its actual order by refinement rather than assuming it from a library label. Test zero initial state and a different amplitude. Under this linear model, doubling initial displacement doubles x and v while multiplying energy by four. Use that scaling as an independent regression check. It does not identify a real material's linear regime.

## A passive damped model

In a separate scenario keep m=1, k=4 and the same initial conditions, but set c=0.4 N s/m. The supplied law is m xddot+c xdot+kx=0. Derive dE/dt=−c v² and the underdamped analytic reference, retaining the sine term required by zero initial velocity. The original [oscillator-reference.csv](oscillator-reference.csv) contains t and x values generated from that exact model, rounded to eight decimal places. It contains synthetic calculation values, not measured independent replicates or noisy observations.

Compare your numerical trajectory with that table and with the unrounded analytic function. Integrate c v² over time and compare it with E0−E(t). Refine both the trajectory step and the dissipation quadrature. Explain why exact instantaneous energy is not generally a single pure exponential even though an oscillation envelope decays exponentially. Show the role of turning points, where v=0 and instantaneous dE/dt=0.

## Calibration and interpretation

Suppose a fictional readout is y=b+g x with unknown offset b and gain g. Explain which features of a release trace can be changed by those observation parameters and which depend on the dynamical law. An amplitude change alone does not uniquely establish a stiffness change. List additional evidence needed to distinguish mass, stiffness, damping, initial state and readout effects. Do not fit a biological diagnosis or material mechanism to this synthetic trace.

## Self-review and completion standard

The undamped angular frequency is two radians per second, with period pi seconds and initial energy 0.02 J. One forward-Euler step gives x=0.1 m, v=−0.04 m/s and energy 0.0208 J. Velocity-first symplectic Euler gives v=−0.04 m/s, x=0.096 m and energy 0.019232 J. The first energy decrease is not physical damping because the declared law has c=0.

For the damped model, the decay parameter is c/(2m)=0.2 s⁻¹ and damped angular frequency is sqrt(3.96) rad/s. Verify your reference function and table comparison independently. A complete study retains tested updates, initial-condition checks, refinement/stability evidence, a dissipation ledger and an observation-model interpretation. This original assignment and synthetic table were developed with substantial AI assistance, with no imported source problem, code or measurements. MIT OCW [8.01SC Fall 2016](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/syllabus/) is the core mechanics scope comparator; the local damping/calibration strand is a selected extension already declared by this package. Qualified review and measured workload remain open; the course remains partial and unreviewed.
