# P4 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-25_R-ext_P4_v1_0_128
**Wall time**: 113.1s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=97086, completion=10795, reasoning=9953, total=107881

---

## PAPER-GEM-B1: [BLOCKER] Isotropic chiral GWs cannot generate a dipole
**Location:** Section 9.8, paragraph "(i) Chiral gravitational-wave power asymmetry $\Pi$"
**Issue:** The paper claims that a primordial chiral tensor signal (which is statistically isotropic) translates to an observable chirality dipole via tidal-torque theory, citing Yu et al. 2020. This violates statistical isotropy: an isotropic chiral background generates parity-odd scalars/tensors (e.g., 3D helicity correlators as in Yu et al.), not a parity-even vector expectation value like a global sky dipole. 
**Fix:** Remove the claim that chiral GWs generate a dipole. Explicitly state that constraining isotropic chiral GWs requires parity-odd correlators (like the monopole), while the dipole strictly constrains anisotropic vector sources.

## PAPER-GEM-M1: [MAJOR] Incorrect EFT of Inflation operator dimension and parameterization
**Location:** Section 9.8, paragraph "(ii) Parity-odd galaxy-trispectrum amplitude"
**Issue:** The paper attributes the parity-odd galaxy 4PCF in Cabass et al. (2023) to "dimension-7 operators in the EFT of Inflation, parameterized by $g_*$". The leading parity-odd scalar operators in the EFT of Inflation appear at dimension 8 (e.g., $\epsilon^{ijk} \delta K_{il} \nabla_j \delta K_{kl}$) and are parameterized by Wilson coefficients $c_i$, not $g_*$.
**Fix:** Correct the text to state "dimension-8 operators" and remove the incorrect $g_*$ parameterization.

## PAPER-GEM-M2: [MAJOR] Missing GR lightcone projection effects in the transfer function
**Location:** Section 9.8, paragraph "Late-universe to primordial: the link, and its caveats"
**Issue:** The paper lists the components required for the morphology-to-primordial transfer function but omits GR lightcone projection effects. The Euclidean projection of the 3D spin vector onto the line of sight is not a gauge-invariant observable; a rigorous transfer function must include lensing deflection of the line-of-sight and parallel transport of the spin vector along the null geodesic.
**Fix:** Add GR lightcone projection effects (lensing deflection and frame-dragging/parallel transport) to the enumerated list of required components for the transfer function.

## PAPER-GEM-m1: [minor] TTT is a dynamical, not kinematic, mechanism
**Location:** Section 9.8, paragraph "(i) Chiral gravitational-wave power asymmetry $\Pi$"
**Issue:** The paper describes Tidal-Torque Theory (TTT) as providing a "kinematic correlation" between galaxy spins and the tidal field. TTT describes the physical torquing of the proto-galactic inertia tensor by the external tidal tensor during linear growth, which is a dynamical process.
**Fix:** Change "kinematic correlation" to "dynamical coupling".

## PAPER-GEM-m2: [minor] Isotropic tensor sources cannot generate a dipole
**Location:** Section 9.8, paragraph "What does the present null constrain?"
**Issue:** The paper states that an axial (pseudo-)vector dipole "would require a background vector or tensor source". A statistically isotropic tensor source cannot generate a vector expectation value (dipole) due to rotational invariance; only an anisotropic source or a background vector field can do so.
**Fix:** Change "background vector or tensor source" to "anisotropic background or vector source".

## PAPER-GEM-nit1: [nit] Redundant symmetry terminology
**Location:** Abstract and Section 9.8
**Issue:** The phrase "parity-even axial-vector" is redundant. Axial vectors (pseudovectors) are parity-even by definition.
**Fix:** Simplify to "axial-vector (which is parity-even)" or simply "axial-vector".
