# INT API Review — P4 v1.0.270 — gemini (gemini-3.1-pro-preview)
paper: P4  version: v1.0.270  model: gemini-3.1-pro-preview
provenance: commit=01340151c1465250c87ea21b94577bdb8527d1b4  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=ac7b39baca9a8196826227fde50c7b76be00a77f11213f833b85bbeca4cda33e
packet: key=d013a01375c6f5c9cbeaa097a8e9f9712f5c197ee325bb69dfdfb2e0abe8bdab  profile=APJS-CATALOG-METHODS
modality: native-PDF (Files/media upload file_uri)
UTC: 2026-07-24T00:32:51.284438Z  |  latency: 44.0s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 44.0, "modality": "native-PDF (Files/media upload file_uri)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "xbJiareQLvi3qtsPqp33iAc", "usage": {"candidatesTokenCount": 492, "promptTokenCount": 16751, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 16640}, {"modality": "TEXT", "tokenCount": 111}], "serviceTier": "standard", "thoughtsTokenCount": 1424, "totalTokenCount": 18667}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

**1. VERDICT:** MINOR REVISIONS

**2. ISSUES:**

1. **[MAJOR] Readability and inline provenance tracking (Throughout, e.g., Sec 2.2, Sec 3, Sec 4.1):** The extensive insertion of raw SHA-256 hashes, exact script file paths (e.g., `pipelines/p2_chirality/outputs/...`), and JSON filenames directly into the main narrative severely disrupts the readability of the manuscript. While the commitment to computational closure and open science is exemplary, these identifiers belong in footnotes, a dedicated provenance table, or the Data Availability section, rather than mid-sentence in the primary text.
2. **[MINOR] Textual artifacts and conversational tone (Appendix C, lines 1523-1524):** The phrase "Bonferroni control does not require independent tests; the earlier sentence claiming that it did was false" reads like an unresolved internal author note, draft comment, or direct response to a reviewer left in the text. This should be revised to state the adopted statistical methodology straightforwardly.
3. **[MINOR] Tone regarding historical data audits (Sec 2.2, Table 13, Appendix B):** The manuscript discusses "conflicting committed historical records," "honest negatives," and "adjudicated conflicts" with language more suited to a software post-mortem audit than a scientific paper. While the rigorous documentation of past un-reproducible states (e.g., CE-ResNet conflicts) is highly valuable for the community, the phrasing should be smoothed to a standard objective scientific tone (e.g., "we found the historical training split to be irreproducible under seeded ingestion...").
4. **[MINOR] Typographical constraints and line breaks (Throughout):** The inline use of long URLs and file paths causes awkward line breaks and text crowding in the two-column format. Moving these paths to references or using appropriate LaTeX macros (like `\path{}` or `\url{}`) will resolve these formatting artifacts.

**3. ONE-SENTENCE SUMMARY:** 
The central claim—that there is no statistically significant primordial chirality dipole in the DESI DR8 galaxy sample once classifier and imaging systematics are properly mitigated via test-time equivariance—is rigorously supported by the provided catalog, exhaustive bias-hardening diagnostics, and null tests.