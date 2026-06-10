# EXT1 P1A — Gemini 3.5 Thinking referee report
**Provider**: gemini.google.com web app · model **3.5 Thinking**
**Chat**: https://gemini.google.com/app/4f6bdc99c91dc1d2
**PDF**: paper1a_ech_nogo_v1A.0.56.pdf (md5 96f18a36) · **Harvested**: 2026-06-10T17:05 PDT

---

Gemini said
Peer Review Evaluation Report

Journal: Physical Review D / JCAP

Manuscript Title: Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter

Author: Houston Golden (Independent Researcher)

Review Date: June 10, 2026

I. Recommendation

MAJOR REVISIONS

General Overview

This manuscript provides a detailed performance analysis of minimal Einstein-Cartan-Holst (ECH) gravity as a dynamical driver of late-time dark energy. By evaluating four explicit physical channels (NJL four-fermion contact interactions, one-loop graviton corrections, quantum running of the Immirzi parameter, and parity-odd CMB spectator alignments), the author establishes an amplitude-level "no-go" framework. The paper also introduces a "perturbation-transparency theorem" showing that for canonical scalar matter fields, the Holst sector decouples entirely from linear and higher-order perturbation equations of motion due to the algebraic Bianchi identity.

While the physical insights, execution, and systematic classification of the 13 logically independent barriers are compelling, the manuscript suffers from foundational issues in its field-theoretic definition of the effective action and mathematical inconsistencies regarding dimensional analysis. These issues must be addressed before publication.

II. Blockers (Must Fix Before Publication)
1. Dimensional Non-Invariance of the Off-Shell Action

Location: Section II.A.2, Eq. (6), and Appendix B, Eq. (B1).

The Problem: The author states that the leading parity-odd effective action term is written as:

S
eff
	​

=∫d
4
x
−g
	​

M
α
	​

ϵ
μνρσ
e
μ
I
	​

e
ν
J
	​

F
IJρσ
	​


The manuscript explicitly notes that the Lagrangian density carries a naive mass dimension of [L
odd
	​

]=+1. Because the spacetime volume element d
4
x has mass dimension −4, this forces the off-shell action to have a mass dimension of [S
eff
	​

]=−3, rather than being dimensionless ([S]=0 in standard units where ℏ=1).
An action that is not dimensionless means the quantum partition function path integral Z=∫D[g,e,ω]e
iS
 is mathematically ill-defined off-shell because the exponent is not a dimensionless quantity.

Proposed Fix: The author cannot define a valid physical framework using an off-shell action that lacks a regular dimension. The operator must be explicitly regularized off-shell by inserting appropriate matching powers of the Planck mass—i.e., replacing the coupling coefficient with the dimensionally valid form 
M
αM
Pl
3
	​

	​

 as sketched out in Section B, rather than treating it merely as an "on-shell scaling ansatz." Rewrite Section II.A.2 to ensure that the mathematical formulation of the action remains strictly dimensionless ([S]=0) throughout the entire off-shell derivation.

2. Contradictory Structural Definition of the Initial Action Principle

Location: Section II.A.1, Eq. (1).

The Problem: The fundamental action is defined as:

S
ECH
	​

=
16πG
1
	​

∫d
4
xe[e
a
μ
	​

e
b
ν
	​

R
μν
ab
	​

+
γ
1
	​

ϵ
abcd
e
a
μ
	​

e
b
ν
	​

R
cdμν
	​

+
4
1
	​

T
abc
T
abc
	​

]+S
matter
	​


The text immediately states: "The T
abc
T
abc
	​

 term... is a shorthand for the four-fermion contact interaction obtained after integrating out the non-propagating torsion; it is not an independently specified kinetic term and is not varied independently."
This statement introduces a severe structural contradiction. If Equation (1) represents the starting unvaried action, adding an explicit torsion-squared term prior to varying the connection while simultaneously using a torsionful Lorentz connection inside the curvature tensor R
μν
ab
	​

 results in double-counting or an unmotivated constraint equations system. In standard Einstein-Cartan theory, the torsionful curvature scalar already generates the torsion-squared terms algebraically upon decomposition into the Levi-Civita connection and contorsion tensor.

Proposed Fix: Clarify the variational status of Equation (1). If it is the first-principles action, remove the explicit 
4
1
	​

T
2
 term and show how it emerges dynamically on-shell via the Cartan field equations after varying with respect to the connection ω
μν
ab
	​

. If Equation (1) is meant to represent a partially on-shell reduced action, it should be explicitly labeled as such, and the connection variation should be shown cleanly.

III. Majors (Should Fix)
1. Theoretical Tension in the Canonical Inflaton Assumption vs. Reheating Reset

Location: Section II.C.1 ("Reheating thermal-reset barrier") and Section X.

The Problem: The author uses a thermodynamic washout argument to show that any primordial memory of bounce-era torsion is erased because the mean axial current ⟨J
μ
5
	​

⟩→0 in a C/P-symmetric thermal bath during reheating. However, Section X claims that minimal ECH gravity is completely "perturbation-transparent" for canonical scalar matter fields (such as a standard inflaton), meaning torsion vanishes identically (T=0) at all perturbation orders throughout the entire epoch.
If the universe is dominated by a canonical scalar inflaton field from the end of the bounce until reheating, there are no active fermionic degrees of freedom available to carry an axial current during inflation. Torsion is already exactly zero by the perturbation-transparency theorem, rendering a thermodynamic "washout" mechanism during reheating unnecessary. The text needs to reconcile why a thermodynamic fermion reset is required if the scalar-dominated inflationary phase has already zeroed out the torsion configuration via first-principles geometry.

Proposed Fix: Restructure the discussion in Section II.C.1 to show that the thermal-reset barrier applies specifically to scenarios where a significant sub-dominant fermion plasma persists through the bounce, or clarify that the geometric decoupling under scalar matter fields makes this thermodynamic erasure an independent parallel barrier.

IV. Minors (Polish)
1. Unpolished Figure Annotations and Placeholders

Location: Section II.A.1, Fig. 1 caption; Section XII.A, Fig. 5 caption.

The Problem: The captions contain literal text notes indicating uncompleted manuscript modifications:

Fig. 1: "The burned-in PTA annotation γ=3.20±0.42 is the superseded pre-real-KDE draft value... and the figure annotation is pending regeneration."

Fig. 5: "The burned-in '115 orders of magnitude improvement' annotation refers to this score difference... inherits the order-of-magnitude status discussed there."

Proposed Fix: Regenerate Figure 1 and Figure 5 using the corrected quantitative parameters (γ=2.567±0.382) and remove all placeholder metadata and draft annotations from the text.

2. Ambiguity in Conformal-to-Cosmic Time Transformations for Primordial GWs

Location: Section X.C, Eq. (21).

The Problem: In defining the tensor perturbation equation of motion, the manuscript writes:

h
ij
′′
	​

+2Hh
ij
′
	​

+k
2
h
ij
	​

=0

The text then says: "in cosmic time, using dt=adη the equivalent form is 
h
¨
ij
	​

+3H
h
˙
ij
	​

+(k
2
/a
2
)h
ij
	​

=0." While the equation is correct for standard transverse-traceless modes, the transformation step from conformal time to cosmic time produces a factor of 3H
h
˙
ij
	​

 only because the background metric leaves the tensor spatial perturbation indices untouched. For clarity and completeness in a journal of record, the notation should explicitly state that the spatial derivatives are comoving.

Proposed Fix: Add a brief clause specifying the comoving nature of the wavenumber k relative to physical spatial derivatives ∇
2
/a
2
 to maximize scannability.

V. Strengths

Rigorous Perturbation Decoupling Demonstration: The explicit step-by-step derivation in Section X proving that the Holst dual contraction ϵ
μνρσ
R
μνρσ
	​

 vanishes identically via the first algebraic Bianchi identity on a Levi-Civita connection provides an elegant resolution to common misconceptions in loop quantum cosmology variants.

Comprehensive Analytical Auditing: The systematic evaluation of the four separate minimal channels (NJL, one-loop effective actions, Immirzi running, and spectator ALPs) successfully shifts the dark energy discussion away from vague operator bases into precise, testable amplitude spaces.

Clear Observational Contextualization: The paper expertly maps out future survey thresholds (e.g., SPHEREx 2028 f
NL
	​

 targets and LiteBIRD CMB polarization windows), defining exact criteria where the surviving mechanism-independent signatures can be falsified.

VI. Specific Scrutiny
1. Four-Route Channel-Level Closure

The systematic closing of the four minimal channels is the core value of the paper. The author's closure of Route 1 (NJL contact) via a clear calculation showing it is suppressed by ∼70 orders of magnitude below ρ
Λ
	​

 at recombination is solid. For Route 2, demonstrating that loop-induced birefringence is suppressed by ≥58 orders of magnitude via the factor H
0
	​

/M
Pl
	​

 cleanly neutralizes this channel.

The reframing of Route 4 (Spectator ALP) is a significant improvement over previous literature: the author correctly points out that Route 4 cannot be ruled out by basic amplitude mismatch, but rather by an explanatory deficit or naturalness objection, since matching the dark energy density requires fine-tuning the field mass to m
θ
	​

∼H
0
	​

, which merely restates the cosmological constant problem.

2. Perturbation-Transparency Result for Canonical Scalar Matter

The proof provided in Section X is mathematically sound and carefully constructed. By using the zero-spin density condition (S
abc
=0) of canonical scalar fields to show that the connection reduces exactly to the Levi-Civita connection, the author correctly applies the first algebraic Bianchi identity:

R
μ[νρσ]
	​

=0

Contracting this identity with the totally antisymmetric Levi-Civita tensor ϵ
μνρσ
 forces the Holst term to vanish pointwise. The author correctly distinguishes this pointwise vanishing from a simple boundary term total-derivative cancellation (as seen in the Pontryagin density R
R
~
). This cleanly establishes that the Barbero-Immirzi parameter γ cannot imprint on linear scalar or tensor perturbation observables.

3. Reheating Thermal-Reset via Axial-Current Expectation Value

The argument that the physical source for algebraic torsion is the axial current expectation value ⟨J
μ
5
	​

⟩ rather than the absolute fermion number density n
ψ
	​

 is an insightful application of quantum statistical mechanics. The author correctly identifies that while n
ψ
	​

∼T
reh
3
	​

 is large, an unpolarized, C/P-symmetric thermal plasma forces the net expectation value ⟨J
μ
5
	​

⟩→0 due to randomizing chiral scattering processes. This provides a robust thermodynamic argument for the complete erasure of bounce-era torsion memory, independent of the model's exact inflationary scaling factors.

4. ALP Birefringence β≈0.27
∘
 as a Benchmark Consistency Point

The manuscript is exceptionally transparent regarding the observational signatures of the axion-like particle sector. The author avoids claiming the isotropic birefringence value β≈0.27
∘
 as a direct prediction of ECH gravity, accurately characterizing it as a generic, mechanism-independent GR+ALP setup benchmark. The section showing that LiteBIRD’s projected sensitivity (σ(β)≈0.03
∘
) cannot separate this benchmark value from the existing WMAP+Planck central value (0.342
∘
±0.094
∘
) in a formal model-discrimination test (yielding only a ∼0.73σ tension) is a mathematically accurate caution that prevents over-interpreting future Stage-IV CMB results.

5. Verification of Legacy External Round Closures

The current text effectively incorporates the modifications mandated during prior evaluation rounds:

The embedded LLM logging fragments and diagnostic purges are complete.

The scope language is clear, repeatedly stating that this is an amplitude-level channel assessment rather than an exhaustive operator-level theorem.

The inclusion of the Benedetti & Speziale (2011) citation accurately balances the Immirzi running derivation in Route 3 against known loop-level calculations.

The Route 4 presentation has been successfully updated to emphasize its naturalness limits rather than relying on a simple amplitude mismatch.




Thinking

