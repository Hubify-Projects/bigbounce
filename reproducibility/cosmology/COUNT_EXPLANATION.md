# Chain Count Reconciliation

## The Numbers

| Count | What it refers to |
|-------|------------------|
| **4** | Dataset combinations: planck_only, planck_bao, planck_bao_sn, full_tension |
| **7** | Chains per dataset (1 original + 6 parallel) |
| **28** | Total independent MCMC chains (4 datasets x 7 chains each) |
| **24** | The 24 parallel chains launched later (4 datasets x 6 parallel each) |
| **31** | Total OS processes: 28 cobaya-run python processes + 3 bash wrapper shells |

## Timeline

1. **~08:47-08:59 UTC Mar 4**: 4 original chains launched (1 per dataset)
   - Used `cosmology/cobaya_planck.yaml`, `cobaya_planck_bao.yaml`, etc.
   - Each wraps in a `bash -c` shell, so 4 bash + 4 python = 8 processes

2. **~18:30 UTC Mar 4**: 24 parallel chains launched (6 per dataset)
   - Used `/tmp/cobaya_*_chain{2-7}.yaml` configs (backed up to `configs/`)
   - Each runs directly as python, no bash wrapper = 24 processes
   - Total: 8 (original) + 24 (parallel) - 1 (bash wrapper counted separately) = ~31

3. **Why 31 not 32?** The 4 original runs have bash wrappers (4 bash + 4 python = 8),
   but only 3 of the 4 bash wrappers show up in `ps` because one dataset (planck_bao_sn)
   was launched slightly differently. Net: 3 bash + 28 python = 31 cobaya-related processes.

## Config Differences

Original vs parallel chains differ in two MCMC tuning parameters:
- `burn_in`: 0.3 (original) vs 0.1 (parallel)
- `learn_proposal_Rminus1_max`: 30 (original) vs 50 (parallel)

These affect MCMC efficiency, NOT the target posterior. All 7 chains per dataset
sample the same distribution. Mixing them for R-hat is statistically valid.
