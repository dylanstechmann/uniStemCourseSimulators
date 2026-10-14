# Homeostasis and feedback

Homeostasis is the regulation of internal conditions within ranges compatible with function. It is dynamic: inputs and outputs continue while stored quantities and regulated variables change. A sensor detects information about a variable, a controller compares it with a reference or operating range, and effectors alter the processes that influence it. This sensor-controller-effector description is a model of organization, not a claim that every physiological system has one fixed setpoint or one central controller.

## Start with a balance

For an amount $A$ in a compartment,

$$
\frac{dA}{dt}=\text{rate in}-\text{rate out}.
$$

At steady state, the two rates balance and the amount is constant. A steady state does not require zero flow; continuous input can be balanced by continuous removal. If the rates depend on the state, a perturbation can create a restoring change in the net balance. Units help expose mistakes: a rate in µmol/min divided by a volume in L gives a concentration rate in µmol·L$^{-1}$·min$^{-1}$.

For a constructed well-mixed compartment with volume $V$, solute input rate $r$, and first-order clearance constant $k$, concentration follows

$$
\frac{dC}{dt}=\frac{r}{V}-kC.
$$

Setting the derivative to zero gives $C^*=r/(kV)$. With $r=12$ µmol/min, $V=2$ L and $k=0.3$ min$^{-1}$, the equilibrium is 20 µmol/L. At $C=30$ µmol/L, removal is $kVC=18$ µmol/min, greater than the 12 µmol/min input, so concentration falls. At $C=10$ µmol/L, removal is 6 µmol/min and concentration rises. The state-dependent removal opposes deviations around this equilibrium.

## Feedback direction and response time

Negative feedback reduces a deviation: a rise in the regulated variable evokes a response that tends to lower it, or a fall evokes a response that tends to raise it. Positive feedback amplifies a change; it may be useful for a process that must proceed decisively, but it needs a terminating event or constraint. The sign is defined by the direction of the response relative to the initial deviation, not by whether a hormone, nerve or organ is involved.

For the simple clearance model, a deviation $\delta C=C-C^*$ obeys $d(\delta C)/dt=-k\delta C$, so it decays as $e^{-kt}$. The response time scale is $\tau=1/k=3.33$ min for $k=0.3$ min$^{-1}$. After one time constant, about 36.8% of the initial deviation remains. This is a property of this first-order model, not a universal physiological response time.

Homeostatic regulation can preserve a measured variable while changing control effort. For example, if a system can increase removal to offset a larger input, the measured concentration may stay near its reference while the effector operates harder. A normal value alone therefore does not reveal reserve or the effort required to maintain it. Compensation can also be incomplete, delayed or limited by capacity. Later lessons distinguish steady-state balance, feedback gain, transport and physiological reserve using separate constructed models.

All values here are synthetic teaching examples. The one-compartment equation omits distribution, multiple pathways, saturable transport and measurement uncertainty. It gives no medical advice and describes no real person's health.
