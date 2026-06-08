# P3 auto-2026-06-08_1520pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 NO_NEW
**Wall time**: 37.2s

---

I cannot complete the requested **citation-forensics audit** to PRD-standard from the text alone, because the prompt does not provide live arXiv/ADS search results or the rendered PDF pages needed to verify every bibliography entry, DOI/arXiv metadata, figures, and page-specific claims. The content is sufficient for a *textual* consistency audit, and it already contains multiple serious internal inconsistencies that would prevent acceptance.

**Critical internal findings from the supplied paper text**

- **P3-E1 — Abstract / Table I / §III / §IV: inconsistent total counts**
  - **Problem:** The abstract says “**378,280** Path-C unique anomalies,” while the body repeatedly distinguishes “**378,080 point-source object detections**” plus “**200 Planck CMB map-patch sky regions**.” Table I further claims the point-source tier is 378,080 and the headline is 378,280.
  - **Required fix:** The paper must use one unambiguous headline count and one stratified count everywhere, with a single definition of what is included in each total.

- **P3-E2 — Table I / §IV C / Appendix F: arithmetic inconsistency in the deduplication bookkeeping**
  - **Problem:** Table I states the Path-C native counts sum to **388,493** and deduplication removes **10,213** objects to yield **378,280**. Appendix F then states “**388,693 − 10,213 = 378,480** unique objects (+200 relative to the headline),” which conflicts with the main text and Table I.
  - **Required fix:** Recompute and correct the totals in all locations; the ACT-including and ACT-excluding tallies must be mutually consistent.

- **P3-E3 — Abstract / §V / Table IV / Appendix C: incompatible \( \sigma(fNL) \) numbers**
  - **Problem:** The abstract reports **\( \sigma(fNL)=8.14 \)** with envelope **[3.92, 8.98]** and a **7.9% improvement**; §V reports the same, but Appendix C / Table VII report a baseline-matched **\( \sigma(fNL)=8.43 \)** at \( \alpha=0.15 \), and Table IV refers to “**95% envelope [3.92, 8.98]**” without reconciling the different central values.
  - **Required fix:** State clearly which forecast is primary, how the envelope was computed, and why multiple central values appear. As written, the cosmology section is internally inconsistent.

- **P3-E4 — §V A / §V B / Table IV: inconsistent significance mapping for \( \gamma \)**
  - **Problem:** The paper states \( \gamma = 2.567 \pm 0.382 \), then says matter-bounce \( \gamma=3.0 \) is **+1.13σ** and SMBHB \( \gamma=4.33 \) is **+4.61σ**. Those sigma offsets are not transparently derivable from the stated uncertainty under a standard Gaussian interpretation.
  - **Required fix:** Show the exact calculation of the significance values from the posterior summary, including whether the uncertainty is symmetric, one-sided, or derived from a non-Gaussian posterior.

- **P3-M1 — §II B / §III C / Table I: threshold definitions are contradictory**
  - **Problem:** §II B says “**Two threshold families are in use**,” with DESI using **S > 5**, SDSS/LAMOST using top-percentile slices, eROSITA using an IsolationForest knee, and Planck/NEOWISE using fixed top-1%. But Table I footnotes also describe per-survey thresholds and then reframe the SDSS/LAMOST headline counts as “top-1%” slices, while the text elsewhere says those counts are “native-retrained counts” on the DESI-trained BigAE score scale.
  - **Required fix:** Give a single threshold scheme per survey, with no ambiguity about whether headline counts are cut on \(S\), top-percentile, or detector-specific raw scores.

- **P3-M2 — §III C / Fig. 2 / Table I: SDSS values conflict**
  - **Problem:** §III C says the SDSS native retrain “re-scores **1,925,279** spectra; the top-77,905 native slice at **S ≥ 0.1060** supersedes the cross-transfer count.” Table I says SDSS DR18 total processed is **2,304,830** and the anomaly rate is **3.38%**. Fig. 2 describes SDSS transfer-learning scores spanning to \(1.9\times 10^{11}\), then says the native re-score compresses the same objects to \(S<14\).
  - **Required fix:** Reconcile the processed-sample size, the scored subset, and the published anomaly set. The paper must state exactly which spectra were scored and why the counts differ.

- **P3-M3 — §III D / Table I: LAMOST counts are inconsistent**
  - **Problem:** §III D says the Path-C native retrain “compresses the anomaly rate **21.5× to 2,054 at S > 5**; top-113,342 native slice at \(S \ge 0.4613\) is the released set.” Table I instead lists **44,075** as the cross-transfer count and **113,342** as the Path-C count, but the narrative in §II A says the native retrain is the primary result while the 2,054 number is also presented as a headline.
  - **Required fix:** Separate the detection-at-\(S>5\) diagnostic from the released catalog selection. Right now the paper conflates them.

- **P3-M4 — §III E / Table I / Fig. 7: eROSITA thresholding is not consistently described**
  - **Problem:** §III E says “**Anomaly count: 298 at \(S>0.259\) (top 0.03%; data-driven score-knee threshold)**,” while Table I describes the eROSITA headline as a “**harder top-298 cap**” equivalent to \(S>0.259\) on an IsolationForest raw-score axis. Later the text states the 298-source canonical-S top-cut overlaps 95.3% with the IF top-9,303.
  - **Required fix:** Clarify whether the published set is defined by a score knee, a fixed cap, or an IF cross-validation proxy. These are not interchangeable.

- **P3-M5 — §III F / Appendix F / Table V: Planck and ACT modeling is inconsistent**
  - **Problem:** §III F says Planck uses a **native convolutional autoencoder**, but Appendix F says ACT DR6 was scanned with the “**same cross-transfer fully connected autoencoder used for SDSS, LAMOST, and Planck (32-dim latent space)**,” while Table V lists ACT as a 32-dim cross-transfer baseline and Planck as a 128-dim native model.
  - **Required fix:** Explicitly distinguish the native Planck model from the quarantined ACT cross-transfer checkpoint and remove language implying the same model architecture was used for both.

- **P3-M6 — Fig. 1 / §III / Table I: figure caption and body counts do not match cleanly**
  - **Problem:** Fig. 1 caption says “**319,443 detections shown**” as the initial cross-transfer baseline and “canonical Path-C unique count is **378,280**,” but the figure is titled “Spatial distribution of all **319,443 anomalies across 8 archives**” while ACT is simultaneously said to be quarantined and excluded from main results.
  - **Required fix:** Make the figure title and caption state exactly whether ACT is included or excluded and whether the figure is diagnostic-only.

- **P3-M7 — §III C / Fig. 3: the “84% cool dwarfs” claim is not traceable from the displayed table/figure**
  - **Problem:** Fig. 3 and §III C assert the dominant cluster is “**84%**” ultra-cool dwarfs, but no supporting table in the supplied text gives the cluster membership counts or the mapping from HDBSCAN labels to physical classes.
  - **Required fix:** Provide the cluster-count table and the classification rule used to derive the 84% figure.

- **P3-M8 — §III A / Table VI: DESI category fractions sum inconsistently by rounding**
  - **Problem:** Table VI lists fractions 77.2%, 22.7%, 0.02%, 0.01%, 0.05%. These do sum to 100.0% only after assuming rounding, but the text elsewhere uses 77.2% and 22.7% as exact figures.
  - **Required fix:** Mark these as rounded percentages or provide exact fractions.

- **P3-M9 — §IV A: “17.8% genuine novelty fraction” is not fully supported**
  - **Problem:** The paper says the DESI top-1,000 anomalies cross-matched against 20 catalogs yields **82.2% archival-ID**, so **17.8%** are novel. But elsewhere it states this is a “single-sample point estimate” with “no upper/lower-bound status,” which is statistically weak for a headline novelty claim.
  - **Required fix:** Downgrade the claim or provide uncertainty bounds and a sensitivity analysis.

- **P3-M10 — §IV C / Table I: deduplication and cross-survey overlap are not fully self-consistent**
  - **Problem:** §IV C says there are **637 multi-survey coincidences** across **388,493 survey-level detections**, yielding **10,213 total collapsed**. Table I then says the 7-way dedup gives **378,280**. The arithmetic can be made consistent only if every intermediate count is interpreted exactly right, but the manuscript alternates between 388,493, 388,693, 378,080, and 378,280.
  - **Required fix:** Provide one audited bookkeeping chain with a single set of intermediate totals.

- **P3-M11 — §V / Appendix C / Fig. 8: Fisher forecast is presented as if derived, but the input assumptions are not fully disclosed**
  - **Problem:** The paper gives \(F_0 = 1/8.98^2\) and \(c=0.0747\), but the derivation is not shown in the body. Fig. 8 gives a dense-limit \( \sigma(fNL)=11.71 \) and baseline \(16.85\), which conflicts with the main-text baseline \(8.98\) unless the figure is for a different tracer configuration.
  - **Required fix:** State clearly which Fisher problem Fig. 8 refers to and why its values differ from the main forecast.

- **P3-M12 — §V A / Appendix E: non-Gaussian posterior language is used without adequate support**
  - **Problem:** The paper claims the posterior is “**non-Gaussian and slightly asymmetric**” and uses both mean±std and quantile forms, but the actual posterior diagnostics shown do not justify the exact significance claims quoted elsewhere.
  - **Required fix:** Provide the posterior plot or numerical summary sufficient to support the sigma-language and Bayes factor claims.

- **P3-M13 — §VI A: the LAMOST “methodological lesson” is overstated as a universal conclusion**
  - **Problem:** The manuscript states that 98% blue-excess implies anomaly rankings reflect training-set composition rather than rarity. That is an overgeneralization from one survey and one architecture.
  - **Required fix:** Narrow the claim to LAMOST/BigAE, not “anomaly detection” in general.

- **P3-M14 — §VII Conclusion / abstract: “largest multi-archive anomaly search reported to date” is unsupported**
  - **Problem:** The paper claims novelty/scale leadership but does not compare against a complete survey of prior multi-archive anomaly searches.
  - **Required fix:** Either provide an explicit literature basis or soften/remove the superlative.

- **P3-M15 — Bibliography item : “in press” is stale and not auditable**
  - **Problem:** “Nicolaou et al., MNRAS (2026, in press)” is not a stable reference and may not be verifiable at submission time.
  - **Required fix:** Replace with a final bibliographic entry, arXiv ID, or a published venue citation.

- **P3-M16 — Bibliography item : arXiv year is stale and metadata likely incomplete**
  - **Problem:** “SPHEREx Collaboration, ‘Cosmology with the SPHEREx All-Sky Spectral Survey,’ arXiv:1412.4872 (2014)” is a proposal-era preprint used as a current forecast source. That may be acceptable as historical context, but it is not the right citation for a 2026 forecast claim unless explicitly justified.
  - **Required fix:** Cite the most relevant modern SPHEREx reference for the forecast being used.

- **P3-M17 — Bibliography item : internal note in citation is unacceptable**
  - **Problem:** The citation includes bracketed editorial metadata: “**[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]**.”
  - **Required fix:** Remove internal bookkeeping from the bibliography; references must contain only bibliographic metadata.

- **P3-M18 — Bibliography item [1]: overly generic release citation**
  - **Problem:** “DESI Collaboration, ‘The DESI Data Release 1,’ 2025, DESI DR1 documentation” is not a standard citable bibliographic record and lacks stable publication metadata in the supplied text.
  - **Required fix:** Replace with a proper archive or journal citation.

- **P3-M19 — Appendix D / Fig. 9: figure labels appear inconsistent with the text**
  - **Problem:** Fig. 9 labels some panels with “AE=” values, while the body says the canonical anomaly score is \(S\), and earlier warns that panel labels report the per-arm Z-arm sub-score \(r_Z\) “printed as AE for legacy compatibility.” This is confusing and easy to misread.
  - **Required fix:** Use one label convention and define it directly in the figure caption.

- **P3-M20 — Abstract / §III / §IV: the paper mixes object-level and patch-level statistics without constant qualification**
  - **Problem:** The abstract, Table I, and survey sections switch between “sources,” “object detections,” “sky regions,” “map patches,” and “anomalies” without always specifying which domain a quoted percentage or count refers to.
  - **Required fix:** Add domain labels to every count and percentage. For PRD standards, this is not optional.

**Additional audit concerns that would block acceptance even without external verification**

- The manuscript is overburdened with many threshold systems, diagnostic sub-analyses, and repeated caveat layers; the result set is too fragmented for clean PRD presentation.
- Several results are explicitly described as *diagnostic only*, *exploratory*, or *not science results*, yet they still appear in the abstract and conclusions as load-bearing claims.
- The bibliography contains multiple entries that need web-verification against arXiv/ADS before the paper can be trusted.

## Summary recommendation
**REJECT**

The manuscript contains multiple internal arithmetic inconsistencies, conflicting definitions of headline results, unresolved threshold bookkeeping, and bibliography entries that are not auditable from the text provided. Several claims in the abstract are not cleanly supported by the body, and the paper mixes diagnostic artifacts with primary results in ways that are incompatible with PRD’s standards for precision and reproducibility.