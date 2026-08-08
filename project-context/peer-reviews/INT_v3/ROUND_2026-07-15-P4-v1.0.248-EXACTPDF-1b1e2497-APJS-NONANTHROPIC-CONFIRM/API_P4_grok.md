# INT API Review — P4 v1.0.248 — grok (grok-4.3)
paper: P4  version: v1.0.248  model: grok-4.3
provenance: commit=5bc450274afa05cf7d6d3a14ca54d66279c83176  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=1b1e2497f5a4083d41b2d56fb627cbced60b8a9ec95da595d86c8d244052d937
packet: key=8444880f5942455e88b75ca4e7bf9d09d357b41a5d806db2710fe259e71c67bd  profile=APJS-CATALOG-METHODS
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-15T12:09:14.906977Z  |  latency: 46.7s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 46.7, "modality": "native-PDF (/v1/files file_id)", "provider": "xai", "provider_reported_cost": "unavailable", "request_id": "0257bf1e-e4b5-930b-a270-f795a6384002", "requested_model": "grok-4.3", "resolved_model": "grok-4.3", "response_id": "0257bf1e-e4b5-930b-a270-f795a6384002", "usage": {"context_details": {"input_tokens": 35870, "output_tokens": 1213}, "cost_in_usd_ticks": 476659000, "input_tokens": 35870, "input_tokens_details": {"cached_tokens": 192}, "num_server_side_tools_used": 0, "num_sources_used": 0, "output_tokens": 1212, "output_tokens_details": {"reasoning_tokens": 806}, "total_tokens": 37082}}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
1. [MAJOR] Section II.B (Training Labels) and Table XII: Irreconcilable committed historical records (26,616 vs. 26,626 rows; 93.6878% vs. 92.10% validation accuracy; 826 vs. 846 CE non-spirals) with no retained object/split manifest or random-state record render the exact training realization non-reproducible, violating ApJS catalog standards for verifiable provenance.
2. [MAJOR] Section III.E (Catalog Tiers) and Data Availability: The science-facing release explicitly quarantines 249,066 rows (including 59,515 HC) as "do_not_use_for_science" and strips raw/flip-pass scores without providing a machine-readable, executable schema or checksum-verified reproducer that allows independent users to regenerate the exact HC selection and null array from the parent Smith42/galaxies dataset.
3. [MINOR] Section IV.C and VI.B (Dipole Analysis; Finite Injection Scores): The 20-axis deterministic Stage-B pilot and 100-injection grids report uncalibrated score-pass fractions (e.g., 16/20 at A=0.75%) without coverage statements, joint covariance, or spatial-transfer mapping, rendering sensitivity claims descriptive only and potentially misleading for an ApJS catalog audience.
4. [MINOR] Appendix B (Classifier Architecture Details): The loss function, TTA implementation, and bias-hardening suite (T1–T8) are described at high level without the exact training script, checkpoint SHA-256 verification steps, or per-galaxy truth-label hold-out manifest required for full methods reproducibility.

(3) The central claim (HC observed-label real-space dipole null at +0.71σ, p=0.225 on N_selected=949,584 under fixed-occupancy randomization) is supported by the reported estimator and null test.