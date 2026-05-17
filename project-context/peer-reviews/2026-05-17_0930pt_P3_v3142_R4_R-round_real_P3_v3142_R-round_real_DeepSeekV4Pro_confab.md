# P3_v3142 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_0930pt_P3_v3142_R4_R-round_real
**Wall time**: 188.3s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=55705, completion=8340, reasoning=7256, total=64045

---

## PAPER-DEE-B1 — BLOCKER: Headline catalog size 378,280 depends on unresolved dedup arithmetic

**Location:** Abstract, §3 (Table 1 footnotes), §4.3, §7, and throughout.

**Issue:** The paper reports 637 multi-survey positional coincidences (all pairwise) but also states that the 7-way dedup script removed 10,213 duplicate detections, yielding 378,280 = 388,493 − 10,213 unique objects. If all cross-survey matches are pairwise and number 637, the maximum possible duplicate count from cross-survey overlaps is 637 (one extra detection per pair). The remaining 10,213 − 637 = 9,576 duplicates are unexplained. The paper acknowledges the mismatch as a deferred item but continues to quote 378,280 as the canonical catalog size throughout the abstract, conclusions, and all downstream scalings (e.g., 141× increase). A central result built on an internally inconsistent dedup is not credible.

**Fix:** Reconcile the union-find dedup output with the 637 coincidences (e.g., publish the full cluster manifest with per-cluster multiplicity) and update the headline number accordingly, or retract the precise count and quote a range until the arithmetic is resolved.

---

## PAPER-DEE-B2 — BLOCKER: 17.8% genuine novelty fraction has no traceable provenance

**Location:** Abstract, §4.1 (“Archival cross-match and genuine novelty fraction”), §6, §7.

**Issue:** The abstract and conclusions prominently feature “a genuine novelty fraction of ∼17.8%” (178/1,000) for DESI top-1,000 anomalies cross-matched against 20 all-sky catalogues via CDS X-Match. No companion artifact path, script, or dataset is provided for this cross-match. The number cannot be reproduced or audited from the paper alone, and it is a load-bearing headline figure.

**Fix:** Provide the exact cross-match script, the list of 20 catalogues, and the output file (e.g., a CSV of the 1,000 objects with match flags) in the data release, or remove the claim until provenance is established.

---

## PAPER-DEE-M1 — MAJOR: 58.8% aggregate SIMBAD-unmatched fraction is not reproducible

**Location:** §4.1, §7 (conclusions).

**Issue:** The paper states “the aggregate SIMBAD-unmatched fraction … is 58.8%, weighted across all surveys with SIMBAD-matchable coordinates.” No weighting formula, per-survey weights, or script is given. The per-survey unmatched fractions are listed, but the aggregate cannot be recomputed from displayed values. This number appears in the conclusions as a summary statistic.

**Fix:** Specify the exact weighting scheme (e.g., inverse-variance, simple average of survey fractions, or total unmatched divided by total matchable) and provide a companion script or a table of intermediate quantities so the 58.8% figure is reproducible.

---

## PAPER-DEE-N1 — minor: Fisher 95% CI bounds contain an arithmetic slip

**Location:** §5 (Cosmological Applications), paragraph beginning “The Wave~14-VVV measurement therefore closes…”

**Issue:** The paper writes “the linear Fisher mapping gives a symmetric σ_fNL interval [3.66, 12.94] at 95% (central 8.27 ∓ 1.96·2.37).” However, 1.96 × 2.37 = 4.6452, so the correct interval is [8.27 − 4.6452, 8.27 + 4.6452] = [3.6248, 12.9152]. The reported bounds are off by ≈0.035. The discrepancy is small but indicates a rounding or transcription error.

**Fix:** Recompute with the exact product (1.96 × 2.379 = 4.66284, giving [3.607, 12.933]) or state the rounding explicitly.

---

## PAPER-DEE-N2 — minor: Linear Fisher slope −3.66 is asserted without derivation

**Location:** §5, “σ_fNL(α) ≈ 8.98 − 3.66α”.

**Issue:** The sensitivity table in Appendix A shows σ_fNL values that imply a local slope of approximately −3.6 (e.g., Δσ_fNL/Δα = −0.18/0.05 = −3.6 between α=0.15 and 0.20). The paper uses −3.66 without explaining its origin (e.g., a linear fit to the table, or matching the fiducial point exactly). While the difference is small, the number is load-bearing for the ±2.37 error propagation, and its provenance should be transparent.

**Fix:** Add a sentence stating that −3.66 is the slope of the linear interpolation that passes through (α=0, σ_fNL=8.98) and (α=0.15, σ_fNL=8.43), or provide the fit coefficients.
