# INT API Review — P4 v1.0.265 — grok (grok-4.3)
paper: P4  version: v1.0.265  model: grok-4.3
provenance: commit=e0faf5c1fcf48c67e20e596aaba64f49379255de  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=67a08a4d3255a6fab0eadacd96580491ac20ae77abda50c55847506f49c16fc5
packet: key=be2d4f0530b8b30f897fd2173af2e1b1a4940c32d100cfb1b348e44b3379ee3d  profile=APJS-CATALOG-METHODS
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-17T21:54:19.245212Z  |  latency: 68.5s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 68.5, "modality": "native-PDF (/v1/files file_id)", "provider": "xai", "provider_reported_cost": "unavailable", "request_id": "47f860bd-6747-9327-adf1-5676fac9edbd", "requested_model": "grok-4.3", "resolved_model": "grok-4.3", "response_id": "47f860bd-6747-9327-adf1-5676fac9edbd", "usage": {"context_details": {"input_tokens": 35660, "output_tokens": 1111}, "cost_in_usd_ticks": 471484000, "input_tokens": 35660, "input_tokens_details": {"cached_tokens": 192}, "num_server_side_tools_used": 0, "num_sources_used": 0, "output_tokens": 1110, "output_tokens_details": {"reasoning_tokens": 801}, "total_tokens": 36770}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MINOR REVISIONS

(2) ISSUES:
[MINOR] Sec. 2.2 (Training Labels): Conflicting committed values for labeled rows (26,616 vs. 26,626), CE non-spirals (826 vs. 846), and validation accuracy (93.6878% vs. 92.10%) are acknowledged but left unresolved with no retained object/split manifest or random-state record, directly impairing exact reproducibility of the training realization.
[MINOR] Sec. 4.1 (Raw/flip quarantine): The executable predicate primary_hc && !raw_flip_qc_unsafe and exclusion of 59,515 rows were introduced and finalized post-review during closure after inspection of an earlier result; this is explicitly noted as not preregistered, violating standard expectations for a methods/catalog paper even if the effect on the dipole is small.
[MINOR] Sec. 3.2 & Table 1 (Declared Analysis Hierarchy): The explicit statement that this is “an internal hierarchy declaration, not a claim of formal preregistration or independent blinding” is appropriate but should be elevated to the abstract or introduction to avoid any misreading of the single primary row as a blinded confirmatory test.

(3) The central claim of a null observed-label chirality dipole (zmom = +0.635, one-sided rank p = 0.23768) on the 890,069 quality-controlled high-confidence spirals is supported.