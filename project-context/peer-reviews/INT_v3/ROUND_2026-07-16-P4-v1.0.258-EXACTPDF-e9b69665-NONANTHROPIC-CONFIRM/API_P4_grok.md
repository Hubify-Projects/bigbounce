# INT API Review — P4 v1.0.258 — grok (grok-4.3)
paper: P4  version: v1.0.258  model: grok-4.3
provenance: commit=68d7e2541aa48de03c15133f7aa9f3b8e1cce5ac  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=e9b69665efdf757de69f27a0474d30ac4bc48bc7559424e077f41c7bcacbe061
packet: key=cb871f150285d1efd9d3ee8a56bd45fde9547ce22ee4bf93ab681a1b31f1dae1  profile=APJS-CATALOG-METHODS
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-16T08:29:14.978121Z  |  latency: 44.4s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 44.4, "modality": "native-PDF (/v1/files file_id)", "provider": "xai", "provider_reported_cost": "unavailable", "request_id": "710353c1-c067-9228-8a63-b69da2a90250", "requested_model": "grok-4.3", "resolved_model": "grok-4.3", "response_id": "710353c1-c067-9228-8a63-b69da2a90250", "usage": {"context_details": {"input_tokens": 34371, "output_tokens": 971}, "cost_in_usd_ticks": 451871500, "input_tokens": 34371, "input_tokens_details": {"cached_tokens": 192}, "num_server_side_tools_used": 0, "num_sources_used": 0, "output_tokens": 970, "output_tokens_details": {"reasoning_tokens": 645}, "total_tokens": 35341}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MINOR REVISIONS

(2) ISSUES:
[MINOR] Sec. 2.2: Conflicting committed training records (26,616 vs. 26,626 rows; 93.6878% vs. 92.10% accuracy; 826 vs. 846 CE non-spirals) are disclosed but unresolved, with no retained object/split manifest or random-state record, undermining exact reproducibility of the historical training realization.
[MINOR] Sec. 2.2 & App. B: GZ1-overlap confusion matrix and agreement metrics (69.91%, κ=0.40) are overlap-contaminated because the 6,637 GZ1 training rows were not removed from the evaluation set; this must be explicitly quantified or an anti-join performed.
[MINOR] Sec. 3.2 & 4.3: The declared analysis hierarchy and primary null (HC-RI, N=890,069) are clearly stated, but the paper should add an explicit statement that the unsafe-row quarantine predicate was finalized before unblinding the primary dipole result.
[MINOR] Sec. 6.2: The illustrative scalar transfer factor g≈0.398 is presented without a spatially resolved confusion model; the text already notes this limitation but should add a one-sentence caveat that no physical amplitude bound is claimed.

(3) The central claim (QC HC real-space observed-label dipole is null-consistent at zmom=+0.635, rank p=0.23768) is supported.