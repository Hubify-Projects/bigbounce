# INT API Review — P4 v1.0.262 — grok (grok-4.3)
paper: P4  version: v1.0.262  model: grok-4.3
provenance: commit=1a1fd5e4b587eec82f50183cbe5ec53fc273931e  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=f59fc937597efe749894eca426e623b21b918bd8e977c9edd85a75732b494cb2
packet: key=f6077529c205b9680b6bb7f7a993339800711d54a0a823495b6442a784a712b7  profile=APJS-CATALOG-METHODS
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-16T23:16:49.896530Z  |  latency: 44.6s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 44.6, "modality": "native-PDF (/v1/files file_id)", "provider": "xai", "provider_reported_cost": "unavailable", "request_id": "97cd5741-58f7-95dd-979c-da4e43c86985", "requested_model": "grok-4.3", "resolved_model": "grok-4.3", "response_id": "97cd5741-58f7-95dd-979c-da4e43c86985", "usage": {"context_details": {"input_tokens": 35949, "output_tokens": 893}, "cost_in_usd_ticks": 469646500, "input_tokens": 35949, "input_tokens_details": {"cached_tokens": 192}, "num_server_side_tools_used": 0, "num_sources_used": 0, "output_tokens": 892, "output_tokens_details": {"reasoning_tokens": 580}, "total_tokens": 36841}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MINOR REVISIONS

(2) ISSUES:
[MINOR] Sec. 2.2/Appendix B: Conflicting immutable audit (26,616 rows) vs. committed BENCHMARK REPORT.md (26,626 rows) and README accuracy (92.10% vs. 93.6878%) are disclosed but leave the exact training realization unreproducible; no object/split manifest is retained.
[MINOR] Sec. 4.1: The raw.flip.qc.unsafe quarantine (59,515 HC rows) and strict primary predicate were finalized post-review rather than pre-specified, converting an earlier unsafe-inclusive result into the declared null.
[MINOR] Sec. 3.2/4.3: Primary estimator hierarchy and support definitions (HC-RI vs. FS-C) are declared internally but the paper does not supply a joint covariance or matched-footprint cross-check against an independent classifier (e.g., CE-ResNet or Ganalyzer).
[MINOR] Sec. 6.2: Finite injection grids and scalar g=0.398 transfer are presented only as descriptive/pilot fractions; they are correctly labeled non-calibrated yet could be moved to an appendix to avoid any appearance of a physical bound.

(3) The central claim of a null observed-label dipole (zmom=+0.635, rank p=0.23768) on the quality-controlled HC sample is directly supported by the checksummed fixed-occupancy primary test.