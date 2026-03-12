# BigBounce Paper-1 MCMC Clean Restart — Run Manifest Template

> **Classification:** CLEAN RESTART — no old chain data is imported.
> Old covariance matrices are used as warm-start proposals only.
> All chains receive fresh run IDs, fresh output directories, and clean provenance.

---

## Run Identity

| Field | Value |
|---|---|
| **Run ID** | `canonical_run_001` |
| **Start Date** | 2026-03-11 (planned) |
| **Classification** | CLEAN RESTART (not a resume of terminated runs) |
| **Previous Run** | Pre-crash Paper-1 runs (terminated 2026-03-09). Old artifacts archived as tuning references. |

---

## Models

### Canonical Model: LCDM + Delta-N_eff

- **Parameters sampled:** logA, nnu, ns, ombh2, omch2, tau, theta_MC_100
- **Derived parameters:** H0, S8, sigma8, omegam, delta_neff, As, age, cosmomc_theta
- **Nuisance parameters:** Mb (for H0 likelihood), A_planck, amp_143, amp_217, amp_143x217, n_143, n_217, n_143x217, calTE, calEE
- **Theory code:** CAMB
- **Priors:**
  - nnu: uniform [2.046, 5.046]
  - logA: uniform [1.61, 3.91]
  - (remaining priors per input.yaml)
- **Output prefix:** `spin_torsion`

### Control Model: LCDM

- Same parameter set as above but **nnu FIXED at 3.046** (no delta_neff)
- Removes 1 degree of freedom for model comparison
- **Output prefix:** `lcdm`

---

## Datasets

| Label | Components |
|---|---|
| **full_tension** | Planck NPIPE TTTEEE + lensing + BAO (SDSS DR16) + SN (Pantheon+) + H0 (Riess 2020) + S8 (DES) |
| **planck_only** | Planck NPIPE TTTEEE + lensing only |
| **planck_bao** | Planck NPIPE TTTEEE + lensing + BAO (SDSS DR16) |
| **planck_bao_sn** | Planck NPIPE TTTEEE + lensing + BAO (SDSS DR16) + SN (Pantheon+) |

---

## Chain Structure

- **4 chains per dataset per model**
- Chain naming: `chain_01`, `chain_02`, `chain_03`, `chain_04`
- NO chain1 legacy (old run had chain1 lagging — clean start here)
- Each chain gets a unique random seed (documented in manifest at launch)

### Total Chains

| Model | Datasets | Chains/Dataset | Total |
|---|---|---|---|
| Delta-N_eff | 4 | 4 | 16 |
| LCDM | 4 | 4 | 16 |
| **Grand Total** | | | **32** |

---

## MCMC Settings (per cobaya config)

| Setting | Value |
|---|---|
| Sampler | mcmc |
| Rminus1_stop | 0.01 |
| Rminus1_cl_stop | 0.2 |
| burn_in | 0.1 |
| learn_proposal | true |
| learn_proposal_Rminus1_max | 50 |
| drag | true |
| oversample_power | 0.4 |
| proposal_scale | 2.4 |
| max_tries | 40d |
| covmat | Path to warm-start covmat from old GPU run (or none for LCDM) |

---

## Warm-Start Policy

### Covariance Matrices

- Use learned covmats from `gpu_run_snapshot_20260305_0824` as initial proposal matrices
- These are 17x17 covariance matrices with full off-diagonal structure
- They encode posterior correlations learned during the first ~24h of the old run
- Available for all 4 Delta-N_eff datasets (28 covmats; use best from chain2-7)
- For LCDM control: remove nnu row/column from Delta-N_eff covmats to create 16x16 LCDM covmats

### What Is NOT Imported

| Artifact | Status |
|---|---|
| Chain files | **NOT imported.** Fresh chains start from sample 0. |
| Checkpoints | **NOT imported.** Fresh run. |
| Old run status | Archived as `pre_crash_tuning_assets/`, clearly labeled as NOT part of canonical posterior. |

---

## Convergence Targets

### Freeze Gates

All of the following must pass for a dataset to be "frozen" for publication:

| Gate | Criterion |
|---|---|
| 1 | R-hat (R-1) < 0.01 for H0 |
| 2 | R-hat (R-1) < 0.01 for Delta-N_eff (or nnu) |
| 3 | R-hat (R-1) < 0.02 for tau |
| 4 | ESS > 2000 for H0 |
| 5 | ESS > 2000 for Delta-N_eff |
| 6 | ESS > 1000 for tau |
| 7 | No drift in chain means > 0.1 sigma over last 25% of samples |
| 8 | GetDist validation passes |

### Priority Order

1. **full_tension** — anchor result for paper
2. **planck_bao_sn** — second strongest constraint
3. **planck_bao**
4. **planck_only**
5. **LCDM controls** — needed for model comparison but lower priority

---

## Hardware

| Resource | Specification |
|---|---|
| Pod type | RTX A6000 (or RTX 6000 Ada fallback) |
| Network volume | `bigbounce-paper1-canonical` (75 GB) |
| Pricing | On-demand (NOT spot) |
| Container image | `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04` |

---

## Provenance Rules

1. All chain data in `canonical_run_001/` is from this run ONLY.
2. No mixing of old and new chain samples.
3. Warm-start covmats are documented but treated as external tuning inputs.
4. Every chain file has a clear lineage from this manifest.
5. `MANIFEST.md` is updated daily with sample counts and convergence state.
6. `SHA256SUMS.txt` is generated for all chain files.

---

## Template Fields (to be filled at launch)

```yaml
run_id: canonical_run_001
start_timestamp: [TO BE FILLED]
pod_id: [TO BE FILLED]
pod_gpu: [TO BE FILLED]
pod_vcpus: [TO BE FILLED]
pod_ram_gb: [TO BE FILLED]
network_volume_id: [TO BE FILLED]
network_volume_name: bigbounce-paper1-canonical
git_commit: [TO BE FILLED]
cobaya_version: [TO BE FILLED]
camb_version: [TO BE FILLED]
python_version: [TO BE FILLED]
chain_seeds:
  dneff_full_tension: [seed1, seed2, seed3, seed4]
  dneff_planck_only: [seed1, seed2, seed3, seed4]
  dneff_planck_bao: [seed1, seed2, seed3, seed4]
  dneff_planck_bao_sn: [seed1, seed2, seed3, seed4]
  lcdm_full_tension: [seed1, seed2, seed3, seed4]
  lcdm_planck_only: [seed1, seed2, seed3, seed4]
  lcdm_planck_bao: [seed1, seed2, seed3, seed4]
  lcdm_planck_bao_sn: [seed1, seed2, seed3, seed4]
```
