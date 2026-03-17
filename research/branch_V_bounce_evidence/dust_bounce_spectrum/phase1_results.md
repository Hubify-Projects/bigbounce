# Phase 1a Results: Dust Contraction → ECH Bounce → Radiation Expansion

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Verdict

$$
\boxed{\textbf{DUST\_BOUNCE\_MIXED}}
$$

The dust contraction + ECH bounce produces a **clean, calculable, internally consistent** primordial spectrum — but the spectrum is **wrong**.

---

## Summary of results

### 1. Viable spectrum produced?

**Partially.** The model produces a well-defined power spectrum with:
- Calculable amplitude (1 free parameter, same as inflation)
- Zero spectral running (α_s = 0, consistent with Planck)
- Negligible tensor-to-scalar ratio (r ~ 10⁻⁵⁵)
- Parameter-free non-Gaussianity (f_NL = 5/12)

But the spectral index is wrong.

### 2. Spectral index

$$
n_s = 1.000 \quad \text{(Harrison-Zel'dovich)}
$$

**8.3σ discrepant** with Planck 2018: n_s = 0.9649 ± 0.0042.

This is the standard result for the matter bounce (Finelli & Brandenberger 2002, Cai & Wilson-Ewing 2014). The ECH bounce does not modify this — it faithfully transmits the pre-bounce spectrum with transfer function T(k) = 1 for all observable modes.

### 3. f_NL survival

$$
f_{\rm NL}^{\rm local} = \frac{5}{12} \approx 0.42
$$

This is a parameter-free prediction, consistent with Planck bounds (f_NL = −0.9 ± 5.1). The non-Gaussianity is generated during dust contraction and passes through the bounce unmodified (correction ~ 10⁻⁵⁶).

### 4. Biggest problem

**n_s = 1.** The scale-invariant spectrum is excluded at high significance. This is not a problem with the ECH bounce — it is a fundamental property of dust-dominated contraction. Any model with a pure dust contraction phase will produce n_s = 1.

### 5. Secondary problem

**BKL instability.** Anisotropies grow faster than matter density during contraction (σ² ∝ a⁻⁶ vs ρ ∝ a⁻³). The FRW assumption may break down before the bounce is reached. This is unresolved in all matter bounce models.

---

## What the ECH framework contributes

The ECH bounce is **technically clean**:
- Regular (no singularity, Bardeen potential finite everywhere)
- Parameter-free (ρ_crit = 0.21 M_Pl⁴ from Barbero-Immirzi γ = 0.274)
- Transparent to super-Hubble perturbations (T = 1)
- No new physics injected at the bounce (no particle production, no k-dependent transfer)

The problem is not the bounce — it's the contraction. The ECH framework provides the best possible bounce (smooth, regular, calculable), but it cannot fix a wrong input spectrum.

---

## Observation compatibility

| Observable | Prediction | Observation | Status |
|-----------|-----------|-------------|--------|
| n_s | 1.000 | 0.9649 ± 0.0042 | **EXCLUDED (8.3σ)** |
| α_s | 0 | −0.005 ± 0.007 | ✓ |
| r | ~10⁻⁵⁵ | < 0.036 | ✓ |
| A_s | tunable | 2.1 × 10⁻⁹ | ✓ (1 free param) |
| f_NL^local | 5/12 | −0.9 ± 5.1 | ✓ |

One fatal failure out of five observables.

---

## Should we proceed to Phase 1b?

**YES**, with specific targets.

The n_s = 1 problem is well-known in the literature and several tilt mechanisms have been proposed. Phase 1b should investigate whether any of these work within the ECH framework:

### Priority 1: ALP curvaton (most natural for ECH)
The spectator ALP already present in the ECH framework (responsible for cosmic birefringence) could act as a curvaton. If the ALP has mass m_a and generates curvature perturbations at decay, the spectral tilt depends on m_a²/H². This is the most natural resolution because it uses existing ECH ingredients.

**Key question:** Does the ALP mass range required for birefringence (m_a ~ 10⁻³³–10⁻³⁰ eV) also give the right spectral tilt?

### Priority 2: Nearly-dust contraction (w ≠ 0 exactly)
If the contracting phase has w = ε (small but nonzero), the spectrum acquires a tilt:
$$
n_s - 1 = \frac{12w}{1 + 3w} \approx 12w
$$

Matching n_s = 0.965 requires w ≈ 0.003. This is physically reasonable if the "dust" is a scalar field with small kinetic energy corrections.

### Priority 3: Entropy-to-curvature conversion
A second field at the bounce could convert isocurvature to curvature perturbations with a k-dependent transfer. This is less natural (requires new ingredients) but is the mechanism most studied in the literature.

---

## Files delivered

| # | File | Status |
|---|------|--------|
| 01 | `01_background_solution.md` | ✓ Complete |
| 02 | `02_scalar_mode_equation.md` | ✓ Complete |
| 03 | `03_initial_conditions.md` | ✓ Complete |
| 04 | `04_mode_solver.ipynb` | ✓ Complete |
| 05 | `05_power_spectrum.md` | ✓ Complete |
| 06 | `06_fNL_estimate.md` | ✓ Complete |
| 07 | `07_consistency_checks.md` | ✓ Complete |
| 08 | `phase1_results.md` | ✓ This file |

---

## One-line summary

> The ECH bounce is the best bounce in the business — regular, parameter-free, transparent — but dust contraction hands it the wrong spectrum (n_s = 1, 8.3σ excluded). The bounce is not the problem. The contraction is. Phase 1b should investigate tilt mechanisms, starting with the ALP curvaton.
