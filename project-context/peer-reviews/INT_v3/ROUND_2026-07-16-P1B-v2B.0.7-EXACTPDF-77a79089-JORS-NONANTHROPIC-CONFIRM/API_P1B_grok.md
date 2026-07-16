# INT API Review — P1B v2B.0.7 — grok (grok-4.3)
paper: P1B  version: v2B.0.7  model: grok-4.3
provenance: commit=b4a395936b542e9417fb3a49af6741040aacdf12  pdf=arxiv/paper1b_namaster_proof.pdf  sha256=77a79089a6ab959e313639ef5cb48873cc5e1d507d2b4ec645338c38918f9582
packet: key=5eed28496d81383ef7c8e813271fc49908afb4779709d901307a97955c869de0  profile=JORS-SOFTWARE
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-16T20:22:42.655072Z  |  latency: 9.5s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 9.5, "modality": "native-PDF (/v1/files file_id)", "provider": "xai", "provider_reported_cost": "unavailable", "request_id": "8f3ed38b-243d-95bb-8064-e442578e551f", "requested_model": "grok-4.3", "resolved_model": "grok-4.3", "response_id": "8f3ed38b-243d-95bb-8064-e442578e551f", "usage": {"context_details": {"input_tokens": 6857, "output_tokens": 939}, "cost_in_usd_ticks": 99754500, "input_tokens": 6857, "input_tokens_details": {"cached_tokens": 896}, "num_server_side_tools_used": 0, "num_sources_used": 0, "output_tokens": 938, "output_tokens_details": {"reasoning_tokens": 683}, "total_tokens": 7795}}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT

(2) ISSUES:
[MAJOR] Availability §11 (and Archive paragraph): explicitly states "A persistent archival identifier is not yet available. This is an explicit submission blocker" and requires the candidate to "bind version 0.1.5 to an immutable archive before journal submission," violating JORS requirements for a citable, permanently archived release (e.g., Zenodo DOI) at submission time.
[MAJOR] Abstract/§1/§11: version string (v2B.0.7 vs. 0.1.5) and repository path (bigbounce/tree/main/packages/namaster-proof) are internally inconsistent with the claimed release; no CITATION.cff or tagged release is verifiable.
[MINOR] §7 Quality Control: maximum absolute difference (1.41×10^{-18}) is presented without the actual workspace tensor or self-contained reproducibility artifacts, weakening the compatibility claim.
[MINOR] §13 AI Usage Disclosure: lacks the required explicit statement of which sections/claims were AI-generated vs. human-verified.

(3) The central claim of exact window inference plus content-bound reproducibility is not supported, because the software has no archived release.