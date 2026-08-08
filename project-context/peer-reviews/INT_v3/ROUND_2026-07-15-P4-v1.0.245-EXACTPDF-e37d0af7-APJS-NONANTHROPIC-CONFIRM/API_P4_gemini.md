# INT API Review — P4 v1.0.245 — gemini (gemini-3.1-pro-preview)
paper: P4  version: v1.0.245  model: gemini-3.1-pro-preview
provenance: commit=54aeaae34614e24ee9d106416b46b7bbb5718128  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=e37d0af72c9d132af6324ddfa80c71d7d78bc14a2f153a7ca7b9a156cc4a2dca
packet: key=dbe7b9f5c0ecea35698757c81cc335d8be36aa578fd598a2002b1187d0657d7f  profile=APJS-CATALOG-METHODS
modality: native-PDF (Files/media upload file_uri)
UTC: 2026-07-15T10:13:21.225719Z  |  latency: 57.3s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 57.3, "modality": "native-PDF (Files/media upload file_uri)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "VF1XaoayN-Cfz7IP7rLIoA4", "usage": {"candidatesTokenCount": 341, "promptTokenCount": 13631, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 13520}, {"modality": "TEXT", "tokenCount": 111}], "serviceTier": "standard", "thoughtsTokenCount": 2041, "totalTokenCount": 16013}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

1. VERDICT: MINOR REVISIONS

2. ISSUES:
[MINOR] 1. Section III.B introduces several specific support acronyms (HC-RI, FS-C, MASTER-AGF) which are used extensively. Table XI in Appendix A summarizes these masks and cuts perfectly; explicitly referencing Table XI at their first introduction in Section III.B, or moving Table XI to the main text, would help the reader track these distinct footprint conventions.
[MINOR] 2. In Table VI and Section IV.D, harmonic-space significances are quoted in $\sigma$ units, though the text accurately notes that the low-$\ell$ permutation null is heavy-tailed relative to a Gaussian. Adding a brief explicit statement clarifying whether the quoted $\sigma$ values in Table VI are computed directly from the sample moments of the null distribution, or mapped from the empirical rank $p$-value via the inverse Gaussian CDF, would resolve any ambiguity in interpreting the harmonic-space statistics. 
[MINOR] 3. The explanation of the test-time equivariant averaging (Eq. 2) and its powerful collapse of the raw 0.79% CW bias is excellent. However, a brief sentence in Section III.D clarifying how the uncertainties on the pseudo-probabilities are handled during this arithmetic averaging, or confirming that the model strictly relies on the post-average argmax without propagating soft score variance, would round out the pipeline description.

3. The central claim of a null observed-label chirality dipole in the DESI Legacy DR8 high-confidence sample is rigorously supported by the robust equivariant averaging methodology, massive catalog scale, and transparent systematics auditing.