# INT API Review — P1B v2B.0.13 — grok (grok-4.3)
paper: P1B  version: v2B.0.13  model: grok-4.3
provenance: commit=44b666cb045f405383bf88aa49f8ed0e252f0a67  pdf=arxiv/paper1b_namaster_proof.pdf  sha256=a84bea85ad993f02230d439825e9a220be894e390e0d1f172d046e50c687cbee
packet: key=43e6d95c977c86fb489109b019b581b72531492ab5217c25c02dcfe304c02a2a  profile=JORS-SOFTWARE
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-23T00:08:16.381152Z  |  latency: 16.8s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 16.8, "modality": "native-PDF (/v1/files file_id)", "provider": "xai", "provider_reported_cost": "unavailable", "request_id": "f35b39c0-71fe-9540-b8ba-7980b45cfe3b", "requested_model": "grok-4.3", "resolved_model": "grok-4.3", "response_id": "f35b39c0-71fe-9540-b8ba-7980b45cfe3b", "usage": {"context_details": {"input_tokens": 8117, "output_tokens": 1085}, "cost_in_usd_ticks": 126546500, "input_tokens": 8117, "input_tokens_details": {"cached_tokens": 192}, "num_server_side_tools_used": 0, "num_sources_used": 0, "output_tokens": 1084, "output_tokens_details": {"reasoning_tokens": 793}, "total_tokens": 9201}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MINOR REVISIONS

(2) ISSUES:
[MINOR] Header (page 1) and Availability/Quality Control (sections 7, 11): version string v2B.0.13 appears only in the title block while the body repeatedly cites “Version 0.1.7” (including test count, PyPI/conda details, and Zenodo deposit), creating an irreproducible mismatch between the declared release and the documented artifact.
[MINOR] Section 11 (Availability): the GitHub path, commit hash, and both Zenodo DOIs are given, yet no PyPI/conda package name, sdist/wheel, or `pip install namaster-proof` command is supplied, contrary to JORS expectations for a reusable Python package.
[MINOR] Section 8 (Worked Examples): the “synthetic CMB recovery campaign” reports exact angle recoveries (0.270° ↦ 0.270°, etc.) without releasing the 500-realization input spectra, seeds, or mask files, so the numerical claims cannot be independently re-run from the manuscript alone.

(3) The central claim—that namaster-proof supplies an auditable, exact-window verification layer plus content-bound receipts that demonstrably eliminate the two stated error classes—is supported by the 41 passing tests, synthetic-operator equivalence checks, and atomic-receipt failure cases described.