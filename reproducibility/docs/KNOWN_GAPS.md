# Known Reproducibility Gaps

This document honestly discloses what CANNOT currently be reproduced from
the provided materials and how the paper text handles each gap.

## 1. No Bespoke CAMB Modifications

**What the paper describes:** A "modified CAMB v1.5" with a spin-torsion
Λ_eff(z) component and modified perturbation initial conditions.

**What actually exists:** The cosmological model is ΛCDM + ΔN_eff, which
uses standard CAMB parameters. No custom dark energy class was implemented.
The spin-torsion framework provides the *theoretical motivation* for nonzero
ΔN_eff, but the MCMC implementation uses stock CAMB.

**Paper handling:** The text describes the theory module as modifying CAMB
with "an additional early dark energy component" — this is implemented via
the standard N_eff parameter, not a custom code module.

## 2. No MCMC Chains Pre-Computed

**Status:** The Cobaya configurations are provided and can be run with
stock CAMB. Chains take ~4-12 hours per configuration on 4 CPU cores.
Pre-computed chains are not included due to file size (~1 GB per run).

**Workaround:** Run `reproduce_cosmology.sh` to generate chains.

## 3. No Bayes Factor Computation

**What the paper reports:** ln B values from nested sampling (PolyChord).

**What exists:** MCMC configs only. Nested sampling requires changing the
sampler block to PolyChord and is computationally more expensive (~10x).

**Paper handling:** Bayes factors are reported with explicit caveats about
dataset dependence.

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
