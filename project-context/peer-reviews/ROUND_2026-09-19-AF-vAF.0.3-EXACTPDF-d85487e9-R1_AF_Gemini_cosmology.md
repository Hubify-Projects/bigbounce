# AF ROUND_2026-09-19-AF-vAF.0.3-EXACTPDF-d85487e9-R1 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-3.1-pro-preview`
**Input PDF**: `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.pdf` sha256=d85487e97f6856040d12ef78b78ab57ce4d74fc6420d6664013cdc9651c17b41 pages=15
**Review packet(s)**: `bb9fd23be9b4c6b82f9ce125b8fd99ad497bdb65ce6ec07be91e0a256e3ccdc5, f81b691830b926a18a4280930460f752957ba1b6013c348ee7209fca02a93e69`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2230 chars)
**Wall time**: 271.3s

---

Here is a comprehensive referee report for the manuscript, evaluated against the ApJS standards for a candidate catalogue and method paper, with specific attention to the requested review profile.

### Referee Report

**General Comments**
The manuscript presents a highly rigorous, provenance-sealed anomaly-score catalogue of DESI DR1 spectra. The methodological transparency, the cryptographic binding of the data products to the inference code, and the inclusion of a machine-checkable validation contract represent a gold standard for reproducibility in astronomical data releases. The mathematical execution of the anomaly scoring and the statistical bounds (e.g., the Wilson score intervals for the recovery benchmark) are flawless. 

However, the manuscript currently falls short of publication standards due to several critical omissions. It explicitly defers the most important physical interpretation of its catalogue to an "open test," contains uncomputed and uncited cosmological claims, leaves explicit placeholders in the text, and fails to propagate a crucial statistical caveat from the body to the abstract. Furthermore, the title does not reflect the paper's own null-recovery conclusions. These issues must be resolved before the paper can be accepted.

---

### Findings

**AF-E1: Title lacks required null/no-discovery framing**
*   **Section & Page:** Title, page 1
*   **Specific problem:** The title reads: *"A provenance-sealed anomaly-score candidate catalogue of DESI DR1 spectra: selection, validation, and a descriptive taxonomy"*.
*   **Required fix:** As requested by the review board's focus criteria, and to prevent the catalogue from being misconstrued as a discovery sample, the title must overtly carry the null/no-discovery or infrastructure framing that the paper itself concludes. Revise the title to explicitly include terms such as "null recovery," "infrastructure," or "no discovery."

**AF-E2: Abstract omits critical statistical power caveat (Pattern-045)**
*   **Section & Page:** Abstract, page 1
*   **Specific problem:** The abstract claims: *"A known-object recovery benchmark against five reference classes recovers no class at the pre-declared bar..."* However, Section V.D (page 6) states: *"the reference footprints are small compared with the parent survey, so the test has little power for rare classes: the 95% upper limit on the recovery of superluminous-supernova hosts is 12.5%, which excludes almost nothing."*
*   **Required fix:** The abstract claim is currently stronger than the body's calibrated statement. You must add the caveat regarding the low statistical power (specifically noting the 95% upper limit of 12.5% on rare classes) directly to the abstract so readers understand the limits of the null recovery.

**AF-E3: Abdication of the blue-arm residual analysis**
*   **Section & Page:** Section V.C, page 6
*   **Specific problem:** The paper identifies that the anomaly score is driven almost entirely by the $b$-camera residual ($\rho_s = +0.527$). It then states: *"Two readings survive this measurement, and the data here do not separate them: blue-end sky-subtraction and calibration residuals... or genuine spectral behaviour... This is the single most consequential open question about the catalogue... It is also cheap to test on public data, and we name that test as OT-3 in Sec. VII C rather than speculating here."*
*   **Required fix:** A catalogue paper cannot defer the "single most consequential open question" about its own selection metric to an open test for the reader to perform, especially when the likely origin is a known instrumental artifact. You must execute OT-3, determine whether the $b$-camera drive is instrumental or astrophysical, and report the results in this manuscript.

**AF-E4: Editorial placeholders left in the manuscript**
*   **Section & Page:** Section VII.C (page 13) and Section IX (page 13)
*   **Specific problem:** The text contains explicit drafting placeholders: 
    1. `[PLACEHOLDER: run and report per-class injection recovery with the exact model and substrate named]`
    2. `[PLACEHOLDER: Zenodo DOI for the public deposit]`
*   **Required fix:** Execute the injection recovery test and report the results. Mint the Zenodo DOI and insert it. Remove all placeholder text.

**AF-E5: Uncomputed and uncited cosmological claims (Pattern-048 / Standalone-Reader Test)**
*   **Section & Page:** Section VIII, page 13
*   **Specific problem:** The text asserts: *"A local-shape primordial non-Gaussianity of the amplitude predicted by a matter-dominated contraction shifts the z ≈ 10–12 massive-halo abundance by roughly 6–15%... a factor-of-two effect would require |fNL| ~ 30, far outside current constraints."*
*   **Required fix:** This is a load-bearing cosmological claim that is neither supported by an in-paper computation nor backed by a citation. You must either provide the explicit derivation/computation for these specific abundance shifts and the $|f_{NL}|$ constraint, or provide the exact literature citations from which these numbers are drawn. Additionally, define the symbol $f_{NL}$, which is currently used without definition.

**AF-M1: Intentional release of defective data tables**
*   **Section & Page:** Section V.E, page 7 and Section IV.C, page 4
*   **Specific problem:** The authors openly state that the released tables contain "defects," including unpopulated redshift columns, an empty `residual_kurtosis` column, and absent flux inverse variances. The text states: *"Two defects in the released tables are recorded openly and must be repaired before public deposit."*
*   **Required fix:** A paper cannot be accepted for publication while its accompanying data products are admittedly defective and missing critical columns (especially flux inverse variances, which are required to compute detection significance). Repair all four listed defects in the data release and update the manuscript to reflect the complete, repaired schema.

**AF-N1: Internal version-history tags in the manuscript**
*   **Section & Page:** Page 1, below author affiliations
*   **Specific problem:** The date line includes an internal version tag: `(vAF.0.3)`.
*   **Required fix:** Remove internal version-history tags from the publication-ready manuscript.

---

### Summary recommendation
**MAJOR REVISIONS**

**Justification:**
The manuscript is methodologically exceptional, featuring a level of cryptographic provenance and reproducibility rarely seen in astronomical literature. The statistical derivations (e.g., the Wilson score intervals) are perfectly executed. However, the paper is currently incomplete. It contains explicit drafting placeholders, makes uncited cosmological claims, intentionally releases defective data tables with missing inverse variances, and—most critically—defers the fundamental physical interpretation of its primary anomaly metric (the $b$-camera residual) to an unexecuted "open test." Once the authors execute OT-3, repair the data tables, remove the placeholders, and align the abstract and title with the paper's null-recovery reality, this will be a benchmark publication for ApJS.

---

## PASS 2 — self-critique findings (what initial review missed)

[AF-A1: Contradictory claim regarding correlation signs]
*   **Section & Page:** Section V.B, page 6
*   **Specific problem:** The text states: *"At n = 1,244 four of these are formally significant and all are negligible in size; the significant ones are negative..."* The five correlations listed are S/N (+0.058), exposure time (-0.076), TSNR2_LRG (-0.093), TSNR2_QSO (-0.096), and r-band flux (-0.016, p=0.56). The four significant correlations include S/N, which is positive (+0.058) and statistically significant at $n=1,244$ ($p \approx 0.041$). 
*   **Required fix:** Correct the text to accurately reflect that one of the statistically significant correlations (S/N) is positive, invalidating the claim that all significant correlations are negative.

[AF-A2: Arithmetic error in validation contract pass count]
*   **Section & Page:** Section V.A, page 6 and Table VI, page 8
*   **Specific problem:** The text in Section V.A claims: *"Thirteen requirements pass."* However, a direct count of the outcomes in Table VI reveals exactly 11 requirements with a "PASS" outcome (V1, V2, V3, V3b, V4, V5, V6, V7, V8, V9, V10). The remaining 5 of the 16 requirements are marked as REPORTED (V11, DEFECT-3), STRUCTURED-BUT-WEAK (V12), or FAIL (DEFECT-1, DEFECT-2). 
*   **Required fix:** Change "Thirteen requirements pass" to "Eleven requirements pass" to match the explicit outcomes listed in Table VI.

[AF-B1: Schema table omits columns explicitly discussed in the text]
*   **Section & Page:** Table IV (page 5) vs. Section V.E (page 7)
*   **Specific problem:** Table IV is presented as the complete "Released column schema." However, Section V.E explicitly identifies two columns that are present in the released tables but are defective (empty/unpopulated): `SUBTYPE` and `residual_kurtosis`. The text correctly distinguishes these from truly "absent" columns (like flux inverse variances). Despite existing in the released files, neither `SUBTYPE` nor `residual_kurtosis` is listed in Table IV.
*   **Required fix:** Add `SUBTYPE` (under the DESI pipeline group) and `residual_kurtosis` (under the anomaly group) to Table IV so that the published schema accurately reflects the columns present in the released data files.