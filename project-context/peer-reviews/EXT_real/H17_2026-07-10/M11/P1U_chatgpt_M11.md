VERDICT: REJECT

ISSUES:

[MAJOR] Section II A, Eqs. (1)–(4)—foundational ECH variational equations: Eq. (1) is presented as the fundamental action while containing a T
abc
	​

T
abc
 term that the reader is then instructed not to vary, so the displayed action is not the action from which the stated equations follow. More importantly, Eq. (3), T
abc
	​

=κS
abc
	​

, is the pure Einstein–Cartan relation, not the finite-γ
BI
	​

 Einstein–Cartan–Holst solution. In the minimally coupled Holst theory, inversion of the connection equation produces both the totally antisymmetric ϵ
IJKL
	​

J
5
L
	​

 component and an additional η
I[J
	​

J
5K]
	​

/γ
BI
	​

 component. Consequently, the statements that the Holst connection remains purely totally antisymmetric, that all other torsion irreducible components vanish, and that Eqs. (3)–(4) follow by the stated substitution are incorrect. This also invalidates structural facts F1–F2 used in the claimed completeness argument. 

ext_P1U_M11

 
arXiv

[MAJOR] Section II A 2 and Appendix B—dimensionally ill-defined effective action: Eq. (6) has Lagrangian-density dimension +1, as the manuscript itself acknowledges, and therefore does not define a dimensionless action. The claim that an algebraic Bianchi identity “strips one curvature factor” and changes the engineering dimension of F
IJμν
	​

 from two to one is not valid; tensor identities can make an operator vanish or relate operators, but cannot change mass dimension. The subsequent insertion of M
Pl
3
	​

, or of sufficient “bounce-curvature factors” to obtain (α/M)M
Pl
5
	​

, is an assumed dimensional completion rather than a result of ECH. The headline dark-energy scale, N
tot
	​

≃92, and the single-scale no-go therefore descend from an arbitrary completion of an action that is not initially well defined.

[MAJOR] Section IV “minimal-ECH completeness” and Appendix B 1—operator-basis completeness is not demonstrated: the set O
1
	​

–O
6
	​

 is asserted to exhaust the relevant local invariants, but no systematic invariant classification is supplied. The accompanying symbolic program verifies selected Bianchi and epsilon-contraction identities; it does not enumerate all Lorentz- and diffeomorphism-invariant operators. The manuscript itself excludes derivative fermion operators, curvature–torsion mixed terms, multi-species chiral structures, and other classes while continuing to claim completeness at the level of M
Pl
	​

 power counting. Moreover, the Bianchi check imposes torsion-free Riemann symmetries, whereas the fermionic ECH branch being classified is torsionful. These omissions cannot be repaired by the assertion that higher operators are “monotonically” more suppressed, because their expectation values, symmetries, and infrared scales have not been classified. 
GitHub

[MAJOR] Appendix C and Appendix D—incorrect Fierz projection and consequent failure of the NJL gap-equation result: under the convention explicitly encoded in the submitted script, the matrix is constructed with the source bilinear as the row index and the produced bilinear as the column index, but the decomposition routine evaluates Fsrc, thereby selecting a column. For an axial source, Eq. (C2) consequently uses the axial column, (1/4,1/2,0,−1/2,−1/4), rather than the axial row of the displayed matrix, (1,1/2,0,−1/2,−1). The scalar and pseudoscalar coefficients used in Appendix D are therefore wrong by a factor of four within the manuscript’s own convention, and the gap-equation code hard-codes the erroneous 1/4. The numerical subcriticality ratios must be recomputed; they are additionally affected by dropping the factor 8π while alternating between reduced and unreduced Planck-mass conventions. The manuscript also incorrectly dismisses a pseudoscalar condensate merely because it breaks parity: such a condensate is still Lorentz scalar, and its effective-potential minimum can contribute vacuum-like stress energy. 
GitHub
+1

[MAJOR] Section IV D, Route 2—no derived one-loop observable and a dimensional substitution error: Eq. (17), (∂
μ
	​

ϑ
NY
	​

)J
5
μ
	​

/M
Pl
	​

, introduces a dynamical Nieh–Yan pseudoscalar that is not part of minimal ECH and is not the operator derived in the cited one-loop analysis, which treats renormalized Holst-sector charges involving external vector and axial currents. The manuscript assigns [ϑ
NY
	​

]=1, so [∂ϑ
NY
	​

]=2, but then substitutes ∂ϑ
NY
	​

∼H
0
	​

, a dimension-one quantity, without specifying a field amplitude. Equation (18) is therefore not a derivation of a rotation angle, and its claimed 10
−58
–10
−60
 suppression is not a valid bound. A complete matching to the electromagnetic anomaly, a background solution for ϑ
NY
	​

, and the line-of-sight integral are required. 
arXiv
+1

[MAJOR] Section IV E, Route 3—running of γ
BI
	​

 is not a dark-energy calculation: even accepting the quoted Benedetti–Speziale beta function and the numerical integration yielding ∣Δγ/γ∣∼10
−6
, that result establishes only a scale dependence of a dimensionless coupling in a particular perturbative calculation. The manuscript never derives an effective stress tensor or vacuum-energy operator generated by this running. The additional factor (Δγ/γ)(H
0
	​

/M
Pl
	​

) is inserted without following from the beta function, so the claimed “41–67 orders” deficit relative to ρ
Λ
	​

 has no theoretical basis. 
arXiv

[MAJOR] Section IV F, Route 4—nonminimal ALP phenomenology is misclassified as a closed minimal-ECH route: minimal ECH contains neither the canonical ALP field, its potential, nor the photon Chern–Simons coupling used in Eq. (21). The manuscript repeatedly concedes that this coupling is not derived and that the same birefringence model exists unchanged in GR. Once α/M, m
θ
	​

, f
a
	​

, and the initial displacement are free, matching β and ρ
Λ
	​

 is a parameter fit, not an ECH prediction; declaring the result “closed” because m
θ
	​

∼H
0
	​

 is judged unnatural is an explanatory preference, not a no-go theorem. Conversely, the claimed rigid-coupling overshoot is not rigid because Eq. (9) contains an uncomputed finite contribution and the manuscript elsewhere treats α/M phenomenologically. Thus R4 cannot support the asserted four-route closure in either its fixed- or free-coupling reading.

[MAJOR] Section X—perturbation transparency is correct only in a much narrower and largely standard sense than claimed: for classical constant-γ
BI
	​

 ECH with canonical scalar matter, zero spin density implies the torsion-free branch, and the Holst density then vanishes by the algebraic Bianchi identity. That restricted observation is sound, but it does not imply that all scalar and tensor observables of the manuscript’s cosmology equal those of GR. LQC holonomy corrections, the nonsingular bounce, a matter-dominated contracting phase, and the bounce-to-inflation transition can all modify the background and perturbation actions independently of the Holst term. Statements such as “the bispectrum is therefore identical to the standard GR result” conflate absence of a Holst contribution with absence of all bounce/LQC contributions. The torsion-free reduction itself is already standard in the Holst literature and does not provide the novelty claimed here. 
arXiv

[MAJOR] Sections II B–C, XII, and XIV—there is no single self-consistent cosmological model: the paper combines an LQC holonomy bounce, an Einstein–Cartan spin bounce, a rotating black-hole-universe origin, matter-bounce contraction, approximately 92 e-folds of inflation, and a spectator ALP without presenting one action, one background solution, or junction conditions demonstrating their compatibility. The proposed dilution mechanism is especially inconsistent with minimal ECH: torsion is algebraic and follows the instantaneous axial current, so it cannot store a bounce-era amplitude through scalar-driven inflation; when the scalar carries no spin, torsion is identically zero. A four-fermion energy density scales as n
2
∝a
−6
, not as the e
−3N
 vacuum contribution used in the dark-energy bookkeeping. The extra (T
reh
	​

/M
GUT
	​

)
3/2
 factor is explicitly admitted to be an ansatz. Hence N
tot
	​

≃92 is a fitted parametrization, not a prediction or a physical closure mechanism.

[MAJOR] Sections XIII and XIV D—the matter-bounce f
NL
	​

 value and its alleged erasure are unsupported: the cited original calculation reports the familiar matter-bounce value −35/8, whereas the manuscript substitutes −35/16 on the authority of an unpublished companion calculation; even the title of its own Ref. [11] retains −35/8. The proposed correction must be derived transparently in this paper before it can be treated as an established prediction. Separately, the statement that the signal is “definitively erased” once N
tot
	​

−N
exit
	​

≳N
coh
	​

 introduces an undefined N
coh
	​

∼O(few) and supplies only scale bookkeeping. The manuscript explicitly does not compute the bounce/inflation transfer function, so it has not shown mutual exclusivity between dark energy and the matter-bounce bispectrum. 
arXiv

[MINOR] Sections V–VIII and Appendices F–H—observational analyses do not test the theory under review: the stock-CAMB ΛCDM+ΔN
eff
	​

 chains contain no ECH Boltzmann equations; the ALP posterior uses a Gaussian summary of the same birefringence datum it is said to “accommodate”; and the NaMaster study is a synthetic-sky estimator test that deliberately retains a biased unweighted fit. These exercises are acknowledged as non-load-bearing and add substantial length without increasing evidential support for the central no-go. They should be removed or published separately.

[MINOR] Figures 3–7 and overall presentation—several displayed quantitative comparisons are not scientifically defined: Fig. 3 is dominated by an intentionally different input H
0
	​

; Fig. 4 combines f
NL
	​

 and birefringence “significances” using assumed correlations without a joint likelihood and depicts positive correlation as an information gain; and Fig. 5 assigns numerical fine-tuning scores to quintessence and f(R) models without a common measure or derivation. The manuscript is also highly repetitive and written in an adversarial, self-referential style, with the same scope defenses and disclaimers repeated across the abstract, introduction, main text, tables, and appendices; a viable submission would require radical condensation and removal of unsupported forecast material.

The central claim is not supported: the restricted classical scalar-matter decoupling of the Holst term is valid, but the claimed basis-complete closure of Routes R1–R4 rests on an incorrect ECH torsion equation, an invalid dimensional construction, a faulty Fierz/gap calculation, and un-derived amplitude mappings.
