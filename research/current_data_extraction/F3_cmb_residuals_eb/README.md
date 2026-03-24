# F3 — CMB Residual / EB Robustness Support

## Scientific Question

Can contamination-aware region scoring, null-tested EB analysis, and map-level robustness improve confidence in current birefringence and bispectrum inferences?

## Canonical Target

Birefringence: β = 0.27° (prediction), observed 0.342 ± 0.094° (Planck+ACT combined)
Bispectrum: support only — F1 handles the primary f_NL extraction

## Pipeline Stages

| Stage | Description | Gating |
|-------|-------------|--------|
| F3.1 | Data acquisition + verification | Must pass first |
| F3.2 | EB estimator baseline on nulls | Before any real-sky claims |
| F3.3 | Injection recovery | Before any real-sky claims |
| F3.4 | Patch / region quality scoring | After F3.2-F3.3 |
| F3.5 | Robustness across masks/frequencies | After F3.4 |
| F3.6 | Birefringence + bispectrum support | After all above |

## Data Products Required

| Dataset | Source | Size | Status |
|---------|--------|------|--------|
| Planck PR3 frequency maps (100/143/217 GHz, I/Q/U) | PLA (pla.esac.esa.int) | ~2GB each | Not downloaded |
| Planck PR3 component-separated maps (SMICA, NILC) | PLA | ~300MB each | Not downloaded |
| Planck PR3 confidence masks | PLA | ~50MB | Not downloaded |
| Planck PR3 beam window functions | PLA | ~10MB | Not downloaded |
| ACT DR6 maps (if accessible) | LAMBDA/ACT | ~1GB | Not downloaded |
| FFP10 simulations (for null tests) | PLA | ~50GB subset | Not downloaded |

## Key Dependencies

- healpy (HEALPix for Python)
- NaMaster (pseudo-Cℓ estimator with purification)
- numpy, scipy, matplotlib

## RunPod Requirements

| Task | Pod type | Reason | Est. time |
|------|----------|--------|-----------|
| Map download | CPU (any) | Network I/O | 1-2 hours |
| EB power spectrum estimation | CPU (32-core) | NaMaster is CPU-bound | 1-2 hours per map pair |
| Null simulation suite (100+ realizations) | CPU (64-core) | Parallelizable | 4-8 hours |
| Patch quality scoring (if CNN) | GPU | Only if justified | 2-4 hours |
