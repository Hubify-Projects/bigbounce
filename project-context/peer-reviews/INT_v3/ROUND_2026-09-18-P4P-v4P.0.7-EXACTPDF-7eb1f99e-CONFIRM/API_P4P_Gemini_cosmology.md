# P4P INT_v3/ROUND_2026-09-18-P4P-v4P.0.7-EXACTPDF-7eb1f99e-CONFIRM/API — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-3.1-pro-preview`
**Input PDF**: `pipelines/p4prime_chirality_test/paper/main.pdf` sha256=7eb1f99ecc5e3d50a90457997e075873750eff0902ac95eadf9e430d27729a9d pages=13
**Review packet(s)**: `4738646f8116429d6e88cb8adce2f2d566322c9d9c7b20b4c114e82cbe7f4905, a0d86f59cb27fd0878d1812cc7943bac998c769914a5d63322c23899b733e9f3`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2564 chars)
**Wall time**: 283.2s

---

Here is the referee report for the manuscript, evaluated against the Physical Review D / ApJS standards for theoretical physics and observational rigor.

### ESSENTIAL

**P4P-E1: Contradiction between Abstract and Body on Sensitivity Floor**
*   **Location:** Abstract (Page 1) vs. Section 5.1/5.2 (Pages 7-8)
*   **Problem:** The abstract states: "...with a 95% sensitivity floor $A_{95}^{\text{obs}} \simeq 0.98\%$ (Neyman 95% CL limit $A_{95}^{CL} \simeq 0.75\%$, the floor used below). our floor disfavors a dipole above ~1%..." This explicitly claims the 0.75% limit is the floor used for the exclusion. However, Section 5 explicitly uses the 0.98% floor: "We therefore confront the model in Sec. 5 with the realization-independent floor $A_{95}^{\text{obs}} = 0.98\%$, the more conservative of the two" (Sec 3, line 317) and "the catalog's coverage-calibrated 95% sensitivity upper limit excludes $\eta > A_{95}^{\text{obs}} \simeq 0.98\%$" (Sec 5.2, line 524). 
*   **Required Fix:** Correct the abstract to accurately reflect the body. If the 0.98% floor is used for the exclusion, remove the parenthetical claim that the 0.75% floor is "the floor used below."

**P4P-E2: Mathematical Inconsistencies in Table 8 $z$-scores**
*   **Location:** Table 8 (Page 11) and Section A.1 (Page 11, lines 735-737)
*   **Problem:** The $z$-scores for the Projected sample in Table 8 completely contradict the provided $f_{CW}$ values. The global mean $f_{CW}$ for this sample is $\approx 0.49605$. 
    *   The Wall/filament bin has the *highest* fraction ($0.49680$), which is above the mean, yet reports a *negative* $z = -1.06$. 
    *   The Node-like bin has the *lowest* fraction ($0.49388$), which is below the mean, yet reports a large *positive* $z = +2.96$. 
    *   Furthermore, the text claims $z = +2.96$ corresponds to a local p-value of $p_{local} = 0.0060$. For a normal distribution (which is exact here given $N=189,917$), $z=2.96$ yields a two-sided $p = 0.0031$. A p-value of $0.0060$ would correspond to $z \approx 2.75$. The numbers are mathematically irreconcilable.
*   **Required Fix:** Recalculate and correct all $z$-scores and p-values in Table 8 and the corresponding text. Ensure the signs of the $z$-scores correctly reflect whether the observed fraction is above or below the null mean.

**P4P-E3: Standalone-Reader Test Violation (Non-Archival Dependency)**
*   **Location:** Section 4.1 (Page 7, line 462), Section A (Page 12, line 753), and Reference [16] (Page 13)
*   **Problem:** The manuscript relies on an unpublished, non-DOI manuscript hosted on a personal web domain (`hubify.app`, Ref [16]) to supply the full GALZONE construction and the full tables for the secondary void/non-void tests. Load-bearing methodological details and secondary proofs cannot be imported by citation to an unrefereed, non-archival URL.
*   **Required Fix:** Either move the necessary methodological details and tables into this manuscript's appendix, or remove the claims that rely on them. Replace the personal URL with a permanent archival DOI (e.g., Zenodo, arXiv) if the companion paper is to be cited at all.

**P4P-E4: Missing Effect Sizes for Cross-Correlations**
*   **Location:** Table 7 (Page 11)
*   **Problem:** Table 7 reports $z$-scores for various cross-correlations (e.g., Anomaly cross-corr $z=-1.05$, Redshift trend $z=-1.63$) but provides zero effect sizes. Every $\chi^2/\sigma/p$ headline must carry a physical effect-size statement (e.g., fractional amplitude, slope, Cramér's V) so the reader can judge practical significance alongside statistical significance.
*   **Required Fix:** Add a column to Table 7 reporting the measured effect size (amplitude, slope, etc.) for each statistic.

**P4P-E5: Unqualified Juxtaposition of Sigmas from Different Nulls**
*   **Location:** Section A.1 (Page 11, lines 733-734)
*   **Problem:** The text juxtaposes $z$-scores from two entirely different null procedures without explicit qualification: "...(spec-z: obs 1.872 vs. null 1.984 ± 1.841, z = -0.06, p = 0.952, confirmed by a sky-rotation null at z = -0.12, p = 0.917...)" Comparing a label-shuffle $z$-score directly to a sky-rotation $z$-score without explicitly stating they are "not directly comparable" violates statistical reporting standards for distinct null families.
*   **Required Fix:** Add an explicit qualification that these $z$-scores are derived from different null distributions and are not directly comparable.

### MAJOR

**P4P-M1: Version-History Language in the Body**
*   **Location:** Table 4 Caption (Page 4)
*   **Problem:** The caption narrates the internal drafting history of the paper: "T5, the former linear-Pearson RA/Dec metadata-leakage row, was removed because... the map-level low-$\ell$ real-$Y_{\ell m}$ regression in the archived release supersedes it". A published paper must present the final methodology, not narrate what was removed or superseded from earlier internal drafts.
*   **Required Fix:** Remove the version-history language. Simply state the tests that *are* applied, or if T5 must be mentioned for strict parity with an external archived release, state "T5 is omitted because..." without using draft-history terms like "former" and "supersedes it".

**P4P-M2: Incomplete Reporting of Pre-registered Battery**
*   **Location:** Section A.1 (Page 10, line 715) and Table 7 (Page 11)
*   **Problem:** The text claims a "pre-registered battery of 15 chirality $\times$ structure statistics" but Table 7 only summarizes 7 "representative statistics." If a look-elsewhere correction is applied over a pre-registered battery of 15 tests, the reader must be able to see all 15 tests and their results to verify the correction and ensure no significant results were buried in the omitted subset.
*   **Required Fix:** Expand Table 7 to include all 15 statistics in the battery.

**P4P-M3: Unexplained Sample Size Discrepancy**
*   **Location:** Section 2.1 (Page 2, line 97) vs. Section A.1 (Page 10, line 706)
*   **Problem:** Section 2.1 defines the classified-spiral sub-catalog as $N_{spiral} = 3,201,160$. However, Section A.1 refers to re-running the null on the "full 3,200,420-galaxy parent (no QC/confidence cuts)". There is an unexplained discrepancy of 740 galaxies between the full spiral catalog and the "full parent" used for the selection behavior test.
*   **Required Fix:** Explicitly state the origin of the 740-galaxy difference (e.g., an upstream base cut not previously mentioned) or correct the numbers if one is a typo.

### MINOR

**P4P-N1: Misleading Significance Claim for Cluster Bin**
*   **Location:** Figure 3 Caption (Page 7)
*   **Problem:** The text claims that neither the Filament nor Cluster bars "individually clears the null threshold used in the primary contrast." However, the Cluster bin ($\bar{f}_{CW} \approx 0.4958$) is approximately $2.02\sigma$ away from the global mean ($0.4974$), which corresponds to an uncorrected $p \approx 0.043$. This *does* clear a standard $1.96\sigma$ ($\alpha=0.05$) threshold.
*   **Required Fix:** Qualify the statement to clarify that it does not clear the threshold *after multiple-comparison correction* (if that is the case), or correct the statistical claim.

**P4P-N2: Missing Effect Size for Sample-Purity Ladder**
*   **Location:** Section A.1 (Page 10, line 676)
*   **Problem:** The text reports a "$+3.29\sigma$ excess" in the 1.87M-galaxy [0.5, 0.6) bin but does not state the physical amplitude (effect size) of this excess.
*   **Required Fix:** Provide the fractional amplitude corresponding to this $+3.29\sigma$ excess.

### NIT

**P4P-N3: Typo in URL**
*   **Location:** Section Data Availability (Page 12, line 748)
*   **Problem:** The Hugging Face URL contains spaces: `https://huggingf ace.co/datasets/bamf ai/galaxy-chirality-catalog`.
*   **Required Fix:** Remove the spaces to fix the URL.

---

## Summary recommendation

**MAJOR REVISIONS**

The manuscript presents a massive, rigorous observational test of a specific theoretical claim, utilizing an impressive dataset and a generally sound statistical framework. The confrontation with the Poplawski model is handled carefully by explicitly defining the necessary closure assumptions. However, the paper currently suffers from severe mathematical inconsistencies in Table 8 (where $z$-scores contradict the reported fractions and p-values), a direct contradiction between the abstract and the body regarding which sensitivity floor is used for the exclusion, and a reliance on an unarchived personal website for load-bearing secondary proofs. Furthermore, the omission of effect sizes in Table 7 and the incomplete reporting of the 15-test battery violate standard reporting requirements. These issues must be resolved to ensure the mathematical integrity and archival self-containedness of the paper before it can be accepted.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a fresh-eyes review of the manuscript, focusing on arithmetic, internal consistency, and precise claims. 

### MAJOR

**[P4P-M4]: Unsupported Novelty Claim / Direct Contradiction on "Largest Test"**
*   **Location:** Title, Abstract (Page 1), Section 1 (Page 2, line 63) vs. Section 5.2 (Page 8, lines 538-541) and Section 6 (Page 9, lines 627-630).
*   **Problem:** The manuscript's title is "The Largest Test of a Preferred Galaxy-Spin Axis," and the abstract claims "We report the largest test of that claim to date." However, the body text explicitly contradicts this. Section 5.2 states that the primary test sample ($N = 887,472$) is larger than every comparison sample *except* "Shamir (2022)'s same-survey DESI Legacy sample ($N = 1.3$ million), which is larger than the primary channel." 
*   **Required Fix:** You cannot claim to be the "largest test" in the title and abstract while explicitly acknowledging in the body that a prior literature test used a larger sample (1.3 million vs. 887k). The fact that the *parent catalog* is 8.47 million galaxies does not make the *test* the largest, because the primary dipole test is only performed on the 887k subset. The title and abstract must be revised to remove the "largest test" claim, or precisely qualify it (e.g., "The Largest Catalog...").

### MINOR

**[P4P-m1]: Ambiguous and Potentially Misleading Table Header**
*   **Location:** Table 6 (Page 10)
*   **Problem:** The third column is titled "$\sigma$ from pixel result". For the "Naive label identity" row, the value is $47\sigma$. A reader skimming the table will likely interpret "$47\sigma$" as the statistical significance of the naive label identity model (i.e., a massive detection). However, the math $(0.434 - 0.0167) / 0.0089 \approx 47$ reveals this is actually a *tension metric*—it means the naive model's prediction is $47\sigma$ *discrepant* from the measured pixel-level injection result. 
*   **Required Fix:** Change the column header to explicitly state this is a tension/discrepancy metric, such as "Tension with measured result ($\sigma$)" or "Discrepancy from measured ($\sigma$)".

### NIT

**[P4P-N4]: Directional Error in Internal Cross-Reference**
*   **Location:** Section 2.3 (Page 4, line 248)
*   **Problem:** The text refers to the harmonic diagnostic in "Sec. 3, above". However, Section 3 immediately follows Section 2.3 and is located physically below/after it in the document flow.
*   **Required Fix:** Change "(Sec. 3, above)" to "(Sec. 3, below)" or simply "(Sec. 3)".