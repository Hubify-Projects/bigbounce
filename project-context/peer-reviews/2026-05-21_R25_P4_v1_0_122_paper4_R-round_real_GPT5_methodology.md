# paper4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R25_P4_v1_0_122
**Wall time**: 150.7s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=94781, completion=7810, reasoning=6690, total=102591

---

## PAPER-GPT-B1 — BLOCKER — Same-data real-space dipole estimators disagree by ~10×

**Section:** §Methods/Pre-Registered Analysis Hierarchy; §Dipole Analysis; §Edge-On Galaxy Contamination, Table “High-confidence-spiral robustness rerun”  
**Issue:** The headline real-space Catalog C dipole is quoted as `+0.43σ, p=0.30`, but the same “Catalog C full” data later gives `+4.31σ, p=0.001` under a weighted LSQ cosθ fit. “Different estimator/null-sample variance” is not a valid reconciliation for a load-bearing null; this implies at least one estimator/null is miscalibrated or measuring a different data vector.  
**Fix:** Define one primary real-space estimand with fixed mask, weights, monopole subtraction, and null covariance; reproduce both numbers side-by-side and show via injections which estimator is calibrated, or remove the `+0.43σ` result from load-bearing status.

## PAPER-GPT-M1 — MAJOR — Canonical `+3.64σ` is over-stated relative to its empirical p-value

**Section:** Abstract; §Dipole Analysis; §Conclusions “Canonical-N MASTER ℓ=1 direct compute”  
**Issue:** The canonical-mask residual is repeatedly presented as `+3.64σ`, but the paper also gives empirical-rank `p_MC = 15/500 = 0.030`, i.e. not a Gaussian 3.64σ tail. Calling this a `3.64σ` significance in the abstract overclaims the calibrated evidence.  
**Fix:** Report everywhere as `moment-z = +3.64; empirical p = 0.030 (~2.2σ two-sided equivalent)` unless Gaussian tail behavior of the MC null is demonstrated.

## PAPER-GPT-M2 — MAJOR — Post-MASTER monopole-only null status contradicts itself

**Section:** Table 1 footnote b; §Monopole+Mask Leakage Generative Null; §Conclusions first paragraph  
**Issue:** The conclusions say “post-MASTER monopole-only realizations were not computed,” but earlier text says the MASTER-decoupled monopole-only null ×500 was computed and gives data `C1=6.55e-6`, null mean `8.0e-7`, accounting for 12%. Also `p=2/500=0.006` is arithmetically wrong (`2/500=0.004`; add-one `3/501≈0.006`).  
**Fix:** Update the conclusion to the computed v1.0.121 result and state one consistent empirical-rank convention with correct arithmetic.

## PAPER-GPT-M3 — MAJOR — Shamir 2022 sample-size comparator is internally wrong

**Section:** Introduction; §Comparison with Previous Work; Conclusions item 2  
**Issue:** The manuscript correctly says Shamir 2022 used ~1.3M total/Ganalyzer-analyzed galaxies and only ~200k retained spirals, but then claims the present 3.2M spirals are `~2.5×` larger than Shamir’s spiral subsample and later calls Shamir’s abstract “nearly 1.3×10^6 spirals.” Arithmetic: `3.2M/200k≈16`, while `3.2M/1.3M≈2.5` only vs total input, not spirals.  
**Fix:** Use two separate ratios: `~2.5×` versus Shamir’s total input pool, or `~16×` versus the retained spiral subsample, with the latter only if the ~200k retained-spiral number is sourced.

## PAPER-GPT-M4 — MAJOR — Dipole sensitivity amplitude convention remains inconsistent

**Section:** §Sensitivity Floor and Minimum Detectable Signal; Conclusions item 1; Falsification criterion  
**Issue:** The section discloses that the derivation is for half-modulation `A/2`, but later still calls `0.14%→0.2%` the “minimum detectable amplitude,” while the full-amplitude Fisher 3σ floor is `~0.29%` or conservative `~0.4%`; the abstract/falsification then uses `0.75%`. This leaves three incompatible “floors” without a single propagated convention.  
**Fix:** Rewrite using full-amplitude `A` throughout; define `h=A/2` only inside the derivation, then present one table with Fisher full-amplitude, conservative full-amplitude, HC empirical threshold, and LSST-scaled projection.

## PAPER-GPT-m1 — minor — “Independent” GZ1 validation denominator includes excluded training objects

**Section:** §Training Labels, “Independent GZ1 cross-match and joint label tabulation”  
**Issue:** The text says the 6,637 GZ1 training objects are excluded and metrics are reported on 234,282 external matches, but the quoted three-class accuracy is `141,438 / 240,919 = 58.71%`, using the pre-exclusion denominator. That contradicts the claimed disjoint validation set.  
**Fix:** Recompute all GZ1 accuracy/confusion/κ metrics after the set-difference exclusion, or explicitly label which metrics include the training overlap.
