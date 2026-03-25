# w0-wa Quintom-B Test: DESI DR2 Phantom-Divide Crossing

## Why This Test

DESI DR2 (arXiv:2503.14738) reports **4.2-sigma evidence** for the dark energy equation of state crossing the phantom divide w = -1 as a function of redshift. Specifically, they find:

- **w0 = -0.752 +/- 0.070** (quintessence-like at z = 0)
- **wa = -1.01 +/- 0.30** (phantom-like in the early universe)
- **w0 + wa = -1.76 +/- 0.25** (firmly below -1)

This is "quintom-B" behavior: the dark energy equation of state starts above -1 at low redshift and crosses below -1 at higher redshift. In standard single-scalar-field models, crossing w = -1 is forbidden by a no-go theorem (Vikman 2005, Cai & Saridakis 2010). However, **spin-torsion bounce cosmology naturally produces an effective quintom EOS** from the torsion scalar field, since the field traverses the bounce where the effective w diverges through -1.

Our existing MCMC infrastructure tested Delta_Neff (extra relativistic species from torsion) but never tested the dark energy equation of state itself. This config fills that gap by fitting the CPL parameterization w(a) = w0 + wa*(1-a) to Planck + BAO + SN data.

## What We Test

**Key question:** Does the same Planck NPIPE + SDSS DR16 BAO + Pantheon+ dataset combination that we used for Delta_Neff independently confirm the DESI DR2 quintom-B signal?

### Quintom-B Criteria (all must hold simultaneously)
1. **w0 > -1** — quintessence-like at z = 0
2. **w0 + wa < -1** — phantom-like in the past
3. **A crossing redshift z_c exists** where w(z_c) = -1

### Derived Diagnostics
- `P(quintom-B)` — posterior probability that both criteria hold
- `z_cross` — the phantom-divide crossing redshift
- `sigma_from_LCDM` — statistical distance from w0 = -1, wa = 0
- `sigma_from_DESI` — consistency check with DESI DR2 values

## How to Run

### Prerequisites

```bash
pip install cobaya==3.5.4
cobaya-install cosmo -p ./packages
```

### Run the MCMC

```bash
# Single chain (for testing)
cobaya-run cobaya_w0wa_quintom_test.yaml

# Multiple chains for convergence (recommended: 4-7 chains)
# Modify the output path and seed for each:
for i in $(seq 1 6); do
    cp cobaya_w0wa_quintom_test.yaml w0wa_chain_${i}.yaml
    # Edit output path in each copy
    cobaya-run w0wa_chain_${i}.yaml &
done
```

On a GPU-enabled RunPod instance (H100), expect ~4-8 hours per chain to converge (R-1 < 0.01). On CPU, expect ~24-48 hours.

### Analyze the Chains

```bash
# After chains converge:
python analyze_w0wa_quintom.py --chain-dir chains/w0wa_quintom --burn-in 0.3

# Custom output directory:
python analyze_w0wa_quintom.py \
    --chain-dir chains/w0wa_quintom \
    --output-dir results/w0wa_quintom \
    --burn-in 0.3
```

### Outputs
- `w0wa_quintom_contours.png` — 2D posterior contours with DESI DR2 and LCDM marked
- `wz_reconstruction.png` — w(z) reconstruction from posterior samples
- `crossing_redshift.png` — posterior distribution of the crossing redshift z_c
- `w0wa_triangle.png` — triangle plot of (w0, wa, H0, Omega_m, sigma8, S8) (requires getdist)
- `quintom_results.txt` — full diagnostic summary
- `quintom_results.csv` — machine-readable results for data explorer embedding

## What to Look For

### Positive Result (supports quintom bounce)
- `P(quintom-B) > 0.68` — strong evidence for phantom-divide crossing
- `sigma_from_LCDM > 2` — significant departure from w = -1
- `sigma_from_DESI < 1` — consistent with DESI DR2 findings
- Crossing redshift `z_c ~ 0.5-1.0` — consistent with DESI pivot redshift

### Null Result (consistent with LCDM)
- `P(quintom-B) < 0.30` — no evidence for crossing
- `sigma_from_LCDM < 1` — w0 = -1, wa = 0 within posterior
- Posterior centered on LCDM point in w0-wa plane

### Dataset Limitation
Our BAO data uses SDSS DR16, not DESI DR2. The DESI BAO measurements (especially the z ~ 0.7 LRG bin) are the primary driver of their quintom signal. If our SDSS-based posterior is consistent with LCDM, the next step is to re-run with DESI DR2 BAO likelihoods once they are available in Cobaya.

## Connection to Bounce Cosmology

The quintom crossing is significant for the BigBounce program because:

1. **Quintom no-go theorem bypass:** Single minimally-coupled scalar fields cannot cross w = -1. Torsion provides a geometric mechanism that bypasses this theorem because the Cartan torsion tensor contributes additional terms to the effective stress-energy.

2. **Bounce-DE unification:** If the same torsion scalar that drives the bounce also generates late-time quintom behavior, this would be the first observational link between pre-bounce physics and dark energy.

3. **f_NL prediction:** The matter bounce branch (Branch V) already has a parameter-free f_NL = -35/8 prediction. If quintom crossing is confirmed, computing f_NL for the quintom bounce model becomes a high-priority next step, as it would give a second independent prediction from the same framework.

4. **Falsifiability:** A confirmed quintom crossing with a specific z_c would give a precise prediction for SPHEREx and Euclid BAO measurements.

## Technical Notes

- **CAMB PPF mode:** The config uses `dark_energy_model: ppf` (parameterized post-Friedmann), which correctly handles the perturbation evolution when w crosses -1. Without PPF, CAMB would produce unphysical perturbation divergences at the crossing.

- **Prior volume:** The flat priors w0 in [-2.5, -0.3] and wa in [-3, 2] are intentionally broad to avoid prejudicing the result. The LCDM point (w0=-1, wa=0) is well within these priors.

- **No nnu:** Unlike our Delta_Neff configs, this config fixes N_eff at the standard value (3.046) and instead frees w0 and wa. This isolates the dark energy EOS test from radiation-sector effects.
