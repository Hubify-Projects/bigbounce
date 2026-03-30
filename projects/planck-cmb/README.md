# Planck CMB Patch Anomaly Detection

**Status:** Prototype | **Paper:** TBD

## Overview
Autoencoder trained on simulated CMB patches, applied to real Planck SMICA data. Prototype found 42 anomalous patches spatially clustered near the CMB dipole axis.

## Key Results (Prototype)
- 42 anomalous patches at 3σ threshold
- Spatial clustering near dipole axis (likely systematic but genuine)
- Conv autoencoder (1.1M params, 128-dim latent)

## Next Steps
- Scale to full resolution (NSIDE=1024+)
- Add ACT DR6 data
- Proper systematic analysis (dust, foregrounds)
- Test birefringence β = 0.27° prediction

## Files
- Pipeline: `pipelines/pipeline_a_cmb/`
- Patches: `pipelines/pipeline_a_cmb/outputs/`

## Cost
~$10 so far (prototype only)
