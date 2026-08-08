# INT API Review — P5 v0.1.139-2026-07-16 — gemini (gemini-3.1-pro-preview)
paper: P5  version: v0.1.139-2026-07-16  model: gemini-3.1-pro-preview
provenance: commit=f2380597f8f6e54f5ef8010e8702857b6a0253d0  pdf=pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf  sha256=948e0412a5f4052747037f38ab2e43f2d888c61c74fbdfe95d29241ef806d2a9
packet: key=83f7dcc56b4c29ef9e41f8b2c9838f2a59deb67a5ff077d63cc63954089eb2ca  profile=AJ-OBSERVATIONAL
modality: native-PDF (inline_data base64)
UTC: 2026-07-16T22:33:17.374269Z  |  latency: 33.7s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 33.7, "modality": "native-PDF (inline_data base64)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "L1xZavLuC8SFz7IPquG5-A8", "usage": {"candidatesTokenCount": 587, "promptTokenCount": 21425, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 105}, {"modality": "IMAGE", "tokenCount": 21320}], "serviceTier": "standard", "thoughtsTokenCount": 1749, "totalTokenCount": 23761}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

**VERDICT:** MINOR REVISIONS

**ISSUES:**

1. [MAJOR] **Dependency on Unpublished Companion Paper (Paper IV):** The core inputs for this analysis—specifically the per-galaxy `class_eq` labels and the catalog-wide CW-fraction monopole scalar—are derived from a companion manuscript (Paper IV) that is stated to be "in preparation." While the author commendably provides the catalog publicly on HuggingFace and summarizes the classifier architecture in Appendix A, the fundamental validation of the machine learning model (e.g., training set construction, parity-equivariance enforcement, and accuracy floor validation) has not yet survived peer review. This manuscript cannot be fully accepted and published until Paper IV is at least concurrently submitted and accepted, or the entirety of the necessary model validation must be integrated into this manuscript.
2. [MINOR] **Manuscript Tone and Readability:** The manuscript's commitment to reproducibility, provenance tracking, and statistical stringency is exceptional and highly commendable. However, the text is written in a highly defensive and legalistic style (e.g., "Analysis-tree declaration", "Residual-ambiguity disclosure", constant inline artifact ID references like `[A10]`). This severely disrupts the narrative flow and makes the astrophysical context difficult to digest. The author should streamline the main text to focus on the astrophysical methods and results, moving the rigorous but distracting software/provenance audits and "declarations" to the appendices or a supplementary reproducibility document. 
3. [MINOR] **Overemphasis on the Contaminated T-Web Diagnostic:** Section IX (Additional Cosmic-Web Cross-Checks) and the surrounding T-Web discussions are excessively long given the author's own admission that the T-Web tidal-tensor path is a "diagnostic stress test, not load-bearing" and is heavily contaminated by the survey-shell density systematic. Since the DESIVAST catalog provides the focal, clean estimate, the T-Web sections should be significantly condensed in the main text to prevent distracting from the primary, robust result. 
4. [MINOR] **Formatting of Statistical Thresholds:** In Section VI and throughout, the author frequently mixes raw $\sigma$ values, monopole-subtracted $\sigma_{obs} - \sigma_{pred}$ residuals, and Bonferroni-corrected thresholds in the main text paragraphs. To aid the reader, these should be systematically tabulated or visually plotted in a summary figure that clearly demarcates the raw signal, the known bias (monopole), and the significance threshold, rather than listing them densely in the prose. 

**One sentence:** The central claim—that there is no statistically significant evidence for environment-dependent spiral galaxy chirality in the DESI DR1/DESIVAST matched sample once catalog-wide classifier biases are accounted for—is rigorously supported by the exhaustive statistical framework and robustness checks presented.