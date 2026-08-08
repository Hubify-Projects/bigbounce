# INT API Review — P4 v1.0.255 — grok (grok-4.3)
paper: P4  version: v1.0.255  model: grok-4.3
provenance: commit=770121acc77f9f40b730863d2bfdbddfdf62c3f8  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=f9b011a84351781b0b0e48e02e811a60ba1666296fa1f80413c918fe131c7dce
packet: key=ced0bbbefbb087ff79a31e648f42d6b95693f02efb35f289ae4213ffc65c8d30  profile=APJS-CATALOG-METHODS
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-16T00:34:27.899562Z  |  latency: 34.1s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 34.1, "modality": "native-PDF (/v1/files file_id)", "provider": "xai", "provider_reported_cost": "unavailable", "request_id": "2ab6fa44-81f5-96a8-b7f1-9867ab07f372", "requested_model": "grok-4.3", "resolved_model": "grok-4.3", "response_id": "2ab6fa44-81f5-96a8-b7f1-9867ab07f372", "usage": {"context_details": {"input_tokens": 35112, "output_tokens": 950}, "cost_in_usd_ticks": 460609000, "input_tokens": 35112, "input_tokens_details": {"cached_tokens": 192}, "num_server_side_tools_used": 0, "num_sources_used": 0, "output_tokens": 949, "output_tokens_details": {"reasoning_tokens": 575}, "total_tokens": 36061}}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
[MAJOR] Section 2.2 (Training Labels) and Table 12: Explicitly conflicting immutable audit vs. committed BENCHMARK REPORT.md records (26,616 vs. 26,626 rows; 826 vs. 846 CE non-spirals; 93.6878% vs. 92.10% accuracy) with no retained object-ID/split manifest or random-state record, rendering the training realization non-reproducible and the catalog's independence from CE-ResNet unverifiable.
[MAJOR] Section 3.2 and Table 1 (Estimator Hierarchy): Declared "primary" HC real-space null (N=949,584) is presented as standalone while the paper simultaneously retains WLS/bootstrap, MASTER ℓ=1 (+7.28σ), and hemisphere diagnostics on different supports/nulls without a joint covariance; this violates ApJS catalog+methods standards requiring a single, self-contained, reproducible claim.
[MAJOR] Section 6.2 and Appendix B: No held-out human-label set with training objects removed, no spatially resolved confusion model, and no object-level transfer function; the illustrative scalar g=0.398 is explicitly non-independent (full-overlap GZ1 includes training rows), so any downstream physical interpretation remains unsupported.
[MINOR] Section 1 and Abstract: Repeated emphasis on "standalone" and "no unpublished companion work" while acknowledging 67.5% CE-ResNet dependence and unresolved training conflicts creates an internal contradiction that must be excised or resolved.

(3) The central claim (HC observed-label real-space dipole consistent with zero at z=+0.71, rank p=0.225) is supported by the fixed-occupancy null on the declared sample.