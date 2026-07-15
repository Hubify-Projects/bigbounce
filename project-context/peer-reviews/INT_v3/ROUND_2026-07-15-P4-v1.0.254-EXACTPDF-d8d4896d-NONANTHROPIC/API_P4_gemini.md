# INT API Review — P4 v1.0.254 — gemini (gemini-3.1-pro-preview)
paper: P4  version: v1.0.254  model: gemini-3.1-pro-preview
provenance: commit=96c3a97eaa33a543420c2e26702fb9e279b87461  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=d8d4896d651f172a9fa407951cea12d96ac79e796ff0a88dad2dc2c7fd6533dd
packet: key=2f281c139445eda6c5899ae8a2b93e10bfce71c6f2ce8e62b2db941de6daf1c1  profile=APJS-CATALOG-METHODS
modality: native-PDF (Files/media upload file_uri)
UTC: 2026-07-15T21:54:54.480186Z  |  latency: 49.2s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 49.2, "modality": "native-PDF (Files/media upload file_uri)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "xAFYarLyNdXRz7IP9LWUsQI", "usage": {"candidatesTokenCount": 655, "promptTokenCount": 15191, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 15080}, {"modality": "TEXT", "tokenCount": 111}], "serviceTier": "standard", "thoughtsTokenCount": 1381, "totalTokenCount": 17227}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

**VERDICT:** MINOR REVISIONS

**ISSUES:**
1. [MINOR] **Terminology ("Historical" vs. "Raw"):** The manuscript frequently uses the term "historical" (e.g., "historical raw Catalog A", "historical WLS fit", "historical training realization" in Sections 3.5, 4.3, and Appendix D). To a general reader, "historical" implies previous literature (e.g., Shamir 2012, 2020), but here it appears to mean the author's own *pre-TTA pipeline pass* or *earlier internal code versions*. This terminology should be explicitly defined early in the text or replaced with clearer phrasing (e.g., "raw/pre-equivariant pipeline") to prevent confusion with prior published literature.
2. [MINOR] **Overly dense version-control provenance (Section 2.2 & Appendix B):** The manuscript's commitment to reproducibility is exceptional and highly suitable for ApJS. However, documenting conflicting internal repository logs (e.g., Table 12's 26,616 vs 26,626 rows) and citing specific SHA-256 commit hashes directly in the main text interrupts the scientific narrative. Consider moving the granular git-level commit hashes and internal audit discrepancies entirely to the Data Availability section or Appendix B, keeping the main text focused on the final data properties and methodological choices.
3. [MINOR] **Spatial Transfer Model (Section 6.2 & 6.4):** The author rightly acknowledges that the physical spatial transfer model remains "open" and cannot be fully calibrated due to the lack of an independent, unbiased spatial ground-truth set. While acceptable, the discussion would benefit from a brief addition in Section 6.4 explicitly outlining what specific future datasets (e.g., space-based Euclid/Roman imaging, dense spectroscopic redshift coverage) would be required to physically close this calibration loop for the community.
4. [MINOR] **Uncertainty Notation (Tables 4 and 14):** The 1-sigma binomial uncertainties are denoted using parenthesis notation, e.g., "0.507879(274)". While standard in particle physics, explicitly writing out $\pm 0.000274$ or ensuring the footnote definition is highly visible will improve readability for the broader astronomical and data-science readership of ApJS.
5. [MINOR] **Figure 7 Colorbar Labeling:** The color map uses a shared scale of [0.47, 0.53] for the CW fraction. For immediate visual comprehension, it would be helpful to mark the $0.50$ (parity-even) midpoint explicitly with a distinct tick or diverging colormap center (e.g., white), emphasizing the spatial artifacts in Catalog A versus the uniform noise around 0.50 in Catalog C.

**One sentence:** The central claim that the observed-label spiral chirality dipole is consistent with zero is robustly supported by the rigorous implementation of equivariant test-time averaging and exhaustive spatial null-hypothesis testing.