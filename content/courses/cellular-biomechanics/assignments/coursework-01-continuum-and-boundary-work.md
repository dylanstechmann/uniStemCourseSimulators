# Assignment 1: continuum and boundary-work evidence

This open report connects a displacement field, constitutive tensor, boundary traction and stored energy. It requires the component conventions and independent work checks that a single reported modulus omits. All coefficients and displacements are invented mathematical inputs. Retain diagrams, derivations, code and report locally; selected browser responses do not grade the full analysis or establish empirical material behavior.

## Part A: derive strain from the field

Use planar displacement u=(0.02x−0.01y,0.03x−0.01y), with coordinates and displacements in compatible length units. Calculate its full gradient, symmetric small strain and antisymmetric infinitesimal spin. The engineering strain vector is e=(0.02,-0.01,0.02), while tensor shear strain is 0.01.

State why the shear components differ by two. Do not turn the rotation part into an extra elastic strain or infer strain from one endpoint displacement without the reference length and field. The specified small-gradient model is not a finite-deformation constitutive theory.

## Part B: stress and work with a distinct material

Use aligned orthotropic normal coefficient block (5,1),(1,4), and engineering shear coefficient C66=2 kPa. Multiply C by the engineering strain vector. The resulting stress vector is (0.09,-0.02,0.04) kPa. Verify that the normal block determinant is nineteen in squared kPa units and that the selected energy is positive definite.

Calculate stored energy by both one-half e'Ce and one-half sigma:epsilon. Both give 0.0014 kPa, or 1.4 J/m³. Preserve the two off-diagonal terms in the tensor contraction. Replacing engineering shear with tensor shear in only one of these formulas produces a convention error, not a new material response.

The compressive normal component is negative under the declared sign convention, yet total stored energy is positive. Explain that difference using work-conjugate components. A list of stress magnitudes would lose both the directional boundary information and this signed energy check.

## Part C: resolve a boundary traction

Take unit outward normal n=(0.8,0.6) and tangent m=(-0.6,0.8). Form the symmetric stress tensor and compute t=sigma n. Its components are (0.096,0.020) kPa. The normal traction n dot t is 0.0888 kPa and the signed tangential traction m dot t is -0.0416 kPa.

Reconstruct the vector as t=(n dot t)n+(m dot t)m. This independent identity checks the normal/tangent orientation and units. Reversing the outward normal changes the traction vector; reversing only the chosen tangent changes the scalar tangential sign without changing the physical traction.

For a rectangular element with this constant stress, write the tractions on opposite faces and verify net force balance. Constant divergence does not prove arbitrary measured fields are homogeneous. If you introduce a nonuniform stress example, state the body force or boundary conditions needed for its balance rather than declaring equilibrium from one local value.

## Part D: rotate and identify the model

Choose a nontrivial passive rotation of axes and transform stress and strain as tensors. Verify invariant elastic work. Transform the constitutive law consistently; an orthotropic matrix written in material axes can acquire normal-shear couplings in a different basis. Simply reusing the same three coefficients after rotating the specimen changes the model.

Consider which coefficients a prescribed pure x-strain test would identify and which remain undetermined. Propose independent normal and shear comparisons that produce different predictions for two admissible coefficient sets. This is a mathematical discrimination task, not an experimental handling procedure or claim that a real cell is a passive orthotropic sheet.

Include one deliberately wrong shear convention and one rigid-infinitesimal-rotation field as implementation checks. Explain why a finite rigid rotation needs a finite-strain treatment if gradients are not small. Keep model-domain failure separate from floating-point error or a mistaken matrix product.

Distinguish prescribed displacement from prescribed traction when comparing candidate tests. They constrain different variables, and a transverse strain fixed at zero is not the same boundary condition as a traction-free transverse face.

## Retained evidence and scope

Retain the field, gradient, strain/spin decomposition, constitutive assumptions, positive-energy check, tensor/vector work comparison, traction reconstruction and rotated-frame evidence. Diagrams need a plain-text description identifying normals, tangents and sign conventions. If using a spreadsheet or program, disclose its operations and compare selected outputs with independent arithmetic.

[MIT OCW 20.310J Spring 2015 calendar](https://ocw.mit.edu/courses/20-310j-molecular-cellular-and-tissue-biomechanics-spring-2015/pages/calendar/) lectures 7–9 supply link-only continuum/anisotropy scope. All text, coefficients and tasks are original and AI-assisted, with no source problem, figure, code or data imported. General finite-strain inference, active cellular constitutive behavior, measured workload and qualified review remain open; the course stays partial and unreviewed.
