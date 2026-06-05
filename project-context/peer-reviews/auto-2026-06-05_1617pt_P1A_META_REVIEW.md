# P1A auto-2026-06-05_1617pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 329.4s

---

Meta-referee report on “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Below are issues that none of the five prior reviewers appear to have caught. I focus on hard-to-spot problems in operator identification, covariant/density structure, cross-equation consistency, and internal logical coherence.

P1A-META-E1
- Severity: ESSENTIAL
- Section/page: Abstract (p.1); Sec. X A–D (pp.14–15); Eq. (23)
- Why missed: Reviewers accepted the “Holst→Pontryagin (total derivative)” slogan without unpacking internal vs spacetime duals.
- Specific problem: The manuscript repeatedly identifies the Holst term/“Holst dual contraction” with the spacetime Pontryagin density. Quotes:
  - Abstract: “the Holst dual contraction ϵµνρσ Rµνρσ reduces on the Levi-Civita connection to the Pontryagin density ∝ RR̃ … a total derivative that contributes only a boundary term”
  - Sec. X D: “Re(Γ̊) = 1/2 ϵµνρσ Rµνρσ(Γ̊) = ∂µKµ (Pontryagin density; total derivative)”
  This conflates distinct objects. The Holst term is S_H ∝ ∫ e^I ∧ e^J ∧ R_IJ (internal-index contraction); the Pontryagin density is P ∝ ∫ Tr(R ∧ R̃) (spacetime dual). On a torsion-free connection, the Holst term is related to the Nieh–Yan density and, using the first Bianchi identity, is non-dynamical or vanishes under variation— but it is not the Pontryagin density. The equalities written between “Holst dual contraction” and spacetime Pontryagin are incorrect.
- Required fix: Correct the operator identities. State (with references) the precise relation among the Holst term, Nieh–Yan 4-form, torsion-squared, and (only separately) the spacetime Pontryagin density. Remove statements equating e∧e∧R with ϵµνρσ Rµνρσ and recast the “transparency” argument using the standard torsion-free/Bianchi-identity route.

P1A-META-M1
- Severity: MAJOR
- Section/page: Sec. II A.2 (Eq. 4, p.5); Sec. IV A (Eq. 13, p.8)
- Why missed: Prior reviewers noted “undefined N” in Eq. (4) but not the cross-equation coefficient inconsistency.
- Specific problem: Two different four-fermion coefficients are presented without reconciliation:
  - Eq. (4): L_int = −(3π G_N/2) × (γ²/(γ²+1)) × J5·J5, and it carries an extra undefined factor “N” in the prefactor.
  - Eq. (13): L_NJL^tor = −(3/16) κ (ψγ̄aγ5ψ)^2 with κ=8πG (no “N,” different normalization).
  These cannot both be correct as written; they mix distinct normalizations and species factors.
- Required fix: Provide a single, self-consistent derivation of the induced axial–axial four-fermion term from EC+Holst, define any species/color sums explicitly, and carry the same coefficient/normalization through the paper. Remove the undefined “N,” or define and use it consistently.

P1A-META-M2
- Severity: MAJOR
- Section/page: Sec. II A.2 (Eq. 6, p.5)
- Why missed: Others focused on overall dimensionality but not the tensor-density structure of the integrand.
- Specific problem: Eq. (6) reads
  Seff = ∫ d^4x √−g (α/M) ϵµνρσ eIµ eJν FIJρσ.
  Here ϵµνρσ is used with a prefactor √−g. If ϵµνρσ denotes the Levi–Civita tensor (not the symbol), √−g should not be outside; if it is the totally antisymmetric symbol, then √−g must be included in building the tensor. At the same time, inserting eIµ eJν with √−g double-counts density weight unless the Levi–Civita is the symbol. The operator is written with mixed tensor/density conventions that render the integrand’s covariance and dimensions unclear.
- Required fix: Declare conventions: whether ϵµνρσ is the tensor (with weight 0) or symbol (weight −1), and write the 4-form density unambiguously (either as a differential form or with ε-tensors and no stray √−g). Re-derive [ε e e F] dimension with these conventions and correct Eq. (6) accordingly.

P1A-META-M3
- Severity: MAJOR
- Section/page: Sec. X C (Eq. 21), p.14
- Why missed: Reviewers checked qualitative parity statements, not the time-variable consistency.
- Specific problem: The tensor-mode equation is written with primes (implying conformal time) but friction is 2H (cosmic-time Hubble). Quote: “h''_ij + 2H h'_ij + k^2 h_ij = 0.” In conformal time it should be 2ℋ = 2 a'/a, not 2H. This is a units/notation inconsistency; as written, Eq. (21) mixes time variables.
- Required fix: Use ℋ for conformal time or dots for cosmic time consistently. If primes are used, replace H with ℋ throughout the tensor equation and any subsequent use.

P1A-META-M4
- Severity: MAJOR
- Section/page: Sec. II C.1 (pp.6–7) vs the same subsection’s “Reheating thermal-reset barrier”
- Why missed: Others criticized the (Treh/MGUT)^(3/2) ansatz, but not the logical incompatibility with algebraic torsion’s instantaneous sourcing.
- Specific problem: The text builds a dilution factor D_inf ∝ e^(−3 N_tot) from “torsion dilutes as a^−3 during inflation,” yet immediately argues torsion is algebraically tied to the instantaneous axial current and is reset to ⟨J5µ⟩_T ≈ 0 by thermalization at reheating. These two premises are contradictory: an algebraically determined, non-propagating torsion cannot carry “memory” to dilute if it is continuously slaved to the local source and then instantaneously erased at reheating.
- Required fix: Choose a single consistent picture. Either drop D_inf entirely (and with it all N_tot numerology tied to torsion “dilution”), or provide a concrete propagating torsion sector (beyond minimal EC) where memory and dilution are well-defined, and re-derive the result in that model.

P1A-META-m1
- Severity: MINOR
- Section/page: Sec. IV D (pp.10–11) and Sec. X D (p.14)
- Why missed: Each section was read in isolation; the symbol reuse was not spotted.
- Specific problem: The same symbol Kµ is used for two different Chern–Simons currents:
  - Sec. IV D: Kµ ≡ ϵµνρσ Aν Fρσ (electromagnetic).
  - Sec. X D: ∂µKµ denotes the gravitational Pontryagin density (without defining the gravitational Chern–Simons current).
  Reusing Kµ for different currents risks confusion, especially near discussions of total-derivative terms.
- Required fix: Use distinct symbols, e.g., Kµ^EM for the electromagnetic CS current and Kµ^grav (or Qµ) for the gravitational CS current; define both explicitly when first used.

P1A-META-m2
- Severity: MINOR
- Section/page: Sec. II A.2 Step 3 (Eq. 5), p.5
- Why missed: Others asked for a definition of F, but not the functional-argument ambiguity.
- Specific problem: The operator is written Seff = (α/M) ∫ eI ∧ eJ ∧ FIJ[K, Γ̊], suggesting F depends simultaneously on contorsion K and the Levi-Civita curvature Γ̊. This is nonstandard and undefined. If F is the Lorentz curvature 2-form, its arguments should be the full spin connection ω (or ω = Γ̊ + K) and not a bracketed pair.
- Required fix: Define F precisely (e.g., F[ω] with ω = Γ̊ + K) and remove the ambiguous [K, Γ̊] notation. If both pieces are meant, show the decomposition explicitly.

P1A-META-m3
- Severity: MINOR
- Section/page: Table I; Sec. III A; Sec. XII B
- Why missed: Others focused on amplitude and novelty; this is a presentation coherence issue.
- Specific problem: The paper states in Sec. III A that “Connecting to a quantitative rotation angle β from the gravitational/torsion operator requires an explicit photon-torsion coupling that has not been derived here,” yet throughout Table I and multiple sections β is treated as a measurable signature linked to “parity-odd effective action.” Without the photon–torsion operator, the paper cannot assign even a scaling prediction for β from ECH; nonetheless, the narrative reads as if β is an ECH-facing observable.
- Required fix: Clearly separate the spectator-ALP β discussion from ECH. In every place β is mentioned, label it explicitly as a non-ECH (spectator) observable unless and until a photon–torsion coupling is derived. Remove any implication that β is a calculable ECH prediction in this paper.

P1A-META-N1
- Severity: NIT
- Section/page: Sec. X C (p.14)
- Why missed: Prior reviews focused on amplitude/closure, not bookkeeping.
- Specific problem: “vR(k, η) = vL(k, η)” is asserted without defining v. For tensor modes, v is not universally standard (sometimes used for scalar Mukhanov variable). Ambiguity here undermines precision.
- Required fix: Define v for tensor perturbations (e.g., vλ = a M_Pl hλ/√2) or write the statement directly in terms of the mode functions hλ.

Meta-review recommendation
REJECT

Rationale: Even setting aside the many substantial issues raised by the five reviewers (unpublished dependencies, the dimension-1 ansatz, arithmetic inconsistencies, scope inflation), the manuscript contains a fundamental operator-identification error (Holst ≠ Pontryagin), inconsistent four-fermion coefficients across equations, a tensor-equation time-variable mismatch, and an internal contradiction between “torsion dilution” and “algebraic thermal reset.” These are not editorial details; they compromise core claims and the main “transparency” exposition. The union of all six reviews surfaces multiple essential and major blockers (well over ten, counting unique items), many tied to first-principles correctness and reproducibility. My confidence that the paper would survive external peer review outside the author’s project ecosystem is low. A viable path forward would be a much shorter, self-contained theoretical note that (i) corrects the Holst/Nieh–Yan/Pontryagin identities, (ii) rigorously proves the perturbative transparency (with boundary conditions) without conflating operators, and (iii) removes all dependence on unpublished “companion” analyses and on the non-EFT “dimension +1” ansatz.