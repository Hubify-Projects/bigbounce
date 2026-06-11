# Convex P4 focusAreas / notables fixes — for wave 2 to push via the bump tool

**Found by the 2026-06-10 site polish wave (QA P0-4).** The /papers/paper-4 page
contradicts itself: the abstract correctly discloses that the −0.122σ
subsample-mask null was **withdrawn in v1.0.166**, but the Convex-driven
"Focus areas" and "Notable contributions" blocks still present it as the
load-bearing headline, keep the "~18σ formally excluded" phrasing (paper
softened to ">99% confidence" in v1.0.151), and `papers.ts` keyResults still
says "Definitively refutes Shamir 2020" (Shamir-refutes shorthand removed from
the paper in v1.0.151).

These strings could NOT be fixed by this wave because they live in Convex
(`papers.focusAreas`, `notables` table) and in `site/src/data/papers.ts`
(excluded surface owned by wave 2). Verified live against
`https://brilliant-panther-471.convex.cloud` on 2026-06-10.

---

## 1. `papers` table — paper-4 `focusAreas` (replace the array)

Current (stale) → corrected, in order:

1. ~~`Subsample-mask −0.12σ MASTER-deconvolved load-bearing null`~~
   → `Real-space ℓ=1 dipole headline: +0.41σ (empirical-rank p=0.31, fixed null generator; A_dip < 6.8×10⁻³ at 95% UL) — earlier −0.122σ subsample-mask MASTER null withdrawn in v1.0.166 (synthetic-footprint provenance, Appendix A)`

2. ~~`v1.0.139 joint nuisance-marginalized fit: interpretation (i) at 1.7% f_CW formally excluded at ~18σ under block-bootstrap σ (NSIDE=8 super-pixels, N_boot=1000) — naive WLS gave 264σ, but residual is spatially coherent`~~
   → `Joint nuisance-marginalized template fit: a clean 1.7% f_CW dipole excluded at >99% confidence (z≈−18 under the adopted block-bootstrap error model, NSIDE=8 super-pixels, N_boot=1000; residual is spatially coherent)`

3. ~~`Canonical-mask +3.64σ three-interpretation closure (interpretation (ii) coherent depth/morphology systematic favored by 5+ anchors)`~~
   → `MASTER channel as systematics diagnostic: +7.28σ on the real apodized footprint, unchanged under depth-stratified nulls — coherent depth/morphology survey systematic (interpretation (ii)), not cosmology`

4. `ℓ=2 cross-spectrum r=−0.65 σ=−2.89 vs pixel-density proxy` — KEEP (still in the v1.0.173 diagnostic set).

5. `MASTER-decoupled monopole-only null × 500 (88% unexplained by monopole-only leakage)` — REVIEW: this null supported the withdrawn subsample-mask channel; confirm against v1.0.173 §/Appendix A before keeping, otherwise drop.

6. `Shamir 2020 vs 2022 split with arXiv IDs (post-R22 Perplexity BL-1)` — KEEP.

## 2. `notables` table — paper-4 rows

- `_id: md7arn2ke10fp2yrfax44a0t918818qk` (ordinal 2)
  ~~`Headline null $\ell=1$ chirality-dipole observable: subsample-mask pseudo-$C_1$ at $-0.12\sigma$, consistent with no dipole`~~
  → `Headline $\ell=1$ chirality-dipole observable: real-space dipole at $+0.41\sigma$ (empirical-rank $p=0.31$; $A_{\rm dip} < 6.8\times10^{-3}$ at 95% UL) — the earlier $-0.12\sigma$ subsample-mask pseudo-$C_1$ null was withdrawn in v1.0.166 after a provenance audit`

- ordinals 1, 3, 4 — KEEP (consistent with v1.0.173).

## 3. `site/src/data/papers.ts` (wave-2-owned, line ~371)

- ~~`Definitively refutes Shamir 2020 3% cosmic parity violation claim`~~
  → `Shamir 2020 3% parity-violation claim not reproduced: clean 1.7% dipole excluded at >99% confidence under the adopted error model` (paper dropped the "refutes Shamir" shorthand in v1.0.151)

## Done elsewhere this wave (no action needed)

- Legacy `/galaxy-explorer` embed: Shamir "REFUTED" → "Not reproduced", 0.43σ
  → +0.41σ, stat-strip counts → canonical, ~0.3% → A_dip < 6.8×10⁻³ 95% UL
  (commit cf2d921e).
