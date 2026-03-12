# BigBounce Dataset Provenance Report

Generated: 2026-03-06
Auditor: Automated + manual review

## Summary

| Status | Count | Description |
|--------|-------|-------------|
| raw_public | 4 | Real observational/survey data from public archives |
| derived_public | 5 | Computed from theory code, fully reproducible |
| reconstructed | 3 | Manually extracted from published papers (not machine-readable) |
| internal_summary | 19 | Small summary tables, model comparisons, forecasts, diagnostics |
| **Total** | **31** | |

## Honesty Assessment

The project has a **mixed provenance picture**. The MCMC infrastructure (Paper 1 cosmological constraints) uses well-established public likelihoods (Planck, BAO, SN) through Cobaya, which is excellent. The theoretical model predictions and parameter scans are fully reproducible from code. However, the galaxy spin data track has significant provenance weaknesses.

---

## Per-Dataset Provenance

### 1. galaxy_spin_data.csv (CRITICAL — WEAK)
- **Path**: `reproducibility/galaxy_spins/galaxy_spin_data.csv`
- **What it is**: 17 rows of binned CW/CCW galaxy counts across 3 "surveys" (SDSS, HST, JWST)
- **What it claims to be**: Published CW/CCW counts per redshift bin from Shamir (2012, 2022)
- **Actual provenance**: **UNKNOWN**. The file contains round numbers (25420/24580, 18960/18240) that do not appear in any specific published table. The "JWST" entries (rows 17-18 with z=2.0, 2.5) are especially problematic — Shamir's JWST JADES paper (arXiv:2401.09450) reports 195 total classified spirals, not the 600/400 implied by these bins.
- **Can a third party reproduce it?**: NO. There is no documented extraction procedure, no table reference, no code that generates these values from a published source.
- **Verdict**: This file appears to be a **manually constructed illustrative example**, not a faithful extraction from published data. It should be clearly labeled as such or replaced.

### 2. galaxy_spin_counts.csv (Paper 2 WP5 — HONEST)
- **Path**: `research/paper2/wp5_spin_amplitude/data/galaxy_spin_counts.csv`
- **What it is**: 5 rows of survey-level aggregate CW/CCW counts
- **Provenance**: Clearly documented header states "Reconstructed from Published Tables" in Shamir (2024), with specific table references per row
- **Can a third party reproduce it?**: YES, by reading the cited paper's Tables 1-3 and Section 2
- **Verdict**: Honest and well-documented. The counts match what Shamir (2024) reports. This is the right way to handle reconstructed data.

### 3. Planck 2018 Parameters (raw_public — STRONG)
- **What it is**: Reference cosmological parameter values from Planck 2018 results
- **Source**: https://arxiv.org/abs/1807.06209 (Table 2)
- **Provenance**: Published, peer-reviewed, widely cited
- **Can reproduce?**: YES — values are in the published paper
- **Verdict**: Excellent provenance. Standard reference dataset.

### 4. Planck PR4/NPIPE Maps (raw_public — STRONG)
- **What it is**: Reprocessed CMB frequency maps
- **Source**: Planck Legacy Archive (https://pla.esac.esa.int/)
- **Provenance**: Official ESA data release, versioned
- **Local mirror**: On RunPod pod only (~13 GB), not in repo
- **Can reproduce?**: YES — download from PLA with documented filenames
- **Verdict**: Excellent provenance. Download commands documented in dataset_registry.csv.

### 5. Galaxy Zoo DECaLS Labels (raw_public — STRONG)
- **What it is**: ~314k galaxy morphology classifications from volunteers
- **Source**: https://zenodo.org/records/4573248
- **License**: CC-BY-4.0
- **Local mirror**: On RunPod pod only
- **Can reproduce?**: YES — Zenodo DOI is permanent
- **Verdict**: Excellent provenance. Real object-level data.

### 6. Birefringence measurements (raw_public — STRONG)
Multiple published β values:
- Minami & Komatsu (2020): β = 0.35° ± 0.14° — arXiv:2011.11254
- Eskilt PR4 (2022): β = 0.30° ± 0.11° — arXiv:2205.13962
- ACT DR6 (2025): β = 0.215° ± 0.074° — arXiv:2509.13654
- SPIDER combined (2025): 7σ detection — arXiv:2510.25489

All are literature values from published papers. Reproducible by reading the cited papers.

### 7. BBN Constraints (raw_public — STRONG)
- **Source**: Burns+(2024), arXiv:2401.15054
- **What it is**: ΔNeff = -0.10 ± 0.21 from light element abundances
- **Verdict**: Published, peer-reviewed. Standard reference.

### 8. WP4 Parameter Scans (derived_public — STRONG)
- **Reheating scan**: 24,000 rows, fully computed from theoretical model
- **Decay scan**: 32,000 rows, same
- **Code**: `research/paper2/wp4_dneff_microphysics/`
- **Can reproduce?**: YES — run the Python scripts
- **Verdict**: Fully reproducible derived data. Code + inputs available.

### 9. WP5 Monte Carlo Samples (derived_public — STRONG)
- **What it is**: 100,000 MC sensitivity samples
- **Code**: `research/paper2/wp5_spin_amplitude/monte_carlo_sensitivity.py`
- **Can reproduce?**: YES — run the script with galaxy_spin_counts.csv as input
- **Verdict**: Fully reproducible. Input data provenance (galaxy_spin_counts.csv) is documented.

### 10. P7 CNN Catalog (internal_summary — SYNTHETIC)
- **What it is**: 2,000 rows with `syn_cw_` prefixed object IDs
- **Provenance**: Synthetically generated for pipeline testing
- **Can reproduce?**: YES — but it's test data, not real observations
- **Verdict**: Clearly synthetic. The P7 track assessment was FAIL (test_acc=0.49, effectively random on synthetic data). This is appropriate for a pipeline test.

### 11. Theory Curves (internal_summary)
- `cls_EE_theory_example.csv` — CAMB output, reproducible
- `instrument_cmbs4_example.csv` — CMB-S4 noise specs, from published expectations
- Figure panel CSVs — Small summary tables (3-5 rows each) containing model comparison values and forecasts

All are either standard cosmological computations or model predictions. Reproducible from theory code.

### 12. MCMC Chain Outputs (derived_public — IN PROGRESS)
- **What it is**: Cobaya MCMC posterior chains for 4 datasets × 7 chains
- **Status**: Still running on GPU + CPU pods
- **Provenance**: Generated by Cobaya using public Planck/BAO/SN likelihoods
- **Can reproduce?**: YES — Cobaya YAML configs are in the repo
- **Verdict**: Will be strong provenance once converged and frozen. Currently internal-only.

### 13. Spreadsheets (internal_summary)
- 7 Excel files in `public/spreadsheets/` corresponding to paper figures
- Contain the same data as the CSV panel files, formatted for web visualization
- All are either model predictions, published comparison values, or forecasts

---

## Key Findings

### STRONG
- Paper 1 MCMC: Uses standard public likelihoods (Planck, BAO, SN) via Cobaya. Excellent.
- Birefringence data: All from published, peer-reviewed papers. Well-cited.
- Paper 2 parameter scans: Fully reproducible from code.
- Paper 2 WP5 galaxy_spin_counts.csv: Honestly documented as reconstructed from published tables.

### WEAK
- `galaxy_spin_data.csv`: The foundational galaxy spin dataset for Paper 1 is a **17-row binned summary with unclear provenance**. The values do not trace to any specific published table. The "JWST" bins contain counts inconsistent with the cited paper. This is the single biggest reproducibility weakness in the project.

### MISSING
- No local mirror of Planck PR4 maps (on RunPod only)
- No local mirror of Galaxy Zoo DECaLS labels (on RunPod only)
- No object-level galaxy spin catalog anywhere in the repo
