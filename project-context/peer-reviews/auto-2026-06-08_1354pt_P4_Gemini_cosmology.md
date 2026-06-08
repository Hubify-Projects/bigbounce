# P4 auto-2026-06-08_1354pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (1931 chars)
**Wall time**: 134.3s

---

## Referee Report: P4

This paper presents a multi-survey, equivariance-corrected analysis of galaxy chirality using a sample of 3.2 million spiral galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of a large-scale chirality dipole, which constrains isotropy-breaking axial-vector modes. The analysis is exceptionally thorough, employing a modern deep-learning pipeline (a Vision Transformer) hardened against systematics, a clear hierarchy of statistical estimators, and a comprehensive suite of null tests. The authors carefully distinguish the parity-even dipole signal from parity-odd observables and correctly interpret their null result within this theoretical framework. A significant portion of the paper is dedicated to diagnosing and quantifying a systematic signal on a specific survey mask, which is convincingly attributed to monopole-to-dipole leakage through the mask geometry rather than a cosmological signal. The paper is well-written, transparent about its methods and limitations, and provides public access to the catalog, model, and code, which is commendable.

The work is of high quality and suitable for publication in Physical Review D, pending revisions to address several issues ranging from essential corrections of metadata and internal language to major clarifications in tables and text.

---

### Findings

#### ESSENTIAL

*   **P4-E1**
    *   **Section/Page:** Byline, p. 1
    *   **Problem:** The paper is dated "June 2026", a future date.
    *   **Fix:** Replace with the correct submission date.

*   **P4-E2**
    *   **Section/Page:** IV D, p. 4
    *   **Problem:** The text contains version-history language: "The canonical-mask direct-MC l = 1 value of +3.64σ and the local hemisphere maximum of 3.05σ were interpreted in earlier paper versions as mask-geometric leakage...". This internal review-process language is inappropriate for a final publication.
    *   **Fix:** Rephrase to be a direct statement about the analysis. For example: "The +3.64σ direct-MC l=1 value on the canonical mask and the 3.05σ local hemisphere maximum are potential signatures of mask-geometric leakage from the global monopole."

*   **P4-E3**
    *   **Section/Page:** Footnote 1, p. 4
    *   **Problem:** The footnote contains explanatory language that refers to previous drafts: "The previous wording 'Binomial(ntotal, pglobal)' PCW was ambiguous...".
    *   **Fix:** Remove this meta-commentary. The current, clearer explanation is sufficient.

*   **P4-E4**
    *   **Section/Page:** Data Availability, p. 9
    *   **Problem:** The catalog release tag is given as "v2026.04", another future date.
    *   **Fix:** Correct the release tag to the actual version at the time of publication.

#### MAJOR

*   **P4-M1**
    *   **Section/Page:** IV B, p. 4
    *   **Problem:** The text states: "The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant -0.53% demonstrates the dominance of the equivariant TTA processing." These percentage values (+2.05% and -0.53%) are inconsistent with the values reported in Table II for Catalog A (raw) and Catalog C (equivariant), which are +0.79% and -0.26%, respectively.
    *   **Fix:** Reconcile this discrepancy. Either the text or Table II is incorrect. If the numbers in the text refer to a different quantity, this must be explicitly defined and clarified.

*   **P4-M2**
    *   **Section/Page:** Table III, p. 5
    *   **Problem:** For the bandpower results (rows 2-6, `leff=4` through `leff=24`), the "Significance (σ)" column is presented without the corresponding uncertainty (`σ_null`) for each bandpower. This makes the significance values unverifiable. The significance is defined as `(C_meas - <C_null>) / σ_null`, and all three quantities on the right-hand side should be available to the reader.
    *   **Fix:** Add a column to Table III for the uncertainty on the null power spectrum, `σ_null(C_l)`, for each reported bandpower.

*   **P4-M3**
    *   **Section/Page:** Table I, p. 4
    *   **Problem:** Estimator (iv), "hemisphere LEE (MC)", reports `PLEE ≤10⁻⁴`. This is a raw p-value before look-elsewhere-effect (LEE) correction. However, the main text (Appendix C, p. 8) clarifies that the post-LEE significance is `< 1σ`. A reader looking only at Table I could misinterpret this as a highly significant detection.
    *   **Fix:** The table caption or a footnote attached to this entry must clarify that this is the *pre-correction* p-value and direct the reader to Appendix C for the final, corrected significance.

#### MINOR

*   **P4-m1**
    *   **Section/Page:** VI B, p. 6
    *   **Problem:** The text states: "...the parity-odd signal lives in the l = 0 monopole and even-l multipoles." The statement about "even-l multipoles" is potentially misleading. The angular power spectrum `C_l` of a scalar or pseudoscalar field is a parity-even quantity for all `l`. Parity violation in two-point statistics manifests in cross-correlation spectra that are odd under parity, such as `C_l^TB` and `C_l^EB` in CMB polarization, not in the auto-power spectrum of chirality. While parity-violating physics can source a monopole (`l=0`), the claim about other multipoles needs to be more precise.
    *   **Fix:** Please clarify this statement. A more accurate phrasing would be that parity-odd signals appear in the monopole and in higher-order correlation functions (e.g., the bispectrum) or specific cross-correlation spectra, which are outside the scope of this paper's `C_l` analysis.

*   **P4-m2**
    *   **Section/Page:** II (p. 2) and VI B (p. 6)
    *   **Problem:** The paper claims to be inconsistent with Shamir's ~3% signal "by a factor of ~ 6-12". This factor is not explicitly derived and seems to depend on whether one compares to the 1σ or 3σ sensitivity. The comparison is valid but the range is vague.
    *   **Fix:** State the basis for this factor more clearly. For example: "This null result is inconsistent with a ~3% signal, which would have been detected at >12σ based on our 1σ sensitivity of ~0.25%, and disfavors such models by a factor of 4 relative to our 3σ detection threshold of 0.75%."

*   **P4-m3**
    *   **Section/Page:** Table IV, p. 5
    *   **Problem:** The z-scores reported in the final column are not precisely reproducible from the rounded data and null values provided. For the `pseudo-C(l=1)` row, the calculation `(1.696 - 1.685) / 0.007` yields `1.57`, not `1.68`. For the `Hemisphere max|A|` row, `(3.48 - 1.69) / 0.41` yields `4.37`, not `4.42`. While this is likely due to rounding of intermediate values, it hinders reproducibility.
    *   **Fix:** Provide the values in the table with enough precision for the z-score calculation to be verified, or ensure the z-score is correct for the given rounded values.

---

## Summary recommendation

**MAJOR REVISIONS**

This is an excellent, rigorous, and important contribution to the field. The analysis is of very high quality, and the conclusions are well-supported. The paper sets a high standard for systematic control in this type of measurement. The recommendation for major revisions is not due to any fundamental flaw in the scientific analysis but reflects the need to correct several significant (though easily fixable) issues, including metadata errors, internal-review language, numerical inconsistencies between text and tables, and omissions in a key data table. Once these revisions are made, the paper will be a strong candidate for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from the second, more rigorous review.

---

### New Findings

#### MAJOR

*   **P4-M4**
    *   **Section/Page:** Table II, p. 4
    *   **Problem:** The "Dev. (σ)" column, which reports the significance of the global CW fraction excess, is not arithmetically consistent with the other columns in the table. Re-computing the values `(fcw - 0.5) / σ` yields significant discrepancies:
        *   Tier A (raw): `(0.5079 - 0.5) / 0.000279 = 28.3`, not `28.8`.
        *   Tier B (calibrated): `(0.504 - 0.5) / 0.000279 = 14.3`, not `14.6`.
        *   Tier C (equivariant): `(0.4974 - 0.5) / 0.000279 = -9.3`, but the table reports `9.5`. This is both a sign error and a magnitude error.
    *   **Fix:** The values in the "Dev. (σ)" column must be re-calculated and corrected to be consistent with the reported `fcw` fractions and uncertainties. The sign for Tier C must also be corrected.

#### MINOR

*   **P4-m4**
    *   **Section/Page:** III, p. 3
    *   **Problem:** The text refers to a "sub-percent systematic floor in Sec. IV C". Section IV C contains the main dipole analysis and does not define or discuss a systematic floor. This concept is more relevant to the sensitivity discussion in Section VI A. The cross-reference is incorrect and potentially confusing.
    *   **Fix:** Correct the cross-reference to point to the appropriate section (likely VI A) or remove the phrase if it is not essential at that point in the text.

*   **P4-m5**
    *   **Section/Page:** IV A, p. 3
    *   **Problem:** The text makes the unquantified claim: "The spiral fraction is consistent with magnitude-limited survey expectations." This is a weak hedge without a supporting citation or a quantitative value for the expectation.
    *   **Fix:** Either provide a citation and a quantitative expected value for the spiral fraction in a DESI-like survey to support this claim, or remove the sentence.