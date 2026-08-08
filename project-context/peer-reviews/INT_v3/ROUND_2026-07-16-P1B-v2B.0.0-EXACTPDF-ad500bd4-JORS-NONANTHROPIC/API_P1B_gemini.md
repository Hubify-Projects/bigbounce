# INT API Review — P1B v2B.0.0 — gemini (gemini-3.1-pro-preview)
paper: P1B  version: v2B.0.0  model: gemini-3.1-pro-preview
provenance: commit=3475392b5ec27be5790580330b40e76f7abd0b5c  pdf=arxiv/paper1b_namaster_proof.pdf  sha256=ad500bd4e8d689628ad3a383e512a1ddd7a1e329b5580e1d41e30637266c75a0
packet: key=40755fdb77414854e749c0f323e77088f9670edd52fca00ae6296fe611b9f82c  profile=JORS-SOFTWARE
modality: native-PDF (inline_data base64)
UTC: 2026-07-16T17:39:55.057441Z  |  latency: 23.1s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 23.1, "modality": "native-PDF (inline_data base64)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "axdZasDnLKXsz7IP0oKIkQQ", "usage": {"candidatesTokenCount": 347, "promptTokenCount": 2187, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 2080}, {"modality": "TEXT", "tokenCount": 107}], "serviceTier": "standard", "thoughtsTokenCount": 1900, "totalTokenCount": 4434}}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

VERDICT: MAJOR REVISIONS

ISSUES:
1. [MAJOR] Section 9 (Availability): The manuscript explicitly states that a "persistent archival DOI... [is] not yet available." JORS strictly requires the described software version to be deposited in an approved, recognized archival repository (e.g., Zenodo, Figshare, Software Heritage) and assigned a DOI prior to acceptance.
2. [MAJOR] Section 9 (Availability): The text references the "BigBounce repository" but fails to provide a URL or hyperlink. Without a link to the source code, reviewers cannot actually evaluate the software, and future readers will be unable to locate it.
3. [MAJOR] Overall Structure: The manuscript does not adhere to the mandatory JORS metapaper template. It is missing required front-matter (Author Affiliations, Contact Email, Keywords) and mandatory JORS section headings, specifically "Quality control", a formally structured "Availability" section (detailing Operating System, Programming Language, Dependencies, Archive, and License), and a "Reuse potential" section.
4. [MINOR] Section 3 (Software Architecture): The paper states that NaMaster is "deliberately not an installation dependency" but requires a user-supplied workspace to function physically. The manuscript needs to explicitly outline the compatible version(s) of PyMaster/NaMaster and the expected mechanism for users to link it to the software in the formal dependencies list.

The central claim that the software calculates exact pseudo-$C_\ell$ window inferences and publishes tamper-evident provenance is theoretically supported by the manuscript's clear mathematical and architectural descriptions, but cannot be empirically verified until the source code repository and archival DOI are provided.