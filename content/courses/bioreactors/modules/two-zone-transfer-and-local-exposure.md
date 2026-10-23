# Two-zone transfer and local exposure

A single well-mixed oxygen balance uses one concentration as both a state and the transfer driving-force reference. That can conceal spatial structure when transfer and consumption occur in different regions. This original two-zone model makes internal exchange explicit, derives steady local states, and shows why a bulk average can pass a threshold while one region fails it. All concentrations, volumes, rates and thresholds are normalized synthetic inputs. They do not specify a vessel, tissue or culture process.

## Declare the two control volumes

Let zone volumes be $V_1,V_2$, with concentrations $C_1,C_2$. A symmetric liquid exchange has volume rate $E$, so its amount flux from one to two is $E(C_1-C_2)$. Each zone has its own transfer rate coefficient $k_j$ and constant consumption per zone volume $u_j$. With a common imposed gas-equilibrium concentration $C^*$, write

$$V_1C_1'=k_1V_1(C^*-C_1)-u_1V_1-E(C_1-C_2),$$

$$V_2C_2'=k_2V_2(C^*-C_2)-u_2V_2+E(C_1-C_2).$$

The exchange appears with equal and opposite amount rates; it does not create oxygen. Dividing each equation by its own volume produces different exchange coefficients if the volumes differ. Using the same concentration-rate coefficient $E/V_1$ in both equations would violate the total ledger unless the volumes are equal.

Adding the equations gives the total liquid-oxygen balance. The volume-weighted mean is $\overline C=(V_1C_1+V_2C_2)/(V_1+V_2)$. Internal exchange cancels, but the external transfer still involves $k_1V_1C_1+k_2V_2C_2$, which cannot generally be replaced by a product of averaged $k$ and averaged $C$. That replacement requires additional assumptions about their spatial relationship.

## Solve a localized-transfer case

Set $k_2=0$, so all external supply occurs in zone one. At steady state, the second equation gives

$$E(C_1-C_2)=u_2V_2.$$

The total balance then gives

$$C_1=C^*-\frac{u_1V_1+u_2V_2}{k_1V_1},\qquad C_2=C_1-\frac{u_2V_2}{E}.$$

Both expressions require positive transfer/exchange coefficients. A negative predicted state invalidates the constant-uptake model there rather than supplying a negative physical concentration. Even when both states are positive, a specified lower admissible concentration can impose a stronger limit than the total supply balance alone.

For the worked case use $V_1=1,V_2=3,k_1=4,C^*=1,u_1=u_2=0.2,E=1$. Total consumption is 0.8. Thus $C_1=0.8$, the interzone gap is 0.6, $C_2=0.2$ and the weighted mean is 0.35. Transfer into zone one is $4(1-0.8)=0.8$, exactly the total consumption. At a lower admissible level 0.3, the mean exceeds the level while zone two does not.

A falsely uniform reduction would use effective coefficient $k_{avg}=1$ and average uptake 0.2, predicting concentration 0.8 everywhere. The real two-zone mean is 0.35; the actual transfer driving force belongs to zone one, not that mean. A closed total ledger alone does not establish local exposure.

## Exchange and capacity answer different questions

In this particular localized-transfer/constant-demand model, raising $E$ does not change $C_1$, because total supply still balances the same total uptake. It does reduce the gap and raise $C_2$. With $E=2$, the gap is 0.3, $C_2=0.5$ and the mean is 0.575. This is an explicitly controlled comparison holding transfer, uptake and volumes fixed; those coefficients need not remain independent in an actual vessel.

For zone two to satisfy $C_2\geq C_{min}$, require $C_1>C_{min}$ and

$$E\geq\frac{u_2V_2}{C_1-C_{min}}.$$

In the worked case with $C_{min}=0.3$, the threshold is $E\geq1.2$. If $C_1$ itself falls below the requested level, no finite positive exchange can solve the supply deficit. Better mixing cannot substitute for missing total oxygen capacity under these fixed assumptions.

## Distinct rehearsal

Use $V_1=V_2=2,k_1=3,k_2=0,C^*=1,u_1=u_2=0.3,E=1.5$. Total demand is 1.2, $C_1=0.8$, gap 0.4, $C_2=0.4$ and mean 0.6. At level 0.5 the bulk average passes while zone two fails. The minimum exchange is $0.6/(0.8-0.5)=2$. With exchange three, $C_2=0.6$ and the mean is 0.7. Reconstruct the two original amount equations rather than checking only their sum.

## Dynamic and evidence checks

Implement the two concentration equations with their separate volume divisions. Track total amount, transfer, demand and the internal exchange residual. Derive the linear system matrix and verify that its stable modes for the selected positive coefficients agree with a numerical transient. Constant uptake can drive a trajectory outside the admissible domain; define a stopping event rather than hiding that failure by clipping concentrations.

A bulk trace alone generally cannot determine every local state, transfer coefficient and uptake. Compare candidate models with a second spatial observation or another justified perturbation; a lower fit residual is not a unique mechanism result. The [MIT OCW 10.442 Spring 2005 calendar](https://ocw.mit.edu/courses/10-442-biochemical-engineering-spring-2005/pages/calendar/) design/mass-transfer/scale-up/scale-down strands are link-only scope comparators. All derivations and tasks are original and AI-assisted. CFD, spatially resolved tissue metabolism, validated exposure limits and actual process design remain outside this model. The course remains partial and unreviewed.
