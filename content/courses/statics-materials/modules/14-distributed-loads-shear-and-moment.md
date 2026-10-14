# Distributed loads, shear force, and bending moment

Before using a beam's bending moment to estimate stress, first determine how the applied loads create that internal moment. A cut through a beam exposes internal force and moment resultants. Their values change along the span, and the shear-force and bending-moment diagrams show those changes.

## From a distributed load to internal resultants

Use the coordinate (x) measured from the left end. In this lesson, downward distributed load intensity (w(x)) is positive, positive bending moment is sagging, and the shear sign is chosen so that

**dV/dx = −w(x),    dM/dx = V(x).**

Thus, over an interval without a concentrated force or couple, the signed change in shear is the negative area under the load-intensity curve, and the signed change in moment is the area under the shear diagram. Where (w) is constant, (V) is linear; where (V) is linear, (M) is quadratic. These derivative relations are local equilibrium statements, not additional material laws.

At a section (x), imagine separating the beam and drawing a free-body diagram of one side. Include every support reaction and applied load on that side, then solve force and moment balance for the internal shear (V(x)) and moment (M(x)). Repeat in each interval where the loading expression changes. The internal actions on the opposite cut face have opposite directions. Keeping one sign convention throughout is more reliable than deciding signs from a curve's appearance after the calculation.

A downward point force (P) creates a downward jump in (V) of magnitude (P); an upward support reaction creates an upward jump. A finite point force does not make (M) jump, so the bending-moment diagram remains continuous there. On a simply supported end with no applied end couple, (M=0). A free-body check at the far end should recover the other reaction and the support boundary condition.

## Worked example: a full-span uniform load

A simply supported beam spans (L=6\,\mathrm{m}) and carries a downward uniform load (w=2\,\mathrm{kN/m}) across its full length. Its resultant is (wL=12\,\mathrm{kN}), acting at the midpoint. Moment balance about the left support gives (R_B(6)-(12)(3)=0), so (R_B=6\,\mathrm{kN}). Vertical force balance then gives (R_A=6\,\mathrm{kN}). The reactions sum to the applied load, and their moments about either support balance.

Cut at a distance (x) from the left support, where (0<x<6\,\mathrm{m}). The load to the left of the cut is (wx). Equilibrium gives

**V(x)=R_A-wx=6-2x\quad\mathrm{kN}.**

Using (dM/dx=V) and the simple-support boundary condition (M(0)=0),

**M(x)=6x-x^2\quad\mathrm{kN\,m}.**

The endpoint check gives (M(6)=36-36=0\,\mathrm{kN\,m}), as required. At (x=3\,\mathrm{m}), (V=0), and (M=9\,\mathrm{kN\,m}). This is the maximum positive moment: (dM/dx=V) changes from positive to negative at that location. The shear diagram is a straight line from (+6\,\mathrm{kN}) just inside the left support to (-6\,\mathrm{kN}) just inside the right support; the moment diagram is a parabola that is zero at both supports.

## A point-load jump check

Now place a (4\,\mathrm{kN}) downward point load (2\,\mathrm{m}) from the left support of the same (6\,\mathrm{m}) span. Moment balance gives (R_B(6)=(4)(2)), so (R_B=4/3\,\mathrm{kN}) and (R_A=8/3\,\mathrm{kN}). The shear is (+8/3\,\mathrm{kN}) before the load and (8/3-4=-4/3\,\mathrm{kN}) after it. The jump is exactly the applied downward force. The moment is (M=(8/3)x\) before the load and (M=(8/3)x-4(x-2)\) after it. Both expressions give (16/3\,\mathrm{kN\,m}) at the load, so moment is continuous, and the latter gives zero at the right support.

## From moment to nominal bending stress

The diagram's largest moment can feed the elementary elastic bending relation **\(\sigma_{\max}=Mc/I\)**, provided the section and material assumptions are suitable. For a rectangular section with width (b=0.10\,\mathrm{m}) and depth (h=0.20\,\mathrm{m}), the centroidal second moment is

**I=bh^3/12=6.667\times10^{-5}\,\mathrm{m^4},    c=h/2=0.10\,\mathrm{m}.**

Using (M_{\max}=9\,\mathrm{kN\,m}=9000\,\mathrm{N\,m}), the extreme-fiber nominal stress is (Mc/I=13.5\,\mathrm{MPa}). The units reduce to ((\mathrm{N\,m})(\mathrm{m})/\mathrm{m^4}=\mathrm{N/m^2}). This is a stress estimate under the stated linear-elastic beam model; it does not check yield, fatigue, deflection, local stress concentration, or structural safety.

## A reliable diagram workflow

1. Draw the complete free-body diagram and solve all support reactions using force and moment equilibrium.
2. Mark where the distributed load or concentrated loading changes. Write a separate cut-section equilibrium equation for each interval.
3. Sketch (V) first. Check that its slope follows (-w(x)), its jumps match point forces, and its end value is consistent with the remaining support reaction.
4. Integrate (V), or use areas under (V), to obtain (M). Check moment continuity across point forces and the zero-moment conditions at simple supports without applied end couples.
5. Locate possible interior extrema where (V=0), compare them with the endpoints and any interval boundaries, and use the largest relevant moment for a stated stress calculation.
6. Keep units attached to load, shear, moment, and stress, and state which ideal beam assumptions the result uses.

The routine beam relations assume a slender member, small deflections, and the idealized loading and support conditions in the model. Distributed loads, support reactions, and section resultants in these examples are synthetic. Real components may have three-dimensional load introduction, changing geometry, material anisotropy, large deformation, or failure modes outside this model.

## Reference

MIT OpenCourseWare, **2.001 Mechanics & Materials I**, Fall 2006: [undergraduate syllabus](https://ocw.mit.edu/courses/2-001-mechanics-materials-i-fall-2006/pages/syllabus/) and [lecture notes](https://ocw.mit.edu/courses/2-001-mechanics-materials-i-fall-2006/pages/lecture-notes/). The syllabus places shear-force and bending-moment diagrams after equilibrium and before deformable-body and stress topics. These pages are scope comparators only; this original reading does not copy or adapt their notes, diagrams, or problems.
