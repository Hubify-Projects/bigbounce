# P4 INT — FINAL pre-arXiv referee review (Claude Code INT leg, full source access)

**Paper:** P4 v1.0.217 — `pipelines/p2_chirality/chirality_catalog_paper.tex`
**Reviewer:** Claude Code INT leg (Houston subscription), read-only, artifact-verified
**Date:** 2026-07-05 (FINAL_ROUND); performed 2026-07-06
**Repo state:** HEAD `6ab357a7`; `CODE_2025/bigbounce` is a symlink to `CODE_YOU/bigbounce` (same tree).

## VERDICT: ACCEPT — publish-ready confirmed.

**Central-claim assessment:** The headline scientific claim — a real-space
chirality dipole consistent with null (+0.41σ) on 8.47M DESI Legacy galaxies,
with the harmonic-channel residuals honestly demoted to systematics diagnostics
and a block-bootstrap WLS template fit disfavoring a clean 1.7% dipole at z≈−18 —
is **fully supported by committed artifacts and internally consistent** across
abstract, body, tables, figures, and appendices. Every number I checked
reproduces digit-for-digit from on-disk JSONs. The paper is unusually and
correctly caveated: it never overclaims a detection, never claims a frequentist
exclusion of Shamir's Ganalyzer, and repeatedly labels non-primary σ values as
systematics-attributed diagnostics.

## Genuinely-new real findings: NONE.

No MAJOR. No MINOR that rises above disclosed/cosmetic. Nothing a fresh referee
would catch that prior rounds missed.

## Numbers verified against committed artifacts

| Paper claim | .tex loc | Artifact | Artifact value | Match |
|---|---|---|---|---|
| HC dipole +0.41σ, p=0.31 | L531, L831, L656 | `outputs/dipole/catalog_c_summary.json` | sig=0.4080, p=0.3085 | ✓ |
| shuffle-null z=0.58 | L531, L831 | same (`shuffle_null`) | 0.5789 | ✓ |
| indep re-impl z=0.70 / z=0.55 | L831 | `c11b_hc_dipole_nulls.json` | per-gal 0.696, pix-perm 0.545 | ✓ |
| HC f_sky=0.4801, N_HC=949,584 | L656, L616 | `catalog_c_summary.json` | 0.48014, 949584 | ✓ |
| WLS z≈−18.1, best-fit 0.455% A_p | L924, L1005 | `joint_nuisance_bootstrap_sigma.json` | A=0.004553, σ_boot=0.00163 → −18.1 | ✓ |
| forward-model imaging ~52%, +0.7σ, cos=0.83 | L924 | `systematic_l1_forward_model.json` | frac=0.5236, σ=0.729, cos=0.835 | ✓ |
| +DR8 morph 52.4→53.0%, ~47% open | L924 | `systematic_l1_forward_model_dr8morph.json` | 0.5236→0.5302, remainder 0.470 | ✓ |
| GZ1-human-only z=−0.54/−0.55, N=46,017, CWfrac 0.4836, amp 0.0546 | L972 | `gz1only_fullN_dipole_result.json` | −0.539/−0.55, 46017, 0.4836, 0.0546 | ✓ |
| edge-on tie-break BASS z=+0.31, DECaLS z=+4.72 | L1247 | `per_leg_confidence_familywise_maxstat.json` | 0.3148, 4.724 | ✓ |
| CW/CCW counts 1,592,107 / 1,609,053; N_spiral 3,201,160 | L746 | catalog stats consistent | exact | ✓ |

## Compile / hygiene

- PDF compiled Jul 6 18:27; page 1 shows "(Dated: July 5, 2026)" = `\paperTimestamp`.
  Version tag intentionally stripped from title block (changelog P4-E1/E6) — only
  timestamp emitted. Consistent with directive.
- **0 real undefined references** (log's lone "undefined" hit is a cosmetic
  `OT1/cmr/bx/sc` font-shape warning).
- Citations: 20 cited keys, **all resolve** to bibitems (0 missing). 20 unused
  bibitems retained under `longbibliography` — harmless, PRD-acceptable.

## Minor observations (non-blocking, no action required)

- (obs-1) The block-bootstrap artifact `joint_nuisance_bootstrap_sigma.json` uses
  a `|b_gal|>15°` mask rather than the canonical `N_spiral≥10` mask. This is
  **explicitly disclosed in the artifact's own `_mask_equivalence_note`** (both
  give A_dipole to 4 sig figs, n_super_pixels=440) and the paper honestly scopes
  it as "under the adopted NSIDE=8 block-bootstrap error model." Not a defect.
- (obs-2) The `gz1only_fullN_dipole_result.json` `date_utc` is 2026-07-06 (run
  today), i.e. freshly regenerated for this closure — consistent with v1.0.214/217
  changelog; values match paper. Confirms the pseudo-label-independence closure is
  real, not stale.

## Bottom line

P4 v1.0.217 is arXiv-submission-ready from the INT full-source referee standpoint.
Central null-dipole claim is genuine, conservative, and artifact-backed; no
fabrication; no overclaim; no stale numbers; 0 undefined refs; all cites resolve.
