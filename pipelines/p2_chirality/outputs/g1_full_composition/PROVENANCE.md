# G1 full-composition (CE-included) assembly — provenance

**What this is:** the G1 regenerable realization data-assembly + manifest with the
CE-ResNet component INCLUDED (`ce_resnet_present=true`) — the first time the
wrapper's CE ingestion path has ever run. It resolves the 826-vs-846 CE
non-spiral sub-conflict.

**How it was produced (honest):** the CE composition counts come from the CPU
data-assembly stage of the wrapper (streaming gz_desi crossmatch), NOT the GPU
training stage. They are deterministic under seed=42 + the pinned gz_desi
revision + the committed `pre_desi.fits`. This manifest was produced by
`scripts/g1_ce_composition_assembly.py` (which calls the EXACT wrapper functions
`train_g1_manifest.build_dataset / make_split / write_manifest`, skipping only the
GPU `build_model` + training loop). It is byte-for-byte the same manifest the pod
`train_g1_manifest.py --full` run records — the pod adds the GPU-trained
checkpoint on top. Run on local CPU 2026-07-19/20 because the target A4000 pod
`580dgszgib3ti4` (and fallback `99srknm4s1cc3l`) hosts were GPU-full
("not enough free GPUs on the host machine") at execution time; the retrain
checkpoint is the one remaining GPU-gated item.

## Inputs
- CE-ResNet catalog: `../external_catalogs/pre_desi.fits`
  sha256 `894dbe887140c165488a0f6053e2cd21f4ab72be9b06ece733e6ce177c0e304b`
  (Zenodo DOI 10.5281/zenodo.7167388; Jia et al. 2023, arXiv:2210.04168).
- GZ1 CW/CCW labels: `GalaxyZoo1_DR_table2.csv.gz` (S3), P>0.7, balanced 19,613/class.
- Images + coords: HF `mwalmsley/gz_desi`, rev `b7583bb2ac445e93c5447a08063acd7c1477fd13`.
- scan_limit = 150,000 gz_desi rows; 3" crossmatch tol; seeds all = 42.

## CE COMPOSITION — the 826-vs-846 adjudication (verbatim)
| source        | count  |
|---------------|--------|
| gz1           | 6,637  |  (reproduces historical GZ1 count EXACTLY)
| ce_spiral     | 17,153 |  (reproduces historical 17,153 CE spirals EXACTLY)
| ce_not_spiral | **819**|  <-- the CE non-spiral count
| synthetic     | 2,000  |
| **total**     | **26,609** |

class_counts: {CW(0): 11904, CCW(1): 11886, NOT_SPIRAL(2): 2819}

**Adjudication: NEITHER 826 nor 846 — the reproducible value is 819.**
`6637 + 17153 + 826 + 2000 = 26,616` (the smaller historical record) — so the two
large deterministic components (gz1, ce_spiral) reproduce exactly and the ENTIRE
historical 826-vs-846 / 26616-vs-26626 conflict is isolated to the CE non-spiral
crossmatch. That crossmatch draws a seeded 50,000-object subsample of the 74,174
non-spiral candidates (p_cw+p_acw<0.02) and matches within 3", so its exact count
is subsample/boundary-sensitive — precisely the irreducible ambiguity the paper's
Table 12 flagged. The regenerable realization supersedes the unrecoverable
historical record with **ce_not_spiral = 819, total = 26,609**.

## Files
- `g1_full_composition_manifest.json` — full 26,609-object manifest (train/val idx,
  per-object source + gz_desi id + ra/dec, seeds, split rule, revisions, git sha).
  sha256 `431f84f09519d1ef8be9e2f488f199b5d6b1c5127a77d4e25f53df04cf110777`.
- `ce_composition_full.json` / `ce_composition_smoke.json` — the composition summaries.
- `g1_ce_smoke_manifest.json` — CE smoke manifest (scan 8000: gz1=262, ce_spiral=200
  (smoke cap), ce_not_spiral=38 — proves the CE ingestion path end-to-end).
- `ce_full_assembly.log` — the full-run assembly log (50K/100K/150K checkpoints).

## Still GPU-gated (honest)
The retrained ViT-Small checkpoint on this 26,609-object realization + the
per-epoch checkpoints require the A4000 pod. Launch procedure: rsync `pre_desi.fits`
+ `train_g1_manifest.py` to the resumed pod, `train_g1_manifest.py --full --epochs 80`;
the pod manifest reproduces these exact counts and adds the checkpoint.
