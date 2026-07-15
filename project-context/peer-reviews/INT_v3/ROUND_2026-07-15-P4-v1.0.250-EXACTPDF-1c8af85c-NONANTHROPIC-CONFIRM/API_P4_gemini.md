# INT API Review — P4 v1.0.250 — gemini (gemini-3.1-pro-preview)
paper: P4  version: v1.0.250  model: gemini-3.1-pro-preview
provenance: commit=155166aa7f6ed5bfef91df8c63b3239ecdd817ae  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=1c8af85c038a50d59dc31d5db991eb5768cbe8f0dd1c91b411a54ebba68647df
packet: key=706457c99ab0c8101b3769d17fe8a88a3616c1e177b9a24ab43186aa3c453baf  profile=APJS-CATALOG-METHODS
modality: native-PDF (Files/media upload file_uri)
UTC: 2026-07-15T13:02:53.174369Z  |  latency: 59.6s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 59.6, "modality": "native-PDF (Files/media upload file_uri)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "F4VXasf5HoLrz7IP08ObwAY", "usage": {"candidatesTokenCount": 549, "promptTokenCount": 15191, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 15080}, {"modality": "TEXT", "tokenCount": 111}], "serviceTier": "standard", "thoughtsTokenCount": 1952, "totalTokenCount": 17692}}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

**VERDICT:** MAJOR REVISIONS

**ISSUES:**

1. **[MAJOR] Manuscript Tone and "Audit" Structure (Section 6, Appendices B/C/D)**: The manuscript contains highly unusual "audit" language that actively repudiates "historical" internal assertions directly in the main text (e.g., line 1171: "The parenthetical 'chirality-neutral' description in the historical sentence above is withdrawn"; line 1249: "The former mask-equivalence assertion is therefore withdrawn"). This reads like an internal forensic audit, a rebuttal letter, or a tracked-changes document rather than a finalized scientific paper. The author must rewrite the manuscript to present the definitive methods and results clearly. The auditing of prior internal drafts or superseded codebases should be removed from the main narrative and relegated to a single brief appendix (if strictly necessary for provenance).
2. **[MAJOR] Integration of Reproducibility Artifacts (Throughout, e.g., lines 1060-1063, 1117-1123)**: The inclusion of exact git hashes, JSON filenames, and artifact paths is commendable for open science, but embedding raw file paths (e.g., `pipelines/p2_chirality/outputs/canonical_provenance/...`) directly into the narrative prose severely disrupts readability. These exact reproducibility pointers should be moved to footnotes, a consolidated summary table, or the Data Availability section. 
3. **[MINOR] Context for "Historical" Baselines (Section 2.2, Table 12)**: The text frequently references "conflicting historical training-data records" and an "immutable model-repository audit." It is jarring and unclear to the reader what "historical" refers to—is this an earlier public preprint by the author, a previously published paper, or simply an earlier internal version of the codebase? A brief sentence clarifying the origin and context of this "historical" baseline is needed.
4. **[MINOR] Abstract Density**: The abstract is overly dense with internal pipeline variable names, specific cut fractions, and methodological jargon (e.g., "WLS and post-MASTER harmonic results"). It should be revised to more plainly state the primary astrophysical takeaway: test-time equivariant averaging resolves classifier biases that otherwise couple with survey masks to produce spurious cosmological dipoles, resulting in a null detection.

**IS THE CENTRAL CLAIM SUPPORTED?**
The central claim that the observed large-scale chirality dipole is null is strongly supported by the rigorous implementation of test-time augmentation, which convincingly demonstrates how non-equivariant classifiers couple with survey footprints to create spurious cosmological signals.