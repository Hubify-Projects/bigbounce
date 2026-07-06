# P4 — Full-N GZ1-human-label-only chirality-dipole re-inference

**Date:** 2026-07-06 (UTC run)
**Trigger:** Both calibrated P4 referees (Grok + Gemini) judged the committed
GZ1-only independence check (N=14,964, `outputs/gz1only_dipole_result.json`)
UNDERPOWERED — that N came from an arbitrary 20,000-galaxy streaming cap in the
pod inference job, ~8× worse σ floor than the headline. They want the GZ1-only
null recomputed at the largest N obtainable, with chirality labels coming ONLY
from Galaxy Zoo 1 human classifications (independent of the CE-ResNet
pseudo-labels the production catalog is built on).

## What limited the old N=14,964

The prior GZ1-only run (`outputs/gz1only_dipole_result.json`, v1.0.202) trained a
GZ1-labels-only model on the pod, then ran inference on **only 20,000 streamed
`mwalmsley/gz_desi` galaxies** (`galaxies_seen: 20000`), of which 14,964 passed
the conf>0.6 spiral cut. The N was capped by the **arbitrary 20k streaming cap**,
NOT by the true GZ1×DESI overlap. Confirmed against the committed GZ1 Platt-recal
artifact (`r42_results/wave_14_fff_gz1_platt_recal.json`): the real confident
GZ1×DESI 1-arcsec cross-match is **46,017** galaxies — ~3× larger.

## Local feasibility — YES, computed with NO pod dependency

Both required inputs are public / already local:

| Input | Source | Status |
|-------|--------|--------|
| GZ1 human CW/ACW votes | `GalaxyZoo1_DR_table2.csv.gz` (Lintott+2011, data.galaxyzoo.org) | public, downloaded (20 MB, 667,944 rows) |
| DESI galaxy positions (ra,dec) | `catalog_production.parquet` | local HF cache (8,474,531 rows) |

**Key design choice — stronger than a GZ1-only model.** Rather than retrain a
GZ1-labels-only network (the pod route the referees couldn't reproduce), this
test uses the **GZ1 human CW/ACW votes themselves as the per-galaxy chirality
label**. There is NO learned model of any kind in the chirality label chain — it
is the maximally CE-ResNet-independent test. The DESI catalog is used ONLY for
sky positions (footprint); its `class_eq` column is never touched.

**Estimator = byte-identical to the headline generator** `run_dipole_catalog_c.py`:
HEALPix NSIDE=64, MIN_PIX_COUNT=10, conf_cut=0.6, `hp.fit_dipole`, N_MC=10,000
per-pixel label-permutation null, seed 20260418.

Cross-match reproduces the committed platt-recal artifact exactly (48,414
confident GZ1 spirals → 46,017 matched to DESI @ 1″), validating the pipeline.

Script (committed): `pipelines/p2_chirality/run_dipole_gz1only_fullN.py`
Result (committed): `pipelines/p2_chirality/outputs/gz1only_fullN_dipole_result.json`

## Result — the null HOLDS at 3× the power

| Quantity | Old GZ1-only (N=14,964) | **New GZ1-human-only (N=46,017)** | Headline CE-ResNet (N=949,584) |
|----------|------------------------|-----------------------------------|--------------------------------|
| N high-conf spirals | 14,964 | **46,017** (3.08×) | 949,584 |
| Label source | GZ1-trained model | **GZ1 human votes (no model)** | CE-ResNet pseudo-labels + eq |
| CW fraction | 0.4981 | **0.4836** | 0.4961 |
| Dipole amplitude | 1.695 (recal units) | **0.05462** | 0.004423 |
| per-pixel-perm null | z=−0.044σ (p=0.45) | **z=−0.539σ (p=0.666)** | z=+0.41σ (p=0.31) |
| per-galaxy null | — | z=−0.551σ (p=0.675) | z=+0.58σ (p=0.257) |

**Verdict: the chirality dipole is consistent with null at z = −0.539σ
(rank-p = 0.666) using N=46,017 galaxies whose CW/CCW labels are Galaxy Zoo 1
human votes ONLY — fully independent of the CE-ResNet pseudo-labels.** The
negative z (below the MC mean) means the observed dipole is if anything *weaker*
than an isotropic random field at this N. Both null procedures agree. The null
does not merely survive the increased power — it is recovered cleanly with the
learned model removed entirely from the label chain.

## Does this answer the referees' underpowered-independence concern?

Yes, on both axes they raised:

1. **Power:** N goes 14,964 → 46,017 (3.08×), tightening the statistical-only
   dipole floor by √3.08 ≈ 1.75× relative to the old cross-check. This is the
   maximal N obtainable for confident (P>0.6) GZ1 CW/CCW votes cross-matched to
   the DESI footprint — the entire confident GZ1 spin catalog.
2. **Independence:** the labels are raw human votes, so this is *more*
   independent than a GZ1-trained model (which still learns CE-ResNet-era image
   features). Zero pseudo-label content.

**Residual honesty:** this is still below the headline N=9.5×10⁵ (the GZ1 spin
catalog simply does not contain more confident CW/CCW spirals inside the DESI
footprint — it is exhausted at ~46k, not truncated). A full-catalog match to
headline N is impossible from GZ1 human labels alone because GZ1 only labeled
~46k confident-spin DESI-overlapping spirals. So N=46,017 is the *ceiling of the
independent human-label test*, not another arbitrary cap. The paper should state
this exhaustion explicitly rather than implying more N is available.

## Proposed P4 .tex update (NOT yet applied)

Replace the "reduced-N, factor-~63" framing in
`\label{sec:pseudolabel_independence}` with the direct human-label result:
- Headline of the subsection: report **z=−0.54σ (p=0.67) at N=46,017 GZ1 human
  CW/CCW labels**, artifact `outputs/gz1only_fullN_dipole_result.json`.
- Keep the old GZ1-only-model run as a corroborating second line.
- Recast the "full-catalog GZ1-only re-inference is a future extension" caveat:
  the independent human-label test is now performed at its natural ceiling
  (N≈46k = the full confident GZ1×DESI spin overlap); the reason it does not
  reach 9.5×10⁵ is that GZ1 human spin labels are *exhausted* at ~46k in the
  DESI footprint, not that compute was unavailable.
- Fix the N in the "Decisive rebuttal" sentence: 1.50×10⁴ → 4.60×10⁴, and z
  −0.04σ → −0.54σ (p 0.45 → 0.67).

Version bump: patch (v1.0.210 → v1.0.211), directive-G PDF hygiene + Convex
`paperVersions:bump` + site + SSOT + reviewTimeline entry in the same bundle.

## Provenance / reproducibility

```
python pipelines/p2_chirality/run_dipole_gz1only_fullN.py
#   auto-downloads GZ1 Table 2 to /tmp, reads local HF catalog cache,
#   cross-matches, runs identical NSIDE=64 / N_MC=10000 / seed 20260418 null.
```
No pod, no HF token, no API key required. Deterministic (fixed seed).
