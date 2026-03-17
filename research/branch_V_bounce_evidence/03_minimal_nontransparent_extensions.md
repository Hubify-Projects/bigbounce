# Branch V: Minimal Nontransparent Extensions

**Created:** 2026-03-17

---

## The Transparency Theorem

The minimal ECH bounce is "transparent" because:
1. **Symmetric radiation bounce**: a(t) = a(-t), w = 1/3 throughout
2. **Time-reversal mapping**: Growing mode of contraction → decaying mode of expansion (unit transfer)
3. **Scale localization**: All bounce effects confined to k ~ k_b ≈ a_b M_Pl ≫ k_observable

**Consequence:** T(k) = 1, n_T = 0, f_NL = 0 for all observable modes.

To break transparency, we must violate at least one of these three properties. Below are six physically motivated extensions, ranked by minimality (fewest new assumptions).

---

## Extension V1: Time Asymmetry (Asymmetric Bounce)

### What changes
Break a(t) = a(-t) by having w_contraction ≠ w_expansion near the bounce.

### Physical motivation
- **Particle production at the bounce**: Rapid expansion at H = 0 → H > 0 creates particles (analogous to preheating). The created particles modify the effective EOS on the expansion side, making it differ from the contraction side.
- **Entropy production**: Second law of thermodynamics demands S_after > S_before. If entropy is produced in radiation (rather than a hidden sector), the effective temperature and EOS shift.
- **Quantum backreaction**: One-loop corrections to the effective action near ρ = ρ_crit are O(ρ/M_Pl⁴) ~ O(1). These corrections generically break time symmetry.

### New parameters
- δw = w_expansion - w_contraction near the bounce (1 parameter)
- Duration of asymmetric phase Δt (1 parameter)

### Observable consequences
- Modified transfer function: T(k) ≠ 1 for modes with k near the transition scale
- Oscillatory features in P(k) with period set by Δt
- Breaking of the growing → decaying mode map: some growing mode power leaks through

### Assessment
- **Minimality:** EXCELLENT (0 new fields, 1–2 parameters, arises from known physics)
- **Calculability:** HIGH (ODE system with modified EOS)
- **Distinctiveness:** MODERATE (oscillatory features also arise in other scenarios, but period/phase encode bounce properties)
- **Overall:** A-tier candidate

---

## Extension V2: Non-Radiation Contraction Phase

### What changes
Instead of w = 1/3 throughout contraction, include an epoch with w ≠ 1/3 before the bounce. The bounce itself remains ECH-driven at ρ = ρ_crit.

### Physical motivation
- **Matter bounce scenario (w = 0)**: If CDM or a massive scalar dominates the contracting phase, the universe contracts with w = 0. This is the best-studied bounce alternative to inflation. It produces a scale-invariant spectrum P(k) ∝ k^(n_s - 1) with n_s = 1 (Harrison-Zel'dovich) from the contraction alone, independent of the bounce mechanism.
- **Ekpyrotic contraction (w ≫ 1)**: A scalar with steep exponential potential V(φ) ∝ e^{-cφ/M_Pl} with c ≫ 1 produces w = c²/3 - 1 ≫ 1. This generates a blue scalar spectrum (suppressed large scales) but can produce scale-invariant perturbations via the entropy mechanism.
- **Kinetic-dominated contraction (w = 1)**: A free scalar φ with V = 0 gives w = 1, which produces specific predictions for tensor tilt: n_T = 2.

### Sub-variants

#### V2a: Dust-dominated contraction → ECH bounce
- **Scalar spectrum:** n_s ≈ 1 (scale-invariant, from contraction)
- **Tensor spectrum:** n_T = 0 (from dust, not radiation)
- **Non-Gaussianity:** f_NL^local = 5/12 ≈ 1.25 (SPECIFIC PREDICTION — no free parameters)
- **Tensor-to-scalar ratio:** r depends on bounce details but is generically small (r < 0.01)
- **Distinctive test:** f_NL^local = 5/12 is unique to matter bounce; inflation predicts f_NL^local ~ 10⁻² or 0

#### V2b: Ekpyrotic contraction → ECH bounce
- **Scalar spectrum:** Blue-tilted unless entropy mechanism operates
- **Tensor spectrum:** Suppressed (n_T very negative, amplitude negligible)
- **Non-Gaussianity:** f_NL^equil ~ O(1–10), strongly scale-dependent
- **Distinctive test:** Combination of very small r + moderate equilateral f_NL

#### V2c: Kinetic contraction → ECH bounce
- **Scalar spectrum:** Blue-tilted (n_s = 3 for w = 1; needs modification)
- **Tensor spectrum:** Blue-tilted with n_T = 2 (STRONG PREDICTION)
- **Non-Gaussianity:** f_NL ~ O(1) equilateral
- **Distinctive test:** n_T = 2 is unique; inflation gives n_T < 0

### New parameters
- w_contraction (1 parameter for single-phase models)
- Transition redshift z_transition (when radiation takes over, 1 parameter)
- For V2b: slope parameter c, plus entropy transfer coefficient (2–3 parameters)

### Observable consequences
- **V2a** produces the cleanest predictions (n_s = 1, f_NL = 5/12, small r)
- **V2c** produces the most distinctive tensor signal (n_T = 2)
- All variants produce specific predictions for the consistency relation n_T(r) that differ from inflation

### Assessment
- **Minimality:** GOOD (requires specifying contraction content, but this is needed anyway)
- **Calculability:** HIGH (well-studied in bounce literature)
- **Distinctiveness:** EXCELLENT (f_NL = 5/12 and n_T = 2 are smoking guns)
- **Overall:** A-tier candidate (V2a is the best single sub-variant)

---

## Extension V3: Spectator Field with Bounce-Modulated Mass

### What changes
Add a spectator scalar χ whose effective mass m²_eff(t) varies through the bounce due to coupling to background curvature or torsion. If m²_eff passes through zero near H = 0, χ experiences tachyonic growth.

### Physical motivation
- **Curvature coupling**: ξRχ² gives m²_eff = m² + ξR. Near the bounce R changes sign rapidly (R ∝ Ḣ > 0 at bounce, R < 0 in contraction). For ξ ~ O(1), m²_eff can pass through zero.
- **Torsion coupling**: In ECH, the torsion-squared term effectively adds ∝ ρ² to the curvature. A χ²T²-type coupling gives m²_eff that depends on energy density, creating a "torsion-modulated" mass.
- **ALP self-interaction**: The birefringence ALP φ already exists in the framework. If it has a λφ²χ² coupling to a second scalar, the ALP's rapid evolution near the bounce can trigger χ amplification.

### New parameters
- ξ (curvature coupling, 1 parameter)
- m_χ (spectator mass, 1 parameter)
- Optional: λ (ALP–spectator coupling, 1 parameter)

### Observable consequences
- **Curvature perturbation enhancement**: Tachyonic growth of χ produces enhanced curvature perturbations at the bounce scale, sourcing:
  - Enhanced P(k) at specific k (possible PBH formation)
  - Induced GW background peaked at the resonance frequency
  - Non-Gaussianity from χ → ζ conversion
- **Scale of enhancement**: Set by m_χ and ξ; could be at any scale from CMB to PBH

### Assessment
- **Minimality:** MODERATE (1 new field + 2 parameters)
- **Calculability:** HIGH (standard curvaton/spectator field calculation)
- **Distinctiveness:** MODERATE (curvaton models exist in inflation too; but bounce geometry sets unique resonance conditions)
- **Overall:** B-tier candidate

---

## Extension V4: Ekpyrotic-to-Bounce Transition

### What changes
Replace the deep contraction phase with an ekpyrotic phase (w ≫ 1) that naturally drives the universe toward the bounce. The ECH bounce provides the non-singular turning point.

### Physical motivation
- **BKL instability resolution**: A contracting universe with w < 1 develops chaotic mixmaster oscillations (Belinskii-Khalatnikov-Lifshitz instability). Ekpyrotic contraction (w ≫ 1) is the *only* known way to isotropize a contracting universe without inflation.
- **Natural setup for bounce**: Ekpyrotic phase drives ρ → ρ_crit, where ECH bounce takes over
- **ECH as "bridge"**: The ECH bounce replaces the problematic singular matching condition used in standard ekpyrotic models (which is their main weakness)

### New parameters
- Ekpyrotic slope c (1 parameter, determines w = c²/3 - 1)
- Transition energy density ρ_ek→rad (1 parameter)
- Entropy transfer efficiency ε (1 parameter, for scale-invariant spectrum)

### Observable consequences
- **Nearly scale-invariant scalar spectrum** (via entropy mechanism)
- **Very small r** (tensors suppressed by ekpyrotic factor)
- **Distinctive non-Gaussianity**: f_NL^equil ~ -c²/8 ~ O(−10) for c ~ 10
- **No B-modes** (decisive test vs inflation)
- **Specific prediction**: n_s - 1 = -2/c² (gives n_s = 0.98 for c = 10)

### Assessment
- **Minimality:** MODERATE (requires specifying ekpyrotic potential, 2–3 parameters)
- **Calculability:** HIGH (well-studied; see Lehners 2008, Ijjas & Steinhardt 2019)
- **Distinctiveness:** EXCELLENT (r ≈ 0 + specific f_NL + n_s prediction = maximally distinguishable from inflation)
- **Overall:** A-tier candidate — ECH solves ekpyrotic's biggest problem (the singular bounce)

---

## Extension V5: Loitering Phase

### What changes
Insert a quasi-static phase (H ≈ 0, Ḣ ≈ 0) of finite duration near the bounce, instead of an instantaneous transition.

### Physical motivation
- **Quantum gravity effects**: Near ρ = ρ_crit, higher-order corrections to the ECH action (e.g., R² terms, torsion-squared beyond minimal) could create a plateau in the effective potential, causing the universe to "loiter" at maximum density.
- **String theory analogy**: Hagedorn phase in string cosmology creates exactly this loitering behavior.
- **LQC holonomy corrections**: In loop quantum cosmology, the bounce can be "widened" by holonomy corrections that create a brief de Sitter-like phase at the Planck scale.

### New parameters
- Duration of loitering phase Δt_loit (1 parameter)
- Effective EOS during loiter w_loit ≈ -1 (approximately fixed)

### Observable consequences
- **Amplification of modes inside horizon during loiter**: Modes with k < a_b H_loit get amplified by factor ~ exp(H_loit Δt_loit), potentially enormous
- **Nearly scale-invariant spectrum from loitering**: If N_loit = H_loit Δt_loit ~ 60, the loitering phase itself produces a scale-invariant spectrum (essentially a mini-inflation at Planck scale)
- **Tensor amplification**: Unlike the transparent bounce, the loitering phase amplifies tensors to potentially detectable levels

### Assessment
- **Minimality:** LOW (introduces a fundamentally new phase; motivation is speculative)
- **Calculability:** HIGH (once EOS and duration are specified, standard perturbation theory applies)
- **Distinctiveness:** MODERATE (loitering models exist in string cosmology; not ECH-specific)
- **Overall:** C-tier candidate (too speculative for first target)

---

## Extension V6: Sound Speed Deformation

### What changes
The effective sound speed for perturbations c_s ≠ 1 near the bounce due to non-linear corrections in the ECH effective action.

### Physical motivation
- **Higher-order torsion terms**: At ρ ~ ρ_crit, the truncation of the EC action to quadratic torsion breaks down. Cubic and quartic torsion terms modify the effective action for perturbations, changing c_s.
- **k-essence analogy**: The modified Friedmann equation H² = (8πG/3)ρ(1 - ρ/ρ_crit) is equivalent to a k-essence scalar with non-trivial sound speed near ρ_crit.
- **Ghost condensation**: Near H = 0, the perturbation Lagrangian may develop a non-trivial kinetic term.

### New parameters
- c_s(ρ/ρ_crit) as a function (effectively 1–2 parameters for polynomial fit)

### Observable consequences
- **Enhanced/suppressed non-Gaussianity**: f_NL ~ 1/c_s² (for c_s < 1, non-Gaussianity is enhanced)
- **Modified dispersion relation**: Sound speed < 1 effectively lowers k_b, bringing bounce features to larger (more observable) scales
- **Scale-dependent modifications**: c_s varies during the bounce, creating k-dependent effects

### Assessment
- **Minimality:** GOOD (no new fields; arises from higher-order corrections to existing action)
- **Calculability:** MODERATE (requires specifying higher-order action terms)
- **Distinctiveness:** LOW (c_s ≠ 1 is generic in modified gravity; not ECH-specific)
- **Overall:** B-tier candidate

---

## Rankings

| Extension | Minimality | Calculability | Distinctiveness | ECH Connection | Overall |
|-----------|-----------|--------------|----------------|----------------|---------|
| **V2a (Matter contraction + ECH bounce)** | GOOD | HIGH | EXCELLENT | Bounce mechanism | **A** |
| **V4 (Ekpyrotic + ECH bounce)** | MODERATE | HIGH | EXCELLENT | Solves singular bounce | **A** |
| **V2c (Kinetic contraction + ECH bounce)** | GOOD | HIGH | EXCELLENT | Bounce mechanism | **A** |
| **V1 (Time asymmetry)** | EXCELLENT | HIGH | MODERATE | Intrinsic to bounce | **A−** |
| **V6 (Sound speed)** | GOOD | MODERATE | LOW | Higher-order ECH | **B** |
| **V3 (Spectator field)** | MODERATE | HIGH | MODERATE | Torsion coupling | **B** |
| **V5 (Loitering)** | LOW | HIGH | MODERATE | Speculative | **C** |

**Key insight:** The three A-tier extensions all share the structure: **specify the contracting phase + use ECH as the non-singular bounce mechanism.** This is not an accident — the ECH bounce's unique contribution is providing a well-defined, calculable, non-singular turning point. The contraction phase determines the spectrum; the bounce determines whether the transition is smooth.
