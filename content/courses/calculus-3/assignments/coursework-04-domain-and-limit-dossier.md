# Assignment 4: domain, coverage and limit dossier

This cumulative open report checks two tempting theorem conversions that lack needed global information. It combines a signed singular integral with differently weighted loops in a punctured spatial domain. All functions and curves are constructed mathematics. Retain calculations, parameterizations, code and report locally; selected browser fields do not evaluate the complete proof. A correct local derivative does not supply missing integrability or boundary coverage.

## Part A: preserve the singular cutoff rule

Use f=(x²−y²)/(x²+y²)² on the open unit square. The foundation derives y-first iterated value pi/four and x-first value -pi/four. Reproduce the section antiderivatives and verify them by differentiation before comparing either result.

For simultaneous rectangular cutoffs impose epsilon_x=three epsilon_y and let epsilon_y tend to zero. Starting from the finite rectangle formula, the limit is arctan3−pi/four=arctan(one half), about 0.46364761. This differs from both iterated values and from the balanced equal-cutoff value zero.

Explain why every finite-cutoff rectangle permits ordinary order exchange while the excluded-corner limit remains dependent on the path. Verify the absolute logarithmic divergence on a quarter annulus. Assigning the corner a finite value changes no neighborhood behavior and cannot restore that missing absolute integrability.

Implement finite-cutoff evaluations in both orders for at least two ratios and decreasing cutoffs. Report numerical error separately from the intentional change in domain. A denominator floor hidden inside a program would define a regularized problem; state it explicitly if introduced rather than claiming it is the original improper integral.

## Part B: a punctured spatial field

Use V=(-y/(x²+y²), x/(x²+y²), zero), defined away from the z axis. Its curl vanishes locally on that domain. In plane z=one, parameterize an outer circle of radius two traced counterclockwise three times and an inner circle of radius one traced clockwise once.

Direct integration gives outer circulation six pi and inner circulation minus two pi. Their signed sum is four pi. A calculation that replaces both loops with one ordinary annular boundary has changed their traversal counts. The boundary of a once-covered annulus uses each component once with opposite directions.

If using a triply covered annulus, its inner component must also carry three compatible clockwise traversals, which would give minus six pi and net zero. Explain this from parameterization and coverage rather than asserting a new surface after seeing the desired answer. A spanning disk crossing the excluded axis also fails the field-smoothness requirement.

Thus zero local curl does not justify converting the supplied mismatched loops into zero surface flux over an ordinary annulus. This is a calculus-level domain/coverage check, not a claim to develop general topology or every version of Stokes' theorem.

## Part C: compare the two failures carefully

In the singular-integral example, the obstacle is insufficient integrability and a limit depending on exclusion order. In the vortex example, the local field is smooth away from its excluded axis, but the proposed region/boundary representation is incompatible with the claimed theorem. Do not merge these into one generic statement that “the theorem fails.” The hypotheses identify different missing information.

Add one regular continuous rectangle example where integration order can be exchanged and one correctly oriented annulus example where the loop/curl relation works. Derive both and identify the restored conditions. A counterexample disproves an unqualified claim; it does not invalidate the valid theorem or prove every singular situation behaves the same way.

## Retained evidence and scope

Your dossier should include function domains, finite-cutoff formulas, absolute-growth proof, loop parameterizations, traversal counts, signed sums and the two regular controls. Diagrams need verbal descriptions identifying the excluded corner or axis, boundary directions and repeated coverage. Disclose software used and distinguish symbolic simplification from checking a theorem's hypotheses.

State explicitly which conclusions are local, which require global geometry and which depend on a limiting convention.

Connect the result to the local implicit-chart and nonlinear-coordinate foundations:nonvanishing local derivatives can support local calculations while global uniqueness, coverage or integrability still need separate arguments. A more precise numerical output cannot supply those missing assumptions.

[MIT OCW 18.02SC Fall 2010 Units 3–4](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/syllabus/) provide link-only integration/vector-theorem scope. The cutoff and weighted-loop comparisons are original bounded extensions, not a full real-analysis or topology curriculum. No source proof, exercise, figure, code or data is imported. All examples are synthetic and AI-assisted; broader coursework, measured workload and qualified review remain open. The package stays partial and unreviewed.
