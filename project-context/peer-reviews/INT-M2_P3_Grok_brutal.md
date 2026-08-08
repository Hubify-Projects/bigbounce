# P3 INT-M2 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=f6b8d9a5 pages=30
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 98.0s

---

**Referee Report – Physical Review D**

**Paper:** Spectrally Unusual Sources at Scale… (Golden, 2026 preprint)

**P3-E1 (ESSENTIAL)**  
Section: Title page (rendered p. 1)  
Quote: “(Dated: June 28, 2026)”  
Problem: Submission dated in the future. This is not a production PDF.  
Required fix: Replace with actual submission or revision date.

**P3-E2 (ESSENTIAL)**  
Section: Abstract + Table I (pp. 1, 9)  
Problem: Abstract headline numbers (269 317 / 378 280) are internally consistent with the body only after the reader accepts seven distinct per-survey threshold definitions and two different native-retrain vs. cross-transfer conventions. No single, reproducible scalar definition of “recommended-tier” is given that a standalone reader can apply to the released tables without the exact pipeline scripts.  
Required fix: Provide one machine-readable column or explicit Boolean mask that directly yields the headline counts.

**P3-E3 (ESSENTIAL)**  
Section: §II D & Table I footnotes (pp. 5, 9)  
Problem: Multiple σ values and Jaccard gates are declared “PASS/FAIL” on survey-specific validation splits whose statistics are never shown side-by-side with a common null. The paper repeatedly juxtaposes these numbers without the explicit qualifier required by instruction 7.  
Required fix: Add the sentence “These figures are not directly comparable across surveys” at every such juxtaposition, or recompute all gates on a common footing.

**P3-M1 (MAJOR)**  
Section: Throughout (e.g., pp. 2, 4, 6, 12)  
Problem: >30 explicit references to internal pipeline paths (“pipelines/p3_anomaly_engine/…”, “committed training.log.json”, etc.) that are not frozen with commit hashes or DOIs in the Data Availability statement. A standalone reader cannot audit the exact preprocessing or scaling constants used for the released catalog.  
Required fix: Deposit a single, version-stamped Git repository or Zenodo bundle containing every script that produced the numbers in Tables I–VIII.

**P3-M2 (MAJOR)**  
Section: Fig. 3 & §III C (p. 8)  
Problem: The SDSS anomaly-score distribution is shown only after the DESI-trained model is applied; the native SDSS retrain distribution is never plotted on the same axes. The claimed “3.9× rate inflation” cannot be verified from the figure.  
Required fix: Add the native SDSS score histogram (or state that it is withheld).

**P3-M3 (MAJOR)**  
Section: §V A & Fig. 9 (p. 19)  
Problem: The 6.1 % central improvement in σ(f_NL) is presented as a forecast under a fixed α = 0.15 prior that is itself derived from the empirical α_jk = 0.19 ± 0.65. The paper never shows the degradation when the measured (uncertain) α is used instead.  
Required fix: Replace the fixed-prior forecast with the marginal posterior that folds in the measured α uncertainty.

**P3-N1 (MINOR)**  
Section: Table I caption (p. 9)  
Problem: Symbol “♠” is defined only in a footnote that appears after the table; the dagger/heart/paragraph symbols are introduced out of order.  
Required fix: Move all symbol definitions into the caption.

**P3-N2 (NIT)**  
Section: Multiple figure captions  
Problem: Several captions contain parenthetical pipeline paths and “see §III E” cross-references that are unnecessary for a reader who only wants to interpret the plotted data.  
Required fix: Move such text to footnotes or the methods section.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript presents an ambitious multi-survey anomaly catalog whose headline numbers are internally consistent only after the reader accepts a thicket of survey-specific thresholds and unreleased pipeline choices. The future date on the title page, the absence of a frozen reproducibility bundle, and the repeated juxtaposition of non-comparable σ/Jaccard figures without explicit caveats are each sufficient to prevent acceptance in their current form. A revised submission that supplies (i) a single reproducible mask for the recommended tier, (ii) a public code repository with exact commit hashes, and (iii) corrected statistical language around cross-survey comparisons would be required before further consideration.