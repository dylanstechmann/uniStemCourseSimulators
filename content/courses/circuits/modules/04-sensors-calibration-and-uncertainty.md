# Sensors, calibration, and uncertainty

A sensor converts a physical quantity into an electrical output through a transfer function. Calibration estimates that mapping using references with known values; validation asks whether the mapping remains useful for the intended samples, range and conditions. A calibration curve is conditional on its domain, model and reference uncertainty. It does not by itself prove accuracy in a new environment.

## Invert an affine calibration only within its range

For a linear sensor model $V=b+Gx$, $b$ is the offset and $G$ is sensitivity in volts per unit of $x$. Recover the measurand with $x=(V-b)/G$. Keep the offset and slope units visible, use unsaturated calibration points, and report the range over which the fit was checked. Hysteresis, drift, cross-sensitivity, temperature, mounting and nonlinear response can make one affine curve inadequate.

For the constructed calibration $V=0.50x+0.10$ V, a measured $V=2.10$ V gives $x=(2.10-0.10)/0.50=4$ units. If only the voltage reading has standard uncertainty $u_V=0.02$ V and the fitted calibration is treated as exact, first-order propagation gives $u_x=u_V/|G|=0.04$ units. This uncertainty statement is conditional: uncertainty in the reference values, fitted offset or slope would add terms.

For independent small uncertainties in $V$, $b$ and $G$, differentiation gives

$$
u_x^2\approx\left(\frac{u_V}{G}\right)^2+
\left(\frac{u_b}{G}\right)^2+
\left(\frac{(V-b)u_G}{G^2}\right)^2.
$$

If inputs are correlated, covariance terms must be included; treating correlated errors as independent can overstate or understate the result. The approximation also assumes the local linear model is suitable and the uncertainties are small enough for first-order propagation.

## Propagate uncertainty through a calculation

For a derived quantity $y=f(a,b)$ with independent small standard uncertainties, first-order propagation is

$$
u_y^2\approx\left(\frac{\partial f}{\partial a}u_a\right)^2+
\left(\frac{\partial f}{\partial b}u_b\right)^2.
$$

For $V=IR$ with independent $I=2.00\pm0.02$ A and $R=10.0\pm0.1$ Ω, the value is 20.0 V and

$$
u_V=\sqrt{(R u_I)^2+(I u_R)^2}
=\sqrt{0.20^2+0.20^2}\approx0.283\text{ V}.
$$

These are standard uncertainties under the stated independence assumption, not guaranteed bounds. Resolution, repeatability, standard uncertainty and a chosen confidence interval describe different evidence and should be named rather than combined informally.

## Keep calibration evidence traceable

Record the reference values and uncertainties, instrument identity, calibration date, units, temperature and range, fit method, residuals and any excluded or clipped points. Use separate validation evidence to check performance under intended operating conditions. A high-resolution display does not remove offset, drift, hysteresis or calibration uncertainty, and extrapolating beyond tested references is not validated by a small residual inside the fitted range.

The calculations here use constructed sensor values. They establish no real sensor specification, biological measurement, traceable reference chain or experimental procedure. The later channel-diagnostic lesson examines clipping and common-mode evidence under its own explicitly synthetic model.
