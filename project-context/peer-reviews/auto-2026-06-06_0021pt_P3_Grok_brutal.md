# P3 auto-2026-06-06_0021pt — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 105.9s

---

**Referee Report for Physical Review D**

**Paper:** Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies… (P3)

**Date of review:** auto-2026-06-06

**Overall assessment:** The manuscript presents a large catalog produced by applying a deterministic autoencoder (BigAE) to seven surveys. While the computational scale is substantial, the paper fails to meet PRD standards for methodological rigor, statistical control, reproducibility, and honest framing of results. Multiple internal-audit artifacts, unverifiable abstract scalars, marginal or null cosmological claims presented without proper qualification, and admitted training-set biases that dominate the output render the work unsuitable for publication without wholesale revision.

**Findings (classified ESSENTIAL / MAJOR / MINOR / NIT)**

**P3-E1 (ESSENTIAL) — Abstract, p. 1**  
Abstract states “378,280 Path-C Unique Anomalies” and “7.9% improvement consistent with no improvement at <1σ”. The 378,280 figure is traceable (378,080 + 200), but the 7.9% improvement is computed from single-tracer baseline \(\sigma(f_{NL})^{\rm std}=8.98\) vs. multi-tracer 8.14; the paper itself states this is <1σ and “not a positive multi-tracer detection claim.” Abstract therefore misleads.  
*Fix:* Remove or explicitly qualify the improvement claim in the abstract; state that no detection is claimed.

**P3-E2 (ESSENTIAL) — Abstract & §V, pp. 1, 10**  
Abstract and §V present \(\gamma=2.567\pm0.382\) and matter-bounce \(\gamma=3.0\) at “+1.13\(\sigma\) (marginally consistent)”. No explicit statement that different null procedures are not directly comparable appears at every juxtaposition of these numbers. Violates instruction 7.  
*Fix:* Add explicit non-comparability language or remove the side-by-side \(\sigma\) claims.

**P3-E3 (ESSENTIAL) — §IIID & Table I, p. 3**  
98% of LAMOST anomalies are blue-excess training artifacts; the native-retrain still releases the tier as “exploratory”. The catalog headline (378,280) includes these objects without a quantitative contamination budget propagated to downstream users.  
*Fix:* Either remove LAMOST from the headline catalog or supply a per-survey contamination posterior that users must apply.

**P3-E4 (ESSENTIAL) — §IIID & Fig. 7, p. 3**  
Three surveys (LAMOST, Gaia, eROSITA) fail the 5\(\sigma\) injection-recovery gate. The paper nevertheless includes them in the “Path-C unique” total. This violates the authors’ own gate criteria.  
*Fix:* Recompute headline numbers excluding all surveys that fail the stated gate, or retract the gate as non-binding.

**P3-E5 (ESSENTIAL) — §IVB & Fig. 5, p. 9**  
“Genuine novelty fraction ~17.8%” is derived from a single top-1,000 stratum cross-match against 20 catalogs. No bootstrap or jackknife uncertainty is provided; the number is presented as a point estimate.  
*Fix:* Supply statistical uncertainty or downgrade to “illustrative”.

**P3-M1 (MAJOR) — §IIA, p. 2**  
BigAE is deterministic; no ensemble or variational treatment. Latent-space stability is asserted via 5-fold Jaccard \(\bar{J}=0.862\) but only on the training pool, not on the full survey.  
*Fix:* Demonstrate that anomaly rank-order is stable under architecture variation or data-split variation on the production catalog.

**P3-M2 (MAJOR) — §IIID Step 6 & Appendix F, p. 3**  
ACT DR6 is formally quarantined yet the 200-patch cross-transfer block is retained “as a sensitivity-check artifact”. The text simultaneously claims the block “contributes zero objects”. This internal contradiction must be resolved.  
*Fix:* Remove the block entirely or document it in a dedicated appendix labeled as non-science.

**P3-M3 (MAJOR) — Fig. 1 & spatial uniformity test, p. 4**  
\(\chi^2=143{,}936\) (38{,}329 dof) is reported; the paper states the distribution is “significantly non-uniform” but attributes it to survey selection functions without modeling those functions. The test is therefore circular.  
*Fix:* Either model the selection function or remove the \(\chi^2\) claim.

**P3-M4 (MAJOR) — Table I footnotes & §IIID, p. 7**  
Multiple footnotes redefine the headline numbers after the fact (“Path-C native-retrained counts are the canonical results”). Readers cannot reconstruct the exact arithmetic without the companion repository.  
*Fix:* Provide a single, self-contained table with all arithmetic steps shown.

**P3-N1 (MINOR) — p. 1**  
“(Dated: June 2026)” appears in the author block. This is an internal placeholder.  
*Fix:* Remove.

**P3-N2 (MINOR) — Throughout**  
Repeated use of internal gate terminology (“gate PASS”, “gate FAIL”, “Path-C rebuild”) without a one-paragraph glossary on first use.  
*Fix:* Add glossary.

**P3-N3 (NIT)**  
Several figure captions refer to “Fig. ??” (pp. 2, 5).  
*Fix:* Correct.

**Summary recommendation**  
**REJECT**

The manuscript contains multiple ESSENTIAL violations: unverifiable or misleading abstract scalars, failure to enforce the authors’ own quality gates, absence of statistical control on the headline novelty fraction, and side-by-side \(\sigma\) claims without the required non-comparability language. The cosmological section presents marginal results as “applications” while the text itself disclaims detection. These are not cosmetic issues; they go to the core of what constitutes a publishable PRD methods paper. A major rewrite that (i) removes or properly caveats all non-detections, (ii) enforces the stated gates, and (iii) supplies a self-contained statistical audit trail would be required before resubmission.