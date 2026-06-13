# Known Reproducibility Gaps

This document honestly discloses what CANNOT currently be reproduced from
the provided materials and how the paper text handles each gap.

> **⚠ Path-C rebuild note (2026-04-22, fire #170):** §6 DESI DR1 Anomaly
> Catalog (195,829 anomalies / BigAE trained on 47K / AutoEncoder proxy)
> and §7 Enhanced 18M Catalog (44% progress) below are pre-Path-C content
> preserved for reproducibility history. Current Path-C state: **11/12
> criteria CLOSED** — SDSS native re-score 1,925,279 scored (~6500×
> anomaly-rate reduction vs cross-transfer, fire #164); LAMOST 21.4×
> reduction; CMB 100% injection-recovery @5σ; NEOWISE ecliptic mask;
> injection-recovery all-surveys; 8-way dedup **378,480 unique + 637
> multi-survey clusters** (fire #164); Paper 3 PDF recompile 28 MB / 33 pp
> / 0 undef (fire #168); HF rebuild 5-file 15.2 MB bundle (fire #166); P1
> PDF V3; site-sync. **Only criterion #4 DESI 5-fold OOS k-fold remains**:
> retrieval scaffold authored + dry-run clean (fire #170, deterministic
> checksum 1812395110), Houston ack gates ~1-2h live SPARCL run at ~$3 pod
> spend. Canonical per-fire state: [`project-context/SSOT/drive-to-100.md`](../../project-context/SSOT/drive-to-100.md)
> Loop log and [`project-context/SSOT/index.md`](../../project-context/SSOT/index.md).

## 1. No Bespoke CAMB Modifications

**What the paper describes (current v1B.0.68):** A ΛCDM + ΔNeff proxy run
using stock CAMB with ΔNeff (nnu − 3.046) as a free parameter. No custom
dark energy class or modified perturbation initial conditions.

**What exists:** Four Cobaya YAML configurations (`cobaya_planck.yaml`,
`cobaya_planck_bao.yaml`, `cobaya_planck_bao_sn.yaml`,
`cobaya_full_tension.yaml`) — all using stock CAMB with `bbn_predictor:
PArthENoPE`. Frozen chain artifacts under
`cosmology/frozen/full_tension_20260311_1728/` and
`cosmology/frozen/planck_bao_sn_20260312_1954/`.

**Paper handling:** Paper explicitly states stock CAMB throughout (§III,
Table I caption, §V). The spin-torsion framework provides theoretical
motivation for nonzero ΔNeff; the MCMC proxy uses the standard nnu
parameter with a flat prior Neff ∈ [2.046, 5.046].

**Sync note:** Stale "modified CAMB v1.5" language present in earlier repo
versions has been removed as of v1B.0.68.

## 2. Frozen Chains Committed; Fresh Proxy Chains Not Pre-Computed

**Status:** The frozen MCMC chains backing Paper I(b) Tables III–IV ARE
committed in this bundle (~257 MB under `reproducibility/cosmology/frozen/`,
including `full_tension_20260311_1728/` and `planck_bao_sn_20260312_1954/`
with chains and diagnostics). What is NOT included are fresh ΛCDM+ΔN_eff
proxy chains for independent re-verification: the Cobaya configurations are
provided and can be run with stock CAMB. Fresh chains take ~4-12 hours per
configuration on 4 CPU cores (~1 GB per run).

**Workaround:** Run `reproduce_cosmology.sh` to generate fresh chains, then
compare against the committed frozen chains.

## 3. No Bayes Factor Computation

**What the paper reports (v1B.0.68):** No ln B values are claimed. The paper
explicitly states that model-comparison statistics (AIC, BIC, ln B) are not
reported because robust ln B against ΛCDM requires dedicated nested sampling
(the ΛCDM point is unsampled by the Metropolis-Hastings chain at >4σ in the
joint marginal tails; see fn. fn:wcaveat in the tex).

**What exists:** MCMC configs only. Adapting to PolyChord nested sampling
requires changing the Cobaya sampler block and is computationally ~10× more
expensive. This remains a post-submission follow-up item.

**Note:** Earlier repo versions quoted ln B = −1.2 ± 0.3 / +4.8 ± 0.5 —
those were fire-#21 bookkeeping confabulation (see §8 of this file) and have
been fully retracted from the paper.

## 4. Galaxy Chirality Classifier — PARTIALLY RESOLVED

**What the paper describes:** A CNN trained on Galaxy Zoo labels.

**What now exists:** Production chirality pipeline v2 running on H100 GPU.
Model: 93.7% accuracy, 3-class (CW/CCW/NOT_SPIRAL), 8/8 bias tests passed,
equivariant CW fraction = 0.5012. Currently at 86.5% (7.3M/8.47M galaxies).
Code at: `pipelines/p2_chirality/train_chirality_v2.py`
Model on HuggingFace: `bamfai/galaxy-chirality-v2`

**Status:** RUNNING — will be fully resolved when H100 inference completes.

## 5. No CMB EB/TB Analysis from Maps

**What the paper describes:** Power spectrum estimation from Planck HFI
data using SMICA.

**What exists:** No Planck map processing code. All birefringence values
are literature citations (Minami & Komatsu 2020, Eskilt 2022, ACT DR6).

**Paper handling:** Updated to cite published measurements, not original
analysis. NaMaster injection tests validate our approach at NSIDE=1024.

## 6. DESI DR1 Anomaly Catalog — NEW (not in original paper)

**What exists:** 195,829 spectral anomalies from 18M DESI DR1 spectra.
AutoEncoder model (BigAE) trained on 47K spectra, inference on H200 GPU.
200/200 top anomalies verified genuine (0% sky artifacts).
6-database cross-reference: 99.8% absent from SIMBAD.
Model on HuggingFace: `bamfai/desi-spectral-anomaly-detector`
Code at: `pipelines/p1_highz_tracers/outputs/desi_dr1/`

**Known gaps in anomaly pipeline:**
- Injection/recovery test uses proxy model (33% baseline) — needs real BigAE
- B-dominant population (44K objects, 23%) not yet investigated for systematics
- Full 195K cross-match against AllWISE/Gaia pending (top 1K done)
- No spectral line identification yet (waiting for enhanced 18M catalog)

## 7. Enhanced 18M Catalog — IN PROGRESS

**What exists:** 45-column catalog of all DESI DR1 spectra including
latent vectors, redshifts, photometry, morphology. Running on H200.
Currently at 44% (7.9M/17.9M spectra). Output: Parquet format.
Code at: `pipelines/p1_highz_tracers/scripts/enhanced_18M_inference.py`

## 8. w0-wa MCMC — RETRACTED fire #25 (2026-04-18)

**What exists:** The Cobaya config (`reproducibility/cosmology/cobaya_w0wa_quintom_test.yaml`) and chain directory skeleton are retained for reproducibility history, but the previously advertised results "Converged CPL MCMC (R-1 = 0.009, 50,880 samples), w0 = -0.871 ± 0.061, wa = -0.542 ± 0.247, P(quintom-B) = 98%" were fire-#21 bookkeeping confabulation. Paper 1 §VII.H is explicit: zero free w0-wa samples among the 309,789 frozen posterior samples in this program. The DESI DR2 2.8-4.2σ w-crossing signal is cited as observational context in the bounce portfolio, not as a BigBounce-group MCMC result.
