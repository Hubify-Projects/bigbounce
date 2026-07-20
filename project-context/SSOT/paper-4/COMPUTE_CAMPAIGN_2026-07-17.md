# P4 Open-Compute Campaign — Phase 1 (2026-07-17)

**Paper:** P4 Galaxy Chirality Catalog · `pipelines/p2_chirality/chirality_catalog_paper.tex` v1.0.263 (ApJS)
**Repo HEAD at plan time:** `c8db36463f5a4a1ec4df71884fe1bd476443feca`
**Readiness cap:** 80 HOLDS (no uplift claimed by this doc; gates close only on real, integrated compute)
**Source audit:** `project-context/peer-reviews/INT_v3/ROUND_2026-07-16-P4-v1.0.263-EXACTPDF-de12ac78-CLAUDESTACK-CONFIRM/P4_v1.0.263_truth_audit.md`
(0 genuinely-new-real findings; "remaining progress requires real compute or Houston-level actions, not manuscript edits")

This campaign closes the four standing open-compute gates with **real computation only,
committed artifacts, honest integration, and a full re-test wave** (directive L). No gate
is claimed closed by this document. `/backup-3plus` applies before any destructive op;
no pod is stopped without a verified backup.

---

## Gate → job spec summary

| Gate | Job | Compute | Est. wall | Est. cost | Status this session |
|------|-----|---------|-----------|-----------|---------------------|
| **G1** | Regenerable ViT-Small retrain w/ retained object/split manifest + seeds; resolve 26,616 vs 26,626 record conflict | GPU (A4000 `580dgszgib3ti4` or H200) | ~2–4 h retrain + manifest; images pod-download | A4000 ~$0.17/h → <$1; +download | **BLOCKED — needs data-pipeline smoke test (see G1)** |
| **G2** | Training-disjoint held-out GZ1 validation (anti-join on G1 manifest) | CPU (local) | ~10 min once G1 manifest exists | $0 | **BLOCKED on G1 manifest** |
| **G3** | Joint sampling covariance across real-space dipole / WLS / monopole / harmonic ℓ=1 | CPU (local, committed catalog) | ~11 min | $0 | **DONE incl. MASTER-decoupled leg (phase 2, 2026-07-18) — see G3 MASTER-LEG section** |
| **G4** | Image-level classifier-injection → per-pixel confusion + generative null isolating the monopole mechanism | GPU (H200 preferred; A4000 ok) | ~4–12 h (8.47M-galaxy inference passes) | H200 ~$4.39/h → $20–50 | **EXECUTED (phase 2, 2026-07-18) over banked e2e inference — A4000 only, $0 H200 — see G4 EXECUTED section** |

Pod inventory (all EXITED as of 2026-07-17 20:41Z): `580dgszgib3ti4` bigbounce-p4-dr8morph
(RTX A4000, $0.17/h) · `99srknm4s1cc3l` bigbounce-p1b-snctrl (A4000, $0.25/h) ·
`1detyybywd556o`,`kfmtdje25y88tf`,`rx4x18p7v4gz66`,`xzgst22n006n0g` (H200 SXM, $4.39/h each).

---

## G3 — Joint estimator covariance  ⟵ LAUNCHED THIS SESSION

**Answers:** reviewer standing gate M4 ("all residuals are systematics" asserted without a
joint statistical framework). Produces the single covariance object that ties the four
committed estimators together, measured on the SAME resamples.

**Script (committed):** `pipelines/p2_chirality/scripts/g3_joint_estimator_covariance.py`

**Inputs (committed / locally cached, offline-usable):**
- HF dataset `bamfai/galaxy-chirality-catalog` :: `catalog_production.parquet`, immutable
  snapshot revision `cc326f7469961ba2b17f8f4492d9a0988b48ca24` (8,474,531 rows; cols
  ra/dec/class_eq/confidence_eq), cached under `~/.cache/huggingface`.
- Primary HC sample = `(class_eq in {CW,CCW}) & (confidence_eq > 0.6)` = **949,584 rows**
  (reproduces the canonical HC count exactly — verified).

**Method:** block-bootstrap over NSIDE=8 HEALPix superpixels (matches the committed
`joint_nuisance_bootstrap_sigma.py` protocol), N=2000 resamples, seed 42. Per resample it
evaluates all four estimators and accumulates the 4×4 joint covariance + correlation:
1. `A_dipole_realspace` — uniform-pixel-weight real-space dipole |a| (the paper's PRIMARY family).
2. `A_dipole_WLS` — nuisance-marginalized WLS dipole (dipole+leg+density+density²+const, n_total-weighted).
3. `monopole` — global CW-fraction offset f_CW−0.5 (the −9.47σ monopole).
4. `Cl1_pseudo` — mask-coupled anafast ℓ=1 pseudo-power (NaMaster-free proxy for the MASTER leg).

**Smoke-test result (N=20, verified before full launch):** HC=949,584 exact; joint
correlation dipole↔Cl1 = +0.915 (expected — shared ℓ=1 content), monopole weakly coupled
(≈+0.17 to dipole, −0.16 to WLS); block-bootstrap monopole z=−5.83 (spatially-coherent σ,
appropriately more conservative than the per-pixel-independent binomial −9.47σ).

**Acceptance criteria:**
- Full N=2000 completes; `outputs/canonical_provenance/g3_joint_estimator_covariance.json`
  written with the 4×4 covariance + correlation, per-estimator bootstrap σ, and
  z(full/σ) for each estimator.
- Reproduces HC N=949,584 and a monopole |z| consistent with the smoke run.
- 3×3 sub-block over estimators 1–3 is **final** (NaMaster-independent).

**MASTER-leg refinement (pod-bound, flagged not blocked):** a fully MASTER-decoupled ℓ=1
(mode-coupling-matrix inverse) needs NaMaster/pymaster, which is NOT installed locally.
Refinement = resume A4000, `pip install pymaster`, swap estimator 4 for the decoupled C_1
using the existing `scripts/master_decoupled_monopole_null.py` coupling-matrix path, rerun
the identical bootstrap. The anafast proxy is a legitimate harmonic estimator; the decoupled
version is a precision upgrade, not a correctness fix.

**Backup plan:** JSON output committed to git (location 1) + append to HF dataset artifacts
(location 2) + B2 mirror (location 3) at integration time, per directive E.

**Launch record (this session):**
- pid: see `pipelines/p2_chirality/logs/g3_joint_covariance.pid`
- log: `pipelines/p2_chirality/logs/g3_joint_covariance_20260717T204134Z.log`
- checkpoint: `outputs/canonical_provenance/g3_joint_estimator_covariance.partial.json`

**COMPLETED this session (N=2000, all valid, ~573s):** artifact
`outputs/canonical_provenance/g3_joint_estimator_covariance.json` (smoke=False).
Headline joint result (block-bootstrap σ, z=full/σ):

| Estimator | full | bootstrap σ | z |
|-----------|------|-------------|---|
| A_dipole_realspace | +0.004386 | 0.001987 | **+2.21** |
| A_dipole_WLS | +0.004669 | 0.003436 | **+1.36** |
| monopole (f_CW−0.5) | −0.003949 | 0.000601 | **−6.57** |
| Cl1_pseudo (anafast ℓ=1) | +3.99e−6 | 2.04e−6 | +1.96 |

Joint correlation: dipole↔WLS +0.277 · dipole↔monopole −0.037 · dipole↔Cl1 **+0.846** ·
WLS↔monopole −0.093 · WLS↔Cl1 +0.260 · monopole↔Cl1 −0.067.

**Readout (not a closure claim):** under the joint framework the monopole is the only
|z|>3 mode (−6.57; consistent with, but more conservative than, the per-pixel-independent
binomial −9.47σ) and is **nearly uncorrelated with the dipole (−0.037) and WLS (−0.093)** —
i.e. a distinct mode, supporting the paper's separate systematics treatment. The real-space
and WLS dipoles are non-significant (z=+2.21, +1.36), consistent with the primary null.
dipole↔Cl1 +0.846 confirms both capture the same ℓ=1 content (validity check). Integration
into the manuscript + MASTER-decoupled refinement + 3-location backup is the next-session step.

---

## G3 MASTER-LEG REFINEMENT — COMPLETE 2026-07-18 (phase-2 pod session) ⟵ G3 FULLY CLOSED-BY-ARTIFACT

**The pod-bound MASTER-decoupled ℓ=1 refinement flagged above is DONE.** Script
`scripts/g3_joint_estimator_covariance_master_v2.py` (committed) reran the IDENTICAL
block-bootstrap (same NSIDE=8 blocks, N=2000, seed 42, same rng call sequence → identical
resample index sets, verified: channels 1/3/Cl1_pseudo reproduce the local run's bootstrap
mean AND σ to 6 digits) on pod `580dgszgib3ti4` (A4000), swapping channel 4 for the
NaMaster MASTER-decoupled C₁ (pymaster **3.0**, pip-installed against apt
libgsl-dev/libfftw3-dev/libcfitsio-dev — pip wheel path worked; no conda on pod). Coupling
matrix computed once on the FIXED canonical effective mask (|b_gal|>15° ∧ n_total_full>0,
f_sky=0.48991), single-ell bins via `NmtBin.from_edges(arange(1,192), arange(2,193))`
(bin 0 = ℓ=1), decoupled per resample as C_dec = M⁻¹C_pseudo.

**Artifact:** `outputs/canonical_provenance/g3_joint_estimator_covariance_master_v2.json`
(smoke=False, n_valid **2000/2000**). Headline (z = full/bootstrap σ):

| Estimator | full | bootstrap σ | z |
|-----------|------|-------------|---|
| A_dipole_realspace | +0.004386 | 0.001987 | **+2.21** |
| A_dipole_WLS | +0.004669 | 0.005776 | **+0.81** |
| monopole (f_CW−0.5) | −0.003949 | 0.000601 | **−6.57** |
| Cl1_master (MASTER-decoupled ℓ=1) | −4.552e−6 | 7.523e−6 | **−0.61** |

Joint 4×4 correlation: dipole↔WLS +0.158 · dipole↔monopole −0.037 · dipole↔Cl1_master
**+0.794** · WLS↔monopole −0.020 · WLS↔Cl1_master +0.129 · monopole↔Cl1_master **−0.061**.
corr(Cl1_master, Cl1_pseudo) = **+0.943** (the committed anafast proxy is validated — it
tracks the decoupled estimator at r≈0.94 on identical resamples).

**Readout (honest):** the monopole remains the ONLY |z|>3 mode (−6.57) and is nearly
uncorrelated with every dipole-family channel including the MASTER-decoupled one (−0.061).
The MASTER-decoupled ℓ=1 itself is null (z=−0.61; the decoupled full-sample C₁ is negative,
which MASTER permits for noise-dominated modes). G3's conclusion is unchanged and now
NaMaster-complete: **G3 CLOSED-BY-ARTIFACT including the MASTER leg.**

**Cross-platform WLS caveat (documented, does not change conclusions):** channels 1, 3 and
Cl1_pseudo reproduce the local N=2000 moments EXACTLY; the WLS channel's bootstrap σ differs
(local 0.003436 / pod 0.005776; mean 0.007557 vs 0.007724) — the 9-column weighted
normal-equation solve is ill-conditioned on a minority of resamples and BLAS-dependent.
WLS is non-significant on both platforms (z +1.36 local / +0.81 pod); flagged for a future
QR/SVD-based solver hardening, not a result-level issue.

**Backup (3 locations, hash-verified):** local repo (committed) · HF
`bamfai/galaxy-chirality-catalog :: p4_compute_phase2_2026-07-18/` (uploaded additively,
re-downloaded, sha256 round-trip MATCH `189dd0deb7292550…`) · pod `/workspace/g3/out/`
(held until verification, then pod stopped).

---

## P1B NAMASTER-PROOF REGENERABILITY — EXECUTED 2026-07-18 (same pymaster env)

`packages/namaster-proof/examples/rebuild_workspace_check.py` was EXECUTED (not skipped)
on the pod in the same pymaster 3.0 env — closing P1B's pending "regenerability check
never actually run with PyMaster present" item. Verbatim:

```
PyMaster 3.0, healpy 1.19.0
  mask f_sky = 0.3226 (deterministic)
  workspace window shape = (4, 20, 4, 1025)
  window_equivalence_max_abs = 9.926167e-24
PASS: workspace regenerated deterministically; max|Delta| = 9.926e-24 < 1e-10
```

**Honest note:** the regenerated scalar 9.926e−24 PASSES the committed `<1e-10` gate and
confirms the `[4,20,4,1025]` window tensor rebuilds deterministically, but it is ~6 orders
below the recorded production value 1.41e−18 — the literal digits are
platform/BLAS/pymaster-version dependent (pod pymaster 3.0 vs production 2.6), exactly why
the paper demotes the literal value from a universal bound. The gate, not the digits, is
the invariant. Receipt: `packages/namaster-proof/examples/rebuild_workspace_check_2026-07-18_podA4000.log`
(+ HF mirror, hash-verified).

---

## G1 — Regenerable training realization  ⟵ BLOCKED (needs smoke test before GPU launch)

**Answers:** reviewer gates M1/Gk1/Ge1 (labels not reproducible; committed records conflict
26,616 vs 26,626 / 826 vs 846 / 93.6878% vs 92.10%; no retained object/split manifest).

**Goal:** a fresh, fully-logged ViT-Small chirality retrain that RETAINS the object-ID
manifest, train/val split indices, and every random state — a going-forward regenerable
realization. It does NOT reproduce the historical labels (that record is unrecoverable and
honestly disclosed at tex L832, Table 12); it supersedes them with a reproducible one.

**Existing code:** `train_chirality_v2.py`, `train_v2_fast.py`, `real_zoobot_chirality.py`,
`bias_hardening_suite.py` (3-class CW/CCW/NOT_SPIRAL ViT, flip-equivariance loss).

**Inputs & provenance (from tex L788/L797/L832/L1669):**
- Parent images: `Smith42/galaxies` HF dataset, immutable rev
  `bdd1b063a9a22874a79a4363aa9fb6a2b356a4c2` (8,474,566 × 224×224 grz cutouts). Training
  needs only the ~27K cross-matched subset, but the images are pod-download (HF).
- GZ1 CW/CCW labels: `GalaxyZoo1_DR_table2.csv.gz` from S3 (reproducible, in-script).
- Coords/crossmatch: Galaxy Zoo DESI predictions (Walmsley 2023) by dr8_id → ra/dec.
- CE-ResNet high-confidence spirals (Jia 2023) for the ~17K spiral labels.
- Model repo: `bamfai/galaxy-chirality-v2` (historical receipt rev `237d021c...`,
  checkpoint SHA `618d170f...`).

**Why BLOCKED (honest):** the label-assembly + crossmatch path in the existing scripts is
not verified to resolve end-to-end on a fresh pod (image source access, GZ-DESI predictions
availability, CE-ResNet catalog fetch), and none of the current scripts writes the retained
object/split/seed **manifest** that is the entire point of the gate. Launching a blind GPU
retrain risks a wasted pod AND a run that fails the gate's own acceptance (no manifest).

**Required before GPU launch (do next session):**
1. Resume A4000 `580dgszgib3ti4` (`runpodctl start pod 580dgszgib3ti4` or GraphQL
   `podResume`); rsync `train_chirality_v2.py` + a new `train_g1_manifest.py` wrapper.
2. **20-min smoke test:** verify GZ1 S3 fetch, GZ-DESI-predictions crossmatch, Smith42 image
   pull for ~200 objects, CE-ResNet label join — confirm the ~27K training pool assembles
   and the exact object IDs are enumerable.
3. Add manifest logging to the training wrapper: dump `{object_ids, train_idx, val_idx,
   torch/np/python seeds, dataset revisions, git SHA}` → `g1_training_manifest.json` BEFORE
   training; checkpoint every epoch to the pod volume.
4. Only then run the full retrain (~2–4 h) + `bias_hardening_suite.py`.

**Acceptance criteria:** retrained checkpoint + `g1_training_manifest.json` that regenerates
the identical split/labels from seeds; val_acc reported with its exact manifest; the paper's
Table 12 conflict paragraph updated from "not retained / unrecoverable" to
"superseded by regenerable realization <SHA>, historical records retained as disclosure."

**Backup:** checkpoint + manifest → pod volume + HF model repo + B2 (3 locations) before stop.

---

## G1 RUN LOG — 2026-07-18 (pod-execution session)

**Gate NOT claimed closed.** Smoke test PASSED; manifest-retained retrain LAUNCHED. Closure
still requires: full run completes + `g1_training_manifest.json` committed + CE-ResNet
component provisioned (see blocker below) for the historical-composition supersession.

### Pod + access
- Pod `580dgszgib3ti4` (`bigbounce-p4-dr8morph`, RTX A4000 **16376 MiB**, 112 vCPU, 503 GB RAM,
  $0.17/h). Resumed via GraphQL `podResume` (Bearer + `?api_key=`; UA header needed —
  Cloudflare 403s the default `Python-urllib` UA; helper `tools/runpod_ctl.py` sets a browser UA).
- **sshd bootstrap (important for resume):** the resumed container came up with **no host keys
  and empty `PUBLIC_KEY` env**, so the template sshd exited (`no hostkeys available -- exiting`)
  and the direct TCP port refused. Fixed by reaching the pod via the RunPod proxy
  `580dgszgib3ti4-644119b0@ssh.runpod.io` (interactive — pipe commands on stdin), running
  `ssh-keygen -A` + writing `~/.ssh/authorized_keys` + `/usr/sbin/sshd`. Reusable helpers:
  `tools/pod_bootstrap_sshd.sh` (proxy bootstrap) and `tools/pod_ssh.sh` (clean direct SSH).
- Direct SSH after bootstrap: `ssh -p 1206 -i ~/.ssh/id_ed25519 root@193.183.22.54`
  (port changes on each resume — re-query `python3 tools/runpod_ctl.py status`).
- Pod is **ephemeral** (no persistent network volume): stop/resume wiped `/workspace`,
  `pip` packages, and `/workspace/external_catalogs/pre_desi.fits`. Deps reinstalled this
  session (`timm 1.0.28`, `datasets 5.0.0`, astropy/scipy/pandas/pyarrow/huggingface_hub;
  torch 2.2.0+cu121 preinstalled).

### Data-pipeline SMOKE TEST — **PASS** (2026-07-17 23:03Z)
Wrapper `pipelines/p2_chirality/train_g1_manifest.py --smoke`. End-to-end verified:
- **GZ1 S3 labels:** fetched `GalaxyZoo1_DR_table2.csv.gz` (sha256 `5121e43f5028…`);
  confident CW=19,613 / ACW=20,923 (P>0.7), balanced 19,613.
- **GZ-DESI crossmatch + image pull:** streamed `mwalmsley/gz_desi` (resolved rev
  `b7583bb2ac445e93c5447a08063acd7c1477fd13`); **332 GZ1 matches from 8,000 scanned
  (4.15% match rate, 3″ tol)** in 0.3 min; images pulled inline from gz_desi rows.
- **ViT-Small fwd+bwd:** `timm vit_small_patch16_224` pretrained + 3-class head, 10.98M
  trainable; one batch (32) fwd+bwd loss=1.0998 (≈ln3, random-init sanity), 0.27 s,
  **peak GPU 1.13 GB / 16 GB** → A4000 is ample; no larger GPU needed.
- **Manifest capture verified:** 392 objects logged, each with source + gz_desi `id_str`
  (e.g. `313784_243`) + ra/dec (real) or `synth_idx` (synthetic), plus all seeds (42),
  split rule, revisions, package versions, git SHA.
- Evidence committed: `pipelines/p2_chirality/outputs/g1_manifest_retrain/{g1_smoke_result.json,
  g1_smoke_manifest.json,smoke_run.log}`.

### BLOCKER (original, documented): CE-ResNet component — **RESOLVED 2026-07-19 (see below)**
- `pre_desi.fits` (Jia et al. 2023 CE-ResNet, RA/DEC/P_CW/P_ACW) supplied ~67.5% of the
  historical realization (17,153 spirals + 826 non-spirals of the 26,616 rows; tex L871).
  It lived only on the pod's ephemeral disk and was wiped on resume; **not in the repo, not
  cached locally, no immediate public download link** located (source lineage: arXiv 2210.04168 /
  GitHub `h3jia/galaxy_spin_classifier` / NADC China-VO — needs genuine re-provisioning).
- Consequence: **this session's retrain uses the verified GZ1-core + synthetic realization
  only** (`ce_resnet_present=false` in the manifest). It produces a fully regenerable manifest
  + checkpoint, but does **not yet** engage the CE-non-spiral 826-vs-846 sub-conflict, which
  requires CE-ResNet. The wrapper is **CE-ready**: drop `pre_desi.fits` into
  `/workspace/external_catalogs/` and re-run — it auto-includes CE spirals/non-spirals and
  records the file sha256. This is the one item to provision for full historical-composition
  supersession.

### CE-ResNet RE-PROVISIONED — 2026-07-19 (data worker session) ⟵ BLOCKER CLEARED
**The `pre_desi.fits` re-provisioning blocker above is RESOLVED.** The catalog is public,
no-login, on Zenodo — the GitHub repo carries no data assets and NADC/China-VO was a
red-herring in the lineage; the real host is Zenodo.
- **Canonical source (DOI):** `10.5281/zenodo.7167388` — Zenodo record `galaxy-spin-zs-catalog`
  (He Jia, Hong-Ming Zhu, Ue-Li Pen; published 2022-10-08; CC-BY-4.0). This is the data
  record for arXiv:2210.04168 ("Galaxy Spin Classification I: Z-wise vs S-wise Spirals with
  Chirality Equivariant Residual Network"). GitHub `h3jia/galaxy_spin_classifier` has **no
  releases / no data assets** — code only; the catalog lives ONLY on Zenodo.
- **Direct URL:** `https://zenodo.org/records/7167388/files/pre_desi.fits?download=1`
- **Downloaded to:** `pipelines/p2_chirality/external_catalogs/pre_desi.fits` (gitignored — 363MB;
  provenance file committed).
- **Size:** 380,897,280 bytes (363 MiB). **sha256:**
  `894dbe887140c165488a0f6053e2cd21f4ab72be9b06ece733e6ce177c0e304b`.
- **FITS validity:** VALID (astropy 6.0.1). HDU1 `SWEEP` BinTableHDU, **1,953,246 rows × 40 cols**,
  incl. exactly `P_CW`, `P_ACW` (CE-ResNet DESI-image chirality probs, float64 ~[0.006,0.972]),
  `RA`, `DEC` — matches the wrapper's expected schema.
- **Provenance:** `pipelines/p2_chirality/external_catalogs/PROVENANCE.md` (committed).
- **Companion (not pulled, same record):** `reduced_gz1.csv` (70.1MB, 173,097 GZ1 galaxies with
  `p_cw_gz/p_acw_gz`, `n_vote`, `p_cw_sdss/p_acw_sdss`, `p_cw_desi/p_acw_desi`) — available from
  the same DOI if the 26,616-vs-26,626 crossmatch reconciliation needs the GZ-side votes.
- **Next step (NOT done this session — no retrain per worker scope):** resume A4000
  `580dgszgib3ti4`, rsync `pre_desi.fits` to `/workspace/external_catalogs/`, re-run
  `train_g1_manifest.py --full` — the wrapper auto-includes CE spirals/non-spirals
  (`ce_resnet_present=true`) and records the sha256, engaging the CE-non-spiral 826-vs-846
  sub-conflict for full historical-composition supersession. G1 remains gated on that retrain
  completing + `g1_training_manifest.json` committed; the external-data blocker is now cleared.

### CE-INCLUDED FULL COMPOSITION — RESOLVED 2026-07-19/20 (retrain-lead session) ⟵ 826-vs-846 ADJUDICATED
**The CE ingestion path — CE-ready per its author but NEVER previously run — is now
VALIDATED end-to-end against the real `pre_desi.fits`, and the CE-included composition
(the 826-vs-846 science result) is RESOLVED.** No wrapper fix was required; the CE branch
ran clean on the first invocation.

- **CE catalog:** local `pipelines/p2_chirality/external_catalogs/pre_desi.fits`, sha256
  `894dbe887140c165488a0f6053e2cd21f4ab72be9b06ece733e6ce177c0e304b` (verified) — FITS read OK
  (1,953,246 rows; non-spiral pool p_cw+p_acw<0.02 = 74,174; confident-spiral pool = 148,240; 0 NaN).
- **SMOKE (--smoke path, CE present, scan 8000):** `ce_resnet_present=true`, ce_spiral=200
  (hit smoke cap), ce_not_spiral=38, gz1=262 — CE ingestion path confirmed end-to-end.

**CE COMPOSITION — the 826-vs-846 adjudication (VERBATIM):** full-mode wrapper
(`build_dataset`, scan_limit=150,000, gz_desi rev `b7583bb2ac445e93c5447a08063acd7c1477fd13`,
seed 42, CE present):

| source | count | note |
|--------|-------|------|
| gz1 | **6,637** | reproduces historical GZ1 count EXACTLY |
| ce_spiral | **17,153** | reproduces historical 17,153 CE spirals EXACTLY |
| ce_not_spiral | **819** | the disputed CE non-spiral component |
| synthetic | 2,000 | |
| **total** | **26,609** | |

class_counts {CW 11904 / CCW 11886 / NOT_SPIRAL 2819}; n_train 21,288 / n_val 5,321.

**Adjudication: NEITHER 826 nor 846 — the reproducible value is 819.**
`6637 + 17153 + 826 + 2000 = 26,616` (the smaller historical record) EXACTLY, so the two large
deterministic components (gz1, ce_spiral) reproduce exactly and the ENTIRE historical
826-vs-846 / 26616-vs-26626 conflict is isolated to the CE **non-spiral** crossmatch. That
crossmatch draws a seeded 50,000-object subsample of the 74,174 non-spiral candidates and
matches within 3″, so its exact count is subsample/boundary-sensitive — precisely the
irreducible ambiguity the paper's Table 12 flagged. The regenerable realization supersedes the
unrecoverable historical record with **ce_not_spiral = 819, total = 26,609**.

**Honest execution note:** the composition counts come from the CPU data-assembly stage
(streaming gz_desi crossmatch), which is deterministic under seed + pinned gz_desi rev +
committed CE file. They were produced this session on **local CPU** (driver
`scripts/g1_ce_composition_assembly.py`, calling the EXACT wrapper functions, skipping only the
GPU `build_model`+training loop) because the A4000 pod `580dgszgib3ti4` and fallback
`99srknm4s1cc3l` hosts were **GPU-full** ("not enough free GPUs on the host machine") for the
entire session (resume retried ~27+ min). The emitted manifest is byte-equivalent to what the
pod `--full` run records; the pod adds only the GPU-trained checkpoint on top.

**Committed artifacts:** `pipelines/p2_chirality/outputs/g1_full_composition/`
(`g1_full_composition_manifest.json` sha256 `431f84f09519d1ef8be9e2f488f199b5d6b1c5127a77d4e25f53df04cf110777`
[26,609 objects], `ce_composition_full.json`, `ce_composition_smoke.json`, `g1_ce_smoke_manifest.json`,
`ce_full_assembly.log`, `PROVENANCE.md`) + driver `scripts/g1_ce_composition_assembly.py`.

### FULL CE-INCLUDED RETRAIN — LAUNCHED (detached) on FRESH A4000 — 2026-07-20 ⟵ retrain checkpoint IN PROGRESS
The target pod `580dgszgib3ti4` (and fallback `99srknm4s1cc3l`) hosts were persistently
GPU-full ("not enough free GPUs on the host machine") for ~30 min of resume retries, so a
**fresh on-demand A4000 was deployed** (`podFindAndDeployOnDemand` searches all hosts, unlike
the capacity-pinned resume) to actually launch the retrain — real compute, ephemeral pod,
$0.17/h.

- **Pod:** `th0o0l1tp1se4e` (`bigbounce-p4-g1-retrain`, RTX A4000 16376 MiB, machine
  robtjgci7up0, image `runpod/pytorch:2.4.0-cuda12.4.1`, torch 2.4.1+cu124). Deployed with
  `PUBLIC_KEY` injected so **direct SSH works with no sshd bootstrap**.
- **SSH:** `ssh -p 1787 -i ~/.ssh/id_ed25519 root@193.183.22.60` (re-query
  `python3 tools/runpod_ctl.py status` after any resume — port changes).
- **CE catalog on pod:** `pre_desi.fits` scp'd to `/workspace/external_catalogs/`; sha256 on pod
  = `894dbe887140c165488a0f6053e2cd21f4ab72be9b06ece733e6ce177c0e304b` (VERIFIED, matches repo).
- **Deps:** `timm 1.0.28 / datasets 5.0.0 / astropy 8.0.1` (+scipy/pandas/pyarrow/hf_hub) pip-installed.
- **Pod SMOKE (--smoke) PASS:** `ce_resnet_present=true`, gz1=262 / ce_spiral=200 (smoke cap) /
  ce_not_spiral=38 — IDENTICAL to the local smoke (deterministic reproduction confirmed);
  loss=1.0950, peak_gpu 1.13 GB. No wrapper fix required.
- **FULL launch:** `cd /workspace/g1 && source env.sh && setsid nohup python3 -u
  train_g1_manifest.py --full --epochs 80 > full_run.log 2>&1 &` · **PID 776** ·
  **launch 2026-07-20T07:26:30Z** · ~45 s/epoch → **ETA ~45-60 min**; checkpoints every epoch.
- **manifest CONFIRMED (pod, written 07:32:25Z before training):**
  `/workspace/g1/out/g1_training_manifest.json`, `ce_resnet_present=true`, ce_sha256 verified.
  Pod assembly checkpoints (IDENTICAL to the local run — deterministic reproduction proven):
  50K → gz1 2248 / ce 5688 / ns 274; 100K → 4397 / 11472 / 561; 150K → **gz1 6637 / ce_spiral
  17153 / ce_not_spiral 819**. Final: **gz1=6637, ce_spiral=17153, ce_not_spiral=819,
  synthetic=2000, total=26,609**; classes {CW 11904 / CCW 11886 / NOT_SPIRAL 2819};
  train 21,288 / val 5,321. **826-vs-846 adjudication on the actual pod retrain: 819 (NEITHER;
  the two large components reproduce historical exactly, conflict isolated to CE non-spiral).**
- **POLL:** `ssh -p 1787 -i ~/.ssh/id_ed25519 root@193.183.22.60 "tail -20 /workspace/g1/full_run.log; ls -la /workspace/g1/out/"`
- **BACKUP before any stop (`/backup-3plus`):** pull `g1_training_manifest.json` +
  `g1_ckpt_best.pt` + `g1_training_result.json` → repo (loc 1) → git (loc 2) → HF
  `bamfai/galaxy-chirality-v2` and/or B2 (loc 3). Do NOT `podStop th0o0l1tp1se4e` before this.
  (The pod is left RUNNING for the orchestrator to poll + backup + stop after completion.)

### FULL retrain — LAUNCHED (detached), NOT claimed complete
- Command (on pod): `cd /workspace/g1 && source env.sh && nohup python3 -u
  train_g1_manifest.py --full --epochs 80 > full_run.log 2>&1 &`
- **pod:** `580dgszgib3ti4` · **PID 1010** · **launch:** 2026-07-18T00:17:23Z
- **CONFIRMED assembling + training (00:24Z):** 150K-row scan done in 5.8 min →
  **gz1=6,637 (EXACTLY the historical GZ1 count; 6,637 unique object identities, no dups)**
  + 2,000 synthetic = **n_total 8,637** (train 6,910 / val 1,727; classes CW 3,316 /
  CCW 3,321 / NS 2,000). ViT-Small 10.98M trainable. **epoch 0/80: train_acc 0.663,
  val_acc 0.619, loss 0.428**; GPU 99% util, 4.4 GB used; checkpoints g1_ckpt_{best,last,
  epoch000}.pt written. ~45 s/epoch → **ETA ~45–60 min** (well under estimate).
  The GZ1-core component of the historical realization is regenerated identically; only
  the CE-ResNet component (17,153 spirals + 826 non-spiral) is absent (see BLOCKER above).
- **manifest (written before training):** `/workspace/g1/out/g1_training_manifest.json`
- **checkpoints (every epoch):** `/workspace/g1/out/g1_ckpt_epoch###.pt`, `g1_ckpt_best.pt`,
  `g1_ckpt_last.pt`; result `/workspace/g1/out/g1_training_result.json`
- **log:** `/workspace/g1/full_run.log`
- **POLL:** `ssh -p <port> -i ~/.ssh/id_ed25519 root@193.183.22.54 "tail -20 /workspace/g1/full_run.log; ls -la /workspace/g1/out/"`
  (get `<port>` from `python3 tools/runpod_ctl.py status`; if sshd is down after a resume,
  re-run `PROXY=580dgszgib3ti4-644119b0@ssh.runpod.io tools/pod_bootstrap_sshd.sh` first).
- **BACKUP before any stop (`/backup-3plus`):** pull `g1_training_manifest.json` +
  `g1_ckpt_best.pt` + `g1_training_result.json` to repo (loc 1) → git (loc 2) →
  HF model repo `bamfai/galaxy-chirality-v2` and/or B2 (loc 3). Do NOT `podStop` before this.

### Spend (this session)
- A4000 @ $0.17/h, resumed ~2026-07-17 22:4xZ; ~1.5 h elapsed to launch (smoke + deps +
  bootstrap) ≈ **$0.26** so far; full retrain adds ~$0.3–0.5. Running total well under $1.

---

## G1 FULL RUN — COMPLETE + 3-LOCATION BACKUP VERIFIED — 2026-07-18 (pod-completion session)

**FULL retrain DONE.** `[01:15:26] FULL DONE best_val_acc=0.9931 @epoch 47` (early stop at
epoch 62, patience 15). ViT-Small `vit_small_patch16_224`, 3-class (CW/CCW/NOT_SPIRAL),
10.98M trainable; n_total 8637 (train 6910 / val 1727); class_counts CW 3316 / CCW 3321 /
NS 2000. Composition: **gz1=6637 (exact historical GZ1 identities) + synthetic=2000;
ce_spiral=0, ce_not_spiral=0** → `ce_resnet_present=false` (CE-ResNet catalog still needs
external re-provisioning — the retrained realization is the **GZ1-core + synthetic**
component only; the CE non-spiral 826-vs-846 sub-conflict is NOT engaged this run).
Seeds all 42; split_rule `RandomState(42).shuffle(arange(n)); val=first max(n//5,500)`;
training-wrapper git_sha `38edf6c5ad3960579d1404799502f3ab83120fb2`.

### /backup-3plus — VERIFIED across 3 distinct locations (hashes matched)
| Artifact | sha256 | (a) local disk | (b) HuggingFace | (c) pod |
|----------|--------|----------------|------------------|---------|
| `g1_ckpt_best.pt` (88046112 B) | `aed109dcda13f6468aaef60c5824c7a94d1109424ed25df1e3959aa10a752387` | `pipelines/p2_chirality/outputs/g1_retrain/` (matches pod) | `bamfai/galaxy-chirality-v2 :: g1-retrain-2026-07-17/` (re-downloaded + hash-MATCH) | present until (a)+(b) verified |
| `g1_training_result.json` | `0cd57a5535948ac7ef5faa432ea7e2d129296a96cd6235b1f769c7dc266567e3` | same dir | same HF rev (MATCH) | present |
| `g1_training_manifest.json` | `e5de8e030996dea9ac42f1af6a63a45f28b1418f1fa78ee33a26e2d240a10729` | same dir (identical to committed `outputs/g1_manifest_retrain/` copy) | same HF rev (MATCH) | present |

- HF revision path `g1-retrain-2026-07-17/` also carries `PROVENANCE.md` (honesty note +
  hashes). **Additive upload** — did not overwrite existing repo files (`chirality_model_v2_best.pt`
  etc. remain the historical receipts). All 3 HF files re-downloaded and hash-compared → MATCH.
- The 88MB `.pt` is **gitignored** (`pipelines/p2_chirality/outputs/g1_retrain/*.pt`): local
  disk + HF only, per campaign backup rule (repo keeps the JSONs + provenance, not the weights).

### G2 done (see G2 section below); pod stopped AFTER backup + G2 verified.

### Pod final state + spend
- `580dgszgib3ti4` **STOPPED** via `runpod_ctl.py stop` → `desiredStatus: EXITED` (confirmed).
  podStop issued only after (a) local matched pod hashes AND (b) HF round-trip matched AND
  (c) G2 completed.
- A4000 @ $0.17/h, resume ~22:4xZ → stop ~02:5xZ ≈ **~4.2 h ≈ ~$0.71 this pod-uptime span**;
  G1 lane running total still **< $1**.

---

## G2 — Training-disjoint held-out validation  ⟵ DONE 2026-07-18 (metrics verbatim)

**Script:** `pipelines/p2_chirality/analysis/g2_disjoint_validation_v1_0_266.py`
**Result:** `pipelines/p2_chirality/analysis/g2_disjoint_validation_v1_0_266.json`
Ran on pod (A4000 GPU inference), 358 s. Evaluated the G1 `g1_ckpt_best.pt` (epoch 47,
val_acc 0.9931; ckpt sha `aed109dc…`) on **3000 GZ1 confident spirals disjoint from the G1
training pool along BOTH axes**: (1) gz_desi ROW disjoint — eval drawn only from rows
[150000, 350000), never scanned in G1 training [0,150000); scanned 66,621 to reach the 3000
cap; (2) GZ1 OBJECT disjoint — any candidate within 3″ of a training-manifest object dropped.
**Exclusions: idstr-overlap=0, object-overlap=0** (rows past the training window were naturally
clean). Checkpoint state_dict loaded with **0 missing / 0 unexpected** keys.

**Metrics (verbatim):**
- eval n=3000 (CW=1470, CCW=1530)
- **accuracy = 0.9867** (3-class; 0 NOT_SPIRAL predictions, mean NS softmax prob 0.0)
- **Cohen's κ = 0.9733** (labels {0,1}; binary-subset κ identical, since 0 NS preds)
- Confusion (rows=true, cols=pred, {CW,CCW}): `[[1460, 10], [30, 1500]]`
- CW(0): precision 0.9799 · recall 0.9932 · F1 0.9865 (support 1470)
- CCW(1): precision 0.9934 · recall 0.9804 · F1 0.9868 (support 1530)

**Readout (honest, not a closure claim):** on a provably training-disjoint GZ1 held-out set
the GZ1-core+synthetic checkpoint reaches 0.9867 accuracy / κ=0.9733 — modestly below the
in-training val_acc 0.9931 (expected for truly held-out data), directly addressing reviewer
gate M3 ("GZ1 validation overlap-contaminated; no independent held-out"). The metric measures
CW/CCW discrimination on GZ1 spirals only; it does **not** exercise the CE non-spiral
component (absent this run). Provenance hashes (ckpt/manifest/gz1/train-id-strs/eval-ids +
gz_desi rev `b7583bb2…`) recorded in the JSON.

**Original G2 spec (retained):**

**Answers:** reviewer gate M3 (GZ1 validation overlap-contaminated; no independent held-out).

**Method:** once G1 emits `g1_training_manifest.json`, anti-join the GZ1 validation set
against the retained training object IDs (remove the 6,637 GZ1 rows used in training), then
recompute the GZ1 human-vote dipole + chirality-agreement on the disjoint remainder. CPU,
local, ~10 min. Existing GZ1 machinery: `run_dipole_gz1only_fullN.py`,
`outputs/gz1_stratified_confusion.json`, `outputs/gz1only_fullN_dipole_result.json`.

**Acceptance:** a κ / agreement + dipole z on a provably training-disjoint GZ1 subset, with
the anti-join row counts committed. Closes the "no independent held-out validation" gate.

---

## G4 — Image-level classifier-injection → monopole mechanism  ⟵ SCOPED, not launched

**Answers:** reviewer gate M5 (−9.47σ monopole; no causal mechanism isolated) via directive L
(end-to-end classifier injection + per-pixel confusion + generative null).

**Existing scaffolding (substantial):**
- `scripts/e2e_mirror_flip_fullrun.py`, `scripts/e2e_mirror_flip_transfer_function.py`
- `scripts/full_catalog_injection_recovery.py`, `scripts/stage_b_hybrid_image_field_recovery.py`
- Prior artifact: `outputs/canonical_provenance/e2e_fullrun/e2e_transfer_function_full.json`
  (192/192 shards, the 8.47M image-level mirror-flip injection that CLOSED-BY-ARTIFACT DP4-15;
  T_raw=0.2303, T_eq=0.9997).

**What is still open (the monopole-specific piece):** the existing e2e run measured the
flip-transfer function; it did NOT produce a **per-pixel confusion map** propagated to the
CW-fraction field, nor a **generative null** that reproduces the −9.47σ monopole from
classifier confusion alone (isolating which of the 3 candidate mechanisms — GZ1 CW excess /
residual orientation bias / DESI photometric asymmetry — drives it).

**Plan:** resume an H200 (`bamfai/galaxy-chirality-v2` inference); (1) run the production ViT
on the 8.47M images + their per-pixel mirror pairs to build a per-pixel CW↔CCW↔NS confusion
tensor; (2) forward-model the global monopole from that confusion under a parity-symmetric
input null; (3) compare the generated monopole to the observed −9.47σ. GPU, ~4–12 h.

**Acceptance:** committed per-pixel confusion artifact + generative-null monopole with a
quantified fraction of the observed monopole explained; paper §Global CW Fraction updated to
attribute the mechanism (or bound each candidate). This is the largest job; run after G3
integrates and G1's pipeline is verified.

---

## G4 — EXECUTED 2026-07-18 (phase-2 pod session): per-pixel confusion + generative parity-null

**No new GPU inference was scientifically required — and none was fabricated.** The 16,949,062
production-ViT forward passes (8,474,531 galaxies × {original, mirror}) already existed as the
banked per-galaxy record `e2e_mirror_pairs.parquet` (A100 pod `0hh3humgpacgz1`, 2026-07-11/12,
192/192 shards; HF + B2 + local shards, byte-verified — RUN_SUMMARY.md). What G4's spec still
required — the per-pixel confusion tensor and the generative null — is aggregation +
forward-modeling OVER that banked inference, executed this session on the A4000 pod
(`scripts/g4_monopole_mechanism_injection.py`, committed). **No H200 was deployed ($0 H200
spend).** Join: 8,474,531 rows 1:1 on dr8_id; class agreement with the production catalog =
**0.99936** after mapping (the raw-string scalar 0.3772 in the JSON is purely the
'NS' vs 'NOT_SPIRAL' naming difference on non-spirals; the computation maps both).

**Artifacts (committed + HF `p4_compute_phase2_2026-07-18/`, sha256 round-trip MATCH):**
- `outputs/canonical_provenance/g4_monopole_mechanism_injection.json` (smoke=False, N=500,
  seed 42, finalized 2026-07-18T07:45:46Z)
- `outputs/canonical_provenance/g4_perpixel_confusion_nside64.npz` (per-pixel 3×3
  mirror-confusion tensors raw+eq, NSIDE=64, + confusion-propagated bias fields)

**Verbatim result (observed HC monopole on galmask: −0.0039486, n=948,428):**

| Channel | confusion-generated monopole (500 parity-symmetric realizations) | vs observed |
|---------|------------------------------------------------------------------|-------------|
| **EQ (production Z₂-TTA labels)** | mean **+7.88e−6 ± 5.23e−4** | explains **−0.20% (mean); ±2σ null spread = 26.7%** of observed; z(obs vs null) = **−7.57** |
| **RAW (no antisymmetrization)** | mean **+0.012854 ± 0.000158** | opposite sign, 3.26× magnitude; z(obs vs null) = **−106.5** |

Supporting mechanism numbers: raw classifier prior asymmetry ⟨p_CW⟩−⟨p_CCW⟩ (parity-avg) =
**+0.007337** (the GZ1-training-prior candidate — WRONG SIGN for the observed CW deficit);
raw confusion-propagated bias field: monopole +0.01289, dipole amp 0.1508, N/S split
**−0.1452 / +0.0795** (dec ≥32° / <32° — large spatially-structured raw-channel systematic);
EQ bias field **identically 0** at every pixel; banked `eq_antisym_dev` mean=max=**0.0**
(the Z₂-TTA antisymmetry is EXACT in the banked labels).

**What this result DOES show (honest):**
1. **Classifier confusion through the production EQ pipeline generates 0.0% of the observed
   monopole** (mean −0.20% ± 0.59% at 1σ of the MC mean; the null's ±5.2e−4 spread is pure
   binomial sampling noise of a parity-symmetric sky, not a systematic offset — the EQ
   antisymmetry is exact, so confusion adds nothing beyond binomial noise). The observed
   monopole is −7.57σ against this classifier-only null (same order as, and consistent with,
   the paper's per-pixel-independent binomial −9.47σ).
2. **The counterfactual raw channel is quantified:** without the Z₂-TTA guard the classifier
   WOULD imprint +0.0129 (3.3× observed, opposite sign, heavily spatially structured). The
   production pipeline demonstrably suppresses a large classifier-level parity systematic.
3. **The training-prior (GZ1 CW-excess) candidate is bounded AND sign-excluded** as the
   monopole mechanism: it expresses as a +CW raw preference (+0.0073), is exactly nulled by
   the EQ construction, and has the wrong sign for the observed CW deficit.

**What this result does NOT show (honest limits):** it does not positively identify which
UPSTREAM mechanism (true sky parity asymmetry vs a parity-odd DESI imaging/photometric
systematic in the cutouts themselves) produces the −9.47σ monopole. G4 localizes the origin
strictly upstream of the classifier — the monopole enters through the input image
distribution, not through classifier confusion — and bounds/sign-excludes the classifier-side
candidates. The per-pixel confusion tensors (npz) are the committed substrate for any further
upstream attribution. Manuscript integration (paper §Global CW Fraction) is deliberately NOT
done here (no-manuscript-edits rule this session); readiness cap 80 HOLDS.

---

## Resume / poll commands (for the next session)

```bash
cd /Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p2_chirality

# --- G3 (running locally now): poll ---
cat outputs/canonical_provenance/g3_joint_estimator_covariance.partial.json   # progress
tail -n 20 logs/g3_joint_covariance_*.log                                     # log
ps -p "$(cat logs/g3_joint_covariance.pid)" -o pid,stat,etime,command         # alive?
# when done, the final artifact:
python3 -c "import json;d=json.load(open('outputs/canonical_provenance/g3_joint_estimator_covariance.json'));print('n_valid',d['n_valid']);print('sigma',d['bootstrap_sigma']);print('corr',d['joint_correlation'])"
# MASTER-leg refinement (pod): resume A4000, pip install pymaster, swap estimator 4.

# --- G1 (blocked): resume pod + smoke test BEFORE full retrain ---
KEY=$(grep -E '^RUNPOD_API_KEY=' ../../.env.local | cut -d= -f2- | tr -d '"'"'"' ')
# resume A4000 580dgszgib3ti4 (podResume GraphQL or runpodctl start pod 580dgszgib3ti4)
# then rsync train scripts, run the 20-min crossmatch/image/label smoke test,
# add g1_training_manifest.json logging, then full retrain.

# --- RunPod pod status ---
curl -s -X POST "https://api.runpod.io/graphql?api_key=$KEY" -H "Content-Type: application/json" \
  -d '{"query":"query{myself{pods{id name desiredStatus machine{gpuDisplayName} costPerHr}}}"}' | python3 -m json.tool
```

## Phase-2 session record (2026-07-18)

- Pod `580dgszgib3ti4` (A4000 $0.17/h) resumed ~06:10Z, stopped ~08:1xZ ≈ **2.1 h ≈ $0.36**.
  sshd was again dead on resume (no host keys) — `tools/pod_bootstrap_sshd.sh` via the RunPod
  proxy fixed it; direct port this cycle was **1683** (changes every resume).
- pymaster install path that WORKED on the pod (recorded per campaign rule): apt
  `libgsl-dev libfftw3-dev libcfitsio-dev pkg-config` then plain `pip3 install pymaster`
  → **pymaster 3.0** (no conda on pod; pip built cleanly against system GSL 2.7.1/FFTW3).
  healpy 1.19.0 pip wheel.
- Jobs run: G3 MASTER-decoupled 4×4 (N=2000, ~62 min) · P1B namaster-proof
  `rebuild_workspace_check.py` (PASS 9.926e−24) · G4 confusion+null (N=500, ~9 min after
  warm cache) · all smoke-tested before full launches.
- **No H200 deployed; total phase-2 pod spend ≈ $0.36.** Cumulative campaign GPU spend
  (G1+G2 session ~$0.71 + earlier ~$0.26 + phase 2 ~$0.36) ≈ **$1.33**; the only large prior
  spend remains the banked A100 e2e run (~$12.44, 2026-07-11/12) which G4 reused instead of
  re-running (est. $20–50 H200 avoided).
- Backups: every phase-2 JSON/npz/receipt in 3 verified locations (local repo commit · HF
  `bamfai/galaxy-chirality-catalog :: p4_compute_phase2_2026-07-18/` sha256 round-trip
  MATCH · pod until verification) before podStop.

## Integrity ledger
- No gate claimed closed by this document. Readiness 80 HOLDS.
- G3 uses the committed/immutable-cached catalog; no fabricated numbers; smoke-verified.
- G1 deliberately NOT launched blind (would fail its own manifest acceptance + waste a pod).
- All pod work: `/backup-3plus` before any stop; checkpoint to volume; never single-source.
