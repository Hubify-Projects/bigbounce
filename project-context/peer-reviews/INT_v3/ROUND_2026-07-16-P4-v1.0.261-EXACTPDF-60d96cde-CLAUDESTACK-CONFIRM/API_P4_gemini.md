# INT API Review — P4 v1.0.261 — gemini (gemini-3.1-pro-preview)
paper: P4  version: v1.0.261  model: gemini-3.1-pro-preview
provenance: commit=21fbef5d36b2f4e7ae4ee4482e028af5ab73f6d9  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=60d96cde47cee1475d58273a4e14fc41046abebf03d89fd50cb03bf10f6f0a64
packet: key=97aaccd6438cf1fee4651d8b485815c2777d41ed6a48486b29747d2040dfabcc  profile=APJS-CATALOG-METHODS
modality: native-PDF (Files/media upload file_uri)
UTC: 2026-07-16T22:50:12.298642Z  |  latency: 49.5s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 49.5, "modality": "native-PDF (Files/media upload file_uri)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "N2BZavrXH8rnz7IPx9nDgQ8", "usage": {"candidatesTokenCount": 477, "promptTokenCount": 13111, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 13000}, {"modality": "TEXT", "tokenCount": 111}], "serviceTier": "standard", "thoughtsTokenCount": 1731, "totalTokenCount": 15319}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

VERDICT: MINOR REVISIONS

ISSUES:
1. [MINOR] Section 2.2 and Data Availability: The main text is heavily cluttered with inline SHA-256 digests, Git commit hashes, and 40-character immutable dataset revision IDs (e.g., `bdd1b063a9a2...`). While this level of strict cryptographic provenance is highly commendable and appropriate for ApJS, placing these strings inline disrupts reading flow; please move these exact identifiers to a dedicated summary table in the Data Availability section or an Appendix.
2. [MAJOR] Section 3.2 and Appendix B (`raw_flip_qc_unsafe` flag): The manuscript excludes 59,515 "unsafe" rows to reach the primary science sample, but the physical or computational reason for this quarantine is scattered and deferred. While Appendix B finally explains that these arise from float32 excursions and raw/equivariant pipeline pass mismatches, a concise, plain-English summary of what triggers this failure mode must be provided when the flag is first introduced in the main text (Section 3.2 or 4.1) so the reader understands what they are excluding.
3. [MINOR] Figures 8, 9 & Section 4: The manuscript frequently refers to "historical" pipelines, diagnostics, and artifacts (e.g., Figure 8's caption notes a "different historical weighting/null implementation"). This defensive framing against the author's own earlier pipeline iterations or diagnostic runs is confusing for a first-time reader; streamline the text and figures to focus clearly on the validation and characteristics of the final, published equivariant product (Catalog C).
4. [MINOR] Section 6.1 & Table 14: The text evaluates the classifier's confusion matrix against Galaxy Zoo 1 labels without removing the training set overlap, which the author explicitly acknowledges. To establish a true physical transfer function or proper calibration scope, a clean hold-out validation metric on a strictly separated test set should ideally be provided, even if it requires a smaller sample size. 

The central claim that the observed-label chirality dipole in DESI spirals is robustly consistent with zero, and that earlier purported detections are attributable to quantifiable pipeline/survey systematics (monopole-mask leakage), is comprehensively supported.