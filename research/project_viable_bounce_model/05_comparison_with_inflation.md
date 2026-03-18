# 05: Comparison with Inflation

**Created:** 2026-03-17
**Status:** IN PROGRESS

---

## The Models Being Compared

**Model A: LQC Matter Bounce + Partial Curvaton**
- Contraction: matter-dominated (w ≈ 0)
- Bounce: LQC (quantum-geometry corrections suppress tensor modes)
- Tilt: curvaton with m_σ ≈ 0.76 H_k, contributing α² ≈ 0.09 of P_ζ
- Parameters: m_σ/H_k, α (curvaton fraction), r_dec (curvaton decay efficiency)

**Model B: Standard single-field slow-roll inflation**
- V(φ) = V₀ × f(φ)
- Parameters: V₀ (amplitude), n_s (from V'/V, V''/V)
- The vanilla benchmark: Starobinsky R² inflation

---

## Parameter Count

| | Bounce + Curvaton | Single-field inflation | Starobinsky R² |
|--|-------------------|----------------------|----------------|
| Background params | 1 (ρ_c from γ) | 1 (V₀) | 1 (M²) |
| Perturbation params | 2 (m_σ/H, α) | 1 (ε or η) | 0 (all fixed) |
| Total free params | 3 | 2 | 1 |

**Inflation is more economical** — especially Starobinsky, which has ONE parameter and predicts everything. Our bounce model has 3 parameters.

However: the bounce model also resolves the singularity (inflation does not address this) and avoids the trans-Planckian problem (inflation requires it). These are theoretical virtues not captured by parameter count.

---

## Observable-by-Observable Comparison

### Spectral Index n_s

| Model | Prediction | Match to data? |
|-------|-----------|---------------|
| Bounce + curvaton | 0.965 (tuned via m_σ) | ✓ (but tuned) |
| Starobinsky R² | 1 − 2/N ≈ 0.964 for N = 55 | ✓ (parameter-free) |
| Generic slow-roll | Depends on V(φ) | ✓ (but V is chosen to fit) |

**Inflation wins:** Starobinsky predicts n_s from a single parameter (N, the number of e-folds), while the bounce model tunes m_σ to fit.

### Tensor-to-Scalar Ratio r

| Model | Prediction | Testable? |
|-------|-----------|----------|
| Bounce + curvaton | ~10⁻⁴ | No (below LiteBIRD sensitivity) |
| Starobinsky R² | 12/N² ≈ 0.004 | Marginal (LiteBIRD target: σ(r) ~ 0.001) |
| Large-field inflation | 0.01–0.1 | Yes (BICEP Array, LiteBIRD) |

**Mixed:** The bounce model predicts r too small to detect. Starobinsky predicts r = 0.004, which is within reach of LiteBIRD. If LiteBIRD detects r ≈ 0.004: Starobinsky wins, bounce model survives (consistent). If LiteBIRD detects r > 0.01: both Starobinsky and bounce are in trouble.

**Key test:** If LiteBIRD finds r = 0.000 ± 0.001 (no detection), this is CONSISTENT with the bounce model and starts to disfavor Starobinsky. But it doesn't distinguish bounce from other inflation models with small r.

### Non-Gaussianity f_NL

| Model | f_NL^local prediction | Testable? |
|-------|----------------------|----------|
| **Bounce + curvaton** | **−3.7** | **YES (MegaMapper: 7.4σ)** |
| Starobinsky R² | O(n_s − 1) ≈ −0.02 | No |
| Multi-field inflation | Model-dependent, |f_NL| < 5 typical | Maybe |
| Curvaton inflation | 5/(4r_dec) − ... | Yes, but positive f_NL |

**THE BOUNCE MODEL WINS HERE.** f_NL = −3.7 is:
1. Large enough to detect (7.4σ with MegaMapper)
2. **Negative** — standard inflation models with curvaton predict POSITIVE f_NL for the same parameter range
3. Of a specific value that is nearly parameter-free (set by the matter contraction dynamics)

**This is the single strongest discriminator between the bounce and inflation.**

If MegaMapper measures f_NL = −3.7 ± 0.5:
- ΛCDM + single-field inflation is ruled out at 7.4σ
- Multi-field inflation with curvaton typically predicts f_NL > 0 → also ruled out
- The matter bounce is the ONLY standard scenario that predicts this specific negative value

### Running α_s

| Model | Prediction |
|-------|-----------|
| Bounce + curvaton | ~ −(n_s − 1)² ≈ −0.001 |
| Starobinsky R² | ~ −2/N² ≈ −0.0007 |

Both predict very small running. Not a discriminator.

### Spectral Features

| Model | Prediction |
|-------|-----------|
| Bounce | Possible oscillatory features from bounce (Zhu & Cai 2026) but at GHz for Planck-scale bounce |
| Inflation | Smooth (unless step/feature in V(φ)) |

Not currently testable.

---

## Does the Bounce Model Explain Anything Inflation CANNOT?

### 1. Singularity Resolution
Bounce: YES — the singularity is replaced by a regular bounce.
Inflation: NO — inflation starts from an initial singularity (or requires eternal inflation with measure problems).

**This is a theoretical virtue, not an observational prediction.**

### 2. Trans-Planckian Problem
Bounce: ABSENT — modes are always sub-Planckian during contraction (they start large and contract).
Inflation: PRESENT — modes start sub-Planckian and are stretched to superhorizon scales, crossing the Planck scale.

**Again theoretical, not observational.**

### 3. Initial Conditions
Bounce: The contraction phase starts from a large, homogeneous, expanding universe that enters contraction — but this raises the question of WHY it started contracting.
Inflation: Requires a patch of slow-rolling scalar field — the "initial patch" problem.

**Both have initial condition issues.** Slow contraction (Ijjas & Steinhardt) argues for bounce; eternal inflation (Linde) argues for inflation. Neither is decisive.

### 4. Negative f_NL
Bounce: Predicts f_NL < 0 (from matter contraction growth of ζ). This is a GENERIC feature.
Inflation: Predicts f_NL ≈ 0 (single field) or f_NL > 0 (most multi-field). Negative f_NL from inflation requires contrived constructions.

**This is a genuine observational difference. If f_NL < 0 is measured, the bounce has a natural explanation while inflation does not.**

### 5. Blue Tensor Tilt
Bounce: n_T > 0 (blue).
Inflation: n_T < 0 (red) — this is a consistency relation (n_T = −r/8).

**If r is too small to measure, n_T is unmeasurable in both cases.**

---

## Honest Assessment

| Criterion | Bounce + Curvaton | Starobinsky R² | Winner |
|-----------|-------------------|----------------|--------|
| Parameter count | 3 | 1 | Inflation |
| n_s | Tuned | Predicted | Inflation |
| r | ~10⁻⁴ (untestable) | 0.004 (testable) | Inflation (more predictive) |
| f_NL | **−3.7 (testable, distinctive)** | ~0 (undetectable) | **BOUNCE** |
| Singularity | Resolved | Unresolved | Bounce (theoretical) |
| Trans-Planckian | Absent | Present | Bounce (theoretical) |
| BKL stability | **UNSOLVED** | N/A | Inflation (no issue) |
| Theoretical economy | Moderate | Excellent | Inflation |

**Overall:** Inflation (especially Starobinsky) is currently a better fit in terms of economy and predictiveness. The bounce model's single advantage is the **negative f_NL prediction**, which is the one observable that could FLIP the comparison if measured.

**The honest bottom line:** The bounce model is NOT currently better than inflation. It is CONDITIONALLY better — it becomes better IF f_NL < 0 is measured. This is a concrete, testable prediction that could be resolved by MegaMapper (~2035).

---

## What Would Make the Bounce Model Decisively Better?

1. **MegaMapper measures f_NL = −3.7 ± 0.5** → inflation is in serious trouble, bounce is vindicated
2. **LiteBIRD finds r < 0.001** → Starobinsky is disfavored (but many inflation models survive), bounce is consistent
3. **Both 1 and 2** → bounce is strongly favored over all standard inflation models
4. **Birefringence confirmed at 5σ+** → supports the ALP ingredient (independent of bounce, but consistent with the framework)

**The research priority is making the f_NL prediction as sharp and robust as possible.**
