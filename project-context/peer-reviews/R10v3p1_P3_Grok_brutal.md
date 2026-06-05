# P3 R10v3p1 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 65.6s

---

**Referee Report**

**P3-E1 (ESSENTIAL, Abstract + §I, p. 1)**  
The abstract states a “genuine novelty fraction of ~17.8%” as a headline result. The body (§IV A, p. 9) explicitly qualifies this as “single-sample point estimate at the top-1,000 score stratum; full-catalog rate empirically untested.” The abstract therefore presents an untested extrapolation as a catalog-level claim.  
**Required fix**: Remove the 17.8% figure from the abstract or replace it with the tested quantity only.

**P3-E2 (ESSENTIAL, §V B, p. 10)**  
The Fisher forecast improvement is reported as 7.9% (central value 8.14 vs. single-tracer baseline 8.98). The text states this is “<1σ” and “not a positive multi-tracer detection claim.” The abstract nevertheless lists the numerical forecast (8.14) without the required “not directly comparable” qualifier demanded by the instruction for juxtaposed null procedures. This is a direct violation of the stated rule.

**P3-E3 (ESSENTIAL, §III D, p. 3 and Table I)**  
LAMOST DR10 native retrain yields only 5.8% injection-recovery at 5σ and is labeled “gate FAIL.” The catalog nevertheless retains 44,075 LAMOST objects in the headline 378,280 count (Table I, Path-C row). The paper’s own validation protocol therefore classifies the dominant contribution of this survey as unreliable, yet it remains in the primary catalog.

**P3-E4 (ESSENTIAL, §III F, p. 3 and Appendix F)**  
ACT DR6 cross-transfer fails both gate criteria (val_loss ~2×10^4, injection recovery <1%). The survey is formally quarantined and contributes zero objects, yet the abstract and title still cite “seven astronomical archives.” This is factually inconsistent.

**P3-M1 (MAJOR, §II D, pp. 2–3)**  
The Path-C “native retrain” protocol is a post-hoc, survey-by-survey gate system with six ad-hoc thresholds and three binary PASS/FAIL outcomes. No global false-discovery-rate control or simulation of the entire multi-survey pipeline is presented. The procedure is therefore not reproducible as a statistical method.

**P3-M2 (MAJOR, §IV A, p. 9)**  
The 58.8% SIMBAD-unmatched fraction is labeled “database-coverage measurement, not a discovery rate.” The abstract and §I nevertheless open with “largest-scale application” and “genuine novelty.” The framing is therefore inconsistent with the paper’s own later qualification.

**P3-M3 (MAJOR, Fig. 7 and §III)**  
Injection-recovery curves show that three of six surveys fail the 5σ gate. The figure caption and text do not state that the majority of the catalog volume therefore rests on surveys whose own validation metric is below the acceptance threshold.

**P3-M4 (MAJOR, §V A, p. 10)**  
The NANOGrav KDE posterior for γ = 2.567 ± 0.382 is compared to the matter-bounce prediction γ = 3.0. The offset is only +1.13σ. The paper presents this as “marginally consistent” while simultaneously stating that neither the +1.13σ deviation nor the Bayes factor constitutes a detection. The cosmological section therefore contains no positive claim yet occupies >1 page.

**P3-N1 (MINOR, p. 1)**  
“(Dated: June 2026)” is a future date on a manuscript under review. Cosmetic but should be corrected.

**P3-N2 (MINOR, Table I footnotes)**  
Multiple footnotes mix cross-transfer and native-retrain counts without a single consolidated column that readers can trace. Minor presentational issue.

**P3-NIT1–NIT3**  
Minor typographic inconsistencies in axis labels of Figs. 2 and 8; repeated use of “Path-C” without expansion on first use in the abstract; reference [12] listed as “in press” while citing a 2026 volume.

**Length assessment**  
The core methodological advance (BigAE + Path-C retraining) plus the single robust result (DESI-only anomaly catalog) could be presented in ≤12 pages. The present 20-page length is driven by six additional surveys whose validation largely fails the authors’ own gates.

## Summary recommendation
**MAJOR REVISIONS**

The manuscript cannot be accepted in its current form. Three essential statistical and framing violations (abstract novelty claim, Fisher-forecast presentation, inclusion of surveys that fail the authors’ own validation gates) must be corrected before the paper can be reconsidered. The cosmological application section adds no statistically significant result and should be either removed or reduced to a one-paragraph caveat. The paper is also substantially over-length relative to its demonstrated, reproducible contribution.