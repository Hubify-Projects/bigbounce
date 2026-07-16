# INT API Review — P1B v2B.0.1 — gemini (gemini-3.1-pro-preview)
paper: P1B  version: v2B.0.1  model: gemini-3.1-pro-preview
provenance: commit=c7b6476794b9ba50c1ad81106d4ca57159ab6ff3  pdf=arxiv/paper1b_namaster_proof.pdf  sha256=5257555381604e6083cb73624f5c2079118c3ea80fe0c3d9f3290bd10dfaf176
packet: key=3c45701ef24cfc5a5e938c9dcc748a216f7dcf5502e52c61dea43a1fd14ec6e4  profile=JORS-SOFTWARE
modality: native-PDF (inline_data base64)
UTC: 2026-07-16T18:03:13.909366Z  |  latency: 21.9s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 21.9, "modality": "native-PDF (inline_data base64)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "4hxZaqWCJ7OIz7IPhejM-A0", "usage": {"candidatesTokenCount": 352, "promptTokenCount": 2707, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 107}, {"modality": "IMAGE", "tokenCount": 2600}], "serviceTier": "standard", "thoughtsTokenCount": 1627, "totalTokenCount": 4686}}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

VERDICT: MAJOR REVISIONS

ISSUES:
1. [MAJOR] Section 10 (Availability / Code repository): The manuscript fails to provide a plain-text URL to the actual software repository. The phrase "available directly at the namaster-proof package directory" must be replaced with or accompanied by a direct URL (e.g., a GitHub or GitLab link) so that reviewers and readers can access, audit, and evaluate the source code. 
2. [MAJOR] Section 10 (Availability / Archive): As explicitly acknowledged by the author in the text, the manuscript lacks a persistent archival identifier. JORS requires the software to be deposited in a recognized immutable archive (e.g., Zenodo, Figshare, Software Heritage) with a cited DOI prior to publication. 
3. [MINOR] Section 8 (Worked Examples): The section describes a "Minimal synthetic operator" and a "Synthetic CMB recovery campaign" conceptually, but it does not provide short code snippets or explicit filenames/paths to the example scripts within the repository, which would greatly aid users in reproducing these exact workflows.
4. [MINOR] Formatting / Structure: The headings slightly deviate from the strict JORS Software Metapaper template. Section 10 should ideally be structured with exact JORS subheadings (e.g., explicit "Software location" containing the Archive and Code repository details) to ensure full compliance with the journal's typesetting requirements.

The central claim that `namaster-proof` provides a mathematically exact window inference and robust content-bound validation layer for reproducible spin-2 analyses is well-supported by the theoretical description and stated quality control measures, pending reviewer access to the source code to verify its execution.