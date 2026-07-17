# INT API Review — P1B v2B.0.10 — grok (grok-4.3)
paper: P1B  version: v2B.0.10  model: grok-4.3
provenance: commit=8ebefbfd3656141304c58a1207e00461c89b43d1  pdf=arxiv/paper1b_namaster_proof.pdf  sha256=c7883afc5050600998b612d7c8a894c7352b5b3770e442befd2b30f78b502673
packet: key=afb4464a60ec6c42b31cea1974f312d84e04f26b8065087c384befe75532a735  profile=JORS-SOFTWARE
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-17T01:22:12.262493Z  |  latency: 11.2s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 11.2, "modality": "native-PDF (/v1/files file_id)", "provider": "xai", "provider_reported_cost": "unavailable", "request_id": "f49a700a-f27a-98fd-9715-18b7ba4cdee7", "requested_model": "grok-4.3", "resolved_model": "grok-4.3", "response_id": "f49a700a-f27a-98fd-9715-18b7ba4cdee7", "usage": {"context_details": {"input_tokens": 7940, "output_tokens": 887}, "cost_in_usd_ticks": 119384000, "input_tokens": 7940, "input_tokens_details": {"cached_tokens": 192}, "num_server_side_tools_used": 0, "num_sources_used": 0, "output_tokens": 886, "output_tokens_details": {"reasoning_tokens": 606}, "total_tokens": 8826}}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT

(2) ISSUES:
[MAJOR] Availability §11: explicitly states "A persistent archival identifier is not yet available. This is an explicit submission blocker" and requires binding v0.1.7 to an immutable archive before journal submission, yet none is provided (only GitHub tree and two SHA-256 artifacts).
[MAJOR] Header + Quality Control §7 + Availability §11: version stated as "v2B.0.10" on title page but all technical claims, test counts, and requirements refer to "Version 0.1.7" with no reconciliation or changelog.
[MINOR] Abstract + §3 + §10: repeatedly asserts the package "is not a sky-analysis pipeline" and lists narrow scope, yet §8 worked examples and production campaign describe end-to-end synthetic recovery runs without clarifying how this avoids over-claiming utility.
[MINOR] §6 Content Validation: describes atomic replacement and fail-closed behavior but notes "The two files are not one filesystem transaction" without providing a concrete mitigation or external-anchor example in the text.

(3) The central claim that namaster-proof supplies exact, reusable, content-bound window inference and provenance for NaMaster spin-2 analyses is supported by the documented API, tests, and algebraic derivation, but the submission itself is not.