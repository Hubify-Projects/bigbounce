# INT API Review — P4 v1.0.252 — grok (grok-4.3)
paper: P4  version: v1.0.252  model: grok-4.3
provenance: commit=40d99073618cb6ce5ae6f6c3410e52ef0a1685be  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=a109f3d150ff02107bc10bc7dec576ad28b0157081b3e521da86e7c06ade3292
packet: key=a083d1ba3e6106d4c396b035af921b990b30d3e5ae90c3bf976c062095210206  profile=APJS-CATALOG-METHODS
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-15T20:14:07.199870Z  |  latency: 48.6s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 48.6, "modality": "native-PDF (/v1/files file_id)", "provider": "xai", "provider_reported_cost": "unavailable", "request_id": "1a64f24c-9263-9b71-9a29-34111d5cb724", "requested_model": "grok-4.3", "resolved_model": "grok-4.3", "response_id": "1a64f24c-9263-9b71-9a29-34111d5cb724", "usage": {"context_details": {"input_tokens": 35939, "output_tokens": 1168}, "cost_in_usd_ticks": 477068500, "input_tokens": 35939, "input_tokens_details": {"cached_tokens": 128}, "num_server_side_tools_used": 0, "num_sources_used": 0, "output_tokens": 1167, "output_tokens_details": {"reasoning_tokens": 835}, "total_tokens": 37106}}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
[MAJOR] Section 2.2 (Training Labels): Conflicting committed records (26,616 vs. 26,626 rows; 826 vs. 846 CE non-spirals; 93.6878% vs. 92.10% validation accuracy) with no retained object/split manifest or random-state record make the classifier training non-reproducible, directly undermining the catalog-generation methods central to an APJS-CATALOG-METHODS submission.
[MAJOR] Section 3.2 and Abstract: The "single primary science sample" (HC \(p_{eq}>0.6\)) and its null result are declared post-hoc without preregistration or blinding record, while the abstract's claim that the parity-even observable "supports no primordial-parity bound" is correct but risks overstating scope given the explicit parity-even/transfer-function caveats in Sec. 6.3.
[MINOR] Section 4.1 (Raw/flip quarantine): The 249,066 unsafe rows (including 59,515 in the HC sample) are quarantined with a Boolean flag, but the paper does not provide a quantitative sensitivity test showing the primary \(z=+0.71\) result is robust to their inclusion/exclusion under the fixed-occupancy null.

(3) The central claim of a null-consistent HC real-space dipole (\(z=+0.71\), rank \(p=0.225\)) is supported by the fixed-occupancy label-randomization test on the released catalog.