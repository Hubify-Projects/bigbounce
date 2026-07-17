# INT API Review — P4 v1.0.264 — grok (grok-4.3)
paper: P4  version: v1.0.264  model: grok-4.3
provenance: commit=104ebb861a901c7ea61a1fb8730d77205249fdea  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=325b7ced736081a201fb5f1bc9c6283760c1296b5adcb1baf7cb503ce98cb862
packet: key=e4b51b68758fb575a56db1e63f0aba599971e1f87bb352a337bc76702e4b86de  profile=APJS-CATALOG-METHODS
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-17T21:10:21.262931Z  |  latency: 34.3s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 34.3, "modality": "native-PDF (/v1/files file_id)", "provider": "xai", "provider_reported_cost": "unavailable", "request_id": "b36e7964-1e80-9c79-bfe4-59be1622413d", "requested_model": "grok-4.3", "resolved_model": "grok-4.3", "response_id": "b36e7964-1e80-9c79-bfe4-59be1622413d", "usage": {"context_details": {"input_tokens": 35704, "output_tokens": 1102}, "cost_in_usd_ticks": 471809000, "input_tokens": 35704, "input_tokens_details": {"cached_tokens": 192}, "num_server_side_tools_used": 0, "num_sources_used": 0, "output_tokens": 1101, "output_tokens_details": {"reasoning_tokens": 651}, "total_tokens": 36805}}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
[MAJOR] Sec. 2.2 (Training Labels) and Appendix B (Table 13): Irreconcilable committed records (26,616 vs. 26,626 rows; 826 vs. 846 CE non-spirals; 93.6878% vs. 92.10% accuracy) with no retained object-ID/split manifest or random-state record render the training realization non-reproducible, violating APJS catalog/methods standards for executable provenance.
[MAJOR] Sec. 4.1 and 4.3 (Raw/flip quarantine): The `raw_flip_qc_unsafe` predicate and strict primary sample (N=890,069) were introduced and finalized during post-review closure after inspection of the unsafe-inclusive result; this is explicitly not preregistered and changes the declared analysis hierarchy after unblinding.
[MAJOR] Sec. 3.2 and 4.5 (Analysis hierarchy): The sole primary result is declared to rest on one estimator/null combination, yet the paper retains multiple non-commensurable diagnostics (WLS, MASTER, block-bootstrap) whose joint covariance is computed only after reviewer request; the text does not demonstrate that the chosen primary is robust to reasonable variations in support or null family.
[MINOR] Sec. 5 (Comparison with previous work): All literature comparisons are stated to be qualitative only because no matched-footprint independent-estimator analysis is performed; the abstract and introduction nonetheless frame the work as a direct test of prior claims without quantifying the mismatch.
[MINOR] Sec. 6.2 and Appendix B: The GZ1-overlap confusion matrix is overlap-contaminated (training rows not removed) and the scalar transfer factor g=0.398 is explicitly illustrative only; the paper does not supply the spatially resolved directional confusion model required to convert observed-label results into physical bounds.

(3) The central claim (strict quality-controlled HC real-space dipole null at zmom=+0.635, rank p=0.23768) is supported by the fixed-occupancy label-randomization test on the declared sample.