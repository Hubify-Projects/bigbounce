# INT API Review — P1B v2B.0.10 — gemini (gemini-3.1-pro-preview)
paper: P1B  version: v2B.0.10  model: gemini-3.1-pro-preview
provenance: commit=8ebefbfd3656141304c58a1207e00461c89b43d1  pdf=arxiv/paper1b_namaster_proof.pdf  sha256=c7883afc5050600998b612d7c8a894c7352b5b3770e442befd2b30f78b502673
packet: key=94578dfa8e9f6dca32577a99b6713b925b0b3354e94457d8fe3f25cc30417466  profile=JORS-SOFTWARE
modality: native-PDF (inline_data base64)
UTC: 2026-07-17T01:22:12.080990Z  |  latency: 17.6s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 17.6, "modality": "native-PDF (inline_data base64)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "xINZaq6rKYHAz7IPjezVUA", "usage": {"candidatesTokenCount": 435, "promptTokenCount": 3227, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 107}, {"modality": "IMAGE", "tokenCount": 3120}], "serviceTier": "standard", "thoughtsTokenCount": 1389, "totalTokenCount": 5051}}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
1. [MAJOR] Section 11 (Availability - Archive): The manuscript explicitly states that a persistent archival identifier is not yet available and acknowledges this as a submission blocker. JORS strictly requires the accepted version of the software to be deposited in an immutable, persistent archive (such as Zenodo, Figshare, or Software Heritage) with a resolvable DOI provided in the manuscript before it can be accepted.
2. [MAJOR] Header & Section 11 (Availability - Code repository): The manuscript uses future placeholder dates ("July 16, 2026" and "2026-07-16"). These must be corrected to reflect the actual release date of the software version being submitted.
3. [MINOR] Section 9 (Author Contributions): The sentence "Correspondence metadata remain author-supplied submission metadata and are not inferred by the software release process" reads as meta-commentary about the submission system. This should be removed and replaced with standard corresponding author contact details (e.g., an email address).
4. [MINOR] Section 8 (Worked Examples): The minimal call sequence contains inline code snippets (e.g., `response = build_rotation_response(workspace, ee, bb)`). For better readability and reproducibility, these should be separated into a formatted, standalone code block.
5. [MINOR] Section 5 (Exact-Window Inference): While the equations for rotation are clear, it would be highly beneficial for reproducibility to explicitly define the ordering of the $i$ and $j$ spectrum indices (e.g., $[EE, EB, BE, BB]$) for the tensor $W_{b\ell}^{ij}$ as it maps directly to the required NaMaster arrays.

(3) The central claim that `namaster-proof` provides a robust verification layer for exact pseudo-$C_\ell$ window inference and content-bound reproducibility in spin-2 analyses is well-supported by the clear mathematical formalization, comprehensive automated test suite, and documented integration examples.