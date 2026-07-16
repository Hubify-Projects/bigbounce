# INT API Review — P1B v2B.0.8 — grok (grok-4.3)
paper: P1B  version: v2B.0.8  model: grok-4.3
provenance: commit=92aa27549f542a0eda62477436535441ada87533  pdf=arxiv/paper1b_namaster_proof.pdf  sha256=cf7ede299ee5d6c28209817c7a0ee195000fe8dd77c276e830d8d04f5d2c3195
packet: key=6582972d9371c4fa487bde5fe3ec59252aa2639d52fcb004594320fccee2208a  profile=JORS-SOFTWARE
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-16T20:34:07.626757Z  |  latency: 10.3s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 10.3, "modality": "native-PDF (/v1/files file_id)", "provider": "xai", "provider_reported_cost": "unavailable", "request_id": "5798ad02-3aad-9464-b566-47be22570196", "requested_model": "grok-4.3", "resolved_model": "grok-4.3", "response_id": "5798ad02-3aad-9464-b566-47be22570196", "usage": {"context_details": {"input_tokens": 6979, "output_tokens": 818}, "cost_in_usd_ticks": 98254500, "input_tokens": 6979, "input_tokens_details": {"cached_tokens": 896}, "num_server_side_tools_used": 0, "num_sources_used": 0, "output_tokens": 817, "output_tokens_details": {"reasoning_tokens": 590}, "total_tokens": 7796}}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT

(2) ISSUES:
[MAJOR] Section 11 (Availability/Archive): paper explicitly states "A persistent archival identifier is not yet available. This is an explicit submission blocker" and requires version 0.1.6 to be bound before submission, violating JORS requirements for deposited, citable software.
[MAJOR] Section 7 (Quality Control) and header: version mismatch between "v2B.0.8" (title page) and repeated claims of "Version 0.1.6" with 41 tests, preventing verification of the released artifact.
[MINOR] Section 11 (Availability): GitHub link points to a tree/main/packages/... path with no DOI/Zenodo archive or CITATION.cff validation possible, and no demonstration that the claimed PyMaster 2.6 compatibility tests are publicly reproducible.

(3) The central claim (exact window inference plus content-bound receipts enable reproducible spin-2 analyses) is not supported because the manuscript itself declares the software unarchived and thus unsubmittable.