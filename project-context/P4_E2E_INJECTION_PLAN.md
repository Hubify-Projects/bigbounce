# P4 end-to-end (image-level) injection-recovery plan — OPEN-COMPUTE directive L

**Status:** Phase 1 (scope + de-risk) complete — inventory done, pilot run locally.
**Do not spin a pod until the orchestrator authorizes this plan.**

## 1. The MAJOR being closed

P4's #1 recurring reviewer MAJOR: the injection-recovery sweep
(`scripts/injection_sweep_extended.py`, `scripts/full_catalog_injection_recovery.py`)
injects dipoles into the **hard-label healpix field** (per-pixel CW rates) and never
traverses the **ViT classifier** at the image level. The paper's classifier-noise
dilution `g = 2a − 1 = 0.398` (a = 0.6991) comes from the GZ1 human-label
cross-match, not from an end-to-end image → classifier → label measurement.

## 2. Inventory (verified 2026-07-11)

| Asset | Found | Location |
|---|---|---|
| Trained v2 classifier weights | YES | HF `bamfai/galaxy-chirality-v2/chirality_model_v2_best.pt` (88 MB, keys `enc`/`head`/`val_acc`=0.9369; ViT-Small/16 timm + 3-class MLP head). GZ1-only variant at `gz1only/chirality_model_gz1only_best.pt`. Pod copy was `/workspace/analysis3_outputs/` (not needed — HF copy verified loadable). |
| Image data pipeline | YES | HF `mwalmsley/gz_desi` streaming dataset, `image` field (PIL) — the exact production source in `pipelines/p2_chirality/run_v2_inference.py`. Preprocessing: `Resize(224,224) → ToTensor → Normalize(ImageNet)`. No Legacy Survey cutout service needed. |
| Injection machinery | YES (field-level only) | `pipelines/p2_chirality/scripts/injection_sweep_extended.py`, `scripts/full_catalog_injection_recovery.py` — healpix-field injections; confirms the gap. |
| Production catalog | YES | HF `bamfai/galaxy-chirality-catalog/catalog_production.parquet` (ra/dec/class_eq/p_eq; no images — images come from gz_desi by `id_str`). |

## 3. The mirror-flip injection (pilot, run locally)

A horizontal mirror of a real galaxy image is a **physically exact chirality
inversion** — no synthetic image generation. Script:
`pipelines/p2_chirality/scripts/e2e_mirror_flip_transfer_function.py`.
Artifact: `pipelines/p2_chirality/outputs/canonical_provenance/e2e_mirror_flip_transfer_function.json`.

**Critical honesty note (affects interpretation):** the production catalog labels
are the **Z₂ mirror-equivariant TTA** outputs (`class_eq`, `p_eq` per
`equivariant_postprocess.py`): `p_eq(x) = [p(x) + swap(p(mirror x))]/2`. Under EQ
inference the mirror response is exactly antisymmetric **by construction**, so a
mirror-flip is registered with probability 1 (verified numerically in the pilot).
Mirror-flip therefore CANNOT probe EQ-pipeline dilution. What the RAW-mode flip
test measures is the classifier's **parity-odd information content**: the fraction
of CW/CCW calls driven by genuine chirality-carrying features rather than
flip-invariant noise. That is exactly the quantity a referee wants when asking
whether `g = 0.398` (human-ground-truth calibration) is an honest transfer factor,
and it is measured **through the actual ViT on real survey images**.

**Pilot smoke result (n=212 pairs, MPS, seed = stream order):**
- RAW transfer function `T_raw = 0.571 ± 0.034` (P(argmax flips CW↔CCW))
- RAW image-level `g_img = 2·a_img − 1 = 0.198` in the spiral↔spiral pool
  vs paper's GZ1-derived `g = 0.398`
- Full pilot (n=2500, confidence-stratified + EQ verification) running; final
  numbers in the JSON artifact.

Interpretation guardrails (NEVER overclaim):
- `T_raw`/`g_img` on unfiltered stream galaxies is dominated by low-confidence
  marginal spirals; the paper's dipole analysis uses the HC cut `p_eq > 0.6`.
  The confidence-stratified bins in the artifact are the referee-grade numbers.
- If HC-stratum `g_img` ≳ 0.398 → the paper's g is conservative at the image
  level for the analysis sample; if < 0.398 → the paper's sensitivity claims
  (A₅₀/A₉₅ → true-amplitude mapping ~1.88%) must be restated with the measured
  image-level transfer. Either way the result goes in the paper — no steering.

## 4. Full-run design (RunPod)

**Goal:** the referee-grade end-to-end statement — mirror-pair inference over the
full production analysis sample, stratified by confidence/leg/depth, plus a hybrid
image→field injection-recovery re-run using the measured per-galaxy transfer.

### Stage A — full-catalog mirror-pair sweep
- Sample: all 8.67M gz_desi galaxies (2 forward passes each = 17.3M inferences),
  or minimally the 3.2M analysis spirals matched by `id_str`.
- Throughput: production inference ran ~1000 gal/s on datacenter GPU with the
  `/gpu-dataloader-pattern` (DataLoader num_workers=16, pin_memory, batch 512).
  Mirror pass doubles work → ~17.3M / 1000 s⁻¹ ≈ 4.8 h; with setup ≈ 6 h wall.
- Outputs: per-galaxy `(id_str, p_raw, p_raw_mirror, p_eq, flip_detected)`
  parquet (~1.5 GB) + summary JSON (transfer function overall, by confidence
  bin, by survey leg, by depth quartile).

### Stage B — hybrid image→field injection-recovery
- Use the measured per-confidence-stratum image-level transfer to redo the
  dipole injection-recovery: inject a dipole by flipping physical chirality of
  a position-dependent subset of galaxies **at the image level** (mirror the
  image, re-run the ACTUAL classifier, take its label), rebuild the healpix
  field from those labels, run the standard MASTER/real-space recovery.
- This is the literal "injection-recovery traverses the classifier" ask.
  Amplitudes A ∈ {0.5, 0.75, 1.0, 1.5, 2.0}%, ≥20 MC axes per amplitude on a
  fixed 1M-galaxy subsample (each MC only re-labels the flipped subset —
  incremental cost small since flip labels are precomputed in Stage A:
  flipping galaxy i's true chirality = swapping its (orig, mirror) labels).
  Stage B is therefore mostly CPU post-processing of Stage A outputs.

### Pod spec + cost
| Item | Spec |
|---|---|
| GPU | 1× A100 80GB (community ~$1.19–1.64/hr) or RTX 4090 (~$0.44–0.69/hr, ~60% throughput) |
| Image | `runpod/pytorch:2.x-cuda12` + `pip install timm datasets` |
| Disk | 100 GB volume |
| Wall time | Stage A ≈ 6 h (A100) / ≈ 10 h (4090); Stage B ≈ 2 h CPU |
| **Cost** | **A100: ~$10–13 total; 4090: ~$5–8 total** |

### Backup-3plus (per directive E — ALWAYS)
1. Local: `pipelines/p2_chirality/outputs/canonical_provenance/` (JSON) + `master_results/` (parquet)
2. HF: `bamfai/galaxy-chirality-catalog` (new files `e2e_mirror_pairs.parquet`, `e2e_transfer_function_full.json`)
3. Backblaze B2 bucket (existing bigbounce backup path)
4. Convex metadata (`activityFeed:add` + artifact record)
Mirror at the 2 h milestone, before stop, and at end of session.

### Abort criteria
- If measured throughput < 300 gal/s after DataLoader tuning → stop, re-plan.
- Budget hard cap: $20.

## 5. Paper integration (after full run)
- New appendix subsection "End-to-end image-level transfer function"; replace the
  "assumes symmetric misclassification" caveat around `g = 2a − 1 = 0.398` with the
  measured image-level numbers; propagate per directive I6 (figure images too).
- Whatever the numbers are, they get reported. NEVER fabricate, never steer.
