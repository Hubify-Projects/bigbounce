# INT API Review — P1B v2B.0.4 — gemini (gemini-3.1-pro-preview)
paper: P1B  version: v2B.0.4  model: gemini-3.1-pro-preview
provenance: commit=f9307445092f16da7634013a89b1ee03bcba8f6d  pdf=arxiv/paper1b_namaster_proof.pdf  sha256=dfe16983718fc8073f256c86a653d6fc3de7ae5fc99788b015e71b33360748b4
packet: key=62fd555efdfbd5b8f50d947332030203b8025ff350dc32f59e489ac577f3bf7b  profile=JORS-SOFTWARE
modality: native-PDF (inline_data base64)
UTC: 2026-07-16T19:17:17.426025Z  |  latency: 16.1s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 16.1, "modality": "native-PDF (inline_data base64)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "PS5ZatftPLqez7IPgvPikQI", "usage": {"candidatesTokenCount": 329, "promptTokenCount": 2707, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 2600}, {"modality": "TEXT", "tokenCount": 107}], "serviceTier": "standard", "thoughtsTokenCount": 1113, "totalTokenCount": 4149}}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
1. [MAJOR] Section 10 (Availability - Archive): The manuscript explicitly states that a persistent archival identifier is not yet available and acknowledges this as a "submission blocker." JORS mandates that the software must be deposited in an approved repository (e.g., Zenodo, Figshare, Software Heritage) and assigned a permanent DOI prior to publication. 
2. [MAJOR] Frontmatter/Overview: The manuscript is missing mandatory JORS template sections, specifically "Paper Author Roles" (using CRediT taxonomy) and a dedicated "Contact" email for the corresponding author. 
3. [MINOR] Section 10 (Availability - Programming language and dependencies): While PyMaster and healpy are mentioned as optional dependencies required for physical workspaces and real integration (Section 8), the specific supported or tested versions of `healpy` should be explicitly listed in the dependencies subsection alongside PyMaster 2.6.
4. [MINOR] Section 8 (Worked Examples): The text references `examples/pymaster_integration.py`, but it would benefit the reader to briefly clarify the exact execution time or computational overhead introduced by the `publish_json` and sidecar-receipt validation steps in these examples compared to a standard NaMaster run.

(3) The central claim that the software provides exact pseudo-$C_\ell$ window inference and fail-closed content validation for reproducible spin-2 analyses is well-supported by the detailed mathematical pre-contraction equations, explicit workflow descriptions, and rigorous test suite documentation.