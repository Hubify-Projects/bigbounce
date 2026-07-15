# INT API Review — P4 v1.0.247 — gemini (gemini-3.1-pro-preview)
paper: P4  version: v1.0.247  model: gemini-3.1-pro-preview
provenance: commit=567136d0d9cd68eccb84e690acf383b039aa4f95  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=a4d915112ab264eefbcf5f250ed5404c2af230fac65bece41b3125133f22ba58
packet: key=8e5b5b03f060da839e4395628e8a4c0c52acb3a887376a7c6e6592d576e7a9ad  profile=APJS-CATALOG-METHODS
modality: native-PDF (Files/media upload file_uri)
UTC: 2026-07-15T11:33:28.118051Z  |  latency: 55.6s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 55.6, "modality": "native-PDF (Files/media upload file_uri)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "IXBXap38LZmFz7IPldmkiA0", "usage": {"candidatesTokenCount": 553, "promptTokenCount": 14151, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 14040}, {"modality": "TEXT", "tokenCount": 111}], "serviceTier": "standard", "thoughtsTokenCount": 1845, "totalTokenCount": 16549}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

VERDICT: MINOR REVISIONS

ISSUES:
1. [MAJOR] Presentation and readability. The main text is severely cluttered with software audit trails, CI/CD pipeline jargon, inline JSON filenames (e.g., `artifact pipelines/p2_chirality/outputs/canonical_provenance/c11_meta_m4_slab_stats.json`), and specific commit SHA-256 hashes. While the commitment to exact computational reproducibility is highly commendable and fitting for ApJS, this presentation style interrupts the scientific narrative and makes the paper read like a software engineering audit rather than an astrophysics manuscript. All inline filenames, specific commit hashes, and codebase path references should be moved to footnotes, an appendix, or a dedicated reproducibility index table.
2. [MAJOR] Physical constraint limitations. The author is commendably transparent that the $+0.71\sigma$ null is an "observed-label" null and that the illustrative scalar transfer ($g=0.398$) does not constitute a calibrated physical bound. However, because a spatially resolved confusion model is not derived, the catalog currently provides no strict physical upper limit on a cosmological parity-violating signal. The abstract and conclusions should be slightly expanded to explicitly state that placing a physical upper limit on cosmic birefringence/parity violation using this catalog requires the future development of an object-level morphology/depth transfer function.
3. [MINOR] Nomenclature and acronym overload. The manuscript uses a dense web of internal operational definitions (e.g., HC-RI, FS-C, MASTER-AGF, P1, D1-D2, Stage-A/B, artifact c9a). Even with the summary tables, keeping track of these distinct support masks and diagnostic tiers is exhausting for the reader. Please streamline the nomenclature where possible, or provide a single, highly visible glossary/cheat-sheet for the acronyms early in the methodology section.
4. [MINOR] Conflicting training records. Section II.B and Table XII disclose a conflict in the historical training-data records (26,616 vs 26,626 rows, differing validation accuracies). Please add a brief concluding sentence in this section explicitly stating whether this missing provenance poses any risk of harboring non-equivariant biases, or if the test-time augmentation (TTA) strictly guarantees that the exact training realization is irrelevant to the final dipole map.

The central claim that the observed-label chirality dipole is null, and that previous literature detections likely stemmed from a combination of classifier bias and monopole-mask leakage, is robustly supported by the rigorous test-time equivariant averaging and pseudo-$C_\ell$ mode-coupling analysis.
