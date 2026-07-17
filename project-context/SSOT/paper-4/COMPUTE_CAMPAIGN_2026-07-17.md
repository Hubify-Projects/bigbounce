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
| **G3** | Joint sampling covariance across real-space dipole / WLS / monopole / harmonic ℓ=1 | CPU (local, committed catalog) | ~11 min | $0 | **LAUNCHED (local, detached)** |
| **G4** | Image-level classifier-injection → per-pixel confusion + generative null isolating the monopole mechanism | GPU (H200 preferred; A4000 ok) | ~4–12 h (8.47M-galaxy inference passes) | H200 ~$4.39/h → $20–50 | **PARTIAL scaffolding exists; scoped, not launched** |

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

## G2 — Training-disjoint held-out validation  ⟵ BLOCKED on G1 manifest

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

## Integrity ledger
- No gate claimed closed by this document. Readiness 80 HOLDS.
- G3 uses the committed/immutable-cached catalog; no fabricated numbers; smoke-verified.
- G1 deliberately NOT launched blind (would fail its own manifest acceptance + waste a pod).
- All pod work: `/backup-3plus` before any stop; checkpoint to volume; never single-source.
