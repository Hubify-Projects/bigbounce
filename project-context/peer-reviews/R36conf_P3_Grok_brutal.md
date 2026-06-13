# P3 R36conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.101.pdf` md5=2cba9f61 pages=28
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 100.0s

---

**Referee Report**

**Paper:** Spectrally Unusual Sources at Scale… (BigAE multi-survey anomaly catalog)

**Journal:** Physical Review D

**Date of review:** First read

**Finding P3-E1 (ESSENTIAL)**  
**Location:** Abstract, p. 1 (first paragraph)  
**Problem:** Abstract states “the recommended catalog-grade tier contains 269,317 unique entries (269,117 point-source…)” and “378,280 Path-C Unique Anomalies”. Body Table I (p. 7) and §III (p. 5) headline the final Path-C catalog as 378,280 (378,080 point-source + 200 Planck patches). The 269 k figure appears nowhere in the final results; it is an earlier cross-transfer number.  
**Required fix:** Rewrite abstract to match the body headline numbers exactly; delete all stale version-specific counts.

**Finding P3-E2 (ESSENTIAL)**  
**Location:** Abstract, p. 1 (“Dated: June 2026”)  
**Problem:** Future date in a submitted manuscript.  
**Required fix:** Remove.

**Finding P3-E3 (ESSENTIAL)**  
**Location:** Abstract, p. 1 and §V (p. 16) Fisher forecast  
**Problem:** Abstract claims “central 9.4 % improvement”. Body (p. 16) shows the de-biased multi-tracer value is exactly equal to the single-tracer baseline once \(\alpha_{jk}=0.19\pm0.65\) is inserted; the 9.4 % figure is an optimistic central-value statement that the text itself labels “not the convex central value”. No effect-size or practical-significance qualifier accompanies the headline percentage.  
**Required fix:** Remove the 9.4 % claim from the abstract or replace with the explicit statement that the improvement is statistically consistent with zero at current S/N.

**Finding P3-E4 (ESSENTIAL)**  
**Location:** Abstract + §IIID (p. 5) and Table I footnotes  
**Problem:** Abstract advertises “a Native-Trained Novelty Fraction from 37.3 Million Sources”. The 37.3 M figure is the sum of raw input catalogs before any deduplication or quality cuts; the actual science sample after 5″ deduplication is 378 k objects. The abstract therefore inflates the search volume by two orders of magnitude.  
**Required fix:** State the final unique-object count in the abstract; move raw input totals to methods.

**Finding P3-M1 (MAJOR)**  
**Location:** Entire manuscript (28 pages)  
**Problem:** PRD methods papers on anomaly detection or catalog construction are routinely 10–15 pages. The present work contains 28 pages of pipeline minutiae, 8 tables, 12 figures, and repeated internal path strings (“pipelines/p3_anomaly_engine/…json”).  
**Required fix:** Condense to ≤15 pages or justify the length to the editor.

**Finding P3-M2 (MAJOR)**  
**Location:** §IIB, §IIIC, Table I footnotes, p. 3–7  
**Problem:** Dozens of literal Unix paths, JSON filenames, and commit-specific scripts appear in the main text and footnotes. These are internal bookkeeping artifacts, not reproducible provenance for a journal reader.  
**Required fix:** Move all such strings to a machine-readable manifest; replace with stable DOIs or Zenodo records.

**Finding P3-M3 (MAJOR)**  
**Location:** §IVA (p. 13) and abstract novelty claim  
**Problem:** “Genuine novelty fraction ~17.8 %” is derived from a single top-1 000 stratum against 18 catalogs. No Wilson-interval or bootstrap uncertainty is quoted in the abstract; the 17.8 % figure is presented as a point estimate.  
**Required fix:** Quote the full binomial interval and state that it is a single-sample, top-1 000 estimate only.

**Finding P3-M4 (MAJOR)**  
**Location:** Figure 7 (p. 15) and §IVB  
**Problem:** The \(\chi^2=376713\) test for spatial uniformity is reported without an effect-size measure (Cramér’s V or equivalent). The reader cannot judge whether the detected non-uniformity is astrophysically meaningful or merely a footprint artifact.  
**Required fix:** Add effect size.

**Finding P3-N1 (MINOR)**  
**Location:** Table I, p. 7, footnote ♠  
**Problem:** Footnote mixes three different threshold definitions without a clear mapping to the columns.  
**Required fix:** Clarify.

**Finding P3-N2 (MINOR)**  
**Location:** Figure 1 caption (p. 3)  
**Problem:** “GOLD QSO-candidate confidence tier” is referenced but never defined in the caption or main text on that page.  
**Required fix:** Add one-sentence definition or pointer.

**Finding P3-N3 (NIT)**  
**Location:** Multiple figure captions  
**Problem:** Color bars and axis labels are legible but lack explicit units in several panels (e.g., anomaly score in Fig. 3 right panel).  
**Required fix:** Add units.

**Summary recommendation: REJECT**

The manuscript in its present form cannot be accepted. The abstract contains multiple numerically inconsistent and inflated claims that are directly contradicted by the body (E1–E4). Internal pipeline bookkeeping text and an excessive page count further render the paper unsuitable for PRD. Even after the abstract is corrected, the work would require major condensation and removal of non-journal-grade artifacts before it could be reconsidered.