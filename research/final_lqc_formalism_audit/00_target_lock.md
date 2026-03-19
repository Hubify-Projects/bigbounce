# Final LQC Formalism Audit: Target Lock

**Created:** 2026-03-19
**Status:** ACTIVE
**Classification:** LAST BOUNDED THEORY OPENING

---

## Context

- **Live model:** Wilson-Ewing LCDM quasi-dust matter bounce in LQC
- **Live observables:** f_NL = -35/8 (squeezed, local-type), n_s = 0.964, r ~ 10^{-4}
- **Live forecasts:** SPHEREx 4-6 sigma, MegaMapper 3-7 sigma
- **Everything else:** closed or killed

This is the last bounded theory opening for the current model class. Every other path has been definitively closed:

| Path | Kill Mechanism | Reference |
|------|---------------|-----------|
| ECH perturbations | Mathematical proof: zero torsion for scalar matter, 14+ barriers | `ech_bispectrum_gate/final_verdict.md` |
| PBH + induced GW | Frequency gate: enhancement at ~10^{11}-10^{12} Hz, T = 1 + O(10^{-30}) at PBH scales | `open_paths_sync_and_continue/05_first_step_execution.md` |
| Chiral GW from ECH | Frequency gate: f ~ 10^{9-10} GHz, 5 independent closures | `project_chiral_bounce_GW/` |
| Bounce-to-DE connection | 7 foundations closed, 7 hybrid splice forms rejected | `foundation_A-G/`, `next_flagship_program/` |
| Galaxy spin dipole | 9-12 OOM coupling gap | `branch_V_bounce_evidence/` |
| Scale-dependent f_NL | LQC correction: 10^{-112}, contraction running: 0.14 sigma | `lqc_specific_openings_audit/03_second_observable_channel_audit.md` |
| Tension reduction | Own MCMC disproved: Delta-N_eff = 0 | MCMC infrastructure |
| Gradient expansion | SUPPORTING_ONLY, not frontier | `gradient_expansion_fnl_derivation/` |

---

## What This Audit Tests

Whether the choice of LQC perturbation formalism (dressed-metric vs hybrid vs deformed algebra) changes ANY of the live observables enough to matter.

The earlier LQC openings audit (`lqc_specific_openings_audit/01_quantization_ambiguity_formalism_audit.md`) estimated a ~15% probability of a non-null result. This audit applies the full scale-hierarchy argument to determine whether that estimate was realistic.

---

## What Counts As:

### Materially different
Formalism changes f_NL by >10% (i.e., |Delta f_NL| > 0.4), OR changes sign, OR changes shape from local to non-local. This would mean the choice of quantum gravity formalism is empirically testable -- a major result.

### Negligible / confirmation
Formalism changes f_NL by <10%, same sign, same shape, same scale-dependence. This confirms that f_NL = -35/8 is a generic matter-bounce result, not an LQC-specific one. Useful for robustness but not a new discovery.

### Genuinely LQC-specific discriminator
An observable that DIFFERS between formalisms AND is detectable by a planned experiment. This would mean the choice of quantum gravity formalism is empirically testable. Would be the strongest possible outcome.

### Final closure
All formalisms agree at observable scales. No LQC-specific content beyond generic bounce. Theory frontier closes.

---

## Scope Boundary

This audit is STRUCTURAL, not computational. The question can be resolved by dimensional analysis and the scale hierarchy k_obs/k_LQC ~ 10^{-56}, without needing to perform any new calculation. If the structural argument closes the question, no computation is warranted.
