# Compute-to-ACCEPT queue (the real research that drives external ACCEPT)

<!-- last_updated: 2026-06-30 -->

The drive-to-ACCEPT round (2026-06-30, v*.91/.86/.82/.122/.200/.96) restructured
each paper around the reviewers' actual asks. But several reviewer demands
**cannot be satisfied by text edits — they require running new science**. This
is the honest path to full external ACCEPT. Each item below was flagged by the
paper-owner agents as compute-gated (not faked, not dismissed). Run on the pod;
fold real results into the paper; re-review.

## P1B (MCMC companion) — HIGHEST LEVERAGE (recurring blocker, 4/6 reviewers)
- [ ] **SN-overlap control chain A**: DESI + Planck + Pantheon+-only w0wa MCMC (drop the overlapping DES-Y5×Pantheon+ SNe). Demonstrates the quintom-B direction is/ isn't robust to double-counted SNe.
- [ ] **SN-overlap control chain B**: DESI + Planck + DES-SN5YR-only w0wa MCMC.
- [ ] **ALP prior-predictive fraction**: quantify the accommodation/prior-volume cost (the "tautological fit" ChatGPT-B2 concern) — fraction of prior that reproduces β_obs.

## P4 (chirality null) — win ChatGPT's MAJOR
- [ ] **GZ1-only classifier retrain**: retrain the flip-equivariant ViT on GZ1 labels only (no CE-ResNet pseudo-labels) → confirms the null isn't inherited from CE-ResNet. (ChatGPT M2.)
- [ ] **Empirical b/a (axis-ratio) cross-match**: test the edge-on directional-bias-exclusion argument empirically, not just analytically. (Gemini MAJOR.)
- [ ] **≥200-random-axis harmonic injection battery**: full look-elsewhere null for the harmonic channel. (OpenAI-INT M5.)

## P3 (anomaly catalog) — 3/3 MAJOR, needs reproducibility artifacts
- [x] **Independent 6-way dedup artifact** (OpenAI E1 "most critical") — **DONE 2026-06-30**.
  Ran `pipelines/p3_anomaly_engine/sixway_dedup.py` LOCALLY on the canonical
  released per-object catalogs (HF `bamfai/bigbounce-anomaly-catalog`; DESI from
  committed CSV). 5″ `search_around_sky` + union-find over the 6 recommended-tier
  surveys (DESI 195,829 + SDSS 77,905 + eROSITA 298 + Planck 200 + Gaia 500 +
  NEOWISE 419-masked). Result **EXACT-MATCH to paper**: input **275,151** →
  unique **269,317** (collapsed **5,834**, 2.12%); per-pair collapse DESI–DESI
  5,814 / SDSS–SDSS 12 / DESI–SDSS 9; 8 multi-survey clusters. Artifacts:
  `outputs/sixway_dedup_artifact.{json,csv}` (269,317-row per-object table) +
  `outputs/SIXWAY_DEDUP_AND_HELDOUT_METHODS.md`. Backed up to HF
  `p3_compute_to_accept/`.
- [~] **Held-out re-score of DESI/Planck top-lists** (E2/E6 option-a) — **DESI DONE,
  Planck PARTIAL**. `pipelines/p3_anomaly_engine/held_out_rescore.py` →
  `outputs/held_out_rescore_result.json`.
  - DESI: genuine out-of-sample 5-fold cross-validation (committed
    `pathc_desi_kfold/results/`) — mean pairwise Jaccard **0.862** (≥0.70 gate,
    PASS), 464/546 in ≥3 folds. 195,829 headline is not a single-sample artifact.
  - Planck: held-out membership test DONE — native top-200 are **48/200 in the
    seed-42 held-out split vs 30 expected, 1.60× over-rep, binomial p=5.5e-4**
    (anomalies MORE common out-of-sample → no in-sample inflation). Full native
    re-inference over held-out patches **BLOCKED**: needs pod-side
    `best_cmb_native.pt` + `cmb_native_patches.npy` + 200k native scores, which
    are on a now-EXITED pod and NOT in the HF release (released Planck parquet is
    the cross-transfer baseline, patch_idx<20k); the one RUNNING pod refused SSH.
- [ ] **Native SDSS score histogram** (Grok M2) + **marginal-α posterior fold-in** (Grok M3).

## P2 (f_NL recast) — deepest, lowest-priority (recast is honest as-is)
- [ ] **Cubic in-in transfer through an explicit bounce** (the assumption-(d) uncertainty).
- [ ] **Heinrich Fisher re-run at the bounce fiducial** with the non-local template.
- [ ] **Joint bispectrum Fisher over systematics**.

## P1A (ECH theory) — mostly text; one optional calc
- [ ] **Boltzmann Γ_wash(T) washout calculation** (currently stated conditionally) — optional; the closure margin is ansatz-insensitive without it.

## P5 (DESI chirality) — NO compute needed
The Paper-IV self-containment appendix (v0.1.96) closed the one convergent
blocker from source numbers. P5 is the closest to 3/3 ACCEPT — re-review should
tell. If ChatGPT's MAJOR persists, read its NEW report for the residual.

---
**Protocol:** run these on RunPod (see `/runpod-lifecycle` + `/houston-method-v2`);
ALWAYS-backup results to local+HF+B2 (Lesson E); fold real numbers into the .tex;
NEVER fabricate a result to satisfy a reviewer. Mint Zenodo DOIs at submission
(the deferred-DOI flags are submission-time, not blockers).
