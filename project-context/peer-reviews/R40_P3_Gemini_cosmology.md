# P3 R40 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=4a8c1172 pages=30
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2210 chars)
**Wall time**: 171.0s

---

## Referee Report: "Spectrally Unusual Sources at Scale..." by Houston Golden

**Report ID:** PRD-2026-06-HG-P3R40

### General Comments

This paper presents a large-scale, multi-survey search for anomalous astronomical objects using an autoencoder framework. The scope of the work is impressive, covering 37.3 million sources from seven major astronomical archives (DESI, SDSS, LAMOST, eROSITA, Planck, Gaia, NEOWISE). The author presents a final catalog of 378,280 unique anomalies and uses a subset of these for novel cosmological applications, including constraining primordial non-Gaussianity and testing bouncing cosmology models against NANOGrav data.

The paper is exceptionally well-written, rigorous, and transparent. The methodology is detailed, and the validation process (the "Path-C rebuild") is thorough. The author is commendably forthright about the limitations of the analysis, potential systematic effects, and methodological failures (e.g., the LAMOST training-bias and the quarantined ACT data). The distinction between different anomaly counts (e.g., full-stream vs. science-target-restricted) and different novelty metrics (SIMBAD-unmatched vs. genuine novelty) is handled with exemplary clarity. The cosmological applications, while not yielding detections, are carefully executed and conservatively interpreted, with proper attention to systematics and statistical caveats.

The manuscript in its current form is of very high quality and represents a significant contribution to the fields of astronomical data analysis and observational cosmology. The findings are substantial and the resulting data products will be of great value to the community. I have only a few suggestions for revision, mostly aimed at improving clarity in the abstract and figures.

---
### Findings

#### MAJOR

*   **P3-M1: Ambiguity of eROSITA result in Abstract**
    *   **Location:** Page 1, Abstract
    *   **Problem:** The abstract states: "eROSITA cross-validation stability 81.5%". This number, presented without context, could be misinterpreted as a successful validation. The body of the paper (p. 12, §IIIE) and the injection-recovery synthesis (p. 20, §VID(ii)) correctly clarify that eROSITA *fails* the injection-recovery gate, and the 81.5% stability is a "FAIL-with-diagnostic" result. The abstract must reflect the full context to avoid misleading the reader.
    *   **Fix:** Modify the abstract to include the "FAIL" status of the eROSITA validation gate alongside the 81.5% stability figure. For example: "...eROSITA 1.2%; eROSITA cross-validation stability 81.5% on a failed gate)." or similar phrasing that captures the nuance presented in the main text.

#### MINOR

*   **P3-m1: Clarity of Figure 2 Caption**
    *   **Location:** Page 7, Figure 2 Caption
    *   **Problem:** The sentence explaining the origin of the canonical unique count is syntactically complex and difficult to parse on first reading: "the canonical Path-C unique count of 378,280 is not a deduplication of this baseline — deduplication only ever reduces its input — but the 7-way 5" dedup of the per-survey native-retrained tallies, which sum to 388,493 and replace the cross-transfer counts survey-by-survey...".
    *   **Fix:** Rephrase this sentence for improved clarity. Suggestion: "The map above shows the 319,443-detection cross-transfer baseline. The final, canonical catalog of 378,280 unique objects is not a subset of this baseline; instead, it results from a 7-way 5" positional deduplication of the 388,493 anomalies found in the per-survey native-retrained analyses, which supersede the cross-transfer results."

*   **P3-m2: Provenance of Scores in Figure 8**
    *   **Location:** Page 17, Figure 8 Caption
    *   **Problem:** The caption notes that the "Score" annotations are "display values from that script rather than catalog-pipeline outputs." While this is transparent, it is not ideal. Displaying non-canonical scores on a key figure showcasing the primary cross-survey discoveries could cause confusion. The score for the TIC object (49.5) is particularly prominent and is cited in the main text.
    *   **Fix:** Replace the "display values" with the actual, canonical scores from the final data release for these specific objects. The caption should then clarify which score axis is being used (e.g., "SDSS score on the DESI-trained cross-transfer axis," "DESI native score," etc.), consistent with the catalog's data schema. This would make the figure a more faithful representation of the paper's data products.

#### NIT

*   **P3-N1: Paper Dating**
    *   **Location:** Page 1, Title Block
    *   **Problem:** The paper is dated "June 13, 2026".
    *   **Fix:** Correct the date to the date of submission.

*   **P3-N2: Notation Consistency for `f_NL`**
    *   **Location:** Throughout the manuscript
    *   **Problem:** The notation for the non-Gaussianity parameter alternates between `f_NL` (e.g., abstract, §V) and `fNL` (e.g., page 2).
    *   **Fix:** Use a single, consistent notation throughout the paper, preferably `f_\mathrm{NL}`.

*   **P3-N3: Table I Footnote `||` Self-Containment**
    *   **Location:** Page 9, Table I, Footnote `||`
    *   **Problem:** The footnote mentions that the aggregate SIMBAD-unmatched fraction (58.8%) is calculated differently from the per-survey values. The main text (§IV A) clarifies that the key difference is the matching radius (3" for the aggregate vs. 5" for the per-survey).
    *   **Fix:** Briefly add the radius information to the footnote to make it more self-contained. E.g., "...(pooled over top-100 anomalies at 3" radius)...".

*   **P3-N4: Citation [12] Date**
    *   **Location:** Page 29, Bibliography
    *   **Problem:** The publication year for reference [12] (Nicolaou et al.) is listed as 2026. This is likely a placeholder.
    *   **Fix:** If the paper is not yet accepted for publication in a 2026 issue, it should be cited with its current status (e.g., "submitted," "in press") or with its arXiv identifier and the year of its appearance on the archive.

---
## Summary recommendation

**MAJOR REVISIONS**

The paper is outstanding in its rigor, scope, and transparency. It is a model for how to conduct and present large-scale, multi-instrument data analysis. The scientific results, both the anomaly catalog itself and the cosmological applications, are significant. My recommendation for "Major Revisions" is based solely on the need to correct the potential for misinterpretation in the abstract (P3-M1), which is the most visible part of the paper. The other requested changes are minor and aimed at further improving the already high quality of the manuscript. I expect the author can address these points easily, and I look forward to seeing the revised version of this excellent work published.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a more rigorous, "fresh eyes" review of the paper.

---
### Additional Findings

A more detailed re-examination of the manuscript, focusing on numerical consistency, cross-references, and the details of the appendices, has revealed a few additional issues that were missed in the initial pass.

#### MAJOR

*   **P3-M2: Broken Cross-Reference in Abstract**
    *   **Location:** Page 1, Abstract, first paragraph
    *   **Problem:** The abstract contains the clause: "...the size benchmark is anchored to the largest published single-survey anomaly catalog [11]; §VIE)". The section reference `§VIE` does not exist in the manuscript. The relevant comparison appears to be in §VI E ("Comparison with Prior Work"). A broken cross-reference in the first paragraph of the abstract is a significant issue that needs correction.
    *   **Fix:** Correct the cross-reference to point to the correct section, likely `§VI E`.

#### MINOR

*   **P3-m3: Potential Typo in Cosmological Equation**
    *   **Location:** Page 25, Appendix E, Equation (E1)
    *   **Problem:** The equation for the log-power of the gravitational-wave background, `log10(Pi)`, includes a leading factor of `1/2`. As written, this implies that the power `Pi` scales with the amplitude `A` rather than `A^2` (since `log10(A)` is inside the brackets). This appears to be dimensionally and physically incorrect for a power quantity.
    *   **Fix:** Please verify this equation against its source. It is likely that the `1/2` pre-factor is a typo and should be removed.

#### NIT

*   **P3-N5: Awkward Self-Referential Cross-References**
    *   **Location:** Page 4, §II B; Page 20, §VID(ii)
    *   **Problem:** The text contains several cross-references that point to the section they are already in. For example, in §II B, the text says "see §II B for the per-survey specification," and in §VID(ii), it says "three surveys fail the 5σ gate (§VID (ii))". This phrasing is circular and confusing.
    *   **Fix:** Rephrase these references for clarity. For example, instead of a self-reference, use phrases like "as specified in the paragraph below" or simply remove the reference if the context is clear.