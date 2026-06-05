# P3 R10v3 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API)
**Wall time**: 87.0s

---

**Referee Report on "Spectrally Unusual Sources at Scale..."**

**To the Editor of Physical Review D,**

This manuscript presents a large-scale application of autoencoder-based anomaly detection to 37.3 million sources across seven astronomical archives, resulting in a catalog of 378,280 unique anomalies. The work has two main thrusts: (1) the creation and validation of this multi-survey anomaly catalog, and (2) the application of a subset of these anomalies as novel tracers to forecast constraints on primordial non-Gaussianity (fNL).

The scale of the data processing is impressive, and the authors have made a commendable effort to be methodologically transparent. The "Path-C rebuild" protocol, which addresses initial cross-survey contamination issues, and the detailed discussion of limitations, artifacts, and validation steps (e.g., injection-recovery tests, the LAMOST training-bias lesson) are strengths of the paper. The resulting catalog is a potentially valuable resource for the astronomical community. The cosmological application, while secondary, is relevant to the scope of PRD.

However, the manuscript in its current form contains several essential-to-fix errors, including a persistent arithmetic error in a headline cosmological result and confusing presentation of the primary data products. The cosmological analysis also requires further justification for its statistical formalism. Therefore, I recommend that the paper undergo **Major Revisions** before it can be considered for publication.

Below is a detailed list of required changes.

---
### Detailed Findings

#### ESSENTIAL Revisions (Paper cannot be accepted without these fixes)

*   **ID: P3-E1**
    *   **Location:** Page 1, Abstract header
    *   **Problem:** The paper is dated `(Dated: June 2026)`. This is a future date and is unacceptable for a submitted manuscript.
    *   **Fix:** Replace this placeholder with the correct submission date.

*   **ID: P3-E2**
    *   **Location:** Page 2 (§II.A, §II.B), Page 5 (§III.B)
    *   **Problem:** The text contains unresolved figure references: `Fig. ??`.
    *   **Fix:** Replace all instances of `Fig. ??` with the correct figure numbers.

*   **ID: P3-E3**
    *   **Location:** Abstract (p. 1), Section V.B (p. 10), Section VII (Conclusions, p. 14)
    *   **Problem:** The paper repeatedly claims a `7.9% improvement` on the constraint on fNL. However, a direct calculation using the paper's own baseline and new forecast values (`σ(fNL)std = 8.98`, `σ(fNL) = 8.14`) yields an improvement of `(8.98 - 8.14) / 8.98 = 9.35%`. This numerical discrepancy in a key cosmological result is a critical error.
    *   **Fix:** The authors must re-calculate and correct this percentage wherever it appears. If the 7.9% figure is somehow correct, a detailed derivation must be provided.

*   **ID: P3-E4**
    *   **Location:** Table I (p. 7)
    *   **Problem:** The primary summary table is highly confusing. The `Nanom` column reports the initial, superseded "cross-transfer" counts, while the final, canonical "Path-C" counts are relegated to footnotes and a summary row. This buries the main result and makes the table difficult to interpret.
    *   **Fix:** Restructure Table I to be a clean summary of the final, canonical results. The `Nanom` column should report the final Path-C anomaly counts for each survey. The superseded cross-transfer counts, while useful for diagnostics, should be moved to a separate table in an appendix.

#### MAJOR Revisions (Significant revision required)

*   **ID: P3-M1**
    *   **Location:** Section II.B (p. 2), Table I caption (p. 7), Discussion
    *   **Problem:** The study employs four different anomaly thresholding methodologies across the seven surveys (absolute S-cut, top-percentile, data-driven knee, fixed-count selection). This methodological heterogeneity makes a direct, physical comparison of anomaly *rates* between surveys highly problematic. While the paper acknowledges the different thresholds in a caption, it does not sufficiently discuss the scientific implications of this choice.
    *   **Fix:** Add a dedicated paragraph to the Discussion (e.g., Section VI.C, Limitations) that explicitly addresses how this heterogeneity impacts the interpretation of the catalog. The authors should caution readers against over-interpreting the relative anomaly rates and clarify that the catalog is primarily a collection of rank-ordered lists, not a uniformly selected sample.

*   **ID: P3-M2**
    *   **Location:** Section V.B (p. 10), Section VI.D (p. 12)
    *   **Problem:** The Fisher forecast relies on the functional form `1/σ(fNL)² = F₀ + cα²`, where `α` is the bias enhancement factor. This form is presented without derivation or citation. While it is plausible as a leading-order Taylor expansion of the Fisher information `I(fNL)`, its validity and applicability in this specific context are not established. For a cosmology paper in PRD, the statistical formalism must be transparent and well-justified.
    *   **Fix:** Provide a brief derivation of this formula or, preferably, cite a standard text or paper that establishes this quadratic dependence of the Fisher information on a linear bias parameter in a multi-tracer analysis.

*   **ID: P3-M3**
    *   **Location:** Section III.E (p. 6), Table I footnote `§` (p. 7)
    *   **Problem:** The text concerning eROSITA is confusing. It refers to a `298-source published catalog headline` and a separate `9,303-object reference set` used for Isolation Forest cross-validation. The relationship between these two samples is not explained, making it difficult to follow the validation logic.
    *   **Fix:** Clarify the relationship between these two eROSITA sets. For instance, is the 298-source set a high-purity subset of the 9,303-object set? The text must be unambiguous about which sample is being discussed at each point.

#### MINOR Revisions (Address but paper can proceed)

*   **ID: P3-m1**
    *   **Location:** Section II.B (p. 2)
    *   **Problem:** The notation for per-band contributions, `rB, rR, rZ`, is introduced without a formal definition of what `r` represents.
    *   **Fix:** Explicitly define `r` in the text (e.g., "per-band anomaly sub-scores, denoted `r`").

*   **ID: P3-m2**
    *   **Location:** Section III.B (p. 5)
    *   **Problem:** The text mentions that image panel labels use the notation `AE` instead of `rz` for the Z-arm sub-score due to "legacy compatibility." This is confusing for readers not familiar with the legacy context.
    *   **Fix:** For clarity, either use `rz` consistently or add a more prominent explanation of the `AE` notation in the main body text, not just the figure caption.

*   **ID: P3-m3**
    *   **Location:** Figure 1 caption (p. 4)
    *   **Problem:** The caption for the sky map in Figure 1 states that it shows the `initial cross-transfer anomaly baseline (319,443 detections)` while also quoting the final `canonical Path-C unique count is 378,280`. This juxtaposition is confusing.
    *   **Fix:** Rephrase the caption to clearly and immediately state that the figure shows a diagnostic "before" state for methodological comparison. For example: "This map shows the spatial distribution of the initial cross-transfer anomaly baseline, which was superseded by the Path-C rebuild protocol described in §IID. This figure is preserved as a diagnostic..."

#### NIT (Cosmetic)

*   **ID: P3-N1**
    *   **Location:** References (p. 19)
    *   **Problem:** Several references list future publication years (e.g., [1] DESI 2025, [12] Nicolaou 2026).
    *   **Fix:** Update these references to "in press," "submitted," or provide the correct publication year and journal details if now available. An arXiv identifier is sufficient if the work is not yet published.

---
## Summary recommendation

**MAJOR REVISIONS**

The paper reports on a massive and potentially impactful data analysis project. The authors' commitment to methodological transparency is a significant strength. However, the manuscript is currently undermined by a critical numerical error in its headline cosmological result, a confusing presentation of its primary data table, and several points of methodological ambiguity. These issues must be thoroughly addressed. Once corrected, the paper will represent a valuable contribution to both the astronomical and cosmological communities and will be suitable for publication in Physical Review D.