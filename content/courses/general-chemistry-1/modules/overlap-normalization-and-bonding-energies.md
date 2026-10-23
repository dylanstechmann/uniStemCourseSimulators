# Overlap normalization and bonding energies

## From a bond diagram to an amplitude model

Lewis structures, VSEPR, valence-bond hybrids and molecular-orbital occupancies answer related but different questions. The existing readings develop their introductory use. This companion supplies a small calculation behind orbital mixing: normalized combinations of two overlapping basis functions. It does not turn a two-level electronic model into a measured bond energy. Nuclear repulsion, other orbitals, electron repulsion and geometry optimization would be needed for that stronger statement.

Take real, individually normalized functions phi_A and phi_B with overlap S=integral(phi_A phi_B). Assume |S|<1, so the basis functions are independent. For an amplitude psi=c_A phi_A+c_B phi_B, normalization requires c_A²+c_B²+2S c_A c_B=1. The cross term is essential. Using c_A=c_B=1/sqrt2 without checking S normalizes only the orthogonal case S=0. Spatial probability contains the same interference term point by point, while S is its integral over the whole space.

For equivalent sites, two symmetry-adapted combinations are

psi_plus=(phi_A+phi_B)/sqrt[2(1+S)],

psi_minus=(phi_A−phi_B)/sqrt[2(1−S)].

Their scalar product is zero under the stated equal-normalization and real-overlap assumptions. Their individual coefficients need not have equal magnitudes across the plus and minus states. A minus sign is an amplitude phase choice; a zero from cancellation is a node of that combination, not a negative probability. Reversing the sign convention of one basis function changes both its overlap and off-diagonal Hamiltonian element, leaving physical predictions unchanged when done consistently.

## Derive the energy equations

Let the diagonal Hamiltonian elements both equal alpha and the off-diagonal element equal beta. Projection of the stationary equation gives

alpha c_A+beta c_B=E(c_A+S c_B),

beta c_A+alpha c_B=E(S c_A+c_B).

Set c_B=c_A for the plus state and c_B=−c_A for the minus state. The resulting energies are E_plus=(alpha+beta)/(1+S) and E_minus=(alpha−beta)/(1−S). This is a generalized eigenvalue problem because the basis is nonorthogonal; no general matrix solver is needed for these two substitutions. Merely diagonalizing the Hamiltonian as though its basis were orthogonal gives different answers.

Whether the plus combination is lower depends on the stipulated matrix elements and overlap. Its name alone is not an energy calculation. In ordinary constructive examples with a chosen compatible basis convention, the lower combination has bonding character; an antibonding combination has a node and higher energy. A change in sign convention cannot itself change which physical state has lower energy.

## Separate worked example

Choose S=0, alpha=−2E* and beta=−E*. The two energies are −3E* and −E*, and each coefficient magnitude is 1/sqrt2. One electron placed in the lower state has electronic energy E* below a separated-site reference at −2E*. Filling that state with two opposite-spin electrons gives −6E* in the independent-electron sum. The model does not include their mutual repulsion or a nuclear potential-energy curve, so this sum is not a dissociation energy.

Now inspect a nonorthogonal rehearsal with S=0.2, alpha=−E* and beta=−0.4E*. The energies are −7E*/6 and −3E*/4. The equal-sign coefficients have magnitude 1/sqrt2.4; the opposite-sign coefficients have magnitude 1/sqrt1.6. Substitution into the full normalization expression gives one for each state. Check each energy by substituting its coefficients into both projected equations rather than checking only a memorized quotient.

## Occupancy and an honest energy ledger

For this stipulated two-level independent-electron model, use at most two opposite-spin electrons per spatial state. With two electrons in the lower state and one in the upper state, the electronic sum is 2E_plus+E_minus. An occupancy-based bond-order indicator is (N_lower−N_upper)/2=0.5 in this example. The indicator is a selected model descriptor; it does not by itself predict a real bond length, reaction enthalpy or stability against all decomposition channels.

Track the reference state as explicitly as the molecular state. Comparing a three-electron sum against two one-electron atoms changes particle number and cannot define a valid binding difference. Even a particle-matched reference lacks the omitted nuclear and interaction terms. A useful calculation can be internally correct and physically incomplete.

## Evidence tasks and limits

Reproduce both rehearsal energies and normalizations, then compare the incorrect S=0 calculation while holding alpha and beta fixed. Explain why that is a model change rather than rounding error. Sketch two amplitudes and their squared magnitudes; label the cross term, node and adopted phase convention. State what additional energy contributions and measured observables would be needed to investigate an actual diatomic molecule.

The linked MIT OCW 5.111SC Fall 2014 Unit II supports the bonding scope, while the local model and numbers are original AI-assisted instruction. The forthcoming open bonding report uses different overlap and matrix entries. Browser checks assess selected energies, exact occupancies and interpretations; amplitude drawings, proofs and full energy ledgers remain locally retained and ungraded. Broader molecular electronic-structure theory remains selective rather than implicitly covered by this small solvable system.
