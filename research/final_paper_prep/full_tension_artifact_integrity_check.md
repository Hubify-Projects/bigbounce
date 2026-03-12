# full_tension Artifact Pack Integrity Check

**Date:** 2026-03-11 ~19:35 UTC
**Status:** ALL CHECKS PASS

---

## 1. SHA256 Checksum Verification

- **69/69 files** verified against `SHA256SUMS.txt`
- **0 failures**
- Snapshot tarball SHA256: `0225e4876b448dd2bc6516bcd094a409dd13148c8db7a83864957fe97a379bb6`

## 2. Chain File Readability

| Chain | Lines | Status |
|-------|-------|--------|
| chain_01 | 15,055 | Readable |
| chain_02 | 14,818 | Readable |
| chain_03 | 14,701 | Readable |
| chain_04 | 14,671 | Readable |
| chain_05 | 14,533 | Readable |
| chain_06 | 102,468 | Readable (drag oversampled) |
| **Total** | **176,246** | **All OK** |

Note: chain_06 has ~7x more lines due to Cobaya's drag sampler oversampling fast nuisance parameters.

## 3. Covariance Matrices

| File | Status |
|------|--------|
| full_tension.covmat | Present |
| planck_bao_sn.covmat | Present |
| planck_bao.covmat | Present |
| planck_only.covmat | Present |

All 4 warm-start covariance matrices readable.

## 4. Diagnostics

| File | Status |
|------|--------|
| convergence_summary.json | Present |
| freeze_diagnostics.json | Present (original, pre-bug-fix) |
| freeze_diagnostics_CORRECTED.json | Present (corrected column mapping) |
| parameter_summary.json | Present (original) |
| parameter_summary_CORRECTED.json | Present (corrected) |

## 5. Plots

| File | Status |
|------|--------|
| full_tension_triangle.png/pdf | Present (original) |
| full_tension_triangle_CORRECTED.png/pdf | Present (corrected mapping) |
| full_tension_posteriors.png/pdf | Present (original) |
| full_tension_posteriors_CORRECTED.png/pdf | Present (corrected mapping) |
| full_tension_chain_comparison.png | Present (original) |
| full_tension_chain_comparison_CORRECTED.png | Present (corrected mapping) |

Total: 10 plot files.

## 6. Plot–Chain Correspondence

The triangle plot (`paper/figures/full_tension_triangle.png`) was generated from the CORRECTED frozen chain data and shows:
- H0 = 67.7 ± 1.1 — matches frozen value 67.68 ± 1.06
- dNeff = -0.02 ± 0.17 — matches frozen value -0.020 ± 0.169
- tau = 0.054 ± 0.007 — matches frozen value 0.054 ± 0.007
- sigma8 = 0.803 ± 0.008 — matches
- Omega_m = 0.308 ± 0.006 — matches
- ns = 0.965 ± 0.006 — matches

The 1D posterior plot (`paper/figures/full_tension_posteriors.png`) is labeled "CORRECTED" and shows values consistent with the frozen parameter summary.

## 7. Supporting Files

| File | Status |
|------|--------|
| MANIFEST.md | Present |
| SHA256SUMS.txt | Present (69 entries) |
| configs/generate_configs.py | Present |
| configs/chain_seeds.json | Present |
| tables/parameter_summary.md | Present |

## Conclusion

**The frozen full_tension artifact pack is intact and verified.**
- 69/69 SHA256 checksums pass
- All chain files, covmats, diagnostics, plots, configs, and tables are readable
- Triangle and posterior plots correspond to the corrected frozen chain data
- No modifications detected since freeze at 2026-03-11 17:28 UTC
