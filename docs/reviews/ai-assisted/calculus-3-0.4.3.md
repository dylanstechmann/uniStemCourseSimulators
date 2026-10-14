# Calculus III 0.4.3 — multiple integrals and coordinate changes

Date: 2026-10-10. Codex expanded the week-8 multiple-integral reading and added separate numerical checks. The same AI assistant authored the lesson and regression, so these checks are not independent mathematical or human review. The course remains **partial, unreviewed and formative-only**.

## Scope

The lesson explains how a Jacobian determinant scales a transformed area cell, why scalar accumulation uses its absolute value, and how polar bounds encode disks. It compares polar and Cartesian disk-area integrals and integrates a nonuniform surface density with consistent units. Existing questions, keys, objectives and item counts are unchanged; one compact prototype reading remains.

## Numerical checks

For a radius-3 disk, polar integration gives $9\pi$ and the transformed Cartesian semicircle integral gives the same area. The map $(u,v)\mapsto(2u,v)$ has determinant 2 and sends the unit-disk area $\pi$ to ellipse area $2\pi$. On a radius-2 disk with constructed density $c(r)=2+r$ mg/cm$^2$, integration gives $40\pi/3$ mg and mean density $10/3$ mg/cm$^2$. These checks cover the stated examples, not biological concentration fields or every coordinate convention.
