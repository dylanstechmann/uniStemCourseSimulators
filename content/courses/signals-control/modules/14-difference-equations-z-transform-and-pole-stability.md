# Difference equations, the Z-transform, and discrete pole stability

A sampled controller and plant evolve one step at a time. A difference equation describes that update directly; its impulse response shows what the system does to a one-sample input; and the Z-transform turns repeated updates into an algebraic transfer function. For a causal, finite-order linear time-invariant (LTI) system, the poles of that transfer function reveal whether the natural response decays. This lesson develops the connection for a first-order model, then uses it to analyze a simple feedback loop. All numerical values are synthetic.

## Start with the recurrence

Let input $x[k]$ and output $y[k]$ be related by

$$y[k] = a y[k-1] + b x[k], \qquad k \geq 0,$$

with an initially resting system $y[-1]=0$. The coefficient $a$ weights the stored previous output, while $b$ weights the current input. Both are dimensionless if input and output use the same units; otherwise $b$ carries output-per-input units. The equation is a discrete-time model: $k$ counts samples and $T$ is the elapsed time per sample.

For $a=0.8$, $b=0.2$, and a unit-step input $x[k]=1$, calculate each sample rather than guessing the final value:

| Sample | Calculation | Output |
| --- | --- | ---: |
| $k=0$ | $0.8(0)+0.2(1)$ | 0.2000 |
| $k=1$ | $0.8(0.2000)+0.2(1)$ | 0.3600 |
| $k=2$ | $0.8(0.3600)+0.2(1)$ | 0.4880 |
| $k=3$ | $0.8(0.4880)+0.2(1)$ | 0.5904 |

The output approaches one because the steady value satisfies $y=a y+b$, or $y=b/(1-a)=1$. For $|a|<1$ the step response has the closed form

$$y[k] = \frac{b}{1-a}\left(1-a^{k+1}\right).$$

Here $y[9]=1-0.8^{10}=0.8926$. A pole near one therefore gives a slow decay in sample time. If $a$ is negative but its magnitude is below one, the natural response alternates sign as it decays.

## The impulse response and transfer function

Apply a unit impulse, $x[0]=1$ and $x[k]=0$ for later samples. Starting from rest, $y[0]=b$, $y[1]=ab$, and each later sample is multiplied by $a$. Thus

$$h[k] = b a^k, \qquad k\geq 0.$$

For the example, the impulse response begins $0.2, 0.16, 0.128, 0.1024,\ldots$. The sum is $b/(1-a)=1$, matching the system's steady response to a unit step.

Define the one-sided Z-transform by $X(z)=\sum_{k=0}^{\infty}x[k]z^{-k}$. With zero initial condition, the transform of the recurrence gives

$$Y(z)=a z^{-1}Y(z)+bX(z), \qquad H(z)=\frac{Y(z)}{X(z)}=\frac{b}{1-a z^{-1}}.$$

This is the transfer function from input to output under the zero-initial-condition assumption. It has a pole at $z=a$, and its causal region of convergence is $|z|>|a|$. The impulse response, transfer function and recurrence are three representations of the same LTI system. Nonzero initial conditions add a natural-response term to $Y(z)$; they do not change the system's pole.

## Read stability from the pole

With zero input, the recurrence becomes $y[k]=a y[k-1]$, so $y[k]=a^{k+1}y[-1]$. The natural response decays to zero when $|a|<1$, persists at $|a|=1$ for a simple pole, and grows when $|a|>1$. For a higher-order causal LTI system, every natural mode decays only when all poles lie strictly inside the unit circle. Repeated poles on the boundary require additional care because their responses can grow polynomially.

| Pole $a$ | Natural response | Interpretation |
| ---: | --- | --- |
| $0.8$ | positive and decaying | stable, nonalternating mode |
| $-0.7$ | alternating sign and decaying | stable, oscillatory mode |
| $1.02$ | increasing positive magnitude | unstable mode |

For the first-order plant in the previous sampled-implementation lesson, $a=e^{-T/\tau}$. With a positive time constant and a positive sampling period this exact first-order model has $0<a<1$. The value of $a$ says how much of the previous output remains after one sample. Other difference equations, controller updates or approximations can have different poles, so their stability must be checked rather than assumed from the continuous plant.

## A proportional feedback example

Use the synthetic plant $P(z)=0.2/(1-0.8z^{-1})$ with a proportional controller $K_c=2$ and unity negative feedback. The closed-loop transfer function is

$$T(z)=\frac{K_cP(z)}{1+K_cP(z)}=\frac{0.4}{1.4-0.8z^{-1}}=\frac{2/7}{1-(4/7)z^{-1}}.$$

Its closed-loop pole is $z=4/7\approx0.571$, inside the unit circle, so this ideal linear model predicts a decaying response. This check says nothing about actuator saturation, quantization, unmodeled delay, noise or whether the model describes a real process. It also does not replace the existing course lessons on sampling, frequency response, margins and implementation constraints.

## Common mistakes

- Treating sample index $k$ as time in seconds without multiplying by the sampling period.
- Omitting the zero-initial-condition assumption when forming a transfer function.
- Confusing the pole $a$ with the steady-state gain $b/(1-a)$.
- Declaring a negative pole unstable even when its magnitude is below one.
- Checking only the open-loop plant pole and ignoring the closed-loop poles after feedback.
- Treating a stable linear recurrence as proof that a saturated or delayed implementation is safe.

## Worked example

**Problem.** A synthetic system follows $y[k]=0.75y[k-1]+0.25x[k]$ from rest. Find the first four outputs to a unit step, its impulse response, transfer function and stability classification.

**Step 1: step response.** The outputs at $k=0,1,2,3$ are $0.25$, $0.4375$, $0.578125$ and $0.683594$.

**Step 2: impulse response.** $h[k]=0.25(0.75)^k$, so its first values are $0.25$, $0.1875$ and $0.140625$.

**Step 3: transform.** $H(z)=0.25/(1-0.75z^{-1})$, with a pole at $z=0.75$.

**Step 4: stability.** Since $|0.75|<1$, the natural response decays. The step tends to $0.25/(1-0.75)=1$.

## Limits and course comparison

The derivation covers a first-order causal LTI recurrence and one proportional feedback example. It does not develop general Fourier analysis, discrete frequency response, the full set of transform properties, controller synthesis, quantization, or nonlinear and switched systems. MIT OpenCourseWare's undergraduate [6.003 Signals and Systems (Fall 2011) calendar](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/pages/calendar/) places discrete-time systems, feedback/poles and the Z-transform in its early sequence; its [Lecture 5: Z transform](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/resources/lecture-5-z-transform/) connects the unit-sample response with the system function. The related [2.004 Dynamics and Control II (Spring 2008) calendar](https://www.ocw.mit.edu/courses/2-004-dynamics-and-control-ii-spring-2008/pages/calendar/) provides a separate continuous-time control comparator. These links informed scope only; no source text, figure, assessment or data is reproduced.
