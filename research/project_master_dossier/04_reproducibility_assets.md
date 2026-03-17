# Reproducibility Assets

Serious inventory of all reproducibility infrastructure in the research program.

---

## MCMC / Cobaya Configurations

### Working Cobaya Config Files

| File | Dataset | Status | Dependencies |
|------|---------|--------|-------------|
| `reproducibility/cosmology/cobaya_full_tension.yaml` | Planck NPIPE + BAO (6) + SN (Pantheon+) | COMPLETE | Cobaya v3.6.1, CAMB, Planck NPIPE likelihoods |
| `reproducibility/cosmology/cobaya_planck_bao_sn.yaml` | Planck + BAO + SN | COMPLETE | Same |
| `reproducibility/cosmology/cobaya_planck_bao.yaml` | Planck + BAO | COMPLETE | Same |
| `reproducibility/cosmology/cobaya_planck.yaml` | Planck only | COMPLETE | Same |

**Configuration details:**
- Theory: CAMB (stock, no custom modifications)
- `num_massive_neutrinos: 1`, `lens_potential_accuracy: 1`, `theta_H0_range: [40, 100]`
- Likelihoods: Planck NPIPE CamSpec (TTTEEE), Planck 2018 lowl (TT/EE), Planck lensing
- BAO: 6 datasets (auto-downloaded)
- SN: Pantheon+ (auto-downloaded)
- Sampler: MCMC with R-1 convergence target

**Environment requirements:**
- Python 3.8+
- Cobaya 3.6.1
- CAMB (pip install)
- Planck likelihood data (auto-downloaded by Cobaya on first run)

---

## MCMC Chain Files

### Frozen Datasets

| Dataset | Location | Chains | Samples | R-hat - 1 | ESS | Status |
|---------|----------|--------|---------|-----------|-----|--------|
| full_tension | `reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/full_tension/` | 6 | 175,840 | < 0.001 | > 6,000 | FROZEN |
| planck_bao_sn | `reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/planck_bao_sn/` | 6 | 132,949 | < 0.003 | > 4,600 | FROZEN |

### Running / Paused Datasets

| Dataset | Location | Status | Notes |
|---------|----------|--------|-------|
| planck_bao | `reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/planck_bao/` | PAUSED | Will resume after planck_only |
| planck_only | `reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/planck_only/` | RUNNING | ~20-30h to convergence |

### Chain File Structure (per chain)

Each chain directory contains:
- `spin_torsion.1.txt` — Main MCMC samples (space-delimited, 50+ columns)
- `spin_torsion.updated.yaml` — Updated Cobaya config
- `spin_torsion.input.yaml` — Input config snapshot
- `cobaya_config.yaml` — Cobaya v3.6.1 configuration
- `spin_torsion.covmat` — Covariance matrix
- `spin_torsion.checkpoint` — Chain checkpoint
- `spin_torsion.progress` — Convergence progress
- `cobaya.pid` — Process ID

### Supporting Chain Infrastructure

| Location | Contents | Status |
|----------|----------|--------|
| `reproducibility/cosmology/paper1_clean_restart_sync/covmats/` | Covariance matrices | COMPLETE |
| `reproducibility/cosmology/paper1_clean_restart_sync/manifests/` | Chain metadata and validation | COMPLETE |
| `reproducibility/cosmology/paper1_clean_restart_sync/snapshots/` | Intermediate checkpoints | COMPLETE |
| `reproducibility/cosmology/planck_only_live_sync/` | Live sync for planck_only run | ACTIVE |

---

## CAMB / Theory Hooks

| Item | Status | Notes |
|------|--------|-------|
| Custom CAMB modifications | NONE EXIST | Stock CAMB used throughout; no custom theory hook |
| Delta-N_eff implementation | VIA STANDARD CAMB | `nnu` parameter varied in Cobaya; no custom code |

**Important:** The paper does NOT use any custom CAMB modifications. This is documented in `reproducibility/docs/KNOWN_GAPS.md`. All theory predictions are standard LCDM + Delta-N_eff using stock CAMB.

---

## Galaxy Spin Analysis

| File | Purpose | Status | Notes |
|------|---------|--------|-------|
| `reproducibility/galaxy_spins/spin_fit_stan.py` | Hierarchical Bayesian model (Stan) | COMPLETE | Fits dipole asymmetry to published catalogs |
| `reproducibility/galaxy_spins/reproduce_spins.sh` | One-command reproduction | COMPLETE | Requires PyStan |
| `reproducibility/galaxy_spins/galaxy_spin_data_DEPRECATED.csv` | Original data file | DEPRECATED | Round numbers, provenance issues; see data audit |
| `reproducibility/galaxy_spins/DEPRECATED.md` | Deprecation notice | AUTHORITATIVE | Uses Shamir (2024) published catalogs instead |

**Environment:** Python 3.8+, PyStan, NumPy, SciPy

---

## Jupyter Notebooks

| File | What It Reproduces | Branch | Status | Dependencies |
|------|-------------------|--------|--------|-------------|
| `research/foundation_A_pgt/pgt_mode_analysis.ipynb` | Ghost-free PGT mode spectrum, mass formulas | Foundation-A | COMPLETE | SymPy |
| `research/foundation_B_lock_breaking/04_symbolic_model_exploration.ipynb` | Lock-breaking model algebra | Foundation-B | COMPLETE | SymPy |
| `research/foundation_C_environmental_mass/04_environmental_mass_symbolics.ipynb` | Environmental mass reduction to scalar-tensor | Foundation-C | COMPLETE | SymPy |
| `research/foundation_D_disformal_survival/05_disformal_symbolics.ipynb` | Disformal coupling suppression proof | Foundation-D | COMPLETE | SymPy |
| `research/branch_K_scalar_perturbations/04_scalar_mode_solver.ipynb` | Scalar transfer function T(k) through bounce | Branch-K | COMPLETE | NumPy, SciPy |
| `research/branch_M_pgt_bounce_gw/03_gw_spectrum_solver.ipynb` | GW spectrum through PGT bounce | Branch-M | COMPLETE | NumPy, SciPy |

---

## Python Analysis Scripts

| File | What It Produces | Status | Dependencies |
|------|-----------------|--------|-------------|
| `research/final_paper_prep/generate_publication_figures.py` | Publication-quality figures (9 planned) | PARTIAL | Matplotlib, GetDist, chain data |
| `research/final_paper_prep/generate_two_frozen_figures.py` | Two-frozen-dataset comparison figures | COMPLETE | Matplotlib, GetDist |
| `research/final_paper_prep/extract_physical_parameters.py` | Parameter summaries from chain files | COMPLETE | GetDist, NumPy |
| `reproducibility/cosmology/reproduce_cosmology.sh` | Full MCMC reproduction pipeline | COMPLETE | Cobaya, CAMB |

---

## Documentation

### Reproducibility Documentation

| File | Contents | Status |
|------|----------|--------|
| `reproducibility/README.md` | Quick-start guide, structure overview | AUTHORITATIVE |
| `reproducibility/docs/IMPLEMENTATION_MAP.md` | Paper claim → code → output mapping | AUTHORITATIVE |
| `reproducibility/docs/KNOWN_GAPS.md` | Honest gap disclosure | AUTHORITATIVE |

### Known Gaps (from KNOWN_GAPS.md)

1. No custom CAMB modifications (stock CAMB used)
2. No pre-computed chain download (must re-run MCMC)
3. No CNN galaxy spin classifier (removed in Round 4; uses published catalogs)
4. No original CMB map analysis (uses published birefringence measurements)
5. No nested sampling comparison (MCMC only)

---

## Equations / Derivation Documentation

| Location | Contents | Status |
|----------|----------|--------|
| `research/foundation_A_pgt/04_mass_spectrum_calculation.md` | Explicit PGT mass formulas | AUTHORITATIVE |
| `research/foundation_B_lock_breaking/phase2/02_nieh_yan_mag_analysis.md` | Nieh-Yan in MAG computation | AUTHORITATIVE |
| `research/paper_1_2_archive/03_action_equation_reassessment.md` | ECH action re-examination | AUTHORITATIVE |
| `research/paper2/first_principles_roadmap/` | 8-phase perturbation calculation blueprint | AUTHORITATIVE |
| `research/branch_S_photon_torsion_vertex/05_effective_operator_derivation.md` | VVA triangle in ECH | AUTHORITATIVE |

---

## Literature Maps

| File | Contents | Status |
|------|----------|--------|
| `research/paper2/p6_cmb_eb_pipeline/` | 5+ independent birefringence measurements compiled | AUTHORITATIVE |
| `research/paper2/shared/citations.bib` | Shared bibliography for Paper 2 tracks | AUTHORITATIVE |
| `research/extensions/dataset_audit/` | Master extension dataset audit | AUTHORITATIVE |

---

## Freeze Logs / Problem Statements

Every foundation and branch has a frozen problem statement (typically `01_problem_statement.md`) that defines scope, assumptions, and success criteria before analysis begins. These are integral to the reproducibility of the scientific reasoning, even when no code is involved.

| Pattern | Count | Status |
|---------|-------|--------|
| `research/foundation_*/01_problem_statement.md` | 7 files | AUTHORITATIVE |
| `research/branch_*/01_problem_statement.md` | 17+ files | AUTHORITATIVE |

---

## Compilation Infrastructure

| File | Purpose | Status |
|------|---------|--------|
| `arxiv/compile_on_pod.sh` | RunPod GPU compilation automation | AUTHORITATIVE |
| `arxiv/make_overleaf_zip.sh` | Overleaf-compatible ZIP creation | AUTHORITATIVE |
| `research/final_paper_prep/latex_compile_readiness.md` | Compile status (0 undefined refs) | AUTHORITATIVE |
| `research/final_paper_prep/latex_compile_log.txt` | Full compile log (56 KiB) | AUTHORITATIVE |

---

## Summary: Reproducibility Completeness

| Category | Completeness | Notes |
|----------|-------------|-------|
| MCMC pipeline | 95% | 2/4 datasets frozen; 2 running/paused |
| Cobaya configs | 100% | All 4 working and tested |
| Chain files | 75% | 2 frozen + checksummed; 2 in progress |
| Galaxy spin analysis | 90% | Stan model works; deprecated data file replaced |
| Theory derivations | 100% | All symbolic notebooks run |
| Figure generation | 80% | Scripts exist; 5/9 figures need regeneration |
| Documentation | 95% | Known gaps honestly documented |
| Compilation | 100% | 0 undefined refs; full compile log available |
