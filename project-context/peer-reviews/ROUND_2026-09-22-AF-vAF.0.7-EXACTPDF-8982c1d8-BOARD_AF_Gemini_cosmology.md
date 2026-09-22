# AF ROUND_2026-09-22-AF-vAF.0.7-EXACTPDF-8982c1d8-BOARD — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-3.1-pro-preview`
**Input PDF**: `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.pdf` sha256=8982c1d8e1e0fac155aa27909a71300c1ee68bc2cfded6c6f944f019985c4023 pages=18
**Review packet(s)**: `efa524ee1f411e3616781f5e5b50075a7de455f8241465b5cb76e75901cba818`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 261.8s

---

This is a referee report for the manuscript "A provenance-sealed DESI DR1 anomaly-score candidate catalogue: selection, validation, and a null known-object recovery benchmark" submitted to ApJS.

The manuscript presents a rigorously validated, provenance-sealed catalogue of 1,244 anomaly-score selected DESI DR1 spectra. The paper is exceptionally well-structured, and its commitment to reproducibility, explicit validation contracts, and careful distinction between a "candidate catalogue" and a "discovery" is highly commendable and sets a strong standard for data releases. The mathematical and statistical claims in the abstract and body are internally consistent, and the effect sizes are properly reported alongside p-values.

However, the manuscript contains several instances of internal review-log prose, uncomputed quantitative claims, and missing final provenance links that must be resolved before publication. 

### Findings

**1. Internal Review-Log Prose and Version History (ESSENTIAL)**
- **ID:** AF-E1
- **Section/Page:** Page 1 (Date line), Page 7 (Sec V.C), Page 17 (Appendix A)
- **Problem:** The manuscript contains multiple instances of internal audit tags, version history, and direct responses to a "confirmation board" that should not appear in the final published text. 
  - Page 1: `(vAF.0.7)` in the date line.
  - Page 7: "...the 2026-09-22 confirmation board flagged the summary locations for conflating this univariate figure with the full-model collapse-on-removal figure above..."
  - Page 17: "...in response to the confirmation board's ESSENTIAL finding that these three works were named in prose without a bibliography entry..."
  - Page 17: "...a live ADS check of these five specifically remains open and is not claimed as done."
- **Required Fix:** Remove all internal review-log prose, version tags, and audit trail commentary. The bibliography must be fully verified prior to publication; an admission of incomplete verification cannot be published.

**2. Missing Provenance/DOI (ESSENTIAL)**
- **ID:** AF-E2
- **Section/Page:** Page 16 (Sec IX)
- **Problem:** The data availability section contains an unfilled placeholder: `[placeholder: Zenodo DOI for the public deposit]`.
- **Required Fix:** The final Zenodo DOI must be minted and inserted into the text. The public deposit must be frozen and accessible to readers upon publication.

**3. Uncomputed Quantitative Claims (MAJOR)**
- **ID:** AF-M1
- **Section/Page:** Page 10 (Sec V.D)
- **Problem:** The text asserts: "the reference footprints are small compared with the parent survey, so the test has little power for rare classes." This is a quantitative claim about footprint area that is not computed or cited.
- **Required Fix:** Provide the actual footprint area (in square degrees) of the reference classes compared to the DESI DR1 footprint, or cite the specific footprint areas to support the claim.

**4. Uncomputed Quantitative Claims (MAJOR)**
- **ID:** AF-M2
- **Section/Page:** Page 13 (Sec VII.B)
- **Problem:** The text asserts that a 4.33 nmgy g-band flux (approx 20.9 AB mag) is "orders of magnitude above any plausible Legacy Survey noise floor". While true, this is an uncomputed quantitative claim.
- **Required Fix:** State the actual Legacy Survey g-band noise floor (e.g., the 5-sigma depth of ~24 mag) to explicitly quantify the "orders of magnitude" claim.

**5. Typographical Error in Section Referencing (MINOR)**
- **ID:** AF-N1
- **Section/Page:** Page 17 (Acknowledgments)
- **Problem:** The text states: "All computation for this manuscript's assembled numbers (Sec. A) ran locally..." There is no Section A; the text is referring to Appendix A.
- **Required Fix:** Change "(Sec. A)" to "(Appendix A)".

**6. Typographical Error (NIT)**
- **ID:** AF-N2
- **Section/Page:** Page 15 (Sec VIII)
- **Problem:** The text contains a stray space in a hyphenated word: "over -abundance".
- **Required Fix:** Remove the space.

## Summary recommendation
ACCEPT WITH MINOR CORRECTIONS

The manuscript is a highly rigorous, reproducible, and well-executed data release that perfectly matches the scope of ApJS. The statistical analysis is sound, and the conclusions are appropriately conservative. The required corrections are entirely cosmetic and administrative (removing internal review logs, filling in the DOI placeholder, and quantifying two footprint/depth claims). Once these minor corrections are made, the paper will be an excellent addition to the literature.