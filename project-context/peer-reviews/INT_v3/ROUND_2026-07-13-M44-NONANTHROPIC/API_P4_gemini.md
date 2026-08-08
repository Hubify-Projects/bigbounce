# INT API Review — P4 v1.0.240 — gemini (gemini-3.1-pro-preview)
paper: P4  version: v1.0.240  model: gemini-3.1-pro-preview
modality: native-PDF (Files/media upload file_uri)
UTC: 2026-07-14T07:18:54.295046Z  |  latency: 53.8s  |  attempt: 1
usage: {"promptTokenCount": 18814, "candidatesTokenCount": 551, "totalTokenCount": 20711, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 94}, {"modality": "IMAGE", "tokenCount": 18720}], "thoughtsTokenCount": 1346, "serviceTier": "standard"}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

VERDICT: MINOR REVISIONS

ISSUES:
1. [MINOR] Presentation and Formatting: The manuscript includes literal software file paths, JSON artifact names, and Python script names (e.g., `pipelines/p2_chirality/outputs/canonical_provenance/...`) embedded directly into the main text and body paragraphs. While the commitment to absolute reproducibility and data provenance is highly commendable, this formatting is highly distracting and violates conventional Physical Review D style guidelines. All artifact paths, script names, and Git commit references should be moved to footnotes, a dedicated appendix table, or the Data Availability statement to preserve the readability of the scientific narrative.
2. [MINOR] Defensive Repetition Regarding Prior Work: The author repeatedly issues defensive caveats stating they "do not claim a frequentist exclusion of Shamir's Ganalyzer estimator" (appearing in the Abstract, Introduction, Section V, and Section VII), while concurrently demonstrating a $3.7–8.8\times$ amplitude tension. This repetition dilutes the paper's impact. The author should state the methodological limitation (the lack of a matched-footprint Ganalyzer reanalysis) clearly and thoroughly exactly once in Section V, and streamline the text elsewhere.
3. [MINOR] Clarity on the "Open Item" Residual: The discussion of the unmodelled $\sim47\%$ of the $+3.64\sigma$ pseudo-$C_\ell$ harmonic residual in Section IV.D (and Appendix D) is extremely dense. While the author's mathematical argument is sound—that even if this entire residual were a true cosmological dipole, it falls below the real-space estimator's $50\%$ recovery threshold ($A_{50} \approx 0.75\%$)—the narrative is buried in a wall of text. Breaking this specific bounding argument into discrete, bulleted logical steps would greatly assist the reader in understanding why this systematic anomaly does not threaten the primary null result.
4. [MINOR] Abstract Clarification on Pseudo-labels: The abstract should briefly note that the ViT-Small training set partially relies on CE-ResNet pseudo-labels, as this is a critical detail of the pipeline's provenance. While Section VI.A exhaustively and convincingly proves this does not circularly induce a null result (via the independent GZ1 human-label cross-check), the use of a teacher-student-like label inheritance for the primary model should be transparently stated upfront.

The central claim that the large-scale chirality dipole of spiral galaxies is consistent with a null signal at sub-percent sensitivity is rigorously supported by the data, robust equivariant methodology, and exhaustive systematic checks.