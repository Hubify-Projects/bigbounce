# P2 — Joint-covariance forecast vs additive-quadrature heuristic (2026-07-05)

**Reviewer MAJOR (shared, harsh reviewers):** the systematic-error budget
(Table `tab:systematics`) is an ADDITIVE-QUADRATURE HEURISTIC —
σ_eff = √(σ_base² + Σᵢσᵢ²) — not a JOINT-COVARIANCE / marginalized Fisher
forecast. Adding systematics in the denominator in quadrature assumes each
nuisance is *independent* of f_NL. The honest treatment marginalizes f_NL over
the nuisance parameters via the inverse Fisher matrix, which for correlated
parameters gives a DIFFERENT (generally larger) σ(f_NL).

## What the paper already has (not fabricated)

- **Bispectrum channel headline:** σ_base = 0.7 (Heinrich et al. imported,
  already b_φ-marginalized under UMF), template overlap r = 0.84
  (Eq. `eq:r_noise`), central |f_NL| = 35/16 = 2.1875 →
  σ(f_NL^bounce)=0.7/0.84=0.833 → **2.63σ optimistic** (matches paper).
- **Quadrature budget (Table `tab:systematics` / `tab:gr`):**
  σ_GR = 0.5 → σ_eff=0.86 → 2.14σ; σ_GR = 1.0 → σ_eff=1.22 → **1.50σ floor**.
- **A REAL joint Fisher already exists for the SIBLING SDB power-spectrum
  channel** (`outputs/c8_fnl_running_fisher.json`, CAMB 1.6.6, Planck 2018,
  Doré+2014-validated SPHEREx products). Its 2×2 (f_NL, n_fNL) Fisher matrix
  is committed. I re-inverted it independently:
  - marginalized σ(f_NL)=√(F⁻¹)₀₀ = **3.078** (paper: 3.078) ✓
  - unmarginalized 1/√F₀₀ = **1.529** (paper: 1.529) ✓
  - implied ρ(f_NL,n_fNL) = −F₀₁/√(F₀₀F₁₁) = **−0.868** (paper: −0.87) ✓
  - +bias co-marginalized: σ=7.06, ρ=−0.97, 4.6× degradation.

## Joint Fisher setup and the marginalized number

For a 2-parameter Gaussian Fisher {f_NL, A_GR} with unmarginalized errors
s_f = σ_base, s_G, and correlation ρ, the standard inverse-Fisher result is

  **σ_marg(f_NL) = σ_base / √(1 − ρ²).**

This is structurally DIFFERENT from quadrature: quadrature adds s_G in the
*noise denominator* (σ_eff=√(σ_base²+s_G²)); marginalization *inflates* σ_base
by 1/√(1−ρ²). Quadrature is only recovered in the degenerate ρ=0,
independent-nuisance limit — exactly the assumption the reviewers reject.

| Treatment | σ(f_NL) | signif. (×r) |
|---|---|---|
| Optimistic (no sys) | 0.700 | 2.63σ |
| **Quadrature** σ_GR=1.0 (paper floor) | 1.221 (σ_eff) | **1.50σ** |
| **Joint Fisher, ρ=−0.87** (paper's own c8 degeneracy) | 1.420 | **1.29σ** |
| Joint Fisher, ρ=−0.97 (c8 +bias) | 2.879 | 0.64σ |
| Joint Fisher, ρ=0.5 | 0.808 | 2.27σ |

## Verdict

**The marginalized significance is WORSE than the quadrature number, not
similar.** At the paper's own directly-measured degeneracy strength (ρ=−0.87,
the only CAMB-computed correlation in the paper), the honest marginalized
f_NL error is 1.42 vs the quadrature σ_eff=1.22 — the conservative floor drops
from **1.50σ → 1.29σ**. The parameters are strongly degenerate (|ρ|≈0.87–0.97
in the sibling channel), so the near-orthogonal ρ→0 case that would justify
quadrature is empirically excluded by the paper's own Fisher.

**Does this close the MAJOR?** PARTIALLY, and honestly:

1. For the **SDB power-spectrum channel** the paper ALREADY replaced quadrature
   with a real joint covariance (c8) — that part of the MAJOR is closed.
2. For the **bispectrum-only headline**, a *fully* self-consistent joint
   covariance needs one input the paper does NOT contain: the **bispectrum
   response derivative ∂B_g/∂A_GR** (the GR-projection template's cross-Fisher
   term with f_NL). The paper explicitly states σ_GR is a *stress-test
   amplitude* "not calibrated to [Addis et al.'s] Fisher results" (L999) and
   that "a full joint bispectrum covariance is the one element still combined
   heuristically" (L971). **This is the precise missing input.**

## Best honest bounded joint estimate (what CAN be done now)

Import the paper's OWN measured degeneracy ρ=−0.87 as the joint-covariance
proxy for the bispectrum GR nuisance (physically motivated: GR projection and
scale-dependent bias both act on the same ultra-large-scale f_NL modes, so a
comparably strong anti-correlation is expected). This upgrades the heuristic
1.50σ floor to a **marginalized 1.29σ** — a real, source-cited number, flagged
as a proxy pending the bispectrum ∂B/∂A_GR derivative. This is a genuine
improvement over re-badging: it shows the marginalized floor is ~14% lower than
quadrature and specifies exactly what compute closes the gap fully
(a bispectrum-triangle Fisher with a GR-projection template column).

## Missing input to fully close (the honest ask)

Compute the multi-tracer galaxy-bispectrum Fisher F_{ij} over
{f_NL, A_GR, b_φ, b_1(z)} with the GR-projection template B_GR(k₁,k₂,k₃)
(Doppler + gravitational-redshift + lensing kernels, Addis/Jolicoeur 2025) as
an explicit nuisance column, then σ_marg(f_NL)=√(F⁻¹)_{f_NL,f_NL}. Required
new ingredient not in the repo: **∂B_g/∂A_GR** on the SPHEREx triangle
configuration set. Everything else (CAMB transfer M(k,z), σ_base=0.7, r=0.84,
c8 machinery) is already in-repo.

## Reproduce

`/tmp/p2_joint_cov.py` — all inputs are paper quantities; the 2×2 inversion is
validated against the committed `c8_fnl_running_fisher.json` to 3 decimals.
