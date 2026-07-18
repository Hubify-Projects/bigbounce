# G1 manifest-retained ViT-Small retrain — revision `g1-retrain-2026-07-17`

BigBounce Paper 4 (Galaxy Chirality Catalog) — Gate G1 regenerable training realization.

## Honest scope (READ FIRST)
This checkpoint is the **GZ1-core + synthetic** realization only. `ce_resnet_present = false`
in the manifest: the Jia et al. 2023 CE-ResNet catalog (`pre_desi.fits`) that supplied
~67.5% of the *historical* realization (17,153 spirals + 826 non-spirals) was lost with the
pod's ephemeral disk and has **not** been re-provisioned. This run produces a fully
regenerable manifest + checkpoint, but does **not** yet engage the CE non-spiral
826-vs-846 sub-conflict. Full historical-composition supersession still requires
re-provisioning CE-ResNet and re-running the CE-ready wrapper.

## Result
- `best_val_acc = 0.9930515344528084` @ epoch 47 (early stop at epoch 62; best=47)
- ViT-Small `vit_small_patch16_224`, 3-class (CW / CCW / NOT_SPIRAL), 10.98M trainable
- n_total = 8637 (train 6910 / val 1727); class_counts CW 3316 / CCW 3321 / NS 2000
- Composition: gz1=6637 (exact historical GZ1 identities) + synthetic=2000; ce_spiral=0, ce_not_spiral=0
- Seeds: all 42 (python/numpy/torch/gz1_sample/split RandomState)
- split_rule: `RandomState(42).shuffle(arange(n)); val=first max(n//5,500)`
- git_sha (training wrapper): `38edf6c5ad3960579d1404799502f3ab83120fb2`

## Provenance
- GZ1 labels: `GalaxyZoo1_DR_table2.csv.gz` (S3), sha256 `5121e43f502856c9f73e31934a6e7d7282669c3ae065564a31f5d5115f45541d`, P>0.7
- Images/coords: `mwalmsley/gz_desi` resolved rev `b7583bb2ac445e93c5447a08063acd7c1477fd13`
- Smith42 parent rev cited: `bdd1b063a9a22874a79a4363aa9fb6a2b356a4c2`

## SHA256 (this revision's artifacts)
- `g1_ckpt_best.pt`         : `aed109dcda13f6468aaef60c5824c7a94d1109424ed25df1e3959aa10a752387` (88046112 bytes)
- `g1_training_result.json` : `0cd57a5535948ac7ef5faa432ea7e2d129296a96cd6235b1f769c7dc266567e3`
- `g1_training_manifest.json`: `e5de8e030996dea9ac42f1af6a63a45f28b1418f1fa78ee33a26e2d240a10729`

Trained on RunPod pod `580dgszgib3ti4` (RTX A4000). Additive upload; does not overwrite
existing repo files (`chirality_model_v2_best.pt` etc. remain the historical receipts).
