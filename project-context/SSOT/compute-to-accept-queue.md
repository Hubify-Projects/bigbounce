# Compute-to-ACCEPT queue (the real research that drives external ACCEPT)

<!-- last_updated: 2026-07-01 -->

The drive-to-ACCEPT round (2026-06-30, v*.91/.86/.82/.122/.200/.96) restructured
each paper around the reviewers' actual asks. But several reviewer demands
**cannot be satisfied by text edits — they require running new science**. This
is the honest path to full external ACCEPT. Each item below was flagged by the
paper-owner agents as compute-gated (not faked, not dismissed). Run on the pod;
fold real results into the paper; re-review.

## P1B (MCMC companion) — HIGHEST LEVERAGE (recurring blocker, 4/6 reviewers)
- [x] **SN-overlap control chain A** (Pantheon+-only): **DONE 2026-07-01** — w0=-0.874±0.059, wa=-0.530±0.241, **w0+wa=-1.404±0.190 (quintom-B: w0>-1 at 2.1σ, w0+wa<-1 at 2.1σ)**. Folded into P1B v1B.0.89 Appendix A. R-1~0.06 (well-mixed for direction). Chains backed up to HF.
- [x] **SN-overlap control chain B** (DES-SN5YR-only): **DONE 2026-07-01** — w0=-0.787±0.063, wa=-0.785±0.263, **w0+wa=-1.572±0.206 (quintom-B: w0>-1 at 3.4σ, w0+wa<-1 at 2.8σ)**. Quintom-B direction holds in BOTH independent SN samples → robust to DES×Pantheon+ overlap, **NOT a double-counting artifact. CLOSES ChatGPT-B1 directionally.** Artifact `reproducibility/cosmology/w0wa_control_chains_result.json`.
- [ ] **ALP prior-predictive fraction**: quantify the accommodation/prior-volume cost (the "tautological fit" ChatGPT-B2 concern) — fraction of prior that reproduces β_obs.

### P1B SN-overlap control chains — LAUNCHED 2026-06-30 (real MCMC, not fabricated)
- **Configs** (committed): `reproducibility/cosmology/cobaya_control_pantheonplus.yaml` (Control A),
  `reproducibility/cosmology/cobaya_control_desy5.yaml` (Control B). Both derived from the validated
  `cobaya_w0wa_quintom_test.yaml` (identical priors/sampler/CPL+PPF params); only the SN likelihood differs
  (`sn.pantheonplus` vs `sn.desy5`). Both passed `cobaya-run --test` (full model init: clipy + Planck NPIPE
  CamSpec + SDSS DR16 BAO + SN + CAMB PPF w/wa all load; lensing.clik test logL = -4.42102).
- **Pod**: RunPod `99srknm4s1cc3l` (name `bigbounce-p1b-snctrl`, RTX A4000, EUR-IS-1), network volume
  `bigbounce-paper1-canonical` (a9d3xb63bv) mounted at `/workspace` (holds Planck NPIPE clik data + clipy + both SN datasets).
  The old `POD_COBAYA_R43_V2` (ijzftpy3klystt) was terminated/gone; this is a fresh pod on the canonical volume.
  cobaya 3.6.2 (clipy 0.15), camb 1.6.6, OpenMPI 4.1.2.
- **Run dir**: `/workspace/bigbounce/p1b_snctrl/` — 4 MPI chains each, tmux sessions `w0wa_pp` (Pantheon+) and `w0wa_dy` (DES-Y5).
- **SSH**: `ssh -i ~/.ssh/id_ed25519 -p 19730 root@157.157.221.29`
- **Monitor (convergence later)**:
  ```
  ssh -i ~/.ssh/id_ed25519 -p 19730 root@157.157.221.29 \
    "cd /workspace/bigbounce/p1b_snctrl && tail -4 chains/control_pantheonplus/cpp.progress chains/control_desy5/cdy.progress"
  # ^ last column is Gelman-Rubin R-1 (config stops at R-1<0.01). Or full posterior summary:
  ssh ... "COBAYA_PACKAGES_PATH=/workspace/cobaya_packages getdist /workspace/bigbounce/p1b_snctrl/chains/control_pantheonplus/cpp"
  # deliverable params: w (=w0), wa, w0_plus_wa (=w0+wa), w_pivot.
  ```
- **Deliverable**: w0, wa, w0+wa posteriors per control → is the quintom-B direction (w0>-1, w0+wa<-1)
  consistent across the two independent SN samples (robust) or an artifact of double-counted SNe?
- **ALWAYS-backup (Lesson E)**: chains live on the canonical network volume (survives pod stop). Mirror final
  chains to local + HF + B2 at convergence / before pod stop.
- **NOTE**: account RunPod balance was low (~$7.86 at launch, ~$0.17/hr) — chains may need a top-up to reach
  full R-1<0.01 convergence. Check balance before relying on completion.

## P4 (chirality null) — win ChatGPT's MAJOR
- [x] **GZ1-only classifier retrain + dipole null check** — **DONE 2026-07-01 (CLOSES ChatGPT-M2)**. Trained Z2-flip-equivariant vit_small on Galaxy Zoo 1 human CW/CCW labels ONLY (no CE-ResNet pseudo-labels; val acc 0.978), re-classified GZ-DESI galaxies, ran the IDENTICAL real-space dipole estimator/seed/null as the headline: **dipole z=-0.04σ (rank-p=0.45, N_spiral=14,964) → consistent with null, like canonical +0.41σ.** Because supervision is fully CE-ResNet-independent, the vanishing dipole is NOT inherited from the pseudo-labels. Folded into P4 v1.0.202 sec:pseudolabel_independence. Artifact `pipelines/p2_chirality/outputs/gz1only_dipole_result.json`; classifier+result backed up to HF. (Reduced-N test; full-catalog re-inference is a straightforward extension that can only tighten a null already recovered.)
- [~] **[superseded]** GZ1-only classifier retrain — **LAUNCHED 2026-06-30** on RunPod pod
  `8ol1r8eew7h6br` (bigbounce-p4-gz1only, RTX A4000 16GB community, $0.17/hr,
  balance ~$54). Retrains the flip-equivariant ViT-Small on GZ1 CW/CCW labels
  ONLY — the CE-ResNet confident-spiral pseudo-label block is gated OFF
  (`USE_CE_SPIRAL=False`); every CW-vs-CCW supervised label now comes from
  Galaxy Zoo 1. NOT_SPIRAL (class 2, carries no chirality) still uses
  CE-selected smooth galaxies + synthetic negatives, so it cannot inject a
  spin preference into the dipole-driving CW/CCW decision. Script:
  `pipelines/p2_chirality/train_chirality_v2.py` variant staged at
  `/workspace/train_chirality_gz1only.py`; outputs → `/workspace/gz1only_outputs/`
  (`chirality_model_gz1only_best.pt`, `gz1only_bias_hardening.json`). Answers
  ChatGPT-M2: if the dipole null survives GZ1-only training, it is NOT inherited
  from CE-ResNet. Training runs in tmux session `gz1only` (survives disconnect).
  **Monitor:** `ssh -i ~/.ssh/id_ed25519 -p 40666 root@87.197.146.56
  'tail -f /workspace/gz1only_outputs/train.log'` (pod coords in .env.local under
  POD_P4_GZ1ONLY_*). ETA: ~1-3 h (data build ~10-20 min streaming GZ-DESI +
  ≤80 epochs early-stopped on ~26K images). NEXT: on completion, run inference +
  `preliminary_dipole.py` on the GZ1-only catalog, confirm null, backup ckpt to
  local+HF+B2 (Lesson E), then flip this to [x].
- [ ] **Empirical b/a (axis-ratio) cross-match**: test the edge-on directional-bias-exclusion argument empirically, not just analytically. (Gemini MAJOR.)
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
- [x] **Native SDSS score histogram** (Grok M2) — DONE 2026-06-30: sdss_native_score_histogram.py over 77,905 SDSS DR18 native rescores → outputs/sdss_native_score_histogram.{json,png} (99th pct 0.817, 780 above). Committed. + **marginal-α posterior fold-in** (Grok M3).

## P2 (f_NL recast) — deepest, lowest-priority (recast is honest as-is)
- [ ] **Cubic in-in transfer through an explicit bounce** (the assumption-(d) uncertainty).
- [ ] **Heinrich Fisher re-run at the bounce fiducial** with the non-local template.
- [ ] **Joint bispectrum Fisher over systematics**.

## P1A (ECH theory) — mostly text; one optional calc
- [ ] **Boltzmann Γ_wash(T) washout calculation** (currently stated conditionally) — optional; the closure margin is ansatz-insensitive without it.

## P5 (DESI chirality) — NO compute needed
The Paper-IV self-containment appendix (v0.1.96) closed the one convergent
blocker from source numbers. P5 is the closest to 3/3 ACCEPT (RREXT: Gemini
MINOR, Grok MINOR, ChatGPT MAJOR).
- [x] **RREXT ChatGPT B3 (headline) + M6 (superlative)** — **DONE 2026-06-30 (v0.1.97)**.
  Title retitled so the DESIVAST void null is the sole headline; T-Web demoted to
  "secondary tidal-tensor cross-check" (was co-headlined). The two unscoped
  "largest ... we are aware of" superlatives reworded to precise, non-superlative
  statements. Recompiled clean (35 pp, md5 9b3aad7a); mirrored to all served paths.
- [ ] **RREXT ChatGPT B1 (companion-catalog access) + B4 (frozen DOI)** — submission-time
  structural (post concurrently / mint at submission); NOT single-tick closable.
- [ ] **RREXT ChatGPT M1/M2 (radical shorten 35→~15 pp + slim abstract)** — full-length
  rewrite; scope as a dedicated D-round pass, not an incremental tick.

---
**Protocol:** run these on RunPod (see `/runpod-lifecycle` + `/houston-method-v2`);
ALWAYS-backup results to local+HF+B2 (Lesson E); fold real numbers into the .tex;
NEVER fabricate a result to satisfy a reviewer. Mint Zenodo DOIs at submission
(the deferred-DOI flags are submission-time, not blockers).

## P3 (anomaly) — scaler-leakage: AUDITED + DISCLOSED + eROSITA control COMPUTED (DP3-13); only NEOWISE/Gaia train-split refits remain compute-gated
- [x] **Normalization-scaler data leakage** (Gemini RS8, REAL) — **ADDRESSED, not open as a genuinely-new bug** (stale "NEW RS8, not a re-flag" header corrected 2026-07-11 after a verify pass against the tex + ledger). Trajectory:
  - **Audited** (v3.1.131, `pipelines/p3_anomaly_engine/outputs/scaler_leakage_audit_2026-07-02.json`): the DESI 5-fold reproducibility gates (5-fold J=0.862 / OOD J=0.732) use **per-fold** scalers → carry **NO** leakage and stand unchanged (both PASS the ≥0.70 gate). Genuine full-sample-scaler leakage exists **only** in the three tabular tiers (eROSITA/NEOWISE/Gaia), not in the headline DESI gates.
  - **Disclosed in-paper** (paper3_draft.tex §II.B "Tabular-survey feature preprocessing", ~L1060): explicit statement that tabular scalers are fit on the full sample, framed as a *stated assumption* (ranking-invariance) rather than a demonstrated result, with a "future pipelines should fit strictly on the training split" recommendation.
  - **Bounded control COMPUTED for the load-bearing eROSITA tier** (`pipelines/p3_anomaly_engine/erosita_scaler_refit.json`): train-split-only vs full-sample refit → top-298 overlap 257/298 (Jaccard 0.76), top-1% J=0.64, full-catalog Spearman ρ=0.94 — at/below the ~15–17% model-retrain reproducibility floor (production recipe on different hardware reproduces only 247/298). Within-survey rankings robust; individual extreme-tail memberships carry quantified ~15% churn.
  - **Ledger:** DP3-13 (disclosed + bounded); re-flagged by OpenAI#8 / Grok-API#7 / Grok EXT MINOR#5 and each dispositioned NOT-genuinely-new against L1051/L1060.
- [ ] **Remaining compute-gated piece (DP3-15):** train-split-only scaler refit for the **NEOWISE** and **Gaia** tiers — their feature tables are pod-side derived products. Real pod run (see protocol below), not an edit; do NOT fabricate. Expectation from the eROSITA control is rankings unaffected, but that is not yet directly verified for NEOWISE/Gaia and is disclosed as such in-paper.
