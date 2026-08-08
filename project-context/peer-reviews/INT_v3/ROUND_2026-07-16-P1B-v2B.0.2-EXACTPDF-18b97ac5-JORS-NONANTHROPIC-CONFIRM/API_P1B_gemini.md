# INT API Review — P1B v2B.0.2 — gemini (gemini-3.1-pro-preview)
paper: P1B  version: v2B.0.2  model: gemini-3.1-pro-preview
provenance: commit=8ad6b00faeb423931b04e4748b57fe532933eba8  pdf=arxiv/paper1b_namaster_proof.pdf  sha256=18b97ac5ffc48d03a60d84822b74562ccd10202430a13054ef2dabf3f267d46c
packet: key=e9f7685aab950494c1c2df19a0d30bc43889672a9011d9d6600fef015329f3e0  profile=JORS-SOFTWARE
modality: native-PDF (inline_data base64)
UTC: 2026-07-16T18:20:08.605316Z  |  latency: 20.3s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 20.3, "modality": "native-PDF (inline_data base64)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "2SBZavqfEf-Gz7IPv_DL0AI", "usage": {"candidatesTokenCount": 325, "promptTokenCount": 2707, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 2600}, {"modality": "TEXT", "tokenCount": 107}], "serviceTier": "standard", "thoughtsTokenCount": 1687, "totalTokenCount": 4719}}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

VERDICT: MAJOR REVISIONS

ISSUES:
1. [MAJOR] Section 10 (Availability) / Archive: The manuscript explicitly states that a persistent archival identifier is missing and acknowledges this as a "submission blocker." JORS mandates that the specific version of the software described must be deposited in an immutable, persistent archive (e.g., Zenodo, Figshare, Software Heritage) and assigned a DOI prior to acceptance.
2. [MAJOR] Section 10 (Availability) / Code repository: The manuscript directs readers to "the namaster-proof package directory" using a hyperlink, but fails to provide the explicit, plain-text URL. JORS requires URLs to be written out explicitly so that the location remains recoverable even if document formatting or hyperlinks are stripped. 
3. [MINOR] Section 10 (Availability) / License: While the MIT license is mentioned inline within the repository text, JORS formatting guidelines typically require a distinct "License" subheading under the Availability section.
4. [MINOR] Sections 7 & 8 (Quality Control & Worked Examples): Because the repository URL is hidden and the archival DOI is missing, reviewers cannot actually access the software to inspect the test suite or run the `examples/pymaster_integration.py` script; providing the links will resolve this issue.

One sentence: The central claim regarding the software's ability to perform exact pseudo-$C_\ell$ window inference and strict content validation is logically supported by the text, but cannot be independently verified by reviewers until the explicit repository URL and persistent archival DOI are provided.