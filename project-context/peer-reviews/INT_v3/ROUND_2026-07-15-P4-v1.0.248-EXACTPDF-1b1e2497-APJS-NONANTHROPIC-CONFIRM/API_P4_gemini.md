# INT API Review — P4 v1.0.248 — gemini (gemini-3.1-pro-preview)
paper: P4  version: v1.0.248  model: gemini-3.1-pro-preview
provenance: commit=5bc450274afa05cf7d6d3a14ca54d66279c83176  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=1b1e2497f5a4083d41b2d56fb627cbced60b8a9ec95da595d86c8d244052d937
packet: key=7099014727f543d854773eb2a30c2da44a42d9a642b09a4d5ce3a6bc60acff55  profile=APJS-CATALOG-METHODS
modality: native-PDF (Files/media upload file_uri)
UTC: 2026-07-15T12:09:14.892141Z  |  latency: 57.4s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 57.4, "modality": "native-PDF (Files/media upload file_uri)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "hXhXap-jA_3Qz7IPyNjRGA", "usage": {"candidatesTokenCount": 631, "promptTokenCount": 13631, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 111}, {"modality": "IMAGE", "tokenCount": 13520}], "serviceTier": "standard", "thoughtsTokenCount": 1586, "totalTokenCount": 15848}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MINOR REVISIONS

(2) ISSUES:
1. [MAJOR] Presentation and Readability (Inline File Paths): The manuscript frequently embeds long repository file paths (e.g., `pipelines/p2_chirality/outputs/canonical_provenance/...`) directly into the main prose (e.g., in Sections IV.B, IV.C, IV.D, VI.B, and Appendices). This severely disrupts reading flow and gives the manuscript the appearance of an internal software audit rather than a peer-reviewed journal article. **Resolution:** Move all specific script and JSON artifact paths to a consolidated "Data and Code Provenance" table in the Appendix, or use standard footnotes/reference citations to point to the repository.
2. [MAJOR] Defensive Repetition and Tone: The manuscript obsessively repeats the distinction between the "single primary science sample/estimator" and "diagnostics" across the Abstract, Sections I, III.B, IV, VI, and Tables I, II, and III. While rigorous constraint definition is appreciated, stating "WLS is a diagnostic, not an independent detection or physical exclusion" half a dozen times dilutes the scientific narrative. **Resolution:** State the analysis hierarchy and the role of each estimator clearly *once* in Section III.B (and summarize in Table I), then report the results confidently in Section IV without defensively repeating the caveats in every paragraph.
3. [MAJOR] Abstract Density: The abstract is currently bogged down by pipeline-specific bookkeeping (e.g., "The release contract removes raw-pass... quarantines all 249,066 catalog-wide reconstruction violators"). **Resolution:** Rewrite the abstract to focus on the broad scientific achievements: the generation of the 8.47M galaxy catalog, the ViT-Small model with equivariant test-time augmentation, the primary null result (+0.71σ), and the critical discovery that monopole-mask leakage accounts for previously claimed dipole detections.
4. [MINOR] Table Caption Lengths: The captions for Tables VI, VII, and XI are excessively long and contain core methodological explanations (like shot-noise floor calculations and generative draw specifics) that belong in the main text. **Resolution:** Move the detailed methodological descriptions out of the captions and into the corresponding subsections of Appendix A or D.
5. [MINOR] Training Data Discrepancy (Section II.B): The author commendably documents a discrepancy between `v2_bias_audit.json` and `BENCHMARK_REPORT.md` regarding the historical training set composition. However, the text should explicitly state the practical impact (or lack thereof) of this missing provenance on the final catalog (e.g., stating explicitly that test-time equivariance forces symmetry regardless of this training imbalance, thereby mitigating the missing record).

(3) The central claim—that the observed chirality dipole is statistically consistent with a null result once equivariant inference and monopole-mask leakage are properly accounted for—is thoroughly supported by exceptionally rigorous systematic checks.
