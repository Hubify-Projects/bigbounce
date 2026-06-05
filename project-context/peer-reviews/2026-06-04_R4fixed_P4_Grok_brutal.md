# P4 2026-06-04_R4fixed — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 15.4s

---

**Referee Report for P4 (Round 2026-06-04_R4fixed)**

**Paper length**: 56 pages. This is excessive for a methods/catalog paper; PRD norms are 15–30 pp. The central contribution (a sub-percent null dipole at ℓ = 1 plus a quantified monopole-mask leakage channel) does not justify the length. Recommended maximum: 22–25 pages after removal of all internal audit language, exhaustive null-battery tables, and repetitive pipeline provenance.

**Classification of findings**

**ESSENTIAL (must be fixed for acceptance)**

- **P4-E1 (Abstract + Sec. I, p. 1–3)**: The abstract and opening paragraphs present the −0.12σ subsample-mask MASTER result as the “headline scientific result” while the body devotes extensive space to the +3.64σ canonical-mask residual. The abstract is technically accurate on the load-bearing estimator, but the narrative framing (“headline”, “load-bearing”) is inconsistent with the explicit statement that the canonical-mask value is systematics-attributed. Required fix: rewrite the abstract and Sec. I to state plainly that the paper reports a null at the analysis-subsample mask and a residual at the canonical mask that is resolved as a depth/morphology systematic; remove all “headline” language.

- **P4-E2 (Throughout, especially Sec. IV C, IV D, VI G, Table II, Table VI, Table VIII)**: Multiple σ values are reported from qualitatively different null procedures (per-pixel-shuffle, label-shuffle MASTER, binomial monopole-only, bootstrap). The paper contains the correct disclaimer (“σ values … are not directly comparable”), yet continues to present them side-by-side as if they form a single narrative. This is a direct violation of the instruction on σ-scale qualification. Required fix: either (a) report only p-values or rank statistics for every estimator, or (b) restrict the main text to a single, clearly identified null procedure and move all cross-null comparisons to a short appendix.

- **P4-E3 (Sec. III A, p. 6; Sec. IV D; Sec. VI G; all pipeline/artifact citations)**: The manuscript contains dozens of internal audit tags, reproducibility paths, version strings (“paper4-v1.0.154”, “wave14”, “R4fixed”, “seed=42”, “companion artifact pipelines/…”, “immutable release tag”), and review-log prose. These have no place in a journal submission. Required fix: delete every such string from the body; retain only the final public data-release URL and DOI.

- **P4-E4 (Sec. I, p. 3; Sec. V A)**: The text repeatedly states that a matched-footprint Ganalyzer reanalysis “is required for a likelihood-level exclusion” of Shamir’s results but then does not perform it. The claim that the present null “disfavors” Shamir at a factor of ∼6–12 in amplitude is therefore an overclaim. Required fix: remove all quantitative amplitude-comparison language with Shamir; state only that the two pipelines differ in classifier, selection, and footprint and that no like-for-like exclusion is claimed.

**MAJOR (significant revision required)**

- **P4-M1 (Entire manuscript)**: The paper is 2–3× longer than justified by the contribution. The core result is a null dipole plus a leakage-channel calibration. All extended multi-null batteries, hemisphere scans, per-leg × confidence tables, brick-boundary tests, and D4-TTA hold-out appendices must be condensed or moved to supplementary material.

- **P4-M2 (Sec. IV B, p. 15–16; Sec. VI A)**: The 9.5σ residual monopole is presented with extensive discussion of possible origins (GZ1 bias, rotation non-equivariance, PSF asymmetry) while the paper simultaneously claims sub-percent sensitivity. The tension is never resolved. Required fix: either demonstrate that the monopole has zero dipole projection (via the missing PSF-ellipticity cross-power test) or downgrade the sensitivity claim to “statistical-only, conditional on zero systematic dipole projection.”

- **P4-M3 (Sec. VI C, Table IX, Table XVI)**: The sensitivity floor is quoted as both a statistical Fisher value (∼0.29 %) and an empirical 50 %-recovery threshold (≥0.75 %). The abstract adopts the latter, but the text continues to cite the former. Required fix: adopt one number consistently and label it clearly as “empirical, systematics-inclusive” or “statistical-only.”

- **P4-M4 (Sec. III E, p. 9–11)**: The D4-TTA hold-out retraction of the argmax-CW-fraction shift is buried in footnote prose. This is a material change to an earlier claim and must be stated in the main text.

**MINOR (should be addressed)**

- **P4-m1 (Table I, Table II)**: The Nmap weighted column (5 547 858) exceeds the physical galaxy count because of 2-fold TTA. The table caption does not explain this. Add one sentence.

- **P4-m2 (Sec. IV G, p. 31)**: The two look-elsewhere corrections (analytic Bonferroni/BH <1σ vs. direct MC pLEE ≤10−4) give contradictory verdicts on the hemisphere signal. The text attributes the MC rejection to systematics but does not reconcile the two numbers. Add a one-paragraph clarification.

- **P4-m3 (Sec. VIII, p. 49)**: The NaMaster configuration appendix is incomplete (missing explicit statement that the headline ℓ=1 result uses a single-multipole bin, not a bandpower). Correct.

**NIT (very minor)**

- Multiple instances of “textemdash” instead of em-dash, inconsistent use of “ℓ = 1” vs. “l = 1”, and a handful of duplicated phrases (“the the”, “null null”) that survived editing.

**Summary recommendation**

**MAJOR REVISIONS**

The central scientific claim—a clean null at the analysis-subsample MASTER ℓ = 1 estimator after explicit removal of a quantified monopole-mask leakage channel—is honest and correctly caveated. However, the manuscript is grossly over-length, riddled with internal review artifacts and pipeline provenance that have no place in a journal article, and contains multiple instances of narrative inflation around σ values and amplitude comparisons that the authors themselves qualify as non-comparable. These are not cosmetic issues; they violate PRD standards for clarity and conciseness. A major revision that (i) removes all internal tags and version language, (ii) condenses the paper to ∼22–25 pages, and (iii) enforces a single, clearly labeled null procedure throughout would make the work acceptable. Without those changes the paper cannot be published in its current form.