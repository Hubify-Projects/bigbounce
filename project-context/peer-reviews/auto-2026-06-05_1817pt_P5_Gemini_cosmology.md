# P5 auto-2026-06-05_1817pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3935 chars)
**Wall time**: 129.0s

---

## Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals"

This manuscript presents a detailed investigation into the potential dependence of spiral galaxy chirality on the large-scale structure environment. The authors cross-match a large chirality catalog with DESI DR1 data, perform a cosmic-web classification, and test for variations in the clockwise (CW) fraction across voids, walls, filaments, and clusters. The headline result is a null detection of environmental dependence, with observed deviations being consistent with a previously identified catalog-wide systematic monopole and statistical noise. The analysis is comprehensive, featuring an impressive array of robustness checks, including variations in analysis parameters, cross-validation against independent void catalogs (DESIVAST) and environment classifiers (Tempel+2014 FoF, ASTRA), and detailed systematic-error investigations.

The work is thorough and the conclusions appear well-supported by the data. The extensive checks for systematics, particularly the tracer-program decomposition and the DESIVAST-anchored re-analysis, are commendable and significantly strengthen the paper's claims. However, the manuscript requires significant revision before it can be considered for publication in Physical Review D. The primary issues relate to the clarity of the narrative structure, several critical errors in the abstract that misrepresent the main results, and a number of minor technical inaccuracies.

Below is a detailed list of required revisions.

---

### ESSENTIAL Revisions

**P5-E1: Abstract — Critical sign error in primary result**
*   **Location:** Page 1, Abstract, Robustness section.
*   **Problem:** The abstract states for the DESIVAST-anchored re-projection: "...returns `f_cw^void = 0.4964` vs `f_cw^non-void = 0.4971`, `Δf_cw = 0.0007`...". The calculation `0.4964 - 0.4971` yields `-0.0007`. The sign is incorrect in the abstract. This is the paper's primary quantitative result from its most robust test, and it must be stated correctly.
*   **Fix:** Change `Δf_cw = 0.0007` to `Δf_cw = -0.0007`.

**P5-E2: Abstract — Inconsistent statistical significance**
*   **Location:** Page 1, Abstract, "Headline result" section.
*   **Problem:** The abstract quotes the CW fraction for filament as `0.4980 (filament; n=408,187, -2.61σ)`. However, a direct calculation using the numbers from Table II (page 5), which are `n=408,187` and `ncw=203,261` (yielding `f_cw = 0.49796...`), gives `σ = -2.606`. A calculation using the rounded `f_cw=0.4980` gives `σ = -2.556`. The value in the abstract is inconsistent with the primary table in the paper and appears to be an error. The abstract must accurately reflect the calculations from the main body.
*   **Fix:** Recompute the sigma value for the filament class based on the precise numbers in Table II and update the abstract. The value should be `-2.61σ` (or `-2.606σ` if more precision is desired), and the `f_cw` should be reported with enough precision to match (e.g., 0.4980 is acceptable, but the sigma must be correct).

**P5-E3: Unconventional Manuscript Dating**
*   **Location:** Page 1, Title block.
*   **Problem:** The paper is dated "June 4, 2026". Several references are also cited with 2026 dates. While these may be preprints, dating the manuscript itself in the future is highly unconventional for a journal submission and may cause confusion.
*   **Fix:** The date should be changed to the date of submission.

### MAJOR Revisions

**P5-M1: Narrative Structure and "Post-Hoc" Framing**
*   **Location:** Page 5, Section V B, "Primary vs. secondary analysis paths".
*   **Problem:** The paper's structure is confusing. It presents the V-Web analysis first, then declares it a "secondary diagnostic path" and designates the DESIVAST analysis (Section VIII) as the "primary analysis path". This declaration is made "post-hoc", which, while honest, makes for a disjointed and difficult-to-follow narrative. The V-Web analysis is crucial as it reveals the systematics (e.g., the unreliability of the V-Web void class at low-z, the target-program dependence) that motivate the cleaner DESIVAST-based analysis.
*   **Fix:** The paper should be restructured for a more linear and logical flow. I recommend the following narrative:
    1.  **Introduction:** State the scientific question.
    2.  **Initial Analysis (V-Web):** Present the V-Web classification as the first, most direct approach. Report the results from Table II.
    3.  **Systematic Investigation:** Show that the V-Web results are dominated by systematics. Use the within-class density checks, the tracer-program decomposition (the bright/dark sign-flip), and the direct cross-check against DESIVAST (0/6 V-Web "voids" are real voids) to demonstrate the need for a more robust method.
    4.  **Primary Analysis (DESIVAST):** Motivated by the systematics found, introduce the DESIVAST-anchored analysis as the definitive test. Present the results from Tables VII and VIII as the paper's main, cleaned result.
    5.  **Robustness and Cross-Checks:** Consolidate all other checks (Phase 2 sweep, Tempel+2014, ASTRA, HEALPix scans) into a subsequent section that demonstrates the robustness of the primary null result.
    This restructuring would transform the paper from a "garden-of-forking-paths" report into a compelling scientific detective story, greatly improving its impact and readability.

### MINOR Revisions

**P5-m1: Ambiguous Internal Referencing**
*   **Location:** Page 12, Section VIII F.
*   **Problem:** The text refers to the "P5 matched-spiral catalog" and the "P4 catalog-level monopole". "P4" is defined as "Paper IV", but "P5" is not defined anywhere in the text. This appears to be an internal project tag that has leaked into the manuscript body (the reviewer metadata also contains "Paper tag: P5").
*   **Fix:** Remove the "P5" designation and clarify what catalog is being referenced (e.g., "the matched-spiral subsample used in this work").

**P5-m2: Typographical error for sigma**
*   **Location:** Page 1, Abstract.
*   **Problem:** The text states "...none reach 30 after look-elsewhere correction."
*   **Fix:** This should be "3σ". This typo also appears on page 17 in the systematics summary. Please correct all instances.

**P5-m3: Inconsistent terminology for HEALPix analysis**
*   **Location:** Page 13, Section VIII F, "Quantitative null correlation".
*   **Problem:** The text states the correlation is measured "across all `n_both = 727` HEALPix pixels". The caption for Figure 6 states "The Pearson correlation across the `n_pix = 727` pixels...".
*   **Fix:** Use consistent terminology. "valid pixels" or simply "pixels" would be clearer than `n_both` or `n_pix`.

**P5-m4: Incorrect formula for Bonferroni threshold**
*   **Location:** Page 4, Equation (2).
*   **Problem:** The formula for the Bonferroni-corrected significance threshold is given as `σ_Bonf = sqrt(2) * erfc⁻¹(α/K)`. For a two-sided test with family-wise error rate α, the per-test p-value threshold is `α/K`, which corresponds to a tail probability of `α/(2K)`. The correct formula relating the z-score to the one-sided p-value `p` is `z = sqrt(2) * erfc⁻¹(2p)`. The formula in the paper is therefore incorrect for a two-sided test. The calculated numerical value (`≈3.09` for K=5, α=0.01) is correct for a two-sided test, but the formula that produces it is wrong.
*   **Fix:** Correct the formula in Equation (2). A clearer, equivalent expression would be `Φ⁻¹(1 - α/(2K))`, where `Φ⁻¹` is the inverse of the standard normal CDF. Alternatively, correct the argument of the `erfc⁻¹` function to `erfc⁻¹(α/K)`.

### NIT (Cosmetic)

**P5-N1: Rounding in Conclusion**
*   **Location:** Page 18, Section XV, Conclusions.
*   **Problem:** The CW fractions are quoted as `{0.484, 0.503, 0.498, 0.496}`. These are rounded versions of the values in Table II (`0.4836`, `0.5034`, `0.4980`, `0.4963`).
*   **Fix:** For consistency, it would be better to quote the values to the same 4-decimal precision as in the main table and abstract, or to state explicitly that they are rounded.

**P5-N2: Redundant Wording**
*   **Location:** Page 1, Abstract, Robustness section.
*   **Problem:** "...spanning the VoidFinder sphere-growing vs. ZOBOV watershed algorithmic axes): (i) re-running the chirality analysis with DESIVAST-defined voids as the classifier (rather than V-Web) on `n_void = 56,981` matched spirals...". The parenthetical "(rather than V-Web)" is redundant given the context.
*   **Fix:** Suggest removing for conciseness.

---

## Summary recommendation

**MAJOR REVISIONS**

This paper presents a valuable and robust null result on a topic of cosmological interest. The level of detail in the systematic checks is a significant strength. However, the paper is currently hampered by a confusing narrative structure that obscures the logical flow of the investigation, as well as several critical errors in the abstract that misstate the primary findings. Once the narrative is restructured and the numerical errors are corrected, the paper will represent a strong contribution to the field. I recommend that the paper be accepted for publication after these major revisions are addressed.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the second-pass review, containing only new findings not present in the initial report.

================================================================
### ADDITIONAL Revisions (Second Pass)

A more detailed re-examination of the manuscript has revealed several additional issues requiring correction, primarily related to arithmetic accuracy and internal consistency. These are distinct from the points raised in the initial review.

---

### ESSENTIAL Revisions

**P5-E4: Arithmetic errors in projected density analysis table**
*   **Location:** Page 6, Table III.
*   **Problem:** The reported observed sigma values (`σ_obs`) in this table are not arithmetically consistent with the provided CW fractions (`f_cw`) and the per-quintile sample size (`N = 158,327` mentioned in the text and figure caption). For example, for Quintile 1, `f_cw = 0.4976` should yield `σ_obs = -1.86`, but the table lists `-1.94`. Similar discrepancies of varying magnitudes exist for Quintiles 2 and 4. As this table underpins the entire projected density dependence analysis (Section VI C), its numerical accuracy is critical.
*   **Fix:** Re-calculate all `σ_obs` values in Table III from the source `n_cw` and `n` counts for each quintile and ensure they are correct. Update the corresponding `|σ_obs - σ_pred|` column accordingly.

**P5-E5: Broken internal section reference**
*   **Location:** Page 10, Section VIII, paragraph on RSD treatment.
*   **Problem:** The text contains the sentence: "This is in contrast to the V-Web secondary path (§XIII), where the tidal-tensor eigenvalue field is computed from redshift-space...". The compiled manuscript does not contain a Section XIII (it ends at XV). This is a broken cross-reference, likely a remnant from a previous draft structure, that makes it impossible for the reader to find the intended discussion.
*   **Fix:** Correct the reference to point to the actual section where V-Web RSD limitations are discussed (presumably Section XV, "Conclusions", or Section XIII, "Limitations", if that is its intended title).

### MINOR Revisions

**P5-m5: Minor arithmetic inconsistencies in monopole-subtracted table**
*   **Location:** Page 13, Table X.
*   **Problem:** The calculated values for `σ_vs_monopole` for the filament and cluster classes show minor inconsistencies. For the filament class, the inputs (`Δf_cw = +0.0008`, `n=408,187`) should yield `σ_vs_monopole = +1.02`, but the table lists `+0.99`. For the cluster class, the inputs (`Δf_cw = -0.0009`, `n=397,505`) should yield `σ_vs_monopole = -1.13`, but the table lists `-1.11`. While small, these inaccuracies should be corrected for rigor.
*   **Fix:** Re-calculate and correct the `σ_vs_monopole` values in Table X.

**P5-m6: Confusing numbers in figure caption**
*   **Location:** Page 16, Figure 7 caption.
*   **Problem:** The caption states that the V-Web and Tempel filament classes "differ by 0.026 percentage points", but the rounded `f_cw` values provided in the same sentence (`0.4980` and `0.4982`) produce a difference of 0.02 percentage points. The 0.026 pp value is correct, but it can only be obtained from the un-rounded data. This presentation is confusing and appears contradictory.
*   **Fix:** Clarify the caption. Either provide the `f_cw` values with enough precision to reproduce the stated difference (e.g., `0.4980` vs `0.49826`) or rephrase to avoid the apparent inconsistency (e.g., "...differ by 0.026 percentage points (from `f_cw` = 0.49796... and 0.49822...)").

**P5-m7: Broken internal concept reference**
*   **Location:** Page 2, Section I.
*   **Problem:** The text refers to "any future model in the bounce-chirality coupling class (Sec. II)". However, Section II ("Relation to Paper IV") does not define or discuss any such "class". This reference is a dead end for the reader.
*   **Fix:** Either add a definition of this concept to Section II or remove the parenthetical reference.