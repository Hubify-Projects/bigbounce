# INT API Review — P4 v1.0.261 — grok (grok-4.3)
paper: P4  version: v1.0.261  model: grok-4.3
provenance: commit=21fbef5d36b2f4e7ae4ee4482e028af5ab73f6d9  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=60d96cde47cee1475d58273a4e14fc41046abebf03d89fd50cb03bf10f6f0a64
packet: key=dc950a6778ee6ae2958307c87e465be6b3d62dfed9064f836f5aec3a0c2605e1  profile=APJS-CATALOG-METHODS
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-16T22:50:12.330240Z  |  latency: 38.9s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 38.9, "modality": "native-PDF (/v1/files file_id)", "provider": "xai", "provider_reported_cost": "unavailable", "request_id": "c8170f16-9bd9-9371-99cd-ff1f30894243", "requested_model": "grok-4.3", "resolved_model": "grok-4.3", "response_id": "c8170f16-9bd9-9371-99cd-ff1f30894243", "usage": {"context_details": {"input_tokens": 34873, "output_tokens": 1082}, "cost_in_usd_ticks": 460921500, "input_tokens": 34873, "input_tokens_details": {"cached_tokens": 192}, "num_server_side_tools_used": 0, "num_sources_used": 0, "output_tokens": 1081, "output_tokens_details": {"reasoning_tokens": 665}, "total_tokens": 35954}}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
[MAJOR] Section 2.2 (Training Labels): Conflicting immutable audit (26,616 rows, 826 CE non-spirals, 93.6878% accuracy) vs. committed BENCHMARK REPORT.md (26,626 rows, 846 CE non-spirals, 92.10% accuracy) with no retained object/split manifest, random-state record, or run receipt prevents exact reproduction of the training realization.
[MAJOR] Sections 3.2, 4.1, 4.3 (Declared Analysis Hierarchy & Primary Estimator): Unsafe-row quarantine (59,515 rows) was introduced post-review and not preregistered; the strict primary result (N=890,069, zmom=+0.635, p=0.23768) is therefore a corrective analysis rather than a pre-specified blinded test.
[MAJOR] Section 6.2 (Finite Injection Scores) & Appendix B: Stage-B deterministic-axis pilot and GZ1-overlap confusion matrix are overlap-contaminated (training rows not removed) and provide only descriptive fractions, not a spatially resolved physical transfer function or calibrated coverage for the claimed sub-percent sensitivity.
[MINOR] Abstract & Section 6.3: Claim that the parity-even observable “supports no primordial-parity bound” is unsupported without a derived galaxy-formation transfer function (explicitly stated as absent).
[MINOR] Section 3.5 & Data Availability: Catalog A (raw) and Catalog B (Platt) are retained only as “historical diagnostics” with no complete executable release contract or byte-verified payload, weakening the catalog-methods emphasis of an ApJS submission.

(3) Yes, the central claim of a null result (zmom=+0.635, one-sided rank p=0.23768) on the strict quality-controlled HC real-space sample is supported by the reported fixed-occupancy null array and checksummed statistics.