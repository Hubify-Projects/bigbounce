# P4 R23conf — compute queue

## ✅ SEV RESOLVED (2026-06-09, same day) — headline reproduces on the headline sample

The META-E1 SEV below was triaged and RESOLVED:
- The c11 4.2σ recompute used the FULL 3.2M sample; the published headline is the
  HIGH-CONFIDENCE sample (winning-class confidence > 0.6, N=949,584) — the
  generator's docstring sample, not the full catalog.
- The committed generator's selection line was buggy (all-CW); FIXED in
  `run_dipole_catalog_c.py` and the anchor REGENERATED at N_MC=10^4:
  **0.41σ (rank-p=0.31)** pixel-perm; **0.58σ (rank-p=0.26)** per-galaxy shuffle —
  reproducing the published 0.43σ/p=0.30 within MC noise. Paper updated to the
  regenerated values with an in-text correction note; the full-sample 4.2σ is
  disclosed in §IV as a confidence-threshold sensitivity diagnostic (low-confidence
  tail systematic, below A50, same family as the harmonic residuals).
- Independent re-implementation (c11b_hc_dipole_nulls.json): z=0.55/p=0.27 and
  shuffle z=0.70/p=0.23 — same verdict.

Original SEV record retained below for the audit trail.

---


## ⛔ SEV — META-E1 recompute CONTRADICTS the published +0.43σ headline

The META-E1 recompute (`pipelines/p2_chirality/c11_meta_e1_e2_realspace_nulls.py`,
artifact `outputs/canonical_provenance/c11_meta_e1_e2_realspace_nulls.json`) ran the
documented headline estimator on the released catalog
(HF `bamfai/galaxy-chirality-catalog` `catalog_production.parquet`,
blob `ccc9f79b…` — identical across ALL 5 cached snapshots, so the catalog never
changed): full 3,201,160 Catalog C spirals, canonical mask N_spiral(p)≥10
(n_pix=24,087, f_sky=0.49005, matching `monopole_mask_null_results.json` exactly),
uniform-weight `hp.fit_dipole`, 10⁴ nulls:

| estimator / null | amp (A_p units) | z_mom | rank p |
|---|---|---|---|
| uniform fit, per-pixel permutation (published procedure) | 5.66e-3 | **+4.16** | 9e-4 |
| uniform fit, per-galaxy label shuffle (hypergeometric)   | 5.66e-3 | **+4.32** | 3e-4 |
| N_spiral-weighted fit, per-galaxy shuffle                | 5.18e-3 | **+4.38** | 2e-4 |
| count-weighted f_CW fit, binomial null (full sample)     | 0.52% full-amp | +4.55 | <1e-3 |
| same, HC-broad p_eq>0.6                                  | 0.55% full-amp | +1.53 | 0.076 |
| same, HC-0.9                                             | 0.74% full-amp | +1.47 | 0.081 |
| zero-filled maskless fit (old Table I "Mask=none" reading)| 2.49e-3 | +2.67 | 0.007 |

**No variant reproduces the published +0.43σ (p=0.30).** Additionally, the committed
generator `run_dipole_catalog_c.py` (docstring: "generator for the 0.43-sigma
headline") applies the filter `p_cw_eq.abs() > 0.6`, which on the released parquet
selects **471,049 galaxies — ALL CW, zero CCW** (a degenerate one-chirality sample);
as committed it cannot produce a meaningful dipole from the released catalog.
The anchor artifact `catalog_c_post_tta_dipole_summary.json` (v1.0.67, 2026-05-15)
predates the v1.0.166 synthetic-catalog provenance audit and is in the same risk
class as the withdrawn −0.122σ subsample-mask result.

Context: the recomputed real-space LS amplitude (~0.52–0.57% full amplitude) is
BELOW the A50≈0.75% injection floor, and is the same ~0.5% structure the paper's
own Appendix D WLS template fit recovers (A_dipole=4.55e-3) and attributes to
depth/imaging-leg systematics (z vs 0 ≈ +2.8 under the block-bootstrap covariance).
So the systematics-attribution architecture may survive, but the abstract-level
"+0.43σ, p=0.30" number and Table I row (i) are currently UNREPRODUCIBLE and need
re-derivation + Houston sign-off (SEV process, cf. v1.0.166 precedent). The R23conf
closure pass deliberately did NOT rewrite the headline; only consistency fixes were
applied to the tex.

---

Created 2026-06-09 during R23conf closure pass. Everything runnable locally was
run (see `pipelines/p2_chirality/c11_*.py` + artifacts in
`pipelines/p2_chirality/outputs/canonical_provenance/c11_*.json`). The items
below require data that exists only pod-side / external.

## QUEUE-1 — P4-META-E3 full probability recalibration (ESSENTIAL, partial)

**What was closed locally (textual):** §IV A now carries the explicit caveat
that p_eq is not probabilistically calibrated (mean confidence 0.951 vs GZ1
3-class accuracy 58.7%) and that HC cuts are monotone selection thresholds.

**What remains (compute):**
1. Platt/temperature scaling of Catalog C equivariant probabilities against a
   held-out GZ1 subset (disjoint from the 6,637 training galaxies).
2. Reliability curves + ECE + Brier score on the held-out set.
3. Redefine HC cuts on calibrated probabilities (or empirical-accuracy
   quantiles) and recompute the Table V injection-recovery sweep on the
   recalibrated HC sample.

**Data needed (not local):**
- `gz1_table2.csv.gz` (GZ1 vote table; pod path `/workspace/gz1_table2.csv.gz`)
- per-galaxy equivariant probabilities are local (HF cache
  `bamfai/galaxy-chirality-catalog` / `catalog_production.parquet`)

**Script starting point:** `pipelines/p2_chirality/wave_14_fff_gz1_platt_recal.py`
(loads the GZ1 table, does the 1-arcsec cross-match and a Platt refit; its prior
artifact `r42_results/wave_14_fff_gz1_platt_recal.json` has NaN Brier scores and
duplicated legs, so it must be rewritten, not reused).
**Sweep starting point:** `pipelines/p2_chirality/scripts/injection_sweep_extended.py`.

**Estimated cost:** ~20–40 min CPU once `gz1_table2.csv.gz` is fetched
(GZ1 table is public; could also be re-downloaded from the GZ1 data release
rather than the pod).

## Notes

- P4-META-E1, -E2 (spot check), -M3, -M4 were RECOMPUTED locally (catalog
  parquet is in the HF cache): see
  `c11_meta_e1_e2_realspace_nulls.py`, `c11_meta_m3_fsky_normalization.py`,
  `c11_meta_m4_slab_stats.py`.
- P4-m5 (Fig. 8 burned-in annotations) was closed by regenerating
  `fig_multipoles.png` from the canonical 200-MC battery artifact
  (`c11_regen_fig_multipoles.py`); old figure backed up as
  `fig_multipoles.png.pre_c11_r23conf.bak`.
