# Baseline Snapshot

**Frozen:** 2026-03-23
**Git commit:** 4ed5569 (fix: final consistency pass)
**Purpose:** Preserve the current state before deeper validation.

---

## Frozen Claim Values

| Claim | Value | Grade | File |
|-------|-------|-------|------|
| f_NL canonical | -35/8 = -4.375 | B (90%) | normalization_audit.md |
| Template mismatch r | 0.84 ± 0.02 | A- | template_overlap_robustness.md |
| SPHEREx significance | ~5.5σ (template-corrected) | C+ | Paper 2 abstract |
| MegaMapper significance | ~7.5σ | C+ | Paper 2 Sec 5 |
| ε correction | +0.026 (0.6%) | C | compute_all.py |
| Consistency relation | f_NL(n_s) = -4.375 - 0.73(n_s-1) | C | Paper 2 Sec 8 |
| Bayes factor | ~8-17:1 vs tuned multifield | B | Paper 2 Sec 6 |

## Known Anomaly

**fnl_combined_integrand** yielded f_NL = +25/16 from an independent mpmath evaluation.
Three errors identified (cubic action coefficient, mode function phase, χ definition).
Errors attributed to using conformal-time Maldacena reconstruction instead of Cai's cosmic-time formulation.
**Correction has NOT been implemented and re-run.**

## File Manifest

All files in `research/matter_bounce_parameters/` as of this snapshot:
- `bayes_and_forecasts.py` (19K)
- `compute_all.py` (23K)
- `generate_figures.py` (10K)
- `normalization_audit.md` (18K)
- `planck_convention_check.py` (8.2K)
- `template_overlap_robustness.md` (6.6K)
- `template_overlap_robustness.py` (16K)
- `verify_vertex_match.py` (5.2K)
- `current_claim_inventory.md` (this session)
- `validation_master_plan.md` (this session)
- `baseline_snapshot.md` (this file)

## Restoration Command

```bash
git checkout 4ed5569 -- research/matter_bounce_parameters/
```
