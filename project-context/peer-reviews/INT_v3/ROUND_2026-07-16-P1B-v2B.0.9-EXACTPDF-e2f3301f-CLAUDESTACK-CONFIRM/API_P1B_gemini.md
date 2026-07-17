# INT API Review — P1B v2B.0.9 — gemini (gemini-3.1-pro-preview)
paper: P1B  version: v2B.0.9  model: gemini-3.1-pro-preview
provenance: commit=23b4afb8a454a16b72ed78c1c11a9c04df4b45a7  pdf=arxiv/paper1b_namaster_proof.pdf  sha256=e2f3301fe74ba2f64ba41d87ec3648a6e3980e8715562ab27440f80ae448bc68
packet: key=6d5bd06cf86a9a620e6168f6d4015d0bb07f823b3235a3cf68ff439cb0f53f99  profile=JORS-SOFTWARE
modality: native-PDF (inline_data base64)
UTC: 2026-07-17T00:44:18.289301Z  |  latency: 20.6s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 20.6, "modality": "native-PDF (inline_data base64)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "43pZau-JB8mHqtsPsPrEqQk", "usage": {"candidatesTokenCount": 393, "promptTokenCount": 3227, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 3120}, {"modality": "TEXT", "tokenCount": 107}], "serviceTier": "standard", "thoughtsTokenCount": 1556, "totalTokenCount": 5176}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

VERDICT: MINOR REVISIONS

ISSUES:
1. [MAJOR] Section 11 (Availability - Archive): JORS strictly requires a persistent archival identifier (e.g., a Zenodo, Figshare, or Software Heritage DOI) that points to the exact version of the software described in the paper. As explicitly acknowledged in the manuscript, this is a submission blocker; the software must be deposited in a compliant repository and the resulting DOI must be added to the manuscript before it can be accepted for publication.
2. [MINOR] Section 11 (Availability - Code repository): Because the software is hosted within a monorepo (`Hubify-Projects/bigbounce/tree/main/packages/namaster-proof`), depositing the archive to a service like Zenodo will likely archive the entire monorepo. Please ensure the final archival metadata and the manuscript clearly direct users to the specific `namaster-proof` subdirectory within the archived release.
3. [MINOR] Section 7 (Quality Control): The phrasing "in a standalone package install 39 run and the 2 replay-equivalence tests skip cleanly" is slightly awkward to read. Consider rephrasing for clarity (e.g., "during a standalone package installation, 39 tests run while the 2 replay-equivalence tests cleanly skip"). 
4. [MINOR] Section 8 (Worked Examples): It would be beneficial to briefly mention the expected computational cost or execution time for the "Real PyMaster integration" and "Synthetic CMB recovery campaign" examples to give readers a sense of the package's overhead in production scenarios.

The central claim that `namaster-proof` provides a mathematically exact, rigorously tested verification and provenance layer for spin-2 pseudo-$C_\ell$ analyses is well-supported by the detailed exact-window algebra, extensive automated testing, and comprehensive fail-closed receipt mechanisms described in the text.