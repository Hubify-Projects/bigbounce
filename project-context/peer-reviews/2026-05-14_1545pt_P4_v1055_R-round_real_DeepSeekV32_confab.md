# P4_v1055 R-round — REAL cross-vendor — DeepSeek-V3.2 confabulation-hunter

**Model**: `deepseek/deepseek-v3.2` (via OpenRouter)
**Round**: 2026-05-14_1545pt
**Wall time**: 52.0s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=52692, completion=1596, total=54288

---

# Adversarial Peer Review: Confabulation-Hunter Report

**Paper:** "A Survey-Scale Chirality Catalog of 8.47 Million Galaxies (3.2 Million Spirals): A Null Detection of Large-Scale Parity Violation in Galaxy Morphology at Sub-Percent Sensitivity"
**Version:** v1.0.55
**Reviewer:** DeepSeek-V3.2 Confabulation-Hunter
**Date:** 2026-05-14

## Executive Summary
Found **2 BLOCKERs**, **2 MAJORs**, and **2 minor** issues. The paper's central null result is credible, but several headline figures lack direct, on-disk provenance from the canonical production catalog. The most severe issues involve the primary sensitivity floor and the post-MASTER canonical result.

---

## PAPER-DEE-B1: BLOCKER – Primary Sensitivity Floor Lacks Provenance
**Location:** Abstract, Sec. 1, Sec. 5 (Conclusions), Sec. VI.J (Sensitivity)
**Issue:** The paper's "primary sensitivity figure" – the empirical injection-recovery sensitivity floor of |A_dipole| ≳ 0.5% – is stated as load-bearing but is not traceable to a JSON/script artifact that produces this exact number from the canonical catalog. The abstract states this is the "primary sensitivity figure for this paper" and the "operational publication-grade limit." However, the cited injection-recovery test (`wave_14_nn_injection_recovery.json`) shows that at A=0.5%, the detection probability P(σ>2) is only 0.18, not 0.5. The 50%-recovery threshold is not demonstrated; the claim "≳0.5%" appears to be an interpretation, not a number directly output by a reproducibility script.
**Fix:** Provide a script `compute_empirical_sensitivity_floor.py` that loads the canonical catalog and the MC injection results, performs a fit to find the 50%-recovery amplitude, and emits `empirical_sensitivity_floor.json` with the exact amplitude and its uncertainty. Update text to reflect the measured threshold, not an interpreted bound.

## PAPER-DEE-B2: BLOCKER – Canonical Post-MASTER ℓ=1 Result is a Projection, Not a Direct Measurement
**Location:** Abstract, Sec. V.B (Dipole Analysis), Sec. 5 (Conclusions)
**Issue:** The canonical post-MASTER ℓ=1 significance of -0.122σ is **not** a direct measurement on the canonical spiral sample (N_spiral=3,201,160, f_sky=0.491). It is an analytic projection from a different analysis subsample (n=5,547,858, f_sky=0.659) using approximations declared in `canonical_n_master_l1_projection.json`. The paper presents this as the "canonical primary" result but it is a derived estimate, not a reproducible output of the NaMaster pipeline on the canonical data. This violates the principle of traceability for load-bearing scalars.
**Fix:** Run the full NaMaster pipeline on the exact canonical Catalog C spiral sample (N=3,201,160) to produce a direct measurement. Deposit the result as `canonical_master_l1_result.json`. Until this is done, clearly label the -0.122σ figure as a "projected estimate" in the abstract and conclusions, not the canonical primary.

## PAPER-DEE-M1: MAJOR – "0.2% Statistical Floor" Calculation Omitted Factor of 2
**Location:** Abstract, Sec. VI.J (Sensitivity), Sec. 5 (Conclusions deferral paragraph)
**Issue:** The abstract and sensitivity section quote a "Fisher-floor statistical Poisson asymptote" of |A_dipole| ≲ 0.2%. The derivation in Sec. VI.J yields σ(A_dip) ≈ 0.048%, leading to a 3σ floor of ~0.14%, rounded to 0.2%. However, the deferral paragraph in Sec. 5 notes a correction: the formula σ(A_dip) = 0.048% is the uncertainty on A/2, making the true 3σ floor ~0.29%. The abstract and main text have not been updated to reflect this corrected factor-of-2 accounting, presenting an inconsistently defined and potentially misleading sensitivity figure.
**Fix:** Update all instances of the statistical floor (abstract, Sec. VI.J, conclusions) to the corrected value (~0.29% at 3σ) with a clear note on the amplitude convention p_CW(𝑛̂) = ½(1 + A cosθ). Ensure the empirical floor (0.5%) remains the primary, conservative figure.

## PAPER-DEE-M2: MAJOR – Shamir (2022) Citation is Unverified/Incorrect
**Location:** Bibliography, citations to Shamir:2022
**Issue:** The bibliography entry for Shamir (2022) points to PASJ 74, 1114 (2022) but lacks a verified arXiv identifier. The note states the prior arXiv ID (2207.11885) pointed to an unrelated optimization paper and was removed. The journal reference is retained but its correctness is pending verification. A key comparison in the paper (factor of 6–12 disfavoring Shamir's signal) relies on this citation being accurate and accessible.
**Fix:** Verify the correct publication details for Shamir (2022). Provide a correct arXiv link or confirm the journal reference (PASJ 74, 1114). If the source cannot be verified, soften the comparative claims or remove the citation until verified.

## PAPER-DEE-m1: minor – "9.5σ" Monopole Significance Uses Rounded σ
**Location:** Abstract, Sec. IV.A (Global CW Fraction)
**Issue:** The global CW fraction deviation is quoted as 9.5σ. The exact calculation (0.5000 - 0.49735)/0.000279 = 9.47σ. The rounding to 9.5σ is acceptable, but the paper should state the exact value and the rounding convention for transparency, as this is a headline figure.
**Fix:** In the abstract and Sec. IV.A, state the exact significance (9.47σ) and note the rounded value (9.5σ) for readability.

## PAPER-DEE-m2: minor – Table III Footnote Ambiguity on "Single mode"
**Location:** Table III (Multipole results), footnote a
**Issue:** Footnote a describes the ℓ=1 row as a "single-mode" result. However, the description references a companion artifact (`master_power_spectrum.json`) from an analysis with n=5,547,858, f_sky=0.659, which is not the canonical sample. This creates confusion about what dataset the "single-mode" result actually corresponds to.
**Fix:** Clarify in the footnote that the "single-mode" result is from the analysis subsample, not the canonical N_spiral sample. Add a cross-reference to the projection script (`canonical_n_master_l1_projection.py`) for the canonical estimate.

---
**Reviewer's Final Note:** The core null result is robust and the catalog construction is impressive. The BLOCKERs are procedural, not substantive—they demand that the paper's most important numbers be directly reproducible from the released data and scripts, which is a requirement for a publication-grade result. The fixes are straightforward but essential for verification.
