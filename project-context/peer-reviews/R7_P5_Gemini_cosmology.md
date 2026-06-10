# P5 R7 — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 65.1s

---

## Referee Report on "Environmental Dependence of Spiral Chirality..."

This paper presents a detailed statistical analysis testing for a correlation between the observed chirality (handedness) of spiral galaxies and their large-scale structure environment. The authors cross-match a large, new chirality catalog with the DESI Data Release 1 spectroscopic sample. They employ multiple cosmic-web classification schemes, with a primary analysis anchored on the public DESIVAST void catalog and supporting analyses using a V-Web tidal-tensor classifier and other external catalogs. The headline result is a null detection: spiral chirality is found to be statistically independent of environment at the sensitivity level of the current data, once a previously identified catalog-wide systematic monopole is accounted for.

The analysis is exceptionally thorough, featuring an extensive suite of robustness checks, sensitivity tests, and cross-validations against independent methods. The authors are commendably transparent about the limitations of their analysis, including the post-hoc definition of their primary analysis path, the statistical power of various subsamples, and the potential impact of redshift-space distortions (RSDs). The conclusion that the only significant deviations from parity are consistent with a global, environment-independent systematic from the parent chirality catalog is well-supported by numerous lines of evidence.

While the work is of high quality, several major and minor revisions are required before it can be considered for publication. The most significant issue is the analysis's foundational reliance on a companion paper that is not yet peer-reviewed or publicly available.

---
### ESSENTIAL Findings

None.

### MAJOR Findings

**ID: P5-M1**
- **Section/Page:** Abstract (p.1), Sec. II (p.2), throughout.
- **Problem:** The entire analysis is critically dependent on "Paper IV" [3], which provides the essential galaxy chirality labels and the value of the systematic "classifier-monopole offset." This foundational work is cited as "in preparation; manuscript in preparation" and is therefore not available to the reader or the reviewer. This raises significant concerns about the paper's self-containment, reproducibility, and the stability of its main inputs. While treating the outputs of Paper IV as fixed inputs is an acceptable approach for a series of papers, the non-peer-reviewed status of such a crucial dependency must be handled with maximal transparency.
- **Required Fix:**
    1.  The Abstract must explicitly state that the chirality labels and the key systematic offset are drawn from a companion work that is not yet peer-reviewed.
    2.  Section II ("Relation to Paper IV") should be expanded to include a brief discussion of the potential impact on this paper's conclusions if the main results of Paper IV (particularly the value and nature of the monopole offset) were to change significantly during its own peer-review process.
    3.  The authors should, if possible, provide a preprint of Paper IV (e.g., on arXiv) to allow for a more complete evaluation of the entire analysis chain. If this is not possible, the caveats regarding the dependency must be strengthened.

**ID: P5-M2**
- **Section/Page:** Primarily Sec. XIII (p.18), but relevant to Sec. IV, VI.
- **Problem:** The paper correctly identifies in the Limitations section that the V-Web tidal-tensor analysis is performed in redshift space and is subject to anisotropic redshift-space distortions (RSDs), which can affect class assignments at boundary regions. However, the V-Web analysis and its results are presented at length in the main results section (Sec. VI) without this crucial caveat being mentioned. The primary DESIVAST-based analysis is argued to be largely immune to RSDs, but since the V-Web results are presented first and in detail, the reader is not aware of this significant systematic uncertainty until the very end of the paper.
- **Required Fix:** The caveat regarding RSDs in the V-Web classification must be moved forward and made more prominent. A concise statement about the analysis being performed in redshift space and the potential impact of RSDs should be added to Section IV (V-Web Classification) and briefly reiterated at the beginning of Section VI (Results) where the V-Web results are first presented. This ensures the reader can properly contextualize the V-Web results as a supporting, but more systematically-limited, analysis compared to the primary DESIVAST path.

### MINOR Findings

**ID: P5-m1**
- **Section/Page:** Entire manuscript.
- **Problem:** At 20 pages, the paper is quite long for a single null result, albeit a very well-tested one. The main narrative, which logically flows from the initial V-Web analysis to the more robust DESIVAST analysis, is somewhat diluted by extensive discussions of multiple secondary cross-checks (e.g., with Tempel+2014, concurrent T-Web literature, ASTRA EDR) in the main body of the text.
- **Required Fix:** The authors should consider restructuring the paper to improve focus and readability. Moving the detailed descriptions and results of the secondary cross-validations (currently in Sec. IX and X) to an appendix would streamline the main text, allowing it to concentrate on the primary V-Web and DESIVAST results and their direct robustness tests. A target length of ~15 pages for the main text and appendices would be more appropriate for the contribution.

**ID: P5-m2**
- **Section/Page:** Abstract (p.1).
- **Problem:** The abstract reports significance values such as "−2.61σ" and "−4.66σ" without immediately clarifying the null hypothesis. While the text explains these track a monopole, it's initially ambiguous whether σ is calculated relative to parity (p=0.5) or some other baseline.
- **Required Fix:** Clarify in the abstract that these σ-values represent deviations from a parity-symmetric (50% CW / 50% CCW) distribution, before the subsequent interpretation involving the monopole offset is introduced. For example: "...are, in order of decreasing n: 0.4980 (filament; n=408,187, a −2.61σ deviation from parity), ...".

**ID: P5-m3**
- **Section/Page:** Sec. VIIa (p.7).
- **Problem:** The text contains the phrase "...(sixteen-cell table, JSON artifact above)...". The reference to a "JSON artifact" appears to be an internal note from the analysis pipeline that was not intended for the final manuscript.
- **Required Fix:** Rephrase this to remove the informal reference. For example: "...(the full sixteen-cell table is available in the data repository)..." or simply remove the parenthetical if it is not essential.

**ID: P5-m4**
- **Section/Page:** Throughout.
- **Problem:** The notation for the global mean CW fraction from Paper IV is inconsistent. It is variously implied by `∆fCW` (the offset), referred to as `f̄_CW` (e.g., Fig. 2 caption), `f_CW^P4` (Sec. VIII F), or simply the numerical value 0.4974. This makes tracking the paper's central systematic correction more difficult than necessary.
- **Required Fix:** Choose a single, consistent notation for the global CW fraction from Paper IV (e.g., `f̄_CW^P4`) and use it throughout the manuscript, including in figures and tables.

**ID: P5-m5**
- **Section/Page:** Appendix A (p.19).
- **Problem:** The toy EFT operator `L_parity ⊃ gϕ (∇i ϕ) (∇i ρ/ρbg ) (L̂ · ẑ)` contains the term `(L̂ · ẑ)`, which explicitly breaks rotational invariance, as the author correctly notes. While the text properly caveats this as a "coordinate-aligned schematic" and not a covariant operator, presenting it this way in an appendix could still be misleading.
- **Required Fix:** To improve the theoretical grounding, the author should replace the problematic `(L̂ · ẑ)` term directly in the equation with a more physically appropriate pseudoscalar, such as `(L̂ · ∇ρ)`, while retaining the caveat that this is a toy model. This would better represent the intended physical coupling between angular momentum and the environmental gradient.

### NITs (Typos and small corrections)

**ID: P5-N1**
- **Section/Page:** Fig. 7 caption (p.16).
- **Problem:** The caption states, "...the primary cross-classifier validation is the on-DESI DESIVAST re-projection in §IX B." The DESIVAST analysis is in Section VIII. Section IX B discusses concurrent literature.
- **Required Fix:** Correct the cross-reference to point to Section VIII.

**ID: P5-N2**
- **Section/Page:** Abstract (p.1), and elsewhere.
- **Problem:** The citation style includes the year in the main text before the reference number (e.g., "Hahn et al. 2007 [5]"). This is redundant and not standard for Physical Review D.
- **Required Fix:** Remove the year from the in-text citations, using the format "(Hahn et al. [5])".

**ID: P5-N3**
- **Section/Page:** p.2, footnote.
- **Problem:** The email address `houston@hubify.com` appears informal for a scientific publication.
- **Required Fix:** Consider using a more formal or institutional email address if one is available.

**ID: P5-N4**
- **Section/Page:** p.11, Sec. VIII B.
- **Problem:** The variable `nlz` is used without definition.
- **Required Fix:** Define the subscript "lz" (presumably "low-z") on its first use.

---
## Summary recommendation

**MAJOR REVISIONS**

This is a methodologically sound and impressively thorough paper that provides a strong null result on a topic of cosmological interest. The author's careful treatment of statistics, systematics, and robustness checks is a model of good practice. However, the paper in its current form cannot be accepted due to its critical dependence on an unavailable, non-peer-reviewed companion paper (P5-M1) and the delayed presentation of significant caveats regarding redshift-space distortions in a key part of the analysis (P5-M2). Once these major issues, along with the minor points on structure and clarity, are addressed, the paper will represent a valuable contribution to the literature.