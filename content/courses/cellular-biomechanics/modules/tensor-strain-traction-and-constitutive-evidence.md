# Tensor strain, traction and constitutive evidence

An axial force divided by area supplies one stress component under a particular loading assumption. A cell-scale deformation field generally has normal, shear and rotational parts. This original foundation turns a displacement gradient into small strain, uses an explicitly anisotropic constitutive model, and checks traction and work. All coefficients and fields are invented mathematical inputs rather than measurements of a material or cell population.

## Separate deformation from rigid spin

For planar displacement u(x,y), let B be its gradient. Small strain is epsilon=(B+B')/2, while the antisymmetric part describes infinitesimal spin. A field u=(-omega y,omega x) has zero small strain despite nonzero displacement gradients. Measuring one displacement magnitude therefore does not identify strain or stored energy.

This is a small-gradient construction. A finite rigid rotation has displacement gradient R−I; inserting a large rotation into linear strain can produce nonzero apparent strain. Large-deformation objectivity needs a finite-strain formulation. Changing the coordinate basis of an existing small strain tensor is a separate operation and transforms both stress and strain consistently.

## Declare work-conjugate components

Use engineering vector e=(epsilon_xx,epsilon_yy,gamma_xy), with gamma_xy=2epsilon_xy. Use stress vector s=(sigma_xx,sigma_yy,tau_xy). Then tensor work sigma:epsilon equals s'e, because the symmetric off-diagonal tensor terms occur twice. Treating epsilon_xy as gamma_xy would omit that factor in both stress and energy calculations.

Stipulate an orthotropic linear model in its aligned material axes:

$$s=Ce,\qquad C=\begin{pmatrix}C_{11}&C_{12}&0\\C_{12}&C_{22}&0\\0&0&C_{66}\end{pmatrix},\qquad W=\tfrac12 e^TCe.$$

The symmetric coefficient matrix admits this elastic energy. Positive stored energy for every nonzero e requires C11>0,C11 C22−C12²>0 and C66>0. Those conditions constrain admissible coefficients; they do not prove a real biological specimen is elastic, homogeneous or aligned with the assumed axes.

## Worked displacement and boundary traction

Choose normal coefficient block with rows (4,1),(1,3), and C66=2, all in kPa. Let u=(0.02x+0.03y,-0.01x-0.01y), with x,y and u in compatible length units. The engineering strain vector is (0.02,-0.01,0.02); tensor shear strain is 0.01.

Stress is (0.07,-0.01,0.04) kPa. The work density is one half times [0.02(0.07)+(-0.01)(-0.01)+0.02(0.04)]=0.00115 kPa, or 1.15 J/m³. Pressure and energy density share dimensions, but the reported physical quantity is stored energy per volume, not a second stress component.

For a boundary with unit outward normal n=(0.6,0.8), form the actual stress tensor with off-diagonal entries tau_xy. Traction is t=sigma n=(0.074,0.016) kPa. It is a vector of force per boundary area, not merely the scalar normal stress. Normal and tangential components follow by projection onto n and an explicitly chosen tangent.

## Distinct rehearsal

Use normal block (6,2),(2,5),C66=3 kPa and displacement u=(0.01x+0.04y,-0.02x+0.02y). Here e=(0.01,0.02,0.02), so stress is (0.10,0.12,0.06) kPa. Stored energy is 2.3 J/m³ and the same boundary normal gives traction (0.108,0.132) kPa. Check both the tensor contraction and engineering-vector work to recover the same energy.

The normal-block determinant is 26 in squared kPa units, and the shear coefficient is positive. A negative work result under these inputs would indicate an arithmetic, component or convention error. Positive energy is a useful consistency test, but cannot identify whether real loading is passive or whether active cellular work contributes.

A negative normal stress component need not make elastic energy negative: its work-conjugate strain and the full coupled contraction matter. In an active cell the selected passive elastic energy can also omit metabolic work or remodeling, so this positive quadratic model is a bounded constitutive assumption rather than a complete cellular energy balance.

## Identify what one loading condition leaves unknown

For a separate prescribed strain e=(0.01,0,0), suppose stress is measured synthetically as (0.06,0.02,0). In the four-coefficient family, this identifies C11=6 and C12=2. It leaves C22 and C66 undetermined. Positive-energy restrictions can bound possible values without selecting a unique pair.

A second normal-strain direction and an independent shear comparison could discriminate remaining coefficients under the model. An isotropic assumption would impose further relations, but it cannot be inferred from one uniaxial response merely to close the equations. Free transverse contraction and prescribed zero transverse strain are also different boundary conditions.

## Verify frames, balance and scope

Under a passive rotation, transform the stress and strain tensors together and verify invariant work. The constitutive tensor must transform too; keeping aligned orthotropic coefficients unchanged in arbitrary axes can lose normal-shear coupling. Constant stress has zero divergence in this simple field, while nonuniform fields require body-force and boundary balance checks.

[MIT OCW 20.310J Spring 2015 calendar](https://ocw.mit.edu/courses/20-310j-molecular-cellular-and-tissue-biomechanics-spring-2015/pages/calendar/) lectures 7–9 provide link-only tensor/anisotropy scope. All examples and derivations are original and AI-assisted, with no imported source problem, figure or data. Finite strain, general three-dimensional constitutive inference and qualified review remain open; the course stays partial and unreviewed.
