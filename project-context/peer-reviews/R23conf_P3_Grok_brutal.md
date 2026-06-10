# P3 R23conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.80.pdf` md5=03f05e26 pages=23
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 182.6s

---

**Referee Report**

**Paper:** P3 (BigAE multi-survey anomaly catalog)

**Journal target:** Phys. Rev. D

**Date of review:** Round R23conf

**Findings (adversarial audit)**

**P3-E1 (ESSENTIAL)**  
Section: Abstract (p. 1)  
Problem: “genuine novelty fraction of ~17.8% (single-sample point estimate at the top-1,000 score stratum)” is stated as a headline result. Body (p. 10, Fig. 6, Table I) shows survey-by-survey SIMBAD-unmatched fractions ranging from 27 % (Gaia) to 99 % (DESI top-10k). The 17.8 % figure is obtained only after aggressive 20-catalog CDS X-Match on the top-1,000 DESI objects and is not reproducible for the full 378 k catalog.  
Required fix: Remove the single scalar from the abstract or replace with the full range and explicit statement that it is an upper bound on discovery rate, not a catalog-wide purity.

**P3-E2 (ESSENTIAL)**  
Section: V (Cosmological Applications), p. 12–13 and abstract  
Problem: Claims “testable at 3–5σ with SPHEREx” and quotes central \(\sigma(f_{NL})=8.14\) (7.9 % improvement). The same paragraph states the improvement is “consistent with no improvement at <1σ”. The Fisher forecast uses an empirical \(\alpha_{jk}=0.19\pm0.65\) that is itself <1σ from null. No multi-tracer covariance or realistic systematics budget is propagated.  
Required fix: Either withdraw the cosmological claim or present a full end-to-end forecast with systematics that actually reaches ≥3σ under realistic assumptions. Current text is internally contradictory.

**P3-E3 (ESSENTIAL)**  
Section: II.D (Path-C Rebuild), p. 3–4 and Table I  
Problem: 98 % of the LAMOST “anomalies” are blue-excess training artifacts (explicitly labeled FAIL). The catalog still includes the full 44 k LAMOST objects in the headline 378 k count. The 7-way deduplication (p. 4) does not remove them.  
Required fix: Either excise the LAMOST tier from the primary catalog or publish a cleaned “science-grade” subset that excludes known artifact classes. The present headline number is inflated by construction.

**P3-M1 (MAJOR)**  
Section: I (Introduction) and abstract  
Problem: Repeated claim of “largest-scale application” and “~141× the size of the largest prior single-survey anomaly catalog [11]”. Liang et al. (2023) processed 250 k spectra; the present work processes 22.5 M DESI spectra but releases only the top 0.87 % (195 k). Effective discovery volume increase is ~73× for DESI alone, not 141×, once selection functions are normalized.  
Required fix: Replace “largest” language with precise effective-volume ratios that account for anomaly fraction and survey depth.

**P3-M2 (MAJOR)**  
Section: III.F (Planck) and Appendix F  
Problem: ACT DR6 cross-transfer block (200 patches) is formally quarantined because both gate criteria fail, yet the 200 patches are still added to the headline 378 k count “for completeness.” The Planck×ACT cross-correlation is null (p. 11).  
Required fix: Remove the 200 patches from the primary catalog or move them to a clearly labeled supplementary table.

**P3-M3 (MAJOR)**  
Section: Fig. 3 (right panel) and p. 6  
Problem: SDSS DR18 anomaly-score distribution spans 12 orders of magnitude because the model was trained on DESI; the extreme tail is dominated by M7–T2 dwarfs that are out-of-distribution by construction. The paper presents this as a feature (“transfer-learning”) rather than a systematic failure mode.  
Required fix: Demonstrate that the same objects remain high-scoring when a native SDSS BigAE is trained, or flag the entire SDSS tier as exploratory.

**P3-N1 (MINOR)**  
Section: Abstract and p. 1  
Problem: Date stamp “(Dated: June 2026)” appears in a submitted manuscript.  
Required fix: Replace with standard “submitted” or “preprint” date.

**P3-N2 (NIT)**  
Multiple figure captions (Figs. 2, 7) contain axis labels that are legible only at full zoom; no unit or coordinate-system statement in the caption itself.  
Required fix: Add explicit coordinate system and unit statements to every sky-map caption.

**Summary recommendation**  
**REJECT**

The manuscript presents an undeniably large catalog, but the core science result is a catalog whose purity is dominated by acknowledged training artifacts in at least one major survey, whose headline novelty fraction cannot be reproduced across the full sample, and whose cosmological application fails to reach even 1σ significance while simultaneously claiming 3–5σ testability. These are not cosmetic issues; they are fatal to the central claims. The work is closer to a data-release note than a Phys. Rev. D article. A substantially revised version that (i) publishes only the artifact-cleaned subset, (ii) removes or heavily qualifies the cosmological section, and (iii) provides a reproducible purity metric would be required before reconsideration.