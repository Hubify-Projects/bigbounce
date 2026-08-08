# INT API Review — P4 v1.0.264 — gemini (gemini-3.1-pro-preview)
paper: P4  version: v1.0.264  model: gemini-3.1-pro-preview
provenance: commit=104ebb861a901c7ea61a1fb8730d77205249fdea  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=325b7ced736081a201fb5f1bc9c6283760c1296b5adcb1baf7cb503ce98cb862
packet: key=57e13e2771a7bbeb45aeeeca21cac739826efd53768b51689e957f8baa00dc88  profile=APJS-CATALOG-METHODS
modality: native-PDF (Files/media upload file_uri)
UTC: 2026-07-17T21:10:21.288854Z  |  latency: 55.1s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 55.1, "modality": "native-PDF (Files/media upload file_uri)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "V5paat6GE6_Xz7IP9vSsSQ", "usage": {"candidatesTokenCount": 581, "promptTokenCount": 14151, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 111}, {"modality": "IMAGE", "tokenCount": 14040}], "serviceTier": "standard", "thoughtsTokenCount": 1423, "totalTokenCount": 16155}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

**VERDICT:** MINOR REVISIONS

**ISSUES:**
1. **[MINOR] Main Text Narrative and "Audit" Language:** Throughout the manuscript (e.g., Section 4.4, Table 13, and Appendix B), the text refers to "historical training records," "conflicting committed historical records," and corrects "older audit language." Additionally, Section 4.5 (line 581) explicitly states, "a reviewer gate asked whether they instead share..." While the transparent tracking of the project's provenance is commendable, referencing internal pipeline history, previous draft versions, or referee reports directly in the text breaks the standard academic narrative flow. Please rephrase these instances into standard scientific prose (e.g., "To test whether the estimators share a single sampling covariance..." or "An earlier iteration of this pipeline [cite preprint if applicable] used...").
2. **[MINOR] Inline Hashes and File Paths:** The manuscript heavily peppers long file paths (e.g., `pipelines/p2_chirality/outputs/canonical_provenance/...`) and exact SHA-256 hashes directly into the main text and appendix paragraphs (e.g., lines 245, 390, 409, 1081). While this is the gold standard for reproducibility and highly appropriate for ApJS, placing them directly in the prose disrupts reading comprehension. Consider moving the exact paths and hashes to footnotes, or mapping them to a centralized "Reproducibility Manifest" table in the Appendix.
3. **[MINOR] Caption Length and Content:** The captions for Figure 7 and Figure 8 are excessively long and contain detailed methodological discussions, pipeline performance analyses, and conclusions (e.g., the discussion of TTA causality in Fig. 7). Please move the interpretive and narrative text into the main body (e.g., Section 3.4 or 4.3) and keep the captions restricted to describing the figure elements. 
4. **[MINOR] Table 13 Context:** Table 13 and its accompanying text (lines 1046-1051) detail "conflicting historical training-data records." It is unclear to the general reader whether this refers to a previously published paper, an earlier preprint by the author, or simply an older git commit of the current project. Please explicitly clarify the origin of these "historical" records so the reader understands what baseline is being audited. 

**Central claim supported?** 
Yes, the central claim—that there is no cosmological chirality dipole in this massive DESI sample and that previous/potential signals are heavily bounded by map-level systematics and monopole-mask leakage—is rigorously supported by state-of-the-art equivariant machine learning and exhaustive statistical null-testing.