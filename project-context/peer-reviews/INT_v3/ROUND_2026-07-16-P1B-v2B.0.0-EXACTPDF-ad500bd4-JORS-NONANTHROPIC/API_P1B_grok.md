# INT API Review — P1B v2B.0.0 — grok (grok-4.3)
paper: P1B  version: v2B.0.0  model: grok-4.3
provenance: commit=3475392b5ec27be5790580330b40e76f7abd0b5c  pdf=arxiv/paper1b_namaster_proof.pdf  sha256=ad500bd4e8d689628ad3a383e512a1ddd7a1e329b5580e1d41e30637266c75a0
packet: key=d13fac2b4358e1de94cbd19976ee4129ed5715ae29963064ef90bc3e9804da5b  profile=JORS-SOFTWARE
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-16T17:39:54.772558Z  |  latency: 12.4s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 12.4, "modality": "native-PDF (/v1/files file_id)", "provider": "xai", "provider_reported_cost": "unavailable", "request_id": "191acba3-5242-9aa0-af89-fbb144dd124d", "requested_model": "grok-4.3", "resolved_model": "grok-4.3", "response_id": "191acba3-5242-9aa0-af89-fbb144dd124d", "usage": {"context_details": {"input_tokens": 5633, "output_tokens": 1004}, "cost_in_usd_ticks": 94143500, "input_tokens": 5633, "input_tokens_details": {"cached_tokens": 128}, "num_server_side_tools_used": 0, "num_sources_used": 0, "output_tokens": 1003, "output_tokens_details": {"reasoning_tokens": 782}, "total_tokens": 6636}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MINOR REVISIONS

(2) ISSUES:
[MINOR] Header (title page) + abstract: version string "v2B.0.0" conflicts with every subsequent reference to "Version 0.1.0" (sections 6, 9).
[MINOR] Section 6 (Validation and Tests): reports a single absolute difference of 1.41 × 10^{-18} for one specific workspace shape without stating the tolerance, floating-point model, or whether this constitutes numerical equivalence under all conditions.
[MINOR] Section 9 (Availability): states that "a persistent archival DOI and an independent package index release are not yet available" while simultaneously claiming the software is ready for citation and reuse; JORS policy expects at least a citable release artifact at submission.

(3) Yes, the central claim that the package supplies exact window inference plus tamper-evident provenance is supported by the described pre-contraction algebra, atomic publish/verify routines, 19 passing tests, and the production compatibility check.