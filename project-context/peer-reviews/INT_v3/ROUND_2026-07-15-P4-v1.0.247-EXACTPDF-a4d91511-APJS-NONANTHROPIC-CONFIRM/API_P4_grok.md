# INT API Review — P4 v1.0.247 — grok (grok-4.3)
paper: P4  version: v1.0.247  model: grok-4.3
provenance: commit=567136d0d9cd68eccb84e690acf383b039aa4f95  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=a4d915112ab264eefbcf5f250ed5404c2af230fac65bece41b3125133f22ba58
packet: key=d8c281c84e827cf24e65ae89ac11367a2fc34cf4b6ad4bf552fb495ad2b823fb  profile=APJS-CATALOG-METHODS
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-15T11:33:28.068375Z  |  latency: 41.0s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 41.0, "modality": "native-PDF (/v1/files file_id)", "provider": "xai", "provider_reported_cost": "unavailable", "request_id": "75f6cb71-6fe1-96c8-b1c1-9fe41e928ce0", "requested_model": "grok-4.3", "resolved_model": "grok-4.3", "response_id": "75f6cb71-6fe1-96c8-b1c1-9fe41e928ce0", "usage": {"context_details": {"input_tokens": 36010, "output_tokens": 935}, "cost_in_usd_ticks": 471484000, "input_tokens": 36010, "input_tokens_details": {"cached_tokens": 192}, "num_server_side_tools_used": 0, "num_sources_used": 0, "output_tokens": 935, "output_tokens_details": {"reasoning_tokens": 611}, "total_tokens": 36945}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MINOR REVISIONS

(2) ISSUES:
[MAJOR] Sec. II.B & Table XII: Irreconcilable conflicting historical training records (26,616 vs. 26,626 rows; 826 vs. 846 CE non-spirals; 93.6878% vs. 92.10% accuracy) with no retained object/split manifest or random-state record, directly violating ApJS reproducibility standards for catalog papers.
[MAJOR] Sec. III.B & Table I: Declared internal estimator hierarchy and primary-sample choice (peq>0.6) are presented without external preregistration, blinding, or timestamped freeze, weakening the claim that the HC real-space row is the sole load-bearing cosmological result.
[MINOR] Sec. VI.B & Table IX: Finite-grid injection scores (e.g., 16/20 at A=0.75%) and Stage-B deterministic-axis surrogates are reported without calibrated coverage, recovery thresholds, or joint nuisance covariance, and the paper correctly flags them as non-physical pilots.
[MINOR] Data Availability & App. B: Quarantine of 249,066 reconstruction violators and omission of raw/flip scores are well documented, but the exact SHA-256 of the null array and executable schema should be elevated to a machine-readable manifest file.

(3) The central claim—that the HC observed-label real-space dipole is null-consistent at +0.71σ—is supported by the fixed-occupancy label-randomization test on the declared primary sample.