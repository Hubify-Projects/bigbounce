# P3 R39conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper3_anomaly_catalog.pdf` md5=8533c5a7 pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 167.9s

---

## Referee Report for "Spectrally Unusual Sources at Scale..."

This paper presents a large-scale, multi-survey search for anomalous astronomical sources using an autoencoder framework. The authors apply their `BIGAE` model to 37.3 million sources and map patches from seven astronomical archives (DESI, SDSS, LAMOST, eROSITA, Planck, Gaia, NEOWISE), producing a catalog of 378,280 unique anomalies. The work includes an extensive "Path-C" validation protocol involving native per-survey retraining, injection-recovery tests, and cross-validation. The resulting catalog is used to assess the genuine novelty fraction of sources and for two cosmological applications: constraining primordial non-Gaussianity (`fNL`) and testing matter-bounce predictions with NANOGrav data.

The paper is exceptionally thorough, methodologically rigorous, and transparent about its limitations. The scale of the analysis is impressive, and the "Path-C" rebuild protocol to address cross-survey domain shift is a significant contribution. The detailed reporting of validation metrics, failure modes (e.g., for LAMOST and ACT), and data-processing caveats (e.g., for eROSITA and Gaia) sets a high standard for work in this area. The cosmological applications are well-motivated, and the authors are commendably cautious in interpreting their results, correctly identifying null results and quantifying systematic uncertainties.

The manuscript is well-written and suitable for publication in Physical Review D, pending minor revisions to address the points listed below.

---
### Findings

#### ESSENTIAL

*   **P3-E1: Abstract — Missing Critical Caveat for NANOGrav Result**
    *   **Section:** Abstract (p. 1)
    *   **Problem:** The abstract reports a Savage-Dickey Bayes factor of `B_MB/SMBHB = 7.14×10^3`, which is described as "decisive only against the idealized circular-orbit SMBHB reference". While this is true, the body of the paper (Sec. V A, p. 19, "SMBHB environmental caveat") presents a much stronger and more physically relevant caveat: environmental effects can flatten the SMBHB spectral index to `γ ~ 2.5-3`, making it degenerate with the matter-bounce prediction. This significantly weakens the impact of the Bayes factor, as it is only decisive against a specific, idealized model, not the broader class of plausible SMBHB models. This crucial physical context is missing from the abstract.
    *   **Required Fix:** The abstract must be revised to include the environmental modification caveat. A phrase such as "environmentally modified SMBHB models can produce a similar spectral index, precluding a definitive exclusion of an astrophysical origin" should be added to the sentence discussing the NANOGrav result to accurately reflect the conclusions in the main text.

#### MAJOR

*   **P3-M1: Inconsistent Reporting of LAMOST Results**
    *   **Section:** Table I (p. 7) and Abstract (p. 1)
    *   **Problem:** There is a confusing juxtaposition of LAMOST anomaly counts. The abstract highlights a `21.5× LAMOST S > 5 anomaly-rate reduction after native retraining (44,075 → 2,054)`. This correctly illustrates the mitigation of a cross-transfer artifact. However, Table I reports the cross-transfer count `N_anom` as 44,075, while footnote `‡` states the *native* top-1% count is 113,342. This gives the misleading impression that native retraining *increased* the number of anomalies. The table's structure obscures the key diagnostic result (the rate compression at a fixed S>5 threshold) in favor of comparing a cross-transfer count to a native-retrained count defined by a different percentile threshold.
    *   **Required Fix:** Revise Table I to be less ambiguous. Either add a "Native Count" column to the main table for all surveys, or modify the LAMOST entry and footnote to explicitly state the S>5 counts (before: 44,075, after: 2,054) that demonstrate the 21.5x rate reduction, as this is the primary methodological finding for that survey. The current presentation requires careful reading of multiple sections to understand.

#### MINOR

*   **P3-m1: Ambiguous Wording of NEOWISE Systematics Mask**
    *   **Section:** II D (p. 5)
    *   **Problem:** The text states: "NEOWISE ecliptic-pole mask (|b_ecl| < 80°) retains 419/436 anomalies (96.1%); the rejected 3.9% polar-cap fraction is 2.6× the uniform-null expectation...". This phrasing is ambiguous. It could be read as the polar caps constituting 3.9% of the sky. The calculation in Table I footnote `†` is correct: 17 rejected objects (3.9% of 436 anomalies) fall in the 10°-radius polar caps (1.52% of the sky), representing a 2.6x overdensity. The main text should be as clear as the footnote.
    *   **Required Fix:** Rephrase the sentence in Sec. II D to clarify. For example: "...the 17 rejected anomalies (3.9% of the total) are concentrated in the 10°-radius ecliptic polar caps, an overdensity of 2.6× the expectation from a uniform sky distribution."

*   **P3-m2: Unreproducible Wilson Confidence Interval**
    *   **Section:** III A (p. 8)
    *   **Problem:** The text quotes Wilson 95% binomial CIs for galaxy and QSO anomaly rates. For galaxies, it states `0.75% ± 0.02% on ~4.9 × 10^6 GALAXY-SPECTYPE spectra`. A standard normal approximation for this large sample size (p=0.0075, N=4.9e6) yields a 95% CI of `± 1.96 * sqrt(p(1-p)/N) ≈ ±0.0076%`, which is a factor of 2.6 smaller than the quoted `±0.02%`. While the Wilson score interval is more precise, it should not produce such a large discrepancy for this N.
    *   **Required Fix:** Please verify the calculation for the quoted confidence intervals. If the numbers are correct, briefly state the reason for the larger-than-expected interval (e.g., if it accounts for sample variance not just binomial error). Otherwise, correct the values.

*   **P3-m3: Inconsistent Terminology for DESI Anomaly Cut**
    *   **Section:** III A (p. 6)
    *   **Problem:** The text states: "The headline 195,829 DESI anomaly count is the top-1% score-cut of the full 22.5-M-spectrum scan...". This is incorrect. As stated correctly in Table I and its caption, the DESI cut is an absolute threshold at `S > 5.0`, which results in an anomaly rate of 0.87%, not a top-1% selection.
    *   **Required Fix:** Correct the sentence to read: "The headline 195,829 DESI anomaly count results from applying a fixed canonical-S threshold of S > 5.0 to the full 22.5-M-spectrum scan, yielding a 0.87% anomaly rate."

*   **P3-m4: Recurring Data Provenance Issue**
    *   **Section:** II B (p. 3), III G (p. 12), Data availability (p. 23)
    *   **Problem:** The paper repeatedly notes that the exact preprocessing script for the Gaia DR3 analysis was not recovered from backups and that the specification is "lineage-inferred" from a successor script. While the transparency is commendable, this is a notable reproducibility flaw.
    *   **Required Fix:** No action is required beyond the existing disclosure, but the authors should ensure that all released data products related to the Gaia tier are clearly marked with this provenance caveat. The current text does this well; this finding is to emphasize its importance.

#### NIT

*   **P3-N1: Minor Typo in Figure 11 Caption**
    *   **Section:** Appendix C (p. 25)
    *   **Problem:** In the caption for Figure 11, the last sentence reads: "absolute σ(fNL) values should be read from §V."
    *   **Required Fix:** The symbol `σ(fNL)` is used throughout the paper. The caption should use the same symbol for consistency. Change `σ(NL)` to `σ(fNL)`.

---
## Summary recommendation

**MINOR REVISIONS**

This is an excellent and substantial paper that represents a major advance in the application of anomaly detection in astronomy. The analysis is careful, the validation is comprehensive, and the conclusions are stated with appropriate caution. The work is of high quality and will be of significant interest to both the cosmology and astronomy communities. The required revisions are minor and primarily aimed at improving clarity and ensuring that the abstract fully reflects the nuanced conclusions presented in the main text. Upon addressing these points, the paper will be a landmark contribution to the field and I will be pleased to recommend it for publication.