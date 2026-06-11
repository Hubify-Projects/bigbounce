# P3 R29 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.88.pdf` md5=bbc52726 pages=26
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 104.8s

---

**Referee Report**

**Paper:** P3 (Round R29)  
**Journal target:** Phys. Rev. D  
**Title:** Spectrally Unusual Sources at Scale…  
**Author:** Houston Golden  

I have examined every page, figure, table, equation, caption, and footnote in the rendered PDF. The manuscript contains multiple classes of fatal defects that preclude acceptance at PRD. Findings are classified below.

### ESSENTIAL (paper cannot be accepted without these fixes)

**P3-E1**  
**Location:** Abstract (p. 1), §I (p. 1), Table I caption (p. 9), and multiple footnotes throughout.  
**Problem:** The manuscript is riddled with internal version-control and audit language that has no place in a submitted journal article: “an earlier draft quoted 264,938/264,738”, “superseded by the empirical”, “Legacy reference only — superseded”, “earlier draft listed 10.6 s”, “R7/R8/R-round” style tags implied by repeated “see Table IV caveat (b)”, “Path-C rebuild”, and “before/after diagnostic”. These phrases appear verbatim in the body and tables.  
**Required fix:** Complete removal of all version-history, “superseded”, “earlier draft”, and internal-audit phrasing. The manuscript must read as a standalone, frozen submission.

**P3-E2**  
**Location:** Abstract (p. 1) vs. §V (p. 15) and Appendix C (p. 21).  
**Problem:** Abstract states the de-biased multi-tracer forecast yields “a central 9.4% improvement”. The body (§V, Fig. 9, Appendix C) shows this 9.4% figure is obtained only under the fixed-α = 0.15 prior; the empirical α_jk = 0.19 ± 0.65 result gives zero improvement inside 1σ. The abstract claim is therefore stronger than, and ordered differently from, the final calibrated body statement.  
**Required fix:** Abstract must be rewritten to match the body’s final calibrated statement exactly, including the explicit caveat that the improvement is a central-value forecast under a fixed prior and disappears under the empirical measurement.

**P3-E3**  
**Location:** Abstract (p. 1), §IV A (p. 11), and §VI A (p. 17).  
**Problem:** The headline 17.8% “genuine novelty fraction” is computed from a single 1,000-object subsample against 20 catalogs; the paper itself states this is “empirically untested” for the full catalog and that the 58.8% SIMBAD-unmatched fraction “overstates true catalog novelty”. The abstract presents 17.8% without the required qualification.  
**Required fix:** Remove or heavily qualify the 17.8% figure in the abstract; the body already labels it untested.

**P3-E4**  
**Location:** Table IV (p. 19) and §VI D (p. 18).  
**Problem:** Ten “residual caveats” are listed as “closed (C = resolved in paper)”. Several closures rely on companion-repository files or “see §VID(ii)” that are not self-contained. A standalone reader cannot verify closure without external material.  
**Required fix:** Every listed caveat must be fully resolved inside the manuscript with explicit numbers and no external pointers.

**P3-E5**  
**Location:** §II D (p. 4), §III (p. 5), and all Path-C gate language.  
**Problem:** The entire analysis pipeline is defined by an internal six-step “Path-C rebuild” protocol whose gate criteria (val_loss ≤ 0.30, Jaccard ≥ 0.70, injection-recovery ≥ 50% at 5σ) are engineering thresholds chosen by the author, not statistically justified procedures. No literature comparison or simulation calibration of these exact thresholds is provided.  
**Required fix:** Replace ad-hoc gates with statistically motivated, pre-registered criteria or demonstrate via end-to-end simulations that the chosen thresholds do not bias the final catalog.

### MAJOR

**P3-M1**  
**Location:** Entire manuscript length (26 pages) vs. claimed contribution.  
**Problem:** The paper is excessively long for a methods catalog paper. PRD methods papers of comparable scope are typically ≤ 12–15 pages. The bulk is consumed by internal protocol description rather than new astrophysical or methodological insight.  
**Required fix:** Reduce to ≤ 15 pages; move all gate-by-gate diagnostics, per-survey training logs, and exhaustive caveat tables to a companion data-release paper.

**P3-M2**  
**Location:** Fig. 3 (p. 7), Fig. 4 (p. 8), and §III C (p. 6).  
**Problem:** The SDSS anomaly-score distribution is shown on a log scale spanning >10 orders of magnitude; the extreme high-score tail (S > 10^4) is labeled a cross-transfer artifact, yet the figure still presents it as part of the scientific result. No quantitative statement of the fraction of the catalog affected by this artifact is given in the main text.  
**Required fix:** Provide a single, prominent table or paragraph stating the exact fraction of each survey’s anomalies that survive after artifact excision.

**P3-M3**  
**Location:** §V (p. 15) and Fig. 9 (p. 17).  
**Problem:** The multi-tracer f_NL forecast improvement is reported as “central 9.4%” with a 1σ envelope that still includes zero. No effect-size or practical-significance metric (e.g., fractional change in posterior volume, Bayes factor) is supplied.  
**Required fix:** Add a quantitative effect-size statement for every headline σ or percentage improvement.

**P3-M4**  
**Location:** Data-availability paragraph (p. 20) and provenance audit.  
**Problem:** The manifest link points to a Hugging Face repository whose file sizes and SHA-256 hashes are stated to be “frozen pre-submission,” yet the text simultaneously refers to “earlier draft” numbers. The release is therefore not verifiably frozen at the version described in the paper.  
**Required fix:** Provide a single, immutable DOI or Zenodo record with explicit file hashes that match the exact numbers quoted in the submitted manuscript.

### MINOR / NIT

**P3-N1** Duplicate phrasing: “canonical canonical-mask” does not appear, but “Path-C native retrain” is repeated verbatim in adjacent sentences on p. 4.  
**P3-N2** Axis label on Fig. 11 (p. 22) uses “Sparse tracer number density n (Mpc/h)^3” while the caption uses “n”; inconsistent notation.  
**P3-N3** “Dated: June 2026” on title page is a future date relative to any plausible submission; remove or correct.

### Summary recommendation

**REJECT**

The manuscript cannot be considered for publication in its current form. It contains pervasive internal audit and version-control language, presents abstract claims that are stronger than or unaccompanied by the caveats present in the body, relies on ad-hoc engineering gates without statistical justification, and is substantially over-length for the incremental methodological contribution. These are not cosmetic issues; they violate PRD standards for a self-contained, frozen, and statistically rigorous manuscript. A complete rewrite that removes all internal bookkeeping, shortens the text by roughly 40%, and supplies statistically motivated rather than protocol-driven thresholds would be required before resubmission.