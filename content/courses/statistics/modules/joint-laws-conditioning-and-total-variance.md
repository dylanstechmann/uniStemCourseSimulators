# Joint laws, conditioning and total variance

A marginal distribution describes one random quantity. A joint law describes which combinations can occur and how probability is distributed among them. It supplies the information needed for conditional prediction, covariance and dependence. Separate marginal means and standard deviations do not determine that law. This original foundation extends the introductory probability reading from event denominators to explicit discrete and continuous joint models.

## A discrete dependence that correlation misses

Let X take -1, 0 and 1 with equal probabilities, and set Y=X². The possible pairs are (-1,1), (0,0) and (1,1), each with probability one third. Thus E[X]=0, E[Y]=2/3, Var(X)=2/3 and Var(Y)=2/9. Because XY=X³ has zero mean, Cov(X,Y)=E[XY]−E[X]E[Y]=0. Both variances are positive, so correlation is also zero.

Nevertheless X and Y are dependent: knowing Y=0 identifies X=0 with certainty, whereas its marginal probability is one third. Independence would require the full joint probabilities to factor into the corresponding marginals. Zero covariance controls one weighted product average; it does not impose that factorization. A scatter plot here has a deterministic curved relation even though the linear correlation vanishes.

## A continuous rehearsal with a declared support

For a distinct model stipulate joint density f(x,y)=2 on the triangle 0<y<x<1 and zero elsewhere. Its normalization is the integral of two over a triangle of area one half. A density value can exceed one; interval or region probabilities, obtained by integrating it, remain between zero and one.

Integrate over the coordinates actually allowed by the support:

$$f_X(x)=\int_0^x2\,dy=2x,\qquad f_Y(y)=\int_y^12\,dx=2(1-y).$$

Both marginals integrate to one. Expectations are E[X]=2/3 and E[Y]=1/3. Their second moments are 1/2 and 1/6, respectively, giving Var(X)=Var(Y)=1/18. Integrating xy against the joint density gives E[XY]=1/4. Therefore covariance is 1/36 and correlation is one half. These values describe the invented triangular model, not a measured biological relationship.

An independent model with these marginals would place positive density in portions of the square where y>x. The triangular support excludes those pairs. Support geometry can therefore reveal dependence even before a covariance calculation.

## Condition on the right reference set

For an interior x, the conditional density is f(y|x)=f(x,y)/f_X(x)=1/x on 0<y<x. It is a uniform distribution over that conditional interval. Consequently E[Y|X=x]=x/2 and Var(Y|X=x)=x²/12. At x=0.6 the conditional mean is 0.3, distinct from the unconditional mean one third.

Conditioning on X=x is defined through densities here, rather than dividing probabilities of two zero-probability exact-value events. The expression applies where the marginal density is positive, with conditional laws understood up to the usual probability-zero qualifications. Conditioning and intervention also differ: a mathematical conditional density alone supplies no randomized causal comparison.

For the event Y<1/4, integrate its marginal density: the probability is 2(1/4)−(1/4)²=7/16. Integrating the joint density over the same region gives the same result but needs the triangle's changing boundary. A rectangular integration bound would include impossible pairs.

## Derive the total-variance ledger

Write Y−E[Y] as the sum of Y−E[Y|X] and E[Y|X]−E[Y]. Conditional expectation makes the cross term vanish. Taking expectations of the squared sum gives

$$\operatorname{Var}(Y)=E[\operatorname{Var}(Y|X)]+\operatorname{Var}(E[Y|X]).$$

In the rehearsal, the first term is E[X²]/12=1/24 and the second is Var(X)/4=1/72. Their sum is 1/18, matching the direct second-moment result. The two nonnegative terms describe variation remaining within a given X and variation of the conditional mean across X. They are not automatically instrument and biological variance components; that interpretation needs an appropriate scientific model.

For finite nonzero variances, the covariance bound |Cov(X,Y)|<=sqrt[Var(X)Var(Y)] keeps correlation within minus one and one. The triangular values satisfy that check. Passing it is necessary for a valid moment pair but does not determine the entire joint law or establish independence.

## Verify and communicate the law

Retain support, normalization, marginals and units before reporting moments. Check event probabilities by two integration orders and verify the variance decomposition independently. A simulation may illustrate the law, but a finite cloud is neither a normalization proof nor evidence that an empirical population follows it. An approximately normal sample mean from independent draws does not make the triangular raw observations jointly normal or independent.

[MIT OCW 18.05 Spring 2022 calendar](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/pages/calendar/) classes 4–7 provide link-only random-variable/joint-law scope. All examples and derivations are original with substantial AI assistance; no source problem, prose, figure or data is imported. General measure-theoretic conditioning and broad distribution families remain outside this selected undergraduate treatment. The package remains partial and unreviewed.
