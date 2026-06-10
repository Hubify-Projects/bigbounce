# P3 R23conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.80.pdf` md5=? pages=?
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2068 chars)
**Wall time**: 160.5s

---

Here is a complete referee report for the submitted paper.

---
**Referee Report: "Spectrally Unusual Sources at Scale..." by Houston Golden**

**PRD Submission ID:** [Assigned by system]

This paper presents a large-scale, multi-survey catalog of astronomical anomalies detected using an autoencoder framework. The work spans seven major astronomical archives (DESI, SDSS, LAMOST, eROSITA, Planck, Gaia, NEOWISE) and identifies 378,280 unique anomalies. The authors develop a "Path-C" methodology involving native per-survey retraining to overcome cross-survey domain-shift issues, which they demonstrate effectively. The paper uses the resulting catalog for several scientific applications, including identifying high-redshift QSO candidates, assessing the genuine novelty of sources, and forecasting constraints on primordial non-Gaussianity (fNL).

The scope of the work is impressive, and the methodological rigor in validating the anomaly detection process is a significant strength. The "Path-C" rebuild protocol and the transparent discussion of its successes (e.g., for SDSS) and failures (e.g., for LAMOST) provide valuable lessons for the community. The cosmological applications, while secondary, demonstrate the potential utility of such catalogs.

However, the paper contains a critical calculation error in one of its key cosmological results, several significant presentation issues that obscure results, and a number of minor errors that must be addressed before it can meet the standards for publication in Physical Review D.

---
### **Detailed Findings**

#### **ESSENTIAL Revisions**

**P3-E1: Critical error in fNL forecast improvement calculation.**
*   **Location:** Abstract (p. 1), Section V.b (p. 12), Section VI.D (p. 15).
*   **Problem:** The paper repeatedly claims a "7.9% improvement" in the constraint on fNL from the multi-tracer analysis using the empirically measured bias. The stated inputs are a single-tracer baseline of σ(fNL)std = 8.98 and a multi-tracer forecast of σ(fNL) = 8.14. The fractional improvement is (8.98 - 8.14) / 8.98 = 0.0935, which is a **9.4%** improvement, not 7.9%. This error appears in the abstract and is central to the summary of the cosmological application.
*   **Fix:** Recompute the percentage improvement and correct it in all instances (abstract, main body, and any other relevant sections). The correct value is 9.4%.

**P3-E2: Internal version-control/bookkeeping note present in a final table.**
*   **Location:** Table V, footnote † (p. 18).
*   **Problem:** The footnote for the Planck CMB training time reads: "...no figure is quoted (an earlier draft listed 10.6 s, which is inconsistent with a ~100-epoch convolutional run and has been withdrawn)". This is an internal author's note that is entirely inappropriate for a published scientific paper. It undermines the professional presentation of the work.
*   **Fix:** Remove the parenthetical comment about an "earlier draft". The footnote should simply state that the exact wall-clock time was not preserved in the run logs and therefore is not reported.

**P3-E3: Inconsistent and incorrect notation for squared quantities in equations.**
*   **Location:** Abstract (p. 1), Section V.b (p. 12), Section VI.D(i) (p. 15), Table IV(i) (p. 16).
*   **Problem:** The Fisher forecast equation is consistently written with the square inside the parentheses, e.g., `1/σ(fNL)²`. The correct notation is `1/σ²(fNL)` or `1/[σ(fNL)]²`. In Table IV, it is further mistyped as `1/6(fNL)²`. This recurring notational error is unacceptable.
*   **Fix:** Correct the notation in all four identified instances to `1/σ²(fNL)` or an equivalent unambiguous form.

#### **MAJOR Revisions**

**P3-M1: Ambiguous presentation of LAMOST anomaly counts.**
*   **Location:** Table I (p. 8) and Section III.D (p. 6).
*   **Problem:** Table I lists the LAMOST cross-transfer anomaly count (`Nanom`) as 44,075. However, the final Path-C catalog incorporates a "top-113,342 native slice" for LAMOST, which is used to compute the final unique anomaly count of 378,280. Meanwhile, the text highlights a 21.5x rate compression down to 2,054 anomalies at a stricter S>5 threshold. This three-way distinction (44,075 vs. 113,342 vs. 2,054) is confusing. While the footnotes attempt to clarify, the main table is misleading at a glance.
*   **Fix:** Add a dedicated column to Table I for the "Final Catalog Count" used in the Path-C unique total, separate from the `Nanom` (cross-transfer) column. This would show 195,829 for DESI, 77,905 for SDSS, 113,342 for LAMOST, etc. This makes the origin of the final 378,280 count transparent directly from the table. The footnotes can then elaborate on the threshold choices for each survey.

**P3-M2: The distinction between "SIMBAD-unmatched" and "genuine novelty" is not sufficiently emphasized.**
*   **Location:** Abstract (p. 1), Section IV.A (p. 9), Figure 6 (p. 10).
*   **Problem:** The abstract leads with high SIMBAD-unmatched fractions (e.g., 99% for DESI), but the true, physically meaningful "genuine novelty fraction" is much lower (~17.8%). While Section IV.A does an excellent job of explaining this crucial distinction, the abstract and figure captions could be misinterpreted by a casual reader. The term "SIMBAD novelty fraction" in Figure 6 is particularly misleading.
*   **Fix:** In the abstract, state the genuine novelty fraction (17.8%) *before* the per-survey SIMBAD-unmatched rates to prioritize the more robust result. In the caption for Figure 6, change "SIMBAD novelty fraction (%)" to "Fraction of anomalies absent from SIMBAD (%)" and explicitly state in the caption that this is a database-coverage metric and the catalog's genuine novelty rate is ~17.8%.

**P3-M3: Placeholder date of publication.**
*   **Location:** Title block (p. 1).
*   **Problem:** The paper is dated "(Dated: June 2026)". This is presumably a placeholder. While not a scientific error, it is unprofessional for a final submission.
*   **Fix:** Replace "June 2026" with the current month and year of submission, or remove the date entirely as it will be set by the journal upon publication.

#### **MINOR Revisions**

**P3-m1: Missing subscript in abstract.**
*   **Location:** Abstract (p. 1).
*   **Problem:** The Savage-Dickey Bayes factor is written as "BMB/SMBHB".
*   **Fix:** Correct to the proper subscripted form, `B_MB/SMBHB`.

**P3-m2: Unclear scope of the "recommended catalog-grade subset".**
*   **Location:** Abstract (p. 1).
*   **Problem:** The abstract recommends a subset of "~265,000 unique entries" but does not explicitly state which surveys are included or excluded *at that point in the text*. The reader has to infer it from the subsequent parenthetical about LAMOST.
*   **Fix:** Reword for clarity, for example: "...the recommended catalog-grade subset is ~265,000 unique entries, which includes all surveys except the exploratory LAMOST tier..."

**P3-m3: Potentially confusing language regarding ACT DR6.**
*   **Location:** Abstract (p. 1) and Section II (p. 2).
*   **Problem:** The abstract says "ACT DR6 quarantined as a cross-transfer artifact". Page 2 says "catalog counts appear as 378,080+200 = 378,280 throughout to distinguish point-source detections from CMB map-patch sky-regions". This parenthetical is slightly confusing as it doesn't mention ACT. The quarantine status of ACT is handled well overall, but this specific sentence could be clearer.
*   **Fix:** The parenthetical on page 2 is not strictly necessary and could be removed to avoid confusion. The primary count breakdown (point-source vs. map-patch) is well-explained in Table I and its footnotes.

**P3-m4: Typo in figure caption.**
*   **Location:** Figure 3 caption (p. 6).
*   **Problem:** The caption states "...where uval and oval are the mean and standard deviation...".
*   **Fix:** These should be μ_val and σ_val to match standard statistical notation and avoid confusion with the letters 'u' and 'o'.

#### **NIT-PICKS (Cosmetic)**

**P3-N1: Inconsistent use of "Path-C".**
*   **Location:** Throughout.
*   **Problem:** The paper sometimes uses "Path-C" and sometimes "Path-C rebuild".
*   **Fix:** Standardize to one form, preferably "Path-C protocol" or "Path-C methodology" for consistency.

**P3-N2: Awkward phrasing in Figure 1 caption.**
*   **Location:** Figure 1 caption (p. 2).
*   **Problem:** The phrase "lie on or near the high-score structures" is slightly informal.
*   **Fix:** Rephrase to "are concentrated within or near the high-score structures".

---
### **Summary recommendation**

**MAJOR REVISIONS**

This is a substantial and valuable contribution, presenting a large, well-validated anomaly catalog with clear potential for discovery. The methodological work, particularly the native-retrain protocol to handle domain shift, is sound and provides an important example for future large-scale survey analyses.

However, the paper is marred by a critical and easily correctable calculation error in its main cosmological forecast, which must be fixed. Furthermore, several major presentation issues, including a leaked author's note in a table and ambiguous reporting of key numbers (e.g., LAMOST counts, novelty fractions), currently prevent the work from meeting the high standards of clarity and professionalism required by Physical Review D.

Once the authors have addressed the ESSENTIAL and MAJOR points listed above, particularly the fNL improvement calculation, the paper will be a strong candidate for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from the second, more rigorous review pass.

---
### **Additional Findings from Second Review Pass**

**MINOR Revisions**

**P3-m5: Broken internal reference regarding DESI sample scope.**
*   **Location:** Section III.A, page 4.
*   **Problem:** The text states, "...per-class anomaly rates and SIMBAD-novelty fractions reported below refer to the ~6.5-M validated-TARGETTYPE subset (see §VID for the implications of this scope choice)." Section VI.D ("Path-C Rebuild Residual Caveats") does not appear to contain a discussion of the implications of this choice. The reference is either broken or points to a non-existent discussion.
*   **Fix:** Either add the promised discussion to Section VI.D or, more likely, remove this dangling and unfulfilled cross-reference.

**P3-m6: Incorrect internal reference for false-match rate.**
*   **Location:** Section III.A, page 4.
*   **Problem:** The text calculates the expected 5" random false-match rate and cites `(§IV A)`. The discussion of SIMBAD cross-matching and novelty is in §IV.A, but the specific calculation of the false-match rate (`P_false`) is in the following subsection, §IV.B.
*   **Fix:** Correct the cross-reference to point to §IV.B.

**P3-m7: Incorrect internal reference in figure caption.**
*   **Location:** Figure 3 caption, page 6.
*   **Problem:** The caption defines the anomaly score `S` and cites `(§IID)` for the definition. Section II.D describes the "Path-C Rebuild Methodology". The actual definition of `S` is given in Section II.B ("Training and Scoring"), specifically in subsection §II.B.a and Equation 2.
*   **Fix:** Correct the cross-reference to point to §II.B.a.

**P3-m8: Typo in figure caption cross-reference.**
*   **Location:** Figure 12 caption, page 20.
*   **Problem:** The caption explains the Z-arm sub-score `rz` and cites `(§IIIB)`. The relevant discussion of the high-z QSO candidates and their Z-arm dominance is in Section III.B. The use of a Roman numeral appears to be a typo.
*   **Fix:** Correct the cross-reference to §III.B.