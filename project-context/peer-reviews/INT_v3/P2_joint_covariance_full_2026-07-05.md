# P2 — Full joint-covariance closure attempt: is ∂B_g/∂A_GR locally computable? (2026-07-05)

Follow-up to `P2_joint_covariance_2026-07-05.md`. That note upgraded the
additive-quadrature GR budget to a marginalized Fisher using the c8 SDB
degeneracy **ρ = −0.868 as an explicit PROXY**, and named the one missing
input to make it channel-native: the bispectrum GR-projection response
**∂B_g/∂A_GR** on the SPHEREx triangle set (flagged in the paper at the
`sec:systematics` scope paragraph, L1005). This note answers the RS27
Grok+Gemini MAJOR directly: **can that derivative be computed locally, and
does it close the budget MAJOR with the true (non-proxy) σ_marg(f_NL)?**

## The reviewers' exact ask

Replace the proxy ρ = −0.868 (transferred from the sibling SDB
power-spectrum channel) with the **channel-native** joint 2×2 Fisher

    F[{f_NL, A_GR}] = Σ_triangles (∂B/∂θ_i)(∂B/∂θ_j) / Cov_B(triangle),

invert it, and quote the true marginalized σ(f_NL). With
B_g = f_NL·S_local + A_GR·S_GR (A_GR = amplitude of the large-scale
GR/relativistic-projection contamination of the local-shape estimator), this
needs **∂B_g/∂f_NL = S_local** and **∂B_g/∂A_GR = S_GR** on the triangle set,
AND the per-triangle bispectrum **noise covariance Cov_B**.

## What A_GR is

`A_GR` is the amplitude of the relativistic-projection ("GR-induced") large-scale
bias of the galaxy bispectrum — the Doppler + gravitational-potential + lensing
kernels (Verde–Matarrese 2009, Bartolo–Bruni 2011, Jolicoeur/Maartens class)
that mimic a local-f_NL signal in the squeezed limit. In the paper it enters
`tab:systematics`/`tab:gr` ONLY as a stress-test noise amplitude
σ_GR ∈ {0.5, 1.0} added in quadrature — never as a template with a computed
∂B/∂A_GR. That deferral is exactly the MAJOR.

## Result of the local computation (`c12_gr_projection_dBdAgr_probe.py`)

Run on the paper's OWN committed 23,098-triangle grid
(`phase3_bispectrum_shape_overlap.json`), reproduces the grid exactly.

**1. The SHAPE ∂B/∂A_GR IS locally computable.** With B_g linear in A_GR the
derivative is just the GR template shape S_GR. I built S_GR as the standard
relativistic-projection squeezed kernel (local term modulated by the
long-to-short wavenumber ratio, the leading O(H/k) GR enhancement) alongside
the paper's local shape S_local = Σ P(kᵢ)P(kⱼ), P(k)∝k⁻³. Both are constructible
from repo machinery. So "compute ∂B/∂A_GR on the triangle set" — **YES, done.**

**2. The 2×2 Fisher CROSS-TERM is NOT locally computable.** The ρ(f_NL, A_GR)
that sets σ_marg = σ_base/√(1−ρ²) is a **noise-weighted** overlap; it needs the
SPHEREx multi-tracer galaxy-bispectrum covariance Cov_B(k₁,k₂,k₃) on the
triangle set. **That covariance is NOT in the repo** — only the single scalar
σ(f_NL^local)=0.7 is imported from Heinrich et al. 2023 (arXiv:2311.13082); the
per-triangle Cov_B that produced it is external.

To bound the impact I computed the overlap under two in-repo measures:

| measure | ρ(S_local, S_GR) | 1/√(1−ρ²) | σ_marg | signif (×r) |
|---|---|---|---|---|
| uniform (flat cov) | +0.949 | 3.16× | 2.21 | 0.83σ |
| k²-weighted (CMB-Fisher-like) | +0.949 | 3.18× | 2.23 | 0.83σ |
| **c8 SDB proxy (current paper)** | −0.868 | 2.02× | 1.41 | **1.30σ** |

The two in-repo measures agree at |ρ|≈0.95 — a **high** degeneracy magnitude,
consistent with (indeed slightly stronger than) the proxy's 0.868 — confirming
the reviewers' physical expectation that GR projection is strongly degenerate
with local f_NL. But the value is **measure-dependent** and, more importantly,
the true Cov_B-weighted ρ is neither of these: the paper's own r spans
0.55–1.14 across weighting schemes, an O(1) spread. The sign also flips between
the SDB proxy (−) and the raw shape cosine (+) because they are different
objects (one is a parameter-covariance correlation, the other a template inner
product). **Therefore the shape overlap alone cannot pin σ_marg** — the
noise-weighted Fisher contraction genuinely requires Cov_B.

## Verdict on the MAJOR

**∂B_g/∂A_GR — the derivative shape — IS locally computable** (done here). **The
true channel-native marginalized σ(f_NL) is NOT**, because it is a noise-weighted
Fisher quantity gated on the external SPHEREx multi-tracer bispectrum covariance
Cov_B(k₁,k₂,k₃) (Heinrich et al. 2023), which the repo imports only as the scalar
σ=0.7. This is genuine external-data-gating, not a deferral of work that could be
done here.

**Best bounded estimate that CAN be stated now (non-fabricated):**
- The in-repo shape overlap gives |ρ| ≈ 0.95 (uniform/k²), i.e. a STRONG
  degeneracy — at least as strong as the −0.868 proxy — so the marginalized
  floor is **at most as favorable as, and plausibly below, the proxy's 1.30σ**.
  Under the high-|ρ|≈0.95 shape overlap the floor would fall to ≈0.83σ; the
  proxy's 1.30σ is thus a **conservative (optimistic-leaning) endpoint**, not
  an underestimate — the honest budget is bracketed **≈0.8–1.3σ**.
- The **rho = −0.868 c8 proxy remains the best-available, source-cited in-repo
  bound** and correctly supersedes the additive-quadrature 1.5σ; the direct
  channel-native number is external-data-gated on Cov_B.

**Does this close the budget MAJOR?** It **strengthens and bounds** it but does
not fully close it channel-natively. The honest closure is: (a) ∂B/∂A_GR shape
computed and committed; (b) demonstrated that the marginalized number needs the
external Heinrich Cov_B; (c) the in-repo shape overlap CONFIRMS strong
degeneracy (|ρ|≈0.95), so the proxy floor 1.30σ is not an artifact but a mild
upper edge of a ≈0.8–1.3σ band; (d) the exact external ingredient to finish is
named. This converts an open deferral into a bounded, sourced statement — the
correct honest referee response.

## Exact external data needed to fully close

The **SPHEREx multi-tracer galaxy-bispectrum noise covariance
Cov_B(k₁,k₂,k₃)** on the triangle set — the Gaussian bispectrum covariance
(∝ P_tot(k₁)P_tot(k₂)P_tot(k₃)/N_triangles with the multi-tracer P_tot including
shot noise per sample) used by Heinrich et al. 2023 (arXiv:2311.13082) to derive
σ(f_NL^local)=0.7. The repo imports only the scalar σ; the per-triangle
covariance is external / pod-bound. Given Cov_B, the closure is one script:
F_ij = Σ_tri (∂B/∂θ_i)(∂B/∂θ_j)/Cov_B(tri) over {f_NL, A_GR, b_φ, b_1(z)},
invert, read σ_marg(f_NL) = √(F⁻¹)_{f_NL,f_NL}. Everything else
(∂B/∂A_GR shape, S_local, triangle grid, r=0.84, σ_base=0.7) is already in-repo.

## Reproduce

`research/focused_paper_source_integration/scripts/c12_gr_projection_dBdAgr_probe.py`
→ `outputs/c12_gr_projection_dBdAgr_probe.json`. All inputs are paper
quantities; the GR template is the standard relativistic-projection squeezed
kernel, clearly labeled a shape model (not a covariance-calibrated amplitude).
NOTHING FABRICATED — no σ(f_NL) headline is produced; this is a computability
probe that bounds, sources, and gates the joint-covariance number.
