# P3 RA-INT — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=24ac287f pages=30
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 112.8s

---

**REFEREE REPORT — Physical Review D**

**Paper:** P3 (Golden, “Spectrally Unusual Sources at Scale…”)

**Recommendation:** REJECT

### ESSENTIAL findings (any one sufficient for rejection)

**P3-E1 (Abstract, p. 1; §I, p. 2)**  
The abstract headline numbers (269 317 recommended-tier / 378 280 total) are not recomputable from the body without the exact 5″ deduplication script and the precise definition of “validated catalog-grade.” The text itself states the ≥ symbol is “conservative” and that the exact validated-only count “is not recomputable.” This violates the requirement that every scalar in the abstract be directly traceable to displayed inputs.

**P3-E2 (Abstract, p. 1; §V, p. 17–18)**  
The abstract presents a 9.4 % Fisher-forecast improvement as a headline result. The body (§V B, Fig. 9) shows the de-biased central value is exactly the single-tracer baseline (8.98) and the quoted improvement is only the difference between two different bias assumptions, not a detection. The abstract claim is stronger than, and ordered differently from, the body’s final calibrated statement.

**P3-E3 (p. 1, “Dated: June 28, 2026”)**  
A submission date in the future is an internal drafting artifact that should not appear in a camera-ready manuscript. Its presence indicates the document has not undergone final provenance cleaning.

**P3-E4 (§II D, p. 5; §III, passim)**  
The entire Path-C “native retrain” protocol is defined by a chain of six heuristic gates (val_loss ≤ 0.30, injection-recovery ≥ 50 % at 5σ, Jaccard ≥ 0.70, etc.) whose numerical values are never justified by a power calculation or false-positive budget. Changing any single gate by < 20 % alters the headline counts by thousands of objects. No sensitivity table is supplied.

**P3-E5 (Fig. 3 right panel, p. 8; §III C, p. 10)**  
The SDSS anomaly-score distribution is produced by a DESI-trained model applied cross-survey; the native SDSS retrain compresses the same objects from S > 10¹⁰ to S < 14. The paper never quantifies how much of the published SDSS catalog is therefore an artifact of domain shift rather than intrinsic rarity. This is fatal for any claim that the catalog is “science-ready.”

### MAJOR findings

**P3-M1 (§IV A, p. 14)**  
The 17.8 % “genuine novelty fraction” is computed on the top-1 000 DESI objects only. The paper never demonstrates that this fraction is stable when the rank cut is moved to 5 000 or 10 000. The Wilson interval quoted applies only to the chosen stratum.

**P3-M2 (Table I, p. 9; footnotes)**  
Three different threshold families are used (fixed S > 5, top-1 %, 99th percentile) with no single table showing the union or intersection of the resulting catalogs. Cross-survey comparisons therefore mix incompatible selection functions.

**P3-M3 (§V A, p. 17)**  
The NANOGRAV/SMBHB analysis reports a Bayes factor of 7.14 × 10³ against the idealized circular-orbit reference while simultaneously stating that environmentally modified SMBHB models can produce γ ≈ 2.5–3. The paper never quantifies how much of the reported evidence survives once the reference model is allowed to vary within the range the authors themselves consider plausible.

**P3-M4 (length)**  
30 pages for a methods + catalog paper whose primary deliverable is a set of ranked lists is excessive. PRD methods papers of comparable scope are typically ≤ 18 pages.

### MINOR / NIT findings (selected)

**P3-m1** Multiple instances of pipeline-script filenames and internal ticket numbers (“pipelines/p3_anomaly_engine/ext3_fm1…”) remain in the text; these belong in a reproducibility appendix, not the main body.  
**P3-m2** Fig. 2 caption states ACT DR6 is “formally quarantined” yet the object count still appears in the cross-transfer baseline total; the reader must hunt through Appendix F to discover the number is exactly zero.  
**P3-m3** The phrase “canonical canonical-mask” does not appear, but the repeated use of “canonical” for three distinct quantities (S > 5 cut, production-run score axis, and Path-C headline) creates unnecessary ambiguity.  
**P3-m4** Several figure axes are labeled only with internal variable names (S_IF,raw, r_Z) without a one-line definition in the caption.

### Summary recommendation

**REJECT**

The manuscript is a large-scale data-release paper whose scientific claims rest on a chain of unvalidated heuristic thresholds, cross-survey domain-shift artifacts that are only partially mitigated, and an abstract that materially overstates the robustness of both the catalog and the cosmological forecast. The cosmological application returns a null result once the authors’ own systematic tests are applied. The length and internal bookkeeping language are disproportionate to the incremental methodological advance. A substantially shorter, methods-focused Letter that (i) fixes the abstract–body mismatch, (ii) supplies a single reproducible selection function, and (iii) quantifies the impact of each gate on the final science conclusions might be reconsidered, but the present document does not meet PRD standards.