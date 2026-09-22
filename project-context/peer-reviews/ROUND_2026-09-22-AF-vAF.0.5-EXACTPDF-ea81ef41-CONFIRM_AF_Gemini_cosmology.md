# AF ROUND_2026-09-22-AF-vAF.0.5-EXACTPDF-ea81ef41-CONFIRM — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-3.1-pro-preview`
**Input PDF**: `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.pdf` sha256=ea81ef413503d25291853a2be714226d3b47fe680ead2f01727aaabe961140ca pages=18
**Review packet(s)**: `3af9f429037c407ec6bcde5a22feea28ea9556c09bf988633a6d041e98559789`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 139.9s

---

This is a referee report for "A provenance-sealed DESI DR1 anomaly-score candidate catalogue: selection, validation, and a null known-object recovery benchmark" submitted to ApJS. 

The paper presents a machine-learning-derived anomaly catalogue from DESI DR1, emphasizing strict provenance, reproducibility, and a pre-declared validation contract. The framing is highly commendable: the authors explicitly refuse to claim a discovery based on unconfirmed pipeline outputs and openly publish their null results and known defects. This level of rigor is exactly what is needed for large-scale anomaly detection in modern surveys. 

However, the manuscript contains a fatal contradiction regarding its primary claim of reproducibility, several missing citations that fail the standalone-reader test, leftover version-history language, and a numerical error in a flux-to-magnitude conversion. These issues must be addressed before the paper can be accepted.

### Findings

**1. ESSENTIAL: Contradiction on Reproducibility / Missing Hyperparameters**
*   **Section + Page:** Abstract (page 1) vs. Section VI.A (page 10)
*   **Specific problem:** The abstract claims the catalogue is published "together with the complete provenance chain needed to reproduce it." However, Section VI.A explicitly admits: "The UMAP and HDBSCAN hyperparameters... are not recorded in this manuscript or its manifest, so this section is not reproducible from the released files alone". 
*   **Required fix:** A paper whose central thesis is strict, hash-bound reproducibility cannot contain an irreproducible section. The authors must either recover the exact hyperparameters used, or re-run the clustering pipeline with recorded seeds/hyperparameters, update the taxonomy (and Tables VIII, IX, X), and bind the new configuration to the release manifest. 

**2. ESSENTIAL: Missing Citations (Standalone-Reader Test)**
*   **Section + Page:** Section VIII, page 15
*   **Specific problem:** The text relies on three external works to compute the $f_{NL}$ abundance shift: "applying the LoVerde, Miller, Shandera & Verde (2008) non-Gaussian correction to a Planck-2018 $\Lambda$CDM mass function (Eisenstein & Hu 1998 transfer function)". None of these three foundational papers are present in the bibliography.
*   **Required fix:** Add the missing references to the bibliography and ensure they are properly cited in the text.

**3. ESSENTIAL: Version History Language**
*   **Section + Page:** Section VII.B, page 14
*   **Specific problem:** The text reads: "and we no longer report one of them as supported." This is internal review-log or version-history language that refers to a previous draft of the manuscript.
*   **Required fix:** Remove the phrase and rewrite the sentence to describe the current state of the analysis without referencing prior drafts.

**4. ESSENTIAL: Missing Frozen-Release DOI**
*   **Section + Page:** Section IX, page 15
*   **Specific problem:** The text contains an internal placeholder: `[PLACEHOLDER: Zenodo DOI for the public deposit]`.
*   **Required fix:** The dataset must be deposited and the actual DOI must be inserted into the manuscript before publication.

**5. MAJOR: Incorrect Flux-to-Magnitude Conversion**
*   **Section + Page:** Section VII.B, page 14
*   **Specific problem:** The text states that a $g$-band flux of $4.33$ nmgy corresponds to "$\approx 20.6$ AB mag". This is incorrect. Using the standard Legacy Survey conversion ($m = 22.5 - 2.5 \log_{10}(f_{\text{nmgy}})$), a flux of $4.33$ nmgy corresponds to $20.91$ AB mag. 
*   **Required fix:** Correct the AB magnitude value to 20.9. (This does not change the physical conclusion that the object is far too bright to be a $z=5.19$ dropout, but the math must be exact).

**6. MAJOR: Uncomputed Quantitative Claim**
*   **Section + Page:** Section VII.B, page 14
*   **Specific problem:** The text dismisses two candidates because their $f_z/f_r$ ratios (1.75 and 1.42) are "far shallower than a Gunn–Peterson trough at $z \approx 6$ would produce." This is a quantitative physical claim without a supporting number. 
*   **Required fix:** State the expected theoretical or empirical $f_z/f_r$ ratio for a $z \approx 6$ quasar in the Legacy Survey filter bands to ground the "far shallower" assertion.

**7. MAJOR: Unaccounted Objects in Morphology Breakdown**
*   **Section + Page:** Section IV.C, page 5
*   **Specific problem:** The text breaks down the morphology: "441 are typed PSF (point-like) and 316 REX, with 406 rows carrying an empty MORPHTYPE". This sums to $441 + 316 + 406 = 1163$ objects. The total catalogue contains 1,244 objects. The remaining 81 objects are completely unaccounted for.
*   **Required fix:** Explicitly state the morphological types of the remaining 81 objects (e.g., DEV, EXP, COMP) so the census sums to 1,244.

**8. MINOR: Uncomputed "Orders of Magnitude" Claim**
*   **Section + Page:** Section VII.B, page 14
*   **Specific problem:** The text states the flux is "orders of magnitude above any plausible Legacy Survey noise floor". 
*   **Required fix:** Briefly state the approximate $g$-band noise floor (e.g., $\sim 24$ mag or the corresponding nmgy value) to make this a verifiable quantitative statement rather than a rhetorical one.

**9. NIT: Typographical Errors**
*   **Section + Page:** Section VIII, page 15
*   **Specific problem:** "early-galaxy over -abundance" contains an errant space.
*   **Required fix:** Change to "over-abundance".

**10. NIT: Double Punctuation**
*   **Section + Page:** Sections VII.B and VII.C, pages 14-15
*   **Specific problem:** Several list headers end with both a period and a colon (e.g., "Refuted.:", "OT-1 Selection function.:", "OT-2 Latent-space taxonomy.:").
*   **Required fix:** Remove the redundant periods.

## Summary recommendation

MAJOR REVISIONS

The paper's commitment to publishing a validated null result with strict provenance is excellent and sets a high standard for the field. However, the admission in Section VI that the clustering hyperparameters were lost directly violates the paper's core claim of complete reproducibility. The authors must re-run or recover the clustering configuration to seal the provenance chain as advertised. Additionally, the missing citations in the cosmology section, the leftover version-history text, and the magnitude conversion error must be corrected before the manuscript meets the standards of ApJS.