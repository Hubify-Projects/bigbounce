# Extension Program Final Report

**Date:** 2026-03-13
**Paper:** Geometric Dark Energy from Spin-Torsion Cosmology (v1.5.0)

---

## 1. Which tracks are actually viable?

| Track | Viable? | Why |
|-------|---------|-----|
| A — SMBH Seeds | **NO** | Zero direct framework connection. Torsion effects vanish at astrophysical densities (suppressed by 10^{-83}). |
| B — PBH Relics | **NO** | No production mechanism exists. The bounce creates baby universes inside BHs, not PBHs in our universe. |
| C — Parity/CMB | **YES** | Direct equation chain from α/M → parity-odd operator → birefringence. Published data at 3.9σ combined significance. |

## 2. Datasets used

### Track C (the only viable track):
| Dataset | Source | β (deg) | σ_β (deg) | Used? |
|---------|--------|---------|-----------|-------|
| Eskilt 2022 | Planck (arXiv: 2205.13962) | 0.300 | 0.110 | YES |
| Diego-Palazuelos & Komatsu 2025 | ACT DR6 (arXiv: 2509.13654) | 0.215 | 0.074 | YES |
| Minami & Komatsu 2020 | Planck (arXiv: 2011.11254) | 0.350 | 0.140 | NO (superseded by Eskilt) |
| SPIDER 2025 | SPIDER+Planck+ACT | 0.500 | 0.070 | NO (calibration degeneracy) |

**Combined constraint:** β = 0.242° ± 0.061° (3.9σ)

## 3. MCMC vs forward-model decision

| Track | Decision | Rationale |
|-------|----------|-----------|
| A | FUTURE WORK ONLY | No model-to-observable map exists |
| B | FUTURE WORK ONLY | No production mechanism |
| C | **CONSTRAINT ANALYSIS** (Gaussian sampling + forward model) | Published β ± σ_β → Gaussian posterior on g_eff and f_photon. No full MCMC needed or justified. |

## 4. Infrastructure

**No new pods were launched.** Track C runs entirely on the local Mac in <1 minute. The existing Paper-1 RunPod pod (planck_only chains running) was not modified.

## 5. Key results from Track C

### Consistency window:
The framework's parity-odd coupling α/M ≈ 10^{-21} GeV^{-1} (giving dimensionless suppression [(α/M)·M_Pl] ≈ 10^{-2}) requires a photon-torsion vertex factor:

**f_photon = 1.73 ± 0.44**

This is O(1) — no fine-tuning needed. The spin-torsion scale is naturally consistent with observed cosmic birefringence.

### Combined birefringence posterior:
β = 0.242° ± 0.061° (3.9σ from two independent experiments)

### EB shape consistency:
The predicted C_ℓ^{EB} = 2β(C_ℓ^{EE} − C_ℓ^{BB}) shape is consistent with uniform (isotropic) birefringence across all ℓ, as expected from the framework's isotropic component.

## 6. Paper integration recommendation

**Include Track C in the current paper** as a ~2-3 paragraph addition to the Discussion section, with 1-2 new figures. This materially strengthens the paper by:

1. Providing a second independent observable constraint (beyond the weak ΔN_eff ≈ 0 result)
2. Showing quantitatively that the framework's coupling scale requires only O(1) photon-torsion vertex
3. Replacing the current "qualitatively consistent" language with a concrete numerical consistency check
4. Identifying f_photon ≈ 1.7 as a specific theoretical target

**Timing:** Integrate with the planck_only results update (~March 19-20), before the referee-style review.

---

## Deliverable Index

| File | Description |
|------|-------------|
| `observable_program_overview.md` | Global strategy memo (Phase 0) |
| `track_A_smBH/model_to_observable_map.md` | Track A model map — REJECTED |
| `track_B_pbh/model_to_observable_map.md` | Track B model map — REJECTED |
| `track_C_parity_cmb/model_to_observable_map.md` | Track C model map — APPROVED |
| `track_C_parity_cmb/README.md` | Implementation documentation |
| `track_C_parity_cmb/scripts/consistency_window.py` | Consistency window analysis |
| `track_C_parity_cmb/scripts/gaussian_posterior.py` | Gaussian posterior sampling |
| `track_C_parity_cmb/scripts/eb_shape_comparison.py` | EB spectrum forward model |
| `track_C_parity_cmb/outputs/*.pdf` | 6 publication-quality figures |
| `track_C_parity_cmb/outputs/*_summary.txt` | Numerical results |
| `dataset_audit/master_extension_dataset_audit.md` | Full dataset audit |
| `dataset_audit/master_extension_dataset_registry.csv` | Structured dataset registry |
| `track_readiness_decision.md` | Phase 3 decisions |
| `infrastructure_plan.md` | Infrastructure assessment |
| `infrastructure_budget.csv` | Cost breakdown |
| `current_paper_integration_decision.md` | Phase 7 integration plan |
