# Final Paper Structure

**Date:** 2026-03-17
**Title:** "From Quantum Bounce to Cosmic Birefringence: Phenomenological Constraints on Spin-Torsion Cosmology with a Planck-Scale ALP"

---

## Target: ~25-30 pages (PRD format), ~45-55 references

---

## Section 1: Introduction (~2.5 pages)

### 1.1 Motivation
- Cosmological constant problem (2 paragraphs)
- Parity violation in gravity: recent evidence from CMB birefringence (1 paragraph)
- Spin-torsion cosmology as a framework (1 paragraph)

### 1.2 This Paper
- Three-part structure announcement: bounce assessment, structural closure, spectator ALP prediction
- Executive summary table: bounce (✓ viable), DE from bounce (✗ 13 barriers), birefringence (✓ β ~ 0.27°)
- "The single surviving testable prediction of the minimal ECH framework is cosmic birefringence via a Planck-scale ALP"

### 1.3 Original Contributions
1. Complete assessment of ECH bounce cosmology
2. Thirteen structural barriers closing all bounce → DE/observable routes
3. Spectator ALP birefringence prediction: β = Cα θ_i / (4π) ~ 0.27°
4. MCMC constraints on (θ_i, m_a) from current birefringence data
5. LiteBIRD forecasts and falsification criteria

### 1.4 Organization
- Guide to remaining sections

---

## Section 2: Theoretical Framework (~4 pages)

### 2.1 Einstein-Cartan-Holst Action
- ECH action with Barbero-Immirzi parameter γ = 0.274
- Torsion integration → four-fermion (J⁵)² interaction
- Parity-odd effective action (one-loop, scheme-dependent)
- **Framing:** "motivates" not "derives"

### 2.2 Nonsingular Quantum Bounce
- Modified Friedmann equation: H² = (8πG/3)ρ(1 - ρ/ρ_crit)
- ρ_crit ≈ 0.27 ρ_Pl
- Bounce properties (singularity resolution, time-reversal symmetry)

### 2.3 Parity-Odd Sector and Late-Time Phenomenology
- The inflationary suppression chain as illustrative (not derivation)
- Four routes to w = -1 tested and closed (brief; full details in companion note or appendix)
- **Conclusion:** "The minimal framework does not derive late-time DE from first principles. DE is treated as Λ."

### 2.4 Effective Spectator ALP
- Lagrangian: L = -½(∂φ)² - V(φ) - (g/4)φFF̃
- Parameters: f_a = M_Pl, C = 8 (SM), θ_i free, m free
- Birefringence formula: β = Cα θ_i η / (4π)
- f_a cancellation (proven explicitly)
- What is claimed vs what is not claimed (Table)
- Spectator regime: m >> H_0, Ω_a ≪ 1, w irrelevant

---

## Section 3: Structural Closure Assessment (~3 pages)

### 3.1 Routes Tested
- Table: all 15 branches (A–O) with one-line status
- 5 failure modes: too high-energy, too generic, too decoupled, too universal, Hamiltonian conservation

### 3.2 The Thirteen Barriers
- Compact table: barrier name, mechanism, which branch
- Key insight: "The bounce is trapped between being too high-energy for late-time observables and too generic at its own scale"

### 3.3 Implications
- Bounce and DE are independent problems
- The framework is theoretically viable but observationally inert in the direct sector
- The ALP birefringence is the sole indirect testable handle

---

## Section 4: Birefringence Prediction and Data (~2.5 pages)

### 4.1 ALP Birefringence Mechanism
- Physical picture: ALP rolls from θ_i to θ_0 during matter era
- CMB photons accumulate rotation β = g Δφ / 2
- Rolling efficiency η(m/H_0) from ODE integration

### 4.2 Current Observations
- Table of birefringence measurements (Planck PR3, PR4, ACT DR6, SPIDER)
- Combined constraint: β = 0.342 ± 0.094°
- 3.6σ evidence for β ≠ 0

### 4.3 Predicted vs Observed
- β_pred = 0.27° × θ_i for spectator (η → 1)
- For θ_i = 1.3: β = 0.35° (within 0.1σ of observation)
- Natural O(1) parameter → no tuning

---

## Section 5: MCMC Analysis (~3 pages)

### 5.1 Method
- Cobaya MCMC framework, custom Theory + Likelihood classes
- ALP ODE solver: DOP853 in ln(a), rtol = 10⁻¹⁰
- Birefringence likelihood: Gaussian on β_obs = 0.342 ± 0.094°
- Convergence criterion: R̂ - 1 < 0.01

### 5.2 Results: Spectator ALP (C = 8)
- θ_i = 1.36 ± 0.44, log₁₀(m/eV) = -31.3 ± 0.7
- β = 0.336 ± 0.107°
- η = 0.957 (field has fully rolled)
- Δχ² = 13.2 vs null (3.6σ)

### 5.3 Degeneracy Analysis (C floated)
- C × θ_i ~ 10.6 (degenerate); C = 8 is within posterior
- Floating C adds parameter without improving fit
- Recommendation: fix C = 8 (SM)

### 5.4 Model Comparison
- Table: ALP vs null vs free-β
- ALP statistically equivalent to free β on current data
- ΔAIC = +2 (marginal penalty for extra parameter)
- Physical advantages: natural O(1) parameters, f_a-independent, falsifiable

---

## Section 6: Experimental Constraints and Forecasts (~2 pages)

### 6.1 Existing Bounds
- Constraint table: CAST, SN1987A, superradiance, spectral distortion, isocurvature, DM overproduction
- All satisfied with margins of 9–32 OOM

### 6.2 LiteBIRD Forecast
- σ(β) ~ 0.01° → θ_i determined to ±0.04 rad
- If β_pred = 0.27°: detected at > 20σ
- If β = 0: ALP model excluded at > 20σ
- Decisive test within ~5 years of launch

### 6.3 CMB-S4 and Ground-Based
- Complementary: anisotropic birefringence, frequency dependence
- Can distinguish ALP from Faraday rotation, instrumental systematics

---

## Section 7: Discussion (~3 pages)

### 7.1 What the ALP Model Provides
- Not a better fit, but a physical interpretation
- Natural parameter prediction (θ_i ~ O(1) from misalignment)
- Falsifiable structure (achromatic, isotropic, specific mass scaling)

### 7.2 Relationship to ECH Framework
- ECH motivates f_a ~ M_Pl through Planck-scale parity-odd sector
- The ALP is NOT uniquely derived from ECH
- Any Planck-scale ALP with SM coupling gives the same prediction
- ECH provides one possible UV completion

### 7.3 Rolling-vs-Freezing Tension
- Single-field ALP-as-DE: max β ~ 0.16° on Ω_DE contour (factor 2 below observed)
- Spectator regime resolves tension by separating birefringence from DE
- Two-field extension deferred to future work with DESI DR2 w(z) constraints

### 7.4 The Structural Closure in Context
- Comparison to other QG approaches (LQC, string, asymptotic safety)
- The bounce is viable; the difficulty is connecting to late-time observables
- This is a generic problem, not specific to ECH

---

## Section 8: Limitations (~1.5 pages)

### 8.1 Theoretical
- w = -1 not derived (Λ assumed)
- ALP not uniquely from ECH
- m ~ H_0 is CC problem in disguise (spectator mass less tuned but still free)
- One-loop ALP-photon vertex not computed from ECH

### 8.2 Observational
- Single Gaussian data point (one effective constraint)
- ALP equivalent to free β on current data
- No anisotropic birefringence data yet

---

## Section 9: Conclusions (~1 page)

Three paragraphs:
1. ECH bounce is well-defined and nonsingular. Thirteen barriers close all routes to DE and distinctive signatures.
2. Spectator ALP with f_a = M_Pl and C = 8 predicts β ~ 0.27°, matching observation. MCMC: θ_i = 1.36 ± 0.44.
3. LiteBIRD will be decisive. Dark energy remains unexplained. The ALP birefringence is the single testable output.

---

## Appendices (~4 pages total)

| App | Content | Pages |
|-----|---------|-------|
| A | Notation and conventions | 0.5 |
| B | ALP parameter table and bounds | 0.5 |
| C | ODE integrator validation | 1 |
| D | Full barrier catalog (13 entries) | 1.5 |
| E | Nieh-Yan topological term | 0.5 |

**Removed from current paper:** Galaxy spin (Bayesian analysis, data methods), joint likelihood with galaxy spin, distance measures, rotation framework details.

---

## Page Budget

| Section | Pages |
|---------|-------|
| Introduction | 2.5 |
| Theory | 4 |
| Closure | 3 |
| Birefringence | 2.5 |
| MCMC | 3 |
| Forecasts | 2 |
| Discussion | 3 |
| Limitations | 1.5 |
| Conclusions | 1 |
| Appendices | 4 |
| References | 2 |
| **Total** | **~28.5** |

This is within PRD standard length. Tight but complete.
