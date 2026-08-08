# INT API Review — P4 v1.0.256 — gemini (gemini-3.1-pro-preview)
paper: P4  version: v1.0.256  model: gemini-3.1-pro-preview
provenance: commit=0197358b17570309ba217070e43b56b55e840e23  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=6dfccf7c26d698599c3512bd91f0f73f714f967604f42f73aeaf4e9a59573110
packet: key=c16d44750a82bd43674674a9c7b4cca94fea76ccc8b3ee88e445d462b5df4b44  profile=APJS-CATALOG-METHODS
modality: native-PDF (Files/media upload file_uri)
UTC: 2026-07-16T06:27:42.251851Z  |  latency: 56.5s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 56.5, "modality": "native-PDF (Files/media upload file_uri)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "-XlYau-tA8StmtkPrYfAyAI", "usage": {"candidatesTokenCount": 621, "promptTokenCount": 15191, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 111}, {"modality": "IMAGE", "tokenCount": 15080}], "serviceTier": "standard", "thoughtsTokenCount": 1889, "totalTokenCount": 17701}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

**VERDICT:** MINOR REVISIONS

**ISSUES:**

1. **[MAJOR] Section 2.2 and Appendix B (Training Data Provenance):** The manuscript commendably and transparently acknowledges an inability to exactly reconstruct the historical training/validation splits due to conflicting repository records. However, because the exact training set is unknown, performance metrics and human-vote cross-checks derived from the GZ1 overlap (Section 6.1, Table 14) are overlap-contaminated. The author should explicitly quantify the worst-case statistical bias this contamination could inject into the primary real-space dipole measurement, or alternatively, introduce a boolean flag in the released dataset for all objects that fall within the ambiguous historical training candidate pool. 

2. **[MAJOR] Section 6.2 and 6.4 (Sensitivity Thresholds):** The manuscript convincingly establishes an "observed-label null" but explicitly leaves the physical confusion model and calibrated physical sensitivity floor open, relying instead on descriptive finite-grid injection scores. For an ApJS catalog release intended to definitively address a persistent cosmological claim, establishing a firm upper limit (e.g., a 95% confidence upper bound on a true physical dipole amplitude) is highly desirable. If computing a fully calibrated, continuous injection-recovery physical ceiling is computationally out of scope for this specific release, this limitation—and exactly what the catalog *cannot* be used to exclude regarding primordial parity—should be stated more prominently in the Abstract and Section 7 (Conclusions).

3. **[MINOR] Section 3.2 (Declared Analysis Hierarchy):** The structural framing of the methodology reads somewhat like a legal contract or a particle-physics blinding declaration (e.g., "We declare the estimator hierarchy...", "load-bearing result"). While the rigor and defensive posture are understandable given the controversial history of the chirality dipole in the literature, consolidating the heavy use of acronyms (HC-RI, FS-C, MASTER-AGF) and slightly softening the "audit" terminology would significantly improve the manuscript's readability for the broader astronomical community.

4. **[MINOR] Figures 4 and 7 (Map Color Scales):** The visual comparison between the raw (Catalog A) and equivariant (Catalog C) sky maps in Figure 7 is the methodological cornerstone of the paper and is highly effective. However, in Figure 4, the linear color scale of [-0.08, +0.08] for the asymmetry $A_p$ may visually wash out low-level coherent systematics. Adding a complementary panel showing the spatial distribution of statistical significance (e.g., a map of local $z$-scores or residuals relative to the monopole) would better visually reinforce the statistical null claim.

**One sentence:** The central claim—that applying rigorous, test-time equivariant machine learning to a massive spiral galaxy catalog eliminates instrumental/algorithmic biases and yields a strict null result for the previously claimed real-space chirality dipole—is rigorously supported by the data, controls, and methodology.