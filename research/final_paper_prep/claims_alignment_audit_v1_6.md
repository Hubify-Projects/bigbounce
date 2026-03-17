# Claims Alignment Audit: v1.6.0

**Date:** 2026-03-13
**Auditor:** Claude (automated)

---

## Audit Results

### 1. ΔN_eff Language
**PASS.** All 6 occurrences correctly state "consistent with zero within 1σ." No overclaiming.

### 2. Track C (Birefringence Consistency Check) Language
**PASS.** New subsection (Sec. 10.X) uses:
- "consistency check" — correct
- "does not constitute independent evidence" — correct
- "algebraic parameter translation of published measurements, not new statistical inference" — correct
- "compatible with" — correct
- "requires f_photon ≈ 1.7" — correct (not "measures")
- Figure caption explicitly states "phenomenological consistency check, not a statistical inference"

### 3. Early-Structure / SMBH / PBH Language
**PASS.** Only occurrence is the new future-work bullet point in Sec. 11.4, which:
- States the feature scale correctly (k ~ 10^15 Mpc^-1)
- Names the mass scale (M ~ 10^-16 M_☉, sub-asteroid)
- Says "remains an open question requiring a full perturbation calculation"
- Does NOT mention SMBH seeds, JWST, or early structure formation
- Does NOT claim the framework predicts PBH dark matter

### 4. Birefringence Signal Attribution
**PASS.** All birefringence detections properly attributed to:
- Minami & Komatsu (2020): Planck 2.4σ
- Eskilt (2022): Planck 2.7σ
- Diego-Palazuelos & Komatsu (2025): ACT DR6 2.9σ
- SPIDER (2025): 7σ total rotation (with calibration caveat)

The combined 3.9σ in the new subsection is properly described as inverse-variance weighting of published values, not as our own analysis.

### 5. "Predicts" vs "Is Consistent With"
**PASS.** The manuscript correctly uses:
- "qualitatively consistent with cosmic birefringence" (not "predicts")
- "without this coupling, the framework strictly predicts β = 0" (honest)
- "consistency benchmark, not a prediction" (Sec. 8.1)
- "compatibility without fine-tuning" (new conclusions paragraph)

### 6. Claims Classification Table
**PASS.** New row added:
- f_photon ≈ 1.7 classified as "Consistency check" with note "Algebraic translation of published β"
- This is the correct classification per the method audit

### 7. Galaxy Spin Language
**PASS.** All galaxy spin claims remain properly hedged:
- "contested anomaly" in section title
- "conditional on the reality of the signal" in table caption
- Null results from Patel & Desmond and Philcox & Ereza cited prominently

### 8. Fine-Tuning Claims
**PASS.** Residual 10^5 fine-tuning from N_tot correctly described as "reparameterizes" not "solves."

---

## Summary

| Check | Status |
|-------|--------|
| ΔN_eff language | PASS |
| Track C framing | PASS |
| Early-structure scope | PASS |
| Birefringence attribution | PASS |
| Prediction vs consistency | PASS |
| Claims table | PASS |
| Galaxy spin hedging | PASS |
| Fine-tuning honesty | PASS |

**Overall: ALL CHECKS PASS. No overclaiming detected in v1.6.0.**
