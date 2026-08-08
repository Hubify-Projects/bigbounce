# INT API Review — P4 v1.0.258 — gemini (gemini-3.1-pro-preview)
paper: P4  version: v1.0.258  model: gemini-3.1-pro-preview
provenance: commit=68d7e2541aa48de03c15133f7aa9f3b8e1cce5ac  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=e9b69665efdf757de69f27a0474d30ac4bc48bc7559424e077f41c7bcacbe061
packet: key=474acf2e4a4aa06915e3973c615718fcef2503bb53cfcd6922ebb2d02f310e6f  profile=APJS-CATALOG-METHODS
modality: native-PDF (Files/media upload file_uri)
UTC: 2026-07-16T08:29:14.955479Z  |  latency: 75.1s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 75.1, "modality": "native-PDF (Files/media upload file_uri)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "hpZYavC6O-ucz7IPwcW5yA4", "usage": {"candidatesTokenCount": 648, "promptTokenCount": 13111, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 13000}, {"modality": "TEXT", "tokenCount": 111}], "serviceTier": "standard", "thoughtsTokenCount": 1538, "totalTokenCount": 15297}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

**VERDICT:** MINOR REVISIONS

**ISSUES:**

1. **[MAJOR] Section 4 / Section 6 / Appendix C (Data Provenance and File Paths):** The manuscript makes extensive inline references to local file paths (e.g., `pipelines/p2_chirality/outputs/canonical_provenance/stage_b_hybrid_image_field_recovery.json` on lines 737-739). While the Data Availability section notes a Zenodo deposit will be made, citing raw software paths in the main text disrupts readability and assumes the reader has the repository open. The text must explicitly summarize the *contents and scientific meaning* of these JSON files (e.g., summary statistics, raw coordinate arrays) so the paper stands alone, and these references should be formatted as standard citations or footnotes pointing to the data repository.
2. **[MINOR] Section 2.2 and Table 12 (Training Reproducibility):** The author transparently notes that the exact training random state and object/split manifests were not retained (lines 114-117 and Table 12). For an ApJS catalog heavily emphasizing strict cryptographic reproducibility (SHA-256 hashes), the manuscript should include a brief, explicit statement clarifying that the loss of the training state does not compromise the exact reproducibility of the *inference* pass and the resulting public catalog, which are the primary scientific products. 
3. **[MINOR] Terminology and Accessibility (Throughout):** The manuscript relies heavily on dense software-engineering and auditing terminology (e.g., "computational-closure ledger", "immutable model-repository receipt", "commit-pinned"). While rigorous, this language is atypical for astronomical literature and may alienate the target audience. The author should consider adding a brief subsection or glossary defining these terms in the context of standard astronomical data releases (e.g., mapping "computational-closure ledger" to "reproducibility manifest").
4. **[MINOR] Section 4.4 (Generative Null Definition):** The term "binomial-monopole generative null" (lines 487-493) is crucial for understanding the masking leakage systematics, but its exact mathematical construction is slightly buried. The text should explicitly state the formula in the main text (e.g., drawing $N_{CW}$ per pixel from a Binomial distribution governed by the global observed fraction and the local $N_{spiral}$ depth) to ensure the baseline is instantly clear to cosmological-statistics readers. 
5. **[MINOR] Figure 8 (Formatting):** The layout of Figure 8 and its caption on page 14 is severely compressed and floats awkwardly over text/blank space. This must be corrected in the LaTeX formatting for the final typesetting.

**One sentence:** The central claim that the observed-label chirality dipole in DESI Legacy DR8 spirals is completely consistent with zero—and that previous non-zero claims are likely driven by survey footprint and mask-leakage systematics—is exceptionally well-supported by the rigorous equivariant pipeline and robust statistical diagnostics provided in this catalog.