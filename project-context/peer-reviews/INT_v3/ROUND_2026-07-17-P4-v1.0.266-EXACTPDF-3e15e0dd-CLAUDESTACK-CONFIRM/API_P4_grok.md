# INT API Review — P4 v1.0.266 — grok (grok-4.3)
paper: P4  version: v1.0.266  model: grok-4.3
provenance: commit=b65cf39fa5b77b983b74429d3f15c315de922fdd  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=3e15e0dd6200855a3866b13b010836b380ac72ae5e5ea1d4f3a5600e9e674a6e
packet: key=cc2149a561da39508880b9a5a56171c063a15f39c83a5386d349081ff46a15ec  profile=APJS-CATALOG-METHODS
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-18T03:06:22.281099Z  |  latency: 47.6s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 47.6, "modality": "native-PDF (/v1/files file_id)", "provider": "xai", "provider_reported_cost": "unavailable", "request_id": "a4964dce-0ebf-919f-b804-cc46f818210a", "requested_model": "grok-4.3", "resolved_model": "grok-4.3", "response_id": "a4964dce-0ebf-919f-b804-cc46f818210a", "usage": {"context_details": {"input_tokens": 35134, "output_tokens": 1128}, "cost_in_usd_ticks": 465309000, "input_tokens": 35134, "input_tokens_details": {"cached_tokens": 192}, "num_server_side_tools_used": 0, "num_sources_used": 0, "output_tokens": 1126, "output_tokens_details": {"reasoning_tokens": 808}, "total_tokens": 36260}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MINOR REVISIONS

(2) ISSUES:
[MINOR] Sec. 2.2 & Table 13: Historical training-composition conflict (26,616 vs. 26,626 rows; 826 vs. 846 CE non-spirals) is disclosed but left unresolved; the manifest-retained GZ1-only retrain explicitly omits the CE-ResNet component (~67.5% of the pool) and does not alter released Catalog C labels.
[MINOR] Abstract & Sec. 6.2/7: The phrasing “supports no primordial-parity bound” is technically correct for the observed-label channel but risks misreading; the coverage-calibrated A_obs^95 ≃ 0.98% is repeatedly (and correctly) qualified as an observed-label sensitivity floor only, yet the sentence structure invites conflation with a physical limit.
[MINOR] Sec. 4.1 & 4.3: The unsafe-row quarantine predicate was finalized post-review after inspection of the earlier unsafe-inclusive result; while the strict rerun is transparently documented, the change was not preregistered, creating a minor provenance ambiguity for the exact primary sample definition.

(3) The central claim—the strict quality-controlled HC real-space observed-label dipole is statistically consistent with zero—is directly supported by the checksummed fixed-occupancy null (N_selected=890,069, z_mom=+0.635, rank p=0.23768) and the matching coverage-calibrated injection test.